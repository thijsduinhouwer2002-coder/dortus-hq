# Click Joints Pro 1.2.1: mooier overlay (Bram, 23 nov 2026)

**Waarom (geld):** onze verkoop loopt via Shorts en winkelbeelden, en keurders vonden het beeld van Pro een "meetblad" (negen getallen, kopregel over het hoofd). 1.2.1 toont standaard alleen het gekozen gewricht, met naam, en kleurt voorbij de stop het hele deel rood. Doel: live vóór wo 25 nov, zodat de saleweek met de nette versie begint (opdracht hoofdchat 23 nov 13:00). Effect op verkoop: GOK, klein maar blijvend (elk filmpje en elke winkelfoto profiteert).

**Versie: 1.2.1 en niet 1.3.** Reden: alle gekeurde 1.2-teksten blijven dan kloppen ("New in Pro 1.2" op Superhive, "1.2 is a free update" op Gumroad, lijst Thijs punt 3). Er komt geen nieuwe functie bij die iets meet of maakt; alleen wat er in beeld staat en hoe. Eén zip om te plaatsen: 1.2.1 in plaats van 1.2.0. Staat 1.2.0 al op Gumroad of Superhive, dan is 1.2.1 gewoon de volgende bestandswissel.

## Stand (bijwerken per stap)
1. Tak `claude/pro-mooier-overlay` samengevoegd met main (87ca7d4), plus 6aec211: schermtest van de standaard Labels Selected in de gewone e2e (moet 1: stap "Standaardbeeld Labels Selected", eis `MOOI SELECTED OK`), boog feller in Selected en bolletje rood voorbij de stop (C4 keuring, sterk aangeraden door Daan), dode code weg (kan 1).
2. e2e op de tak in 4.2.23, 5.2.3 en 5.3.0: loopt (moet 3).
3. Winkelteksten hieronder: naar Daan (moet 2).
4. Daarna: tak naar main, PRO_VERSIE en uitgave-workflow op 1.2.1, uitgave-run, melden aan de hoofdchat.

## Releasenotes 1.2.1 (Engels, Gumroad en Superhive)
```
Click Joints Pro 1.2.1
- Cleaner view on figures: new Labels setting in Figure joints (Selected, All or None). Selected is the new default: only the joint you select shows its arc and range, with its name. Set Labels to All for the old view, or None for a clean render.
- On a figure, past the end stop the whole moving part turns red, so you see it at once.
- Labels on a figure are now dark pills that read on any model.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```

## Winkelteksten: vervangen (moet 2 keuring, C1)
Plekken met de oude zin "Every range in one view. A small degree arc at each joint with its number, ...":
- Gumroad "What you get" (`platformen/blender-2/gumroad-1.1.md` r39, live pagina)
- Superhive (`platformen/blender-2/superhive-1.1.md` r52)
- `platformen/blender/superhive/where-to-find-it.md` r25
- `platformen/blender-2/winkeltekst-1.1.md` r13 (zelfde zin, vet begin)

Nieuwe zin (overal dezelfde):
```
Every range at a glance. Select a joint to see its degree arc and range, with its name. Set Labels to All to show every joint at once, or None for a clean render. Plus a list in the panel: name, type, range and where the range came from (from rig, mirror or preset).
```

## Gumroad: plakklaar blok bij de zipwissel (moet van Daan, 23 nov 12:50)
Letterlijk uit Daans keuring (`keuring/2026-11-23-gumroad-pro-tekst-vs-1-2-daan.md`), dus geen herkeuring nodig:
1. "Already bought Pro? 1.1 is a free update: download it again from your Gumroad library." wordt:
```
Already bought Pro? 1.2 is a free update: download it again from your Gumroad library.
```
2. Nieuw punt onder "What you get":
```
Fit test strip. Print this first: five joints from 0.10 to 0.30 mm clearance, each with its number, so you know which gap fits your printer.
```
3. (kan) "print a test joint first" wordt "print the Fit test strip first".
4. Nieuw met 1.2.1: de zin "Every range in one view ..." vervangen door de nieuwe zin hierboven (wel langs Daan).

## Superhive: Update log erbij
```
1.2.1 (<dag van upload> Nov 2026): Labels Selected, All or None in Figure joints (Selected is the new default); on a figure, past the end stop the whole part turns red.
```
Het blok "New in Pro 1.2" (`superhive/nieuw-in-1-2.md`) blijft gelden. Plus de nieuwe zin "Every range at a glance ..." in plaats van de oude.

## Na te kijken door de keurder
- Klopt elke zin met de code op de tak (Labels in Figure joints, standaard Selected, rood deel alleen bij een figuur, pillen).
- Geen prijs, geen korting, niets beloofd wat niet in de zip zit.
