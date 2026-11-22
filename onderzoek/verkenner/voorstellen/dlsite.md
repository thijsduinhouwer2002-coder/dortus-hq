# Voorstel: DLsite, alle leeftijden (dlsite.com/home)

Vera, 8 nov 2026 run 13:33 (tweede platform van deze run). Zelf toegevoegd. DLsite is de grote Japanse winkel voor digitale werken van kleine makers ("circles"): manga, ASMR en stemwerk, muziek, beeld- en geluidsmateriaal, tools en kleine spellen. Ik keek alleen naar de afdeling voor alle leeftijden (/home), niet naar de volwassenenafdeling.

## In het kort
- **Advies: nee voor nu, cijfer 3.**
- **Geld is echt en de deur staat open:** registratie gratis, korte controle, DLsite rekent af. Bij een prijs van 1.000 yen krijgt de maker 600 yen, vanaf 4.400 yen 78,4% (GEZIEN, wervingspagina). DLsite noemt 17,1 miljoen leden en 2,1 miljoen werken (DERDEN, zelfde pagina). AI-werk mag, in een aparte AI-afdeling; deels AI-werk mag in de gewone afdeling (GEZIEN).
- **Maar wat wij kunnen maken verkoopt bijna niet:** nieuwe betaalde werken mei t/m aug 2026: mediaan 3 verkopen, 12,6% haalt 100+. Wat goed verkoopt is stemwerk en ASMR (mediaan 33, 38% haalt 100+), dat vraagt stemacteurs. Tools: mediaan 3, niemand 100+. Beeldmateriaal mediaan 1, geluidsmateriaal mediaan 0, niemand 100+ (GEZIEN).
- De teller is hier echt verkoop: de productpagina toont het getal als aantal aankopen ("purchase_label", 販売数) (GEZIEN in de broncode).

## Wat ik gemeten heb (GEZIEN)
Bron: de sitemaps van DLsite (home, work_0 t/m work_6, samen 68.491 werken) en de open productinfo `https://www.dlsite.com/home/product/info/ajax?product_id=<100 id's>`, met 10 seconden tussen verzoeken zoals robots.txt vraagt. Velden: dl_count (verkopen), prijs, registratiedatum, soort, maker.

Ik haalde alle 2.477 werken met een id tussen RJ01595000 en RJ01690000 (eind maart t/m eind augustus 2026). Maart en augustus zijn daardoor niet volledig, april t/m juli wel. Werken die niet meer te koop zijn staan mogelijk niet in de sitemap.

Bestanden in `data/`: `dlsite-home-mrt-aug-2026-11-08.jsonl.gz`, scripts `dlsite-haal-script.py` en `dlsite-analyse-script.py`.

### Nieuwe betaalde werken mei t/m aug 2026 (verkopen op 8 nov)
| Soort | Aantal | Mediaan | 0 verkopen | 100+ | 1.000+ | Makers | Mediaanprijs |
|---|---|---|---|---|---|---|---|
| Alle | 1.898 | 3 | 27% | 12,6% | 4,2% | 712 | 462 yen |
| Stemwerk/ASMR (SOU) | 468 | 33 | 12% | 38,0% | 16,2% | 179 | 742 |
| Manga (MNG) | 457 | 5 | 19% | 10,9% | 0,2% | 218 | 385 |
| Geluidsmateriaal (AMT) | 260 | 0 | 66% | 0% | 0% | 34 | 462 |
| Beeldmateriaal (IMT) | 219 | 1 | 38% | 0% | 0% | 56 | 550 |
| Muziek (MUS) | 120 | 1 | 17% | 0% | 0% | 34 | 275 |
| Tools (TOL) | 55 | 3 | 20% | 0% | 0% | 22 | 275 |
| Spellen (ADV, RPG, SLN, samen) | 58 | ±5 | | ±5% | 0% | 45 | ±450 |
| Makers met maar 1 werk in deze maanden | 449 | 11 | 9% | 21,6% | 7,3% | 449 | 550 |

- Drukte (alle leeftijden): ±440 tot 620 nieuwe betaalde werken per maand (april t/m juli). Rustig.
- Bruto per maker (verkopen x prijs, cohort): mediaan 5.610 yen (±€35) in 3 tot 6 maanden; 185 van de 712 makers kwamen boven 50.000 yen bruto (±€300). De top twee haalden 170 en 95 miljoen yen, allebei stemwerk (GEZIEN, ruwe rekensom).

## Voordelen
- Echte verkoopteller, open data, geld gaat contant naar de maker, iedereen mag beginnen, AI toegestaan als je het eerlijk aangeeft.
- Rustig en een groot koopgraag publiek; makers met één werk doen het beter dan het gemiddelde (mediaan 11).

## Nadelen
- De soorten die Dortus kan maken (tools, materiaal, kleine spellen met code) verkopen hier bijna niets: niemand haalde 100 verkopen.
- Wat verkoopt is stemwerk en manga, en (buiten dit onderzoek) volwassenenwerk. Dat past niet bij ons.
- Japans publiek, Japanse pagina's; Thijs moet een viviON ID en circle registreren en gegevens invullen.

## Wat we zouden bouwen
Alleen als proef: een set 3D-achtergrondmateriaal (GLB) voor makers, omdat zulke werken er al staan (bijvoorbeeld "電車内 3D背景素材 GLB" voor 660 yen). De cijfers van beeldmateriaal (mediaan 1, niemand 100+) maken dat weinig kansrijk.

## Advies
**Nee voor nu, cijfer 3.** Geld en toegang zijn goed, maar alleen voor werk dat wij niet maken. Herhaalmeting kan met de scripts in `data/`.

## Controle
Geen aparte controleur ingezet (tijd van de run op). Wel zelf nagekeken: de API-tellers zijn dezelfde als die de productpagina toont (veld dl_count onder het label voor aankopen), en het script draait opnieuw op het bewaarde bestand met dezelfde uitkomst. Een volgende run kan een controleur de tabel laten narekenen.
