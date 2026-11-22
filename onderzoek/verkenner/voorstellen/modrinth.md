# Voorstel: Modrinth (Minecraft-mods)

Onderzocht door Vera op 7 nov 2026 (run 08:31 UTC). Eigen meting via de open API van Modrinth (api.modrinth.com), zonder sleutel. Hulpagent zocht het geld-deel uit met bronnen. Nakijken: zie onderaan.

## Kort
- **Cijfer: 3 van 10.** Advies: **nee.**
- Bereik is het beste dat ik tot nu toe zelf mat: een nieuwe mod van 3 tot 6 maanden oud heeft mediaan **371 downloads**, en 88% haalt 100+ (GEZIEN, 16.231 mods).
- Geld is er bijna niet voor een kleine maker. Mods verkopen mag niet (EULA van Minecraft). Het enige geld is een deel van de advertentiepot, verdeeld naar paginaweergaven en downloads in de eigen app. Voor €350 per maand moet een mod bij de ±100 tot 300 grootste projecten van heel Modrinth horen (GOK op basis van eigen meting, zie Geld). En door NET 60 komt geld pas ±2 maanden later binnen.
- Doelen zeggen: geld gaat voor bereik. Daarom nee, ondanks het bereik.

## Hoe gemeten
- Script `data/modrinth-haal-script.py` haalt via `/v2/search?index=newest` alle mods op tot 1 april 2026: **23.600 mods** (GEZIEN). Analyse: `data/modrinth-analyse-script.py`. Ruwe gegevens: `data/modrinth-mods-2026-11-07.json`.
- De zoekindex loopt iets achter op de echte tellers (bij de top 3.000 ±0,05% verschil, GEZIEN). Voor dit doel maakt dat niets uit.
- Downloads per dag voor de hele site: de 3.000 grootste projecten gekozen met `data/modrinth-top-script.py` (zoekindex), daarna twee keer de echte tellers via `/v2/projects` (`data/modrinth-top3000-a/b-2026-11-07.json`, 9 minuten ertussen). De controleur deed het opnieuw met 15,6 minuten ertussen (08:56 tot 09:11 UTC). De zoekindex zelf werkt in schokken bij en is hiervoor niet bruikbaar. Eén tijdstip op zaterdagochtend, dus een ruwe schatting.
- Omzet: `/v3/payout/platform_revenue`, openbaar, per dag (GEZIEN).

## Bereik (GEZIEN, mods goedgekeurd mei tot aug 2026, gemeten 7 nov)

`date_created` in de zoekindex is de datum van goedkeuring, niet van maken (controleur zag dat bij 10 van 10 mods). Mods die nog op keuring wachten zitten er niet in.

| Groep | Aantal | Mediaan | 100+ | 1.000+ | 10.000+ |
|---|---|---|---|---|---|
| Alle mods mei tot aug | 16.231 | 371 | 88% | 29% | 6,3% |
| Makers met 1 mod in de hele set (apr tot nov) | 7.342 | 305 | 85% | 25% | 4,9% |
| Makers met 1 mod binnen mei tot aug (controleur) | 8.130 | 314 | | | |
| Mei | 4.549 | 545 | 93% | 37% | 9,1% |
| Augustus | 3.106 | 234 | 80% | 18% | 3,4% |
| Oktober (1 maand oud) | 1.619 | 109 | 54% | 8% | 1,1% |

- Bibliotheken (604 stuks) mediaan 490, de rest 368. Dus het hoge cijfer komt niet alleen van bibliotheken die andere mods meenemen.
- Let op: een download op Modrinth is niet één speler. Elke modpack-installatie, server en launcher-update telt mee. Volgers zeggen meer over echte belangstelling: mediaan **1 volger** (GEZIEN). Echte gebruikers zijn dus waarschijnlijk veel minder dan downloads (GOK).

## Drukte (GEZIEN)
- Nieuwe (goedgekeurde) mods per maand: 2.835 (apr), 4.549 (mei), 3.605 (jun), 4.971 (jul), 3.106 (aug), 2.516 (sep), 1.619 (okt). Oktober en september zijn lager omdat nieuwe mods eerst gekeurd worden (GOK) of door minder aanbod; niet nagezocht.
- In totaal 167.165 projecten en 72.115 makers (GEZIEN, `/v2/statistics`). Heel druk.

