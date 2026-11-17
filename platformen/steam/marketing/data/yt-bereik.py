#!/usr/bin/env python3
"""Bereik per maker voor een onbekend spel (Sem, run 13). Per openbaar YouTube-kanaal (curl):
abonnees (kop van het kanaal) en de laatste ±30 video's. Berekent:
- mediaan weergaven van alle recente video's,
- mediaan van de recente video's met idle/desktop/cozy/demo/fest/upcoming/wishlist in de titel (ons soort video),
- die mediaan gedeeld door de abonnees (hoeveel van zijn publiek zo'n video ziet),
- dagen sinds de laatste video en video's in 30 dagen.
Gebruik: python3 yt-bereik.py <uit.csv> /@handle ...   (1,5 s tussen kanalen)"""
import sys, csv, statistics, time, importlib.util, os, re
hier = os.path.dirname(os.path.abspath(__file__))
def laad(naam):
    spec = importlib.util.spec_from_file_location(naam.replace("-", "_"), os.path.join(hier, naam + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
rec, kan = laad("yt-recent"), laad("yt-kanaal")
SOORT = re.compile(rec.WOORDEN.pattern + r"|upcoming|wishlist|new games|hidden gem|first look|you missed|overlooked", re.I)
def abo(s):
    m = re.match(r"([\d.,]+)([KM]?) subscribers", s or "")
    if not m: return None
    return float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6}[m.group(2)]
w = csv.writer(open(sys.argv[1], "w", newline=""))
w.writerow(["handle", "abonnees", "videos_gelezen", "laatste_video_dagen", "videos_30_dagen", "mediaan_alle",
            "n_soort", "mediaan_soort", "soort_per_abonnee", "beste_soort_titel", "beste_soort_weergaven"])
for h in sys.argv[2:]:
    try:
        a = abo(kan.kanaal(h)["abonnees"]); time.sleep(1.5)
        v = rec.lees(h)
    except Exception as e:
        print(h, "fout", e, file=sys.stderr); continue
    g = [(x[0], rec.getal(x[1]), rec.dagen(x[2])) for x in v]
    alle = [x[1] for x in g if x[1] is not None]
    srt = [x for x in g if x[1] is not None and SOORT.search(x[0])]
    d = [x[2] for x in g if x[2] is not None]
    ms = statistics.median([x[1] for x in srt]) if srt else None
    best = max(srt, key=lambda x: x[1]) if srt else ("", None)
    w.writerow([h, int(a) if a else "", len(v), min(d) if d else "", sum(1 for x in d if x <= 30),
                int(statistics.median(alle)) if alle else "", len(srt), int(ms) if ms else "",
                round(ms / a, 2) if ms and a else "", best[0][:90], int(best[1]) if best[1] else ""])
    print(h, a, len(v), len(srt), file=sys.stderr)
    time.sleep(1.5)
