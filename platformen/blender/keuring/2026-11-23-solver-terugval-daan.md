# Keuring terugval naar Exact, 23 nov 2026, Daan
Wat ik keurde: tak `claude/blender-solver-terugval` op 02ac53f (`gewricht.py`, `e2e/toetsen_correcties.py`, CHANGELOG), e2e run 45192782267 (job 5.3.0 gelezen; 4.2.23 en 5.2.3 liepen nog om 14:35 UTC)
Akkoord: nee (1 moet, de code zelf is goed)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Manifold met open deel: één keer opnieuw met Exact, daarna pas de fout. Alleen als de eerste solver MANIFOLD is, dus op 4.2 (Exact) geen dubbel werk. | feit (code) | hoog | |
| A2 | Toets 1x open in 5.3.0: twee gesloten delen, `cj_solver` EXACT, `cj_solver_terugval` aan, geen hulpresten, passing groen (log regels 1156-1172). | feit (log GEZIEN) | hoog | |
| A3 | Toets 2x open: nette weigering, figuur heel en zichtbaar, geen `cj_hulp` over (log 1173-1177). | feit (log GEZIEN) | hoog | |
| A4 | `ruim_extra` haalt alleen weg wat na de eerste `bereid` in de hulpcollectie kwam; `bereid` werkt op een bmesh-kopie en `snij` maakt alles via `bak` in `hulp`, dus `cj_werk` blijft gelijk voor poging 2. Namen als `cj_boven` komen weer vrij omdat de oude objecten echt weg zijn. | feit (code gelezen) | midden | Een echte Manifold-fout (het arm-figuur van Olaf, 8 tegen 9 gewrichten) door de tak halen in plaats van alleen FORCEER_OPEN. |
| A5 | Alle overige e2e-stappen in 5.3.0 OK ("klaar, fouten: []", regel 1326). | feit (log GEZIEN) | hoog | |
| A6 | Exact kan traag zijn: in dezelfde run duurde Exact 84,5 s op 261.120 driehoeken (en gaf daar toch 139 foute randen). Bij een zwaar figuur betekent de terugval dus tot anderhalve minuut stil scherm, met daarna mogelijk alsnog de fout. | feit (log regel 1154) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | **De e2e is rood**: `toets_zips.py` FOUT "gratis zip gelijk aan de gekeurde stand 014172e (sha256 per bestand) gewricht.py" (log regel 1485, exit 1). De wijziging zit in het gratis deel, en dat moet gelijk blijven aan de gekeurde live zip. Precies dezelfde rode toets als run 7 bij de snippers (`ontwerp-1.1.md` regel 64). | feit (log GEZIEN) | hoog | Werk is pas af als de tests groen zijn; gratis deel blijft gelijk aan de gekeurde stand |
| B2 | Toets niet aangepast om te slagen; nieuwe toets met echte eisen. Bestanden 361 en 350 regels (onder 400). | feit | hoog | |
| B3 | De CHANGELOG-regel staat bij de gratis versie (Unreleased, die de releasenotes op extensions.blender.org voedt). Hoort mee te verhuizen met B1. | feit | hoog | |

## Deel C: zou een gebruiker het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Minder vaak "no watertight parts" is precies wat een koper wil; dit is een goede wijziging. | | |
| C2 | Als de terugval lang duurt (A6) ziet de gebruiker niets en denkt dat Blender vastzit. | In de melding na afloop zeggen dat het opnieuw is geprobeerd, bv. "Joint placed (retried with the Exact solver).", en vooraf een cursor-wacht of `window_manager.progress_begin`. | klein |

## Moet (blokkeert akkoord)
1. **Toets_zips groen maken (B1, B3).** Mijn keuze: zet de terugval in Pro, zoals de snippers (`betaald/` omhult de stap in `gewricht.py` van buitenaf), en laat de gratis bestanden byte voor byte op 014172e. Reden: de gratis 0.1.2-zip uit 6e3e768 wacht op uploaden en moet gelijk blijven; Pro krijgt er een echte reden bij ("fewer failed cuts") vlak voor de saleweek. De CHANGELOG-regel gaat dan naar de Pro-releasenotes (1.2.2). In het gratis deel kan hij later mee in 0.1.3, met een bewuste nieuwe gekeurde stand.

## Kan (mag later)
1. C2: de melding noemt de terugval, en een wachtcursor tijdens de tweede snede.
2. A4: één keer door een echt Manifold-open figuur halen (spoor Olaf) naast de FORCEER_OPEN-toets.
3. Na moet 1 keur ik alleen moet 1 opnieuw, plus de groene uitslag in alle drie de versies.
