#!/usr/bin/env python3
"""Beeldvergelijking (roestronde R4): schermafbeeldingen van deze run naast die van de vorige geslaagde run.

Gebruik: python3 beeldvergelijk.py <nu-map> <ref-map> <uit-map> <grens-procent> <naam>

Per PNG die in beide mappen staat: aantal pixels dat verschilt (een kanaal wijkt meer dan DREMPEL af,
zodat zachte randen niet tellen), als procent van het plaatje. Boven de grens heet het "groot" en komt er
een verschilbeeld bij (het oude plaatje grijs, de verschillen rood). Een andere maat telt ook als groot.
Nieuwe en verdwenen plaatjes staan in het verslag maar tellen niet als groot.

Nooit een rode stap: het verslag (verslag.md) en de verschilbeelden zijn voor de keurder.
Schrijft groot=<aantal> en verslag=<pad> naar GITHUB_OUTPUT als die bestaat.
Nodig: Pillow en numpy.
"""
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image

DREMPEL = 24  # van 255 per kanaal


def laad(pad):
    return np.asarray(Image.open(pad).convert("RGB"), dtype=np.int16)


def verschilbeeld(oud, mask, pad):
    grijs = (oud.mean(axis=2, keepdims=True) * 0.35 + 140).clip(0, 255)
    beeld = np.repeat(grijs, 3, axis=2).astype(np.uint8)
    beeld[mask] = (230, 20, 20)
    pad.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(beeld).save(pad)


def vergelijk(nu, ref, uit, grens, naam):
    nu, ref, uit = Path(nu), Path(ref), Path(uit)
    uit.mkdir(parents=True, exist_ok=True)
    nieuw_lijst = {p.relative_to(nu).as_posix() for p in nu.rglob("*.png")} if nu.is_dir() else set()
    ref_lijst = {p.relative_to(ref).as_posix() for p in ref.rglob("*.png")} if ref.is_dir() else set()
    regels, groot = [], []
    opmerking = "" if ref_lijst else f"Nog geen referentie voor {naam}: deze run wordt de referentie als hij groen is.\n"
    for rel in sorted(nieuw_lijst & ref_lijst):
        try:
            a, b = laad(ref / rel), laad(nu / rel)
        except Exception as e:  # kapot plaatje: melden, niet stoppen
            regels.append(f"| {rel} | niet te lezen: {e} | |")
            continue
        if a.shape != b.shape:
            groot.append(rel)
            regels.append(f"| {rel} | andere maat: {a.shape[1]}x{a.shape[0]} werd {b.shape[1]}x{b.shape[0]} | GROOT |")
            continue
        mask = (np.abs(a - b) > DREMPEL).any(axis=2)
        n = int(mask.sum())
        pct = 100.0 * n / mask.size
        if n == 0:
            regels.append(f"| {rel} | gelijk | |")
            continue
        ys, xs = np.nonzero(mask)
        vak = f"x {xs.min()} tot {xs.max()}, y {ys.min()} tot {ys.max()}"
        if pct > grens:
            groot.append(rel)
            verschilbeeld(a, mask, uit / "verschil" / rel)
            regels.append(f"| {rel} | {n} px ({pct:.3f}%), {vak} | GROOT |")
        else:
            regels.append(f"| {rel} | {n} px ({pct:.3f}%), ruis | |")
    for rel in sorted(nieuw_lijst - ref_lijst):
        if ref_lijst:
            regels.append(f"| {rel} | nieuw (niet in de referentie) | |")
    for rel in sorted(ref_lijst - nieuw_lijst):
        regels.append(f"| {rel} | verdwenen (wel in de referentie) | |")
    kop = [
        f"## Beeldvergelijking {naam}",
        f"GROOT: {len(groot)} (grens {grens}% van de pixels, drempel {DREMPEL}/255 per kanaal; "
        f"{len(nieuw_lijst & ref_lijst)} plaatjes vergeleken)",
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
    if len(sys.argv) != 6:
        print(__doc__)
        sys.exit(2)
    vergelijk(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5])
