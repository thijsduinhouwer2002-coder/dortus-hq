#!/bin/bash
# per soort: totaal en groter dan 2 kB
for s in "$@"; do
  if [[ $s == \*.* ]]; then q="extension:${s#*.}"; else q="filename:$s"; fi
  a=$(gh api -X GET search/code -f q="$q" --jq .total_count 2>/dev/null); sleep 6.5
  b=$(gh api -X GET search/code -f q="$q size:>2000" --jq .total_count 2>/dev/null); sleep 6.5
  echo -e "$s\t$a\t$b"
done
