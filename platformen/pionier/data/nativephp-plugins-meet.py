#!/usr/bin/env python3
"""Meet de NativePHP Plugin Marketplace (Noor, pionier). Alleen lezen, rustig.

Telt alle plugins op https://nativephp.com/plugins/marketplace (pagina's ?page=N),
haalt per plugin prijs, maker en "last updated" op, en telt op Packagist
de pakketten van type nativephp-plugin met hun eerste release per maand.
Schrijft een regel bij in nativephp-plugins.csv en de details in nativephp-plugins-<datum>.json.

Gebruik: python3 nativephp-plugins-meet.py   (duurt ±3 minuten)
"""
import csv, datetime, html, json, os, re, time, urllib.request
from collections import Counter

UA = {"User-Agent": "Mozilla/5.0 (dortus-onderzoek, alleen lezen)"}
HIER = os.path.dirname(os.path.abspath(__file__))


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


def tekstregels(s):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return [l.strip() for l in t.split("\n") if l.strip() and len(l.strip()) < 80]


def plugins_lijst():
    slugs = []
    for p in range(1, 40):
        s = get(f"https://nativephp.com/plugins/marketplace?page={p}")
        nieuw = sorted(set(re.findall(r'href="https://nativephp.com/plugins/([a-z0-9_-]+/[a-z0-9_-]+)"', s)))
        nieuw = [x for x in nieuw if x not in slugs]
        if not nieuw:
            break
        slugs += nieuw
        time.sleep(1)
    return slugs


def plugin_info(slug):
    regels = tekstregels(get(f"https://nativephp.com/plugins/{slug}"))
    info = {"slug": slug, "prijs": 0, "maker": slug.split("/")[0], "versie": "", "bijgewerkt": "", "ultra_prijs": None}
    for i, l in enumerate(regels):
        m = re.match(r"^\$(\d+)$", l)
        if m and i + 1 < len(regels) and "purchase" in regels[i + 1].lower():
            info["prijs"] = int(m.group(1))
        m = re.match(r"Get this plugin for \$(\d+) with Ultra", l)
        if m:
            info["ultra_prijs"] = int(m.group(1))
        if l == "Author" and i + 1 < len(regels):
            info["maker_naam"] = regels[i + 1]
        if l == "Version" and i + 1 < len(regels):
            info["versie"] = regels[i + 1]
        if l.startswith("Last updated"):
            info["bijgewerkt"] = l.replace("Last updated ", "")
    return info


def packagist():
    namen = json.loads(get("https://packagist.org/packages/list.json?type=nativephp-plugin"))["packageNames"]
    try:
        namen += json.loads(get("https://packagist.org/packages/list.json?type=nativephp-ui-plugin"))["packageNames"]
    except Exception:
        pass
    rijen = []
    for n in sorted(set(namen)):
        try:
            d = json.loads(get(f"https://packagist.org/packages/{n}.json"))["package"]
            tijden = [v.get("time", "") for v in d.get("versions", {}).values() if v.get("time")]
            rijen.append({"naam": n, "eerste": min(tijden)[:7] if tijden else "",
                          "downloads": d.get("downloads", {}).get("total", 0),
                          "maand": d.get("downloads", {}).get("monthly", 0)})
        except Exception:
            rijen.append({"naam": n, "eerste": "", "downloads": 0, "maand": 0})
        time.sleep(0.3)
    return rijen


def main():
    nu = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    slugs = plugins_lijst()
    infos = []
    for s in slugs:
        try:
            infos.append(plugin_info(s))
        except Exception as e:
            infos.append({"slug": s, "fout": str(e)})
        time.sleep(0.7)
    pk = packagist()
    betaald = [x for x in infos if x.get("prijs")]
    eigen = [x for x in infos if x["slug"].startswith("nativephp/")]
    derden_betaald = [x for x in betaald if not x["slug"].startswith("nativephp/")]
    per_maand = Counter(r["eerste"] for r in pk if r["eerste"])
    samenvatting = {
        "datum": nu,
        "plugins_winkel": len(infos),
        "eigen_nativephp": len(eigen),
        "makers": len({x["maker"] for x in infos}),
        "betaald": len(betaald),
        "betaald_derden": len(derden_betaald),
        "makers_betaald_derden": len({x["maker"] for x in derden_betaald}),
        "prijzen": dict(Counter(x["prijs"] for x in betaald)),
        "packagist_pakketten": len(pk),
        "packagist_nieuw_per_maand": dict(sorted(per_maand.items())),
        "packagist_downloads_derden_totaal": sum(r["downloads"] for r in pk if not r["naam"].startswith("nativephp/")),
    }
    with open(os.path.join(HIER, f"nativephp-plugins-{nu}.json"), "w") as f:
        json.dump({"samenvatting": samenvatting, "plugins": infos, "packagist": pk}, f, indent=1)
    pad = os.path.join(HIER, "nativephp-plugins.csv")
    nieuw_bestand = not os.path.exists(pad)
    with open(pad, "a", newline="") as f:
        w = csv.writer(f)
        if nieuw_bestand:
            w.writerow(["datum", "plugins_winkel", "eigen", "makers", "betaald", "betaald_derden", "makers_betaald_derden", "packagist_pakketten"])
        w.writerow([nu, len(infos), len(eigen), samenvatting["makers"], len(betaald), len(derden_betaald),
                    samenvatting["makers_betaald_derden"], len(pk)])
    print(json.dumps(samenvatting, indent=1))


if __name__ == "__main__":
    main()
