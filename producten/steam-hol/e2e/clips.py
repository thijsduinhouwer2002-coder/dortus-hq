# Olaf 16 nov: knipt echte mp4's voor Chris (TikTok) uit een Movie Maker-opname van een nieuw spel.
# Gebruik: python clips.py <map met f00000000.png...> <film.log> <uitmap> <fps>
# Zoekt in de log de eerste hap ("Gloop ate", "<bewoner> ate") en de eerste terugkomer ("is back for") en knipt
# 1 hap: 3 s ervoor tot 9 s erna (12 s); 2 terug: 2 s ervoor tot 10 s erna (12 s). Ware grootte, alle beelden.
import re, subprocess, sys, pathlib
import imageio_ffmpeg

bron, log, uit, fps = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), int(sys.argv[4])
uit.mkdir(parents=True, exist_ok=True)
regels = log.read_text(encoding="utf-8", errors="replace").splitlines()
def eerste(patroon):
    for r in regels:
        m = re.match(r"HOL kroniek ([0-9.]+) \(wacht ([0-9.]+)\): (.*)", r)
        if m and re.search(patroon, m.group(3)):
            return float(m.group(1)) - float(m.group(2)), m.group(3)   # moment dat het gebeurde, niet dat de regel kwam
    return None, None
n = len(list(bron.glob("f*.png")))
ff = imageio_ffmpeg.get_ffmpeg_exe()
for naam, patroon, voor, na in [("1-hap", r" ate ", 3.0, 9.0), ("2-terug", r" is back for ", 2.0, 10.0)]:
    t, regel = eerste(patroon)
    if t is None:
        print(f"{naam}: niet gevonden in de log"); continue
    start = max(0, int((t - voor) * fps))
    aantal = min(int((voor + na) * fps), n - start)
    if aantal <= 0:
        print(f"{naam}: opname te kort (t={t:.1f}, {n} beelden)"); continue
    doel = uit / f"{naam}.mp4"
    subprocess.run([ff, "-loglevel", "error", "-y", "-framerate", str(fps), "-start_number", str(start),
                    "-i", str(bron / "f%08d.png"), "-frames:v", str(aantal), "-c:v", "libx264", "-crf", "14",
                    "-preset", "slow", "-pix_fmt", "yuv420p", str(doel)], check=True)
    print(f"{naam}: t={t:.1f} s, beelden {start} tot {start + aantal}, {aantal / fps:.1f} s, {doel.stat().st_size} bytes, regel: {regel}")
