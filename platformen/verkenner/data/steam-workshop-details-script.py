import sys,json,subprocess,time
ids=open(sys.argv[1]).read().split(); out=open(sys.argv[2],'w')
for i in range(0,len(ids),100):
    b=ids[i:i+100]
    args=["curl","-sS","-m","60","https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/","-d",f"itemcount={len(b)}"]
    for k,x in enumerate(b): args+=["-d",f"publishedfileids[{k}]={x}"]
    r=json.loads(subprocess.run(args,capture_output=True,text=True).stdout)
    for d in r["response"]["publishedfiledetails"]:
        out.write(json.dumps({k:d.get(k) for k in ["publishedfileid","result","creator","creator_app_id","consumer_app_id","title","time_created","time_updated","subscriptions","lifetime_subscriptions","favorited","views","tags"]})+"\n")
    time.sleep(0.5)
