# Vera 8 nov 2026: haalt per betaalde/freemium plugin de eerste publicatiedatum (cdate), downloads en maker.
import csv,json,sys,time,subprocess,concurrent.futures as cf
src=sys.argv[1]; out=sys.argv[2]
ids=[r['id'] for r in csv.DictReader(open(src),delimiter='\t')]
def get(i):
    for a in range(3):
        try:
            r=subprocess.run(['curl','-s','--max-time','20',f'https://plugins.jetbrains.com/api/plugins/{i}'],capture_output=True,text=True)
            d=json.loads(r.stdout)
            v=d.get('vendor') or {}
            return {'id':i,'naam':d.get('name'),'model':d.get('pricingModel'),'cdate':d.get('cdate'),'downloads':d.get('downloads'),
                    'maker':v.get('publicName') or v.get('name'),'maker_type':v.get('type'),'verified':v.get('isVerified'),'land':v.get('countryCode')}
        except Exception: time.sleep(2)
    return {'id':i,'fout':1}
with cf.ThreadPoolExecutor(4) as ex, open(out,'w') as f:
    for res in ex.map(get,ids):
        f.write(json.dumps(res)+'\n')
