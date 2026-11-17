# Telt in de schermafbeeldingen van de bouwstraat hoeveel van het scherm aan staat in het slaapbeeld
# (regel van Garmin voor schermen die kunnen inbranden: onder 10%; onze grens is 8%) en hoeveel px het
# beeld tussen twee slaapbeelden verschuift. Gebruik: python3 tel_slaap.py <map> <horloge> [<horloge> ...]
# Beeld 0 is een wit scherm (het masker), beeld 2 en 3 zijn slaapbeelden. Schrijft regels "SLAAP ..." naar stdout.
import sys
import numpy as np
from PIL import Image

GRENS = 8.0
INBRAND = {"fenix847mm", "venu3s", "vivoactive5", "venusq2"}

def laad(pad):
    return np.asarray(Image.open(pad).convert("RGB")).astype(int)

def tel(wit, slaap):
    """Geeft (scherm_px, aan_px, vak) voor een wit beeld en een slaapbeeld van gelijke maat."""
    masker = (wit.min(axis=2) >= 250) & (slaap.max(axis=2) < 250)
    aan = masker & (slaap.max(axis=2) > 24)
    ys, xs = np.nonzero(aan)
    vak = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())) if len(xs) else None
    return int(masker.sum()), int(aan.sum()), vak

def main(map_, horloges):
    fout = False
    for d in horloges:
        try:
            wit, s2, s3 = (laad(f"{map_}/{d}-{n}.png") for n in (0, 2, 3))
        except OSError as e:
            print(f"SLAAP {d} NIET GEMETEN beeld ontbreekt: {e}")
            continue
        if not (wit.shape == s2.shape == s3.shape):
            print(f"SLAAP {d} NIET GEMETEN maten ongelijk: {wit.shape[:2]} {s2.shape[:2]} {s3.shape[:2]}")
            continue
        n2, a2, v2 = tel(wit, s2)
        n3, a3, v3 = tel(wit, s3)
        if n2 < 20000 or v2 is None or v3 is None:
            if d in INBRAND:
                # Een inbrandscherm dat niet te meten is, is niet gekeurd: dat telt als fout.
                fout = True
                print(f"SLAAP {d} NIET GEMETEN scherm_px={n2} (wit scherm of slaapbeeld niet gevonden) oordeel=FOUT")
            else:
                # Gezien op fr55 (8 kleuren) en instinct2 (zwart-wit), run 43993153363: grijs wordt daar wit of zwart,
                # en wit is niet te onderscheiden van het witte scherm waarmee het masker gemaakt wordt.
                print(f"SLAAP {d} NIET GEMETEN scherm_px={n2} (scherm met weinig kleuren, grijs wordt wit of zwart) oordeel=telt niet (geen inbrandscherm)")
            continue
        p2, p3 = 100.0 * a2 / n2, 100.0 * a3 / n3
        dx, dy = v3[0] - v2[0], v3[1] - v2[1]
        stap = max(abs(dx), abs(dy))
        if d in INBRAND:
            goed = max(p2, p3) < GRENS and 1 <= stap <= 4
            fout = fout or not goed
            oordeel = "goed" if goed else "FOUT"
        else:
            oordeel = "telt niet (geen inbrandscherm)"
        print(f"SLAAP {d} scherm_px={n2} aan={p2:.1f}% en {p3:.1f}% schuif={dx},{dy} oordeel={oordeel}")
    print("SLAAP_TELLING " + ("FOUT" if fout else "goed"))
    return 1 if fout else 0

if __name__ == "__main__":
    # Met --streng faalt de bouwstraat als een inbrandscherm boven de grens zit of niet te meten is.
    args = [a for a in sys.argv[1:] if a != "--streng"]
    code = main(args[0], args[1:])
    sys.exit(code if "--streng" in sys.argv else 0)
