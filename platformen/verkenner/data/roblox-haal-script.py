import json,sys,time,urllib.request,urllib.parse
out=[];tok=None;base="https://apis.roblox.com/toolbox-service/v2/assets:search"
extra=dict(a.split('=',1) for a in sys.argv[2:])
for i in range(40):
    q=dict(searchCategoryType='Plugin',maxPageSize=100,**extra)
    if tok: q['pageToken']=tok
    with urllib.request.urlopen(base+'?'+urllib.parse.urlencode(q),timeout=30) as r: d=json.load(r)
    for a in d.get('creatorStoreAssets',[]):
        p=a['creatorStoreProduct']['purchasePrice']['quantity']
        out.append(dict(id=a['asset']['id'],name=a['asset']['name'],created=a['asset']['createTime'],updated=a['asset']['updateTime'],
          votes=a['voting'].get('voteCount',0),up=a['voting'].get('upVotes',0),price=p['significand']*10**p['exponent'],
          creator=a['creator']['name'],ctype=a['creator']['creator'].split('/')[0],verified=a['creator'].get('verified')))
    tok=d.get('nextPageToken')
    if not tok: break
    time.sleep(0.5)
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(out), d.get('totalResults'))
