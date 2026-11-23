# Keuring scripts week 49 Click Joints Pro, 23 nov 2026, Daan
Wat ik keurde: `commercie/filmpjes/scripts/week-49-click-joints.md` (d61abec, Sanne), tegen `platformen/blender-2/gumroad-1.1.md`, `platformen/blender/pro-1.2.0.md`, `pro-1.2.1.md` en de code op main (`click_joints/`)
Akkoord: nee (3 moet, alle drie klein; scripts 2, 4 en 5 mogen zo door)

## Deel A: klopt elke gesproken zin?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Script 1 verkoopt exporteren als reden voor Pro, maar exporteren zit ook in de gratis Click Joints: `exporteer.py` en de knop "Export STL / 3MF" in `paneel.py` r. 119 zijn gratis bestanden. Zin 3 "In Click Joints Pro, step three is Fit and export" is letterlijk waar, maar wie Pro koopt om te exporteren, had het gratis al. Kans op spijt en terugbetaling. | feit (code) | hoog | |
| A2 | Script 6 zin 2 en 3: "only places a joint when the fit is good" en "the seam turns green" kloppen niet met de code. Een kogel met Tight (oranje) wordt wel gesneden, alleen rood niet (`gewricht.py`: "Tight blijft Tight"; `passing.fit_tekst` geeft "Tight: wall ... mm"). De Pro 1.0-tekst waar Sanne uit putte zegt het zo, maar de add-on doet het anders. | feit (code) | hoog | Een opname waarin een oranje gewricht verschijnt. |
| A3 | Script 3 zin 6 ("elbows and the shoulders") en script 5 ("Left ankle") heeft Sanne zelf al als GOK gemarkeerd met een terugvaltekst. Goed zo. | feit | hoog | De opname. |
| A4 | Script 4: Labels Selected/All/None, "only the joint you select ... with its name", "whole part turns red" kloppen met `pro-1.2.1.md` r. 16-17. De schuif heet echt "Bend" (`betaald/__init__.py`). | feit | hoog | |
| A5 | Script 5: "More bones (ankles too)" staat zo in `betaald/figuur.py` r. 226; standaard schouders, ellebogen, heupen, knieën en nek klopt met `rig.py` r. 5. | feit | hoog | |
| A6 | Script 2: zin 3, 4 en 5 letterlijk uit "Good to know" en "Honest when it can not". Goed. | feit | hoog | |
| A7 | Hooks: alle twaalf 5 tot 7 woorden en met vraagteken. Elf zijn een vraag over het probleem; 2B "Printing your figure at 150 millimetres?" is een vraag over een maat, niet over het probleem. | feit (geteld) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Script 1 zin 2 noemt als beeld "de gekleurde figuur in delen (studio-1)". Thijs vond die figuur "super nep"; hoofdchat 23 nov 14:40 NL: niet gebruiken in nieuwe Shorts (`berichten/bram.md`). | feit | hoog | Besluit Thijs via hoofdchat |
| B2 | Printzin en eindkaart in elk script; geen slicer- of AI-dienstnaam; "Measured in Blender, not print tested by us yet" blijft. Script 4 netjes op slot tot 1.2.1 op Gumroad staat. | feit | hoog | |

## Deel C: zou een kijker het leuk vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Script 6 en 2 zijn eerlijk en sterk ("the list tells you why"), maar drie scripts (2, 3, 6) draaien om wat níet lukt. In één week voelt dat als een add-on die vaak weigert. | 2 en 3 niet in dezelfde week als 6 plaatsen; of in 2 en 3 eindigen op een beeld dat wél lukt (de figuur op 200 mm, de elleboog die buigt). | klein |
| C2 | Script 1 kan juist de beste Pro-reden laten zien: tien delen met gewrichten uit één klik op Figure from rig, dán één klik export. Dat is iets wat gratis niet kan. | Zie moet 1. | klein |
| C3 | 2B is zwak als hook (A7). | Bv. "Arms too thin for a hinge?" (6 woorden). | klein |

## Moet (blokkeert akkoord)
1. **Script 1 (A1, C2):** maak Figure from rig de Pro-reden en export het gevolg. Bv. zin 2: "One button, Figure from rig, cut this figure into ten parts with joints." en zin 3: "Then step three, Fit and export, writes every part as its own file." Nergens zeggen of laten denken dat exporteren alleen in Pro zit.
2. **Script 6 (A2):** zin 2 en 3 vervangen door wat de code doet, bv. "Click Joints Pro colours every joint by fit before you print." en "Green fits, orange is tight, and red is too thin to cut." Kop: "Green, orange, red". De opname moet dan ook echt een groen en een oranje gewricht tonen.
3. **Script 1 (B1):** geen studio-1-figuur. Beeld uit studio-2 (robotfiguur, `figuur_robot.py`, 73398a8) of de renders van shorts-4; het aantal delen in zin 2 is dan wat die figuur echt geeft.

## Kan (mag later)
1. C3: hook 2B vervangen door "Arms too thin for a hinge?".
2. C1: in de volgorde van week 49 niet 2, 3 en 6 vlak na elkaar.
3. Na de moet-punten keur ik alleen script 1 en 6 opnieuw.
