#!/usr/bin/env python3
"""Meet de pluginlijst van Filament (open API filamentphp.com/api/plugins) en de Packagist-downloads per plugin.
Gebruik: python3 filament-plugins-meet.py <uitvoer.json>
Haalt per GitHub-repo composer.json op en dan de Packagist-tellers (totaal, maand, dag). Rustig: 0,2 s tussen verzoeken."""
import json, os, re, subprocess, sys, time, urllib.request
uit = sys.argv[1] if len(sys.argv) > 1 else 'filament-plugins.json'
def get(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'dortus-meting/1.0'})
        return urllib.request.urlopen(req, timeout=30).read().decode()
    except Exception as e:
        return None
# Open API van de pluginlijst (15 per pagina)
plugins = []
eerste = json.loads(get('https://filamentphp.com/api/plugins?page=1'))
last = eerste['meta']['last_page']
plugins += eerste['data']
for pg in range(2, last + 1):
    t = get(f'https://filamentphp.com/api/plugins?page={pg}')
    if t:
        plugins += json.loads(t)['data']
    time.sleep(0.3)
for p in plugins:
    p.pop('author', None)
print('lijst', len(plugins), file=sys.stderr)
def verrijk(p):
    repo = p.get('github_repository')
    p['composer'] = None
    if repo:
        c = get(f'https://raw.githubusercontent.com/{repo}/HEAD/composer.json')
        if c:
            try:
                p['composer'] = json.loads(c).get('name')
            except Exception:
                pass
    if p['composer']:
        s = get(f"https://packagist.org/packages/{p['composer']}/stats.json")
        if s:
            try:
                p['downloads'] = json.loads(s)['downloads']
            except Exception:
                pass
    time.sleep(0.3)
    return p
# 4 tegelijk, elk met een pauze: rustig voor GitHub en Packagist
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(4) as ex:
    for i, _ in enumerate(ex.map(verrijk, plugins)):
        if i % 100 == 0:
            print(i, len(plugins), file=sys.stderr)
json.dump(plugins, open(uit, 'w'), indent=1)
print('klaar', len(plugins), uit)
