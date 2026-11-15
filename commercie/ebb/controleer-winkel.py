# Chris, 15 nov 2026: winkelpagina van een Garmin-app nalopen tegen de plakteksten.
# Gebruik: python3 controleer-winkel.py <winkel-id> <voorvoegsel> [vergelijk-id]
#   voorvoegsel: calm of ebb (leest platformen/garmin/upload/<voorvoegsel>-en|de|nl.md)
#   vergelijk-id: optioneel een andere app (bijv. Ebb) om de horlogelijst naast te leggen.
# Voorbeeld voor Calm: python3 controleer-winkel.py bcc58192-667b-4bd8-a824-e6fe26794466 calm 5280653d-1681-452d-8c03-7cbdc7284641
# Leest alleen de openbare winkel-API met curl. Schrijft niets.
import json, os, re, subprocess, sys

B = "https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/"
HIER = os.path.dirname(os.path.abspath(__file__))
UPLOAD = os.path.join(HIER, "..", "..", "platformen", "garmin", "upload")


def haal(app_id):
    r = subprocess.run(["curl", "-s", "--max-time", "40", B + app_id], capture_output=True, text=True).stdout
    try:
        return json.loads(r)
    except ValueError:
        return {"fout": r[:200]}


def blok(tekst, kop):
    # eerste ```-blok na de kop die met <kop> begint
    i = tekst.find("\n## " + kop)
    if i < 0:
        return None
    m = re.search(r"```\n(.*?)\n```", tekst[i:], re.S)
    return m.group(1).strip() if m else None


def gewoon(s):
    s = s.replace("\r", "")
    s = re.sub(r"\n?Tags:.*$", "", s.strip())  # Tags-regel mag ontbreken als er een apart veld was
    return re.sub(r"\s+", " ", s).strip()


def main():
    app_id, voor = sys.argv[1], sys.argv[2]
    d = haal(app_id)
    if "status" not in d:
        print("NIET OPENBAAR:", d.get("message") or d.get("fout"))
        return 1
    goed = True
    print("status", d["status"], "| versie", d.get("latestExternalVersion"), "| downloads", d.get("downloadCount"))
    if d["status"] != "APPROVED":
        print("  FOUT: status is niet APPROVED"); goed = False
    prijs = ((d.get("pricing") or {}).get("listPrice") or {}).get("price")
    print("prijs (listPrice):", prijs if prijs is not None else "NIET GEZIEN", "| paymentModel", d.get("paymentModel"), "| trial", d.get("hasTrialMode"))
    if voor == "calm" and prijs != 0:
        print("  FOUT: Calm hoort gratis te zijn (of prijs niet te lezen)"); goed = False
    nb = len(d.get("screenshotFileIds") or [])
    print("beelden:", nb, "| icoon:", bool(d.get("iconFileId")))
    if nb != 5:
        print("  FOUT: 5 beelden verwacht"); goed = False
    print("horloges (artikelnummers):", len(d.get("compatibleDevicePartNumbers") or []))
    if len(sys.argv) > 3:
        e = haal(sys.argv[3])
        a, b = set(d.get("compatibleDevicePartNumbers") or []), set(e.get("compatibleDevicePartNumbers") or [])
        print("  naast vergelijk-app:", len(b), "| alleen hier:", len(a - b), "| ontbreekt hier:", len(b - a))
    loc = {l["locale"]: l for l in d.get("appLocalizations", [])}
    for taal in ("en", "de", "nl"):
        pad = os.path.join(UPLOAD, f"{voor}-{taal}.md")
        t = open(pad, encoding="utf-8").read()
        l = loc.get(taal)
        if not l:
            print(f"[{taal}] ONTBREEKT in de winkel"); goed = False; continue
        titel, lang, nieuw = blok(t, "Titel"), blok(t, "Lange beschrijving"), blok(t, "Wat is nieuw")
        ok_t = l["name"].strip() == titel
        ok_l = gewoon(l["description"]) == gewoon(lang)
        ok_n = (l.get("whatsNew") or "").strip() == (nieuw or "")
        print(f"[{taal}] titel {'gelijk' if ok_t else 'ANDERS'} | lange tekst {'gelijk' if ok_l else 'ANDERS'} | wat is nieuw {'gelijk' if ok_n else 'ANDERS'}")
        if not ok_t:
            print("   winkel:", l["name"], "\n   plak:  ", titel)
        if not ok_l:
            w, p = gewoon(l["description"]), gewoon(lang)
            n = next((i for i in range(min(len(w), len(p))) if w[i] != p[i]), min(len(w), len(p)))
            print(f"   eerste verschil op teken {n}:\n   winkel: ...{w[max(0,n-40):n+60]}\n   plak:   ...{p[max(0,n-40):n+60]}")
        goed = goed and ok_t and ok_l and ok_n
    print("UITKOMST:", "alles gelijk" if goed else "verschillen, zie boven")
    print("winkellink: https://apps.garmin.com/apps/" + app_id)
    return 0 if goed else 2


if __name__ == "__main__":
    sys.exit(main())
