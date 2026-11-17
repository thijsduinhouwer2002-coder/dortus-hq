# Haalt per TikTok-account de openbare lijst (yt-dlp, flat, niet ingelogd) en bewaart
# id, datum, duur, views en het geluid (titel van het geluid, maker(s), album).
# Gebruik: python3 tiktok-geluid-haal.py <uitmap> account1 account2 ...
import json, subprocess, sys, os, csv
uit = sys.argv[1]
for h in sys.argv[2:]:
    p = os.path.join(uit, h + '.csv')
    if os.path.exists(p):
        continue
    r = subprocess.run(['yt-dlp', '--flat-playlist', '-J', '--playlist-end', '600',
                        'https://www.tiktok.com/@' + h], capture_output=True, text=True, timeout=900)
    try:
        d = json.loads(r.stdout)
    except Exception:
        print(h, 'mislukt', r.stderr[-200:]); continue
    rows = []
    for e in d.get('entries') or []:
        rows.append([e.get('id'), e.get('timestamp'), e.get('duration'), e.get('view_count'),
                     e.get('track') or '', '|'.join(e.get('artists') or []), e.get('album') or '',
                     e.get('uploader') or '', e.get('channel') or ''])
    with open(p, 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['id','ts','duur','views','track','artists','album','uploader','channel']); w.writerows(rows)
    print(h, len(rows))