## Geld
- **Regeling:** 75% van alle advertentie-inkomsten gaat naar makers, verdeeld per dag naar "punten": een paginaweergave of een download in de eigen Modrinth-app met ingelogde gebruiker is één punt (DERDEN, eigen pagina modrinth.com/legal/cmp-info, gelezen met curl). Uitbetaling 60 dagen na de maand, via PayPal, Tremendous of bank (DERDEN, modrinth.com/news/article/creator-withdrawals-overhaul, 27 okt 2025). Modrinth+ ($4,99 per maand) geeft 50% aan makers (DERDEN, modrinth.com/plus).
- **De pot:** ±$160.400 voor makers in de 29 dagen van 9 okt tot 6 nov 2026, ±$3.700 tot $7.800 per dag (GEZIEN, platform_revenue, nagerekend door controleur). Per maand wisselt het sterk: $74.000 (jul 2026) tot $191.000 (okt 2026), gemiddeld ±$150.000 over 12 maanden (GEZIEN, controleur). In maart 2023 was het ±$2.200 per maand, tot aug 2024 ±$10.000 (GEZIEN, controleur).
- **Downloads op de hele site:** de 3.000 grootste projecten samen ±29,5 miljoen (mijn meting, 9 minuten) tot ±37,5 miljoen (controleur, 15,6 minuten) downloads per dag. Gemeten verschil is GEZIEN, het dagcijfer is een GOK.
- **Wat levert een punt op:** telden alle downloads als punt, dan ±$5.500 per dag gedeeld door ±37,5 miljoen, dus ±$0,15 per 1.000 downloads (GOK). Maar alleen downloads in de eigen app tellen, plus paginaweergaven, en die aantallen zijn niet openbaar. De echte waarde ligt dus hoger, maar hoeveel is niet te meten. Oud verslag van een maker: $0,27 per 1.000 downloads op Modrinth (maart 2023) (DERDEN, mastodon.social/@shedaniel/110024590363648782). De pot is sindsdien ±65 keer zo groot geworden (GEZIEN, controleur), dus dat cijfer zegt nu weinig.
- **Modpacks:** een download van een mod als deel van een modpack telt even zwaar (DERDEN, cmp-info). Een mod in een populaire modpack krijgt dus een punt per installatie van die pack. Dat is de enige echte route naar geld hier.
- **Wat is nodig voor €350 per maand (alles GOK, afgeleide rekensom):** €350 is ±$405 (koers ±1,16), plus opnamekosten. Bij een pot van $150.000 is dat ±0,27%, in zwakke maanden tot ±0,55%. Op de tellers van de controleur is 0,25% ±94.000 downloads per dag; 99 projecten haalden dat. Is maar een derde van de downloads een punt, dan ±31.000 per dag, en dat halen ±250 tot 313 projecten. De top 3.000 is niet de hele site, dus de drempel ligt nog iets hoger. Samen: een plek in de top ±100 tot 300. Een nieuwe mod van 3 tot 6 maanden heeft in totaal mediaan 371 downloads.
- **NET 60:** geld van januari 2027 komt eind maart 2027 binnen (DERDEN, cmp-info). Voor €350 in maart 2027 moet een mod over ±2 maanden al in die top staan. Voor een nieuwe mod is dat vrijwel onmogelijk (GOK).
- **Mods verkopen mag niet:** de EULA van Minecraft verbiedt geld vragen voor mods (DERDEN, minecraft.net/en-us/eula). Alleen donaties (Patreon, Ko-fi). Zelfs grote mods halen daar weinig: Iris (193 miljoen downloads) $123 per maand, ReplayMod $295 (DERDEN, graphtreon.com).
- **Betaalde serverplugins (SpigotMC premium) mogen wel**, maar daar verkoopt een nieuwe plugin weinig: van 742 premium plugins uit de laatste twee jaar mediaan 3 downloads (gelijk gesteld aan aankopen), 17 met 100+ (hulpagent, eigen telling via de Spiget-API, niet door mij nagerekend).
- **CurseForge** (de grote concurrent) werkt met punten en een interne drempel voordat je iets krijgt (DERDEN, support.curseforge.com). Niet beter voor een kleine maker.

## Vindbaarheid
- Zoeken met sortering op relevantie, downloads, volgers, nieuwste en bijgewerkt (GEZIEN in de API). Nieuwe mods krijgen downloads, vooral via modpacks en zoeken op versie en loader (GOK).

## Past het bij ons
- Een Fabric- of NeoForge-mod is Java of Kotlin, wat we van JetBrains kennen. In 1 tot 2 weken te bouwen (GOK).
- Nadeel: elke nieuwe Minecraft-versie (nu 26.x, GEZIEN in de versielijst van nieuwe mods) vraagt bijwerken. Veel werk voor iets dat geen geld oplevert.

## Eerste idee (alleen als we ooit bereik willen kopen met tijd)
Een kleine hulpmod voor iets dat spelers veel vragen, voor Fabric en NeoForge. Dat levert downloads op, geen geld. Niet nu doen.

## Voor en tegen
Voor: bereik voor nieuwe makers is echt en meetbaar (mediaan 371, 88% 100+); open API; geld wordt per dag naar gebruik verdeeld (en ±60 dagen na de maand uitbetaald); pot van gemiddeld ±$150.000 per maand (wisselend $74.000 tot $191.000).
Tegen: verkopen verboden; ads leveren een kleine maker centen op; €350 per maand vraagt een plek in de top ±100 tot 300 van 167.000 projecten, en komt door NET 60 pas 2 maanden later binnen; ±4.000 nieuwe mods per maand in mei tot aug (GEZIEN, gemiddeld 4.058); downloads zijn geen gebruikers (mediaan 1 volger); onderhoud bij elke Minecraft-versie.

## Wat zou het oordeel veranderen
- Als Mojang of Modrinth betaalde mods toestaat (de officiële Bedrock Marketplace bestaat al, maar alleen voor goedgekeurde partners, GOK uit eigen kennis, niet nagezocht).
- Als makers openbaar een $ per 1.000 punten van 2026 delen dat 10 keer hoger is dan mijn schatting.

## Nakijken
Controleur: eerst niet akkoord, met 10 correcties. Alle verwerkt: pot was verkeerd opgeteld ($160.400, niet $132.800), downloads per dag 29,5 tot 37,5 miljoen, drempel top ±100 tot 300 in plaats van 75 tot 200, NET 60 erbij, datum is goedkeuring, labels aangevuld, modpack-route erbij. Bereiktabel, regels en omzet per dag klopten. Cijfer 3 en advies nee vond de controleur eerlijk.
