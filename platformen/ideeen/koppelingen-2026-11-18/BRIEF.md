# Opdracht: nieuwe koppelingen naar nieuwe tools (18 nov 2026, 23:15)

Van Thijs: "zoeken hoe we onze workflow kunnen verbeteren met nieuwe koppelingen naar nieuwe tools, via GitHub en andere kanalen, ik denk echt dat hier winst ligt." Een half uur, vijf zoekers (A tot E), elk een eigen hoek.

## Wat telt als winst
Een koppeling telt alleen als ze één van deze twee doet:
1. **Tijd of fouten besparen** bij bouwen, testen, uitbrengen of meten (agents hoeven minder op Thijs te wachten, minder handwerk, minder kans op fouten).
2. **Bereik opleveren**: meer mensen zien of installeren onze producten (Click Joints, Bison & Flex, Rollwright, Hats of the Fallen).
Gereedschap om het gereedschap telt niet.

## Wat we al hebben (niet opnieuw voorstellen)
Lees `organisatie/toegang.md` (alle sleutels en accounts) en `platformen/ideeen/afkijken-2026-11-18/K-ai-opzet-5-voorbeelden.md` (wat winnaars al gebruiken). Al in gebruik: GitHub Actions, Context7 (`.mcp.json`), Metricool (Free), Kit, Gumroad, Discord-webhook, Google Alerts, Search Console, Amami, automatische Claude-keurder, hooks in `.claude/settings.json`. Playwright werkt niet in onze omgeving (browser-download geweigerd).

## Onze omgeving (belangrijk)
- Agents draaien in een cloudomgeving met een netwerk-allowlist: npm, pip en GitHub werken, de meeste andere sites niet vanuit de shell. Een koppeling die tijdens het werk naar een externe API moet, werkt misschien niet in een agentsessie, maar wel in GitHub Actions (daar is het netwerk open). Zeg per voorstel waar het zou draaien.
- Test wat je kunt testen (npm-pakket installeren, `npx` starten, een openbare API met curl). Zet erbij of je het getest hebt.

## Regels
- Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
- Geen accounts aanmaken, niets kopen, niets plaatsen, niemand benaderen. Wat dat nodig heeft, zet je als "stap voor Thijs" in je verslag.
- Elk cijfer krijgt GEZIEN, DERDEN (met link) of GOK.

## Verslag
Schrijf `platformen/ideeen/koppelingen-2026-11-18/<letter>-<hoek>.md`:
1. **Top 5**, per voorstel: wat het is (in gewone woorden), welk probleem van ons het oplost (noem het product of de stap), hoe het koppelt (MCP, API, GitHub Action, CLI), waar het draait (agentsessie of Actions), kosten (gratis tot welke grens), getest ja/nee en wat je zag, moeite om in te bouwen (uren, GOK), en wat Thijs ervoor moet doen.
2. **Afgevallen**: wat je bekeek en waarom niet (één regel per stuk).
3. **Bronnen**: links.
Commit en push je bestand (`git pull --rebase` eerst, nooit geforceerd).
