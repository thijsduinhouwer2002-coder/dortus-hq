#!/bin/bash
# Vera 16 nov 2026: volgers per Steam-app met curl, 1 verzoek per 6 s; stopt bij de eerste 429.
# Gebruik: bash steam-volgers-curl.sh lijst.json uit.jsonl
for a in $(python3 -c "import json,sys;print(' '.join(json.load(open(sys.argv[1]))))" "$1"); do
  t=$(curl -s -m 20 -w "\nCODE%{http_code}" "https://steamcommunity.com/games/$a/memberslistxml/?xml=1")
  c=$(echo "$t" | grep -oE "CODE[0-9]+" | tail -1 | cut -c5-)
  if [ "$c" = "429" ]; then echo "429 bij $a, gestopt" >&2; exit 0; fi
  n=$(echo "$t" | grep -oE "<memberCount>[0-9]+" | head -1 | cut -c14-)
  echo "{\"appid\": \"$a\", \"volgers\": ${n:-null}, \"fout\": $([ -n "$n" ] && echo null || echo "\"$c\""), \"gemeten\": \"$(date -u '+%Y-%m-%d %H:%M UTC')\"}" >> "$2"
  sleep 6
done
