import json,sys,statistics as st,collections
d=json.load(open(sys.argv[1]))
# alleen echte stream-producten: naam bevat een streamwoord
W=["overlay","alert","stream","twitch","obs","widget","stinger","panel","vtuber","kick","emote"]
ps=[p for p in d.values() if any(w in p["name"].lower() for w in W)]
paid=[p for p in ps if p["price"]>0 and not p["pwyw"]]
print("gevonden",len(d),"streamproducten",len(ps),"betaald",len(paid),"makers",len({p["seller"] for p in ps}))
r=[p["ratings"] for p in paid]
print("betaald ratings mediaan",st.median(r),"1+",round(100*sum(x>=1 for x in r)/len(r),1),"10+",round(100*sum(x>=10 for x in r)/len(r),1),"20+",round(100*sum(x>=20 for x in r)/len(r),1),"50+",round(100*sum(x>=50 for x in r)/len(r),1))
print("prijs mediaan $",st.median([p["price"] for p in paid])/100)
s=collections.Counter()
for p in paid: s[p["seller"]]+=p["ratings"]
print("top makers op ratings:",s.most_common(10))
for p in sorted(paid,key=lambda x:-x["ratings"])[:12]: print(p["ratings"],p["price"]/100,p["seller"][:20],"|",p["name"][:60])
