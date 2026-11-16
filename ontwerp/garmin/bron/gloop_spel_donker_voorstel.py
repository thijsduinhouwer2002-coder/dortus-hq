import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
def donker(src, mid=(150,70,18), rand=(18,9,5), beam=(255,200,140), bk=0.55):
    im=Image.open(src).convert('RGB'); a=np.array(im).astype(float); N=a.shape[0]
    gl=Image.new('L',(N,N),0); ImageDraw.Draw(gl).ellipse([-0.15*N,0.2*N,1.15*N,1.45*N],fill=255)
    g=np.array(gl.filter(ImageFilter.GaussianBlur(N*0.16)))[...,None]/255.0
    bg=np.array(rand)*(1-g)+np.array(mid)*g
    def m(c,t=3): return (np.abs(a-np.array(c)).max(-1)<=t)[...,None]
    out=np.where(m((172,85,0)),bg,a)
    for c,k in [((230,161,90),bk),((189,109,24),bk*0.5)]:
        out=np.where(m(c),bg*(1-k)+np.array(beam)*k,out)
    out=np.where(m((82,0,0)),bg*0.35+np.array((60,8,4))*0.65,out)
    return Image.fromarray(out.clip(0,255).astype('uint8'))
if __name__=='__main__':
    donker(sys.argv[1]).save(sys.argv[2])
