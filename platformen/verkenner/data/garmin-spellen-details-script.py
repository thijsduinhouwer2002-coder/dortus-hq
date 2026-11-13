# Vera 13 nov 2026: haal de detailpagina (beschrijving, permissies, toestellen) van alle Garmin-spellen (categorie 206)
# Gebruik: python3 -I garmin-spellen-details-script.py garmin-niet-wijzerplaten-2026-11-09.json.gz uit.jsonl
import json,gzip,subprocess,time,sys
d=json.load(gzip.open(sys.argv[1]))
g=[x for x in d if x['cat']=='206']
with open(sys.argv[2],'w') as f:
  for x in g:
    r=subprocess.run(['curl','-s','--max-time','30',f"https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/{x['id']}"],capture_output=True,text=True).stdout
    try: j=json.loads(r)
    except Exception: continue
    loc=j.get('appLocalizations') or []
    en=[l for l in loc if l.get('locale')=='en'] or loc
    f.write(json.dumps({'id':x['id'],'naam':x['naam'],'maker':x['maker'],'dl':j.get('downloadCount'),'reviews':j.get('reviewCount'),'rating':j.get('averageRating'),
      'prijs':(j['pricing']['listPrice']['price'] if j.get('pricing') else 0),'pm':j.get('paymentModel'),'trial':j.get('hasTrialMode'),
      'perm':j.get('permissions'),'ndev':len(j.get('compatibleDeviceTypeIds') or []),'devs':j.get('compatibleDeviceTypeIds'),
      'eerst':j.get('firstApprovalDate'),'besch':(en[0].get('description') if en else '')[:3000]},ensure_ascii=False)+'\n'); f.flush()
    time.sleep(0.25)
