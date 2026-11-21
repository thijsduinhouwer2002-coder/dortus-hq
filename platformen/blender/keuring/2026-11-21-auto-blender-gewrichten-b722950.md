# Keuring gids 3 figuurschermen (scherm_gids_figuur.py), 21-11-2026, automatische keurder
Wat ik keurde: commit b72295061 (b41b76a..b722950), bestand producten/blender-gewrichten/e2e/scherm_gids_figuur.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De opdracht is een hulpscript voor twee plaatjes op de gidspagina (voor de knop, na de knop). Het script legt precies die twee vast en maakt van elk ook een uitsnede van de zijbalk. | Feit | hoog | Staat in de code: `schiet("f1-voor")` en `schiet("f2-na")`. |
| 2 | Of de plaatjes er goed uitzien, kan ik niet zien. Er is geen run en geen beeld meegestuurd. Dat is voor Daan, zoals de commit zegt. | Vermoeden | hoog | Een groene run met "GIDS KLAAR 0 FOUT" en de bijbehorende PNG's. |
| 3 | Het script leent veel uit `scherm_mens.py` en `scherm_basis.py`: M, A, staat, etalagepop, rustig, kijk, buig, zijbalk en meer. Die bestanden zitten niet in de diff, dus of die namen bestaan kan ik niet nagaan. | Vermoeden | midden | Een run in Blender 4.2 of 5.2, of een blik op die twee bestanden. |
| 4 | De regel `_src.replace(... register(stap ...))` haalt de eigen timer van `scherm_mens.py` weg. Als die tekst daar niet exact zo staat, doet de replace stil niets. Dan lopen twee scripts tegelijk. | Vermoeden | midden | Een controle of het script na de replace nog `register(stap` bevat, of een log met dubbele regels. |
| 5 | Het script roept de knop `figuur_uit_rig` en de module `betaald.figuur` aan. Een mislukking wordt wel gelogd ("GIDS FOUT") en geeft afsluitcode 1. | Feit | hoog | Staat in de code. De aanroepen zelf kon ik niet toetsen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het is een nieuw bestand van 116 regels. Er is geen test aangepast en de add-on zelf is niet veranderd. | Feit | hoog | Tests niet aangepast om te slagen. Bestanden onder ±400 regels. |
| 2 | `architectuur.md` is niet bijgewerkt. Het script is alleen een site-hulpmiddel en geen onderdeel van de add-on. | Feit | midden | architectuur.md bijgewerkt. Ik zie dit als kan, want de add-on veranderde niet. |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. De pop komt uit MakeHuman base.obj (CC0, volgens de docstring), dus geen AI-beeld. | Feit | hoog | Geen persoonsgegevens. Geen AI-beeld of -geluid op Steam. |
| 4 | Er staan geen cijfers voor kopers in. De "60 graden" staat alleen in een docstring. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK. |
| 5 | De plaatjes tonen betaalde knoppen (Pro) en zijn voor dortus.com. De regel dat extensions.blender.org alleen gratis functies toont, geldt hier dus niet. | Vermoeden | midden | ToS 6.2. Het gaat mis als deze plaatjes ook naar de extensions-pagina gaan. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Ik kan geen beeld zien, dus ik kan niets zeggen over leesbaarheid of uitstraling. Daan moet dat doen. | Daan keurt f1-voor en f2-na. Let op: staan de bogen per gewricht en de knie op 60 graden duidelijk in beeld, en is de zijbalk scherp genoeg? | klein |
| 2 | Op de poster kijkt de lezer in één oogopslag naar een voor-en-na. Het hangt van het beeld af of dat duidelijk is. Vermoeden. | Zet in het "na"-plaatje ook de samenvattingsregel van de add-on zichtbaar in het paneel. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Verwijder oude PNG's in de uitmap voor een run. Nu kan een oud bestand een nieuwe mislukking verbergen, want `schiet` kijkt alleen of het bestand bestaat.
- Laat het script stoppen als de replace van de timerregel niets verving (bijvoorbeeld met een `assert`).
- Noem bij de commit de run die dit script draaide, zodat Daan de beelden kan openen.
- Zet de aanname van de CC0-pop (MakeHuman base.obj) kort bij het plaatje op de site.

---
Automatische keurder, model `claude-sonnet-5-5`, 19449 tokens in, 3062 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
