import sys, pathlib
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1920,'height':1080})
    pg.goto(pathlib.Path(src).resolve().as_uri()); pg.wait_for_timeout(1500)
    pg.screenshot(path=out); b.close()
