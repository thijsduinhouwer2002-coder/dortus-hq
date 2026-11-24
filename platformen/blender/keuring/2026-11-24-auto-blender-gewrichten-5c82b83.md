# Keuring blender-gewrichten gids 5 (downloaded STL), 24-11-2026, automatische keurder
Wat ik keurde: commits 7cd90ef..5c82b83 (5c82b83f1), bestanden `e2e/gids_stl_bron.py` en `e2e/scherm_gids_stl.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De add-on zelf is niet veranderd. Deze wijziging maakt alleen de schermen voor gidspagina 5. Ik toets daarom of de scripts doen wat de kopregel zegt: echte Knight CC0, gewricht in de linkerelleboog, drie plaatjes.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De add-on, het manifest en de zip zijn niet aangeraakt. De akkoorden uit `ontwerp.md` blijven dus gelden. | Feit (alleen twee e2e-bestanden in de diff) | Hoog | n.v.t. |
| 2 | Het gewricht komt nu langs de bovenarm (cursor gedraaid met `rotation_difference`, as uit het bot). Dat is logischer dan het oude vaste middel van het figuur. De logica klopt in de tekst. | Vermoeden (niet gedraaid) | Midden | Het logboek "GIDS plaats: ... passing=groen" en plaatje s2-joint van de run |
| 3 | De opmerking "GEZIEN 24 nov, 5.3.0: wand 0,93 mm oranje op -6 mm, 1,55 mm groen op -12 mm" staat alleen in een commentaar. Ik zie geen log of beeld ervan. | Vermoeden | Midden | Het run-log van de schermen met `wand=` en `passing=` |
| 4 | `gids_stl_bron.py` neemt aan dat de botten "UpperArm.L" en "UpperLeg.L" heten (vervanging "Lower" door "Upper"). Heten ze anders in Knight.blend, dan stopt het script met een KeyError. | Vermoeden | Laag | Eén run van het script op `Knight.blend` |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het vaste pad `/home/claude/g5` en de losse glb zijn weg. De bron wijst nu naar een blend in de repo. Dat is beter herhaalbaar. | Feit | Hoog | Herhaalbare tests |
| 2 | Het bestand `commercie/filmpjes/monsters/blends/Knight.blend` zit niet in deze diff. De CC0-claim (Quaternius, Ultimate Monsters) komt alleen uit het docstring. | Vermoeden (DERDEN, niet nagekeken) | Midden | Testfiguren zelf gemaakt of CC0 (ontwerp eis 1). Bevestigen door de licentie bij het bronbestand te zoeken. |
| 3 | Beide bestanden zijn ruim onder 400 regels. Er staan geen persoonsgegevens, sleutels of machinepaden in. De export gaat naar een tijdelijke map zodat er geen pad in beeld staat. | Feit | Hoog | Bestandsgrootte, geen persoonsgegevens |
| 4 | De commitregel noemt "keuring Daan (Claude)", maar die keuring zit niet in de diff. Of de bouwer zichzelf als keurder noemt, kan ik niet zien. | Vermoeden | Laag | Het bijbehorende keuringsbestand van Daan lezen |
| 5 | `gids_stl_bron.py` heeft nu een `-- <map>` argument. Wat het script aanroept (workflow of handmatig) staat niet in de diff. Een oude aanroep zonder argument zou dus stuk gaan. | Vermoeden | Midden | De workflow of het gidsverslag bekijken |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan geen beeld zien, dus dit zijn aandachtspunten voor wie de plaatjes bekijkt.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De variabele heet ELLEBOOG, maar het gewricht staat 12 mm boven de elleboog. Op de echte elleboog is de arm "Too thin". Een lezer die de gids volgt en op zijn elleboog klikt, krijgt dus rood. | Eén zin in de gids dat dunne ledematen een dikkere plek vragen. Dat is ook eerlijk over wat de add-on doet. | Klein |
| 2 | Het plaatje staat bewust op groen. Dat is een gunstig geval. Voor een gids is dat goed, maar de lezer ziet nooit hoe oranje of rood eruitziet. | Eventueel een vierde plaatje met Tight of Too thin, met de melding erbij. | Klein |
| 3 | De camera kijkt 160 mm breed naar het gewricht, met "Exploded view" aan. Of het beeld na 30 seconden duidelijk is, kan ik niet zien. | Iris of Daan bekijkt s2-joint op leesbaarheid. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- De licentie van Knight.blend (Quaternius, CC0) bij het bronbestand vastleggen, zodat de claim in het docstring gecontroleerd is (Deel B, 2).
- Nagaan of de botnamen "UpperArm.L" en "UpperLeg.L" kloppen, en of de aanroep van `gids_stl_bron.py` het nieuwe argument meegeeft (Deel A 4, Deel B 5).
- In de gids erbij zetten dat de elleboog van dit figuur te dun is en dat het gewricht daarom hoger staat (Deel C, 1).
- Daan of Iris bekijkt de drie plaatjes op beeld en leesbaarheid. Een agent kan dat niet doen.
- Het bestand voor `gewrichten.json` wordt geopend zonder `with`. Dat is een klein netheidspunt.

---
Automatische keurder, model `claude-sonnet-5-5`, 21407 tokens in, 4355 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
