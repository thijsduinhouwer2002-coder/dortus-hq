"""Vult een script-sjabloon met plekken uit de opname (film.json, metingen van OCR) en schrijft het script voor
../stem/montage.py. In het sjabloon mag een beeld hebben:
  "uitsnede": [["@fit_ocr", breedte, dx, dy], [x, y, b]]   een sleutel met @naam neemt de OCR-plek uit metingen
  "nadruk_ocr": ["fit_ocr", halve_breedte, halve_hoogte, dx]  kader rond die plek (dx mag weg)
  "nadruk_rel": [van, tot]                                   bronbeelden vanaf het begin van het deel
Mist een OCR-plek, dan geldt de reserveplek uit RESERVE (gemeten op reeks 4, zelfde scherm).
    python3 vul.py <sjabloon.json> <film.json> <uit.json>"""
import json
import sys

RESERVE = {"fit_ocr": [1360, 1317], "fit_hinge_ocr": [1840, 1317], "clearance_ocr": [1180, 715]}


def plek(m, naam):
    p = m.get(naam)
    return list(p) if p else RESERVE[naam]


def main():
    sj = json.load(open(sys.argv[1]))
    film = json.load(open(sys.argv[2]))
    m, delen = film.get("metingen", {}), film["delen"]
    for sc in sj["scenes"]:
        b = sc["beeld"]
        if "uitsnede" in b:
            uit = []
            for s in b["uitsnede"]:
                if isinstance(s[0], str):
                    x, y = plek(m, s[0].lstrip("@"))
                    uit.append([x + s[2], y + s[3], s[1]])
                else:
                    uit.append(s)
            b["uitsnede"] = uit
        if "nadruk_ocr" in b:
            naam, hb, hh, *dx = b.pop("nadruk_ocr")
            x, y = plek(m, naam)
            x += dx[0] if dx else 0
            b["nadruk"] = [[x - hb, y - hh, x + hb, y + hh]]
        if "nadruk_rel" in b:
            van, tot = b.pop("nadruk_rel")
            d0 = delen[b["deel"]]
            b["nadruk_bron"] = [d0 + van, d0 + tot]
    json.dump(sj, open(sys.argv[3], "w"), indent=1, ensure_ascii=False)
    print("gevuld:", sys.argv[3], {k: m.get(k) for k in RESERVE})


if __name__ == "__main__":
    main()
