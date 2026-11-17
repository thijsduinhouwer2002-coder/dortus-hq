import re,subprocess,json,time,os,sys
from datetime import datetime
def versions(slug):
    f=f'v_{slug}.html'
    if not os.path.exists(f):
        subprocess.run(["curl","-sS","-o",f,f"https://extensions.blender.org/add-ons/{slug}/versions/"]); time.sleep(1)
    h=open(f,errors='ignore').read()
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' | ',h))
    t=re.sub(r'(\| )+','| ',t)
    out=[]
    for m in re.finditer(r'\| (\d[\w.\-+]*) \| Compatibility \|.*?\| [\d.]+ [KMG]?B \| ([\d,]+) \| (\w+ \d+)\w\w, (\d{4}) \|',t):
        d=datetime.strptime(m.group(3)+' '+m.group(4),'%B %d %Y').date()
        out.append((m.group(1),int(m.group(2).replace(',','')),str(d)))
    return out
if __name__=='__main__':
    print(versions(sys.argv[1]))
