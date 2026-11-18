# Keuring zaad voor de dobbelstenen per test (Rollwright e2e), 19-11-2026, automatische keurder
Wat ik keurde: commit 1cd470c4 (a237762..1cd470c), bestanden `e2e/wdio.conf.mjs` en `architectuur.md` van obsidian-rollwright
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is de commitbelofte: het zaad gaat voor elke test terug naar het begin. `ontwerp.md` gaat over `src/` en `styles.css`, en die zijn niet geraakt, dus het akkoord van Daan voor 0.3.5 blijft ongemoeid.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De hook `beforeTest` roept `zaai()` aan. Die zet `window.__dortusZaad` terug op 20261119. De functie wordt alleen geïnstalleerd als `__dortusRandom` nog niet bestaat. Zo begint elke test met dezelfde reeks. | Feit (uit de diff) | hoog | Een run waarin twee runs van dezelfde commit gelijke schermen geven. |
| 2 | Na een herstart van Obsidian is het venster nieuw, dus `__dortusRandom` ontbreekt en `zaai()` installeert de functie opnieuw. Dat dekt het geval dat de oude `before` miste. | Vermoeden | midden | Een spec die Obsidian herstart en daarna dezelfde worpen toont. |
| 3 | Tests die eerder op een dieper punt in de reeks draaiden, krijgen nu andere getallen. Een test die op een bepaalde worp rekende (bijvoorbeeld geen natuurlijke 20, of twee verschillende uitkomsten na elkaar) kan nu rood worden. | Vermoeden | midden | Een groene e2e-run op main met deze commit. In de tekst staat geen run. |
| 4 | Specs die `Math.random` zelf vastzetten (crit, classic) en niet herstellen, behouden die override in een volgende test. `zaai()` zet de functie niet terug als `__dortusRandom` al bestaat. | Vermoeden | laag | Nalezen of crit en classic in een `finally` of `after` herstellen, zoals de commentaar zegt. |
| 5 | Het commit-onderwerp noemt een "bericht aan Olaf", maar er is geen `berichten/olaf.md` meegestuurd. | Vermoeden | midden | De commit zelf bekijken op dat bestand. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Alleen de testconfiguratie (hooks) en de uitleg zijn veranderd. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt: de hooks `before` en `beforeTest`, de reden en het feit met bron (GEZIEN 19 nov, run 44420801178). | Feit | hoog | architectuur.md bijgewerkt, cijfers met GEZIEN/DERDEN/GOK |
| 3 | `wdio.conf.mjs` is klein. De lengte van `architectuur.md` is afgekapt en dus niet te controleren. | Vermoeden | laag | Bestanden onder ±400 regels |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. Het zaad is een getal. | Feit | hoog | Geen persoonsgegevens |
| 5 | De regel `console.log("ZAAD GEZET")` is weg. Als een workflow daarop zoekt, valt die controle weg. | Vermoeden | laag | Zoeken naar "ZAAD GEZET" in `.github/workflows/` en `organisatie/controle/`. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer bij de eerstvolgende e2e-run op main dat geen test rood wordt door het nieuwe begin van de reeks (A3).
- Controleer dat crit en classic hun eigen `Math.random` altijd herstellen, ook bij falen (A4).
- Zoek of iets op "ZAAD GEZET" in het log vertrouwt, en zet zo nodig een logregel terug (B5).
- Zet een lege regel tussen de koptekst en de nieuwe JSDoc boven `zaai()`. Dat is puur netheid.
- Voeg het bericht aan Olaf toe of controleer dat het in de commit zit (A5).

---
Automatische keurder, model `claude-sonnet-5-5`, 21334 tokens in, 3237 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
