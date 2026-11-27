#!/usr/bin/env bash
# Controle na het plakken van Click Joints Pro 1.2.9 (Bram, 27 nov 2026, issue #299).
# Draai na het plakken op ma 30 nov: bash producten/blender-gewrichten/winkel/controle-1.2.9.sh
# Leest alleen openbare pagina's met curl. Geen inloggen, geen sleutel. Code 0 = alles GOED.
set -u
UA="Mozilla/5.0"
G="https://duinhouwer8.gumroad.com/l/click-joints-pro"
S="https://superhivemarket.com/products/click-joints-pro"
T=$(mktemp -d)
curl -sL -A "$UA" "$G" -o "$T/gumroad.html"
curl -sL -A "$UA" "$S" -o "$T/superhive.html"
curl -sL -A "$UA" "$S/docs" -o "$T/docs.html"
curl -sL -A "$UA" "$S/faq" -o "$T/faq.html"
python3 - "$T" <<'PY'
import sys, re, html
d = sys.argv[1]
def tekst(n):
    t = open(f"{d}/{n}.html", encoding="utf-8", errors="replace").read()
    t = re.sub(r"<script(?![^>]*data-page).*?</script>|<style.*?</style>", " ", t, flags=re.S)
    t = html.unescape(html.unescape(t)).replace("\\u003c", "<").replace("\\u003e", ">")
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)
# (pagina, moet erin staan, mag er niet in staan)
regels = [
    ("gumroad", ["Version 1.2.9", "What's new in 1.2.9", "click_joints_pro-1.2.9.zip", "turns the free Click Joints off for you"],
                ["turn the free one off first", "click_joints_pro-1.2.8.zip", "Version 1.2.8", "print tested"]),
    ("superhive", ["New in Pro 1.2.9", "it turns the free one off for you"],
                  ["Disable the free one first", "New in Pro 1.2.8", "print tested"]),
    ("docs", ["click_joints_pro-1.2.9.zip", "Free Click Joints was turned off; Pro includes everything in it.", "in step 2, under Clearance (mm)"],
             ["turn the free one off first", "click_joints_pro-1.2.8.zip", "print tested"]),
    ("faq", ["How do I install it?", "click_joints_pro-1.2.9.zip", "turns the free Click Joints off for you", "in step 2, under Clearance (mm)"],
            ["Disable the free Click Joints first", "Print one small joint first", "print tested"]),
]
fout = 0
for n, moet, niet in regels:
    t = tekst(n)
    if len(t) < 2000:
        print(f"{n}: FOUT pagina leeg of geweigerd ({len(t)} tekens), later opnieuw")
        fout = 1
        continue
    for z in moet:
        ok = z in t
        print(f"{n}: {'GOED' if ok else 'FOUT'} staat erin: {z}")
        fout |= not ok
    for z in niet:
        ok = z not in t
        print(f"{n}: {'GOED' if ok else 'FOUT'} staat er niet meer: {z}")
        fout |= not ok
print("ALLES GOED" if not fout else "NIET ALLES GOED: zie FOUT hierboven")
sys.exit(1 if fout else 0)
PY
