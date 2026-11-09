"""Maakt richtingen.css: drie richtingen voor de betaalde skins van Rollwright (Daan, 9 nov 2026).
Prototype voor de keuze van Thijs, geen plugincode. Elke richting = een eigen wereld:
achtergrond rond de worp, eigen letter, eigen kleuren, eigen vorm van het token, eigen Roll log,
en de optie "icoon bij een worp" (de gebruiker kiest zelf een icoon, hier wolf en val).
Letters: Alegreya SC, Uncial Antiqua, UnifrakturMaguntia, Spectral (SIL Open Font License 1.1).
Iconen: wolf-head en jaw-trap van game-icons.net (Lorc en Delapouite, CC BY 3.0)."""
import base64, pathlib, re, urllib.parse

HIER = pathlib.Path(__file__).parent
VAULT = HIER.parent.parent / "vaults" / "ontwerp"

def font(naam, bestand):
    b = base64.b64encode((HIER / bestand).read_bytes()).decode()
    return f'@font-face {{ font-family: "{naam}"; src: url(data:font/woff2;base64,{b}) format("woff2"); font-display: block; }}\n'

def svg_uri(bestand, kleur="#000"):
    s = (VAULT / bestand).read_text()
    s = re.sub(r'fill="[^"]*"', f'fill="{kleur}"', s)
    return "url(\"data:image/svg+xml;utf8," + urllib.parse.quote(s) + "\")"

