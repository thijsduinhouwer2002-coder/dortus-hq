import re,json,subprocess,sys
slug=sys.argv[1]
h=subprocess.run(['curl','-sL','--max-time','20','https://www.crazygames.com/game/'+slug],capture_output=True,text=True).stdout
m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
try:
    g=json.loads(m.group(1))['props']['pageProps']['game']
    keep={k:g.get(k) for k in ['id','name','slug','rating','upvotes','downvotes','developerId','addedOn','basicLaunchOn','technology','hasIap','isOriginal','isSelfHosted']}
    keep['cat']=(g.get('category') or {}).get('name')
    print(json.dumps(keep))
except Exception as e:
    print(json.dumps({'slug':slug,'err':str(e)}))
