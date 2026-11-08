#!/usr/bin/env python3
# Daan: maakt src/styles/08-skins-v3.css. Elke regel geldt voor het token in de notitie en voor de tegel in de instellingen.
import sys

def sel(skin, extra="", tail="", block=True):
    nb = "" if block else ":not(.rollwright-roll-block)"
    a = f"body.rollwright-skin-{skin} .rollwright-roll{extra}:not(.rollwright-error){nb}:not(.rollwright-skin-preview-tile .rollwright-roll){tail}"
    b = f".rollwright-skin-preview-tile.rollwright-skin-{skin} .rollwright-roll{extra}:not(.rollwright-error){nb}{tail}"
    return f"{a},\n{b}"

out = []
def rule(skin, body, extra="", tail=""):
    out.append(f"{sel(skin, extra, tail)} {{\n" + "\n".join("\t" + l.strip() for l in body.strip().splitlines()) + "\n}\n")

def raw(s):
    out.append(s.strip("\n") + "\n")

raw("""
/* ==========================================================================================
   Skins v3 (Daan, 8 nov 12:30, na Thijs 12:33 en 12:34): een skin is een eigen wereld, niet
   hetzelfde token in een andere kleur. Elke skin krijgt nu een eigen VORM, een eigen LETTER,
   een eigen MERKTEKEN en een eigen BEWEGING bij het rollen.
   Parchment, "het scriptorium": een gescheurde strook oud papier, geschreven in een letter uit
   de 17e eeuw. Het merkteken is een rood lakzegel met de d20 erin gedrukt. Bij een worp drukt het
   zegel neer en schrijft de inkt het getal van links naar rechts, met een paar spatjes inkt.
   Arcane, "de sterrenkaart": een kristal met punten aan beide kanten en een rand van licht,
   in Romeinse kapitalen. Bij een worp draait de d20 twee keer rond in een cirkel van runen en
   verschijnt het getal uit het licht, met een wolkje sterrenstof.
   Hoe: het lichaam van het token is ::before met een clip-path (de vorm), het token zelf is
   doorzichtig en isoleert (isolation), zodat ::before achter de tekst blijft maar voor de
   pagina. De rand en schaduw komen van filter: drop-shadow op het token, dat volgt de vorm.
   De sticker (NAT 20, NAT 1) staat er boven (z-index 1) en wordt niet afgeknipt.
   Blokken (tabel, sectie) krijgen dezelfde vorm.
   ========================================================================================== */
""")

# ---------------------------------------------------------------- PARCHMENT
TORN = ("polygon(0 12%, 5% 2%, 12% 7%, 19% 0, 27% 6%, 36% 1%, 45% 5%, 53% 0, 61% 6%, 70% 2%, 78% 7%, 86% 0, 93% 5%, "
        "100% 1%, calc(100% - 0.14em) 28%, 100% 50%, calc(100% - 0.1em) 74%, 100% 97%, 92% 100%, 84% 94%, 75% 99%, "
        "66% 93%, 57% 100%, 48% 95%, 39% 100%, 30% 94%, 21% 99%, 13% 93%, 6% 100%, 0 95%, 0.12em 70%, 0 46%, 0.1em 24%)")
NOISE = "var(--rw-paper-noise)"