def ruis(freq, oct_, alpha, kleur="0 0 0"):
    s = (f"<svg xmlns='http://www.w3.org/2000/svg' width='320' height='320'><filter id='n'>"
         f"<feTurbulence type='fractalNoise' baseFrequency='{freq}' numOctaves='{oct_}' stitchTiles='stitch'/>"
         f"<feColorMatrix values='0 0 0 0 {kleur.split()[0]} 0 0 0 0 {kleur.split()[1]} 0 0 0 0 {kleur.split()[2]} 0 0 0 {alpha} 0'/></filter>"
         f"<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
    return "url(\"data:image/svg+xml;utf8," + s.replace("<", "%3C").replace(">", "%3E").replace("\"", "'") + "\")"

WOLF = svg_uri("wolf-head.svg")
TRAP = svg_uri("jaw-trap.svg")
HOUT = ruis("0.012 0.22", 4, 0.55, "0.12 0.06 0.02")
STEEN = ruis("0.035", 5, 0.5, "0 0 0")
VELIJN = ruis("0.6", 2, 0.10, "0.4 0.3 0.1")

css = "/* Rollwright skins, drie richtingen (prototype Daan, 9 nov 2026). Zie maak.py. */\n"
css += font("RX Alegreya SC", "alegreya.woff2") + font("RX Uncial", "uncial.woff2")
css += font("RX Fraktur", "fraktur.woff2") + font("RX Spectral", "spectral.woff2")

T = '.rollwright-roll:not(.rollwright-skin-preview-roll)'
NOTE = '.markdown-preview-view.richting'
SHEET = NOTE + ' .markdown-preview-sizer'
VIEW = '.workspace-leaf-content[data-type="markdown"] .view-content'

# Gemeenschappelijk: icoon-optie en vlakke basis, zodat elke wereld van nul begint.
css += f"""
body[class*="rwx-"] {NOTE} .inline-title {{ display: none; }}
body[class*="rwx-"] {SHEET} {{ max-width: 780px; margin: 22px auto 30px !important; padding: 26px 58px 34px !important; min-height: auto !important; border-radius: 4px; }}
body[class*="rwx-"] {NOTE} {{ --font-text-size: 18px; --line-height-normal: 1.6; }}
body[class*="rwx-"] {T} {{ position: relative; isolation: isolate; box-shadow: none !important; animation: none; }}
body[class*="rwx-"] {T} .rollwright-stamp {{ box-shadow: none !important; }}
body[class*="rwx-"] {T}.rwx-ico::after {{ content: "" !important; position: static !important; display: inline-block !important; opacity: 1 !important; width: 1.3em; height: 1.3em; margin-left: .4em; vertical-align: -0.28em; animation: none !important;
  -webkit-mask: var(--rwx-ico) center / contain no-repeat; background: currentColor; }}
body[class*="rwx-"] {T}.rwx-ico-wolf {{ --rwx-ico: {WOLF}; }}
body[class*="rwx-"] {T}.rwx-ico-trap {{ --rwx-ico: {TRAP}; }}
body[class*="rwx-"] {NOTE} .callout {{ position: relative; overflow: visible !important; }}
body[class*="rwx-"] {NOTE} .callout-content, body[class*="rwx-"] {NOTE} p {{ overflow: visible !important; }}
body[class*="rwx-"] {T}.rollwright-crit, body[class*="rwx-"] {T}.rollwright-fumble {{ animation: none !important; }}
body[class*="rwx-"] {NOTE} .metadata-container, body[class*="rwx-"] {NOTE} .frontmatter-container {{ display: none !important; }}
body[class*="rwx-"] .view-header-title {{ color: var(--rwx-kop, #e8d8b8) !important; }}
body[class*="rwx-"] {NOTE} .callout[data-callout="beast"]::after,
body[class*="rwx-"] {NOTE} .callout[data-callout="trap"]::after {{ content: ""; position: absolute; right: 16px; top: 50%; translate: 0 -50%; width: 84px; height: 84px;
  -webkit-mask: var(--rwx-ico) center / contain no-repeat; background: var(--rwx-ico-kleur, currentColor); opacity: .9; }}
body[class*="rwx-"] {NOTE} .callout[data-callout="beast"] {{ --rwx-ico: {WOLF}; padding-right: 116px; }}
body[class*="rwx-"] {NOTE} .callout[data-callout="trap"] {{ --rwx-ico: {TRAP}; padding-right: 116px; }}
body[class*="rwx-"] {NOTE} .callout-icon {{ display: none; }}
"""

# ---------------- A. De Taverne: eikenhout, messing, kaarslicht ----------------
A = "body.rwx-taverne"
css += f"""
{A} {{ --rwx-ico-kleur: #d9a441; }}
{A} {VIEW}, {A} .workspace-leaf-content[data-type="rollwright-history"] .view-content {{
  background: radial-gradient(ellipse 55% 50% at 50% 30%, rgba(255,175,80,.42), rgba(255,140,40,.12) 55%, transparent 75%), {HOUT}, linear-gradient(90deg,#2a1608,#3b2010 20%,#2c170a 45%,#3d2211 70%,#26140a); }}
{A} .view-header, {A} .workspace-tab-header-container {{ background: #1a0d05 !important; }}
{A} {NOTE} {{ --text-normal: #f3dfbd; --text-muted: #c9a77a; --bold-color: #ffd98a; --h1-font: "RX Alegreya SC"; --font-text: "RX Spectral", Georgia, serif; color: var(--text-normal); }}
{A} {SHEET} {{ background: linear-gradient(180deg, rgba(30,14,5,.86), rgba(22,10,4,.92)); border: 1px solid #6e4a22;
  box-shadow: 0 0 0 5px #23120a, 0 0 0 6px #b0823f, 0 26px 70px rgba(0,0,0,.65), inset 0 0 60px rgba(255,160,60,.08); }}
{A} {NOTE} h1 {{ font-family: "RX Alegreya SC"; font-size: 2.5em; color: #f0c26a; text-align: center; letter-spacing: .04em; margin: .1em 0 0;
  text-shadow: 0 2px 0 #3a1d08, 0 0 24px rgba(255,170,60,.35); }}
{A} {NOTE} h1 + p {{ text-align: center; color: #c9a77a; }}
{A} {NOTE} .callout {{ background: rgba(255,200,120,.06); border: 1px solid #6e4a22; border-left: 4px solid #c08a3e; border-radius: 3px; }}
{A} {NOTE} .callout-title {{ font-family: "RX Alegreya SC"; color: #f0c26a; letter-spacing: .03em; font-size: 1.1em; }}
{A} {T} {{ font-family: "RX Alegreya SC"; color: #2b1606 !important; padding: .1em .6em .12em .48em !important; border-radius: 999px !important;
  background: radial-gradient(ellipse at 35% 25%, #fff1c4 0%, #e8b955 28%, #b07a26 62%, #7a4d14 100%) !important;
  border: 1px solid #5a3608 !important; box-shadow: inset 0 1px 0 rgba(255,255,255,.6), inset 0 -2px 3px rgba(80,40,0,.45), 0 2px 0 #3a2006, 0 4px 10px rgba(0,0,0,.5) !important;
  text-shadow: 0 1px 0 rgba(255,235,180,.7); }}
{A} {T} .rollwright-icon {{ color: #4a2808 !important; filter: drop-shadow(0 1px 0 rgba(255,240,190,.6)); }}
{A} {T} .rollwright-value {{ font-size: 1.12em; font-weight: 700; }}
{A} {T}.rollwright-crit {{ background: radial-gradient(ellipse at 35% 25%, #ffffff 0%, #ffe27a 22%, #f5b81c 55%, #a86a00 100%) !important;
  box-shadow: inset 0 1px 0 #fff, 0 2px 0 #3a2006, 0 0 0 2px rgba(255,215,90,.55), 0 0 22px 6px rgba(255,170,40,.65), 0 0 60px 14px rgba(255,120,20,.35) !important; }}
{A} {T}.rollwright-fumble {{ background: radial-gradient(ellipse at 35% 25%, #d9b9a0, #8a5a3e 45%, #4a2414) !important; color: #1a0802 !important;
  box-shadow: inset 0 -2px 3px rgba(0,0,0,.5), 0 2px 0 #1a0802, 0 0 16px 3px rgba(150,20,10,.55) !important; }}
{A} {T} .rollwright-stamp {{ font-family: "RX Alegreya SC" !important; background: #7a1a0c !important; color: #ffe2a0 !important; border: 1px solid #ffcf6a !important; border-radius: 3px !important; rotate: -8deg; }}
{A} .rollwright-history {{ --text-normal: #f3dfbd; --text-muted: #c9a77a; color: #f3dfbd; font-family: "RX Spectral", Georgia, serif; }}
{A} .rollwright-history-item {{ background: rgba(20,9,3,.6) !important; border: 1px solid #6e4a22 !important; border-radius: 3px !important; }}
{A} .rollwright-history-result {{ font-family: "RX Alegreya SC"; color: #f0c26a !important; }}
{A} .rollwright-history-group-title, {A} .rollwright-history-name {{ font-family: "RX Alegreya SC"; color: #e8c58a !important; }}
"""

# ---------------- B. De Kerker: koude steen, gebeitelde runen, sintels ----------------
B = "body.rwx-kerker"
css += f"""
{B} {{ --rwx-ico-kleur: #ff7a2a; }}
{B} {VIEW}, {B} .workspace-leaf-content[data-type="rollwright-history"] .view-content {{
  background: radial-gradient(ellipse 70% 50% at 50% 110%, rgba(255,90,20,.28), transparent 70%), {STEEN}, linear-gradient(160deg,#2b2f2e,#1a1d1d 55%,#121414); }}
{B} .view-header, {B} .workspace-tab-header-container {{ background: #0d0f0f !important; }}
{B} {NOTE} {{ --text-normal: #d7dcd6; --text-muted: #8f9a93; --bold-color: #ffb27a; --font-text: "RX Spectral", Georgia, serif; color: var(--text-normal); }}
{B} {SHEET} {{ background: {STEEN}, linear-gradient(180deg,#3a3f3d,#2a2e2d); border: 1px solid #555d59;
  box-shadow: inset 0 2px 0 rgba(255,255,255,.08), inset 0 -3px 0 rgba(0,0,0,.4), 0 0 0 6px #151717, 0 0 0 7px #4a514e, 0 30px 80px rgba(0,0,0,.75); }}
{B} {NOTE} h1 {{ font-family: "RX Uncial"; font-size: 2.6em; text-align: center; margin: .05em 0 0; color: #ffb36a;
  text-shadow: 0 -1px 0 #000, 0 0 10px rgba(255,120,30,.75), 0 0 34px rgba(255,80,10,.45); }}
{B} {NOTE} h1 + p {{ text-align: center; }}
{B} {NOTE} .callout {{ background: rgba(0,0,0,.42) !important; border: 1px solid #4e5652; border-radius: 2px; box-shadow: inset 0 2px 6px rgba(0,0,0,.6), 0 1px 0 rgba(255,255,255,.07); }}
{B} {NOTE} .callout-title {{ font-family: "RX Uncial"; color: #ff9a55; font-size: 1.12em; text-shadow: 0 0 10px rgba(255,100,20,.45); }}
{B} {T} {{ font-family: "RX Uncial"; color: #e7ece7 !important; padding: .12em .7em .14em .55em !important; border-radius: 2px !important;
  background: {STEEN}, linear-gradient(180deg,#5b625f,#3b403e) !important; border: none !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.25), inset 0 -2px 0 rgba(0,0,0,.55) !important; text-shadow: 0 -1px 0 #000, 0 1px 0 rgba(255,255,255,.15); }}
{B} {T} .rollwright-value {{ font-size: 1.12em; }}
{B} {T} .rollwright-icon {{ color: #ff8a3a !important; filter: drop-shadow(0 0 4px rgba(255,110,30,.8)); }}
{B} {T}.rollwright-crit {{ color: #fff3c0 !important; background: radial-gradient(ellipse at 50% 120%, rgba(255,200,60,.95), rgba(255,120,20,.55) 45%, transparent 75%), {STEEN}, linear-gradient(180deg,#5b625f,#2f3331) !important;
  text-shadow: 0 0 6px #ffb020, 0 0 14px #ff7a00; }}
{B} {T}.rollwright-crit .rollwright-value {{ color: #ffe07a; }}
{B} {T}.rollwright-fumble {{ color: #ff8a70 !important; background-color: #151717 !important; background-image:
  linear-gradient(104deg, transparent 4%, #ff4a1c 5.5%, #ffb070 6.5%, #ff4a1c 7.5%, transparent 9%), linear-gradient(72deg, transparent 92%, #ff4a1c 93.5%, transparent 95%),
  radial-gradient(ellipse at 50% 50%, rgba(255,60,20,.28), transparent 70%), linear-gradient(180deg,#26292a,#0f1111) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.12), 0 0 14px rgba(255,50,20,.45) !important; text-shadow: 0 0 8px rgba(255,40,20,.8); }}
{B} {T} .rollwright-stamp {{ font-family: "RX Uncial" !important; background: #1b1d1d !important; color: #ffb36a !important; border: 1px solid #ff8a3a !important; border-radius: 1px !important; }}
{B} .rollwright-history {{ color: #d7dcd6; font-family: "RX Spectral", Georgia, serif; }}
{B} .rollwright-history-item {{ background: rgba(0,0,0,.35) !important; border: none !important; border-left: 2px solid #ff7a2a !important; border-radius: 0 !important; box-shadow: inset 0 1px 4px rgba(0,0,0,.6) !important; }}
{B} .rollwright-history-result {{ font-family: "RX Uncial"; color: #ffb36a !important; }}
{B} .rollwright-history-group-title, {B} .rollwright-history-name {{ font-family: "RX Uncial"; color: #c8d0cb !important; }}
"""

# ---------------- C. De Hofcodex: velijn, lapis, vermiljoen, bladgoud ----------------
C = "body.rwx-codex"
css += f"""
{C} {{ --rwx-ico-kleur: #1f3f8f; --rwx-kop: #e9d79a; }}
{C} .workspace-tab-header.is-active, {C} .workspace-tab-header.is-active .workspace-tab-header-inner-title {{ background: #1a2550 !important; color: #e9d79a !important; }}
{C} {VIEW}, {C} .workspace-leaf-content[data-type="rollwright-history"] .view-content {{
  background: radial-gradient(ellipse at 50% 0%, #2a3a6e, #121a36 70%); }}
{C} .view-header, {C} .workspace-tab-header-container {{ background: #0e1430 !important; }}
{C} {NOTE} {{ --text-normal: #2a1d14; --text-muted: #6b5644; --bold-color: #a8231a; --font-text: "RX Spectral", Georgia, serif; --background-primary: #f6eedb; color: var(--text-normal); }}
{C} {SHEET} {{ background: {VELIJN}, linear-gradient(180deg,#fbf5e6,#efe4c8); border: 1px solid #c9b48a;
  box-shadow: inset 0 0 0 10px #fbf5e6, inset 0 0 0 11px #b8892a, inset 0 0 0 14px #fbf5e6, inset 0 0 0 15px #1f3f8f, 0 30px 80px rgba(0,0,20,.6); padding: 40px 64px 40px !important; }}
{C} {NOTE} h1 {{ font-family: "RX Fraktur"; font-size: 2.7em; text-align: center; color: #1f3f8f; margin: .05em 0 0; font-weight: 400; }}
{C} {NOTE} h1::first-letter {{ color: #a8231a; font-size: 1.35em; text-shadow: 1px 1px 0 #d9a830; }}
{C} {NOTE} h1 + p {{ text-align: center; color: #a8231a; }}
{C} {NOTE} .rollwright-roll {{ margin-left: .25em; }}
{C} {NOTE} .callout {{ background: rgba(31,63,143,.05); border: none; border-top: 2px solid #1f3f8f; border-bottom: 2px solid #1f3f8f; border-radius: 0; }}
{C} {NOTE} .callout-title {{ font-family: "RX Fraktur"; color: #a8231a; font-size: 1.3em; font-weight: 400; }}
{C} {T} {{ font-family: "RX Fraktur"; color: #fbf5e6 !important; padding: .1em .62em .14em .5em !important; border-radius: 2px !important;
  background: linear-gradient(180deg,#2c55b8,#1a3683) !important; border: 1.5px solid #c99a2e !important;
  box-shadow: 0 0 0 2px #fbf5e6, 0 0 0 3px #a8231a !important; }}
{C} {T} .rollwright-icon {{ color: #f0c544 !important; }}
{C} {T} .rollwright-value {{ font-size: 1.15em; }}
{C} {T}.rollwright-crit {{ color: #4a2a00 !important; background: linear-gradient(135deg,#fff3b0 0%,#e8b730 30%,#fff0a0 48%,#c88f12 70%,#f5d55a 100%) !important; border-color: #8a5a08 !important;
  box-shadow: 0 0 0 2px #fbf5e6, 0 0 0 3px #1f3f8f, 0 0 0 5px #fbf5e6, 0 0 0 6px #a8231a !important; }}
{C} {T}.rollwright-crit .rollwright-icon {{ color: #a8231a !important; }}
{C} {T}.rollwright-fumble {{ background: linear-gradient(180deg,#c0392b,#7f1d14) !important; border-color: #3a0d08 !important; }}
{C} .workspace-tab-header.is-active::before, {C} .workspace-tab-header.is-active::after {{ display: none !important; }}
{C} .rollwright-history-group-title {{ font-family: "RX Spectral" !important; font-variant: small-caps; font-size: 1em !important; }}
{C} {T} .rollwright-stamp {{ font-family: "RX Spectral" !important; font-weight: 700; background: #a8231a !important; color: #fbf5e6 !important; border: 1px solid #c99a2e !important; border-radius: 50% !important; }}
{C} .rollwright-history {{ color: #2a1d14; font-family: "RX Spectral", Georgia, serif; }}
{C} .workspace-leaf-content[data-type="rollwright-history"] .view-content {{ background: {VELIJN}, #f6eedb !important; }}
{C} .rollwright-history-item {{ background: transparent !important; border: none !important; border-bottom: 1px solid #c9b48a !important; border-radius: 0 !important; }}
{C} .rollwright-history-result {{ font-family: "RX Fraktur"; color: #1f3f8f !important; font-size: 1.2em; }}
{C} .rollwright-history-name {{ font-family: "RX Fraktur"; color: #a8231a !important; text-transform: none !important; letter-spacing: 0 !important; font-size: 1.15em; }}
"""

(HIER / "richtingen.css").write_text(css)
print(len(css))
