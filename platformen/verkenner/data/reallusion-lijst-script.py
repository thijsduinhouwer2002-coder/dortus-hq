import json,subprocess,sys,time
out=[];page=1
while True:
    c=json.dumps({"OrderBy":[12],"Range":{"Page":page,"PageSize":500}})
    r=subprocess.run(['curl','-s','-X','POST','-F','Condition='+c,'https://api.reallusion.com/Marketplace20/v1/Content/OpenSearch'],capture_output=True,text=True).stdout
    d=json.loads(r)['ReturnData']['Result']
    if not d: break
    out+=d
    oldest=d[-1]['Image'].split('_')[1][:8] if '_' in d[-1]['Image'] else '?'
    print(page,len(d),oldest,file=sys.stderr)
    if oldest!='?' and oldest<'20260301': break
    page+=1; time.sleep(1.5)
json.dump(out,open(sys.argv[1],'w'))