rule("parchment", f"""
font-family: "Rollwright Fell", "Palatino Linotype", Palatino, Georgia, serif;
font-style: italic;
font-size: 1.08em;
letter-spacing: 0;
color: #2a1808;
background: transparent;
background-color: transparent;
border: 0;
border-radius: 0;
box-shadow: none;
isolation: isolate;
padding: 0.04em 0.62em 0.02em 0.5em;
filter: drop-shadow(0 1px 1px rgba(60, 35, 5, 0.45)) drop-shadow(0 0 0.5px rgba(90, 55, 15, 0.6));
transform: rotate(-0.4deg);
""")
rule("parchment", f"""
content: "";
position: absolute;
inset: 0;
z-index: -1;
border-radius: 0;
pointer-events: none;
clip-path: {TORN};
background:
	{NOISE},
	radial-gradient(ellipse at 18% 25%, rgba(255, 249, 225, 0.85), transparent 55%),
	radial-gradient(ellipse at 88% 85%, rgba(140, 85, 30, 0.38), transparent 62%),
	linear-gradient(180deg, #f2e3b8, #e0c78d);
box-shadow: inset 0 0 0.5em rgba(110, 60, 15, 0.55);
animation: none;
""", tail="::before")
rule("parchment", """
transform: rotate(-1.2deg) translateY(-1px);
box-shadow: none;
filter: drop-shadow(0 3px 3px rgba(60, 35, 5, 0.4)) drop-shadow(0 0 0.5px rgba(90, 55, 15, 0.6));
""", tail=":hover")
rule("parchment", """
font-family: "Rollwright Garamond", "Palatino Linotype", Palatino, "Book Antiqua", serif;
font-weight: 700;
font-size: 1.1em;
font-variant-numeric: lining-nums tabular-nums;
""", tail=" .rollwright-value")
# tekst uit een tabel blijft in de oude letter
rule("parchment", "font-family: \"Rollwright Fell\", Georgia, serif; font-weight: 400; font-size: 1em;", extra=".rollwright-text", tail=" .rollwright-value")
rule("parchment", "color: #6a4220; opacity: 1;", tail=" .rollwright-label")
# lakzegel met de d20 erin gedrukt
rule("parchment", """
width: 1.22em;
height: 1.22em;
background: radial-gradient(circle at 35% 30%, #e0503f, #a8261a 55%, #6a0f08);
-webkit-mask: var(--rw-d20) center / 72% no-repeat, radial-gradient(circle, #000 64%, transparent 67%);
-webkit-mask-composite: xor;
mask: var(--rw-d20) center / 72% no-repeat exclude, radial-gradient(circle, #000 64%, transparent 67%);
filter: drop-shadow(0 0.6px 0.4px rgba(40, 0, 0, 0.6));
""", tail=" .rollwright-icon::before")
# tekst uit een tabel: een lichtere snipper
rule("parchment", f"""
background:
	{NOISE},
	linear-gradient(180deg, #f5e9c8, #e9d6a6);
""", extra=".rollwright-text", tail="::before")
for sk in ("parchment", "arcane"):
    rule(sk, """
background: transparent;
background-color: transparent;
box-shadow: none;
border: 0;
border-bottom: 0;
border-radius: 0;
""", extra=".rollwright-text.rollwright-text")
# crit: bladgoud
for ex in (".rollwright-crit", ".rollwright-fumble"):
    rule("parchment", """
background: transparent;
background-color: transparent;
box-shadow: none;
border: 0;
""", extra=ex)
rule("parchment", f"""
background:
	linear-gradient(115deg, transparent 35%, rgba(255, 236, 170, 0.45) 48%, transparent 60%),
	{NOISE},
	linear-gradient(180deg, #f8dc82, #d9a531 60%, #b47c18);
box-shadow: inset 0 0 0.45em rgba(120, 70, 0, 0.55);
animation: none;
""", extra=".rollwright-crit", tail="::before")
rule("parchment", """
color: #3b2000;
text-shadow: 0 1px 0 rgba(255, 240, 190, 0.7);
filter: drop-shadow(0 0 0.35em rgba(230, 170, 40, 0.7)) drop-shadow(0 1px 1px rgba(60, 35, 5, 0.45));
""", extra=".rollwright-crit")
rule("parchment", f"""
background:
	radial-gradient(ellipse 26% 70% at 100% 55%, rgba(25, 10, 5, 0.65), transparent 100%),
	radial-gradient(circle 0.13em at 84% 16%, rgba(25, 10, 5, 0.6), transparent 100%),
	{NOISE},
	linear-gradient(180deg, #e7d39d, #d3b77c);
animation: none;
""", extra=".rollwright-fumble", tail="::before")
rule("parchment", "color: #5e0d07;", extra=".rollwright-fumble")

