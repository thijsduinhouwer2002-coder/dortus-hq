# Keuring Pro mooier overlay, 23 nov 2026, Daan
Wat ik keurde: voorstel `platformen/blender/mooier-overlay-2026-11-23.md`, tak `claude/pro-mooier-overlay` (kop 2250ff6, 5 commits voor op main), beelden in release `pro-mooier-1` (vergelijk-m1, m3, m4, m5, na-m7-paneel, zelf bekeken met Read).
Akkoord: **ja voor het ontwerp (A tot E en de pil-kleuren van H)**. Uitbrengen pas na moet 1 en 2 hieronder.

Ik keur dit uit eigen beweging: het voorstel vroeg de hoofdchat om een keurder, en uiterlijk van Click Joints is mijn rol. Ik heb niets gebouwd.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Van 9 zwevende getallen plus kopregel naar 1 label met naam bij het gekozen gewricht (m1, m3, m5). Geen tekst meer over het hoofd. | Feit (GEZIEN, vergelijk-m1 en m5) | hoog | |
| A2 | Voorbij de stop is het hele onderbeen met voet rood, met een rode pil "+12° past limit" (m4). "The part turns red" klopt nu met het beeld. | Feit (GEZIEN, vergelijk-m4) | hoog | |
| A3 | Rood gaat terug: `groei()` roept eerst `_terug` voor A en B aan, en `_terug` zet eerst `cj_rood_deel` terug, dan de rakende vlakken. Die volgorde klopt met hoe ze rood werden. | Feit (code gelezen) | hoog | toets rood heen en terug in `toetsen_figuur.py` staat erin |
| A4 | Export verandert niet: `drie_mf.py` schrijft geen materiaal of kleur weg, dus een rood deel komt niet rood in de 3MF. | Vermoeden (grep op material/kleur/color in drie_mf.py: niets) | midden | een 3MF exporteren met het been voorbij de stop en de kleur in het bestand nakijken |
| A5 | Paneel Figure joints toont "Labels Selected / All / None" onder de samenvatting; leest rustig (na-m7-paneel). | Feit (GEZIEN) | hoog | |
| A6 | Los scharnier en losse kogel tekenen zoals eerst, dus de gekeurde winkelbeelden 12 en 14 blijven waar. | Vermoeden (voorstel en code: `cj_figuur`-check bij kleur_deel) | midden | e2e plaatjes 11, 12 en 14 op de tak gelijk aan main |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | e2e op de tak: run 45160902348 (89b6cd1) **rood** in 4.2.23, 5.2.3 en 5.3.0, stap "Schermafbeeldingen van het scharnier (betaalde zip, plaatjes 11 en 12)". Run 45163344163 (2250ff6) liep nog toen ik keek. | Feit (GEZIEN, Actions-API 23 nov ±12:30 UTC) | hoog | tests groen voor af |
| B2 | De tak heeft geen gemeenschappelijke basis met de ondiepe kloon en staat 14 commits achter main (compare-API). Voor uitbrengen moet hij op de nieuwste main, anders mis je Lite/1.2-werk. | Feit (GEZIEN) | hoog | uitbrengen |
| B3 | De schermtests van de figuur zetten zelf Labels op All. Dat is geen test die zwakker is gemaakt om te slagen: die plaatjes toetsen de plek van alle getallen, en de stand Selected wordt zonder scherm getoetst in `toetsen_figuur.py`. | Feit (diff gelezen) | hoog | tests niet aangepast om te slagen |
| B4 | `scharnier_boog.py` is 437 regels (was al 420 op main, nu +17). | Feit | hoog | bestanden onder ±400 regels |
| B5 | `architectuur.md` +1 regel; cijfers in het voorstel hebben GEZIEN/DERDEN/GOK; geen persoonsgegevens. | Feit | hoog | |

## Deel C: zou een koper het mooi en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Grootste winst: de figuur leest nu als een mens met groene banden in plaats van een meetblad. Dit is het beeld dat Thijs bedoelt met "ziet er mooi uit". | | |
| C2 | De boog is in "na" veel bleker en doorzichtiger dan in "voor" (vergelijk-m3: voor fel groen, na lichtgroen waas). Op een telefoon in een Short valt hij weg op het grijze been. Nu er maar één boog staat, mag die juist feller. | Vulling van de boog in stand Selected terug naar de dekking van voor (of hoger), rand fel groen. | klein |
| C3 | Voorbij de stop houdt de naampil zijn groene bolletje terwijl het been rood is (m4). Twee kleuren die elkaar tegenspreken. | Bolletje rood zodra het voorbij de stop is. | klein |
| C4 | De rode pil hangt met een lange dunne lijn schuin over boog en scheen (m4); dat oogt rommelig. | Rode pil direct onder de naampil zetten (gestapeld), zonder of met korte lijn. | klein |
| C5 | Met niets gekozen staat er 0 labels (m2-schoon). Een nieuwe koper die net Figure from rig drukt ziet groene banden maar geen enkel getal en denkt misschien dat het niet werkt. | Na Figure from rig het eerste gewricht (knie) kiezen, of in de samenvatting een regel "Select a joint to see its range". | klein |
| C6 | Vooraanzicht (m1): de knieboog staat op zijn kant en is bijna onzichtbaar. Geen fout van de add-on, wel belangrijk voor opnames. | Winkelfoto's en eerste beeld van Shorts schuin (3/4) opnemen, zoals m3/m4. | klein (opname) |
| C7 | De keuze Labels staat op de WindowManager en wordt niet in de .blend bewaard (vermoeden): wie All kiest, krijgt na herstart weer Selected. | Op de scene of in de voorkeuren van de add-on bewaren. | klein |

## Moet (blokkeert uitbrengen, niet het ontwerp)
1. e2e op de tak groen in 4.2, 5.2 en 5.3 (B1). Is het rood door deze wijziging, eerst oplossen; is het een oude fout, dat laten zien.
2. Tak bijwerken met de nieuwste main en daarna opnieuw e2e (B2).
3. Bij uitbrengen de winkelzin aanpassen zoals het voorstel zelf zegt ("... at every joint (Labels: Selected or All)").

## Kan (sterk aangeraden vóór de nieuwe opnames)
C2 (feller boog) en C3 (rood bolletje) zijn klein en maken elk volgend filmpje beter; die zou ik meenemen vóór 1.2.1. C4, C5, C7 mogen later. F en G uit het voorstel: eens dat ze later kunnen.

Na moet 1 en 2 (en C2/C3 als ze worden gedaan) keur ik alleen die punten opnieuw, met nieuwe vergelijk-beelden.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
