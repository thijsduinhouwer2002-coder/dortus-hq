# Joris, run 34. Winkelpagina per extensie (id of naam via zoekbalk): gebruikers, beoordelingen, bijgewerkt. Rustig: 1 verzoek per 1,2 s.
import subprocess,re,json,time,sys,html
L=[l.split('|') for l in open(sys.argv[1]).read().strip().split('\n')]
out={}
for pid,ident in L:
  if re.fullmatch(r'[a-p]{32}',ident):
    url='https://chromewebstore.google.com/detail/'+ident+'?hl=en'
  else:
    s=subprocess.run(['curl','-sS','-L','-m','30','-A','Mozilla/5.0','https://chromewebstore.google.com/search/'+ident.replace(' ','%20')+'?hl=en'],capture_output=True,text=True).stdout
    ids=re.findall(r'"([a-p]{32})"',s)
    time.sleep(1.2)
    if not ids: out[pid]={'zoek':ident,'fout':'niet gevonden'};continue
    ident=ids[0];url='https://chromewebstore.google.com/detail/'+ident+'?hl=en'
  h=subprocess.run(['curl','-sS','-L','-m','30','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
  t=re.search(r'<title>(.*?)</title>',h,re.S)
  u=re.search(r'>([\d,\.]+K?\+?) users<',h) or re.search(r'([\d,]+) users',h)
  r=re.search(r'([\d,\.]+K?) ratings',h)
  up=re.search(r'Updated</div><div[^>]*>([^<]+)<',h)
  out[pid]={'id':ident,'naam':html.unescape(t.group(1)) if t else '','gebruikers':u.group(1) if u else '','ratings':r.group(1) if r else '','updated':up.group(1) if up else ''}
  print(pid,out[pid],flush=True)
  time.sleep(1.2)
json.dump(out,open('winkel.json','w'),indent=1)
