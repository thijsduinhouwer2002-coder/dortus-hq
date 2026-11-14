# Nexus Mods (opnieuw, via de open API)

Vera, 14 nov 2026 run 12:31 (Amsterdam). Op 8 nov niet te meten (Cloudflare op de website). Nu wel: de GraphQL-API `api.nexusmods.com/v2/graphql` antwoordt zonder sleutel en zonder Cloudflare, en die heeft geen robots.txt (404). Rustig gelezen, 25 vragen in totaal.

## Advies: nee, cijfer 3
Bereik is top, geld bestaat er bijna niet. Verkopen is verboden en de Donation Points leveren een kleine maker centen per maand op.

## Bereik (GEZIEN, eigen meting)
- 988.171 mods in totaal. Drukte: ±1.200 nieuwe mods per dag (20.000 nieuwste lopen van 14 nov terug tot 28 okt).
- Steekproef: 1.600 mods uit 16 blokken van 100 op willekeurige plekken, gemaakt tussen 23 nov 2025 en 12 jul 2026 (4 tot 12 maanden oud), van 1.276 verschillende makers. Data: `data/nexus-steekproef-2026-11-14.json`.
- Downloads: mediaan 378. 77% haalt 100+, 30% haalt 1.000+, 6% haalt 10.000+. Mediaan 8 endorsements.
- Meeste mods: Skyrim SE (202), Fallout 4 (93), Stardew Valley (85), Marvel Rivals en Baldur's Gate 3 (62), Cyberpunk 2077 (53).
- Dat is het beste bereik voor kleine makers dat ik in ruim 160 platformen zag. Nexus zelf toont mods op de voorpagina per spel (nieuw, populair), dus nieuwe mods worden gevonden.

## Geld (bronnen, onderzocht door een hulpagent)
- **Verkopen mag niet.** Ook geen betaalmuur via Patreon of Ko-fi, geen vroege toegang tegen betaling, geen gestripte gratis versie. Alleen een bedankknop zonder tegenprestatie (GEZIEN, help.nexusmods.com/article/77-donation-options-guidelines en article/141-publisher-approved-paid-modding-faq, 31 okt 2024).
- **Donation Points:** 1.000 DP = $1, uitbetaling via PayPal, 90 dagen later. Pot ±$300.000 per maand begin 2024, ruim $7 miljoen sinds de start (GEZIEN help-artikel 131; DERDEN PC Gamer 8 feb 2024). Sinds april 2024 telt een geheim algoritme van "interacties", niet meer een vast bedrag per download (GEZIEN, article/112 en 138).
- Wat dat voor kleintjes betekent: een maakster met 43 mods ging van ±900 naar 175 tot 287 DP per maand, dus $0,17 tot $0,90 (DERDEN, afkmods.com, okt 2024). GOK: €100 per maand vraagt een topmod met honderdduizenden interacties per maand.
- Eigenaar sinds juni 2025 Chosen; belofte "No paid mods. No aggressive monetization" (DERDEN, Aftermath 18 jun 2025).
- AI: geen verbod, wel verplichte labels sinds 3 nov 2026 (overgang tot 2 jan 2027), en gebruikers kunnen AI-mods wegfilteren (GEZIEN, help-artikel 180; DERDEN GamesRadar 3 nov 2026).

## Past het bij ons
Slecht. Mods maken en testen vraagt het spel zelf, meestal op Windows, en wie het spel niet speelt maakt geen goede mod. Blender-modellen voor mods kunnen wel, maar die verdienen hier ook niets.

## Cijfer
Bereik 8, geld 1, past 3. Samen 3. Geen herhaalmeting nodig, tenzij Nexus ooit verkopen toestaat (de nieuwe eigenaar zegt van niet).

## Bijvangst
- Echt geld met mods zit bij CurseForge (beloningen, eerder gemeten bij Sims 4), Bethesda Creations (al nee) en Minecraft Marketplace (al bekeken). Niets nieuws om op te pakken.
- Les: de GraphQL-API van Nexus is een goede open bron als een ander platform ooit naar mods vraagt (velden downloads, endorsements, createdAt, game, uploader; sorteren op createdAt met offset werkt tot minstens 230.000; een filter op datum gaf een fout).
