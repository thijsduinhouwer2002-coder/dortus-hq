import subprocess,sys,numpy as np
SR=22050;L=22
for f in sys.argv[1:]:
    a=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True).stdout,np.float32)
    h=SR//2; r=np.array([20*np.log10(np.sqrt(np.mean(a[i:i+h]**2))+1e-9) for i in range(0,len(a)-h,h)])
    best=None
    for s in range(0,len(r)-2*L):
        w=r[s:s+2*L]; sc=w.min()+w.mean()-w.std()
        if best is None or sc>best[0]: best=(sc,s/2,w.mean(),w.min(),w.std())
    s0=best[1]; seg=a[int(s0*SR):int((s0+L)*SR)]
    hop=512; fr=np.lib.stride_tricks.sliding_window_view(seg,1024)[::hop]
    sp=np.abs(np.fft.rfft(fr*np.hanning(1024),axis=1)); fl=np.maximum(0,np.diff(np.log1p(sp),axis=0)).sum(1); fl-=fl.mean()
    ac=np.correlate(fl,fl,'full')[len(fl)-1:]; fps=SR/hop; lags=np.arange(len(ac)); bpm=60*fps/np.maximum(lags,1); m=(bpm>85)&(bpm<170); l=lags[m][np.argmax(ac[m])]
    print(f"{f}: beste begin {s0:.1f}s gem {best[2]:.1f} min {best[3]:.1f} spreiding {best[4]:.1f} dB, tempo ±{60*fps/l:.0f} bpm, tel {ac[l]/ac[0]:.2f}, duur {len(a)/SR:.0f}s")
