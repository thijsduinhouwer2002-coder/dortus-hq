# Click Joints: architectuur (v0.1, gratis kern)

Blender-extensie (4.2+) die een figuur op de 3D-cursor in twee gesloten, printbare delen snijdt met een kogel en kom (of pen en gat). Ontwerp: `ontwerp.md`. Bouwproef waar de geometrie uit komt: `proef/proef_gewricht.py`.

## Onderdelen (`click_joints/`)
- `__init__.py`: registreert de klassen van alle modules.
- `eigenschappen.py`: instellingen per scene (`scene.click_joints`): speling in mm (standaard 0,2), diameter in mm, soort kogel of pen, as (kijkrichting of cursor), voxelgrootte, exportmap. Ook `eenheid_per_mm(scene)`: mm volgt de eenheidschaal van de scene.
- `paneel.py`: zijbalk N, tabblad "Click Joints", drie genummerde stappen (1 Plek, 2 Gewricht, 3 Controleer en exporteer), per stap één grote knop. Passing met kleurnaam en icoon (vinkje, uitroepteken, kruis).
- `gewricht.py`: operator `click_joints.plaats`. Volgorde: manifold-check, kopie in wereldcoördinaten, passingcontrole, dan snijden met de Boolean-modifier (Manifold op 4.5+, anders Exact). Deel A = onder het snijvlak plus kogel en nek; deel B = boven het snijvlak min (kom plus klikopening als één snijvorm). De klikopening is 0,85 keer de kogeldiameter, zodat los geprinte delen met wat druk in elkaar klikken; de nek is 0,48 keer, dus het gewricht beweegt. Kogelmidden op 1,4 keer de straal boven het snijvlak, zodat de bodem van deel B dik genoeg is. Snijvlak 0,0137 mm naast de cursor. Origineel blijft verborgen bewaard. Bij rood wordt niet gesneden: er komt alleen een rode draadbol als teken.
- `vormen.py`: hulpvormen (bol, cilinder, doos) in een frame waarvan Z de gewrichtsas is, 64 segmenten.
- `passing.py`: BVH-tree van het figuur; stralen vanuit het kommidden (alle kanten op, naar beneden tot het snijvlak) en rond de opening geven de kleinste wanddikte, plus de dikte van de bodem van deel B naast de opening. Rood onder 0,8 mm of als het gewricht uitsteekt, oranje onder 1,5 mm, anders groen. Meet ook de speling (find_nearest van kogelpunten naar het komdeel).
- `gesloten.py`: telling van randen met een ander aantal vlakken dan 2 (numpy) en volume; operators `click_joints.controleer` en `click_joints.maak_gesloten` (voxel-remesh op een kopie).
- `exporteer.py`: operator `click_joints.exporteer`, elk zichtbaar deel als binaire STL in mm via `bpy.ops.wm.stl_export`.

Op elk deel staan eigenschappen: `cj_deel` (A/B), `cj_passing` (groen/oranje/rood), `cj_wand_mm`, `cj_speling_mm`, `cj_speling_gemeten_mm`, `cj_centrum`, `cj_as`, `cj_kogel_r`, `cj_solver`, `cj_duur_s`, `cj_bron`. De objectkleur volgt de passing (zichtbaar met Viewport Shading op Object).

## Testen (`e2e/`, workflow `.github/workflows/blender-gewrichten-e2e.yml`)
- `maak_zip.sh`: extensie-zip naar `/tmp/click_joints.zip`, daarna `blender --command extension validate`.
- `figuren.py`: testfiguren (arm van ±261K driehoeken, pop van bollen en cilinders, open arm) in een scene met 1 eenheid = 1 mm.
- `test_achtergrond.py`: harde poort zonder scherm: twee gesloten delen, speling 0,1/0,2/0,3 mm over 500+ punten, klikopening tussen 0,80 en 0,90 keer de kogel en de nek past erdoor, rood bij een wand van 0,4 mm en oranje bij 1,1 mm (staaf), Manifold onder 5 s, open figuur en Maak gesloten, tijd per solver, STL heen en terug.
- `schermen.py`: echte interface onder Xvfb, tabblad via xdotool Ctrl+muiswiel, plaatjes naar tak `schermen` in `blender-gewrichten/<tak>/<versie>/`.

Niet in v0.1: 3MF, beweegproef, inklik-animatie, betaalde functies, undo-toets in Xvfb.
