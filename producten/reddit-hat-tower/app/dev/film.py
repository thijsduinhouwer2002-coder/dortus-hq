"""Maakt het inzendfilmpje: 1080x1920, onder 1 minuut, met geluid, een hele ronde en het eindmoment.

Gebruik (lokale server moet draaien: PROEF=1 npm run local):
    python3 dev/film.py <uit.mp4>

Hoe: het screencast van Chrome levert beelden op 1080x1920 (360x640 op 3x), elk met zijn tijd. Het spel onthoudt in ?film=1 elke klank
met zijn tijd en rendert die achteraf tot een WAV (OfflineAudioContext). De tijden zetten
beeld en geluid gelijk via performance.timeOrigin. De Engelse teksten komen er met ffmpeg overheen.
"""
import base64
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

UIT = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/gloop-film.mp4")
APP = Path(__file__).resolve().parent.parent
LETTER = APP / "public/fonts/LilitaOne-Regular.ttf"
WERK = Path(tempfile.mkdtemp(prefix="gloop-film-"))
SPELER = re.search(r'SPELER_JS = """(.*?)"""', (APP / "dev/schermen.py").read_text(), re.S).group(1)
# Voor het filmpje mikt de speler iets beter (zoals iemand die het spel kent).
SPELER = SPELER.replace("* 40", "* 22").replace("< 0.12", "< 0.04")

with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--autoplay-policy=no-user-gesture-required"])
    ctx = browser.new_context(viewport={"width": 360, "height": 640}, device_scale_factor=3, is_mobile=True, has_touch=True)
    pagina = ctx.new_page()
    fouten = []
    pagina.on("pageerror", lambda e: fouten.append(str(e)))
    pagina.goto(f"http://localhost:5173/game.html?proef=1&film=1&u=film{int(time.time()) % 100000}")
    pagina.wait_for_selector("body.klaar")
    # Beelden op ware grootte (1080x1920) met hun tijd, via het screencast van Chrome.
    beelden = []
    cdp = ctx.new_cdp_session(pagina)

    def beeld(e):
        n = len(beelden)
        (WERK / f"b{n:05d}.jpg").write_bytes(base64.b64decode(e["data"]))
        beelden.append(e["metadata"]["timestamp"])
        cdp.send("Page.screencastFrameAck", {"sessionId": e["sessionId"]})

    cdp.on("Page.screencastFrame", beeld)
    cdp.send("Page.startScreencast", {"format": "jpeg", "quality": 90, "maxWidth": 1080, "maxHeight": 1920, "everyNthFrame": 1})
    pagina.wait_for_timeout(500)
    oorsprong = pagina.evaluate("performance.timeOrigin")
    merk = pagina.evaluate("performance.now()")
    pagina.wait_for_timeout(3000)
    print("start,", len(beelden), "beelden", flush=True)
    pagina.click("#knop-speel")
    t_speel = pagina.evaluate("performance.now()")
    pagina.evaluate(SPELER)
    for _ in range(600):
        if pagina.evaluate("window.gloopProef().toestand") == 5:
            break
        pagina.wait_for_timeout(100)
    print("ronde klaar,", len(beelden), "beelden", flush=True)
    t_einde = pagina.evaluate("performance.now()")
    pagina.wait_for_timeout(6500)
    # Rustig door het uitslagvel naar de ranglijst.
    pagina.evaluate("document.getElementById('einde').scrollTo({top: 420, behavior: 'smooth'})")
    pagina.wait_for_timeout(2600)
    t_stop = pagina.evaluate("performance.now()")
    cdp.send("Page.stopScreencast")
    duur = (t_stop - merk) / 1000 + 0.5
    wav = pagina.evaluate(f"window.gloopFilmGeluid({merk}, {duur})")
    (WERK / "geluid.wav").write_bytes(base64.b64decode(wav))
    ctx.close()
    browser.close()

# Tijden in seconden vanaf het merk (begin van het filmpje).
nul = (oorsprong + merk) / 1000
lijst = []
for i, ts in enumerate(beelden):
    if ts >= nul:
        lijst.append((i, ts - nul))
with open(WERK / "lijst.txt", "w") as f:
    for k, (i, tt) in enumerate(lijst):
        volgende = lijst[k + 1][1] if k + 1 < len(lijst) else tt + 0.04
        f.write(f"file 'b{i:05d}.jpg'\nduration {max(0.001, volgende - tt):.4f}\n")
    f.write(f"file 'b{lijst[-1][0]:05d}.jpg'\n")
eerste = lijst[0][1]
print(f"{len(lijst)} beelden, gemiddeld {len(lijst) / ((t_stop - merk) / 1000):.1f} per seconde")


def t(perf):
    return (perf - merk) / 1000 - eerste


s, e = t(t_speel), t(t_einde)
eind = t(t_stop)
teksten = [
    (s + 2.6, s + 6.0, "One tap. 30 seconds."),
    (s + 9.0, s + 13.0, "Perfect gulps stack more hats"),
    (s + 17.0, s + 21.0, "Same tower for everyone today"),
    (s + 24.0, s + 28.5, "Every subreddit builds one tower"),
    (e + 7.0, eind, "Share your run. New tower tomorrow."),
]
filters = []
for a, b, tekst in teksten:
    filters.append(
        f"drawtext=fontfile={LETTER}:text='{tekst}':fontsize=66:fontcolor=white:borderw=9:bordercolor=0x2b1206:"
        f"x=(w-text_w)/2:y=h*0.17:enable='between(t,{a:.2f},{b:.2f})'"
    )
subprocess.run(
    [
        "ffmpeg", "-v", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", str(WERK / "lijst.txt"),
        "-ss", f"{eerste:.3f}", "-i", str(WERK / "geluid.wav"),
        "-t", f"{eind:.2f}",
        "-vf", ",".join(["fps=30", "scale=1080:1920:flags=lanczos", *filters]),
        "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
        str(UIT),
    ],
    check=True,
)
for f in WERK.iterdir():
    f.unlink()
WERK.rmdir()
print(f"filmpje: {UIT} ({eind:.1f} s), ronde begint op {s:.1f} s, einde op {e:.1f} s")
print("fouten in de browser:", fouten or "geen")
