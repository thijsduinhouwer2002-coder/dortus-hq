#!/usr/bin/env python3
"""Talen van de demo's uit de nulmeting naast spelers tegelijk (Sem, 16 nov 2026).
Gebruik: python3 talen-demos.py demo-spelers-2026-11-16.csv uit.csv   (appdetails van het hoofdspel, 1 per 0,8 s)"""
import sys, csv, json, re, time, subprocess
rij = list(csv.DictReader(open(sys.argv[1])))
w = csv.writer(open(sys.argv[2], 'w', buffering=1)); w.writerow(['appid','naam','spelers_tegelijk','lijkt_op_hats','aantal_talen','zh_hans','zh_hant','ja','ko','talen'])
for r in rij:
    out = subprocess.run(['curl','-s','-m','20',f"https://store.steampowered.com/api/appdetails?appids={r['appid']}&l=english&filters=basic"],capture_output=True,text=True).stdout
    try:
        d = json.loads(out)[r['appid']]['data']; t = re.sub(r'<[^>]+>','',d.get('supported_languages','')).replace('languages with full audio support','')
    except Exception:
        t = ''
    tl = [x.strip(' *') for x in t.split(',') if x.strip(' *')]
    w.writerow([r['appid'], r['naam'], r['spelers_tegelijk'], r['lijkt_op_hats'], len(tl), int('Simplified Chinese' in t), int('Traditional Chinese' in t), int('Japanese' in t), int('Korean' in t), ';'.join(tl)])
    time.sleep(0.8)
