#!/usr/bin/env bash
# Controle na het plakken van de plakkaart Click Cuts (Productbouwer, 27 nov 2026, issue #300).
# Gebruik: bash producten/blender-splitser/winkel/controle-laatste-meter.sh <1|2|3>
# Leest alleen openbare pagina's met curl. Geen inloggen, geen sleutel. Code 0 = alles GOED.
set -u
DEEL="${1:-}"
case "$DEEL" in 1|2|3) ;; *) echo "Gebruik: $0 <1|2|3>"; exit 2 ;; esac
UA="Mozilla/5.0"
T=$(mktemp -d)
haal() { curl -sL -A "$UA" "$2" -o "$T/$1.html" -w "%{http_code}" ; }
declare -A CODE
if [ "$DEEL" = 1 ]; then
  CODE[gumroad]=$(haal gumroad https://duinhouwer8.gumroad.com/l/click-cuts)
  CODE[hulp]=$(haal hulp https://dortus.com/click-cuts/)
  CODE[beeld]=$(curl -s -A "$UA" -o /dev/null -w "%{http_code}" https://dortus.com/click-cuts/draw-cut.jpg)
elif [ "$DEEL" = 2 ]; then
  CODE[shcuts]=$(haal shcuts https://superhivemarket.com/products/click-cuts)
  CODE[voor]=$(haal voor https://dortus.com/)
  CODE[cj]=$(haal cj https://dortus.com/click-joints/)
  CODE[pro]=$(haal pro https://duinhouwer8.gumroad.com/l/click-joints-pro)
  CODE[gratis]=$(haal gratis https://duinhouwer8.gumroad.com/l/click-joints-free)
  CODE[shpro]=$(haal shpro https://superhivemarket.com/products/click-joints-pro)
else
  CODE[shcuts]=$(haal shcuts https://superhivemarket.com/products/click-cuts)
  CODE[docs]=$(haal docs https://superhivemarket.com/products/click-cuts/docs)
  CODE[faq]=$(haal faq https://superhivemarket.com/products/click-cuts/faq)
fi
for k in "${!CODE[@]}"; do echo "$k=${CODE[$k]}"; done > "$T/codes"
python3 - "$T" "$DEEL" <<'PY'
import sys, re, html, json
d, deel = sys.argv[1], sys.argv[2]
codes = dict(r.strip().split("=") for r in open(f"{d}/codes") if "=" in r)
def ruw(n):
    t = open(f"{d}/{n}.html", encoding="utf-8", errors="replace").read()
    return html.unescape(html.unescape(t)).replace("\\u003c", "<").replace("\\u003e", ">").replace('\\"', '"')
def tekst(n):
    t = re.sub(r"<style.*?</style>", " ", ruw(n), flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)
fout = 0
def zeg(ok, wat):
    global fout
    print(("GOED " if ok else "FOUT ") + wat)
    fout |= not ok
# (pagina, moet erin, mag er niet in)
if deel == "1":
    regels = [
        ("gumroad", ["Draw cut:", "The part that comes off lights up white before you cut.",
                     "from 0.10 mm for resin to 0.30 mm for TPU",
                     "Yes. Split to fit cuts along the X, Y and Z axes.", "dortus.com/click-cuts"],
                    ["Partly. Split to fit", "Free cut: an extra cut at any angle", "print tested"]),
        ("hulp", ["Choose where it cuts: Draw cut", "click_cuts-1.1.0.zip", "draw-cut.jpg",
                  "Yes. Split to fit cuts along the X, Y and Z axes."],
                 ["click_cuts-1.0.0.zip", "Partly. Split to fit", "print tested"]),
    ]
    zeg(codes.get("beeld") == "200", f"dortus.com/click-cuts/draw-cut.jpg geeft {codes.get('beeld')}")
    r = ruw("gumroad"); i = r.find('"covers":')
    try:
        covers = json.JSONDecoder().raw_decode(r[i + 9:])[0] if i >= 0 else []
    except Exception:
        covers = []
    zeg(len(covers) == 6, f"Gumroad heeft {len(covers)} covers (verwacht 6: vijf oude plus Draw your own cut)")
    if len(covers) > 1:
        zeg((covers[1].get("native_width"), covers[1].get("native_height")) == (1920, 1080),
            f"cover 2 is {covers[1].get('native_width')} x {covers[1].get('native_height')} (Draw your own cut is 1920 x 1080; met eigen ogen nakijken dat het dat beeld is)")
elif deel == "2":
    regels = [
        ("voor", ["Click Cuts"], []),
        ("cj", ["Also from Dortus", "Click Cuts"], []),
        ("pro", ["Model too big for your printer bed?", "/l/click-cuts?utm_source=gumroad"], []),
        ("gratis", ["Model too big for your printer bed?", "/l/click-cuts?utm_source=gumroad"], []),
        ("shpro", ["Model too big for your printer bed?", "superhivemarket.com/products/click-cuts"], []),
    ]
    zeg(codes.get("shcuts") == "200" and len(tekst("shcuts")) > 2000,
        f"Superhive Click Cuts is zichtbaar (code {codes.get('shcuts')}); 403 = nog niet goedgekeurd, deel 2 nog niet plakken")
else:
    regels = [
        ("shcuts", ["Draw cut", "1.1.0"], ["print tested"]),
        ("docs", ["click_cuts-1.1.0.zip", "Choose where it cuts: Draw cut"], ["click_cuts-1.0.0.zip"]),
        ("faq", ["Yes. Split to fit cuts along the X, Y and Z axes."], ["Partly. Split to fit"]),
    ]
for n, moet, niet in regels:
    t = tekst(n) + " " + ruw(n)
    if codes.get(n) != "200" or len(t) < 2000:
        zeg(False, f"{n}: pagina gaf code {codes.get(n)} of is leeg; Superhive geeft soms 429, dan na 5 minuten opnieuw")
        continue
    for z in moet:
        zeg(z in t, f"{n}: staat erin: {z}")
    for z in niet:
        zeg(z not in t, f"{n}: staat er niet (meer): {z}")
print("ALLES GOED" if not fout else "NIET ALLES GOED: zie FOUT hierboven")
sys.exit(1 if fout else 0)
PY
