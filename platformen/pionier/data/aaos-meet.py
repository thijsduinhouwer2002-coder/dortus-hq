#!/usr/bin/env python3
"""Herhaalmeting Android Automotive (Google built-in): installs van apps die alleen voor de auto zijn.
Bron: openbare app-pagina's van AppGoblin (schattingen, label DERDEN) en Google Play (installs-bucket, GEZIEN).
Gebruik: python3 aaos-meet.py  -> voegt regels toe aan aaos.csv"""
import csv, datetime, html, re, urllib.request, os
APPS = ["com.foreca.car.automotive", "com.vivaldi.browser.automotive", "mobi.byss.weather.navigation"]
UA = {"User-Agent": "Mozilla/5.0 (Dortus-meting)"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8", "ignore")
def tekst(h):
    h = re.sub(r"(?s)<(script|style).*?</\1>", "", h)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h)))
pad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aaos.csv")
nieuw = not os.path.exists(pad)
with open(pad, "a", newline="") as f:
    w = csv.writer(f)
    if nieuw:
        w.writerow(["datum", "app", "appgoblin_installs", "appgoblin_4weken", "play_bucket"])
    for a in APPS:
        try:
            t = tekst(get("https://appgoblin.info/apps/" + a))
            tot = re.search(r"about ([\d.,]+K?M?)\+ installs", t)
            mnd = re.search(r"\(\s*([\d.,]+K?)\s*over 4 weeks", t)
        except Exception as e:
            tot = mnd = None
        try:
            p = get("https://play.google.com/store/apps/details?id=%s&hl=en" % a)
            b = re.search(r">([\d.,]+[KMB]?\+)</div><div[^>]*>Downloads", p)
        except Exception:
            b = None
        rij = [datetime.date.today().isoformat(), a, tot.group(1) if tot else "", mnd.group(1) if mnd else "", b.group(1) if b else ""]
        w.writerow(rij); print(rij)
