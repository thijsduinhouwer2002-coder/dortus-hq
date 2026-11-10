"""Pro-poster maken uit de echte Blender-opname (e2e/scherm_pro.py op de workflow, tak schermen):
    python3 render.py <pro-knie.json> <13-pro-knie-schoon-x.png> <uit.png>
De gradenboog tekenen we hier in SVG, groot en om de as (straal boog_r_mm uit de json, buiten het been), met de
punten die Blender zelf in beeld projecteerde. Getallen (grens, speling) komen uit de json, nooit met de hand."""
import json
import pathlib
import sys

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

HIER = pathlib.Path(__file__).resolve().parent
VAK_B, VAK_H, RUIM_B, RUIM_H = 1000, 760, 900, 680


def onderwerp(png):
    """Kader van alles wat niet de effen achtergrond is (hoekpixel), in pixels van 1920x1080."""
    px = np.asarray(Image.open(png).convert("RGB")).astype(int)
    anders = np.abs(px - px[5, 5]).sum(axis=2) > 18
    ys, xs = np.nonzero(anders)
    return xs.min(), ys.min(), xs.max(), ys.max()


def svg(d, s):
    c = np.array(d["centrum"])
    boog = np.array(d["boog"])
    w = 1.0 / s
    pt = lambda p: f"{p[0]:.1f},{p[1]:.1f}"  # noqa: E731
    delen = [f'<polygon points="{pt(c)} {" ".join(pt(p) for p in boog)}" fill="rgba(255,255,255,.10)"/>',
             f'<polyline points="{" ".join(pt(p) for p in boog)}" fill="none" stroke="#fff" stroke-width="{4*w:.2f}" '
             f'stroke-linecap="round"/>']
    for g in range(0, len(boog), 5):
        p = boog[g]
        q = p + (p - c) * 0.07
        delen.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#fff" '
                     f'stroke-width="{2.5*w:.2f}"/>')
    for p, dik in ((boog[0], 2.5), (boog[-1], 3.5)):
        delen.append(f'<line x1="{c[0]:.1f}" y1="{c[1]:.1f}" x2="{p[0]:.1f}" y2="{p[1]:.1f}" stroke="rgba(255,255,255,.75)" '
                     f'stroke-width="{dik*w:.2f}" stroke-dasharray="{8*w:.1f} {6*w:.1f}"/>')
    pe = np.array(d["pose_eind"])
    delen.append(f'<line x1="{c[0]:.1f}" y1="{c[1]:.1f}" x2="{pe[0]:.1f}" y2="{pe[1]:.1f}" stroke="#3BE6B0" '
                 f'stroke-width="{5*w:.2f}" stroke-linecap="round"/>')
    delen.append(f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{6*w:.1f}" fill="#3BE6B0"/>')
    for p, tekst in ((boog[0], "0°"), (boog[-1], f'{d["grens"]}°')):
        r = p - c
        q = p + r / np.linalg.norm(r) * 46 * w
        delen.append(f'<text x="{q[0]:.1f}" y="{q[1]:.1f}" fill="#fff" font-family="Inter" font-weight="700" '
                     f'font-size="{34*w:.1f}" text-anchor="middle" dominant-baseline="middle" '
                     f'paint-order="stroke" stroke="rgba(18,19,23,.85)" stroke-width="{6*w:.1f}">{tekst}</text>')
    return '<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">' + "".join(delen) + "</svg>"


def main(js, png, uit):
    d = json.loads(pathlib.Path(js).read_text())
    x0, y0, x1, y1 = onderwerp(png)
    boog = np.array(d["boog"])
    x0, y0 = min(x0, boog[:, 0].min() - 60), min(y0, boog[:, 1].min() - 60)
    x1, y1 = max(x1, boog[:, 0].max() + 60), max(y1, boog[:, 1].max() + 60)
    s = min(RUIM_B / (x1 - x0), RUIM_H / (y1 - y0))
    tx, ty = VAK_B / 2 - s * (x0 + x1) / 2, VAK_H / 2 - s * (y0 + y1) / 2
    html = (HIER / "poster.html").read_text()
    html = html.replace("TRANSFORM", f"translate({tx:.1f}px,{ty:.1f}px) scale({s:.4f})")
    html = html.replace("SCHERM", pathlib.Path(png).resolve().as_uri()).replace("BOOG_SVG", svg(d, s))
    html = html.replace("GRENS", str(d["grens"])).replace("SPELING", f'{d["speling_mm"]:.1f}')
    tijdelijk = HIER / "_poster_gevuld.html"
    tijdelijk.write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto(tijdelijk.as_uri())
        pg.wait_for_timeout(1500)
        pg.screenshot(path=uit)
        b.close()
    tijdelijk.unlink()
    print(f"poster {uit}: schaal {s:.3f}, onderwerp {x0},{y0} tot {x1},{y1}, grens {d['grens']}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
