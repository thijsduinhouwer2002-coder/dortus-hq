# Haalt rating-samenvattingen voor alle apps uit autodesk-apps-*.jsonl via de openbare winkel-API.
# Gebruik: python3 -I autodesk-reviews-script.py invoer.jsonl uit.json
import sys, json, time, subprocess
ids=[json.loads(l)['url'].split('/')[-1] for l in open(sys.argv[1])]
uit={}
for i in range(0,len(ids),50):
    q=','.join(ids[i:i+50])
    for poging in range(3):
        r=subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0','https://developer.api.autodesk.com/ngappapi/public/apps/comments/batch-rating-summary?appIds='+q],capture_output=True,text=True)
        try: uit.update(json.loads(r.stdout)['results']); break
        except Exception: time.sleep(3)
    time.sleep(0.7)
json.dump(uit,open(sys.argv[2],'w'))
print(len(ids),len(uit))
