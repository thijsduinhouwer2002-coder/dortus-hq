"""Ruismeter (Thijs 24 nov 21:16: "die ruis kan ik niet tegen").

Telt de commits op main van de laatste N uur: hoeveel veranderen iets aan het product
(code, beeld, film, data, workflow, site) en hoeveel zijn alleen papier (berichten, logboeken, bord).
Doel: minstens 60% product. Gebruik: python3 organisatie/controle/ruismeter.py [uren]
"""
import re, subprocess, sys
from collections import Counter

# Sinds 26 nov telt ook marketingwerk mee als werk: plaatsteksten, mails aan makers, wachtrij van filmpjes.
PRODUCT = re.compile(r"\.(py|gd|ts|js|png|jpg|jpeg|webp|mp4|mp3|wav|ogg|json|yml|yaml|html|css|blend|cs|kt|java|mc|xml)$|^producten/.*/(app|godot|src|addon)/|^commercie/(outreach|verspreiden)/|^marketing/wachtrij/")


def soort(bestanden):
    return "product" if any(PRODUCT.search(b) for b in bestanden) else "papier"


def main(uren=24):
    log = subprocess.run(["git", "log", f"--since={uren} hours ago", "--name-only", "--pretty=@@%an"],
                         capture_output=True, text=True, check=True).stdout
    tel, per_maker = Counter(), Counter()
    for blok in log.split("@@")[1:]:
        regels = [r for r in blok.strip().splitlines() if r]
        if not regels:
            continue
        s = soort(regels[1:])
        tel[s] += 1
        if s == "papier":
            per_maker[regels[0]] += 1
    totaal = sum(tel.values()) or 1
    pct = round(100 * tel["product"] / totaal)
    print(f"Laatste {uren} uur: {totaal} commits, {tel['product']} product ({pct}%), {tel['papier']} alleen papier. Doel: 60% product.")
    return pct


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 24)
