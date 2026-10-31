#!/bin/bash
# Copy the regenerable, gitignored bulk data of this repo to Dropbox (copy, never sync/delete on the remote).
# Remote: dropbox:india-govt-yellow-pages-archive/<same relative path>.  Restore:
#   rclone copy dropbox:india-govt-yellow-pages-archive/data/signatories/pdf ~/india-govt-yellow-pages/data/signatories/pdf
# Usage: scripts/archive_to_dropbox.sh [copy|verify]
set -u
REPO="$HOME/india-govt-yellow-pages"; REMOTE="dropbox:india-govt-yellow-pages-archive"
MODE="${1:-copy}"; LOG="$REPO/data/archive_to_dropbox.log"
TREES="data/signatories/pdf data/signatories/text data/career/articles data/states/UP/pdf data/states/TN/pdf data/states/KL/pdf data/states/UP/text data/states/TN/text data/states/KL/text ministry_documents/data/sites data/agents/groupA data/agents/groupC data/agents/groupD"
for st in $(ls "$REPO/data/states" 2>/dev/null); do
  case "$st" in ??) for sub in pdf text; do [ -d "$REPO/data/states/$st/$sub" ] && TREES="$TREES data/states/$st/$sub"; done;; esac
done
TREES=$(printf '%s\n' $TREES | sort -u | tr '\n' ' ')
echo "=== $MODE $(date)" >> "$LOG"
for t in $TREES; do
  [ -d "$REPO/$t" ] || continue
  if [ "$MODE" = copy ]; then
    rclone copy "$REPO/$t" "$REMOTE/$t" --exclude '*.part' --transfers 8 --checkers 16 --size-only --retries 5 --low-level-retries 10 --stats-one-line -v --log-file "$LOG" 2>&1 | tail -1
  else
    rclone check "$REPO/$t" "$REMOTE/$t" --size-only --one-way --exclude '*.part' --log-file "$LOG" 2>&1 | tail -1
    echo "$t verify rc=$?" >> "$LOG"
  fi
done
echo "=== done $MODE $(date)" >> "$LOG"
