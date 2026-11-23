# Keuring blender-gewrichten (script mooie voor/na-beelden), 23-11-2026, automatische keurder
Wat ik keurde: commit b94d5aefc, bestand `producten/blender-gewrichten/e2e/scherm_mooi.py` (nieuw, 198 regels)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De goedkeuring in `ontwerp.md` gaat over de add-on (gratis 0.1.1 en Pro 1.0.2). Deze wijziging is alleen een proefscript voor schermbeelden en raakt de add-on niet.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De add-on, het manifest en de zips zijn niet gewijzigd. Het ja van 16 nov blijft voor de gebruiker ongewijzigd. | Feit | Hoog | De bestandenlijst bevat alleen `e2e/scherm_mooi.py`. |
| 2 | Het commitbericht noemt "script en workflow", maar `pro-mooier.yml` staat niet bij de gewijzigde bestanden. De docstring verwijst er wel naar. | Vermoeden | Midden | Zit het bestand in de volgende commit, of is het wel meegekomen maar niet meegestuurd? `git show b94d5ae --stat` laat het zien. |
| 3 | De regel die de eigen `stap` van `scherm_mens.py` uitschakelt werkt met `str.replace` op een exacte tekst. Komt die tekst daar niet precies zo voor, dan gebeurt er stilletjes niets. Dan lopen twee timers tegelijk en zijn de beelden onbetrouwbaar. | Vermoeden | Midden | Het log van een echte run. Staat er maar één keer "Blender ..., betaalde zip ..." en komt "MOOI OK"? Dan gaat het goed. |
| 4 | Het script gebruikt sleutels uit `scherm_mens.py` (`S["A"]["actief"]`, `S["kijk"]`, `S["bouw"]`, `S["rustig"]`). Dat bestand is niet meegestuurd. | Vermoeden | Laag | Een groene run van het script, of die sleutels in `scherm_mens.py`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Het is een nieuw script dat alleen beelden maakt en regels logt. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Het bestand is 198 regels. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | Er staan geen persoonsgegevens of sleutels in. | Feit | Hoog | Geen persoonsgegevens |
| 4 | `architectuur.md` is niet bijgewerkt. Dat is hier niet nodig, want er verandert niets aan de add-on. | Feit | Midden | architectuur.md bijgewerkt |
| 5 | De figuur komt van MakeHuman en de beelden zijn echte uitvoer van de add-on, dus geen AI-beeld. | Vermoeden | Midden | Geen AI-beeld of -geluid op Steam (hier Superhive) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beelden, alleen het script. Dit zijn dus plannen, geen oordeel over het resultaat.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De vijf standen (heel, schoon, knie dichtbij, rood voorbij de stop, uit elkaar) dekken de verkoopmomenten goed. Het rode beeld is waarschijnlijk het sterkste. | Daan beoordeelt de echte beelden op de tak `schermen`. Pas dan gaan ze naar de winkel. | klein |
| 2 | Deze beelden tonen Pro-functies (scharnier, figuur). | Gebruik ze niet bij de gratis add-on op extensions.blender.org (ToS 6.2). Daar mogen alleen gratis functies in beeld. | klein |
| 3 | Als het kniebeeld niet leest, wordt het zwak: de camerastand en afstand 120 zijn gegokt. | Kijk bij de eerste run of het getal en de boog plat in beeld staan. Het log noemt het aantal getekende getallen. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of `pro-mooier.yml` echt is toegevoegd (Deel A, 2).
- Laat het script stoppen met een duidelijke melding als de `replace` op `scherm_mens.py` niets verving, bijvoorbeeld door `assert` op de vervangen tekst (Deel A, 3).
- Laat "MOOI OK" ook falen als er in alle beelden nul getallen getekend zijn. Dan blijkt op de nieuwe code dat de verbetering werkt, en op de oude code dat hij ontbrak (Deel A, 3).
- Daan keurt de beelden zelf voordat ze in de winkel komen (Deel C).

---
Automatische keurder, model `claude-sonnet-5-5`, 20808 tokens in, 2755 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