raw("""
@keyframes rw-p-seal {
	0% { transform: scale(2.6) rotate(-40deg); opacity: 0; }
	50% { transform: scale(0.82) rotate(6deg); opacity: 1; }
	72% { transform: scale(1.1) rotate(-2deg); }
	100% { transform: none; }
}

@keyframes rw-p-ink {
	0% { clip-path: inset(-0.2em 100% -0.2em 0); filter: blur(1.2px); opacity: 0.5; }
	70% { filter: blur(0.3px); opacity: 1; }
	100% { clip-path: inset(-0.2em -0.2em -0.2em -0.2em); filter: none; opacity: 1; }
}

@keyframes rw-p-splat {
	0% { transform: scale(0.3); opacity: 0; }
	30% { transform: scale(1.05); opacity: 0.9; }
	100% { transform: scale(1.15); opacity: 0; }
}
""")
rule("parchment", "animation: rw-p-seal calc(520ms * var(--rw-slow)) cubic-bezier(0.3, 1.3, 0.5, 1) both;", extra=".rollwright-rolled", tail=" .rollwright-icon")
rule("parchment", """
display: inline-block;
animation: rw-p-ink calc(440ms * var(--rw-slow)) calc(200ms * var(--rw-slow)) cubic-bezier(0.4, 0, 0.3, 1) both;
""", extra=".rollwright-rolled", tail=" .rollwright-value")
rule("parchment", """
animation: rw-p-ink calc(440ms * var(--rw-slow)) calc(200ms * var(--rw-slow)) cubic-bezier(0.4, 0, 0.3, 1) both, rw-shake calc(420ms * var(--rw-slow)) calc(700ms * var(--rw-slow)) ease-in-out;
""", extra=".rollwright-rolled.rollwright-fumble", tail=" .rollwright-value")
# spatjes inkt na de worp (niet bij crit: daar is ::after de vonk)
rule("parchment", """
content: "";
position: absolute;
inset: -0.35em -0.5em;
z-index: -2;
pointer-events: none;
background:
	radial-gradient(circle 0.09em at 4% 20%, #2a1808 90%, transparent),
	radial-gradient(circle 0.06em at 9% 88%, #2a1808 90%, transparent),
	radial-gradient(circle 0.07em at 97% 12%, #2a1808 90%, transparent),
	radial-gradient(circle 0.05em at 93% 92%, #2a1808 90%, transparent),
	radial-gradient(circle 0.04em at 50% 2%, #2a1808 90%, transparent);
animation: rw-p-splat calc(900ms * var(--rw-slow)) calc(260ms * var(--rw-slow)) ease-out both;
""", extra=".rollwright-rolled:not(.rollwright-crit)", tail="::after")

