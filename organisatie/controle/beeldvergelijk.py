#!/usr/bin/env python3
"""Beeldvergelijking (roestronde R4): schermafbeeldingen van deze run naast die van de vorige geslaagde run.

Gebruik: python3 beeldvergelijk.py <nu-map> <ref-map> <uit-map> <grens-procent> <naam> [maskers]

maskers: vakken die niet meetellen omdat ze elke run anders zijn, gescheiden door ';', elk als
<bestandspatroon>[@<breedte>x<hoogte>]:<x0>,<y0>,<x1>,<y1> (pixels, x1 en y1 tellen niet mee), bijvoorbeeld de
willekeurige kluisnaam van Obsidian: "*:50,755,345,800". Met @2880x1800 geldt het vak alleen voor plaatjes van
die maat (zo dekt een masker voor het hele IDE-venster de kopregel van een dialoog niet af).

Per PNG die in beide mappen staat: aantal pixels dat verschilt (een kanaal wijkt meer dan DREMPEL af,
zodat zachte randen niet tellen), als procent van het plaatje. Boven de grens heet het "groot" en komt er
een verschilbeeld bij (het oude plaatje grijs, de verschillen rood). Een andere maat telt als groot, behalve als
hij hooguit MAAT_SPELING pixels scheelt: losse dialoogvensters van de IDE springen tussen runs een paar pixels
(1600x1174 en 1592x1172, keuring R4). Dan wordt toch vergeleken: een pixel telt alleen als anders als hij ook niet
klopt met het nieuwe plaatje verschoven naar rechts, onder of rechtsonder (zo kloppen knoppen die aan de rechter- of
onderkant vastzitten), en het verschil telt net zo tegen de grens.
Nieuwe en verdwenen plaatjes staan in het verslag maar tellen niet als groot.
Een plaatje van deze run dat (bijna) helemaal één kleur is (standaardafwijking onder LEEG_GRENS, bijvoorbeeld
helemaal zwart) telt altijd als groot, met "LEEG", ook als de referentie net zo leeg is (keuring R5: 1-paneel.png
en 10-winkel-paneel.png waren sinds 8 nov zwart en heetten "gelijk").

Nooit een rode stap: het verslag (verslag.md) en de verschilbeelden zijn voor de keurder.
Schrijft groot=<aantal> en verslag=<pad> naar GITHUB_OUTPUT als die bestaat.
Nodig: Pillow en numpy.
"""
import fnmatch
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image

DREMPEL = 24  # van 255 per kanaal
MAAT_SPELING = 16  # pixels
LEEG_GRENS = 2.0  # standaardafwijking van de pixelwaarden


def laad(pad):
    return np.asarray(Image.open(pad).convert("RGB"), dtype=np.int16)


def verschilbeeld(oud, mask, pad):
    grijs = (oud.mean(axis=2, keepdims=True) * 0.35 + 140).clip(0, 255)
    beeld = np.repeat(grijs, 3, axis=2).astype(np.uint8)
    beeld[mask] = (230, 20, 20)
    pad.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(beeld).save(pad)


def lees_maskers(tekst):
    maskers = []
    for deel in filter(None, (tekst or "").split(";")):
        patroon, vak = deel.rsplit(":", 1)
        maskers.append((patroon.strip(), [int(v) for v in vak.split(",")]))
    return maskers


def past(patroon, rel, vorm):
    naam, _, maat = patroon.partition("@")
    if maat and maat != f"{vorm[1]}x{vorm[0]}":
        return False
    return fnmatch.fnmatch(rel, naam)


def verschil_verschoven(a, b):
    """Masker op de maat van a: anders als b op geen van de vier hoekuitlijningen klopt."""
    ha, wa, hb, wb = a.shape[0], a.shape[1], b.shape[0], b.shape[1]
    dy, dx = hb - ha, wb - wa
    mask = np.ones((ha, wa), dtype=bool)
    for sy, sx in ((0, 0), (dy, 0), (0, dx), (dy, dx)):
        y0, y1 = max(0, -sy), min(ha, hb - sy)
        x0, x1 = max(0, -sx), min(wa, wb - sx)
        if y1 <= y0 or x1 <= x0:
            continue
        deel = (np.abs(a[y0:y1, x0:x1] - b[y0 + sy:y1 + sy, x0 + sx:x1 + sx]) > DREMPEL).any(axis=2)
        mask[y0:y1, x0:x1] &= deel
    return mask


