import json,urllib.parse,subprocess,time,sys
terms=["safari extension","for safari","safari","safari web extension","safari dark mode","safari ad blocker","safari tab","safari youtube","safari translate","safari reader","safari ai","safari productivity","safari privacy","safari shopping","safari video speed","safari userscript","safari css","safari screenshot","safari password","safari bookmarks","safari new tab","safari focus","safari summarize","safari grammar","safari coupon","safari pip","safari autoplay","safari cookie","safari redirect","safari history","safari notes","safari theme","safari download","safari github","safari twitter","safari reddit","safari instagram","safari email","safari pdf","safari vpn","web extension","browser extension"]
seen={}
for ent in [sys.argv[1]]:
  for c in sys.argv[2].split(","):
    for t in terms:
      u=f"https://itunes.apple.com/search?term={urllib.parse.quote(t)}&entity={ent}&country={c}&limit=200"
      out=subprocess.run(["curl","-s","-m","20",u],capture_output=True,text=True).stdout
      try: r=json.loads(out)["results"]
      except Exception: time.sleep(3); continue
      for x in r:
        k=(x["trackId"]);d=x.get("description","")
        if "safari" not in d.lower() or "extension" not in d.lower(): continue
        e=seen.setdefault(k,dict(id=k,name=x["trackName"],seller=x.get("sellerName"),price=x.get("price"),release=x["releaseDate"][:10],kind=x.get("kind"),genres=x.get("genres"),ratings={},iap=None,cur=x.get("currency")))
        e["ratings"][c]=max(e["ratings"].get(c,0),x.get("userRatingCount",0))
      time.sleep(0.4)
    json.dump(list(seen.values()),open(sys.argv[3],"w"))
  print(ent,len(seen),file=sys.stderr)
json.dump(list(seen.values()),open(sys.argv[3],"w"))
