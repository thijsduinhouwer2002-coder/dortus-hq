# Fit test strip in Pro: ontwerp (Bram, 19 nov 2026 ±16:40 UTC)

Opdracht hoofdchat 19 nov 14:00 NL punt 3; plan `platformen/blender/click-joints-plan-2026-11-19.md` C1 (2 tot 3 runs). Skill `bouwen-in-stappen`, stap 1 en 2 (begrijpen en ontwerp). Bouwen vanaf de volgende run, na Gumroad 1.1.0.

## Waarom (geld)
De eerste vraag van een koper is "welke speling?". Wij schrijven zelf "print a test joint first", maar geven er geen knop voor. Een los testkaartje wordt op Superhive voor $7 verkocht (GEZIEN 8 nov, `prijs.md`). Een knop "Print this first" maakt Pro waardevoller op de pagina en scheelt slechte reviews van mensen bij wie het eerste gewricht vastzit of los valt.

## Wat de koper ziet
- In het paneel Click Joints, bovenaan het Pro-deel: knop **Fit test strip** met de regel "Print this first: five joints from 0.10 to 0.30 mm".
- Keuze in het venster van de knop: Ball of Hinge (standaard het type dat nu gekozen is).
- Klik: in een nieuwe collectie "Fit test" staan vijf staafjes naast elkaar (20 mm uit elkaar), elk met één gewricht bij 0.10 / 0.15 / 0.20 / 0.25 / 0.30 mm speling, en op de bovenkant van elk staafje het getal in reliëf (0,6 mm hoog). Geen ander object wordt aangeraakt; de eigen speling van de scene blijft zoals hij was.
- Daarna de gewone knop Export: tien delen als STL of 3MF (bestaande `exporteer.py`, alles met `cj_deel`).
- Meldregel: "Print all five. Use the clearance of the one that turns without wobble."

## Hoe (code)
- Nieuw `betaald/testkaart.py`, operator `click_joints.testkaart`, geregistreerd in `betaald/__init__.py` (KLASSEN en een `teken_knop` in het paneel, zoals `scharnier.teken_knop`).
- Per speling: staaf maken zoals `commercie/blender-click-joints/testprint/maak.py` (`staaf`, r 10 mm voor kogel, 7 mm voor scharnier, 40 mm lang), `inst.speling_mm` tijdelijk op de waarde, cursor in het midden, `bpy.ops.click_joints.plaats()` of `plaats_scharnier(stand='115', kijk_richting=(0,-1,0), kijk_omhoog=(0,0,1))` zodat het zonder venster werkt. Na afloop (ook bij een fout, `try/finally`) speling, cursor en actief object terug.
- Getal: tekstobject, `body` "0.15", omzetten naar mesh, extruderen 0,6 mm, met een boolean (EXACT, union) op het bovenste deel. Daarna `is_gesloten` op dat deel: niet gesloten = getal weglaten en dat melden, nooit een kapot deel achterlaten.
- Eenheden: alles via `eenheid_per_mm(scene)`, zodat het ook in een scene in meters goed staat.

## Toetsen (e2e, zelf schrijven vóór de code)
`e2e/toetsen_testkaart.py`, in de e2e-workflow, op de Pro-zip, Blender 4.2.23, 5.2.3 en 5.3.0:
1. Na de knop precies 10 delen met `cj_deel`, in collectie "Fit test".
2. `cj_speling_mm` (of wat het gewricht nu opslaat) per paar gelijk aan 0.10 tot 0.30.
3. Alle tien delen gesloten (`is_gesloten`), ook met getal.
4. `scene.click_joints.speling_mm` na afloop gelijk aan ervoor (bijvoorbeeld 0.20).
5. Export daarna geeft 10 bestanden.
6. Een tweede klik maakt een nieuwe set naast de eerste, niet over een bestaande heen.
Beeld: plaatje 20 (testkaartje schuin van boven, getallen leesbaar) voor Daan en voor de winkel.

## Open vragen (zelf beslist, met reden)
- Eén STL voor alles (plan C1) of losse delen? **Losse delen**: de bestaande export doet dat al en een slicer zet ze in één keer op het bed. Scheelt een run.
- Gratis versie? **Nee**: plan regel 138, het testkaartje hoort bij Pro.
- Winkeltekst: pas als het gekeurd en uit is één regel "Fit test strip: print five joints first and pick your clearance". Geen belofte over welke speling werkt (er is nog geen print).

## Volgende stappen
1. Toetsen schrijven (stap 3), lokaal Blender 5.3 laden (kost ±30 s, les 19 nov) en rood zien.
2. `testkaart.py` bouwen tot de toetsen groen zijn, lokaal 4.2 en 5.3.
3. Push naar main, e2e groen in drie versies, plaatje 20 zelf bekijken, Daan vragen.
4. Pro 1.2.0 (of 1.1.1) pas uitbrengen samen met de volgende Pro-wijziging; niet los vóór Gumroad 1.1.0 staat.
