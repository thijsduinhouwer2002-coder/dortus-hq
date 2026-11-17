# Verhaal 23 (Fenna): demo-teksten indelen (tijdsgrens, inhoudsgrens, save mee). Gebruik: python3 -I demo-einde-analyse.py <uitmap van demo-einde-haal.py> <csv-uit>
import json,re,html,csv,sys
T=re.compile(r'(time.limit|\b\d+\s*(?:-\s*\d+\s*)?(?:min|mins|minutes|hours?|hrs)\b(?: of)? (?:play|gameplay|demo)|playtime limit|limited time)',re.I)
C=re.compile(r'[^.!?]*(level cap|capped|cap of|up to (?:level|stage|wave|floor|day)|first (?:chapter|area|zone|region|biome|world|act|layer|floor|stage|island|map)|limited to|only (?:the first|includes|contains)|out of \d+|includes? (?:the )?(?:first|\d+)|contains? (?:the )?(?:first|\d+|a portion|part)|portion of|part of the|stopping point|full (?:version|game|release) (?:adds|includes|will include|unlocks|offers|features|has|will have)|(?:more|additional) (?:\w+ )?(?:in|with) the full)[^.!?]*',re.I)
SJ=re.compile(r'(save|progress|data|kitten|tank|grow)[^.!?]{0,60}(carr(?:y|ies|ied) over|transfer|inherit)',re.I)
SN=re.compile(r'not (?:be )?(?:carr|transfer)|won.t (?:carr|transfer)|does not carry|doesn.t carry|cannot be (?:carr|transfer)',re.I)
w=csv.writer(open(sys.argv[2],'w',newline='')); w.writerow(['appid','naam','binnenkort','reviews','pct_positief','lijkt_op_hats','demo_appid','tekst_op_demopagina','tijdsgrens','zegt_geen_tijdsgrens','inhoudsgrens','save_mee','save_niet_mee','voorbeeld_inhoud'])
for l in open(sys.argv[1]+'/demos.jsonl'):
    r=json.loads(l)
    t=html.unescape(re.sub(r'<br ?/?>|</?p>|</li>|</h\d>|<li>','. ',(r.get('demo_short') or '')+' . '+(r.get('demo_desc') or '')))
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)).strip(' .')
    ti=[m.group(0) for m in T.finditer(t)]; geen=any(re.search('no time limit|without time limit',x,re.I) for x in [t])
    ci=[m.group(0).strip()[:140] for m in C.finditer(t)]
    sn=bool(SN.search(t)); sj=bool(SJ.search(t)) and not sn
    w.writerow([r['appid'],r['naam'],r['binnenkort'],r['reviews'],r['pct'],r['lijkt'],(r.get('demos') or [{}])[0].get('appid',''),int(len(t)>20),int(bool(ti) and not geen),int(geen),int(bool(ci)),int(sj),int(sn),ci[0] if ci else ''])
