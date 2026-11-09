# XENEON EDGE-widgets: ondergrens van verkopen per widget (Chris, 9 nov 2026, run 24)

Voor Hans en Noor, bij het voorstel `platformen/pionier/voorstellen/xeneon-edge-widgets.md` (cijfer 6). Noor schreef: "7 bij een verkoopcijfer van een widget". De winkel toont geen downloads of verkopen. Maar de openbare volgorde Popular verraadt wel een ondergrens. Ik kies het product niet; dit is alleen marktbewijs.

## Kort
- **Van de 307 betaalde widgets hebben er minstens 122 al 10 of meer downloads, 80 er 20 of meer en 13 er 50 of meer** (GEZIEN, afgeleid, ondergrens; meting 9 nov 05:47 UTC).
- **De best gedownloade betaalde widget, Sidekick for Discord ($7,99, sinds 13 sept), heeft minstens 74 downloads.** Nummer twee en drie: Deckord (SAR 37,54, ±$10) minstens 69, Music Pro ($12) minstens 68 (GEZIEN, afgeleid, ondergrens).
- **Ook nieuwkomers verkopen:** van de betaalde widgets van oktober heeft 53% al minstens 5 downloads (mediaan minstens 5); van september 57% (mediaan minstens 8); van augustus 78% (mediaan minstens 12,5). Van november (nog maar 3 tot 8 dagen oud) 5% (GEZIEN, afgeleid).
- **Omgerekend naar geld, als een download van een betaalde widget een aankoop is:** samen minstens ±$27.000 netto voor de makers sinds augustus; 24 van de 39 makers met betaalde widgets minstens $100 netto, de grootste (Respawn Icons, 29 betaalde) minstens ±$7.600 (GOK: ondergrens downloads keer prijs keer 70%, ruwe wisselkoersen).
- **De enige widget over AI-hulpen, AI Usage Dashboard (PackRat, $11,99), heeft minstens 22 downloads.**
- **Correctie op het voorstel:** de mediaanprijs $7,99 telt verschillende valuta door elkaar (USD 173, GBP 64, SAR 23, CAD 20, EUR 17 en andere). Omgerekend naar dollars is de mediaan ±$6,35 (GEZIEN voor de bedragen, GOK voor de koersen). Ook "van $0,99 tot $120" klopt niet: die $120 is MXN 120 (±$6,60); omgerekend lopen de prijzen van $0,99 (Valheim Raid Danger Bar) tot $34,99 (XENEON EDGE Ultimate).

## Hoe ik dit afleid (zodat iedereen het kan nameten)
1. De winkel sorteert op Popular met `ordering=-download_count`, dezelfde openbare lijst die Noor al gebruikte (`platformen/pionier/data/xeneon-widgets-meet.py`). Ik heb geen andere parameters of verborgen velden gebruikt.
2. In die lijst staan lange stukken waarin de id's precies oplopend staan: de onderste 53 widgets, daarboven 40, 15, 14, 12 en 12 (GEZIEN). 53 willekeurige id's die toevallig oplopend staan, kan niet (kans 1 op 53!, ±10^-70); dit is de tweede sortering bij gelijke tellingen. Dus: binnen zo'n stuk is de downloadtelling gelijk, en bij elke breuk in de oplopende reeks wordt de telling lager.
3. Telt de lijst 97 van zulke stukken, dan zijn er minstens 97 verschillende tellingen. Een widget met k stukken onder zich heeft minstens k downloads (het onderste stuk heeft er 0 of meer). Script: `data/ondergrens-downloads.py`, uitkomst `data/ondergrens-2026-11-09.txt`, ruwe lijst `data/widgets-2026-11-09.json`.
4. Nagemeten met de lijst van Noor van 8 nov 23:58 UTC: 96 stukken, dezelfde onderste stukken (53, 40, 15, 14, 12, 12, met dezelfde widgets). 118 widgets kregen een ondergrens 1 of 2 hoger (vooral doordat er onderaan een stuk bij kwam), 2 widgets 1 lager, 275 bleven gelijk. In 5 uur en 49 minuten veranderden 47 widgets van plek (GEZIEN): er wordt dus nu gedownload. De 96 van 8 nov kan 1 te hoog zijn: daar valt een breuk precies op de paginagrens bij plek 200 (pagina's op net andere momenten opgehaald).
5. Extra controles (controleur): de id's zijn UUID versie 4 (willekeurig); binnen het onderste stuk staat created_at niet op volgorde, dus de tweede sortering is niet de aanmaakdatum; vergelijken als tekst of als bytes geeft allebei 97 stukken; in de lijst van 9 nov valt geen breuk op een paginagrens; een willekeurige volgorde geeft gemiddeld ±198 stukken, niet 97; en een nieuwe ophaalronde om 05:51 UTC gaf precies dezelfde volgorde.
6. Het onderste stuk van 53 bestaat helemaal uit betaalde widgets (0 gratis), wat past bij 0 downloads.

## Wat dit niet zegt (eerlijk)
- **Het is een ondergrens, en vaak een flinke onderschatting.** Tussen twee stukken kan het verschil veel groter zijn dan 1. Bovenaan zeker: de gratis Sensor Bar van Corsair komt op "minstens 96", terwijl die waarschijnlijk duizenden heeft (GOK).
- **Een download is niet zeker een aankoop.** Mogelijk tellen ook opnieuw downloaden door dezelfde koper, de maker zelf of gratis codes mee (GOK, niet te zien). De bedragen hierboven zijn daarom GOK.
- **De volgorde Popular is misschien niet het hele getal van downloads** (bijvoorbeeld een telling per periode). Het veld heet `download_count` en de stukken gedragen zich als een totaal (oude widgets hoger, nieuwe van november onderaan), maar zeker is het niet (GOK).
- **De ondergrens van een widget kan ook dalen** als stukken eronder samenvallen (2 keer gezien tussen 8 en 9 nov); het is geen telling.
- Prijzen in GBP en EUR zijn misschien inclusief btw, en terugbetalingen kunnen meetellen; het netto voor de maker is dan lager (GOK).
- Koersen voor de omrekening zijn ruw (GBP 1,27, EUR 1,08, CAD 0,72, SAR 0,267 en andere, GOK nov 2026).

## Wat het betekent voor het voorstel
Noor gaf een 6 omdat er geen verkoopcijfer was. Dit is geen precies verkoopcijfer, maar wel een harde ondergrens uit openbare gegevens: in twee tot drie maanden halen tientallen betaalde widgets van kleine makers 20 tot 70+ downloads, en ook widgets van oktober verkopen al. Voor Agent Deck (Pro eenmalig $12 tot $15) zou een plek in de bovenste 13 betaalde (minstens 50) betekenen: minstens ±$420 tot $525 netto (GOK, zelfde aanname), eenmalig, en dat is wat de top nu haalt na twee maanden, niet per maand. Dat is beter dan de mediaan van JetBrains-nieuwkomers waar geen enkel bedrag van te zien is, maar het blijft een kleine winkel. Hans beslist.

## Nameten
Elke week (of vóór een besluit): `python3 -I platformen/pionier/data/xeneon-widgets-meet.py commercie/xeneon-widgets/data/widgets-<datum>.json` en dan `python3 -I commercie/xeneon-widgets/data/ondergrens-downloads.py` op dat bestand. Groeit het aantal stukken en de ondergrens van de top, dan loopt de winkel.
