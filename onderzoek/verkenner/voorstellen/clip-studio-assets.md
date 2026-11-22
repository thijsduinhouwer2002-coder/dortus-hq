# Voorstel: CLIP STUDIO ASSETS (materialen voor Clip Studio Paint, Celsys)

Vera, 8 nov 2026 run 13:33 (Amsterdamse tijd). Zelf toegevoegd. Clip Studio Paint is het tekenprogramma voor manga, webtoon en illustratie; Celsys meldt 11 miljoen geregistreerde makers en een omzet van 9,47 miljard yen in 2025 (DERDEN, IR-stuk 13 feb 2026). ASSETS is de ingebouwde winkel voor penselen, 3D-modellen, poses, rasters en auto-acties.

## In het kort
- **Advies: nog niet klaar, cijfer 5.**
- **Bereik is het beste dat ik tot nu toe zag:** nieuwe gratis materialen (mei t/m aug 2026) hebben een mediaan van 91 tot 103 downloads en ±50% haalt 100+. Nieuwe betaalde GOLD-materialen: mediaan 86, 47% haalt 100+, 97,5% minstens 1 (GEZIEN, alle items, geen steekproef).
- **Geld kan echt:** GOLD-materialen leveren de maker 70% van de prijs op, contant via bankoverschrijving, uitbetaling voor de 25e van de volgende maand, 325 yen kosten per uitbetaling (GEZIEN, officiële hulp). 1 GOLD is ±1 yen (DERDEN).
- **Maar de teller is downloads, geen verkopen.** De officiële hulp zegt zelf dat het downloadgetal niet gelijk is aan het aantal betalingen, 38% van de GOLD-items is ook met Clippy (gratis punten, geen geld) te koop, en het bruto totaal dat uit de tellers volgt (1,28 miljard GOLD voor items van maart t/m oktober alleen) past niet bij de jaarrekening van Celsys. De controleur schat dat 10 tot 50% echte GOLD-verkoop is (GOK). Een kleine verkoper komt dan op ±€10 tot €45 per maand per maker, met uitschieters tot vele duizenden.
- **De deur is smal:** GOLD verkopen mag pas na een screening van de persoon (er moeten al betaalde Clippy-materialen met downloads online staan), een contract met Celsys en bankgegevens. Er zijn maar ±65 actieve GOLD-verkopers per maand en ±330 tot 480 nieuwe GOLD-items per maand. In mei t/m aug kwam er geen enkele nieuwe GOLD-verkoper bij; in jan t/m apr 2026 vijf (GEZIEN).
- **Past deels:** 65% van de nieuwe GOLD-items zijn 3D-modellen (voorwerpen, gebouwen, interieurs) en daar heeft Dortus met Blender al werk in. AI-beeldgeneratie is verboden; modellen gemaakt met Blender-scripts staan niet in dat verbod, maar het blijft een grijs gebied.

## Wat ik gemeten heb (GEZIEN)
Bron: de open zoek-API die de site zelf gebruikt, `https://assets.clip-studio.com/en-us/search/ajax` met `order=new`, `pay=gold|clippy|free`, `published_from`, `published_to` en `cursor` (60 per pagina, 1 verzoek per seconde). robots.txt: `User-agent: * Disallow:` (alles toegestaan). Per item: `purchase_count` (op de site getoond met een download-icoon, op de detailpagina `downloadCount`), prijs in GOLD en Clippy, maker, soort. 136 items van bedrijfsaccounts (filter `corp=corp`) heb ik eruit gehaald.

Bestanden in `data/`: `csa-gold-mrt-okt-2026-11-08.jsonl.gz` (alle 3.129 GOLD-items mrt t/m okt 2026), `csa-alle-mei-aug-2026-11-08.jsonl.gz` (alle 20.707 materialen mei t/m aug, ingekorte velden), `csa-makers-2026-11-08.json` (per verkoper hoeveel GOLD-items en sinds wanneer), `csa-corp-ids.json`, scripts `csa-haal-script.py`, `csa-makers-script.py`, `csa-analyse-script.py`.

### Drukte: nieuwe materialen per maand (2026, alle talen)
| Maand | Alle | GOLD | Clippy | Gratis |
|---|---|---|---|---|
| jan | 4.492 | 478 | 1.636 | 2.508 |
| mrt | 5.074 | 418 | 1.548 | 3.228 |
| mei | 4.838 | 358 | 1.628 | 2.980 |
| jul | 5.428 | 329 | 1.878 | 3.330 |
| aug | 5.465 | 365 | 1.859 | 3.366 |
| okt | 5.247 | 480 | 1.707 | 3.250 |

Rustig: ±5.000 per maand, waarvan maar ±400 betaald met GOLD.

### Bereik nieuwe materialen (downloads op 8 nov, zonder bedrijven)
| Groep | Aantal | Mediaan | 100+ | 1.000+ | Makers |
|---|---|---|---|---|---|
| Gratis, mei | 2.980 | 102 | 50,5% | 9,3% | 1.082 |
| Gratis, aug | 3.366 | 91 | 48,1% | 7,0% | 1.353 |
| Alleen Clippy, mei | 1.500 | 73 | 42,9% | 16,0% | 575 |
| Alleen Clippy, aug | 1.734 | 80 | 46,1% | 17,5% | 692 |
| GOLD, mei t/m aug | 1.338 | 86 | 46,9% | 20,6% | 98 |
| GOLD, makers met minder dan 10 GOLD-items in die maanden | 182 | 263 | 60,4% | 37,9% | 59 |
| GOLD, 5 verkopers die pas in 2026 begonnen | 72 | 225 | 65,3% | 20,8% | 5 |
| GOLD, soort 3D-model | 876 | 84 | 46,0% | 13,9% | 55 |
| GOLD, soort catalogus (sets penselen, enz.) | 360 | 316 | 59,4% | 40,8% | 67 |
| GOLD, soort plaatje | 89 | 2 | 2,2% | 0% | 4 |

