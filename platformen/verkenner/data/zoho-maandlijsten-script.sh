#!/bin/sh
# Haalt de maandlijsten "What's new on Zoho Marketplace in <maand> <jaar>" (help.zoho.com) op
# en zet alle app-links met hun maand in nieuw-maand.json. Daarna: python3 zoho-nieuw-haal-script.py nieuw-ids.txt uit.json
mkdir -p maand
for y in 2025 2026; do for m in january february march april may june july august september october november december; do
  curl -sL --max-time 30 "https://help.zoho.com/portal/en/kb/zoho-marketplace/new-on-marketplace/articles/what-s-new-on-zoho-marketplace-in-$m-$y" -o maand/$y-$m.html
done; done
python3 - <<'PY'
import re,glob,json
rows={}
for f in sorted(glob.glob('maand/*.html')):
    mon=f.split('/')[1][:-5]
    for m in re.findall(r'marketplace\.zoho\.[a-z.]+/app/([a-z]+/[a-z0-9-]+)',open(f).read()): rows.setdefault(m,mon)
open('nieuw-ids.txt','w').write('\n'.join(rows)); json.dump(rows,open('nieuw-maand.json','w')); print(len(rows))
PY
