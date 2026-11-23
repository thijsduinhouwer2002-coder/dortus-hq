# Keuring blender-gewrichten Pro mooier overlay, 23-11-2026, automatische keurder
Wat ik keurde: commits 5bbee65..4a4f971 (alleen de tekst van de wijziging, niets gedraaid of gezien)
Akkoord: ja

## Deel A: doet het wat beloofd is?
Toetsmaat: de commitberichten en `architectuur.md`. Een apart ontwerp voor deze wijziging zag ik niet.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De schakelaar Labels (Selected, All, None, standaard Selected) staat in het paneel Figure joints en in `labels.py`. `toon()` regelt de drie standen. Een los gewricht tekent altijd. | Feit (code) | hoog | De toets `mooier` in `toetsen_figuur.py` dekt alle vier de gevallen. Een groene run bevestigt het. |
| 2 | Het label is een pil met bolletje, naam en onderlijn. In Selected valt de kopregel weg en staat de naam in het label. | Feit (code), uiterlijk vermoeden | midden | `m1-heel` en `m3-knie` uit `scherm_mooi.py`, bekeken door Daan of Iris. |
| 3 | Voorbij de stop wordt bij een figuur het hele deel B rood. Het eigen vak staat in `cj_rood_deel`, en `_terug` zet het terug. De volgorde (eerst het hele deel, dan de rakende vlakken) klopt met hoe `pose` ze vult. | Feit (code) | midden | De toets "voorbij de stop: hele deel B rood" en "binnen de stop: alle vakken weer zoals eerst" in een groene run. |
| 4 | In Selected is de boog feller (vlak 38%, lijn 4 px) en het bolletje is rood voorbij de stop. | Feit (code) | hoog | Beeld `m4-rood`. |
| 5 | Een nieuwe toets in de gewone e2e eist `MOOI SELECTED OK`: 1 label met naam, geen kopregel, 0 labels zonder keuze, rode vlakken voorbij de stop. De workflow zelf zit niet in deze diff, dus of die regel de run laat falen kan ik niet zien. | Vermoeden | laag | De workflowstap moet de regel `MOOI SELECTED OK` eisen en bij `FOUT` rood worden. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De schermtests 15, 16, 17 en 19 zetten nu zelf de stand All. De reden staat erbij: ze toetsen de plek van alle getallen. De standaardstand heeft een eigen nieuwe test. De eisen zijn dus niet verzwakt. | Feit | hoog | Tests niet aanpassen om te slagen: in orde |
| 2 | `architectuur.md` is bijgewerkt voor `labels.py`, de schakelaar, `kleur_deel`, `figuur_x` en de toetsen. | Feit | hoog | architectuur.md bijgewerkt: in orde |
| 3 | `labels.py` is 163 regels en `scherm_mooi.py` 235. De totale lengte van `scharnier_boog.py`, `figuur_teken.py` en `scharnier_beweeg.py` zie ik niet. | Vermoeden | laag | Bestanden onder ±400 regels: `wc -l` op die drie bestanden |
| 4 | Alle nieuwe code staat onder `betaald/`, dus de gratis zip blijft gelijk. De gratis CHANGELOG hoeft niet te veranderen. | Feit (paden) | midden | Gratis zip zonder betaalde delen: `toets_zips.py` groen |
| 5 | Er zijn geen persoonsgegevens, sleutels, AI-beeld of -geluid en geen cijfers zonder bron gevonden. | Feit | hoog | Persoonsgegevens, cijfers en AI-regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beelden, dus dit is alles vermoeden.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Standaard Selected betekent dat direct na "Figure from rig" nog niets in beeld staat tot je een deel kiest. De eerste indruk (en het winkelplaatje) kan leeg lijken. | Kort na het maken van een figuur even All tonen, of een hint in het paneel ("Select a joint to see its range"). | klein |
| 2 | Het hele deel rood voorbij de stop is duidelijker dan een strook. Op een groot figuur kan het wel schreeuwerig zijn. | Een iets doorzichtiger rood, of alleen een gloed. Eerst naar `m4-rood` kijken. | klein |
| 3 | De pil met bolletje en onderlijn lijkt rustiger dan losse getallen. Of hij leesbaar is op een licht model zie ik niet. | Daan of Iris kijkt naar `m1`, `m3` en `m5`. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. `kleur_deel` slaat de materiaalindex van elk vlak als lijst op het object (`idx.tolist()`). Bij een deel van 200K vlakken is dat zwaar bij elke schuifbeweging voorbij de stop en maakt het .blend groter. Dat is een vermoeden. Meet de tijd van `pose` voorbij de stop op het grote figuur, of bewaar het in een numpy-bestand of in het geheugen.
2. De eis in `selected_ok` telt `len(cj_rood_deel) // 2`. Dat is de helft van het aantal vlakken, geen echte telling. De drempel van 200 klopt dus alleen losjes. Tel het echt of noem het anders.
3. `figuur_teken._teken_een` geeft nu `None` terug als het label niet getoond wordt. Controleer dat elke aanroeper dat aankan.
4. Controleer of `scharnier_boog.herteken` bestaat, en of een nieuw gewricht op een deel dat nog rood staat niet rood blijft. Pose gaat meestal terug naar 0 voor de export. Een groene run laat dat zien.
5. Controleer de workflow `pro-mooier.yml` en de e2e-stap: laat die echt falen op `MOOI SELECTED FOUT`?

---
Automatische keurder, model `claude-sonnet-5-5`, 44570 tokens in, 6092 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
