# Keuring blender-gewrichten: uitslag toets verlies bij kogels, 24-11-2026, automatische keurder
Wat ik keurde: commit 37de78bce (bestand `producten/blender-gewrichten/proeven/betrouwbaar-rig-2026-11-23/uitslag.md`, bereik 25efd95..37de78b)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging raakt alleen het uitslagbestand van een proef. De add-on, de zips en de winkelbelofte blijven gelijk. De eerdere akkoorden (0.1.1 en 1.0.2) worden dus niet geraakt.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | In de diff staat geen add-on-code, alleen twee regels tekst in de uitslag. | Feit | Hoog | Niets nodig, dit staat in de diff. |
| 2 | De tekst zegt dat de toets "verlies bij kogels" (`CJ_HERKANS=3`) groen is in 4.2.23, 5.2.3 en 5.3.0, in run 45282711688. Ik kan die run niet openen. | Vermoeden | Midden | Het log van run 45282711688, stap Figuurpresets, met de regel "na een kogelsnede die te veel verliest neemt de knop een volgende plek" in alle drie versies. |
| 3 | De regel over afgebroken runs is veranderd van "4.2 rigify tak 1 van 5" in "4.2 rigify tak (2 van 5)". De diff laat niet zien waarom het getal verandert. | Vermoeden | Laag | De loglijst van de run met de afgebroken 4.2-taken (exit 143). |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast. De diff bevat alleen tekst in het uitslagbestand. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Er staan geen persoonsgegevens of sleutels in de diff. | Feit | Hoog | Geen persoonsgegevens |
| 3 | De nieuwe zin over de e2e-run mist een label GEZIEN, DERDEN of GOK, terwijl de zin ervoor GEZIEN heeft. Het is een eigen run, dus waarschijnlijk GEZIEN. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | De regels over bestanden onder ±400 regels en over `architectuur.md` zijn hier niet van toepassing, want er is geen code gewijzigd. De totale lengte van het uitslagbestand kan ik niet zien. | Vermoeden | Midden | Bestanden onder ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niets te zien of te spelen in deze wijziging, dus geen bevindingen.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Geen beeld of spel in deze wijziging. | Niet van toepassing. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij de nieuwe zin over run 45282711688 het label GEZIEN, en noem de stap en de drie versies bij naam.
- Leg in één zin uit waarom "tak 1 van 5" nu "tak (2 van 5)" is. Het lijkt een correctie, maar de uitslag zegt dat niet.
- Het succes in de e2e-job (4.2.23) staat naast een afgebroken 4.2-rigify-taak in de rig-toetsen. Dat zijn andere taken, maar zet er één regel bij dat de 4.2-dekking daar nog niet volledig is.

---
Automatische keurder, model `claude-sonnet-5-5`, 18012 tokens in, 2049 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
