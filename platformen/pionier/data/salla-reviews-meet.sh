#!/bin/bash
# Noor, 9 nov 2026. Telt reviews per maand voor een Salla-app via de openbare API (curl, rustig, alleen lezen).
# Gebruik: bash salla-reviews-meet.sh <app_id> [stopmaand JJJJ-MM, standaard 2024-06]
# Google Analytics (165566897) installeert bijna elke nieuwe winkel: ruwe maat voor nieuwe actieve winkels per maand.
app=$1; stop=${2:-2024-06}; p=1; tmp=$(mktemp)
while :; do
  curl -s -m 30 "https://api.salla.dev/marketplace/v2/apps/$app/reviews?page=$p" -o "$tmp" || break
  out=$(python3 -I -c "import json,sys;d=json.load(open(sys.argv[1]));r=d.get('data',[]);[print('R',x['date'][:7]) for x in r];print('N',(d.get('cursor') or {}).get('next') or '')" "$tmp") || break
  echo "$out" | grep '^R'
  last=$(echo "$out" | grep '^R' | tail -1 | cut -d' ' -f2); nxt=$(echo "$out" | grep '^N' | cut -d' ' -f2)
  [ -z "$nxt" ] && break; [[ "$last" < "$stop" ]] && break
  p=$nxt; sleep 0.3
done | cut -d' ' -f2 | sort | uniq -c
rm -f "$tmp"
