import subprocess,re,json
repo='or'
log=subprocess.run(['git','-C',repo,'log','--reverse','--format=%H %at','--','community-plugins.json'],capture_output=True,text=True).stdout.split('\n')
log=[l.split() for l in log if l]
pick=log
p=subprocess.Popen(['git','-C',repo,'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
first={}
rx=re.compile(rb'"id":\s*"([^"]+)"')
for h,t in pick:
    p.stdin.write(f'{h}:community-plugins.json\n'.encode());p.stdin.flush()
    hdr=p.stdout.readline().split()
    if hdr[-1]==b'missing': continue
    n=int(hdr[2]);data=p.stdout.read(n);p.stdout.read(1)
    for m in rx.findall(data):
        i=m.decode()
        if i not in first: first[i]=int(t)
json.dump(first,open('firstseen.json','w'));print(len(first))
