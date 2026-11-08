# Haalt de lijst nieuwste Quest-apps van vrdb.app (__data.json, 50 per pagina) tot een einddatum.
import sys,json,time,subprocess
sys.path.insert(0,'.'); dv=__import__("meta-vrdb-devalue")
out=sys.argv[1]; stop=sys.argv[2]; start=int(sys.argv[3]) if len(sys.argv)>3 else 1
f=open(out,'a')
p=start
while True:
    tmp='/tmp/meta-pg.json'
    r=subprocess.run(['curl','-sL','-m','60','-o',tmp,'-w','%{http_code}',f'https://vrdb.app/new-releases/__data.json?page={p}'],capture_output=True,text=True)
    try: a=dv.apps(tmp)['applications']
    except Exception as e:
        print('fout',p,r.stdout,e,flush=True); time.sleep(10); continue
    last=None
    for x in a:
        pa=(x.get('prices_all') or {}).get('USD') or {}
        rec={k:x.get(k) for k in ['id','name','slug','release_date_clean','rating_count','rating_score','written_review_count','review_count_increase_one_week','developer','developer_id','publisher','category','genres','is_early_access','subscription_type','has_iap_disclosure','has_in_app_ads','has_catalog_addons','has_subscription','store_removal_date','purchase_signals','in_horizon_plus_catalog','steam_app_id']}
        rec['usd']=(pa.get('price') or {}).get('amount'); rec['page']=p
        f.write(json.dumps(rec)+'\n'); last=x.get('release_date_clean')
    f.flush(); print(p,len(a),last,flush=True)
    if not a or (last and last<stop): break
    p+=1; time.sleep(1.5)
