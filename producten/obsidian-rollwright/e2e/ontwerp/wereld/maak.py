"""Maakt wereld.css: de skin kleurt de hele notitie (Daan, 9 nov 2026, ontwerp-notitiesfeer.md).
Prototype voor de bouw door Olaf. Alles onder body.rollwright-skin-<skin> .rollwright-world,
waarbij .rollwright-world op view.containerEl van het notitieblad staat (zoals in bouwplan-notitiesfeer.md).
Letters: Cinzel, Cinzel Decorative, IM Fell English, Uncial Antiqua, Spectral (SIL Open Font License 1.1)."""
import base64, pathlib

HIER = pathlib.Path(__file__).parent

def font(naam, bestand, extra=""):
    b = base64.b64encode((HIER / bestand).read_bytes()).decode()
    return f'@font-face {{ font-family: "{naam}"; src: url(data:font/woff2;base64,{b}) format("woff2"); font-display: block; {extra} }}\n'

def ruis(freq, oct_, alpha, kleur="0 0 0"):
    k = kleur.split()
    s = (f"<svg xmlns='http://www.w3.org/2000/svg' width='320' height='320'><filter id='n'>"
         f"<feTurbulence type='fractalNoise' baseFrequency='{freq}' numOctaves='{oct_}' stitchTiles='stitch'/>"
         f"<feColorMatrix values='0 0 0 0 {k[0]} 0 0 0 0 {k[1]} 0 0 0 0 {k[2]} 0 0 0 {alpha} 0'/></filter>"
         f"<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
    return "url(\"data:image/svg+xml;utf8," + s.replace("<", "%3C").replace(">", "%3E").replace("\"", "'") + "\")"

PAPIER_FIJN = ruis("0.9", 2, 0.10, "0.35 0.22 0.08")
PAPIER_VLEK = ruis("0.012", 3, 0.22, "0.55 0.35 0.12")
STEEN = ruis("0.035", 5, 0.5, "0 0 0")

css = "/* Rollwright: de skin kleurt de hele notitie (prototype Daan, 9 nov 2026). Zie maak.py. */\n"
css += font("RW Cinzel", "cinzel.woff2", "font-weight: 400 900;") + font("RW Cinzel Deco", "cinzeldec.woff2", "font-weight: 700;")
css += font("RW Fell", "fell.woff2", "font-style: normal;") + font("RW Fell", "felli.woff2", "font-style: italic;")
css += font("RW Uncial", "uncial.woff2") + font("RW Spectral", "spectral.woff2")

T = '.rollwright-roll:not(.rollwright-skin-preview-roll)'

# ---------------- Parchment: oud papier en inkt, altijd licht ----------------
P = "body.rollwright-skin-parchment .rollwright-world"
css += f"""
{P} {{
  --background-primary: #ead8b2; --background-primary-alt: #e3cfa5; --background-secondary: #e0cb9f;
  --text-normal: #2e1d10; --text-muted: #6b4f35; --text-faint: #8d7356;
  --text-accent: #7a3b1f; --text-accent-hover: #5a2a12;
  --link-color: #7a3b1f; --link-color-hover: #5a2a12; --link-external-color: #7a3b1f; --link-unresolved-color: #9a6a4a;
  --font-text: "RW Fell", Georgia, serif; --font-text-theme: "RW Fell", Georgia, serif; --font-text-size: 19px; --line-height-normal: 1.55;
  --h1-font: "RW Cinzel Deco", serif; --h2-font: "RW Cinzel", serif; --h3-font: "RW Cinzel", serif; --h4-font: "RW Cinzel", serif; --h5-font: "RW Cinzel", serif; --h6-font: "RW Cinzel", serif;
  --h1-color: #4a1f0e; --h2-color: #5a2a12; --h3-color: #5a2a12; --h4-color: #5a2a12; --h5-color: #5a2a12; --h6-color: #5a2a12;
  --inline-title-font: "RW Cinzel Deco", serif; --inline-title-color: #4a1f0e;
  --bold-color: #4a1f0e; --italic-color: #5a3a22;
  --hr-color: #b89a6c; --table-border-color: #b89a6c; --blockquote-border-color: #7a3b1f; --background-modifier-border: #c8ab7c;
  --list-marker-color: #7a3b1f; --checkbox-color: #7a3b1f; --checkbox-border-color: #8d7356;
  --tag-color: #7a3b1f; --tag-background: rgba(122,59,31,.10); --tag-background-hover: rgba(122,59,31,.18);
  --code-background: rgba(90,58,34,.08); --code-normal: #4a1f0e;
  --text-selection: rgba(122,59,31,.22); --caret-color: #4a1f0e;
  --metadata-label-text-color: #6b4f35; --metadata-input-text-color: #2e1d10;
  --callout-title-color: #7a3b1f;
  --callout-blend-mode: normal; --tab-background-active: #dcc595; --titlebar-background-focused: #dcc595;
  color-scheme: light;
}}
{P} .markdown-preview-view, {P} .markdown-rendered, {P} .markdown-source-view, {P} .cm-content, {P} .callout-content {{ color: var(--text-normal); }}
{P} .view-content {{
  background: {PAPIER_FIJN}, {PAPIER_VLEK}, radial-gradient(ellipse 120% 90% at 50% 40%, #f0e0bd 0%, #e6d2a8 55%, #d8bd8a 100%);
  box-shadow: inset 0 0 120px rgba(120,72,24,.42), inset 0 0 18px rgba(90,50,15,.35);
}}
body .workspace-leaf {P} .view-header, {P} .view-header {{ background: #dcc595; border-bottom: 1px solid #b89a6c; }}
{P} .view-header-title, {P} .view-header-breadcrumb {{ font-family: "RW Cinzel", serif; letter-spacing: .06em; color: #4a1f0e; }}
{P} .view-header .clickable-icon {{ color: #6b4f35; }}
{P} .markdown-rendered h1, {P} .HyperMD-header-1, {P} .inline-title {{ text-align: center; font-size: 2.3em; letter-spacing: .02em; }}
{P} .markdown-rendered h1::first-letter, {P} .inline-title::first-letter {{ color: #a8231a; font-size: 1.25em; }}
{P} .markdown-rendered h1 {{ padding-bottom: .3em; border-bottom: 3px double #b89a6c; }}
{P} .markdown-rendered h1 + p {{ text-align: center; }}
{P} .callout {{ --callout-color: 122, 59, 31; background: rgba(255,248,230,.55); border: none; border-left: 3px solid #7a3b1f; border-radius: 2px;
  box-shadow: 0 1px 0 rgba(255,255,255,.5) inset, 0 2px 6px rgba(90,50,15,.18); }}
{P} .callout-title {{ font-family: "RW Cinzel", serif; font-variant: small-caps; letter-spacing: .05em; font-size: .95em; color: #7a3b1f; }}
{P} .callout-icon {{ color: #7a3b1f; }}
{P} {T} {{ font-family: "RW Cinzel", serif; }}
"""

# ---------------- Arcane: donkere steen en vuur, altijd donker ----------------
A = "body.rollwright-skin-arcane .rollwright-world"
css += f"""
{A} {{
  --background-primary: #2a2e2d; --background-primary-alt: #232726; --background-secondary: #1a1d1d;
  --text-normal: #d7dcd6; --text-muted: #8f9a93; --text-faint: #66706b;
  --text-accent: #ff9a55; --text-accent-hover: #ffb36a;
  --link-color: #ff9a55; --link-color-hover: #ffb36a; --link-external-color: #ff9a55; --link-unresolved-color: #c27a4a;
  --font-text: "RW Spectral", Georgia, serif; --font-text-theme: "RW Spectral", Georgia, serif; --font-text-size: 18px; --line-height-normal: 1.6;
  --h1-font: "RW Uncial", serif; --h2-font: "RW Uncial", serif; --h3-font: "RW Uncial", serif; --h4-font: "RW Spectral", serif; --h5-font: "RW Spectral", serif; --h6-font: "RW Spectral", serif;
  --h1-color: #ffb36a; --h2-color: #ff9a55; --h3-color: #ff9a55; --h4-color: #d7dcd6; --h5-color: #d7dcd6; --h6-color: #d7dcd6;
  --inline-title-font: "RW Uncial", serif; --inline-title-color: #ffb36a;
  --bold-color: #ffb27a; --italic-color: #c8d0cb;
  --hr-color: #4e5652; --table-border-color: #4e5652; --blockquote-border-color: #ff7a2a; --background-modifier-border: #3e4542;
  --list-marker-color: #ff7a2a; --checkbox-color: #ff7a2a; --checkbox-border-color: #66706b;
  --tag-color: #ffb36a; --tag-background: rgba(255,122,42,.12); --tag-background-hover: rgba(255,122,42,.2);
  --code-background: rgba(0,0,0,.35); --code-normal: #e7ece7;
  --text-selection: rgba(255,122,42,.28); --caret-color: #ffb36a;
  --metadata-label-text-color: #8f9a93; --metadata-input-text-color: #d7dcd6;
  --callout-title-color: #ff9a55;
  --callout-blend-mode: normal; --tab-background-active: #0d0f0f; --titlebar-background-focused: #0d0f0f;
  color-scheme: dark;
}}
{A} .markdown-preview-view, {A} .markdown-rendered, {A} .markdown-source-view, {A} .cm-content, {A} .callout-content {{ color: var(--text-normal); }}
{A} .view-content {{
  background: radial-gradient(ellipse 70% 45% at 50% 112%, rgba(255,90,20,.30), transparent 70%), {STEEN}, linear-gradient(160deg,#2b2f2e,#1a1d1d 55%,#121414);
  box-shadow: inset 0 0 100px rgba(0,0,0,.55);
}}
body .workspace-leaf {A} .view-header, {A} .view-header {{ background: #0d0f0f; border-bottom: 1px solid #2a2e2d; }}
{A} .view-header-title, {A} .view-header-breadcrumb {{ font-family: "RW Uncial", serif; color: #ffb36a; }}
{A} .view-header .clickable-icon {{ color: #8f9a93; }}
{A} .markdown-rendered h1, {A} .HyperMD-header-1, {A} .inline-title {{ text-align: center; font-size: 2.5em;
  text-shadow: 0 -1px 0 #000, 0 0 10px rgba(255,120,30,.75), 0 0 34px rgba(255,80,10,.45); }}
{A} .markdown-rendered h1 + p {{ text-align: center; }}
{A} .callout {{ --callout-color: 255, 122, 42; background: rgba(0,0,0,.42); border: 1px solid #4e5652; border-radius: 2px;
  box-shadow: inset 0 2px 6px rgba(0,0,0,.6), 0 1px 0 rgba(255,255,255,.07); }}
{A} .callout-title {{ font-family: "RW Uncial", serif; color: #ff9a55; font-size: 1.1em; text-shadow: 0 0 10px rgba(255,100,20,.45); }}
{A} .callout-icon {{ color: #ff7a2a; }}
{A} {T} {{ font-family: "RW Uncial", serif; color: #e7ece7 !important; padding: .12em .7em .14em .55em !important; border-radius: 2px !important;
  background: {STEEN}, linear-gradient(180deg,#5b625f,#3b403e) !important; border: none !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.25), inset 0 -2px 0 rgba(0,0,0,.55) !important; text-shadow: 0 -1px 0 #000, 0 1px 0 rgba(255,255,255,.15); }}
{A} {T} .rollwright-icon {{ color: #ff8a3a !important; filter: drop-shadow(0 0 4px rgba(255,110,30,.8)); }}
{A} {T}.rollwright-crit {{ color: #fff3c0 !important; background: radial-gradient(ellipse at 50% 120%, rgba(255,200,60,.95), rgba(255,120,20,.55) 45%, transparent 75%), {STEEN}, linear-gradient(180deg,#5b625f,#2f3331) !important;
  text-shadow: 0 0 6px #ffb020, 0 0 14px #ff7a00; }}
{A} {T}.rollwright-crit .rollwright-value {{ color: #ffe07a; }}
{A} {T}.rollwright-fumble {{ color: #ff8a70 !important; background-color: #151717 !important; background-image:
  linear-gradient(104deg, transparent 4%, #ff4a1c 5.5%, #ffb070 6.5%, #ff4a1c 7.5%, transparent 9%), linear-gradient(72deg, transparent 92%, #ff4a1c 93.5%, transparent 95%),
  radial-gradient(ellipse at 50% 50%, rgba(255,60,20,.28), transparent 70%), linear-gradient(180deg,#26292a,#0f1111) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.12), 0 0 14px rgba(255,50,20,.45) !important; text-shadow: 0 0 8px rgba(255,40,20,.8); }}
{A} {T} .rollwright-stamp {{ font-family: "RW Uncial", serif !important; background: #1b1d1d !important; color: #ffb36a !important; border: 1px solid #ff8a3a !important; border-radius: 1px !important; }}
"""

# ---------------- ronde d: titelbalk, eigenschappen, oude skins v2 eruit, Roll log per wereld ----------------
H = '.rollwright-history'
css += f"""
/* Titelbalk: een regel van het thema won; met !important binnen de wereld. */
{P} .view-header {{ background: #dcc595 !important; border-bottom: 1px solid #b89a6c !important; }}
{P} .view-header-title, {P} .view-header-title-parent, {P} .view-header-breadcrumb {{ color: #4a1f0e !important; }}
{A} .view-header {{ background: #0d0f0f !important; border-bottom: 1px solid #2a2e2d !important; }}
{A} .view-header-title, {A} .view-header-title-parent, {A} .view-header-breadcrumb {{ color: #ffb36a !important; }}
{P} .metadata-container {{ --font-interface: "RW Fell", Georgia, serif; font-family: "RW Fell", Georgia, serif; color: #2e1d10; }}
{P} .metadata-property-key {{ font-variant: small-caps; letter-spacing: .04em; color: #6b4f35; }}
{A} .metadata-container {{ --font-interface: "RW Spectral", Georgia, serif; font-family: "RW Spectral", Georgia, serif; color: #d7dcd6; }}
{A} .metadata-property-key {{ color: #8f9a93; }}
/* Arcane: geen ijsblauwe of paarse resten van skins v2 meer op de tokens. */
{A} {T} .rollwright-icon::before {{ background: #ff8a3a !important; }}
{A} {T}:not(.rollwright-crit):not(.rollwright-fumble) .rollwright-value, {A} {T}:not(.rollwright-crit):not(.rollwright-fumble) .rollwright-label {{ color: #e7ece7 !important; }}
{A} {T}.rollwright-crit .rollwright-icon::before {{ background: #ffe07a !important; }}
{A} {T}.rollwright-fumble .rollwright-icon::before {{ background: #ff6a4a !important; }}

/* ===== Roll log, Parchment: een kroniek op perkament, inkt en lakzegel ===== */
body.rollwright-skin-parchment {H} {{
  --background-primary: #ead8b2; --background-modifier-border: #c8ab7c; --text-normal: #2e1d10; --text-muted: #6b4f35; --text-faint: #8d7356;
  --rollwright-accent: #7a3b1f; --interactive-accent: #7a3b1f; --text-on-accent: #f6ead0; --interactive-accent-hover: #5a2a12;
  --font-interface: "RW Fell", Georgia, serif; color-scheme: light;
  background: {PAPIER_FIJN}, {PAPIER_VLEK}, linear-gradient(180deg, #efdfbb, #e3cd9f) !important;
  box-shadow: inset 0 0 60px rgba(120,72,24,.35); color: #2e1d10; font-family: "RW Fell", Georgia, serif;
}}
body.rollwright-skin-parchment {H} input {{ background: rgba(255,248,230,.6); border: 1px solid #b89a6c; color: #2e1d10; font-family: "RW Fell", serif; }}
body.rollwright-skin-parchment {H} .rollwright-history-form button {{ background: #7a3b1f; color: #f6ead0; font-family: "RW Cinzel", serif; letter-spacing: .06em; box-shadow: none; }}
body.rollwright-skin-parchment {H} .rollwright-history-clear {{ color: #8d7356 !important; font-style: italic; }}
body.rollwright-skin-parchment {H} .rollwright-history-group-title {{ font-family: "RW Cinzel", serif; font-variant: normal; letter-spacing: .08em; color: #5a2a12;
  border-bottom: 3px double #b89a6c; padding-bottom: .25em; }}
body.rollwright-skin-parchment {H} .rollwright-history-list::before {{ background: none; border-left: 2px dotted #8d7356; width: 0; }}
body.rollwright-skin-parchment {H} .rollwright-history-item {{ background: transparent; border: none; border-bottom: 1px solid rgba(122,82,40,.28); border-radius: 0; box-shadow: none; padding: .35em .2em .55em; }}
body.rollwright-skin-parchment {H} .rollwright-history-item::before {{ background: #6b4f35; filter: none; }}
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-history-latest {{ border: none; border-bottom: 1px solid rgba(122,82,40,.28); box-shadow: none; }}
body.rollwright-skin-parchment {H} .rollwright-history-name {{ font-family: "RW Cinzel", serif; text-transform: none; font-variant: small-caps; font-size: .95em; letter-spacing: .06em; color: #7a3b1f; }}
body.rollwright-skin-parchment {H} .rollwright-history-result {{ font-family: "RW Fell", serif; font-weight: 400; font-size: 1.7em; color: #2e1d10; }}
body.rollwright-skin-parchment {H} .rollwright-history-formula, body.rollwright-skin-parchment {H} .rollwright-history-details {{ font-style: italic; color: #6b4f35; }}
body.rollwright-skin-parchment {H} .rollwright-history-meta {{ font-style: italic; color: #8d7356; font-size: .9em; }}
body.rollwright-skin-parchment {H} .rollwright-history-meta .clickable-icon {{ color: #8d7356; }}
/* NAT 20: het getal in bladgoud met een rode lakzegel als merkteken. */
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-crit {{ background: linear-gradient(90deg, rgba(201,150,40,.16), transparent 80%); }}
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-crit::before {{ -webkit-mask: none; mask: none; border-radius: 50%; width: 1.5em; height: 1.5em; left: -1.85em; top: .5em;
  background: radial-gradient(circle at 38% 32%, #d0453a, #a8231a 55%, #6e140e); box-shadow: 0 1px 2px rgba(60,20,5,.5), inset 0 0 0 2px rgba(255,255,255,.12); filter: none; }}
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-crit .rollwright-history-result {{ color: #8a5a0a; background: linear-gradient(180deg,#e9bf4a,#9a6a12); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; font-size: 2em; }}
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-crit .rollwright-history-name {{ color: #8a5a0a; }}
body.rollwright-skin-parchment {H} .rollwright-history-item .rollwright-stamp {{ font-family: "RW Cinzel", serif !important; background: transparent !important; color: #a8231a !important; border: 1.5px solid #a8231a !important;
  border-radius: 2px !important; transform: rotate(-4deg); box-shadow: none !important; }}
/* NAT 1: een inktvlek, het getal in rode inkt doorgestreept. */
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-fumble::before {{ -webkit-mask: none; mask: none; width: 1.4em; height: 1.2em; left: -1.8em;
  background: radial-gradient(ellipse 50% 45% at 50% 50%, #2a1a10 60%, transparent 62%), radial-gradient(circle at 85% 20%, #2a1a10 18%, transparent 20%), radial-gradient(circle at 15% 85%, #2a1a10 14%, transparent 16%); filter: none; }}
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-fumble .rollwright-history-result {{ color: #a8231a; text-decoration: line-through 2px #a8231a; }}
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-fumble .rollwright-history-name {{ color: #a8231a; }}

/* ===== Roll log, Arcane: stenen tabletten in een kerker, vuur als licht ===== */
body.rollwright-skin-arcane {H} {{
  --background-primary: #2a2e2d; --background-modifier-border: #3e4542; --text-normal: #d7dcd6; --text-muted: #8f9a93; --text-faint: #66706b;
  --rollwright-accent: #ff7a2a; --interactive-accent: #c4521a; --text-on-accent: #fff1e0; --interactive-accent-hover: #e0621f;
  --font-interface: "RW Spectral", Georgia, serif; color-scheme: dark;
  background: radial-gradient(ellipse 120% 40% at 50% 105%, rgba(255,90,20,.22), transparent 70%), {STEEN}, linear-gradient(180deg,#1e2121,#121414) !important;
  color: #d7dcd6; font-family: "RW Spectral", Georgia, serif;
}}
body.rollwright-skin-arcane {H} input {{ background: rgba(0,0,0,.45); border: 1px solid #4e5652; color: #e7ece7; box-shadow: inset 0 2px 4px rgba(0,0,0,.6); }}
body.rollwright-skin-arcane {H} .rollwright-history-form button {{ background: linear-gradient(180deg,#e0621f,#a8400f); color: #fff1e0; font-family: "RW Uncial", serif; box-shadow: 0 0 10px rgba(255,100,20,.35); }}
body.rollwright-skin-arcane {H} .rollwright-history-clear {{ color: #66706b !important; }}
body.rollwright-skin-arcane {H} .rollwright-history-group-title {{ font-family: "RW Uncial", serif; font-variant: normal; text-transform: none; letter-spacing: .02em; font-size: 1em; color: #ffb36a;
  text-shadow: 0 0 8px rgba(255,110,20,.5); }}
body.rollwright-skin-arcane {H} .rollwright-history-list::before {{ width: 2px; background: linear-gradient(180deg, #ff7a2a, rgba(255,90,20,.15) 60%, transparent); box-shadow: 0 0 6px rgba(255,100,20,.6); }}
body.rollwright-skin-arcane {H} .rollwright-history-item {{ border: none; border-radius: 2px; background: {STEEN}, linear-gradient(180deg,#3d4341,#2a2e2d);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.12), inset 0 -2px 0 rgba(0,0,0,.6), 0 2px 6px rgba(0,0,0,.5); }}
body.rollwright-skin-arcane {H} .rollwright-history-item::before {{ background: #ff8a3a; filter: drop-shadow(0 0 4px rgba(255,110,30,.8)); }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-history-latest {{ border: none; box-shadow: inset 0 1px 0 rgba(255,255,255,.14), inset 0 -2px 0 rgba(0,0,0,.6), 0 0 0 1px rgba(255,122,42,.45), 0 0 16px rgba(255,90,20,.28); }}
body.rollwright-skin-arcane {H} .rollwright-history-name {{ font-family: "RW Uncial", serif; text-transform: none; letter-spacing: .02em; font-size: .95em; color: #ff9a55; }}
body.rollwright-skin-arcane {H} .rollwright-history-result {{ font-family: "RW Uncial", serif; font-weight: 400; font-size: 1.6em; color: #eef2ee; text-shadow: 0 -1px 0 #000, 0 1px 0 rgba(255,255,255,.12); }}
body.rollwright-skin-arcane {H} .rollwright-history-formula, body.rollwright-skin-arcane {H} .rollwright-history-details, body.rollwright-skin-arcane {H} .rollwright-history-meta {{ color: #8f9a93; }}
body.rollwright-skin-arcane {H} .rollwright-history-meta .clickable-icon {{ color: #8f9a93; }}
/* NAT 20: het tablet gloeit van onderen alsof het uit de smidse komt. */
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-crit {{ background: radial-gradient(ellipse 90% 80% at 50% 120%, rgba(255,170,50,.55), rgba(255,100,20,.2) 50%, transparent 75%), {STEEN}, linear-gradient(180deg,#3d4341,#2a2e2d);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.14), inset 0 -2px 0 rgba(0,0,0,.6), 0 0 0 1px rgba(255,180,60,.6), 0 0 20px rgba(255,120,20,.35); }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-crit::before {{ background: #ffe07a; filter: drop-shadow(0 0 6px #ffb020); }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-crit .rollwright-history-result {{ color: #fff3c0; font-size: 1.9em; text-shadow: 0 0 6px #ffb020, 0 0 16px #ff7a00; }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-crit .rollwright-history-name {{ color: #ffe07a; }}
body.rollwright-skin-arcane {H} .rollwright-history-item .rollwright-stamp {{ font-family: "RW Uncial", serif !important; background: #1b1d1d !important; color: #ffb36a !important; border: 1px solid #ff8a3a !important; border-radius: 1px !important; box-shadow: none !important; }}
/* NAT 1: een gebarsten tablet met rood licht door de barst. */
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-fumble {{ background:
  linear-gradient(104deg, transparent 70%, #ff4a1c 71%, #ffb070 71.6%, #ff4a1c 72.2%, transparent 73.5%), linear-gradient(64deg, transparent 84%, #ff4a1c 85%, transparent 86.2%),
  {STEEN}, linear-gradient(180deg,#26292a,#141616); box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 0 0 1px rgba(255,60,30,.45), 0 0 14px rgba(255,50,20,.3); }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-fumble::before {{ background: #ff5a3a; filter: drop-shadow(0 0 4px rgba(255,40,20,.8)); }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-fumble .rollwright-history-result {{ color: #ff8a70; text-shadow: 0 0 8px rgba(255,40,20,.8); }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-fumble .rollwright-history-name {{ color: #ff7a5a; }}
"""

# ---------------- ronde e: leesbare cijfers, kortere kop, fijnere barst ----------------
css += f"""
/* IM Fell heeft alleen ouderwetse cijfers (1d20 leest als id2o): formules, invoer en details in Cinzel. */
body.rollwright-skin-parchment {H} .rollwright-history-formula, body.rollwright-skin-parchment {H} .rollwright-history-details,
body.rollwright-skin-parchment {H} input {{ font-family: "RW Cinzel", serif; font-style: normal; font-size: .82em; letter-spacing: .03em; }}
body.rollwright-skin-parchment {H} .rollwright-history-result {{ font-family: "RW Cinzel", serif; font-weight: 600; font-size: 1.5em; }}
body.rollwright-skin-parchment {H} .rollwright-history-item.rollwright-crit .rollwright-history-result {{ font-weight: 700; font-size: 1.8em; }}
body.rollwright-skin-arcane {H} .rollwright-history-group-title {{ font-size: .85em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
body.rollwright-skin-arcane {H} .rollwright-history-item.rollwright-fumble {{ background:
  linear-gradient(101deg, transparent 77%, rgba(255,90,40,.85) 77.4%, rgba(255,90,40,.85) 77.8%, transparent 78.2%),
  linear-gradient(72deg, transparent 86.5%, rgba(255,90,40,.7) 86.8%, transparent 87.2%),
  radial-gradient(ellipse 30% 60% at 80% 55%, rgba(255,60,20,.22), transparent 70%),
  {STEEN}, linear-gradient(180deg,#26292a,#141616); }}
"""

(HIER / "wereld.css").write_text(css)
print(len(css), "tekens")
