#!/bin/bash
# Repeatedly: shard + upload not-yet-archived state data (data/states/*), then free local PDFs that are verified in the
# cloud AND already extracted.  Runs until the state pipeline process has ended, then does one final pass.
cd "$HOME/india-govt-yellow-pages" || exit 1
while true; do
  alive=$(pgrep -f "state_pipeline.py all" | wc -l | tr -d ' ')
  echo "=== $(date '+%H:%M') pipeline alive=$alive" >> data/archive_states_watch.log
  /usr/bin/python3 scripts/archive_shards.py --shard-mb 1500 --only data/states >> data/archive_states_watch.log 2>&1
  /usr/bin/python3 scripts/archive_free.py --apply >> data/archive_states_watch.log 2>&1
  [ "$alive" = "0" ] && break
  sleep 600
done
echo "=== finished $(date '+%H:%M')" >> data/archive_states_watch.log