- Bijna niemand blijft op 0: gratis 0,0%, GOLD 2,5%. Ter vergelijking: Printables gratis mediaan 11, Moodle 32, Rhino 58.
- Mediaanprijs GOLD: 200 GOLD (±€1,20).
- Het bruto (downloads x prijs) zit heel geconcentreerd: top 10 items 28%, top 50 items 49% (controleur). Top-verkoper nise (penselen van 200 GOLD) heeft 35 nieuwe items met samen 681.722 downloads.

### Verkopers
- 100 verkopers hadden een GOLD-item in mei t/m aug. Mediaan 89 GOLD-items per verkoper in totaal: het zijn vaste, productieve makers.
- Geen van hen begon na april 2026. Vijf begonnen in jan t/m apr 2026 (EllisEltra, Happy★Creator, あたる03, にふ7y, まるまるねっこ), met 16 tot 65 GOLD-items en een mediaan van 225 downloads per item.

## Is een download een verkoop? (DERDEN en GOK)
- Officieel: "The number of downloads in My Uploads is not necessarily the number of payments that have been made" (accounts.clip-studio.com/information/royalty/bank).
- 1.131 van de 2.993 GOLD-items zijn ook met Clippy te koop, vaak voor meer punten (bijvoorbeeld 800 GOLD of 3.500 Clippy). Clippy krijg je gratis bij uploaden en met een GOLD-lidmaatschap (1.500 per maand); een verkoop voor Clippy levert de maker geen geld op (GEZIEN).
- Als alle downloads betaalde verkopen waren, ging er ±1,28 miljard GOLD om in items van maart t/m oktober alleen. De jaarrekening van Celsys 2025 laat geen ruimte voor uitbetalingen van ±2 miljard yen per jaar aan makers (controleur, EDINET). De oude wervingspagina van Celsys noemt "sommige makers meer dan 500.000 yen per maand" als iets bijzonders.
- Een maker meldde in 2018 met ±250 GOLD-materialen ±10.000 tot 15.000 yen netto per maand (DERDEN, yakumoreo.com).
- **Conclusie:** de tellers zijn een bovengrens. Met 10 tot 50% echte verkoop (GOK) haalt een doorsnee verkoper in het cohort netto ±€10 tot €45 per maand met zijn nieuwe items, de top tientallen tot honderden keren meer. Dit kon ik niet zelf meten. Meten kan alleen met een eigen verkopersaccount (Mijn GOLD-verkopen toont echte verkoop) of als een maker zijn cijfers openbaar maakt.

## Voordelen
- Echt grote, actieve doelgroep in het programma zelf; nieuwe materialen worden altijd gedownload.
- Weinig concurrentie in betaald: ±400 nieuwe GOLD-items per maand, ±65 verkopers.
- Contant geld, 70%, geen bovengrens.
- 3D-modellen zijn de grootste betaalde soort, en die kunnen wij met Blender maken zonder te tekenen.

## Nadelen
- Downloads zijn geen verkopen; het echte geld is onbekend.
- GOLD alleen na screening en contract met Celsys (naam, adres, geboortedatum, bank): allemaal stappen voor Thijs. Je moet eerst gratis of Clippy-materialen met downloads opbouwen. In mei t/m aug kwam er geen enkele nieuwe verkoper bij.
- Uploaden gaat via de Clip Studio-app op een computer, met een Clip Studio-account (GOK op basis van de handleidingen van Celsys). 3D-materialen moeten naar het eigen formaat van Clip Studio. Dat kunnen wij vanuit de cloud niet zelf; Thijs moet elke upload doen, of er moet een computer met de app beschikbaar zijn.
- AI-beeldgeneratie verboden sinds dec 2022; materialen van lage kwaliteit of met weinig nut worden zonder aankondiging verwijderd (golf in sep 2026, weekly.ascii.jp).
- Sterk Japans en Koreaans; makers schrijven in hun eigen taal.

## Wat we zouden bouwen (eerste idee)
Een set bruikbare 3D-modellen voor achtergronden in manga en webtoon (klaslokaal-meubels, treinen, keukens, winkelinterieurs), gemaakt met onze Blender-scripts, eerst gratis of voor Clippy om downloads op te bouwen, daarna GOLD-screening aanvragen en sets van 150 tot 300 GOLD verkopen. Kijken welke soorten 3D-modellen de beste verhouding downloads per item hebben kan met de bestanden in `data/`.

## Advies
**Nog niet klaar, cijfer 5.** Bereik is top en het geld bestaat, maar ik kan niet aantonen hoeveel een kleine nieuwe verkoper echt verdient, de toegang tot GOLD is streng en elke upload vraagt een computer met de app. Wat er nog moet:
1. Echte verkoopcijfers: een openbare bron van een maker met downloads en uitbetaling naast elkaar, of een eigen proef.
2. Uitzoeken of 3D-materialen zonder Clip Studio Modeler te maken zijn (bestandsformaat) en of uploaden echt alleen via de app kan. Als dat zo is, is dit voor Dortus alleen haalbaar als Thijs elke upload doet.
3. Herhaalmeting over 4 weken met `data/csa-haal-script.py` om te zien hoe snel de tellers van de GOLD-items groeien.

## Controle
Controleur (aparte agent) akkoord met de cijfers: alle hoofdcijfers exact gelijk, geen dubbele id's, ophaling volledig, 30 detailpagina's gelijk aan de API. Correctie overgenomen: de teller is een downloadteller, het bruto is geen omzet, schatting 10 tot 50% echte verkoop (GOK).
