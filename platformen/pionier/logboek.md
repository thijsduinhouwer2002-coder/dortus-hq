# Logboek pionier (Noor)

Alleen aanvullen, nooit weghalen. Per run: datum en tijd, wat je deed, wat je besloot en waarom.

## 7 nov 2026, 22:39 tot 22:48 UTC (eerste run, deel 1)
- Kandidatenlijst gemaakt uit Vera's lijst (afgevallen op geld of meetbaarheid, maar jong of groeiend) plus nieuwe ideeën. ChatGPT-apps als eerste gepakt: grootste jonge winkel en bij Vera "niet te meten".
- Onderzoeker (agent) en controleur (agent) ingezet; hoofdcijfers zelf nagelopen met curl op pluginsradar.com en de richtlijnen van OpenAI. Controleur akkoord, 5 correcties verwerkt.
- Besluit: cijfer 4, nee voor nu. Waarom: geen vroege plek meer (213 nieuwe per dag), geld vragen voor digitale producten uitdrukkelijk verboden zonder datum, en geen gebruikscijfers, dus een eerste plek is niet te bewijzen.
- Herhaalscript gemaakt: `data/chatgpt-plugins-meet.py`, eerste regel in `data/chatgpt-plugins.csv`.
- Les: platformen met een miljard gebruikers lopen binnen een jaar vol. Volgende runs zoeken kleiner en sneller groeiend.

## 7 nov 2026, 22:50 tot ±23:05 UTC (eerste run, deel 2)
- Godot Asset Store gepakt: Vera gaf een 3 omdat er nu niets te verdienen is, met de pionier-meetlat juist een kans.
- Eigen meting van de hele winkel via de open API (1.701 items, 0 betaald, 33 met 10+ stemmen) en van de instroom per maand via de scroll-sleutel van de zoekpagina (±200 per maand sinds mei 2026). Herhaalscript `data/godot-store-meet.py`.
- Onderzoeker (agent) voor groei, betalen en vraag; controleur (agent) akkoord met 4 correcties (itch.io-plekken en prijzen) en een tegenargument (weinig bezoekers in de winkel), verwerkt.
- Besluit: cijfer 6, ja met kleine inzet, categorie level design in de editor. Waarom: groei en jonge winkel sterk aangetoond, eerste plek te pakken, betalen komt maar zonder datum; save-systemen afgewezen omdat itch.io er al 20+ heeft.

## 7 nov 2026, 23:05 tot 23:10 UTC (eerste run, deel 3)
- Snelle schifting van Raycast, Zed, ComfyUI en Claude-koppelingen op vraag 3 (geld): bij geen van vieren een plan om in de winkel te betalen gevonden. Staat in kandidaten.md, niet in onderzocht.md, omdat het geen grondig onderzoek is.
- Run afgesloten na ±30 minuten werk: twee voorstellen af en nagekeken; een derde half beginnen is tegen de regel "liever één goed".

## 7 nov 2026 23:37 tot 8 nov ±00:25 UTC
- Hytale gekozen als nieuwe kandidaat, niet op Vera's lijst: modding-first spel, early access sinds jan 2026, winkel (CurseForge) jong. Paste beter dan n8n of Framer (Framer al vol en half betaald bij Vera).
- Onderzoeker (agent) voor groei, geld en vraag. Zelf de hele winkel geteld via de open API-spiegel api.curse.tools (6.807 projecten), herhaalscript `data/hytale-curseforge-meet.py`, eerste regel in `data/hytale-curseforge.csv`. Controleur (agent): cijfers kloppen, 8 correcties verwerkt.
- Besluit: cijfer 3, nee voor nu. Waarom: vraag 1 weegt het zwaarst en is negatief (instroom van 3.559 naar ±160 per maand, nieuwe mods mediaan 110 tot 200 downloads); betalen in de winkel wil de baas niet. Wel noteren: een lege niche in een spel dat na de hype stilstaat is geen pionierskans.
- Les: kijk bij een jonge winkel naar de instroom per maand van na de hype, niet naar de lanceringscijfers.

## 8 nov 2026, ±23:55 tot 00:05 UTC (zelfde run, tweede platform)
- Na Hytale gezocht naar winkels die net een betaalde laag openden. Gevonden: Grafana Marketplace (algemeen beschikbaar 20 okt 2026). Bij Vera viel Grafana af op geld; dat is het nieuwe feit.
- Zelf de catalogus geteld via de open API (388 plugins, 38 betaald, 3 betaalde panelen), herhaalscript `data/grafana-plugins-meet.py`, eerste regel in `data/grafana-plugins.csv`. Onderzoeker (agent) voor voorwaarden, groei en vraag; controleur (agent): cijfers kloppen, 6 correcties, cijfer 6 naar 5 verwerkt. Bron van "independent developers" zelf nagekeken (blog Grafana).
- Besluit: cijfer 5, nog niet klaar. Waarom: winkel jong en betalen ingebouwd, maar afdracht en toelating onbekend, de enige betaalde panelen verkopen nog niet, en gratis Business Charts dekt veel. Mail om voorwaarden klaargezet op lijst-thijs (niet dringend).
- Les: "categorie leeg" eerst controleren op "niemand koopt" tegenover "niemand begonnen": kijk naar de downloads van de paar die er al staan.
