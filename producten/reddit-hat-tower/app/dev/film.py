"""Maakt het inzendfilmpje: 1080x1920 echt (beeld voor beeld op 3x), ±33 s, met geluid.

Gebruik (lokale server moet draaien: PROEF=1 npm run local):
    python3 dev/film.py <uit.mp4>

Hoe: met ?film=1 loopt het spel op een eigen klok (src/client/filmklok.ts). Dit script zet de klok
telkens 1/30 s verder (in 4 stapjes, zodat de speler precies kan mikken) en maakt dan een
schermbeeld op 360x640 bij 3x, dus echt 1080x1920. De klanken van het spel worden met hun tijd
onthouden en achteraf tot een WAV gerenderd. Het filmpje begint meteen met de ronde, een stuk uit
het midden gaat eruit, en de Engelse teksten komen er met ffmpeg overheen.
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
FPS = 30
SPELER = re.search(r'SPELER_JS = """(.*?)"""', (APP / "dev/schermen.py").read_text(), re.S).group(1)
# Voor het filmpje mikt de speler iets beter (zoals iemand die het spel kent).
SPELER = SPELER.replace("* 40", "* 22").replace("< 0.12", "< 0.04")
# Het stuk uit het midden van de ronde dat eruit gaat (seconden vanaf de start), zodat het ±33 s wordt.
KNIP = (12.0, 18.0)

ruw = WERK / "ruw.mp4"
enc = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "png", "-i", "-",
     "-c:v", "libx264", "-preset", "veryfast", "-crf", "10", "-pix_fmt", "yuv420p", str(ruw)],
    stdin=subprocess.PIPE,
)
with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path="/usr/bin/google-chrome")
    ctx = browser.new_context(viewport={"width": 360, "height": 640}, device_scale_factor=3, is_mobile=True, has_touch=True)
    pagina = ctx.new_page()
    fouten = []
    pagina.on("pageerror", lambda e: fouten.append(str(e)))
    pagina.goto(f"http://localhost:5173/game.html?proef=1&film=1&u=speler{int(time.time()) % 100000}")
    pagina.wait_for_selector("body.klaar")
    pagina.evaluate("gloopFilmStap(100)")
    pagina.click("#knop-speel")
    t0 = pagina.evaluate("performance.now()")
    pagina.evaluate(SPELER)
    beelden = 0
    t_einde = None
    t_vel = None
    while True:
        pagina.evaluate(f"gloopFilmStap({1000 / FPS}, 4)")
        enc.stdin.write(pagina.screenshot(type="png"))
        beelden += 1
        nu = pagina.evaluate("performance.now()")
        if t_einde is None and pagina.evaluate("window.gloopProef().toestand") == 5:
            t_einde = nu
        if t_einde is not None and t_vel is None and pagina.evaluate("!document.getElementById('einde').hidden"):
            t_vel = nu
        if t_vel is not None and nu - t_vel > 4800:
            break
        if beelden > FPS * 60:
            raise SystemExit("ronde liep niet af")
        if beelden % 150 == 0:
            print(f"{beelden} beelden", flush=True)
    duur = beelden / FPS
    wav = pagina.evaluate(f"window.gloopFilmGeluid({t0}, {duur + 0.5})")
    (WERK / "geluid.wav").write_bytes(base64.b64decode(wav))
    ctx.close()
    browser.close()
enc.stdin.close()
enc.wait()

e = (t_einde - t0) / 1000
a, b = KNIP


def na(t):
    """Tijd in het ingekorte filmpje (met de overgang op de knip)."""
    return t if t <= a else t - (b - a) - 0.3


OVER = 0.3  # korte overgang op de knip


def tekst(s, van, tot, grootte=66, y="h*0.17", kleur="white", x="(w-text_w)/2"):
    return (
        f"drawtext=fontfile={LETTER}:text='{s}':fontsize={grootte}:fontcolor={kleur}:borderw=9:bordercolor=0x2b1206:"
        f"x={x}:y={y}:enable='between(t,{van:.2f},{tot:.2f})'"
    )


knip = a - OVER  # in het ingekorte filmpje begint het tweede stuk hier (overgang van OVER s)
t_vel_s = (t_vel - t0) / 1000
lengte = duur - (b - a) - OVER
slot = lengte - 2.2  # laatste 2,2 s: de eindkaart
rechts = "w-text_w-50"  # titel rechts, zodat de eerste held (van links) niet over de G valt
teksten = [
    tekst("Gloop's Hat Tower".replace("'", "\u2019"), 0.0, 2.4, 100, "h*0.13", "0x6fe0b0", rechts),
    tekst("a daily game on Reddit", 0.0, 2.4, 56, "h*0.13+120", "white", rechts),
    tekst("One tap. 30 seconds.", 2.6, 6.0),
    tekst("Perfect gulps stack more hats", 6.6, knip),
    tekst("Same tower for everyone today", knip + OVER, knip + OVER + 4.2),
    tekst("Every subreddit builds one tower", knip + OVER + 4.8, na(e) - 0.4),
    tekst("Share your run.", na(t_vel_s) - OVER + 0.2, slot, 64, "h*0.05"),
]
eindkaart = (
    f"drawbox=x=0:y=0:w=iw:h=ih:color=0x24110a@0.78:t=fill:enable='gte(t,{slot:.2f})',"
    + tekst("New tower every day", slot + 0.1, lengte, 84, "h*0.40", "white")
    + ","
    + tekst("on r/GloopsHatTower", slot + 0.1, lengte, 92, "h*0.40+120", "0x6fe0b0")
)
filter_complex = (
    f"[0:v]trim=0:{a},setpts=PTS-STARTPTS[v1];[0:v]trim={b}:{duur},setpts=PTS-STARTPTS[v2];"
    f"[1:a]atrim=0:{a},asetpts=PTS-STARTPTS[a1];[1:a]atrim={b}:{duur},asetpts=PTS-STARTPTS[a2];"
    f"[v1][v2]xfade=transition=fade:duration={OVER}:offset={knip:.3f}[v];"
    f"[a1][a2]acrossfade=d={OVER}[au];[v]{','.join(teksten)},{eindkaart}[vt]"
)
subprocess.run(
    ["ffmpeg", "-v", "error", "-y", "-i", str(ruw), "-i", str(WERK / "geluid.wav"),
     "-filter_complex", filter_complex, "-map", "[vt]", "-map", "[au]",
     "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(UIT)],
    check=True,
)
for f in WERK.iterdir():
    f.unlink()
WERK.rmdir()
print(f"filmpje: {UIT} ({lengte:.1f} s, {beelden} beelden opgenomen), knip op {knip:.1f} s, einde ronde op {na(e):.1f} s")
print("fouten in de browser:", fouten or "geen")
