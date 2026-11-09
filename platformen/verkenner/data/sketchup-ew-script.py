# Haalt alle extensies uit de Extension Warehouse (openbare winkel-API, zonder inlog) en schrijft jsonl.
# Gebruik: python3 sketchup-ew-script.py uit.jsonl
import json,sys,time,urllib.request
U="https://extensions.sketchup.com/warehouse/v1.0/packages?count=1000&offset={}&recordEvent=false&showAttributes=true&showBinaryMetadata=true&showHidden=false&contentType=sew"
out=open(sys.argv[1],'w');o=0
while True:
    d=json.load(urllib.request.urlopen(U.format(o),timeout=120));e=d['entries']
    for x in e:
        v=x['attributes'].get('--sewVersionInfo',{});g=lambda k:(v.get(k) or {}).get('value')
        ei=x['attributes'].get('extensionInfo',{})
        out.write(json.dumps(dict(id=x['id'],title=x['title'],maker=(x.get('creator') or {}).get('displayName'),
          create=x['createTime'],modify=x['modifyTime'],downloads=x['downloads'],views=x['views'],reviews=x['reviewCount'],
          paid=(ei.get('isPaid') or {}).get('value'),price=g('price'),listing=g('isListing'),trial=g('hasTrial'),
          trialLength=g('trialLength'),versions=g('sketchupVersions'),categories=g('categories')))+"\n")
    o+=len(e)
    if not e or o>=d['total']: break
    time.sleep(3)
print(o)
