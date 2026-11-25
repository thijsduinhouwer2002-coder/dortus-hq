#!/usr/bin/env bash
# Controle saleweek Click Joints Pro (Bram, 25 nov 2026, issue #61).
# Draai op vr 27 nov 's ochtends (en gerust elke dag t/m 2 dec): bash platformen/blender/sale-controle.sh
# Leest alleen openbare pagina's met curl. Geen inloggen, geen sleutel.
set -u
UA="Mozilla/5.0"
G="https://duinhouwer8.gumroad.com/l/click-joints-pro"
S="https://superhivemarket.com/products/click-joints-pro"
T=$(mktemp -d)
curl -sL -A "$UA" "$G" -o "$T/plain.html"
curl -sL -A "$UA" "$G/CYBER25" -o "$T/link.html"
curl -sL -A "$UA" "$S" -o "$T/sh.html"
python3 - "$T" <<'PY'
import sys, re, html
d = sys.argv[1]
def lees(n):
    return html.unescape(open(f"{d}/{n}.html", encoding="utf-8", errors="replace").read())
def korting(t):
    m = re.search(r'"discount_code":(null|\{[^}]*\})', t)
    return m.group(1) if m else "niet gevonden"
fout = 0
link = korting(lees("link"))
print("1. Gumroad salelink /CYBER25:", link)
if '"valid":true' in link:
    print("   GOED: de link geeft de korting.")
elif "inactive" in link:
    print("   NOG NIET ACTIEF: de code bestaat, maar loopt nu niet. Na 27 nov 00:00 NL is dit fout: meld het de hoofdchat.")
    fout = 1
else:
    print("   FOUT: de code wordt niet herkend. Meld het de hoofdchat.")
    fout = 1
plain = korting(lees("plain"))
print("2. Gumroad gewone pagina (zonder code):", plain)
if '"valid":true' in plain:
    print("   Vanzelf toegepast staat AAN: elke koper krijgt de korting, ook zonder link.")
else:
    print("   Vanzelf toegepast staat UIT of loopt nog niet: zonder de salelink betaalt een koper de volle prijs,")
    print("   tenzij hij CYBER25 typt. Gebruik dan saleregel A (met code) en overal de salelink.")
sh = re.sub(r"<script.*?</script>|<style.*?</style>", "", lees("sh"), flags=re.S)
sh = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", sh))
m = re.search(r"Personal[^$]{0,60}\$", sh)  # het blok met de prijs, niet de uitlegzin
stuk = sh[m.start():m.start() + 120] if m else ""
prijzen = [float(x) for x in re.findall(r"\$(\d+(?:\.\d\d)?)", stuk)]
print("3. Superhive Personal, bedragen in de buurt:", prijzen or "niet gevonden")
if any(abs(p - 7.80) < 0.01 for p in prijzen):
    print("   GOED: $7.80 (35% van $12) staat op de pagina.")
elif prijzen and min(prijzen) < 12:
    print("   LAGER dan $12, maar niet $7.80: kijk zelf of het de saleprijs is.")
else:
    print("   GEEN saleprijs te zien. Op 27 nov t/m 2 dec is dat fout of de sale staat alleen bij het afrekenen: kijk na in het dashboard.")
    fout = 1
sys.exit(fout)
PY
uit=$?
rm -rf "$T"
exit $uit
