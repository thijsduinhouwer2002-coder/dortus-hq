# Keuring blender-gewrichten (rig: volgende plek na overlap), 23-11-2026, automatische keurder
Wat ik keurde: commit da1c13465 (rig.py, e2e/meet_rig.py, e2e/meet_tabel.py)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging in `rig.py` is klein: bij het bericht "overlap before they move" probeert "Figure from rig" nu de volgende plek, net als bij "too close" en "no watertight parts". | Feit (diff) | hoog | n.v.t. |
| 2 | De tekst "overlap before they move" moet letterlijk zo uit de add-on komen (kleine letters, na `laag`). Dat kan ik hier niet nakijken. | Vermoeden | midden | `grep -i "overlap before they move"` in `gewricht.py` of `betaald/` met precies deze spelling. |
| 3 | De opmerking zegt dat de mesh na zo'n snede onveranderd is. Als die niet klopt, werkt de volgende plek op een half bewerkte mesh. | Vermoeden | midden | Een run op 4.2 met een scharniersnede die overlap geeft, waarna de mesh vóór en na de poging gelijk is (puntenhash). |
| 4 | Het commitbericht belooft dat het in 4.2 beter wordt. Er zit geen uitslag bij, alleen het script `meet_tabel.py` om die te maken. | Vermoeden | midden | De tabel van `meet_tabel.py` met twee runs (voor en na) laat meer gewrichten of minder slechte sneden zien op 4.2.23. |
| 5 | De opdracht die ik zie (`ontwerp.md`) gaat over de gratis 0.1.1 en Pro 1.0.2. Deze Pro-wijziging (opmerking "1.2.3") staat daar niet in. Het ontbrekende deel is afgekapt. | Vermoeden | laag | Een opdracht of bericht voor 1.2.3 in het afgekapte deel of in `berichten/`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen bestaande test aangepast om te slagen. | Feit (diff) | hoog | Tests niet aanpassen |
| 2 | Er is geen test voor de nieuwe voorwaarde. De meting op de testset moet dat dekken. | Feit | midden | Toetsbaar werk |
| 3 | `rig.py` is minstens 758 regels, dus ver boven ±400. De wijziging voegt maar twee regels toe. | Feit (regelnummer in diff) | hoog | Bestanden onder ±400 regels (bestaand probleem, geen nieuw) |
| 4 | `architectuur.md` is niet bijgewerkt. Dat is alleen een gemis als daar het doorgaan naar de volgende plek beschreven staat. Die tekst is afgekapt. | Vermoeden | laag | architectuur.md bijgewerkt |
| 5 | `bouw_meshy` is alleen voor onderzoek en zit niet in de testset, want de licentie van de Meshy-set is niet nagelezen. Dat is eerlijk gemeld en past bij de regels. | Feit | hoog | Geen figuren zonder duidelijke licentie in de testset |
| 6 | Ik zie geen persoonsgegevens, sleutels of AI-beeld in de wijziging. | Feit | hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Als de volgende plek werkt, ziet de gebruiker minder "geen gewricht gemaakt" op figuren waar de eerste plek overlap gaf. Zien kan ik het niet. | Een voor-en-nameting op de Meshy-figuren in de tabel laten zien. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen.

Kan:
- Controleer dat de tekst "overlap before they move" precies zo in de add-on staat, bijvoorbeeld met een test op die tekst. Anders werkt de nieuwe voorwaarde niet, ook al lijkt de code goed.
- `meet_tabel.py` crasht als `knop_s` ontbreekt in een uitslag (`.0f` op `None`). Vang dat af.
- `bouw_meshy` gebruikt `os.environ["CJ_GLB"]` zonder melding als die variabele ontbreekt. Het laadt ook `proef_meshy_rig.py` met een `replace("\nmain()\n", ...)`, en dat breekt zodra die regel anders staat. Geef een duidelijke foutmelding.
- Leg de uitslag van de voor-en-nameting vast bij de commit, zodat zichtbaar is dat de wijziging iets oplost.
- Splits `rig.py` ooit onder ±400 regels.

---
Automatische keurder, model `claude-sonnet-5-5`, 19478 tokens in, 2675 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
