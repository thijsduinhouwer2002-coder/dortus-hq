import subprocess, sys
F="/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
def esc(t): return t.replace("\\","\\\\").replace(":","\\:").replace("'","\u2019").replace(",","\\,")
def clip(src, start, end, caps, title, out):
    dur=end-start
    flt=["[0:v]scale=-2:1080,setsar=1[v]","color=c=0x15171c:s=1920x1080:d=%.2f:r=30[bg]"%dur,"[bg][v]overlay=x=W-w:y=0:shortest=1[b]"]
    cur="b"
    dt=[f"drawtext=fontfile={F}:text='{esc(title)}':x=48:y=64:fontsize=34:fontcolor=0x8fb3ff"]
    for a,b,t in caps:
        lines=t.split("|")
        for i,l in enumerate(lines):
            dt.append(f"drawtext=fontfile={F}:text='{esc(l)}':x=48:y=440+{i}*62:fontsize=46:fontcolor=white:enable='between(t,{a-start:.2f},{b-start:.2f})'")
    flt.append(f"[{cur}]"+",".join(dt)+"[o]")
    cmd=["ffmpeg","-v","error","-y","-ss",str(start),"-t",str(dur),"-i",src,"-filter_complex",";".join(flt),"-map","[o]","-an","-c:v","libx264","-crf","23","-preset","medium","-pix_fmt","yuv420p","-movflags","+faststart",out]
    subprocess.run(cmd,check=True)
T="Click Joints Pro"
if "2" not in sys.argv: clip("r17/opname-pro.mkv",0,45.5,[
 (0,2.8,"Start with your|rigged figure"),
 (2.8,4.2,"Click|Figure from rig"),
 (4.2,10.6,"Every joint gets|a type and a|bend range"),
 (10.6,17.7,"Show bend range:|see how far|the knee bends"),
 (17.7,22.6,"Past the stop,|the parts turn red"),
 (22.6,25.6,"Pose the figure|to check it"),
 (25.6,35.2,"Exploded view:|every printable part"),
 (35.2,39.5,"Export STL or 3MF"),
 (39.5,45.5,"Ready to print"),
],T+"  ·  1. Figure from rig","1-figure-from-rig.mp4")
# Daan M1 (24 nov): begin bij de staafjes (frame 1222, de figuur met kniebereik is weg vanaf 1220);
# einde op 1612, want vanaf ±1620 komt de figuur terug in beeld. C1: getallen als onderschrift (testkaart.py SPELINGEN).
clip("regisseur1.mkv",1222/30,1612/30,[
 (1222/30,1400/30,"Print this first:|a small fit test|with your clearances"),
 (1400/30,1500/30,"Five joints:|0.10  0.15  0.20|0.25  0.30 mm"),
 (1500/30,1612/30,"Keep the one that|turns without wobble"),
],T+"  ·  2. Fit test","2-fit-test.mp4")