# ---------------------------------------------------------------- ARCANE
HEX = "polygon(0.6em 0, calc(100% - 0.6em) 0, 100% 50%, calc(100% - 0.6em) 100%, 0.6em 100%, 0 50%)"
rule("arcane", """
font-family: "Rollwright Cinzel", "Trajan Pro", "Cinzel", Georgia, serif;
font-weight: 700;
font-size: 0.94em;
letter-spacing: 0.035em;
color: #effdff;
background: transparent;
background-color: transparent;
border: 0;
border-radius: 0;
box-shadow: none;
isolation: isolate;
padding: 0.16em 0.95em 0.1em 0.85em;
filter: drop-shadow(0 0 0.6px #d8fbff) drop-shadow(0 0 0.6px #7fe3f5) drop-shadow(0 0 0.35em rgba(90, 220, 245, 0.55));
text-shadow: 0 0 0.35em rgba(160, 240, 255, 0.85);
""")
rule("arcane", f"""
content: "";
position: absolute;
inset: 0;
z-index: -1;
border-radius: 0;
pointer-events: none;
clip-path: {HEX};
background:
	linear-gradient(180deg, rgba(220, 250, 255, 0.35), transparent 38%),
	conic-gradient(from 90deg at 50% 55%, #0d3550, #145a78 12%, #0a2a40 25%, #1b6f8f 37%, #0b2f47 50%, #12506d 62%, #082236 75%, #17627f 87%, #0d3550),
	linear-gradient(170deg, #0f3d57, #061826);
box-shadow: none;
animation: none;
""", tail="::before")
rule("arcane", """
filter: drop-shadow(0 0 0.8px #ffffff) drop-shadow(0 0 0.8px #9ff3ff) drop-shadow(0 0 0.6em rgba(90, 220, 245, 0.8));
box-shadow: none;
""", tail=":hover")
rule("arcane", "font-weight: 700;", tail=" .rollwright-value")
rule("arcane", "color: #a9e9f5; opacity: 1; letter-spacing: 0.04em;", tail=" .rollwright-label")
rule("arcane", f"""
background:
	linear-gradient(180deg, rgba(220, 250, 255, 0.28), transparent 40%),
	linear-gradient(100deg, #0f3d57, #0a2a40 30%, #145a78 55%, #0a2a40 80%, #12506d);
""", extra=".rollwright-text", tail="::before")
for ex in (".rollwright-crit", ".rollwright-fumble"):
    rule("arcane", """
background: transparent;
background-color: transparent;
box-shadow: none;
border: 0;
""", extra=ex)
rule("arcane", f"""
background:
	linear-gradient(180deg, rgba(255, 228, 140, 0.5), transparent 24%),
	conic-gradient(from 90deg at 50% 55%, #10304a, #1b4a66 25%, #0c2538 50%, #1a4560 75%, #10304a),
	linear-gradient(170deg, #12354f, #071a29);
animation: none;
""", extra=".rollwright-crit", tail="::before")
rule("arcane", """
color: #ffd45e;
text-shadow: 0 0 0.35em rgba(255, 200, 80, 0.8);
filter: drop-shadow(0 0 0.8px #ffe9a8) drop-shadow(0 0 0.8px #ffc94a) drop-shadow(0 0 0.7em rgba(255, 190, 60, 0.85));
""", extra=".rollwright-crit")
rule("arcane", f"""
background:
	radial-gradient(ellipse at 50% 120%, rgba(255, 70, 110, 0.4), transparent 65%),
	conic-gradient(from 90deg at 50% 55%, #2a1020, #3d1830 25%, #1d0a16 50%, #36152a 75%, #2a1020);
animation: none;
""", extra=".rollwright-fumble", tail="::before")
rule("arcane", """
color: #ff9ab8;
text-shadow: 0 0 0.35em rgba(255, 60, 110, 0.8);
filter: drop-shadow(0 0 0.7px #ff7aa8) drop-shadow(0 0 0.5em rgba(255, 40, 100, 0.6));
""", extra=".rollwright-fumble")

