# Haalt per TikTok-account de openbare lijst (yt-dlp, flat) en bewaart alleen
# id, datum, duur, views, likes, saves, reacties en het begin van het onderschrift.
# Gebruik: python3 tiktok-lengte-haal.py <uitmap> account1 account2 ...
import json, subprocess, sys, os, csv
uit = sys.argv[1]
for h in sys.argv[2:]:
    p = os.path.join(uit, h + '.csv')
    if os.path.exists(p):
        continue
    r = subprocess.run(['yt-dlp', '--flat-playlist', '-J', '--playlist-end', '600',
                        'https://www.tiktok.com/@' + h], capture_output=True, text=True, timeout=600)
    try:
        d = json.loads(r.stdout)
    except Exception:
        print(h, 'mislukt', r.stderr[-200:]); continue
    rows = []
    for e in d.get('entries') or []:
        rows.append([e.get('id'), e.get('timestamp'), e.get('duration'), e.get('view_count'),
                     e.get('like_count'), e.get('save_count'), e.get('comment_count'),
                     (e.get('description') or '').replace('\n', ' ')[:140]])
    with open(p, 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['id','ts','duur','views','likes','saves','reacties','tekst']); w.writerows(rows)
    print(h, len(rows))
