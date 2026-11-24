# Keuring blender-gewrichten winkelschermbeelden ronde 2, 24-11-2026, automatische keurder
Wat ik keurde: commit 11d225cd6, bestand producten/blender-gewrichten/e2e/scherm_winkel.py (alleen tekst gelezen, niets gedraaid)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het script zet voor de winkelbeelden "More bones" aan via `figuur_uit_rig(meer=True)`, zodat de enkels in de lijst staan. Dat past bij de akkoord-regel van 24 nov voor Pro 1.2.6 (robot-enkels). | Feit (diff) | Hoog | Dat is het doel van de commit en past bij de opdracht. |
| 2 | Of de operator `figuur_uit_rig` een parameter `meer` heeft, zie ik in deze diff niet. De assert controleert alleen de tekst van de aanroep, niet de parameter. | Vermoeden | Midden | Een groene run van dit script in de e2e, of `meer` in de operator in Pro 1.2.6. |
| 3 | `kies_romp` kiest het deel met de meeste hoekpunten als actief object en selecteert alle delen. Zo tonen lijst, knoppen en stap 3 het figuur. | Feit (code) | Hoog | De beelden w1 en w2 zouden dit bevestigen. |
| 4 | Dit is alleen een script voor winkelbeelden. Er verandert niets in de add-on of de zip. | Feit | Hoog | `git diff --stat` laat één bestand zien. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test is versoepeld om te slagen. De nieuwe assert controleert juist strenger dat de bronregel nog bestaat. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Het script voegt ±15 regels toe. De totale lengte van het bestand zie ik niet. | Vermoeden | Laag | Bestanden onder ±400 regels: `wc -l` op het bestand |
| 3 | `architectuur.md` is niet bijgewerkt. Voor een e2e-hulpscript is dat waarschijnlijk niet nodig. | Vermoeden | Midden | Staat `scherm_winkel.py` in architectuur.md? |
| 4 | Geen persoonsgegevens, sleutels of cijfers zonder bron in de diff. Het beeld komt uit de echte Blender, niet van een AI. | Feit | Hoog | Persoonsgegevens, geen AI-beeld |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De commentaarregel zegt "oranje rand is uit". Maar `kies_romp` selecteert alle delen, en geselecteerde objecten krijgen in Blender normaal een oranje rand. Zo'n rand maakt het winkelbeeld drukker. Ik kan het beeld niet zien. | Check op w1 en w2 of er een oranje rand staat. Zo ja, selecteer alleen de romp of zet de overlay uit. | Klein |
| 2 | Ik kan de beelden zelf niet beoordelen. Of de enkels er goed uitzien en de lijst leesbaar is, moeten Daan en Iris met de Read-tool zien. | Daan bekijkt w1, w2 en w3 voor ze in de winkel gaan. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer dat `figuur_uit_rig` echt `meer` kent (B/A2). De groene run van het script bevestigt dat.
- Controleer of de oranje rand op w1 en w2 echt weg is (C1).
- Controleer de bestandslengte van `scherm_winkel.py` (B2).
- Daan keurt de beelden zelf op uiterlijk voor ze live gaan.

---
Automatische keurder, model `claude-sonnet-5-5`, 18246 tokens in, 2322 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
