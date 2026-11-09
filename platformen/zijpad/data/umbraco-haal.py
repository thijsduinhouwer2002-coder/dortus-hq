import json,sys,time,urllib.request
UA={'User-Agent':'Mozilla/5.0 (compatible; DortusResearch/1.0)'}
ids=[l.rsplit('/',1)[1] for l in open(sys.argv[1]).read().split() if '/package/' in l]
out=open(sys.argv[2],'w')
for i in ids:
  try:
    d=json.load(urllib.request.urlopen(urllib.request.Request('https://api.marketplace.umbraco.com/api/v1.0/packages/'+i,headers=UA),timeout=30))
    out.write(json.dumps({k:d.get(k) for k in ['packageId','title','createdOn','licenseTypes','authors','numberOfNuGetDownloads','licenseUrl','projectUrl']})+'\n')
  except Exception as e: out.write(json.dumps({'packageId':i,'err':str(e)})+'\n')
  time.sleep(0.3)
