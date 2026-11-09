#!/usr/bin/env python3
"""Telt de Connected Apps in Gemini (officiele hulptabel) en kijkt of de docs nog 'U.S.' of 'preview' noemen.
Gebruik: python3 -I google-connected-apps-meet.py [uitvoer.json]"""
import sys, re, json, html, subprocess, datetime
def get(u):
    return subprocess.run(['curl','-sL','--max-time','40',u],capture_output=True,text=True).stdout
t = get('https://support.google.com/gemini/table/17434654?hl=en')
rows = re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S)
apps = []
for r in rows:
    cells = [re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',c))).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
    if cells and cells[0]: apps.append(cells)
home = get('https://developers.google.com/connected-apps')
out = {'datum': datetime.date.today().isoformat(), 'rijen': len(apps), 'apps': apps,
       'docs_noemt_preview': 'preview' in home.lower(), 'docs_noemt_US': bool(re.search(r'U\.S\.|United States', home))}
print('rijen in de tabel:', len(apps), '| preview in docs:', out['docs_noemt_preview'], '| VS in docs:', out['docs_noemt_US'])
for a in apps[:100]: print(' -', ' | '.join(a)[:120])
if len(sys.argv) > 1: json.dump(out, open(sys.argv[1],'w'), ensure_ascii=False, indent=1)
