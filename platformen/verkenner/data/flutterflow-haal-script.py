import json, time, urllib.request, urllib.parse, sys
base="https://firestore.googleapis.com/v1/projects/flutterflow-io-6f20/databases/(default)/documents/marketplace_items"
fields=["name","type","status","price_cents","num_times_added","publish_time","create_time","category","marketplace_creator_ref","sample_app_type","last_updated","ratings","price_last_updated"]
out=[]; tok=None
while True:
    q=[("pageSize","300")]+[("mask.fieldPaths",f) for f in fields]
    if tok: q.append(("pageToken",tok))
    url=base+"?"+urllib.parse.urlencode(q)
    d=json.load(urllib.request.urlopen(url,timeout=60))
    for doc in d.get("documents",[]):
        r={"id":doc["name"].split("/")[-1]}
        for k,v in doc.get("fields",{}).items():
            r[k]=list(v.values())[0]
        out.append(r)
    tok=d.get("nextPageToken")
    print(len(out),file=sys.stderr)
    if not tok: break
    time.sleep(1)
json.dump(out,open(sys.argv[1],"w"))
