#!/usr/bin/env python3
"""Herhaalmeting Ableton Live Extensions (Noor, 8 nov 2026).
Telt (1) nieuwe GitHub-repo's per maand met 'ableton extension' via gh api,
(2) extensies op liveextensions.co per maand van lastmod in de sitemap.
Draai: python3 -I data/ableton-extensions-meet.py"""
import collections, json, re, subprocess, time, urllib.request

def gh_count(maand):
    out = subprocess.run(["gh", "api", "-X", "GET", "search/repositories", "-f",
                          f"q=ableton extension created:{maand}", "--jq", ".total_count"],
                         capture_output=True, text=True)
    return out.stdout.strip()

maanden = ["2026-06", "2026-07", "2026-08", "2026-09", "2026-10", "2026-11", "2026-12", "2027-01"]
print("GitHub-repo's 'ableton extension' per maand:")
for m in maanden:
    print(" ", m, gh_count(m)); time.sleep(2)

req = urllib.request.Request("https://liveextensions.co/sitemap.xml", headers={"User-Agent": "Mozilla/5.0"})
s = urllib.request.urlopen(req, timeout=30).read().decode()
ext = re.findall(r"<loc>https://liveextensions.co/extensions/([^<]+)</loc>\s*<lastmod>([^<]+)", s)
print("liveextensions.co extensies:", len(ext))
print("per maand (lastmod):", dict(sorted(collections.Counter(d[:7] for _, d in ext).items())))
