# Keuring blender-gewrichten Check parts (issue 42, Pro), 26-11-2026 00:14 NL, automatische keurder
Wat ik keurde: commit 9f5f8153d (68cf411..9f5f815), tak `claude/blender-check-delen`
Akkoord: nee

## Deel A: doet het wat beloofd is?
Getoetst tegen de sectie "Ontwerp Check parts" in `ontwerp.md`.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De code heeft alle onderdelen van "Af als": knop Check parts, Min wall, per deel open randen, losse stukken en dunne wand bij een gewricht, en een klik opent Edit Mode met die selectie. De haak in `STAP3` staat er, met register en unregister. | Feit (uit de diff) | hoog | n.v.t. |
| 2 | "Af als" eist een groene e2e in 4.2, 5.2 en 5.3. In de wijziging staat geen run-id of uitslag. Dat de test slaagt, kan ik niet zien. | Vermoeden | midden | Een groene Actions-run met id voor alle drie de versies. |
| 3 | `toetsen_check.py` leunt op `toetsen_los._blok`, `toetsen_paneel.teken` en `toetsen_paneel.plek`, en op de tekst "3  Fit and export". Die staan niet in deze diff. | Vermoeden | midden | De run uit rij 2, of een blik in die helpers. |
| 4 | De uitslag bewaart `gewricht` (waar/onwaar), maar `teken()` gebruikt het niet. Zonder gewricht staat er dus "All 1 parts OK" terwijl de wandcontrole nooit liep. Dat klinkt als "wand gecontroleerd". | Feit (uit de code) | hoog | Check parts op een figuur zonder `cj_deel`: komt er "OK" zonder uitleg? |
| 5 | `dunne_vlakken` doorloopt alle vlakken in Python, met een numpy-aanroep per vlak. Dat gebeurt bij elke Check parts én bij elke klik op "dun". Op delen van ±200K driehoeken kan dat merkbaar traag zijn. Er is geen tijdtoets. | Vermoeden | laag | Een meting op het figuur van 261K driehoeken. |
| 6 | De uitslag in `scene["cj_check"]` veroudert zodra je de mesh aanpast. Het paneel blijft dan de oude aantallen tonen tot je opnieuw controleert. De klik rekent wel opnieuw uit, dus de selectie kan afwijken van het getal op de knop. | Feit (uit de code) | midden | Een gat dichtmaken in Edit Mode en het paneel bekijken. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` staat niet bij de gewijzigde bestanden. De nieuwe module `betaald/check_delen.py`, de vulling van `STAP3` en `scene["cj_check"]` staan er dus niet in. Het bestand beschrijft juist de betaalde stukken en de lijsten `BOVEN`, `STAP2`, `STAP2_KEUS` en `STAP3`. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er is geen bestaande test aangepast. Er zijn alleen een nieuw testbestand en één aanroep in `test_betaald.py` bij gekomen. | Feit | hoog | Tests niet aangepast om te slagen: voldaan |
| 3 | `check_delen.py` is 261 regels en `toetsen_check.py` 119. Beide blijven onder ±400. Hoe lang `test_betaald.py` en `betaald/__init__.py` nu zijn, zie ik niet. | Feit (nieuwe bestanden), vermoeden (de rest) | midden | Bestanden onder ±400 regels |
| 4 | De wijziging staat alleen in `betaald/`, en het ontwerp zegt dat het gratis deel gelijk blijft aan de gekeurde stand. De toets `toets_zips.py` heb ik niet kunnen zien draaien. | Vermoeden | midden | Gratis build gelijk aan gekeurde stand |
| 5 | Het getal "700.759 downloads" in het ontwerp heeft GEZIEN met bron en datum. Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | hoog | Cijfers met label, geen persoonsgegevens: voldaan |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen schermen, alleen tekst. Dit is dus een lezing van de code.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een regel per fout met een klik naar de plek is duidelijk en volgt het voorbeeld van 3D Print Toolbox. | Niets nodig. | n.v.t. |
| 2 | De standaard Min wall is 1,5 mm (grens Tight). De rest van het paneel noemt 0,8 mm als "Too thin". Twee grenzen naast elkaar kunnen verwarren. | Zet een korte hint bij Min wall, bijvoorbeeld "1.5 = Good fit". | klein |
| 3 | Na een klik zit je in Edit Mode. Er is geen aanwijzing hoe je terugkomt of de selectie herhaalt. | Zet in de melding "Tab to leave Edit Mode". | klein |
| 4 | De oude uitslag blijft staan na een reparatie (zie A6). Dat voelt als een fout die niet weggaat. | Wis de uitslag bij een wijziging, of toon "run again". | midden |
| 5 | "All parts OK" zonder gewricht suggereert meer dan gecontroleerd is (zie A4). | Zeg "OK (no joint, wall not checked)". | klein |

Is het goed genoeg? Er is geen beeld of schermafbeelding meegestuurd, dus ik kan geen cijfers geven. Dit is geen eerste-indrukbeeld, dus de blinde test geldt hier niet. Daan keurt het uiterlijk, zoals het ontwerp zelf zegt ("na Daans keuring").

| Vraag | Cijfer 1 tot 10 | Waarom |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | niet te geven | Geen scherm gezien. |
| Zou ik het zelf kopen of bekijken op basis van dit? | niet te geven | Geen scherm gezien. |
| Zou Thijs er trots op zijn? | niet te geven | Geen scherm gezien. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Werk `architectuur.md` bij met `betaald/check_delen.py`, de haak in `STAP3`, `cj_check_wand_mm` en `scene["cj_check"]` (B1).

**Kan**
1. Laat de groene run in 4.2, 5.2 en 5.3 zien met run-id; zonder die run valt het akkoord van Daan niet te geven (A2, A3).
2. Zeg bij "OK" zonder gewricht dat de wand niet gecontroleerd is (A4, C5).
3. Meet de tijd op een figuur van ±261K driehoeken (A5).
4. Wis of ververs de uitslag na een wijziging aan de mesh (A6, C4).
5. Voeg hints toe bij Min wall en bij het verlaten van Edit Mode (C2, C3).
6. Daan keurt het uiterlijk van het paneel; dat hoort bij de keuring na deze ronde.

---
Automatische keurder, model `claude-sonnet-5-5`, 29548 tokens in, 6891 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
