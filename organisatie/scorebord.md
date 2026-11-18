# Scorebord Dortus

Gemeten op 2026-11-18 om 23:13 UTC met `organisatie/controle/scorebord.py`, openbare bronnen, plus Gumroad, Kit en bezoekers van dortus.com (Amami) met leessleutels. Elk cijfer is GEZIEN: het script leest het zelf; de bron staat per regel. Draait elke dag om 06:41 UTC (workflow "Scorebord"). Gisteren en 7 dagen terug: de laatste meting op of vóór die dag; staat er een datum tussen haakjes, dan is dat een oudere meting. Geschiedenis in `organisatie/scorebord-data.csv`.

| Product | Platform | Maat | Vandaag | Gisteren | 7 dagen terug | Erbij in 7 dagen | Stand | Bron |
|---|---|---|---|---|---|---|---|---|
| Click Joints | Blender | downloads | 240 | 197 | geen meting |  | versie 0.1.1 | GEZIEN, extensions.blender.org (API en productpagina) |
| Click Joints | Blender | beoordelingen | 0 | 0 | geen meting |  |  | GEZIEN, extensions.blender.org (API en productpagina) |
| Click Joints Pro | Superhive | verkoopklasse | ? | geen meting | geen meting |  | niet leesbaar (Superhive weigert dit adres soms) | GEZIEN, superhivemarket.com productpagina |
| Gloop's Hat Tower | Garmin | downloads | 10 | geen meting | geen meting |  | app, gratis, versie 1.0.0 | GEZIEN, apps.garmin.com winkel-API |
| Gloop's Hat Tower | Garmin | beoordelingen | 0 | geen meting | geen meting |  |  | GEZIEN, apps.garmin.com winkel-API |
| Ebb Calm | Garmin | downloads | 10 | 1 | geen meting |  | app, gratis, versie 1.0.1 | GEZIEN, apps.garmin.com winkel-API |
| Ebb Calm | Garmin | beoordelingen | 0 | 0 | geen meting |  |  | GEZIEN, apps.garmin.com winkel-API |
| Ebb | Garmin | downloads | 1 | 0 | geen meting |  | app, $2.99 USD, versie 1.0.1 | GEZIEN, apps.garmin.com winkel-API |
| Ebb | Garmin | beoordelingen | 0 | 0 | geen meting |  |  | GEZIEN, apps.garmin.com winkel-API |
| Rollwright | Obsidian | downloads | 45 | 44 | geen meting |  | community-plugin-stats.json | GEZIEN, obsidian-releases community-plugin-stats.json |
| Bison & Flex | JetBrains | downloads | 6 | 1 | geen meting |  | in keuring, freemium | GEZIEN, plugins.jetbrains.com API |
| Bison & Flex | JetBrains | beoordelingen | 0 | 0 | geen meting |  |  | GEZIEN, plugins.jetbrains.com API |
| Click Joints Pro for Blender | Gumroad | verkopen | 0 | geen meting | geen meting |  | gepubliceerd, $12 | GEZIEN, Gumroad API v2 /products (leessleutel) |
| Click Joints Pro for Blender | Gumroad | omzet USD | 0.00 | geen meting | geen meting |  | bruto, vóór kosten van Gumroad | GEZIEN, Gumroad API v2 /products (leessleutel) |
| Kit (alle) | Kit | abonnees | 0 | geen meting | geen meting |  | actief, alle tags samen | GEZIEN, Kit API (leessleutel), alleen aantallen |
| Hats of the Fallen | Discord | leden | ? | geen meting | geen meting |  | uitnodigingscode ontbreekt (vraag staat bij de hoofdchat) | GEZIEN, discord.com invite-API (with_counts) |
| YouTube @Dortusapps | YouTube | weergaven sgcC965GVps | 56 | geen meting | geen meting |  | 2026-11-17 Breathing exercise on your watch? Close your eyes and follow | GEZIEN, youtube.com/feeds/videos.xml (RSS) |
| YouTube @Dortusapps | YouTube | weergaven (RSS) | 56 | geen meting | geen meting |  | 1 filmpjes in de RSS (alleen de nieuwste openbare, max 15) | GEZIEN, youtube.com/feeds/videos.xml (RSS) |

## Bezoekers dortus.com (Amami, per dag, Amsterdamse tijd)

Bezoekers, bezoeken en weergaven gelden voor de hele site. Per pagina: het getal dat Amami per pad geeft (Umami-metrics), opgeteld per product inclusief subpagina's. Amami bewaart cijfers 7 dagen; oudere dagen staan alleen hier en in de csv.

| Dag | Bezoekers | Bezoeken | Weergaven | voorpagina | Click Joints | Ebb | Rollwright | Bison & Flex | overig |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 tot 00:13 (nog niet om, niet in de csv) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2026-11-18 | 36 | 36 | 43 | 2 | 31 | 0 | 0 | 0 | 8 |
| 2026-11-17 | 8 | 8 | 9 | 1 | 3 | 0 | 0 | 0 | 4 |
| 2026-11-16 | 5 | 5 | 6 | 3 | 2 | 0 | 0 | 0 | 0 |

## Wat niet te zien is

- Gumroad-bezoekers staan niet in de Gumroad API v2 (alleen verkopen en omzet per product); bezoekers van de productpagina's op dortus.com staan hierboven (Amami).
- YouTube: de RSS toont alleen de nieuwste openbare filmpjes (max 15); oudere filmpjes en abonnees vragen de YouTube Data API (sleutel ontbreekt nog, zie toegang.md).
- Kit en Gumroad: alleen aantallen, nooit namen of mailadressen van kopers of abonnees.
- Superhive toont alleen een verkoopklasse (0, 10+, 100+ ...), geen precies aantal.
- Garmin telt downloads per app; bij een betaalde app is dat ongeveer het aantal kopers, inclusief terugbetalingen binnen 48 uur (GOK).
- Steam (Hats of the Fallen) is nog niet in de winkel; volgers zijn pas te meten als de pagina openbaar is.

## Meldingen van deze run

- Kit: nog geen tags aangemaakt, alleen het totaal gemeten.
- Discord: geen uitnodigingscode. Zet de code in HATS_DISCORD_INVITE in scorebord_bronnen.py.
