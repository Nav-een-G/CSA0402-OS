#!/usr/bin/env bash
set -euo pipefail
LIMIT="${1:-80}"
if ! [[ "$LIMIT" =~ ^[0-9]+$ ]] || (( LIMIT < 1 || LIMIT > 100 )); then
  echo "Usage: $0 [threshold 1-100]" >&2; exit 2
fi
df -P -h | awk -v limit="$LIMIT" 'NR==1 {print; next} {u=$5; gsub(/%/,"",u); print; if (u+0>=limit) printf "WARNING: %s is at %s%% (limit %s%%)\n",$6,u,limit}'
