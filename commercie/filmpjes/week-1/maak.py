# Maakt staande filmpjes (1080x1920) uit echte beelden van Click Joints. Chris, 15 nov 2026.
# Gebruik: python3 maak.py f1.json werkmap   (bronbeelden in ./bron, zie bronnen.sha256)
import json,subprocess,sys,os,re
from PIL import Image,ImageDraw,ImageFont
W,H=1080,1920; BG='0x15171c'; GROEN=(0,214,150); WIT=(255,255,255)
FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; FR='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
def run(c): subprocess.run(c,check=True)
def tekstpng(pad,regels,grootte=78,y0=0,font=FB):
    """regels: lijst van strings; woorden tussen *sterren* worden groen."""
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=ImageFont.truetype(font,grootte)
    y=y0
    for r in regels:
        delen=[]
        for k,stuk in enumerate(re.split(r'\*',r)):
            for w in stuk.split(' '):
                if not w: continue
                if delen and w[0] in ',.:;!?' and stuk.startswith(w):
                    delen.append(('\x00'+w,False))
                else: delen.append((w,k%2==1))
        sp=d.textlength(' ',font=f)
        stukken=[]
        for w,g in delen:
            if w.startswith('\x00'): stukken.append((w[1:],g,False))
            else: stukken.append((w,g,True))
        breedte=sum(d.textlength(w,font=f) for w,_,_ in stukken)+sp*sum(1 for i,(_,_,s2) in enumerate(stukken) if s2 and i>0)
        x=(W-breedte)/2
        for i,(w,g,s2) in enumerate(stukken):
            if s2 and i>0: x+=sp
            d.text((x,y),w,font=f,fill=GROEN if g else WIT,stroke_width=4,stroke_fill=(10,10,12))
            x+=d.textlength(w,font=f)
        y+=int(grootte*1.22)
    im.save(pad)
def segment(i,s,map_):
    out=f'{map_}/seg{i}.mp4'; dur=s['dur']
    mh=s.get('h',1013); my=s.get('y',540)+s.get('dy',0)
    if s['bron'].endswith('.mp4'):
        cw=s.get('cw',1152); cx=s.get('cx',(1920-cw)//2)
        inp=['-ss',str(s['start']),'-t',str(dur),'-i',s['bron']]
        vf=s.get('vf') or f"crop={cw}:1080:{cx}:0,scale=1080:{mh}"
    else:
        bron=s['bron']
        if 'rond' in s:  # [mx,my,r]: ronde uitsnede (horloge zonder witte simulatorrand) op de donkere achtergrond
            mx,mmy,r=s['rond']; im=Image.open(bron).convert('RGB').crop((mx-r,mmy-r,mx+r,mmy+r))
            mask=Image.new('L',(8*r,8*r),0); ImageDraw.Draw(mask).ellipse((0,0,8*r-1,8*r-1),fill=255)
            m=int(r*s.get('marge',1.0))  # marge > 1: donkere rand om het horloge
            vlak=Image.new('RGB',(2*m,2*m),tuple(int(BG[2:][k:k+2],16) for k in (0,2,4)))
            vlak.paste(im,(m-r,m-r),mask.resize(im.size,Image.LANCZOS)); bron=f'{map_}/rond{i}.png'; vlak.save(bron)
            s=dict(s,crop=[0,0,2*m,2*m])
        inp=['-loop','1','-t',str(dur),'-framerate','30','-i',bron]
        cx,cy,cw,ch=s['crop']; z=s.get('zoom',0.06)
        vf=(f"crop={cw}:{ch}:{cx}:{cy},scale={int(1080*1.0)*2}:-2,"
            f"zoompan=z='1+{z}*on/({dur}*30)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x{mh}:fps=30")
    run(['ffmpeg','-v','error','-y',*inp,'-f','lavfi','-t',str(dur),'-i',f'color=c={BG}:s={W}x{H}:r=30',
         '-filter_complex',f"[0:v]{vf},setsar=1,fps=30[m];[1:v][m]overlay=0:{my}:shortest=1,format=yuv420p[v]",
         '-map','[v]','-an','-c:v','libx264','-preset','veryfast','-crf','20',out])
    return out
def bouw(spec,map_):
    os.makedirs(map_,exist_ok=True)
    segs=[segment(i,s,map_) for i,s in enumerate(spec['segmenten'])]
    with open(f'{map_}/lijst.txt','w') as f: f.write(''.join(f"file '{os.path.abspath(p)}'\n" for p in segs))
    basis=f'{map_}/basis.mp4'
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{map_}/lijst.txt','-c','copy',basis])
    inps=['-i',basis]; fc=''; last='0:v'
    for k,t in enumerate(spec['teksten']):
        p=f'{map_}/t{k}.png'; tekstpng(p,t['regels'],t.get('grootte',78),t.get('y',230),FR if t.get('licht') else FB)
        inps+=['-i',p]; nxt=f'v{k}'
        fc+=f"[{last}][{k+1}:v]overlay=0:0:enable='gte(t,{t['van']})*lt(t,{t['tot']})'[{nxt}];"; last=nxt
    run(['ffmpeg','-v','error','-y',*inps,'-filter_complex',fc.rstrip(';'),'-map',f'[{last}]','-an',
         '-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-movflags','+faststart',spec['uit']])
if __name__=='__main__':
    bouw(json.load(open(sys.argv[1])),sys.argv[2])
