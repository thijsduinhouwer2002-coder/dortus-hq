#!/usr/bin/env python3
"""Leest een openbaar YouTube-kanaal (met curl): abonnees, aantal video's, land, beschrijving,
en een zakelijk mailadres alleen als het kanaal dat zelf in zijn openbare beschrijving zet.
Gebruik: python3 yt-kanaal.py /@handle"""
import sys, re, json, subprocess
def kanaal(h):
    url = "https://www.youtube.com" + h + "/about?hl=en&gl=US"
    html = subprocess.run(["curl", "-sL", "--max-time", "30", "-H", "Accept-Language: en-US,en;q=0.9",
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36", url],
        capture_output=True, text=True).stdout
    def f(p):
        m = re.search(p, html); return m.group(1) if m else ""
    beschr = f(r'"description":"((?:[^"\\]|\\.)*)"')
    try: beschr = json.loads('"' + beschr + '"')
    except Exception: pass
    mails = sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", beschr)))
    return {"handle": h,
        # Eerst de kop van het kanaal zelf ("content"); het eerste "subscribers" op de pagina
        # kan van een ander (uitgelicht) kanaal zijn. Fout gevonden 16 nov run 5 (Kripparrian, Krayn).
        "abonnees": f(r'"content":"([\d.,]+[KM]? subscribers)"') or f(r'"([\d.,]+[KM]? subscribers)"'),
        "videos": f(r'"([\d,]+ videos)"'),
        "land": f(r'"country":"([^"]*)"'),
        "beschrijving": beschr[:400],
        "mail_in_beschrijving": mails,
        "zakelijk_knop": "businessEmail" in html or "View email address" in html}
if __name__ == "__main__":
    print(json.dumps(kanaal(sys.argv[1]), ensure_ascii=False))
