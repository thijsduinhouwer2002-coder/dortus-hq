# Keuring tenen-toets volume (blender-gewrichten), 28-11-2026, automatische keurder
Wat ik keurde: commit f893c6804 (Click Joints 0.1.3, #306, keuring #326 K1), alleen `producten/blender-gewrichten/e2e/toetsen_tenen.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De toets meet nu het volume van het figuur vóór het snijden (`vol0`) en van A en B erna. Hij faalt als A+B meer dan 6% kleiner is dan het figuur. | Feit (diff) | hoog | Dat past bij K1: een voxelvorm mag niet ongemerkt veel van de voet of het figuur wegeten. |
| 2 | De grens van 6% en de ondergrens van -0,5% staan er zonder gemeten waarde in de commit. Het is niet te zien of de huidige uitvoer ruim binnen de grens blijft. | Vermoeden | midden | Een groene e2e-run met de regel `VOLUME ... verlies x%` in het log, in 4.2, 5.2 en 5.3. |
| 3 | De log-regel gebruikt `lid.get('h_soort')`. Of `lid` op die plek in `main()` bestaat, is in de diff niet te zien. | Vermoeden | laag | Eén run van de toets zonder NameError. |
| 4 | De add-on zelf en de CHANGELOG zijn niet veranderd. De gebruiker merkt dus niets van deze commit, wat klopt bij een toetswijziging. | Feit | hoog | Niet van toepassing. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is strenger gemaakt en niet versoepeld, dus niet aangepast om te slagen. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | Het bestand blijft ruim onder ±400 regels (de diff voegt ±20 regels toe aan een kort script). | Feit | midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Voor een extra toetsregel is dat niet nodig. | Feit | midden | architectuur.md bijgewerkt |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens |
| 5 | `calc_volume` geeft op een open mesh een onbetrouwbaar getal. Of het testfiguur gesloten is, staat niet in de diff. De toets telt wel open randen (`open_`), maar gebruikt dat niet voor het volume. | Vermoeden | laag | Controle in het log dat `vol0` redelijk is, bijvoorbeeld vergeleken met een bekende maat. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing. Er is niets wat een speler of koper ziet of speelt, en ik kan niets bekijken.

## Deel C: is het goed genoeg?
Niet van toepassing: geen beeld, video, winkeltekst of spel dat een klant als eerste ziet. Er zijn geen cijfers gegeven en de blinde test geldt hier niet.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet het gemeten verlies uit de eerste groene run in de commit of in `ontwerp.md`. Dan is de grens van 6% onderbouwd (A2).
- Controleer in het log dat `lid` bestaat en dat `vol0` klopt. Laat de toets anders vooraf een waarschuwing geven als het figuur open randen heeft (A3, B5).

---
Automatische keurder, model `claude-sonnet-5-5`, 18832 tokens in, 2330 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
