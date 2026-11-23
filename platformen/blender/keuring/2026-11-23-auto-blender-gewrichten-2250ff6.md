# Keuring blender-gewrichten (Pro mooier overlay), 23-11-2026, automatische keurder
Wat ik keurde: commits 89b6cd1..2250ff6 (2250ff6c5), alleen de tekst van de diff, niets gedraaid
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht in `ontwerp.md` gaat over gratis 0.1.1 en Pro 1.0.2. Dit is een kleine verplaatsing in de Pro-overlay (Pro mooier), dus ik toets tegen de commit-titel en de beschrijving in `architectuur.md`.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `label_tekst` en `figuur_x` staan nu in `labels.py` en `scharnier_boog.py` haalt ze daar op. De logica is gelijk: Selected geeft 1,0, anders 0,7. | Feit (diff) | Hoog | Groene `mooier` in `toetsen_figuur.py` en groene schermtests 15 tot 19. |
| 2 | De rode pil "+N° past limit" komt alleen bij een figuur (`fig`). Een los scharnier gebruikt weer `waaier._tekst(... ROOD ...)`, zodat beeld 12 en 14 hetzelfde blijven. De architectuurtekst zegt hetzelfde. | Feit voor de code, vermoeden voor het beeld | Midden | Schermtest 12 en 14 op de rode pixels van de stop, ongewijzigd groen. |
| 3 | In de nieuwe `else`-tak is `rood_tekst` de teruggave van `waaier._tekst(...)`. In de `if`-tak is het `pil(...) is not None`. Of `_tekst` iets teruggeeft dat even waar of onwaar is, zie ik niet. | Vermoeden | Laag | De definitie van `waaier._tekst` en hoe `rood_tekst` daarna wordt gebruikt. |
| 4 | `scharnier_boog.py` importeert nu bovenaan `.labels`, terwijl `figuur_x` dat eerst pas binnen de functie deed. Een kringimport zou bij registreren stuk gaan. Het commentaar in `labels.py` ("zelfde als scharnier_boog.FIGUUR_X") wijst erop dat `labels.py` zelf `scharnier_boog` niet importeert. | Vermoeden | Midden | De groene run van `test_betaald.py` (installeren en registreren van de betaalde build). |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | In de vier schermtests is alleen een lege regel toegevoegd (stijl). Er zijn geen toetsen aangepast om te slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` beschrijft de nieuwe labels en de rode pil. De verhuizing van `label_tekst` en `figuur_x` naar `labels.py` staat er niet letterlijk in. | Feit | Midden | `architectuur.md` bijgewerkt |
| 3 | `FIGUUR_X_ALLE = 0.7` staat nu dubbel: in `labels.py` en als `FIGUUR_X` in `scharnier_boog.py`. Past men er één aan, dan lopen ze uit elkaar. | Feit | Hoog | Klein onderhoudspunt, geen regelbreuk |
| 4 | De regelaantallen van `labels.py` en `scharnier_boog.py` staan niet in de tekst. `scharnier_boog.py` wordt korter, `labels.py` groeit met ongeveer 14 regels. | Vermoeden | Laag | Bestanden onder ±400 regels (`wc -l`) |
| 5 | Er staan geen persoonsgegevens of sleutels in de diff, en er is geen beeld of geluid voor Steam. De gratis build bevat `betaald/` niet, dus `toets_zips` blijft daar naar verwachting groen. | Feit | Hoog | Geen persoonsgegevens, twee builds |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beelden, dus dit zijn vermoedens. De diff verandert zelf bijna niets aan het beeld.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Bij een figuur staat de rode pil voorbij de stop nu in dezelfde pilstijl als de andere labels. Dat oogt waarschijnlijk rustiger, maar zonder beeld niet te bevestigen. | Kijk naar de beelden van `scherm_mooi.py` (release `pro-mooier-1`) voor en na. | klein |
| 2 | Een los scharnier houdt zijn oude rode tekst. Een gebruiker ziet dan twee stijlen in één add-on. | Op een later moment ook los de pil gebruiken, met nieuw gekeurde beelden 12 en 14. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Haal `FIGUUR_X_ALLE` en `FIGUUR_X` samen naar één plek, zodat er één waarheid is.
- Controleer dat `waaier._tekst` een bruikbare teruggave heeft voor `rood_tekst` (Deel A 3).
- Controleer de regelaantallen van `labels.py` en `scharnier_boog.py`.
- Noem de verhuizing van `label_tekst` en `figuur_x` expliciet in `architectuur.md`.
- Dit oordeel is alleen op tekst gebaseerd. Beeld en speelplezier keuren Daan en Iris, en voor live zetten blijft een keuring door een agent nodig.

---
Automatische keurder, model `claude-sonnet-5-5`, 23816 tokens in, 4190 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
