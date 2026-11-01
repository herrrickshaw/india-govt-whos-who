#!/usr/bin/env python3
"""Prepare and (optionally) launch the cloud markdown conversion.

  manifest : builds manifest.json for every PDF shard already present in s3://BUCKET/in/ and not yet converted (out/), with
             presigned GET/PUT URLs (7 days), per-tree metadata JSON and a code bundle, all stored in the private bucket.
  aws      : launches a self-terminating Ubuntu spot instance whose user-data installs poppler + tesseract (+ Indic language packs),
             pulls the code and manifest by presigned URL, runs scripts/cloud_md_worker.py, uploads its log, and shuts down.
             The instance holds NO AWS credentials — only time-limited URLs for exactly the files it needs.
  colab    : writes out/colab_cell.txt, one cell to paste/run in a Colab notebook (same worker, same URLs, no credentials).
  status   : prints progress from the status object the worker keeps updating.

Usage:  scripts/cloud_md_launch.py manifest [--workers 16] | aws [--type c7g.4xlarge] | colab | status
"""
import argparse, io, json, os, subprocess, sys, tarfile, time
from pathlib import Path

import boto3
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
BUCKET = "yp-md-120354379043"; REGION = "us-east-1"; DAYS = 7
s3 = boto3.client("s3", region_name=REGION)
sys.path.insert(0, str(REPO / "scripts"))

OCR_PACKS = "eng hin tam tel kan mal guj ben ori pan mar asm urd nep"
CENTRE_LANG = "eng+hin"


def presign(method, key, ctype=None):
    params = {"Bucket": BUCKET, "Key": key}
    if ctype:
        params["ContentType"] = ctype
    return s3.generate_presigned_url(method, Params=params, ExpiresIn=DAYS * 86400)


def lang_for(tree):
    p = tree.split("__")
    if p[:2] == ["data", "states"] and len(p) >= 3:
        from state_pipeline import STATE_LANG
        return STATE_LANG.get(p[2], ("eng",))[0]
    return CENTRE_LANG


def list_keys(prefix):
    keys, tok = [], None
    while True:
        r = s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix, **({"ContinuationToken": tok} if tok else {}))
        keys += [(o["Key"], o["Size"]) for o in r.get("Contents", [])]
        if not r.get("IsTruncated"):
            return keys
        tok = r["NextContinuationToken"]


def tree_meta_json(tree):
    from shards_to_md import tree_meta
    return tree_meta(tree)


def build_manifest(workers, final=None):
    done = {k for k, _ in list_keys("out/")}
    jobs = []
    for key, size in sorted(list_keys("in/")):
        parts = key.split("/")
        if len(parts) != 3 or not parts[2].endswith(".zip") or size < 1000:
            continue
        tree, shard = parts[1], parts[2]
        if not tree.endswith("__pdf"):
            continue
        out_key = f"out/{tree}/{shard.replace('.zip', '.md.zip')}"
        if out_key in done:
            continue
        jobs.append(dict(tree=tree, shard=shard, size=size, in_key=key, out_key=out_key))
    metas = {}
    for tree in sorted({j["tree"] for j in jobs}):
        mk = f"meta/{tree}.json"; body = json.dumps(tree_meta_json(tree)).encode()
        s3.put_object(Bucket=BUCKET, Key=mk, Body=body, ServerSideEncryption="AES256"); metas[tree] = presign("get_object", mk)
    for j in jobs:
        j.update(get_url=presign("get_object", j.pop("in_key")), put_url=presign("put_object", j["out_key"]),
                 meta_url=metas[j["tree"]], ocr_lang=lang_for(j["tree"]), ocr_pages=10)
        j.pop("out_key")
    s3.put_object(Bucket=BUCKET, Key="status/status.json", Body=b"{}", ServerSideEncryption="AES256")
    man = dict(jobs=jobs, workers=workers, status_put_url=presign("put_object", "status/status.json", "application/json"))
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        for f in ("shards_to_md.py", "cloud_md_worker.py"):
            t.add(REPO / "scripts" / f, arcname=f)
    s3.put_object(Bucket=BUCKET, Key="code/code.tgz", Body=buf.getvalue(), ServerSideEncryption="AES256")
    mkey = "manifests/next.json" if final is not None else f"manifests/manifest-{time.strftime('%Y%m%d-%H%M%S')}.json"
    if final is not None:
        man["final"] = bool(final)
    s3.put_object(Bucket=BUCKET, Key=mkey, Body=json.dumps(man).encode(), ServerSideEncryption="AES256")
    out = REPO / "data/cloud_md"; out.mkdir(exist_ok=True)
    info = dict(manifest_key=mkey, manifest_url=presign("get_object", mkey), next_url=presign("get_object", "manifests/next.json"), code_url=presign("get_object", "code/code.tgz"),
                log_put_url=presign("put_object", f"logs/worker-{time.strftime('%Y%m%d-%H%M%S')}.log", "text/plain"), jobs=len(jobs),
                gib=round(sum(j["size"] for j in jobs) / 2**30, 1))
    (out / "launch_info.json").write_text(json.dumps(info))
    print(f"{time.strftime('%H:%M:%S')} manifest: {len(jobs)} shards ({info['gib']} GiB) not yet converted, {len(done)} already done -> s3://{BUCKET}/{mkey}")
    return info


