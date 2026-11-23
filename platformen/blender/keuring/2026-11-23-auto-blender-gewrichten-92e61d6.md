# Keuring blender-gewrichten, 23-11-2026 11:54 NL, automatische keurder
Wat ik keurde: commits 884ccce..92e61d6 (92e61d603 "Pro mooier"), bestanden figuur_teken.py, scharnier_boog.py en e2e/scherm_mooi.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
Het akkoord in ontwerp.md gaat over gratis 0.1.1 en Pro 1.0.2. Deze wijziging is een uiterlijke verbetering aan Pro en heeft geen eigen opdrachttekst. Ik toets daarom aan de commitbeschrijving.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | In de stand Selected is de boog nu heel (1,0), bij alle gewrichten samen blijft hij 0,7. Dat staat zo in `figuur_x()` en wordt in `_teken_een` en `scharnier_getallen` gebruikt. | Feit | Hoog | Het diff zelf. |
| 2 | `kogel_vorm` roept `figuur_x()` aan zonder context, de andere twee plekken geven wel een context mee. Als `labels.stand(None)` niet netjes op `bpy.context` terugvalt, is de kogelboog 0,7 en de scharnierboog 1,0, of het geeft een fout. | Vermoeden | Midden | De code van `labels.stand` of een run met stand Selected. Daar vraagt de e2e-run "fout_kogel" in het log om. |
| 3 | Het label wordt nu na de pose-lijn getekend, zodat de lijn er niet doorheen loopt. De variabelen `naam`, `q` en `getal` worden pas op functieniveau gebruikt. Of ze altijd bestaan, zie ik niet. | Vermoeden | Laag | Een run met een gewricht zonder label of zonder pose-lijn. Geen NameError betekent dat het klopt. |
| 4 | Het beeld van het paneel Figure joints (m7) is nieuw. Ik kan niet zien of de uitsnede de lijst echt toont. | Vermoeden | Laag | Het beeld `m7-paneel.png` bekijken met de Read-tool. |
| 5 | `klap_hoofdpaneel` komt uit `scherm_basis.py`, dat in deze commit niet verandert. Het moet dus al bestaan. | Vermoeden | Midden | De MOOI-regel "hoofdpaneel ingeklapt" in het log. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is strenger geworden, niet losser: een assert op de vervangregel en de eis dat er minstens één getal is getekend. | Feit | Hoog | Tests niet aangepast om te slagen: in orde. |
| 2 | Er is geen aparte toets voor `figuur_x` (Selected tegenover All). Alleen het beeldscript test het, en dat kijkt nauwelijks naar de grootte van de boog. | Feit | Midden | Toets bij elke gedragsverandering: kan. |
| 3 | `architectuur.md` is niet bijgewerkt voor de nieuwe grootte van de boog in Selected. Het gaat om een kleine verandering. | Feit | Midden | architectuur.md bijgewerkt: kan. |
| 4 | `scharnier_boog.py` komt boven de 300 regels uit en wordt langer. De totale lengte zie ik niet. | Vermoeden | Laag | Bestanden onder ±400 regels: controleer met `wc -l`. |
| 5 | Geen persoonsgegevens, sleutels of AI-beeld of -geluid in de wijziging. | Feit | Hoog | Regels in orde. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beelden, dus dit zijn vermoedens uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een hele boog bij één gewricht en het label bovenop de pose-lijn leest waarschijnlijk rustiger. | Bekijk m7 en een beeld in Selected met de Read-tool voordat je het in een winkelplaatje gebruikt. | Klein |
| 2 | Een hele boog kan bij een knie het lijf of het paneel overlappen. Dat zie ik niet. | Een schermafbeelding bij een gewricht dicht bij de rand van het beeld. | Klein |
| 3 | Het label als pil met een bolletje in de passingkleur is een duidelijke stijlkeuze. Het kleurverschil tussen pil en bolletje helpt wie geen groen ziet niet. | Voeg een klein vinkje of icoon toe naast het kleurbolletje. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Geef bij de aanroep in `kogel_vorm` ook de context mee (of check `labels.stand(None)`), zodat kogel en scharnier dezelfde grootte krijgen in stand Selected (Deel A 2).
- Controleer dat `naam`, `q` en `getal` altijd bestaan in `_teken_een` voor het label (Deel A 3).
- Kijk met de Read-tool naar `m7-paneel.png` en een beeld in Selected (Deel A 4, Deel C 1 en 2).
- Voeg een kleine toets toe voor `figuur_x` in Selected en All en werk `architectuur.md` bij (Deel B 2 en 3).

---
Automatische keurder, model `claude-sonnet-5-5`, 20997 tokens in, 4657 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
