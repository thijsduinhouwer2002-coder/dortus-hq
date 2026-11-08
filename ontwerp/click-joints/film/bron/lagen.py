"""Rendert de lagen van het filmpje naar PNG (transparant waar nodig). Gebruik: python3 lagen.py <uitmap>"""
import sys, pathlib
from playwright.sync_api import sync_playwright
uit = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "."); uit.mkdir(parents=True, exist_ok=True)
src = (pathlib.Path(__file__).parent / "film.html").resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    for laag in ["bg", "rand", "masker", "kop1", "kop2", "kop3", "kop4", "eind"]:
        pg.goto(f"{src}?laag={laag}"); pg.wait_for_timeout(1200)
        pg.screenshot(path=str(uit / f"{laag}.png"), omit_background=laag not in ("bg", "masker", "eind"))
    b.close()
