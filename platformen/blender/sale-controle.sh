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
# Stap 4 t/m 7 (26 nov, #178): de rest van de kopersreis.
curl -sL -A "$UA" "https://extensions.blender.org/add-ons/click-joints/" -o "$T/gratis.html"
curl -sL -A "$UA" "$S/docs" -o "$T/docs.html"
curl -sL -A "$UA" "https://dortus.com/click-joints/" -o "$T/site.html"
curl -sL -A "$UA" "https://dortus.com/click-joints/gids/articulated-figure-3d-print-blender/" -o "$T/gids1.html"
curl -sL -A "$UA" "https://dortus.com/click-joints/gids/hinge-joint-3d-print-blender/" -o "$T/gids2.html"
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
    # Bedrag nalopen: 25% van de prijs op de pagina moet $14.25 zijn (geen mandje nodig, de pagina rekent zelf).
    pc = re.search(r'"price_cents":(\d{3,})', lees("link"))
    pct = re.search(r'"percents?":(\d+)', link)
    if pc and pct:
        na = int(pc.group(1)) * (100 - int(pct.group(1))) / 10000
        print(f"   Korting {pct.group(1)}% op ${int(pc.group(1))/100:.2f} = ${na:.2f}")
        if int(pct.group(1)) != 25 or abs(na - 14.25) > 0.005:
            print("   FOUT: niet 25% of niet $14.25: de saleregel klopt dan niet. Niet plakken, meld het de hoofdchat.")
            fout = 1
    else:
        print("   Percentage niet in de pagina gevonden: open de salelink zelf en kijk of $14.25 naast de doorgestreepte $19 staat.")
    if not fout:
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
gratis = lees("gratis")
naar_g = "duinhouwer8.gumroad.com/l/click-joints-pro" in gratis
naar_s = "superhivemarket.com/products/click-joints-pro" in gratis
print(f"4. Gratis pagina (extensions.blender.org) linkt naar Gumroad Pro: {'ja' if naar_g else 'NEE'}, naar Superhive Pro: {'ja' if naar_s else 'NEE'}")
if not (naar_g and naar_s):
    print("   FOUT: een koper van de gratis versie vindt Pro niet meer. Meld het de hoofdchat.")
    fout = 1
zips = sorted(set(re.findall(r"click_joints_pro-[0-9.]+\.zip", lees("docs"))))
print("5. Superhive Docs noemt:", zips or "geen zip")
if "click_joints_pro-1.2.8.zip" not in zips:
    print("   FOUT: de docs noemen niet click_joints_pro-1.2.8.zip.")
    fout = 1
versie = re.search(r"Version 1\.2\.8[^<]{0,40}", lees("plain"))
print("6. Gumroad Pro noemt de versie:", versie.group(0) if versie else "NEE")
if not versie:
    print("   FOUT: het versieblok (platformen/blender/pro-gumroad-versieblok-1.2.8.md) staat er niet. Meld het de hoofdchat.")
    fout = 1
na = "After you buy" in lees("plain") and "Click Joints tab" in lees("plain")
print("6b. Gumroad Pro zegt wat te doen na het kopen (gratis uit, paneel in de zijbalk):", "ja" if na else "NEE")
if not na:
    print("   FOUT: de alinea 'After you buy' (platformen/blender/pro-gumroad-na-kopen-1.2.8.md) staat er niet. Meld het de hoofdchat.")
    fout = 1
vies = [n for n in ("site", "gids1", "gids2") if "print tested" in lees(n).lower()]
print("7. dortus.com/click-joints en de twee gidsen zonder 'print tested':", "ja" if not vies else "NEE, nog op " + ", ".join(vies))
if vies:
    fout = 1
sys.exit(fout)
PY
uit=$?
rm -rf "$T"
exit $uit
