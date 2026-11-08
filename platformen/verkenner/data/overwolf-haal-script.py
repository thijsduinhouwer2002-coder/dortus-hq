import sys,re,json,subprocess,time
slugs=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out=open(sys.argv[2],'w')
def g(pat,s,cast=str):
    m=re.search(pat,s); return cast(m.group(1)) if m else None
for s in slugs:
    h=subprocess.run(['curl','-sL','-m','25','-A','Mozilla/5.0','https://www.overwolf.com/app/'+s],capture_output=True,text=True).stdout
    h=h.replace('\\"','"')
    d={'slug':s,
     'titel':g(r'"title":"([^"]+)"',h),'maker':g(r'"author":"([^"]+)"',h),
     'downloads':g(r'"downloads":"(\d+)"',h,int),'ratings':g(r'"totalRatings":(\d+)',h,int),
     'gem':g(r'"averageRate":([\d.]+)',h,float),'updated':g(r'"updatedAt":"([^"]+)"',h),
     'ads':g(r'"doesContainsAds":(true|false)',h),'premium':g(r'"isPremium":(true|false)',h),
     'gratis':g(r'"isFree":(true|false)',h),'versie':g(r'"latestVersion":"([^"]+)"',h),
     'electron':g(r'"isElectron":(true|false)',h),
     'reviewdatums':sorted(set(re.findall(r'"createdAt":"(\d{4}-\d\d-\d\d)',h)))}
    out.write(json.dumps(d,ensure_ascii=False)+'\n'); out.flush(); time.sleep(0.4)
