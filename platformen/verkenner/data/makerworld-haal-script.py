import sys,json,subprocess,random,time,concurrent.futures as cf
lo,hi,n,out,seed=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5])
random.seed(seed); ids=random.sample(range(lo,hi),n)
def get(i):
    time.sleep(0.5)
    r=subprocess.run(["curl","-sS","-m","25","-A","Mozilla/5.0","https://makerworld.com/api/v1/design-service/design/%d"%i],capture_output=True,text=True).stdout
    try: d=json.loads(r)
    except Exception: return {"id":i,"err":r[:80]}
    if "createTime" not in d: return {"id":i,"err":r[:80]}
    c=d.get("designCreator") or {}
    g=lambda k,s: (d.get(k) or {}).get(s)
    return {"id":i,"t":d.get("createTime"),"title":d.get("title"),"dl":d.get("downloadCount"),"pr":d.get("printCount"),"like":d.get("likeCount"),
      "col":d.get("collectionCount"),"excl":d.get("isExclusive"),"lic":d.get("license"),"paid":g("paidSetting","isPaid"),"crowd":g("paidSetting","crowdfunding"),
      "boost":g("boostInfo","total"),"boostusers":g("boostInfo","boostDesignUserCnt"),"redeem":g("pointRedeemDetail","price"),"aigc":d.get("isAIGC"),
      "cust":d.get("designCustomizeCount"),"dtype":d.get("designType"),"status":d.get("status"),"makerlab":d.get("customizedByMakerLab"),
      "official":d.get("isOfficial"),"staff":d.get("isStaffPicked"),"uid":c.get("uid"),"handle":c.get("handle"),"cats":[x.get("name") for x in (d.get("categories") or [])]}
with open(out,"w") as f, cf.ThreadPoolExecutor(2) as ex:
    for k,res in enumerate(ex.map(get,ids)):
        f.write(json.dumps(res)+"\n"); f.flush()
