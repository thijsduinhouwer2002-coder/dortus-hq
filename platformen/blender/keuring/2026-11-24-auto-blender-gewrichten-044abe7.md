# Keuring blender-gewrichten takenlijst, 24-11-2026, automatische keurder
Wat ik keurde: commit 044abe7eb, bestand producten/blender-gewrichten/taken.md
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt alleen een nieuw bestand `taken.md` toe, met een kop, een leeg "Weekdoel" en een lege "Open taken". De add-on, de opdracht in `ontwerp.md` en de winkelbeloftes blijven ongemoeid. | Feit (diff) | hoog | Een diff die alleen dit ene bestand toont. |
| 2 | De commitregel noemt meer dan alleen deze lijst: geen lege rondes, lichter keuren, laatste meter 20:00, dagrapport 21:30. Die onderdelen staan niet in de meegestuurde diff voor dit product. | Vermoeden | midden | De andere bestanden uit commit 044abe7eb. Ze horen bij een andere keuring en niet bij dit product. |
| 3 | Het akkoord in `ontwerp.md` voor Pro 1.2.6 (robot-enkels) hangt aan tak 6dc287f en blijft staan. Deze wijziging raakt de code niet, dus dat akkoord verandert niet. | Feit (diff) | hoog | Geen wijziging in `click_joints/` of in de zip-builds. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast of weggehaald. | Feit (diff) | hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand is 6 regels, ruim onder de ±400. | Feit | hoog | Bestandsgrootte |
| 3 | De wijziging bevat geen persoonsgegevens, sleutels of wachtwoorden. | Feit (diff) | hoog | Geen persoonsgegevens |
| 4 | `architectuur.md` is niet bijgewerkt. Dat hoeft niet, want er is geen code of structuur veranderd. | Feit | hoog | architectuur.md bijgewerkt |
| 5 | Er staan geen cijfers, spelerstekst of beeld en geluid in. | Feit (diff) | hoog | GEZIEN/DERDEN/GOK, CONCEPT, geen AI-beeld op Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Dit is een intern werkbestand. Er verandert niets wat een gebruiker ziet of speelt. | Niets nodig. | klein |
| 2 | Het bestand heeft nog geen inhoud: "(eigenaar vult in)" en een lege lijst. Het is dus nog niet te zien of het werkritme helpt. | Zodra er taken in staan, de eerste taak koppelen aan het open punt "hap uit de hiel van de blokvoet kleiner" uit het akkoord van Daan. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Vul het weekdoel en de eerste open taken in, zodat de lijst niet leeg blijft staan. Een leeg weekdoel gaat tegen "geen lege rondes" in.
- Zet er een datum en een eigenaar bij, en bij elke taak het product of de tak. Dan is de lijst na een week nog te volgen.
- Laat in de commitregel de onderdelen weg die niet bij dit product horen, of splits ze in aparte commits. Dan is te zien welke keuring waarbij hoort.

---
Automatische keurder, model `claude-sonnet-5-5`, 17204 tokens in, 1433 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
