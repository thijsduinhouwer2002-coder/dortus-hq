import json,subprocess,time,sys
lijst=json.load(open(sys.argv[1])); stap=int(sys.argv[2]); uit=sys.argv[3]
f=open(uit,'a')
for a in lijst[::stap]:
    r=subprocess.run(['curl','-sS','-m','30','https://marketplace.zoom.us/api/v1/marketplaceV2/detailV2/'+a['id']],capture_output=True,text=True)
    try: d=json.loads(r.stdout)
    except Exception: continue
    b=d.get('appDeveloperBusinessInfo') or {}
    f.write(json.dumps({'id':a['id'],'naam':d.get('displayName'),'bedrijf':d.get('companyName'),'created':d.get('createdTime'),'modified':d.get('modifiedTime'),'monetized':d.get('monetized'),'devtype':d.get('developerType'),'zapp':d.get('zapp'),'adres':b.get('address'),'cats':d.get('categories'),'installType':d.get('installType')})+'\n'); f.flush()
    time.sleep(0.6)
