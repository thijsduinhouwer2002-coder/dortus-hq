"""Controle vloeiend (wens Thijs 25 nov): gelijkmatig 30 beelden per seconde, geen overgeslagen beelden.
1. Tijdstempels: elk beeld 1/30 s na het vorige (ffprobe). Een gat van meer dan 1,5 keer is een overgeslagen beeld.
2. Waar de muis beweegt (uit film.json en de opname zelf) mogen geen twee beelden achter elkaar gelijk zijn
   (ffmpeg mpdecimate telt ze). Stilstand in een pauze is wel gelijk: dat is geen haperen.
Gebruik: python3 vloeiend.py <video> [van_s tot_s ...]  (paren: stukken waarin beweging moet zijn)"""
import json
import subprocess
import sys

video = sys.argv[1]
stukken = [(float(a), float(b)) for a, b in zip(sys.argv[2::2], sys.argv[3::2])]
uit = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "frame=pts_time",
                      "-of", "csv=p=0", video], capture_output=True, text=True).stdout.split()
t = [float(x.strip(",")) for x in uit if x.strip(",").strip()]
d = [b - a for a, b in zip(t, t[1:])]
gaten = [round(t[i], 3) for i, x in enumerate(d) if x > 1.5 / 30]
dubbel_ts = [round(t[i], 3) for i, x in enumerate(d) if x < 0.5 / 30]
fps = (len(t) - 1) / (t[-1] - t[0]) if len(t) > 1 else 0
uitslag = {"beelden": len(t), "duur_s": round(t[-1] - t[0], 3) if t else 0, "fps": round(fps, 3),
           "gaten": gaten[:20], "aantal_gaten": len(gaten), "dubbele_tijd": len(dubbel_ts), "stukken": []}
for van, tot in stukken:
    # eigen telling: twee beelden zijn gelijk als minder dan 4 pixels meer dan 24 grijswaarden verschillen
    # (mpdecimate ziet een kleine muispijl niet als verschil)
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(van), "-t", str(tot - van), "-i", video,
                          "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
    br, ho = (int(x) for x in subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
              "stream=width,height", "-of", "csv=p=0", video], capture_output=True, text=True).stdout.strip().split(",")[:2])
    b = np.frombuffer(raw, np.uint8).reshape(-1, ho, br)
    gelijk = sum(1 for k in range(1, len(b)) if (np.abs(b[k].astype(np.int16) - b[k - 1]) > 24).sum() < 4)
    uitslag["stukken"].append({"van": van, "tot": tot, "beelden": len(b), "gelijk": gelijk})
ok = not gaten and not dubbel_ts and abs(fps - 30) < 0.05 and all(s["gelijk"] <= s["beelden"] * 0.10
                                                                     for s in uitslag["stukken"])
uitslag["oordeel"] = "GOED" if ok else "FOUT"
print(json.dumps(uitslag, indent=1))
sys.exit(0 if ok else 1)
