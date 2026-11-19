# Keuring blender-gewrichten, 19-11-2026 12:13 NL, automatische keurder
Wat ik keurde: commit 3fb6d4a2 (8ad9273..3fb6d4a): `betaald/scharnier.py`, `e2e/toetsen_scharnier.py`, `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is hier niet het akkoord op 1.0.2 in `ontwerp.md`. Het is de eigen belofte van de commit: een eerder Tight-gewricht blijft Tight op zijn deel na Place hinge, en de toetsen Good fit en Tight.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De code onthoudt `cj_passing`, `cj_snijpunt` en `cj_wand_mm` van het bronobject voor het snijden. Na het snijden houdt het deel aan de kant van het oude snijpunt oranje of rood en de oude wand. Het andere deel blijft groen. | Feit (uit de diff) | Hoog | Een groene run van `toets_tight_blijft`. |
| 2 | Ontbreekt het oude snijpunt, dan houden beide delen de oude passing. Dat is een bewuste keuze en staat zo in `architectuur.md`. | Feit | Hoog | Geen. |
| 3 | De nieuwe toets `toets_tight_blijft` zet zelf een staaf met oranje, wand 0,9 en snijpunt op x=15. Hij plaatst een scharnier op x=0 en eist oranje met wand 0,9 op het rechterdeel en groen op het linkerdeel. De toets neemt aan dat `vorm.kant` het punt op x=15 aan het rechterdeel geeft. | Vermoeden | Midden | Een groene run in 4.2 en 5.2 (in de tekst niet te zien). |
| 4 | De Good fit-toets controleert `cj_passing == ["groen","groen"]` op beide delen en dat `fit_tekst("groen", -1.0)` "Good fit" geeft. Dat dekt de eerdere klacht dat stap 3 "No joint yet" zei. | Feit (toetsinhoud) | Hoog | Een groene run. |
| 5 | Het rode geval (`oud_pas == "rood"`) heeft geen eigen toets. De toets dekt alleen oranje. | Feit | Hoog | Een extra toets, of de bevestiging dat een rood object nooit een scharnier kan krijgen. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is alleen een toets bijgekomen en er is geen bestaande toets versoepeld. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` heeft een nieuwe regel over de passing bij het scharnier, met de bestanden en de toetsen. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Of `scharnier.py` en `toetsen_scharnier.py` nog onder ±400 regels zijn, kan ik niet zien. De diff voegt ongeveer 8 en 35 regels toe. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | De wijziging raakt alleen de betaalde build. De gratis zip en de changelog blijven ongewijzigd, dus er is geen betaald woord in de gratis build gekomen. | Feit | Midden | Gratis zip zonder betaald (`toets_zips.py`) |
| 6 | Er is geen run of log meegestuurd. Dat de nieuwe toetsen slagen is dus niet gezien. | Feit | Hoog | Cijfers GEZIEN, niet geraden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Draai de run in 4.2 en 5.2 en bevestig dat `toets_tight_blijft` slaagt. Dit gaat om de aanname dat `vorm.kant` x=15 aan het rechterdeel geeft.
- Voeg een toets toe voor het rode geval, of leg vast dat dit geval niet kan voorkomen.
- Controleer of na het scharnier het oude `cj_snijpunt` van het eerdere gewricht nog bruikbaar is. Zo niet, dan houden bij een derde gewricht beide delen de oude passing.
- Controleer de regelaantallen van `scharnier.py` en `toetsen_scharnier.py` tegen de grens van ±400.
- Als `cj_wand_mm` ontbreekt bij het oude gewricht, blijft de wand van het scharnier staan. Controleer dat die waarde dan niet misleidend is.

---
Automatische keurder, model `claude-sonnet-5-5`, 23397 tokens in, 3133 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
