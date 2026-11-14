import re, json, subprocess, time, sys, os
OUT = '/tmp/yt/games.json'
games = {g['id']: g for g in json.load(open(OUT))} if os.path.exists(OUT) else {}

def parse(html, tag):
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html, re.S)
    if not m:
        return -1
    d = json.loads(m.group(1)); cards = []; dialogs = []
    def walk(o):
        if isinstance(o, dict):
            if 'miniGameCardViewModel' in o: cards.append(o['miniGameCardViewModel'])
            if 'miniAppGameInfoDialogViewModel' in o: dialogs.append(o['miniAppGameInfoDialogViewModel'])
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(d)
    info = {}
    for x in dialogs:
        r = {i.get('label'): i.get('value') for i in x.get('infoRow', [])}
        r['genre'] = x.get('primaryGenre')
        info[x['title']] = r
    n = 0
    for c in cards:
        url = c['onTap']['innertubeCommand']['commandMetadata']['webCommandMetadata']['url']
        gid = url.split('/')[-1]
        acc = c.get('accessibilityText', '')
        mm = re.search(r' - ([\d.,]+ ?\w*) plays', acc)
        g = games.setdefault(gid, {'id': gid, 'title': c['title'], 'seen_in': []})
        g['plays_text'] = mm.group(1) if mm else None
        g.update(info.get(c['title'], {}))
        g['seen_in'].append(tag); n += 1
    return n

for gl in sys.argv[1:]:
    h = subprocess.run(['curl', '-sL', '-m', '40', '-H', 'Accept-Language: en-US',
                        f'https://www.youtube.com/playables?hl=en&gl={gl}'],
                       capture_output=True, text=True).stdout
    print(gl, parse(h, gl), len(games), flush=True)
    json.dump(list(games.values()), open(OUT, 'w'), indent=0)
    time.sleep(3)
