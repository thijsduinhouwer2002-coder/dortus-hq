# Keuring blender-gewrichten winkelschermbeelden ronde 5, 24-11-2026, automatische keurder
Wat ik keurde: commit 45bba0d5a (db725d6..45bba0d), bestand producten/blender-gewrichten/e2e/scherm_winkel.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht in de commit: w2 op 1,25x, zodat Export STL/3MF in beeld staat. Alleen de tekst van de wijziging is bekeken, geen beeld.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De code zet `ui_scale` voor w2 op 1,25 (instelbaar via `CJ_WINKEL_SCHAAL_W2`) en voor w3 terug op `SCHAAL` (1,5). Dat past bij de beschrijving. | Feit | Hoog | Het diff zelf. |
| 2 | Of Folder, Export STL/3MF en de exportknop nu echt in beeld staan, staat niet in de tekst. De opmerking noemt run 45447006294 als bewijs van het oude probleem. Over de nieuwe stand zegt hij niets. | Vermoeden | Midden | De nieuwe w2-opname met de Read-tool bekijken: staan de exportknoppen onder de rand of erin? |
| 3 | `schaal(SCHAAL_W2)` staat als eerste in de lambda, vóór `klap_hoofdpaneel()` en `kijk_figuur()`. Of Blender na de schaalwissel eerst opnieuw tekent voordat `zijbalk_omlaag` scrolt, is niet te zien. | Vermoeden | Laag | Een groene run met w2 volledig tot de exportknop. |
| 4 | De bovenkant van het script is niet meegestuurd. Daardoor is niet te zien of `ui_scale` vóór w1 al op `SCHAAL` staat. Anders zou w1 op de Blender-standaard staan. | Vermoeden | Laag | De regels bovenin `scherm_winkel.py` of het w1-plaatje. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Het is een hulpscript voor schermbeelden, en er zijn geen beweringen of drempels veranderd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | De wijziging is ongeveer 10 regels. Het bestand zelf is niet zichtbaar, maar bijna zeker ruim onder ±400 regels. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Dat is hier niet nodig, want er verandert geen onderdeel of gedrag van de add-on. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. Er zijn geen AI-beelden of -geluiden en geen cijfers zonder label. De opmerking noemt een run met "GEZIEN". Die claim kan ik niet nagaan. | Feit | Hoog | Geen persoonsgegevens, cijfers met label |
| 5 | w3 toont de testkaart, een betaalde functie. Dat is goed voor Superhive. Voor extensions.blender.org mogen alleen gratis functies in beeld (ToS 6.2). Of dit beeld daar wordt gebruikt, staat niet in de wijziging. | Vermoeden | Midden | Winkelbeelden tonen op extensions.blender.org alleen gratis functies |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er zijn geen beelden meegestuurd en ik kan niets zien. Dit moet Daan beoordelen.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De schaal verschilt nu per plaatje: w1 en w3 op 1,5x en w2 op 1,25x. In een winkelreeks kan dat er ongelijk uitzien, bijvoorbeeld met tekst van een andere grootte. Dat is een vermoeden, want ik zie de beelden niet. | De drie plaatjes naast elkaar bekijken. Past de tekstgrootte, dan is het goed. Anders in alle drie 1,25x gebruiken, als de testkaart daar ook past. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Bekijk het nieuwe w2-plaatje met de Read-tool en bevestig dat Folder, STL/3MF en Export in beeld staan. Dat is de enige belofte van deze commit en ik kan haar uit de tekst niet bevestigen.
- Controleer dat de schaal vóór w1 op `SCHAAL` staat, zodat w1 niet op de Blender-standaard blijft.
- Laat Daan de drie plaatjes op eenheid in grootte beoordelen.
- Gebruik het testkaartplaatje (w3) niet op extensions.blender.org, want dat toont een betaalde functie.

---
Automatische keurder, model `claude-sonnet-5-5`, 18042 tokens in, 2532 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
