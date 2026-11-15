import re,subprocess,json,time,html,sys
A="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
out=open(sys.argv[1],'w')
for p in range(1,92):
    h=subprocess.run(['curl','-s','-m','30','-A',A,f'https://developers.reddit.com/apps?page={p}'],capture_output=True,text=True).stdout
    for m in re.finditer(r'<devvit-app-card ([^>]*)>',h):
        at=dict(re.findall(r'([a-z-]+)="([^"]*)"',m.group(1)))
        out.write(json.dumps({k:html.unescape(v) for k,v in at.items()})+'\n')
    time.sleep(0.7)
