#!/bin/bash
# usage: probe.sh host path...
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
host=$1; shift
for p in "$@"; do
  out=$(curl -sS -L -A "$UA" -o /dev/null -w "%{http_code} %{size_download} %{url_effective} %{content_type}" --max-time 25 "$host$p" 2>&1)
  echo "$p -> $out"
  sleep 1
done
