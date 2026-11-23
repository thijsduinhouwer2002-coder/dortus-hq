# Keuring Verifier met EAP-build, 23-11-2026, automatische keurder
Wat ik keurde: commit 4b1ee69f9, bestand `producten/jetbrains-bison-flex/build.gradle.kts` (uit bereik 5370d78..7029107)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging raakt alleen de build. De opdracht in `ontwerp.md` (de plugin zelf) verandert niet, dus ik toets hier of de commit doet wat de titel zegt.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|------------------------------|--------------------------------------|
| 1 | Het filter laat nu ook `IU/263.8311.30` door (`":" in it \|\| "/" in it`). De splitsing op `[:/]` met limit 2 geeft dan soort `IU` en versie `263.8311.30`. De oude vorm `IU:2026.3` werkt hierdoor nog steeds. | Feit (uit de diff) | Hoog | Een handmatige Verifier-run met `-PverifierExtra=IU/263.8311.30` die de build toont in het log. |
| 2 | Of Gradle de EAP-build `IU/263.8311.30` echt vindt en downloadt, hangt af van de repository-instellingen in de rest van het bestand. Die zie ik niet. | Vermoeden | Midden | Een groene run van de handmatige workflow met die waarde, of een foutmelding over een niet gevonden build. |
| 3 | De opmerking dat er voor een EAP-build "geen licentie nodig is" is een bewering in een commentaar. Uit de tekst kan ik dat niet bevestigen. | Vermoeden | Midden | Het Verifier-log van een EAP-run, zonder licentiefout. |
| 4 | Een waarde zonder versie, zoals `IU/`, geeft een lege versie. Dat is een randgeval bij een handmatige invoer. | Feit | Hoog | Een run met zo'n waarde. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | Er is geen test aangepast en geen test verwijderd. Alleen `build.gradle.kts` is gewijzigd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand blijft naar schatting ruim onder de 400 regels (de wijziging is +4/-2 rond regel 77). De totale lengte zie ik niet. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` staat niet in de wijziging. Wat ik ervan zie noemt de Verifier-opzet niet, en alleen het begin van het bestand is meegestuurd. Het is een build-hulpmiddel, geen onderdeel van de plugin, dus bijwerken is hier niet nodig. | Vermoeden | Midden | architectuur.md bijgewerkt |
| 4 | De wijziging bevat geen persoonsgegevens, sleutels of cijfers, en er is geen spelerstekst of beeld. De changelog hoeft niet mee: er verandert niets voor de gebruiker. | Feit | Hoog | Geen persoonsgegevens, cijfers, changelog |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing: de wijziging is een build-instelling, er is niets te zien of te spelen.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|-----------|---------------------|-----------------------------|
| 1 | Geen gebruikerszichtbare wijziging. | Niet van toepassing. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Draai de handmatige workflow één keer met `IU/263.8311.30` en bewaar de uitslag. Dan is deel A, punt 2 en 3, bevestigd.
- Laat een waarde zonder versie (`IU/`) een duidelijke foutmelding geven, in plaats van een lege versie.
- Zet in de skill `actions` of het workflow-bestand hoe `-PverifierExtra` met `/` wordt ingevuld.

---
Automatische keurder, model `claude-sonnet-5-5`, 18412 tokens in, 2130 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
