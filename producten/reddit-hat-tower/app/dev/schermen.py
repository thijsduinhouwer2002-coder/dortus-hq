"""Speelt Gloop's Hat Tower in een telefoonbrowser en maakt schermbeelden en een filmpje.

Gebruik (lokale server moet draaien: PROEF=1 npm run local):
    python3 dev/schermen.py <uitmap> [--breed]

De speler mikt op de bek zoals een mens: hij kijkt naar de stand en tikt als de held laag genoeg is,
met wat spreiding en af en toe te laat, zodat ook "bye!" en een gele vangst in beeld komen.
"""
import random
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

UIT = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/gloop-schermen")
BREED = "--breed" in sys.argv
UIT.mkdir(parents=True, exist_ok=True)
BASIS = "http://localhost:5173"
random.seed(4)
NAAM = "you" + str(int(time.time()) % 100000)


def stand(pagina):
    return pagina.evaluate("window.gloopProef && window.gloopProef()")


SPELER_JS = """
(() => {
  // Speelt in de pagina zelf, zodat de tik op het goede moment valt (geen vertraging van Playwright).
  let held = -1, doel = 9999, laat = false
  const canvas = document.getElementById('canvas')
  function f() {
    const s = window.gloopProef()
    if (s.toestand === 5) return
    if (s.held !== held) {
      held = s.held
      doel = 815 + (Math.random() * 2 - 1) * 40
      laat = Math.random() < 0.12
    }
    if (s.toestand === 1 && !laat && s.y >= doel) {
      canvas.dispatchEvent(new PointerEvent('pointerdown', {bubbles: true, clientX: 200, clientY: 300}))
      doel = 9999
    }
    requestAnimationFrame(f)
  }
  requestAnimationFrame(f)
})()
"""


def speel(pagina, beelden, film_naam):
    """Speelt één ronde. Maakt onderweg beelden van een slok en van "bye!"."""
    pagina.evaluate(SPELER_JS)
    begin = time.time()
    gezien = set()
    while time.time() - begin < 40:
        s = stand(pagina)
        if not s or s["toestand"] == 5:
            break
        if s["toestand"] == 2 and s["held"] in (4, 9, 15) and s["held"] not in gezien:
            gezien.add(s["held"])
            time.sleep(0.06)
            pagina.screenshot(path=str(UIT / f"{film_naam}-slok-{s['held']}.png"))
            beelden.append(f"slok-{s['held']}")
        if s["toestand"] == 3 and "bye" not in beelden:
            time.sleep(0.25)
            pagina.screenshot(path=str(UIT / f"{film_naam}-bye.png"))
            beelden.append("bye")
        time.sleep(0.01)


with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--autoplay-policy=no-user-gesture-required"])
    if BREED:
        maat = {"viewport": {"width": 1280, "height": 760}, "device_scale_factor": 1}
    else:
        maat = {"viewport": {"width": 390, "height": 780}, "device_scale_factor": 3, "is_mobile": True, "has_touch": True}

    # De post in de feed.
    ctx = browser.new_context(**({"viewport": {"width": 390, "height": 512}, "device_scale_factor": 3} if not BREED else maat))
    pagina = ctx.new_page()
    pagina.goto(f"{BASIS}/splash.html?u={NAAM}")
    pagina.wait_for_selector("body.klaar")
    time.sleep(0.4)
    pagina.screenshot(path=str(UIT / "1-feed-post.png"))
    ctx.close()

    # Het spel, met filmpje.
    ctx = browser.new_context(**maat, record_video_dir=str(UIT / "film"), record_video_size={"width": 390, "height": 780} if not BREED else {"width": 1280, "height": 760})
    pagina = ctx.new_page()
    fouten = []
    pagina.on("pageerror", lambda e: fouten.append(str(e)))
    pagina.on("console", lambda m: fouten.append(m.text) if m.type == "error" else None)
    pagina.goto(f"{BASIS}/game.html?proef=1&u={NAAM}")
    pagina.wait_for_selector("body.klaar")
    time.sleep(0.6)
    pagina.screenshot(path=str(UIT / "2-start.png"))
    pagina.click("#knop-speel")
    beelden = []
    speel(pagina, beelden, "3")
    time.sleep(1.6)
    pagina.screenshot(path=str(UIT / "4-uitslag.png"))
    try:
        pagina.click("#knop-reactie", timeout=5000)
    except Exception as e:  # noqa: BLE001
        fouten.append(f"knop-reactie: {e}")
    time.sleep(0.5)
    pagina.screenshot(path=str(UIT / "5-gedeeld.png"))
    pagina.evaluate("document.getElementById('einde').scrollTop = 99999")
    time.sleep(0.3)
    pagina.screenshot(path=str(UIT / "5b-uitslag-onder.png"))
    # Terug naar het startscherm: nu met de eigen uitslag.
    pagina.click("#knop-terug", timeout=5000)
    time.sleep(0.4)
    pagina.screenshot(path=str(UIT / "6-start-na.png"))
    ctx.close()
    browser.close()

print("beelden:", sorted(p.name for p in UIT.glob("*.png")))
print("film:", [str(p) for p in (UIT / "film").glob("*.webm")])
print("fouten in de browser:", fouten or "geen")