def user_data(info):
    return f"""#!/bin/bash
exec > /var/log/yp.log 2>&1
set -x
export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y poppler-utils curl python3 tesseract-ocr {' '.join('tesseract-ocr-' + p for p in OCR_PACKS.split() if p != 'eng')}
shutdown -h +840        # hard stop after 14 h whatever happens (instance is set to terminate on shutdown)
mkdir -p /opt/yp && cd /opt/yp
curl -fsSL "{info['code_url']}" | tar xz
curl -fsSL "{info['manifest_url']}" -o manifest.json
YP_WORK=/mnt/work; mkdir -p $YP_WORK; export YP_WORK
python3 cloud_md_worker.py --manifest "{info["next_url"]}" --workers 8 || true
curl -fsS -X PUT -H "Content-Type: text/plain" -T /var/log/yp.log "{info['log_put_url']}" || true
shutdown -h now
"""


def launch(itype):
    info = json.loads((REPO / "data/cloud_md/launch_info.json").read_text())
    ec2 = boto3.client("ec2", region_name=REGION)
    ami = ec2.describe_images(Owners=["099720109477"], Filters=[{"Name": "name", "Values": ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-arm64-server-*"]}, {"Name": "state", "Values": ["available"]}])["Images"]
    ami = sorted(ami, key=lambda i: i["CreationDate"])[-1]["ImageId"]
    kw = dict(ImageId=ami, InstanceType=itype, MinCount=1, MaxCount=1, UserData=user_data(info), InstanceInitiatedShutdownBehavior="terminate",
              BlockDeviceMappings=[{"DeviceName": "/dev/sda1", "Ebs": {"VolumeSize": 60, "VolumeType": "gp3", "DeleteOnTermination": True}}],
              TagSpecifications=[{"ResourceType": "instance", "Tags": [{"Key": "Name", "Value": "yp-md-worker"}, {"Key": "project", "Value": "india-govt-yellow-pages"}]}],
              MetadataOptions={"HttpTokens": "required"})
    try:   # this account has no spot allowance and an 8-vCPU on-demand cap; spot is tried first and falls back
        r = ec2.run_instances(InstanceMarketOptions={"MarketType": "spot", "SpotOptions": {"SpotInstanceType": "one-time", "InstanceInterruptionBehavior": "terminate"}}, **kw)
        kind = "spot"
    except Exception as e:
        print("spot launch failed:", str(e)[:200], "-> on-demand")
        r = ec2.run_instances(**kw); kind = "on-demand"
    iid = r["Instances"][0]["InstanceId"]
    (REPO / "data/cloud_md/instance.txt").write_text(iid)
    print(f"launched {kind} {itype}: {iid} ({ami})")


def colab(info):
    code = f"""# Colab cell: converts the PDF shards to markdown with CPU OCR; no credentials involved.
!apt-get -qq install -y poppler-utils tesseract-ocr {' '.join('tesseract-ocr-' + p for p in OCR_PACKS.split() if p != 'eng')} > /dev/null
!mkdir -p /content/yp && cd /content/yp && curl -fsSL "{info['code_url']}" | tar xz && curl -fsSL "{info['manifest_url']}" -o manifest.json
!cd /content/yp && YP_WORK=/content/work python3 cloud_md_worker.py --manifest manifest.json --workers 2
"""
    (REPO / "data/cloud_md/colab_cell.txt").write_text(code)
    print("wrote data/cloud_md/colab_cell.txt")


def status():
    try:
        d = json.loads(s3.get_object(Bucket=BUCKET, Key="status/status.json")["Body"].read())
    except Exception as e:
        print("no status yet", e); return
    print({k: v for k, v in d.items() if k != "shards"}, "| last shards:", d.get("shards", [])[-2:])
    outs = list_keys("out/"); print(f"out/: {len(outs)} markdown shards, {sum(s for _, s in outs)/2**20:.0f} MiB")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cmd"); ap.add_argument("--workers", type=int, default=8); ap.add_argument("--type", default="c7g.2xlarge")
    a = ap.parse_args()
    if a.cmd == "manifest":
        build_manifest(a.workers)
    elif a.cmd == "feeder":     # keep manifests/next.json current while the Dropbox->S3 copy is still running
        expected = len([l for l in subprocess.run(["rclone", "lsf", "dropbox:india-govt-yellow-pages-archive/zips", "-R", "--files-only", "--include", "*__pdf/**"], capture_output=True, text=True).stdout.split() if l.endswith(".zip")])
        print("expected shards:", expected, flush=True)
        while True:
            present = len([k for k, sz in list_keys("in/") if k.endswith(".zip")])
            copying = subprocess.run(["pgrep", "-f", "rclone copy dropbox"], capture_output=True).returncode == 0
            final = (present >= expected) and not copying
            build_manifest(a.workers, final=final)
            if final:
                print("final manifest written", flush=True); break
            time.sleep(300)
    elif a.cmd == "aws":
        launch(a.type)
    elif a.cmd == "colab":
        colab(json.loads((REPO / "data/cloud_md/launch_info.json").read_text()))
    elif a.cmd == "status":
        status()
