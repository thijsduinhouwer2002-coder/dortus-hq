# Keuring blender-gewrichten, Pro 1.2.9 paneel (issue 70), 25-11-2026 18:12, automatische keurder
Wat ik keurde: commits c52c9a2..11323f7 (alleen de tekst van de wijziging, niets gedraaid, niets gezien)
Akkoord: ja

## Deel A: doet het wat beloofd is?
Getoetst tegen de beschrijving van issue 70 in de commits en in KAART.md. Het 1.2.9-stuk van ontwerp.md zat niet in wat ik kreeg.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | "Figure from rig" staat nu in `BOVEN`, vóór stap 1, en alleen als de mesh een rig heeft (`teken_boven`). De test in `toetsen_paneel.py` controleert "Rig found" en de knop vóór "1  Place" en dat zonder rig niets komt. | Feit (code en test) | Hoog | De groene run 45644233399 zelf bekijken. Die staat alleen in KAART, dus uit tweede hand. |
| 2 | De proefstrip staat in stap 2 onder Clearance, het scharnier onder Place joint. Beide komen via `STAP2` en `STAP2_KEUS`. De test controleert de volgorde en dat er niets van Pro meer onder Export staat. | Feit (code en test) | Hoog | Schermbeeld van stap 2 in Blender. |
| 3 | Stap 3 zegt "Hinge placed" bij een geplaatst scharnier en toont het bereik of "No end stop found". Dit volgt Daan #83 C2 en is getoetst. | Feit (code en test) | Hoog | Run-uitslag. |
| 4 | Na een Good fit komt "Happy with it? Leave a rating:" met een knop per winkel. De gratis build wijst naar extensions.blender.org, Pro naar Superhive en Gumroad. Bij uitzetten van Pro gaan de links terug naar gratis. Alles is getoetst in `test_betaald.py`. | Feit (code en test) | Hoog | Run-uitslag. |
| 5 | De links zijn "met curl nagekeken (200)" volgens de commentaren. Ik kan dat niet zien. Vooral `extensions.blender.org/add-ons/click-joints/reviews/` kan een 404 geven als de naam of het pad anders is. | Vermoeden | Midden | `curl -sI` op beide links. |
| 6 | Schermbeeld 16a (Rig found bovenaan) is niet meegestuurd. Of het paneel er netjes uitziet, kan ik niet zeggen. | Vermoeden | Laag | Beeld 16a met Read bekijken. Daan keurde het volgens de commit al met ja (#89). |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De hashes van `paneel.py` en `meld.py` in `toets_zips.py` zijn aangepast. Er staat een datum en reden bij, en de diff van beide bestanden komt overeen met die reden. Het is geen aanpassing om een test te laten slagen. | Feit | Hoog | Tests niet aangepast om te slagen: ok, wel hier genoemd. |
| 2 | De gratis `paneel.py` en `meld.py` noemen de betaalde versie nergens. De lege lijsten en de gratis winkel staan er zonder verwijzing naar Pro. | Feit | Hoog | Extensions-regels 3.3, 3.10 en 6.1: ok. |
| 3 | `architectuur.md` is bijgewerkt voor lijsten, rating en de verplaatste Pro-knoppen. In de bullet van `meld.py` staat nog "`paneel.py` blijft gelijk", terwijl dat nu niet meer klopt. | Feit | Hoog | architectuur.md bijgewerkt: bijna. Zie kan. |
| 4 | Ik kan de regeltelling van `paneel.py`, `test_betaald.py` en `scharnier_boog.py` niet nagaan. Alleen de diff staat erbij. | Vermoeden | Laag | Bestanden onder ±400 regels: `wc -l` erop. |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden gezien in de wijziging. Cijfers in KAART hebben GEZIEN of een bron. | Feit | Hoog | Persoonsgegevens en cijferlabels: ok. |
| 6 | Hoewel de wijziging klaar is, staat in de opdracht (ontwerp.md zoals ik die kreeg) nog geen regel "Akkoord: ja" van Daan voor 1.2.9. Het ja staat alleen in de commitberichten en KAART. | Feit | Midden | Bij uiterlijk: Akkoord van Daan bovenaan ontwerp.md. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Alleen uit de tekst afgeleid, niets gezien of gespeeld.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De beoordelingsregel blijft staan zolang er ergens in de scène een groen gewricht is. Een gebruiker ziet hem dus bij elke sessie, ook na een rating. | Een eigenschap "al gevraagd" onthouden, of de regel verbergen na een klik op een winkelknop. | Klein |
| 2 | De regel verschijnt al bij het eerste groene gewricht, voordat de gebruiker iets geprint heeft. Het is nog niet bewezen dat het klikt. | Alleen vragen na een export, bijvoorbeeld zodra de STL of 3MF is geschreven. | Klein |
| 3 | Figure from rig staat nu bovenaan in een vak met een grote knop (scale 1,6). Dat is voor wie een rig heeft duidelijk de eerste stap. Of het paneel hierdoor te lang wordt, weet ik niet. | Hoogte meten op een schermbeeld van 4.2 in een smalle zijbalk. | Klein |

## Deel C: is het goed genoeg?
Er is geen hoofdbeeld, omslag of thumbnail veranderd, dus de blinde test is niet nodig. Ik zie geen beeld, dus ik geef geen cijfers en kijk niet naast een concurrent. Dat blijft aan Daan, die volgens de commit ja zei (#89).

| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | Geen cijfer | Geen beeld gezien. Daan #89 bij het paneel naast Cleave en CatPin is de enige bron (DERDEN). |
| Zou ik het zelf kopen of bekijken op basis van dit? | Geen cijfer | Geen beeld gezien. |
| Zou Thijs er trots op zijn? | Geen cijfer | Geen beeld gezien. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer met `curl -sI` de twee winkellinks, vooral het pad `/reviews/` op extensions.blender.org, voor de gratis versie uitkomt (Deel A 5).
- Zet Daan's "Akkoord: ja" voor 1.2.9 bovenaan `ontwerp.md`, voor het uitbrengen.
- Haal "`paneel.py` blijft gelijk" uit de `meld.py`-bullet van `architectuur.md`.
- Controleer de regeltelling van `paneel.py` en `test_betaald.py`.
- Vraag pas om een beoordeling na een export of na één keer vragen (Deel C 1 en 2).
- In KAART staat "op main sinds ±18:20", terwijl deze keuring om 18:12 gedaan is. Pas de tijd aan als hij niet klopt.

---
Automatische keurder, model `claude-sonnet-5-5`, 37451 tokens in, 7928 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
