# veilige zone voor de ronde-5 dieren: tekstvakken opmeten (tekst niet tekenen), held aan/uit vergelijken
import sys; sys.path.insert(0,'/home/claude/dortus-hq/ontwerp/garmin/bron')
import werelden_v21 as w
import werelden_v4_vliegers as V, werelden_v4_huisjes as H
from werelden_v21 import DAG, NACHT
import numpy as np
vakken=[]
def nep(self, x, y, s, maat, c, dik=True):
    f = w.f(w.FS if dik else w.FM, round(maat * self.s)); l, t, r, b = f.getbbox(s)
    ww = self.dr.textlength(s, font=f); X = x * self.s - ww / 2; Y = y * self.s
    K = self.k; vakken.append((s, (X/K, (Y + t)/K, (X + ww)/K, (Y + b)/K)))
w.Doek.tekst = nep
def zet(mod, aan):
    if mod is V: V.HELD_AAN = aan
    else: H.ZONDER_HELD[0] = not aan; H.ZONDER_DIER[0] = not aan
slecht=0
for mod, dier in ((V,'manta'),(H,'eel'),(H,'cucumber')):
  for nacht in (False,True):
   for D_,am in ((260,False),(454,True)):
    for naam in ('hold','in','uit','calm','eind','menu'):
      dd=NACHT if nacht else DAG
      vakken.clear(); a=np.array(mod.scherm(naam,dier)(D_,am,dd,nacht)).astype(int); vk=list(vakken)
      zet(mod,False); b=np.array(mod.scherm(naam,dier)(D_,am,dd,nacht)).astype(int); zet(mod,True)
      ys,xs=np.where(abs(a-b).sum(2)>30)
      if not len(ys): continue
      k=260/D_; ys=ys*k; xs=xs*k; best=99; vk=[(s,(x0*k,y0*k,x1*k,y1*k)) for s,(x0,y0,x1,y1) in vk]; wat=''
      for s,(x0,y0,x1,y1) in vk:
          dx=np.maximum(0,np.maximum(x0-xs,xs-x1)); dy=np.maximum(0,np.maximum(y0-ys,ys-y1))
          m=float(np.sqrt(dx*dx+dy*dy).min())
          if m<best: best,wat=m,s
      if best<6: slecht+=1; print(dier,naam,'nacht' if nacht else 'dag',D_,'TE DICHT',round(best,1),'bij',repr(wat))
      elif D_==260 and not nacht: print(dier,naam,'ok',round(best,1),'bij',repr(wat))
print('te dicht:',slecht)
