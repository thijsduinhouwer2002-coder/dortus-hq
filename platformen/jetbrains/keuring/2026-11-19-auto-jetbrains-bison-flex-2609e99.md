# Keuring Bison & Flex beeldvergelijking (roestronde R4), 19-11-2026, automatische keurder
Wat ik keurde: commit 2609e997 (8c12304..2609e99): `architectuur.md`, `e2e/.../Gedeeld.kt`, `e2e/.../Winkelschermen.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is `ontwerp.md`. Deze wijziging raakt alleen de testhulp voor de beeldvergelijking, niet de plugin of de winkelbelofte.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Er verandert niets aan wat de gebruiker van de plugin ziet of krijgt. De belofte (gratis en Pro, eis 1 t/m 11) blijft ongemoeid. | Feit | hoog | Een diff van `src/main` zou leeg zijn. Dat staat hier niet in de lijst van gewijzigde bestanden. |
| 2 | `schermStil` is gesplitst in `wachtTotStil(bestand, venster, pogingen)` en daarna `scherm(bestand)`. In de getoonde regels is het gedrag van `schermStil` gelijk gebleven. | Feit | hoog | Die twee regels in de diff. |
| 3 | `winkelAllePlekken` wacht nu op een stilstaand scherm ("root") vóór `schermHeel("winkel-alleplekken.png")`. Of dat de wisselende boom oplost, is niet uit de tekst te halen. | Vermoeden | midden | Twee push-runs op dezelfde code met 0 grote verschillen op `winkel-alleplekken` zouden het bevestigen. |
| 4 | Daans akkoord (tot en met 281d0a3) blijft geldig, want er is niets zichtbaars gewijzigd. | Feit | hoog | Geen wijziging buiten `e2e/` en documentatie. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test versoepeld. De assert op "Find-paneel open" blijft staan. Er komt alleen een wachtstap bij. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt met de gevonden oorzaak. Daarbij zijn run-nummers genoemd met GEZIEN. | Feit | hoog | architectuur.md bijgewerkt, cijfers met GEZIEN/DERDEN/GOK |
| 3 | De doc zegt dat de boom in het conflictvenster en het Find-paneel "niet meetellen". In deze diff staat geen wijziging in `beelden.sh` of `beeldvergelijk.py`. Mogelijk zat dat masker er al, mogelijk klopt de doc nog niet met de code. | Vermoeden | midden | architectuur.md moet kloppen met de code |
| 4 | De misplaatste kdoc van `scherm` stond boven `schermStil`. Die staat nu weer bij `scherm`. | Feit | hoog | Leesbaarheid (kan) |
| 5 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De bestanden zijn korter dan 400 regels, voor zover in de diff te zien. | Feit | midden | Geen persoonsgegevens, bestanden onder ±400 regels |
| 6 | Er komt geen AI-beeld of -geluid op Steam, en geen spelerstekst van Hats. Beide zijn niet van toepassing. | Feit | hoog | Overige regels |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Controleer of het masker voor de boom in het conflictvenster en het Find-paneel echt in `organisatie/controle/beelden.sh` of `beeldvergelijk.py` zit. Zo niet, zet het erin of haal die zin uit `architectuur.md`. Alleen die twee scripts zouden dit bevestigen.
2. De doc zegt dat de bomen ook bij stilstaand beeld wisselen. Dan helpt `wachtTotStil` op `winkel-alleplekken` waarschijnlijk niet. Kijk na twee push-runs of het verschil weg is. Zo niet, vertrouw dan op het masker.
3. Laat `wachtTotStil` loggen als het scherm na alle pogingen nog niet stil is. Dan blijft zichtbaar dat de opname toch is gemaakt. Ik zag in de diff niet of dat al zo is.

---
Automatische keurder, model `claude-sonnet-5-5`, 22254 tokens in, 3321 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
