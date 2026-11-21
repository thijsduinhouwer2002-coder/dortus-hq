# Keuring blender-gewrichten Pro-link in direct-zip, 22-11-2026, automatische keurder
Wat ik keurde: commit d8980241e (b8afdb7..d898024), bestanden `e2e/direct/direct.py` en `e2e/test_direct.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `URL` in `direct.py` is nu `https://dortus.com/click-joints/?from=addon#pro`. Dat is precies wat de commit over de Pro-link zegt. | Feit | Hoog | Het diff zelf. |
| 2 | De commit zegt ook dat de uitgave de direct-zip weigert en dat `indienen.md` twee zips noemt. Geen van beide staat in de gewijzigde bestanden. | Feit (ontbreekt in het diff) | Hoog | Een diff of eerdere commit met de wijziging aan `click-joints-uitgave.yml` en `indienen.md`. |
| 3 | Of de Pro-pagina een anker `#pro` heeft, en of de pagina `?from=addon` verwerkt, is hier niet te zien. Zonder anker opent de pagina gewoon bovenaan, dat is geen fout. | Vermoeden | Midden | De HTML van dortus.com/click-joints/ met `id="pro"` (curl). |
| 4 | De link opent alleen via `wm.url_open` na een klik van de gebruiker. De parameter `from=addon` bevat geen persoonsgegevens. | Feit | Hoog | Het diff en de kop van `direct.py`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is aangepast aan de nieuwe URL. De controle is niet verzwakt: het blijft een exacte gelijkheid. Dat is een bewuste wijziging, geen aanpassing om te slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het gewijzigde bestand `direct.py` blijft ver onder de ±400 regels. | Vermoeden | Midden | Bestandsgrootte (alleen een regel in het diff) |
| 3 | `architectuur.md` is niet bijgewerkt. In het zichtbare deel staat de URL ook nergens, dus dat lijkt niet nodig. | Vermoeden | Midden | architectuur.md bijgewerkt |
| 4 | De Pro-link zit in de direct-zip, niet in de zip voor extensions.blender.org. Of de uitgave dat echt scheidt, staat niet in dit diff (zie A2). | Vermoeden | Midden | Geen verwijzing naar betaald op extensions.blender.org (ToS 3.3, 3.10, 6.1) |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden gezien. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik kan niets zien of spelen. Met `#pro` komt iemand direct bij het Pro-gedeelte, als het anker bestaat. | Controleer in een browser dat de pagina bij `#pro` goed scrolt, ook op een telefoon. | Klein |
| 2 | Meetbaar via `?from=addon` hoeveel klikken uit de add-on komen. | Zet in `indienen.md` waar Daan of Thijs dat terugziet. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Laat zien waar de weigering van de direct-zip in de uitgave en de twee zips in `indienen.md` staan. De commit noemt ze, maar ze zitten niet in dit diff. Als ze nergens staan, kan de direct-zip met Pro-link op extensions.blender.org belanden en dat is dan wel een moet.
- Controleer met curl dat `id="pro"` op dortus.com/click-joints/ bestaat.
- Het diff is te klein om de bestandsgrootte en architectuur.md sluitend te toetsen. Kijk bij de volgende grotere wijziging weer.

---
Automatische keurder, model `claude-sonnet-5-5`, 17808 tokens in, 2545 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