def vergelijk(nu, ref, uit, grens, naam, maskers=""):
    maskers = lees_maskers(maskers)
    nu, ref, uit = Path(nu), Path(ref), Path(uit)
    uit.mkdir(parents=True, exist_ok=True)
    nieuw_lijst = {p.relative_to(nu).as_posix() for p in nu.rglob("*.png")} if nu.is_dir() else set()
    ref_lijst = {p.relative_to(ref).as_posix() for p in ref.rglob("*.png")} if ref.is_dir() else set()
    regels, groot = [], []
    opmerking = "" if ref_lijst else f"Nog geen referentie voor {naam}: deze run wordt de referentie als hij groen is.\n"
    for rel in sorted(nieuw_lijst):
        try:
            sd = float(laad(nu / rel).std())
        except Exception as e:  # kapot plaatje: melden, niet stoppen
            groot.append(rel)
            regels.append(f"| {rel} | niet te lezen: {e} | GROOT |")
            continue
        if sd < LEEG_GRENS:
            groot.append(rel)
            regels.append(f"| {rel} | LEEG: (bijna) helemaal één kleur (standaardafwijking {sd:.2f}) | GROOT |")
    for rel in sorted(nieuw_lijst & ref_lijst):
        if rel in groot:
            continue
        try:
            a, b = laad(ref / rel), laad(nu / rel)
        except Exception as e:
            regels.append(f"| {rel} | referentie niet te lezen: {e} | |")
            continue
        notitie = ""
        if a.shape != b.shape and abs(a.shape[0] - b.shape[0]) <= MAAT_SPELING and abs(a.shape[1] - b.shape[1]) <= MAAT_SPELING:
            notitie = f" (maat {a.shape[1]}x{a.shape[0]} werd {b.shape[1]}x{b.shape[0]}, vergeleken met verschuiving)"
            mask = verschil_verschoven(a, b)
        elif a.shape != b.shape:
            groot.append(rel)
            regels.append(f"| {rel} | andere maat: {a.shape[1]}x{a.shape[0]} werd {b.shape[1]}x{b.shape[0]} | GROOT |")
            continue
        else:
            mask = (np.abs(a - b) > DREMPEL).any(axis=2)
        for patroon, (x0, y0, x1, y1) in maskers:
            if past(patroon, rel, a.shape):
                mask[y0:y1, x0:x1] = False
        n = int(mask.sum())
        pct = 100.0 * n / mask.size
        if n == 0:
            regels.append(f"| {rel} | gelijk{notitie} | |")
            continue
        ys, xs = np.nonzero(mask)
        vak = f"x {xs.min()} tot {xs.max()}, y {ys.min()} tot {ys.max()}"
        if pct > grens:
            groot.append(rel)
            verschilbeeld(a, mask, uit / "verschil" / rel)
            regels.append(f"| {rel} | {n} px ({pct:.3f}%), {vak}{notitie} | GROOT |")
        else:
            regels.append(f"| {rel} | {n} px ({pct:.3f}%), ruis{notitie} | |")
    for rel in sorted(nieuw_lijst - ref_lijst):
        if ref_lijst:
            regels.append(f"| {rel} | nieuw (niet in de referentie) | |")
    for rel in sorted(ref_lijst - nieuw_lijst):
        regels.append(f"| {rel} | verdwenen (wel in de referentie) | |")
    kop = [
        f"## Beeldvergelijking {naam}",
        f"GROOT: {len(groot)} (grens {grens}% van de pixels, drempel {DREMPEL}/255 per kanaal; "
        f"{len(nieuw_lijst & ref_lijst)} plaatjes vergeleken"
        + (f"; niet meegeteld: {'; '.join(f'{p} {v}' for p, v in maskers)})" if maskers else ")"),
        f"Referentie: {os.environ.get('BV_REF', 'onbekend')}",
        opmerking,
        "| plaatje | verschil met de vorige geslaagde run | |",
        "|---|---|---|",
    ]
    tekst = "\n".join(kop + regels) + "\n"
    (uit / "verslag.md").write_text(tekst, encoding="utf-8")
    print(tekst)
    if groot:
        print(f"BEELDVERSCHIL GROOT {naam}: " + ", ".join(groot))
    uitvoer = os.environ.get("GITHUB_OUTPUT")
    if uitvoer:
        with open(uitvoer, "a", encoding="utf-8") as f:
            f.write(f"groot={len(groot)}\nverslag={uit / 'verslag.md'}\n")
    samenvatting = os.environ.get("GITHUB_STEP_SUMMARY")
    if samenvatting:
        with open(samenvatting, "a", encoding="utf-8") as f:
            f.write(tekst + "\n")
    return len(groot)


if __name__ == "__main__":
    if len(sys.argv) not in (6, 7):
        print(__doc__)
        sys.exit(2)
    vergelijk(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5], sys.argv[6] if len(sys.argv) == 7 else "")
