import sys,glob,re,random,html
root=sys.argv[1]
files=sorted(f for f in glob.glob(root+'/**/*.html',recursive=True) if '/fileTemplates/' not in f)
EN=set('the and is of to this with that for are be you can'.split()); FR=set('le la les et est de des du pour que une un avec vous dans'.split())
def score(f):
    t=open(f,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<pre.*?</pre>|<code.*?</code>','',t,flags=re.S); t=html.unescape(re.sub(r'<[^>]+>',' ',t))
    w=re.findall(r"[a-zA-Zéèàùâêîôûç']+",t.lower())
    return sum(x in EN for x in w), sum(x in FR for x in w)
stat={'fr':0,'en':0,'leeg':0}; en_list=[]
for f in files:
    e,r=score(f)
    if e+r<3: stat['leeg']+=1
    elif e>r: stat['en']+=1; en_list.append(f)
    else: stat['fr']+=1
print(len(files),stat)
for f in en_list[:15]: print('EN?',f)
random.seed(81126)
for f in random.sample(files,10): print('SAMPLE',f,score(f))
