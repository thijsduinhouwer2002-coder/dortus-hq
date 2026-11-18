# Opdracht: nieuwe koppelingen naar nieuwe tools (18 nov 2026, 23:15)

Van Thijs: "zoeken hoe we onze workflow kunnen verbeteren met nieuwe koppelingen naar nieuwe tools, via GitHub en andere kanalen, ik denk echt dat hier winst ligt." Een half uur, vijf zoekers (A tot E), elk een eigen hoek.

## Wat telt als winst (bijgesteld door Thijs 23:14)
1. **Vooral distributie**: koppelingen waardoor meer mensen onze producten zien, wishlisten of installeren (Click Joints, Bison & Flex, Rollwright, Hats of the Fallen), en die agents zelf kunnen bedienen of meten.
2. **Daarna kwaliteit van de apps**: koppelingen waardoor we fouten, crashes en klachten eerder zien of beter testen.
Gereedschap om het gereedschap telt niet.

Let op harde regel 4: niets naar buiten onder de naam van Thijs zonder zijn ja op de tekst. Een koppeling die zelf post, mag; de tekst gaat dan eerst langs Thijs of (als hij dat later kiest) langs een keuring. Zeg per voorstel hoe dat zou lopen.

## Hoeken
- **A. Posten en plannen:** sociale kanalen en hun API's of MCP's (YouTube, TikTok, Reddit, Bluesky, Mastodon, X, Postiz, Buffer, alternatieven voor Metricool Free), zodat agents filmpjes en posts klaarzetten en cijfers lezen.
- **B. Gevonden worden in winkels en zoekmachines:** Steam (wishlists volgen, curators, persmensen, streamers, keys), Blender extensions, JetBrains Marketplace, Obsidian, Gumroad, awesome-lijsten, Product Hunt, SEO voor dortus.com.
- **C. Community en mond-tot-mond:** Discord-bots, meldingen als iemand ergens over ons of ons soort product praat (Reddit, Hacker News, forums), maillijst laten groeien, reviews en sterren uitlokken, verwijzingen.
- **D. Wat makers op GitHub inzetten voor distributie:** zoek in echte repo's naar workflows en tools die bij een release vanzelf aankondigen, posten, nieuwsbrieven sturen of winkels bijwerken; plus Claude Code plugins, skills en MCP's die op marketing gericht zijn.
- **E. Kwaliteit:** crash- en foutmeldingen uit de apps (Godot, Blender, JetBrains, Obsidian), beter testen (Godot-testtools, beeldvergelijking, plugin verifier), feedback van gebruikers binnenhalen.

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
