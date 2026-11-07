# Leest per app-pagina (openbare HTML) de 5 nieuwste reviews en het prijsplan. Voor apps met 1 tot 5 reviews is de oudste getoonde review de eerste.
# Gebruik: python3 wix-reviewdata-script.py slugs.txt uit.jsonl
import re,base64,json,sys,subprocess,time
from concurrent.futures import ThreadPoolExecutor
def one(slug):
    s=subprocess.run(['curl','-s','-A','Mozilla/5.0','https://www.wix.com/app-market/'+slug],capture_output=True,text=True).stdout
    for k,v in re.findall(r"window\.(__\w+)\s*=\s*JSON\.parse\(__decodeBase64\('([A-Za-z0-9+/=]+)'\)\)",s):
        if k=='__REACT_QUERY_STATE__':
            d=json.loads(base64.b64decode(v).decode())
            for q in d['queries']:
                if q['queryKey'][0].startswith('app-page'):
                    x=q['state']['data']
                    return {'slug':slug,'company':x['app']['company']['name'],'reviews':x['app']['reviews'],
                            'dates':[r['createdAt'][:10] for r in x['reviews']['reviews']],'pricing':x['app']['pricing']['label'],
                            'plans':x.get('pricingPlans')}
    return {'slug':slug,'fout':True}
slugs=open(sys.argv[1]).read().split()
with open(sys.argv[2],'w') as f, ThreadPoolExecutor(3) as ex:
    for r in ex.map(one,slugs): f.write(json.dumps(r)+'\n'); f.flush()
