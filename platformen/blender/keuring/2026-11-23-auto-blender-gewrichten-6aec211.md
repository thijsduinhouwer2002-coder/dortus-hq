# Keuring blender-gewrichten, Pro "mooier" (Labels Selected) en AI-figurenproef, 23-11-2026, automatische keurder
Wat ik keurde: commits 2250ff6..6aec211 (6aec2111e, 87ca7d4c5, de4d115fa), alleen de tekst van de wijziging
Akkoord: ja

## Deel A: doet het wat beloofd is?
Ik toets tegen de commitberichten en `architectuur.md`. In `ontwerp.md` staat nog geen akkoord voor deze Pro-wijzigingen.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De boog is in de stand Selected feller: vlak 38% in plaats van 22%, lijnen 4 px in plaats van 3 px en alpha 1,0. De code doet dit alleen bij een figuur in de stand SELECTED. | Feit (uit de diff) | hoog | n.v.t. |
| 2 | Het bolletje in de pil wordt rood voorbij de stop (`accent=ROOD if v["voorbij"]`). Of `ROOD` een RGB-drietal is zoals `KL`, en of `v["voorbij"]` bestaat, zie ik niet. De rode tekstcall suggereert dat het klopt. | Vermoeden | midden | Groene run van de gewone e2e, of een blik op `ROOD` en de sleutels van `v` in `scharnier_boog.py` |
| 3 | De nieuwe test `selected_ok` eist 1 label met de naam en geen kopregel (m1, m3), 0 labels bij niets gekozen (m2) en meer dan 200 rode vlakken (m4). Dat dekt moet 1 van de vorige keuring. De drempel 200 is een eigen gok, afgeleid van "17 vlakken voor". | Feit (eisen), vermoeden (drempel) | midden | Gemeten aantal rode vlakken in een run |
| 4 | `selected_ok` gebruikt `koppen`, `rood_vlakken()` en `KNIE`. Die staan niet in de diff; ze staan vast elders in `scherm_mooi.py`. Anders geeft `schiet` een NameError. | Vermoeden | laag | Groene run van stap "Standaardbeeld Labels Selected" |
| 5 | De uitslag meldt dat `MOOI SELECTED` alleen wordt gelogd. Dat de workflow op `OK` eist, staat in `architectuur.md` maar de workflow zit niet in deze wijziging. | Vermoeden | midden | `grep "MOOI SELECTED OK"` in de workflow, of rood vinkje bij opzettelijk FOUT |
| 6 | De AI-figurenproef beantwoordt de vraag "waar valt een gewricht weg". Het log komt overeen met de uitslagtabel voor spacetrooper1 en man_cap. Businessman kan niet geriggd worden (benen niet gevonden). | Feit (log) | hoog | n.v.t. |
| 7 | Oorzaak van de verkeerde tip bij de knie op een dik been ("Try a thicker spot", spacetrooper1) is zelf al als GOK gemarkeerd. Dat is eerlijk. | Vermoeden | laag | Waarden van `maten_neus` en `zaag_diepte` bij die knie |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt voor labels, schermtest en C4. Het noemt het verwijderen van `tekst_rand` en de losse `FIGUUR_X` niet, maar dat is geen kernzaak. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er zijn geen tests versoepeld. Er is een eis bij gekomen. | Feit (uit de diff) | hoog | Tests niet aangepast om te slagen |
| 3 | `tekst_rand` en `FIGUUR_X` zijn verwijderd als "dode code". Dat ze nergens meer worden aangeroepen of gelezen, zie ik niet. In een tekenhandler geeft dat pas bij het tekenen een fout. De comment in `labels.py` is wel meegenomen, wat wijst op een grep. | Vermoeden | midden | Geen kapotte code. Bevestigen: grep op `tekst_rand` en `FIGUUR_X` in `click_joints/` en `e2e/` |
| 4 | De uitslag zegt "5 van 6 heupen vallen weg". Het log laat 4 weggevallen heupen zien (2 spacetrooper, 2 man_cap) en businessman is niet geriggd, dus 4 van 4 of 6 van 6. | Feit (log) | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | De bewering "ook gedraaid met `CJ_HEUP_PCT=52`: zelfde uitslag" staat niet in het meegestuurde log. De licentie "MIT" van de set is niet als DERDEN gemarkeerd. | Vermoeden | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | In het log of de uitslag staan geen persoonsgegevens, sleutels of paden. De wijziging raakt alleen `betaald/` en `e2e/`, dus de gratis zip en `toets_zips` zijn niet geraakt. | Feit | hoog | Geen persoonsgegevens, twee builds |
| 7 | Bestandsgrootte: `scherm_mooi.py` is ruim onder de 400 regels. De lengte van `scharnier_boog.py` en `labels.py` zie ik niet. `scharnier_boog.py` komt in de diff tot ruim 300 regels. | Vermoeden | laag | Bestanden onder ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zag geen beelden en kan alleen de keuzes in de code beoordelen.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Standaard één label met naam en één felle boog is rustiger en leest sneller dan zes bogen. Dat lijkt een goede keuze. Of 38% groen op een licht model nog leesbaar is, moet iemand zien. | Daan bekijkt de schermen m1 en m3 op een licht en een donker model | klein |
| 2 | Voorbij de stop is het hele deel rood, de pil rood en het bolletje rood. Dat is drie keer hetzelfde signaal. De tekst "+N° past limit" helpt wie geen rood ziet. | Een vinkje of uitroepteken in het bolletje voor de kleurenblinde koper (eerder advies van Daan) | klein |
| 3 | Op AI-figuren houdt de koper met één klik vaak 1 tot 2 gewrichten over (spacetrooper1: alleen de nek). Heupen vallen bijna altijd weg. Dat voelt als "werkt niet". | Na Figure from rig een samenvatting "N van M geplaatst, hier handmatig" met per gemist gewricht een knop "place by hand" | midden |
| 4 | De tip "Try a thicker spot" bij een knie op een dik been stuurt de koper de verkeerde kant op. | Melding aanpassen of oorzaak eerst uitzoeken (de eigen GOK in de uitslag) | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Controleer met grep dat `tekst_rand` en `FIGUUR_X` echt nergens meer worden gebruikt, en wacht op de groene gewone e2e voor het uitbrengen (zie A2 en B3).
2. Bevestig dat de workflow op `MOOI SELECTED OK` eist en dat `koppen`, `rood_vlakken` en `KNIE` bestaan (A4, A5).
3. Corrigeer in `uitslag.md` "5 van 6 heupen" naar het gelogde aantal. Markeer de MIT-licentie als DERDEN en neem de run met `CJ_HEUP_PCT=52` op in het log.
4. Daan keurt het uiterlijk van de labels en de boog (Deel C 1 en 2) voor het in een winkelplaatje komt. Het huidige akkoord in `ontwerp.md` geldt voor 0.1.1 en 1.0.2, niet voor deze overlay.
5. Pak de verkeerde knie-tip aan en verzacht het wegvallen van heupen (Deel C 3 en 4).

---
Automatische keurder, model `claude-sonnet-5-5`, 32328 tokens in, 8203 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
