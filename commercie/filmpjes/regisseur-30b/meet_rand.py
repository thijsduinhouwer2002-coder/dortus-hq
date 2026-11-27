import sys,subprocess,json,numpy as np
opn=sys.argv[1]
f=json.load(open(opn+'/film.json'));st=float(open(opn+'/start.txt').read())
a0=f['delen']['knie']-st; a1=f['delen']['kleur']-st
W,H=1080,1920
p=subprocess.run(['ffmpeg','-v','error','-ss',f'{a0:.3f}','-t',f'{a1-a0:.3f}','-i',opn+'/scherm-ruw.ts','-vf','fps=10','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
n=len(p)//(W*H*3); res=[]
for i in range(n):
    v=np.frombuffer(p[i*W*H*3:(i+1)*W*H*3],np.uint8).reshape(H,W,3)[360:1880,0:687].astype(int)
    rood=(v[:,:,0]>180)&(v[:,:,1]<90)&(v[:,:,2]<90)
    gr=(v[:,:,1]>150)&(v[:,:,0]<120)&(v[:,:,2]<140)
    pil=(v.max(2)<40)  # donkere pil achter label (achtergrond is 48)
    c=lambda m:int(np.where(m.sum(0)>3)[0].min()) if (m.sum(0)>3).any() else 999
    res.append((c(rood),c(gr)))
print(json.dumps({'beelden':n,'rood_min_x':min(r[0] for r in res),'groen_min_x':min(r[1] for r in res)}))
