import sys, struct, json
def varint(b,i):
    r=0;s=0
    while True:
        c=b[i];i+=1;r|=(c&0x7f)<<s;s+=7
        if c<0x80: return r,i
def fields(b):
    i=0;n=len(b)
    while i<n:
        k,i=varint(b,i);f=k>>3;t=k&7
        if t==0: v,i=varint(b,i)
        elif t==2:
            l,i=varint(b,i);v=b[i:i+l];i+=l
        elif t==5: v=b[i:i+4];i+=4
        elif t==1: v=b[i:i+8];i+=8
        else: raise ValueError(t)
        yield f,t,v
data=open(sys.argv[1],'rb').read()
i=0;out=[]
while i+4<=len(data):
    l=struct.unpack('<I',data[i:i+4])[0];i+=4
    msg=data[i:i+l];i+=l
    s={'res':[],'vars':{}}
    for f,t,v in fields(msg):
        if f==1: s['ep']=v.decode('utf8','replace')
        elif f==2:
            for f2,t2,v2 in fields(v):
                if f2==1: s['max']=v2
                elif f2==2: s['clients']=v2
                elif f2==4: s['host']=v2.decode('utf8','replace')[:200]
                elif f2==5: s['gametype']=v2.decode('utf8','replace')
                elif f2==8: s['res'].append(v2.decode('utf8','replace'))
                elif f2==12:
                    kk=vv=None
                    for f3,t3,v3 in fields(v2):
                        if f3==1: kk=v3.decode('utf8','replace')
                        elif f3==2: vv=v3.decode('utf8','replace')[:200]
                    if kk: s['vars'][kk]=vv
    out.append(s)
with open(sys.argv[2],'w') as fo:
    for s in out: fo.write(json.dumps(s,ensure_ascii=False)+'\n')
print(len(out))
