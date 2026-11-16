import re,html,sys,subprocess,csv,json
w=csv.writer(sys.stdout)
for u in open(sys.argv[1]).read().split():
    try:
        t=subprocess.run(['curl','-s','-m','25','-L','-A','Mozilla/5.0',u],capture_output=True).stdout.decode('utf8','ignore')
    except Exception as e: t=''
    def m(p):
        r=re.search(p,t,re.S|re.I); return html.unescape(r.group(1)).strip() if r else ''
    date=m(r'"datePublished"\s*:\s*"([^"]+)"') or m(r'article:published_time"\s+content="([^"]+)"') or m(r'content="([^"]+)"\s+property="article:published_time"')
    auth=m(r'"author"\s*:\s*\[?\s*\{[^}]*?"name"\s*:\s*"([^"]+)"') or m(r'name="author"\s+content="([^"]+)"')
    title=m(r'<title>(.*?)</title>')[:110]
    w.writerow([date[:10],auth,len(t),title,u])
