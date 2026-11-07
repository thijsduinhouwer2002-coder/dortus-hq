#!/usr/bin/env python3
"""Herhaalmeting ChatGPT-plugindirectory (Noor). Leest de openbare statistiekpagina van
pluginsradar.com en voegt een regel toe aan chatgpt-plugins.csv naast dit script.
Gebruik: python3 chatgpt-plugins-meet.py"""
import csv, datetime, html, os, re, urllib.request

URL = "https://pluginsradar.com/chatgpt/stats"
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
t = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
t = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", "", t)
t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))

def num(pat):
    m = re.search(pat, t)
    return m.group(1).replace(",", "") if m else ""

rij = {
    "datum": datetime.date.today().isoformat(),
    "vermeld": num(r"Plugins listed ([\d,]+)"),
    "apps": num(r"([\d,]+) apps ·"),
    "terug_in_zoeken": num(r"Come back in ChatGPT.s plugin search ([\d,]+)"),
    "nieuw_per_dag": num(r"New per day ~([\d,]+)"),
    "alleen_zoeken": num(r"Search only ([\d,]+)"),
}
pad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatgpt-plugins.csv")
nieuw = not os.path.exists(pad)
with open(pad, "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rij))
    if nieuw:
        w.writeheader()
    w.writerow(rij)
print(rij)
