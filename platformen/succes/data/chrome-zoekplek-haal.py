# Joris, run 32 (17 nov 2026). Haalt per zoekterm de eerste 10 resultaten van de
# zoekbalk van de Chrome Web Store, met de gegevens die de zoekpagina zelf meestuurt.
# Gebruik: python3 -I chrome-zoekplek-haal.py uit.csv [zoektermen.txt]   (rustig: 1 verzoek per 1,2 s)
import csv, json, re, subprocess, sys, time, urllib.parse
Q = """google calendar bulk delete|delete multiple calendar events|google calendar duplicate events|calendar bulk edit|gmail bulk delete|gmail unsubscribe|save gmail attachments|gmail mail merge|email tracker gmail|gmail templates
youtube speed control|youtube ad skip|youtube transcript|youtube dislike|youtube playlist length|youtube loop|youtube summary|youtube shorts blocker|youtube comments download|youtube volume booster
tab manager|tab suspender|close duplicate tabs|tab rotate|auto refresh page|save all tabs|session manager|tab groups|vertical tabs|new tab dashboard
screenshot full page|screen recorder|pdf merge|pdf editor|word counter|grammar checker|color picker|font identifier|ruler measure|image downloader
dark mode|ad blocker|password manager|vpn|cookie editor|user agent switcher|json formatter|clear cache|proxy switcher|wappalyzer
translate page|dictionary|text to speech|reading mode|highlighter|sticky notes|to do list|pomodoro timer|website blocker|time tracker
linkedin automation|linkedin email finder|instagram downloader|tiktok downloader|twitter video downloader|facebook unfriend|whatsapp web|pinterest downloader|reddit enhancement|discord
chatgpt sidebar|chatgpt export|ai writing assistant|ai summarizer|prompt manager|claude|gemini|perplexity|ai image generator|ai email writer
google sheets|google docs dark mode|google drive download|google meet attendance|google meet transcript|google photos bulk|google keep|google maps scraper|google search results scraper|google forms
amazon price tracker|coupon finder|cashback|price history|shopify spy|etsy seo|ebay sniper|aliexpress|honey alternative|walmart
web scraper|seo meta|broken link checker|page ruler|css viewer|react developer tools|lighthouse|responsive viewer|wayback machine|tampermonkey
volume booster|equalizer|spotify|netflix party|picture in picture|video speed controller|subtitles|twitch|audio recorder|music downloader""".replace('\n','|').split('|')

def haal(url):
    return subprocess.run(['curl','-sS','-L','-m','30','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout

def recs(h):
    m = re.search(r"AF_initDataCallback\(\{key: 'ds:1', hash: '\d+', data:(.*?), sideChannel: \{\}\}\);</script>", h, re.S)
    if not m: return []
    out = []
    def walk(x):
        if isinstance(x, list):
            if len(x) > 17 and isinstance(x[0], str) and re.fullmatch(r'[a-p]{32}', x[0]) and isinstance(x[2], str):
                out.append(x); return
            for y in x: walk(y)
    walk(json.loads(m.group(1))); return out

if len(sys.argv) > 2: Q = open(sys.argv[2]).read().strip().split('\n')
w = csv.writer(open(sys.argv[1], 'w', newline=''))
w.writerow(['zoekterm','plek','id','naam','sterren','beoordelingen','korte_omschrijving','categorie','gebruikers','bijgewerkt','website','veld8','featured','veld13','veld15'])
for q in Q:
    q = q.strip()
    rs = recs(haal('https://chromewebstore.google.com/search/' + urllib.parse.quote(q) + '?hl=en'))
    for i, r in enumerate(rs, 1):
        cat = r[11][0] if isinstance(r[11], list) and r[11] else ''
        ts = r[17][0] if isinstance(r[17], list) and r[17] else ''
        w.writerow([q, i, r[0], r[2], r[3], r[4], (r[6] or '').replace('\n',' ')[:200], cat, r[14], ts, r[7] or '', r[8] or 0, r[9] or 0, r[13] or 0, r[15] or 0])
    print(q, len(rs), flush=True)
    time.sleep(1.2)
