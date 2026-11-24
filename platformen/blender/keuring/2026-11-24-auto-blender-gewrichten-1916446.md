# Keuring blender-gewrichten, 24-11-2026, automatische keurder
Wat ik keurde: commit 1916446be (a2b6d73..1916446), bestand producten/blender-gewrichten/repo-click-joints/README.md
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één zin in de README van de loketrepo, onder het kopje over installeren. Hij vraagt om een korte review op Blender Extensions. De belofte van het product (kogel- en pengewricht, bereik in graden, passingkleur) verandert niet. | Feit | Hoog | Diff: één regel plus een lege regel erbij. |
| 2 | De zin noemt alleen de gratis add-on en verwijst niet naar de betaalde versie. Dat past bij de regel dat de gratis versie niet doorverwijst. | Feit | Hoog | Diff. |
| 3 | De link naar `extensions.blender.org/add-ons/click-joints/reviews/` kan ik niet openen. Of die pagina bestaat en of de naam van de add-on daar precies zo heet, weet ik dus niet. | Vermoeden | Midden | Een `curl` op de link die status 200 geeft, na de publicatie van 0.1.1. |
| 4 | Het commitbericht noemt ook een "review-zin site (patch)" en "keuring Daan". Alleen de README zit in de diff. Een wijziging aan de site of een keuring van Daan kan ik dus niet beoordelen. | Feit | Hoog | De diff van de site, of een Daan-keuring in een apart bestand. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen code of test aangepast, dus er is ook niets aangepast om een test te laten slagen. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Het bestand blijft ver onder de 400 regels. | Vermoeden | Midden | Bestandsgrootte; de volledige README is niet meegestuurd. |
| 3 | `architectuur.md` hoeft niet mee te veranderen, want het is een tekstwijziging zonder invloed op de werking. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of cijfers in de nieuwe regel. | Feit | Hoog | Geen persoonsgegevens; cijfers met GEZIEN/DERDEN/GOK |
| 5 | Er is geen AI-beeld of -geluid toegevoegd. | Feit | Hoog | Geen AI-beeld of -geluid op Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De zin is kort, vriendelijk en eist niets van de gebruiker. | Niets nodig. | klein |
| 2 | De vraag staat bij "installeren", dus voordat iemand de add-on heeft gebruikt. Hij zou beter werken na het stuk over wat er per versie veranderd is, of bij het kopje voor problemen melden. | De zin verplaatsen. | klein |
| 3 | Een review vraagt een account op Blender Extensions. Een korte hint dat dat nodig is, voorkomt een omweg. | Eén half zinnetje erbij. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- De reviewlink controleren met `curl` zodra 0.1.1 live staat (A3).
- De zin verplaatsen naar een plek na gebruik van de add-on (C2).
- Melden dat de sitewijziging en de keuring van Daan uit het commitbericht niet zijn meegestuurd, zodat ze apart gekeurd worden (A4).

---
Automatische keurder, model `claude-sonnet-5-5`, 17302 tokens in, 1932 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
