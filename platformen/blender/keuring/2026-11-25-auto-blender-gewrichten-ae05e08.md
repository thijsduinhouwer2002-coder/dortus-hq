# Keuring blender-gewrichten, 25-11-2026, automatische keurder
Wat ik keurde: commits c4f14e5..ae05e08 (ae05e08c2, Click Joints Pro 1.2.9, issue 70): architectuur.md, e2e/scherm_rig.py en e2e/test_betaald.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
Deze wijziging bevat alleen tests, een schermopname en documentatie. De add-on-code voor issue 70 (meld.py, paneel.py) zit niet in dit bereik en heb ik niet gezien.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De toets eist dat de gratis build alleen "Blender Extensions" als beoordelingslink heeft, en de betaalde build "Superhive" en "Gumroad". Dat past bij wat architectuur.md beschrijft. | Feit | Hoog | Een groene e2e-run met deze stappen in het log. |
| 2 | De toets "betaald uit: winkellinks teruggezet" slaagt ook als de betaalde meld-module niet geladen is (`bm is None`). Hij bewijst dan niets over het terugzetten. | Feit (uit de code) | Midden | Een run waarin de betaalde module wel geladen was vóór het uitzetten, of een aparte eis dat `bm` bestaat. |
| 3 | Schermbeeld 16a toetst alleen dat de rig gevonden is en dat de uitsnede gelukt is. Of het vak "Rig found" echt bovenaan staat, volgt niet uit de tekst. | Vermoeden | Midden | Het bestand `16a-rig-boven-paneel.png` bekijken met Read. |
| 4 | Er is geen Akkoord van Daan voor 1.2.9 in ontwerp.md. Het laatste ja geldt voor 1.2.8. Voor deze testwijziging is dat geen blokkade, voor uitbrengen van 1.2.9 wel. | Feit | Hoog | Een regel "Akkoord: ja ... Pro 1.2.9" van Daan. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn alleen toetsen bijgekomen. Er is geen toets versoepeld of weggehaald. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | architectuur.md is bijgewerkt voor de vier lijsten `BOVEN`, `STAP2`, `STAP2_KEUS` en `STAP3` en voor de beoordelingsregel. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | `bouw()` is gesplitst in `bouw()` en `bouw_figuur()`. In de diff zie ik niet of de rest van de oude functie nog een lokale variabele (zoals `mesh`) gebruikt. Dan zou het schermscript met een NameError stoppen. | Vermoeden | Laag | Een groene run van het schermscript bevestigt dit. |
| 4 | De regel `RIG BOVEN FOUT` komt alleen in het log. Of een andere toets of de workflow erop faalt, zie ik niet. | Vermoeden | Midden | Een workflow of toets die op `RIG BOVEN OK` eist. |
| 5 | De bestandsgrootte van scherm_rig.py is niet te zien, dus de grens van ±400 regels kan ik niet controleren. | Vermoeden | Laag | `wc -l` op het bestand. |
| 6 | Er staan geen persoonsgegevens, sleutels of cijfers zonder label in de wijziging. De regels over Hats en AI-beeld zijn hier niet van toepassing. | Feit | Hoog | Persoonsgegevens, cijfers, Hats, AI-beeld |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De regel "Happy with it? Leave a rating:" blijft volgens architectuur.md staan zolang er ergens in de scène een Good fit is. Je kunt hem niet wegklikken. Dat kan na 30 seconden als zeuren voelen. Dit is een vermoeden uit de beschrijving. | Een knop "Don't ask again" of de regel maar één keer per sessie tonen. | Klein |
| 2 | De gratis CHANGELOG ("Unreleased") noemt de beoordelingsregel niet. De gebruiker leest dus niet dat er iets bij is gekomen. | Een regel erbij in de Added-sectie, vanuit de gebruiker geschreven. | Klein |

## Deel C: is het goed genoeg?
Er zijn geen beelden of spelsessies te zien, alleen testcode. Ik geef daarom geen cijfers.

| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | n.v.t. | Niet te beoordelen uit tekst. Dit is geen klantbeeld. |
| Zou ik het zelf kopen of bekijken op basis van dit? | n.v.t. | Idem. |
| Zou Thijs er trots op zijn? | n.v.t. | Idem. Daan keurt het schermbeeld 16a. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Maak de toets "betaald uit: winkellinks teruggezet" strenger, zodat hij niet vanzelf slaagt als `bm` ontbreekt (A2).
- Controleer in de run dat `bouw_figuur()` na de splitsing nog werkt, en laat Daan het bestand `16a-rig-boven-paneel.png` bekijken (A3, B3).
- Zet de beoordelingsregel in de CHANGELOG en overweeg een manier om hem te verbergen (C1, C2).
- Zonder een groene e2e-run (Blender 4.2.23, 5.2.3 en 5.3.0) is deze keuring niet bevestigd. Daan moet nog akkoord geven op 1.2.9 voordat het uitkomt (A4).

---
Automatische keurder, model `claude-sonnet-5-5`, 23529 tokens in, 4549 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
