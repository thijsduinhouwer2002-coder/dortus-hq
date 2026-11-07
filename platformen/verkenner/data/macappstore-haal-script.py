import json,time,urllib.request,urllib.parse,sys
terms=sys.argv[2].split(',');out={}
for t in terms:
    for c in ['us']:
        u='https://itunes.apple.com/search?'+urllib.parse.urlencode({'term':t,'entity':'macSoftware','country':c,'limit':200})
        try: d=json.load(urllib.request.urlopen(u,timeout=60))
        except Exception as e: print('err',t,e); time.sleep(5); continue
        for a in d['results']:
            out[a['trackId']]={k:a.get(k) for k in ['trackName','artistName','sellerName','price','currency','releaseDate','currentVersionReleaseDate','userRatingCount','averageUserRating','primaryGenreName','artistId']}
        time.sleep(3.2)
json.dump(out,open(sys.argv[1],'w'));print(len(out))
