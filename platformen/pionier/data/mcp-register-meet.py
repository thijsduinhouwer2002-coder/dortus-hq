#!/usr/bin/env python3
"""Telt het officiele MCP-register (registry.modelcontextprotocol.io) en de officiele
Claude Code plugin-marketplace. Herhaalmeting: python3 mcp-register-meet.py
Per servernaam telt de vroegste publishedAt als 'nieuw in maand'. Rustig: 0,3 s per pagina."""
import json, time, urllib.request, urllib.parse, collections, datetime, sys
B = "https://registry.modelcontextprotocol.io/v0/servers"
first, latest, remote = {}, {}, set()
cur, pages = None, 0
while True:
    q = {"limit": "100"}
    if cur: q["cursor"] = cur
    for poging in range(6):
        try:
            with urllib.request.urlopen(B + "?" + urllib.parse.urlencode(q), timeout=60) as r:
                d = json.load(r)
            break
        except Exception as e:
            print("opnieuw", pages, e, file=sys.stderr); time.sleep(3 * (poging + 1))
    else:
        raise SystemExit("register geeft steeds fouten")
    for s in d.get("servers", []):
        n = s["server"]["name"]; m = s["_meta"]["io.modelcontextprotocol.registry/official"]
        p = m["publishedAt"][:7]
        if n not in first or p < first[n]: first[n] = p
        if s["server"].get("remotes"): remote.add(n)
    pages += 1
    if pages % 50 == 0: print("pagina", pages, len(first), file=sys.stderr, flush=True)
    cur = d.get("metadata", {}).get("nextCursor")
    if not cur: break
    time.sleep(0.3)
per = collections.Counter(first.values())
ns = collections.Counter(n.split("/")[0] for n in first)
out = {"gemeten": datetime.datetime.utcnow().isoformat()[:16], "servers_uniek": len(first),
       "met_remote": len(remote), "nieuw_per_maand": dict(sorted(per.items())),
       "namespaces": len(ns)}
mp = json.load(urllib.request.urlopen("https://raw.githubusercontent.com/anthropics/claude-plugins-official/main/.claude-plugin/marketplace.json", timeout=60))
out["claude_plugins_official"] = len(mp["plugins"])
print(json.dumps(out, indent=1))
