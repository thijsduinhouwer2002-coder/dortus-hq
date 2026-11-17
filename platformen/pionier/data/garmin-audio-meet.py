# Meet de nieuwe hoek "microfoon en luidspreker" (Toybox.Audio, API 6.0.3, SDK 9.3.0, ±21 okt 2026) in de Connect IQ Store.
# Gebruik: python3 -I garmin-audio-meet.py uit.json   (±1 minuut, alleen lezen, 1 verzoek per seconde)
import json, subprocess, urllib.parse, time, sys, datetime
B = 'https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords'
woorden = ['voice memo', 'voice recorder', 'voice note', 'audio recorder', 'dictation', 'transcribe', 'speech to text',
           'tuner', 'decibel', 'sound meter', 'noise', 'metronome', 'walkie', 'voice assistant', 'audio note', 'recorder']
apps = {}
tot = {}
for w in woorden:
    for s in ['mostRelevant', 'mostRecent']:
        u = f"{B}?keywords={urllib.parse.quote(w)}&startPageIndex=0&pageSize=30&sortType={s}&appType=watch-app"
        r = subprocess.run(['curl', '-s', '-m', '40', u], capture_output=True, text=True).stdout
        try: d = json.loads(r)
        except Exception: print('fout', w, r[:80]); continue
        tot[w] = d.get('totalCount')
        for a in d['apps']:
            loc = [l for l in a.get('appLocalizations', []) if l.get('locale') == 'en'] or a.get('appLocalizations', [{}])
            pr = (a.get('pricing') or {}).get('salePrice') or {}
            apps.setdefault(a['id'], {'naam': loc[0].get('name'), 'woorden': set(), 'prijs': pr.get('price', 0),
                'downloads': a.get('downloadCount'), 'reviews': a.get('reviewCount'), 'score': a.get('averageRating'),
                'apparaten': len(a.get('compatibleDeviceTypeIds', [])), 'bijgewerkt': datetime.datetime.fromtimestamp((a.get('changedDate') or 0)/1000, datetime.timezone.utc).date().isoformat(),
                'rechten': a.get('permissions', []), 'id': a['id']})['woorden'].add(w)
        time.sleep(1.0)
for v in apps.values(): v['woorden'] = sorted(v['woorden'])
json.dump({'gemeten': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='minutes'), 'totaal_per_woord': tot, 'apps': apps},
          open(sys.argv[1], 'w'), indent=1, ensure_ascii=False, default=str)
print(len(apps), 'apps'); print(tot)
rechten = {}
for v in apps.values():
    for r in v['rechten']: rechten[r] = rechten.get(r, 0) + 1
print(rechten)
