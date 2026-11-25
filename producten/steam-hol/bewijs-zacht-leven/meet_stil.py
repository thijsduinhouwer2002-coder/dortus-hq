import sys, subprocess, numpy as np
w,h=1024,120
def meet(pad, zonder_gloop, drempel=12):
    p=subprocess.Popen(["ffmpeg","-v","error","-i",pad,"-f","rawvideo","-pix_fmt","gray","-"],stdout=subprocess.PIPE)
    vorig=None;i=0;sb=None;st=[]
    while True:
        b=p.stdout.read(w*h)
        if len(b)<w*h:break
        f=np.frombuffer(b,np.uint8).reshape(h,w).astype(np.int16)
        f=np.concatenate([f[:,:500],f[:,600:670]],1) if zonder_gloop else f[:,:670]
        if vorig is not None:
            n=int((np.abs(f-vorig)>drempel).sum())
            if n<3:
                if sb is None: sb=i
            elif sb is not None: st.append((sb/5,(i-sb)/5)); sb=None
        vorig=f;i+=1
    if sb is not None: st.append((sb/5,(i-sb)/5))
    st.sort(key=lambda s:-s[1])
    return i/5, st
for pad in sys.argv[1:]:
    for zg in (False, True):
        d,st=meet(pad,zg)
        print(pad.split('/')[-1], "zonder Gloop" if zg else "hol met Gloop", "duur %.0f s"%d, "langste stil %.1f s"%(st[0][1] if st else 0), "stukken >15 s: %d"%sum(1 for a,b in st if b>15), "samen >15 s: %.0f s"%sum(b for a,b in st if b>15))
