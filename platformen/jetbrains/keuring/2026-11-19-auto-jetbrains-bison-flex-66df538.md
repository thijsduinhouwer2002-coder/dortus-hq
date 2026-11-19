# Keuring Bison & Flex e2e-scheiding en CLion-scherm, 19-11-2026, automatische keurder
Wat ik keurde: commit 66df5380 (48b9ea3..66df538), `architectuur.md`, `ClionTest.kt`, `Gedeeld.kt` in `producten/jetbrains-bison-flex/`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen testcode en documentatie. De belofte in `ontwerp.md` (functies, Pro-grens, winkeltekst) verandert niet. | Feit | hoog | Geen bestand onder `src/main` in de lijst gewijzigde bestanden. |
| 2 | De scheiding van 0,33 in `workspace.xml` geldt nu alleen nog voor IDEA, via `voorvoegsel.startsWith("bisonflex-")`. De kleurenpagina zit in `IdeTest`, dus die blijft vast. | Vermoeden | midden | Een e2e-run waarin `IdeTest` `winkelproject` met een voorvoegsel `bisonflex-...` aanroept en de kleurenpagina gelijk blijft. |
| 3 | In `ClionTest` is `schermStil(..., pogingen = 15)` terug naar `scherm(...)`. Het commentaar noemde run 44490202883, waar de kleuring van `calc.y` nog niet klaar was. Dat risico op een half gekleurd CLion-plaatje kan terugkomen. | Vermoeden | midden | Een paar CLion-runs op rij waarin `clion-*-calc-y.png` volledig gekleurd is (beeldvergelijking met 0 groot). |
| 4 | De commit noemt "twee opdrachten (R4)". In de diff zie ik de scheiding voor IDEA en het terugzetten van het CLion-scherm. Een derde of vierde onderdeel zie ik niet. | Vermoeden | laag | Het verslag van de keuring R4 of de opdrachttekst, om te zien welke twee opdrachten bedoeld zijn. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen assertie weggehaald of verzwakt. De `assertTrue(meter == null, ...)` blijft staan. Wat verdwijnt is alleen het wachten tot het beeld stilstaat bij een schermafbeelding. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt en beschrijft dat de scheiding alleen voor IDEA geldt, met de twee run-nummers als GEZIEN. Dat de runs bestaan en dit laten zien kan ik uit de tekst niet nagaan. | Feit (bijgewerkt), vermoeden (juistheid van de runs) | midden | architectuur.md bijgewerkt, cijfers met GEZIEN/DERDEN/GOK |
| 3 | De bewering "zonder dit bestand bleef CLion gelijk" staat in de code, maar in de diff staat geen run die dat bewijst. | Vermoeden | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 5 | De regelgrootte van `Gedeeld.kt` en `ClionTest.kt` is uit de diff niet te zien. De alinea in `architectuur.md` is wel één zeer lange regel. | Vermoeden | laag | Bestanden onder ±400 regels |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Kijk na of `IdeTest` echt `winkelproject("bisonflex-...")` gebruikt. De koppeling aan een tekstvoorvoegsel breekt stil als iemand de naam wijzigt. Een expliciete parameter ("metSplitter") is robuuster.
- Houd de eerstvolgende CLion-runs in de gaten op een half gekleurd `calc.y`. Komt dat terug, zet dan `schermStil` alleen daar terug.
- Leg vast welke twee opdrachten R4 bedoelt, of zet in de commit wat er is gedaan.
- Splits de lange alinea in `architectuur.md` in kortere stukken.

---
Automatische keurder, model `claude-sonnet-5-5`, 23064 tokens in, 2700 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
