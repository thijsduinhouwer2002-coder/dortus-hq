# Keuring blender-gewrichten studio-figuren-proef, 23-11-2026, automatische keurder
Wat ik keurde: commits 649680f..4a4f971, dus `proeven/studio-figuren-2026-11-23/uitslag.md` en twee beelden (de beelden kreeg ik niet te zien)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt geen add-on-code. Het is alleen een proefverslag en twee beelden. Het akkoord van 16 nov voor Click Joints 0.1.1 en Pro 1.0.2 blijft dus ongewijzigd. | Feit (lijst gewijzigde bestanden) | hoog | Een diff van `click_joints/` tussen de commits die leeg is. |
| 2 | De opdracht was uit te zoeken waar een gewricht wegvalt. De tabel geeft per figuur het aantal gewrichten, de reden van de add-on en wie het aan ligt. Dat beantwoordt de vraag. | Feit (tekst) | hoog | n.v.t. |
| 3 | De tellingen kloppen onderling. Voorbeelden: 0,8 × 61 = 48,8 mm, en knight met 3 gewrichten (twee ellebogen plus één knie) past bij de tekst. | Feit (nagerekend) | midden | De logs `kandidaten.txt` en `proef-<model>.log` uit release `studio-1`. |
| 4 | De claim over het beeld ("rechts in beeld alleen 140° bij de elleboog, geen kogel") kan ik niet nagaan. Ik zie geen beelden. | Vermoeden | laag | Het beeld `figuur-a-lijst-linkerschouder-weg.jpg` bekijken met de Read-tool. |
| 5 | Het verslag zegt "8 van 9" in de tabel en "9 gewrichten na f9391c8". Onderaan staat "vol figuur (8 gewrichten)". Dat is verwarrend, maar de 9 is eerlijk als "nog niet zelf gezien" gemarkeerd. | Feit (tekst) | hoog | Een nieuwe studio-run na f9391c8. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen testbestanden aangepast. Het bestand is 39 regels. | Feit | hoog | Tests niet aanpassen om te slagen; bestanden onder ±400 regels |
| 2 | `architectuur.md` hoeft niet bij, want er is geen code veranderd. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | Geen persoonsgegevens, sleutels of wachtwoorden in de tekst. De twee beelden kon ik niet inzien. | Feit voor de tekst | midden | Geen persoonsgegevens |
| 4 | Cijfers zijn meestal gemarkeerd (GEZIEN, GOK, "nog niet zelf gezien"). De regelnummers (r746, r205, r767) en de uitleg bij punt 3 (de rek van de wang) kan ik niet nagaan. Punt 3 is wel als GOK gemarkeerd. | Feit (tekst) | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Het verslag noemt de Quaternius-modellen en makehuman, maar niet hun licentie. Voor de filmpjes is dat later nodig. | Vermoeden | laag | De licentie van elk model in de bron (CC0 of niet) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | "Neck (not placed)" geeft geen reden, op 4 van 6 figuren. Een koper snapt dan niet wat hij moet doen. | Een eigen NECK-zin in `kogel_reden`, zoals Olaf voorstelt. | klein |
| 2 | "Try a thicker spot" bij dikke ledematen stuurt de koper de verkeerde kant op. Dit gebeurde op 3 figuren. | De tip aanpassen, of de wang bij dikke ledematen dunner maken. | midden |
| 3 | Een figuur zonder schouder ziet er in elk filmpje of op elke plaat kapot uit. Bij "no watertight parts" probeert de add-on geen volgende plek. | Dan de volgende kandidaat van `kogel_schuif` proberen. | midden |
| 4 | Een heup op een dij van 61 mm wordt geweigerd, terwijl een koper die verwacht. | De grens 0,8 × bot iets ruimer maken. Lage prioriteit. | klein |
| 5 | Medieval krijgt knieën met wand onder 1 mm. Die breken bij het printen, ook al staat er een melding. | Bij zulke figuren in de filmpjes en op plaatjes geen knie tonen. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Het beeld `figuur-a-lijst-linkerschouder-weg.jpg` laten bekijken door een mens of agent met de Read-tool. `figuur-a-staand-pose.jpg` wordt in het verslag niet genoemd. Zet er één regel bij.
- Maak de tellingen in het verslag eenduidig: 8 of 9 gewrichten op het filmfiguur, en welke studio-commit erbij hoort.
- De drie add-on-voorstellen (NECK-zin, volgende kandidaat bij "no watertight parts", tip bij dikke ledematen) horen in een aparte wijziging. Pro 1.2.0 heeft nog geen akkoord van Daan en Iris. Keur die wijziging apart.
- Zet de licentie van de gebruikte modellen in het verslag.

---
Automatische keurder, model `claude-sonnet-5-5`, 19420 tokens in, 3478 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
