import sys,re,json,subprocess,time
A=[json.loads(l) for l in open(sys.argv[1])]
out=open(sys.argv[2],'w')
for a in A:
    if a['downloads'] is None: continue
    h=subprocess.run(['curl','-sL','-m','25','-A','Mozilla/5.0','https://www.overwolf.com/app/'+a['slug']],capture_output=True,text=True).stdout.replace('\\"','"')
    ids=[int(x) for x in re.findall(r'"comment_ID":(\d+)',h)]
    ds=sorted(set(re.findall(r'"editedAt":"(\d{4}-\d\d-\d\d)',h)))
    a['comment_ids']=sorted(set(ids)); a['datums']=ds
    out.write(json.dumps(a,ensure_ascii=False)+'\n'); out.flush(); time.sleep(0.3)
