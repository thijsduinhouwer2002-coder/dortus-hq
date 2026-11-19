#!/usr/bin/env python3
"""Eén kort beeldbericht per run per eigenaar (roestronde R4, keuring 19 nov).

Gebruik: python3 beeldbericht.py <map met beeldverschil-artefacten> <product> <tak> <uitmap>

Leest de verslagen (verslag.md) van alle jobs van deze run, slaat vergelijkingen met een terugval over, en schrijft
alleen als er een groot verschil is:
  <uitmap>/sleutel.txt  product, tak en een vingerafdruk van wat er groot is: per plaatje LEEG, of VERSCHIL met de
                        referentierun. Dezelfde sleutel = al gemeld. Zo komt een blijvend leeg plaatje één keer,
                        en een verschil één keer per referentie, ook als runs tegelijk lopen.
  <uitmap>/gemeld.md    sleutel plus de grote verschillen per versie (komt op de tak schermen, de link in het bericht)
  <uitmap>/bericht.md   een paar regels voor berichten/<eigenaar>.md, zonder kop (die zet beelden.sh erboven)
"""
import hashlib
import os
import re
import sys
from pathlib import Path


def main(artmap, product, tak, uitmap):
    per_versie, refs, items = {}, set(), []
    for verslag in sorted(Path(artmap).glob("*/verslag.md")):
        tekst = verslag.read_text(encoding="utf-8")
        kop = tekst.splitlines()[0] if tekst else ""
        if "terugval" in kop:
            continue
        rijen = [r for r in tekst.splitlines() if r.endswith("| GROOT |")]
        if not rijen:
            continue
        m = re.search(r"^Referentie: .*?run (\d+)", tekst, re.M)
        ref = m.group(1) if m else "onbekend"
        versie = verslag.parent.name.replace(f"beeldverschil-{product}", "").strip("-") or product
        groot = []
        for r in rijen:
            plaatje = r.strip("| ").split(" | ")[0]
            leeg = "| LEEG:" in r
            groot.append(plaatje + (" (LEEG)" if leeg else ""))
            items.append(f"{versie}/{plaatje}:" + ("LEEG" if leeg else f"ref{ref}"))
            if not leeg:
                refs.add(ref)
        per_versie[versie] = groot
    if not per_versie:
        print("geen groot beeldverschil")
        return
    uit = Path(uitmap)
    uit.mkdir(parents=True, exist_ok=True)
    vinger = hashlib.sha1("\n".join(sorted(items)).encode()).hexdigest()[:12]
    sleutel = f"{product} {tak} {vinger}"
    (uit / "sleutel.txt").write_text(sleutel + "\n", encoding="utf-8")
    run = f"https://github.com/{os.environ.get('GITHUB_REPOSITORY', '?')}/actions/runs/{os.environ.get('GITHUB_RUN_ID', '?')}"
    regels = [sleutel, "", f"Run: {run} (verschilbeelden als artefact beeldverschil-*). "
              f"Referentieruns: {', '.join(sorted(refs)) or 'geen'}. LEEG = (bijna) helemaal één kleur.", ""]
    for versie, groot in per_versie.items():
        regels.append(f"- {versie}: {len(groot)} plaatje(s): {', '.join(groot)}")
    (uit / "gemeld.md").write_text("\n".join(regels) + "\n", encoding="utf-8")
    totaal = sum(len(g) for g in per_versie.values())
    (uit / "bericht.md").write_text(
        f"{totaal} plaatje(s) sterk anders dan de vorige geslaagde run of leeg ({', '.join(per_versie)}). "
        "Geen rode test: kijk of het zo bedoeld is.\n", encoding="utf-8")
    print(sleutel)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(2)
    main(*sys.argv[1:])
