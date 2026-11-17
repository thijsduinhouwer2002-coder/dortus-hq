import json,re,subprocess,time,os,sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
L=[x for x in json.load(open('bext.json'))['data'] if x['type']=='add-on']
def get(x):
    url=x['website'] if 'extensions.blender.org' in (x['website'] or '') else None
    slug=x['id'].replace('_','-')
    f=f"bp/{x['id']}.html"
    if not os.path.exists(f) or os.path.getsize(f)<1000:
        u=x['website'] if url else f"https://extensions.blender.org/add-ons/{slug}/"
        subprocess.run(['curl','-sS','-L','-o',f,u],timeout=30); time.sleep(0.6)
    h=open(f,errors='ignore').read()
    p=re.search(r'<dt>Published</dt>\s*<dd title="\w+ (\d+)\w\w, (\w+) (\d{4})',h)
    d=re.search(r'Downloads\s*</dt>\s*<dd>([\d,]+)</dd>',h)
    pub=str(datetime.strptime(f"{p.group(1)} {p.group(2)} {p.group(3)}",'%d %B %Y').date()) if p else ''
    return (x['id'],x['name'],pub,int(d.group(1).replace(',','')) if d else -1,';'.join(x.get('tags') or []))
with ThreadPoolExecutor(2) as ex: R=list(ex.map(get,L))
import csv
w=csv.writer(open('blender_vroeg.csv','w'));w.writerow(['id','naam','gepubliceerd','downloads','tags']);w.writerows(R)
print(len(R),sum(1 for r in R if r[2]=='' or r[3]<0))
