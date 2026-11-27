# Keuring blender-gewrichten kaart #306 (M1 en K1 verwerkt), 28-11-2026, automatische keurder
Wat ik keurde: commit 8003e4bf5 (af966bb..8003e4b), alleen `producten/blender-gewrichten/KAART.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één alinea in de kaart: de status van #306 is bijgewerkt. Er zit geen code of toets in deze diff. | Feit | Hoog | Het diff-bestand zelf. |
| 2 | De kaart zegt dat K1 (de tenen-toets meet nu volume) gedaan is in f893c68, met e2e 46081457885 groen in 4.2.23, 5.2.3 en 5.3.0 en een verlies van 0,2 tot 1,0%. Die commit en die run zitten niet in deze diff. | Vermoeden | Midden | Het toetsbestand `e2e/toetsen_tenen.py` in f893c68 en het log van run 46081457885. |
| 3 | De kaart zegt "Daan ja (8, #326)". In het meegestuurde `ontwerp.md` staat geen akkoord voor dit werk (het laatste is 25 nov, Pro 1.2.8). Wat "8" betekent is onduidelijk. | Vermoeden | Midden | Het keuringsbestand van Daan voor #326. |
| 4 | De kaart houdt het samenvoegen terug tot na de plak van 1.2.9 (ma 30 nov). Dat sluit aan bij de eerdere afspraak. | Feit | Hoog | Niets nodig. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Bij de cijfers staat GEZIEN, ook bij het verlies van 0,2 tot 1,0%. Dat label kan ik hier niet nagaan. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 2 | In de kaart staat dat een toets aangepast is nadat 4.2.23 rood was ("te strenge aanname", ogen smelten samen met het hoofd). De reden is plausibel. Of de toets daardoor slapper werd, zie ik niet. K1 maakt hem juist strenger, want hij meet nu volume. | Vermoeden | Midden | Tests niet aangepast om te slagen |
| 3 | De kaart is klein (±40 regels) en bevat geen persoonsgegevens of sleutels. `architectuur.md` hoefde niet mee te veranderen, want er is geen code gewijzigd. | Feit | Hoog | Bestanden onder ±400 regels, geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niet van toepassing: dit is een interne kaart, de gebruiker ziet er niets van. | Niets. | Klein |

## Deel C: is het goed genoeg?
Niet van toepassing: er is geen beeld, spel, winkeltekst of site gewijzigd, dus geen blinde test en geen cijfers. Het akkoord hangt hier niet aan.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Schrijf bij "Daan ja (8, #326)" de datum en het bestand van de keuring, en wat "8" is.
- Schrijf bij "keurder liep opnieuw (moeten al gedekt door run 46072364194)" kort wat M1 precies was en welk bewijs het dekt.
- Zet bij de aangepaste toets voor 4.2.23 in één zin dat hij niet slapper is geworden. Dat kan met het aantal controles of de grens van voor en na.
- De code en toets van f893c68 zitten niet in deze diff. Ze moeten door de gewone keuring van de tak `claude/blender-306` voor ze samengevoegd worden.

---
Automatische keurder, model `claude-sonnet-5-5`, 19085 tokens in, 2570 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
