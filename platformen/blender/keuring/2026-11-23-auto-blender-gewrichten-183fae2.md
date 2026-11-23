# Keuring blender-gewrichten, opschonen na Exact-snede (Pro 1.2.3), 23-11-2026, automatische keurder
Wat ik keurde: commit 183fae213 (herstel.py, scharnier.py, terugval.py, architectuur.md)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging doet wat de commit zegt. Na een Exact-snede (4.2) voegt `opschonen` punten binnen 0,0001 mm samen en haalt platte vlakjes weg. Dat gebeurt alleen als het deel gesloten blijft en het volume gelijk is, anders blijft de mesh zoals hij was. | Feit (uit de code) | hoog | Niet van toepassing. |
| 2 | Of dit het echte probleem oplost (de robot van studio-3 viel op 4.2 terug van 4 naar 2 gewrichten), blijkt niet uit de tekst. Run 45273407326 in architectuur.md beschrijft het probleem, niet de uitslag na de fix. | Vermoeden | midden | Een groene 4.2.23-run van de robot-meting met 4 gewrichten en `cj_opgeschoond` groter dan 0 op de elleboogsnede. |
| 3 | De gratis build is niet geraakt (alleen bestanden onder `betaald/`). De gratis zip blijft dus gelijk. | Feit | hoog | `toets_zips.py` groen. |
| 4 | De aanroepen kloppen op papier. In `scharnier.py` en `terugval.py` wordt `na_exact` alleen bij EXACT gebruikt. Na de Manifold-terugval wordt het ook gebruikt, want die snijdt dan met Exact. Het pad voor Manifold (5.x) blijft gelijk. | Vermoeden (alleen diff gelezen) | midden | De regressietoetsen op 5.2.3 en 5.3.0 groen, en de toets `solver_terugval` groen. |
| 5 | Extra rekentijd op grote delen is niet bekend. `opschonen` bouwt een bmesh en telt alle randen met Python op elk gesloten deel. Het scharnier en de kogelsnede krijgen dit nu na elke Exact-snede. | Vermoeden | laag | De snijtijd op 4.2 bij het arm-figuur van 261K driehoeken in de nieuwe run (eis 4 blijft onder 5 s voor de gratis kern). |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt: herstel.py, `opschonen`, `na_exact`, `cj_opgeschoond` en de reden staan erin. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er is geen testbestand gewijzigd, dus er is niets aangepast om te slagen. Er is ook geen nieuwe toets voor `opschonen` meegekomen. | Feit | hoog | tests niet aangepast om te slagen |
| 3 | De bestandslengte van `herstel.py` en `scharnier.py` is uit de diff niet te zien. `herstel.py` groeit met ongeveer 40 regels. | Vermoeden | laag | bestanden onder ±400 regels |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | geen persoonsgegevens |
| 5 | Het getal "2 gewrichten in plaats van 4" staat bij een run-nummer, maar zonder het label GEZIEN, DERDEN of GOK. | Feit | midden | cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze tekst. Voor de koper telt vooral dat "Figure from rig" op 4.2 minder gewrichten overslaat. Dat is alleen te beoordelen op de uitslag van de robot-meting. | Na de run de lijst "Skipped" voor de robot in 4.2 naast de oude leggen. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Een toets die een deel met twee samenvallende punten maakt en bewijst dat `opschonen` het gesloten houdt met gelijk volume. Ook een toets dat het niets doet als het volume of de sluiting zou breken.
- Het resultaat van de 4.2-run (aantal gewrichten, snijtijd) in architectuur.md zetten, met GEZIEN erbij.
- De snijtijd op 4.2 na deze wijziging controleren (vermoeden 5 hierboven).

---
Automatische keurder, model `claude-sonnet-5-5`, 24881 tokens in, 4184 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