rule("arcane", """
color: #2a1c00;
background: #ffd45e;
background-image: none;
border-color: #0a2a40;
font-family: "Rollwright Cinzel", Georgia, serif;
""", extra=".rollwright-crit", tail=" > .rollwright-stamp")
rule("arcane", """
color: #ffffff;
background: #b3204e;
background-image: none;
border-color: #0a2a40;
font-family: "Rollwright Cinzel", Georgia, serif;
""", extra=".rollwright-fumble", tail=" > .rollwright-stamp")
raw("""
/* Arcane in een licht thema: geen waas om elk token, alleen de lichtrand (controleur run 26). */
body.theme-light.rollwright-skin-arcane .rollwright-roll:not(.rollwright-crit):not(.rollwright-fumble):not(.rollwright-error):not(.rollwright-skin-preview-tile .rollwright-roll) {
	filter: drop-shadow(0 0 0.6px #0a2a40) drop-shadow(0 0 0.6px #5fc9e0) drop-shadow(0 1px 1.5px rgba(5, 30, 45, 0.35));
}
""")
raw("""
@keyframes rw-a-spin {
	0% { transform: rotate(-720deg) scale(0.3); opacity: 0; }
	70% { transform: rotate(10deg) scale(1.25); opacity: 1; }
	100% { transform: none; }
}

@keyframes rw-a-form {
	0% { transform: scale(1.7); opacity: 0; filter: blur(5px) brightness(2.2); }
	60% { transform: scale(0.94); opacity: 1; filter: blur(0) brightness(1.5); }
	100% { transform: none; filter: none; }
}

@keyframes rw-a-runes {
	0% { transform: rotate(0) scale(0.4); opacity: 0; }
	25% { opacity: 1; }
	100% { transform: rotate(200deg) scale(1.5); opacity: 0; }
}

@keyframes rw-a-dust {
	0% { transform: scale(0.5); opacity: 0; }
	30% { opacity: 1; }
	100% { transform: scale(1.35) translateY(-0.2em); opacity: 0; }
}
""")
rule("arcane", "position: relative; animation: rw-a-spin calc(560ms * var(--rw-slow)) cubic-bezier(0.2, 0.8, 0.3, 1.2) both;", extra=".rollwright-rolled", tail=" .rollwright-icon")
rule("arcane", """
display: inline-block;
animation: rw-a-form calc(420ms * var(--rw-slow)) calc(180ms * var(--rw-slow)) cubic-bezier(0.2, 0.8, 0.3, 1.1) both;
""", extra=".rollwright-rolled", tail=" .rollwright-value")
rule("arcane", """
animation: rw-a-form calc(420ms * var(--rw-slow)) calc(180ms * var(--rw-slow)) ease-out both, rw-shake calc(420ms * var(--rw-slow)) calc(620ms * var(--rw-slow)) ease-in-out;
""", extra=".rollwright-rolled.rollwright-fumble", tail=" .rollwright-value")
# cirkel van runen om de d20 (niet bij crit: daar is icon::after de gouden ring)
rule("arcane", """
content: "";
position: absolute;
inset: -0.32em;
border-radius: 50%;
border: 1.5px dashed #9ff3ff;
box-shadow: 0 0 6px #9ff3ff;
pointer-events: none;
animation: rw-a-runes calc(900ms * var(--rw-slow)) calc(60ms * var(--rw-slow)) ease-out both;
""", extra=".rollwright-rolled:not(.rollwright-crit)", tail=" .rollwright-icon::after")
rule("arcane", """
content: "";
position: absolute;
inset: -0.45em -0.4em;
z-index: -2;
pointer-events: none;
background:
	radial-gradient(circle 0.07em at 6% 30%, #ffffff 80%, transparent),
	radial-gradient(circle 0.05em at 14% 90%, #9ff3ff 80%, transparent),
	radial-gradient(circle 0.06em at 96% 18%, #ffb8f0 80%, transparent),
	radial-gradient(circle 0.05em at 90% 94%, #ffffff 80%, transparent),
	radial-gradient(circle 0.05em at 44% 0%, #9ff3ff 80%, transparent),
	radial-gradient(circle 0.04em at 62% 100%, #ffffff 80%, transparent);
animation: rw-a-dust calc(1000ms * var(--rw-slow)) calc(300ms * var(--rw-slow)) ease-out both;
""", extra=".rollwright-rolled:not(.rollwright-crit)", tail="::after")

raw("""
@media (prefers-reduced-motion: reduce) {
	body.rollwright-skin-parchment .rollwright-roll .rollwright-icon,
	body.rollwright-skin-parchment .rollwright-roll .rollwright-value,
	body.rollwright-skin-arcane .rollwright-roll .rollwright-icon,
	body.rollwright-skin-arcane .rollwright-roll .rollwright-value {
		animation: none !important;
	}

	body.rollwright-skin-parchment .rollwright-roll::after,
	body.rollwright-skin-arcane .rollwright-roll:not(.rollwright-crit)::after,
	body.rollwright-skin-arcane .rollwright-roll .rollwright-icon::after {
		display: none;
	}
}
""")

open(sys.argv[1], "w").write("\n".join(out))
print(len(out), "blokken")
