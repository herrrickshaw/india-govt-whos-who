#!/bin/bash
# Keeps this 8 GB Mac from running out of disk or memory while the long jobs run.
# Every 30 s it reads free disk and free-memory %, and
#   * disk free < PAUSE_DISK_GB  -> frees archived+extracted PDFs, then PAUSES (SIGSTOP) the state pipeline's fetch/extract
#     process; resumes it at > RESUME_DISK_GB.  The archive uploader keeps running (it is what frees space).
#   * memory free < PAUSE_MEM_PCT -> pauses the pipeline (and its OCR children); resumes at > RESUME_MEM_PCT.
#   * disk free < EMERGENCY_DISK_GB -> also pauses the Dropbox->S3 copy and any other rclone/tesseract work (never the uploader).
# It only pauses and resumes; it never deletes anything except via archive_free.py (archived + extracted PDFs only).
# Usage: scripts/resource_guard.sh [--once]      Log: data/resource_guard.log
PAUSE_DISK_GB=${PAUSE_DISK_GB:-15}; RESUME_DISK_GB=${RESUME_DISK_GB:-22}; EMERGENCY_DISK_GB=${EMERGENCY_DISK_GB:-7}
PAUSE_MEM_PCT=${PAUSE_MEM_PCT:-12}; RESUME_MEM_PCT=${RESUME_MEM_PCT:-25}
cd "$HOME/india-govt-yellow-pages" || exit 1
LOG=data/resource_guard.log; paused=0; emergency=0
log() { echo "$(date '+%m-%d %H:%M:%S') $*" >> "$LOG"; }
pipeline_pids() {   # Python processes (by executable name) whose arguments mention the pipeline script - never a shell that merely contains the text
  local out="" pid
  for pid in $(ps -axo pid=,comm= | awk '$2 ~ /[Pp]ython/ {print $1}'); do
    ps -o args= -p "$pid" 2>/dev/null | grep -Eq "${PIPE_PATTERN:-state_pipeline[.]py}" && out="$out $pid"
  done; echo "$out"; }
while true; do
  read_disk() { if [ -n "$MOCK_DISK_FILE" ] && [ -f "$MOCK_DISK_FILE" ]; then cat "$MOCK_DISK_FILE"; else df -k / | awk 'NR==2{printf "%d", $4/1048576}'; fi; }   # MOCK_DISK_FILE is a test hook only
  disk_gb=$(read_disk)
  mem_pct=$(memory_pressure -Q 2>/dev/null | awk '/free percentage/{gsub("%","",$NF); print $NF}'); mem_pct=${mem_pct:-50}
  if [ "$disk_gb" -lt "$PAUSE_DISK_GB" ]; then /usr/bin/python3 scripts/archive_free.py --apply >> "$LOG" 2>&1; disk_gb=$(read_disk); fi
  want_pause=0
  [ "$disk_gb" -lt "$PAUSE_DISK_GB" ] && want_pause=1
  [ "$mem_pct" -lt "$PAUSE_MEM_PCT" ] && want_pause=1
  if [ "$paused" = 1 ]; then       # hysteresis: resume only when both are comfortable
    [ "$disk_gb" -lt "$RESUME_DISK_GB" ] && want_pause=1
    [ "$mem_pct" -lt "$RESUME_MEM_PCT" ] && want_pause=1
  fi
  if [ "$want_pause" = 1 ] && [ "$paused" = 0 ]; then
    for p in $(pipeline_pids); do kill -STOP "$p" 2>/dev/null; done; paused=1
    log "PAUSED pipeline: disk=${disk_gb}GB mem_free=${mem_pct}%"
  elif [ "$want_pause" = 0 ] && [ "$paused" = 1 ]; then
    for p in $(pipeline_pids); do kill -CONT "$p" 2>/dev/null; done; paused=0
    log "RESUMED pipeline: disk=${disk_gb}GB mem_free=${mem_pct}%"
  fi
  if [ "$disk_gb" -lt "$EMERGENCY_DISK_GB" ] && [ "$emergency" = 0 ]; then
    for p in $(pgrep -x rclone ; pgrep -x tesseract ; pgrep -x pdftoppm); do kill -STOP "$p" 2>/dev/null; done; emergency=1
    log "EMERGENCY: disk=${disk_gb}GB - paused S3 copy and OCR processes"
  elif [ "$disk_gb" -ge "$PAUSE_DISK_GB" ] && [ "$emergency" = 1 ]; then
    for p in $(pgrep -x rclone ; pgrep -x tesseract ; pgrep -x pdftoppm); do kill -CONT "$p" 2>/dev/null; done; emergency=0
    log "EMERGENCY cleared: disk=${disk_gb}GB"
  fi
  [ "$1" = "--once" ] && { echo "disk_free=${disk_gb}GB mem_free=${mem_pct}% paused=$paused"; break; }
  sleep ${GUARD_INTERVAL:-30}
done
