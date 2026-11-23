# Keuring Bison & Flex e2e-vensterverslag, 23-11-2026, automatische keurder
Wat ik keurde: commit 5528f80da (reeks ab5a168..b665b07), drie bestanden in `producten/jetbrains-bison-flex/e2e/`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Er is geen productcode gewijzigd, alleen de e2e-test. De belofte op de winkelpagina is daarom niet geraakt.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt `vensterVerslag` toe. Die schrijft in het log welk venster actief is, met naam en maat, en welke vensters zichtbaar zijn. Hij wordt aangeroepen na `waitForIndicators` en bij een mislukte structuurwissel. Dat past bij het doel uit de commit: uitzoeken of op de EAP 263 een dialoog boven het IDE-venster staat. | Feit | Hoog | n.v.t. |
| 2 | De test slaagt of faalt niet anders dan voorheen. De nieuwe aanroepen leggen niets vast en verwachten niets. | Feit | Hoog | n.v.t. |
| 3 | Ik kon de code niet bouwen of draaien. Dat hij compileert en dat `xdotool` op de runner bestaat, is dus een vermoeden. De `try/catch` zou een ontbrekende `xdotool` opvangen. | Vermoeden | Midden | Een groene e2e-run met de regels `DORTUS-E2E [..-start] actief venster` in het log. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Er zijn alleen logregels bijgekomen, geen verwachtingen weggehaald of verruimd. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De run-nummers in de commentaar zijn gewone CI-nummers. | Feit | Hoog | Geen persoonsgegevens |
| 3 | `architectuur.md` is niet bijgewerkt. Voor een extra logregel in een testhulpje is dat niet nodig. | Feit | Midden | architectuur.md bijgewerkt |
| 4 | De bestandslengte van `Gedeeld.kt`, `IdeTest.kt` en `StructuurEnZweven.kt` kon ik niet zien. De wijziging voegt maar 18 regels toe. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 5 | In de wijziging staan geen cijfers voor de winkel, geen spelerstekst en geen beeld of geluid. | Feit | Hoog | GEZIEN/DERDEN/GOK, Hats-tekst, AI-beeld |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Dit is alleen testlogging, de gebruiker ziet er niets van.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niet van toepassing: geen zichtbare of speelbare wijziging. | n.v.t. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Als er geen actief venster is, staat er `(null)` in het log. Dat kan `(geen)` worden.
- Het `ProcessBuilder`-proces wordt niet expliciet afgesloten. Dat is bij een kort log-hulpje geen probleem, maar `destroy()` in een `finally` is netter.
- Controleer bij de volgende run of het venster 1720x1134 in het log een dialoog blijkt. Haal het verslag weg of beperk het als het probleem is opgelost.

---
Automatische keurder, model `claude-sonnet-5-5`, 19678 tokens in, 1969 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
