import subprocess,sys,numpy as np
f,s0,klik=sys.argv[1],float(sys.argv[2]),float(sys.argv[3])
SR=22050
a=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-ss",str(s0-2),"-i",f,"-t","30","-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True).stdout,np.float32)
hop=256; fr=np.lib.stride_tricks.sliding_window_view(a,1024)[::hop]
sp=np.abs(np.fft.rfft(fr*np.hanning(1024),axis=1)); low=sp[:,:12]  # bas/kick onder ±250 Hz
fl=np.maximum(0,np.diff(np.log1p(low),axis=0)).sum(1)
t=(np.arange(len(fl))+1)*hop/SR+(s0-2)
# sterkste kick in 2 s rond s0
m=(t>s0-1)&(t<s0+1); k=t[m][np.argmax(fl[m])]
print(f"sterkste kick bij {k:.3f}; begin zodat die op {klik} valt: {k-klik:.3f}")
