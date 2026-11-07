# Voorstel: Thunderbird (extensies op addons.thunderbird.net)

**Advies: nee. Cijfer: 3 van 10.** Klein en goed te meten, maar nieuwe extensies halen weinig gebruikers (mediaan 16 per dag na 3 tot 6 maanden, 18% haalt 100+), en nieuwe betaalde extensies mediaan 7. Echt geld zit bij oude makers (Owl for Exchange sinds 2018, SmartTemplates sinds 2011). Geschreven op 7 nov 2026, run 13:31 (tweede platform). Nagekeken door de controleur (akkoord, 8 correcties verwerkt).

## Wat ik zelf mat
- Met `data/thunderbird-haal-script.py` via de open API van addons.thunderbird.net alle **2.282 extensies** gehaald, met aanmaakdatum, gemiddeld aantal gebruikers per dag (ADU, uit de updatecontrole van Thunderbird) en de vlag "vraagt betaling". Uitkomst in `data/thunderbird-extensies-2026-11-07.json`, tellen met `data/thunderbird-analyse-script.py`. GEZIEN
- **Meetgrens:** ADU telt Thunderbird-installaties die per dag contact maken; dat is dichter bij echte gebruikers dan downloads (zoals bij Obsidian en JetBrains), maar niet hetzelfde. GOK hoe die verhouding ligt.

## Cijfers

**Bereik**
- Nieuw in mei t/m aug 2026 (2 tot 6 maanden oud): n=145, **mediaan 16 gebruikers per dag, 64% 10+, 18% 100+**, 2 boven 1.000 (top 1.157). GEZIEN
- Nieuw in feb t/m mei 2026 (mei telt in beide groepen): n=142, mediaan 24, 22% 100+. GEZIEN
- Nieuw in mei t/m okt 2025 (ruim een jaar oud): n=77, mediaan 29, 34% 100+, 8 boven 1.000. GEZIEN. Groei na het eerste halfjaar is dus klein.
- Hele winkel: mediaan 8, 25% 100+, 204 boven 1.000 (vooral oude extensies); grootste is ImportExportTools NG met ±316.000, daarna Provider for Google Calendar ±158.000 en Send Later ±130.000. GEZIEN
- Thunderbird zelf: "tientallen miljoenen" gebruikers en $10,3 miljoen giften van 335.000+ gevers in 2024. DERDEN: [jaarverslag 2023-2024](https://blog.thunderbird.net/2024/10/thunderbird-annual-report-2023-2024/), [State of the Bird 2024-25](https://blog.thunderbird.net/2025/10/state-of-the-bird-2024-25/). De basis is groot, maar nieuwe extensies halen weinig.
- Ter vergelijking (eigen metingen, zie `onderzocht.md`): JetBrains mediaan 111 en 54%, Obsidian 213 tot 364.

**Geld**
- Geen betaling in de winkel; 56 extensies hebben de vlag "vraagt betaling" en verkopen zelf een licentie. GEZIEN
- Betaalde extensies sinds nov 2025: n=33, **mediaan 7 gebruikers per dag**, hoogste 406 (Nextcloud for Thunderbird, van het bedrijf Sendent). GEZIEN
- Grootste betaalde: Owl for Exchange (Beonex, sinds 2018) 41.817 per dag, prijs ±€10 per jaar via Stripe. GEZIEN / DERDEN: [beonex.com/owl](https://www.beonex.com/owl/). Als een deel betaalt is dat veel geld, maar het is een oud product van een GmbH. GOK
- SmartTemplates (Axel Grude, sinds 2011) 4.039 per dag, met betaalde Pro-licentie. GEZIEN
- Geen nieuwe kleine maker gevonden met een bedrag. TrustMRR doorzocht (controleur, 7 nov): geen Thunderbird-maker, alleen een Chrome-mailextensie met $134 in 30 dagen. DERDEN
- Thunderbird 145 (nov 2025) heeft Exchange-mail zelf ingebouwd; agenda en adresboek volgen. Dat raakt Owl, het beste geldvoorbeeld. DERDEN: [blog Thunderbird](https://blog.thunderbird.net/2025/11/thunderbird-adds-native-microsoft-exchange-email-support/)

**Drukte**
- Nieuwe extensies per maand: 2025 tussen 5 en 18, 2026 tussen 17 en 60 (sep 60; nov telt pas 7, maand net begonnen). GEZIEN. Rustig vergeleken met andere winkels, maar wel stijgend, veel AI-mailhulpjes.

**Vindbaarheid**
- Zoeken en lijsten in de winkel en in Thunderbird zelf (Add-ons Manager). GOK, niet nagelezen.

**Past het bij ons**
- WebExtension met de Thunderbird-API's (mail, mappen, berichten), in 1 tot 2 weken te bouwen. GOK. Account op addons.thunderbird.net door Thijs.

## Voor
- Open API, volledig te meten, weinig nieuwe extensies per maand.
- Gebruikers betalen soms (Owl, SmartTemplates), dus de cultuur is er.

## Tegen
- Bereik van nieuwe extensies is laag: mediaan 16 per dag, ver onder JetBrains en Obsidian.
- Nieuwe betaalde extensies mediaan 7: met een paar procent betalers is dat bijna niets.
- Geld zit bij makers die 8 tot 16 jaar bestaan (Owl 2018, SmartTemplates 2011, ExQuilla 2010).
- Thunderbird bouwt Exchange zelf in, dus het grootste betaalde gat sluit.

## Eerste idee (als het ooit ja wordt)
Een koppeling die een grote groep mist (zoals Owl voor Exchange), met jaarlicentie. Alleen zinvol als er nog zo'n gat bestaat; Exchange-mail is sinds Thunderbird 145 geen gat meer.

## Wat het van nee naar ja zou brengen
- Een nieuwe kleine maker (start 2025 of later) met een aantoonbaar bedrag boven $300 per maand.
- Een herhaalmeting over 4 weken met de scripts laat zien of de groep van nu groeit.
