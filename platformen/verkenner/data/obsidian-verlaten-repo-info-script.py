import json,subprocess,time
old=json.load(open('oud_top1000.json'))
repos=[r[3] for r in old]
batches=[];cur=[]
for r in repos:
    q=' '.join('repo:'+x for x in cur+[r])
    if len(q)>240: batches.append(cur);cur=[r]
    else: cur.append(r)
batches.append(cur)
info={}
for b in batches:
    q=' '.join('repo:'+x for x in b)
    out=subprocess.run(['gh','api','-X','GET','search/repositories','-f','q='+q,'-f','per_page=100'],capture_output=True,text=True).stdout
    try:
        for it in json.loads(out)['items']:
            info[it['full_name'].lower()]=[it['open_issues_count'],it['pushed_at'],it['archived'],it['stargazers_count']]
    except Exception as e: print('fout',out[:200])
    time.sleep(2.2)
json.dump(info,open('repo_info.json','w'))
print(len(batches),len(info))
