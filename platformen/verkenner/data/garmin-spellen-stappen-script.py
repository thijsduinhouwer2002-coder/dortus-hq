# Vera 13 nov 2026: welke Garmin-spellen draaien op echte stappen of beweging (beschrijving), en hoe doen ze het?
# Gebruik: python3 -I garmin-spellen-stappen-script.py garmin-spellen-details-2026-11-13.jsonl
import json,re,sys,datetime
pat=re.compile(r"(your|real[- ]?life|real[- ]world|daily|every|actual|garmin) (daily )?steps|steps (you|that you) (take|walk)|step[- ]powered|steps into|steps (power|fuel|earn|grow|turn)|walk(ing)? (to|more)|by walking|move more|stay active|powered by (your )?(steps|movement|activity)|daily activity|your activity|intensity minutes|move to (earn|grow)|schritte|stappen",re.I)
rows=[]
for l in open(sys.argv[1]):
  x=json.loads(l)
  t=(x['naam'] or '')+' '+(x['besch'] or '')
  if pat.search(t): rows.append(x)
dt=lambda ms: datetime.datetime.fromtimestamp(ms/1000,datetime.UTC).date().isoformat() if ms else '?'
for x in sorted(rows,key=lambda x:(-(x['dl'] or 0),-(x['reviews'] or 0))):
  m=pat.search((x['naam'] or '')+' '+(x['besch'] or ''))
  print(f"{x['dl']}+ | {x['reviews']}r {x['rating']} | ${x['prijs']} pm{x['pm']} | {dt(x['eerst'])} | {x['naam'][:45]} | {x['maker']} | '{m.group(0)}'")
print(len(rows),'stappenspellen')
