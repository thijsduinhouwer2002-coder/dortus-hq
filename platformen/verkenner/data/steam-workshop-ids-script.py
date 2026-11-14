import sys,re,subprocess,time,json
app,pages,out=sys.argv[1],int(sys.argv[2]),sys.argv[3]
ids=[]
for p in range(1,pages+1):
    u=f"https://steamcommunity.com/workshop/browse/?appid={app}&browsesort=accepted&section=mtxitems&numperpage=30&p={p}"
    h=subprocess.run(["curl","-sS","-m","30","-A","Mozilla/5.0",u],capture_output=True,text=True).stdout
    got=[]
    for m in re.findall(r'filedetails/\?id=(\d+)',h):
        if m not in got: got.append(m)
    new=[g for g in got if g not in ids]
    ids+=new
    if not new: break
    time.sleep(0.7)
open(out,'w').write("\n".join(ids))
print(app,len(ids))
