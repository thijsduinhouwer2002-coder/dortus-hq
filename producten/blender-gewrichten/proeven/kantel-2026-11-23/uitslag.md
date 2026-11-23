# Proef kantel-herkansing (Olaf, 23 nov 2026 ±20:15 tot 20:35 NL)

Vraag: de booleaanse snede valt per processor net anders uit (CI AMD, lokaal Intel). Een kapotte snede ("blocked" of
"no watertight parts") kostte een gewricht. De omweg van 6dcadc8 (laatste plek 0,3 mm verder) werkt op MakeHuman niet
(toets CJ_HERKANS=2: "too close" of "blocked"), en de Exact-terugval van 1.2.2 geeft op MakeHuman nergens gesloten
delen (tak claude/olaf-a4-exact). Werkt een tweede kans op **dezelfde plek met de as 0,5 graad gekanteld**?

Code: tak `claude/olaf-kantel` (07b0c8f), niet op main.
- `click_joints/betaald/rig.py`: `KANTEL_GRADEN = 0.5`, `gekanteld(m)`, en in Figure from rig `kantel_in`: na
  "blocked" of "no watertight parts" op een kogelplek komt dezelfde plek gekanteld direct als volgende kandidaat
  (één keer per plek, scharnieren niet).
- `e2e/toetsen_mens.py`: toets `CJ_HERKANS=4` met `CJ_HERKANS_LID`: op dat lid weigert de beweegproef elke
  ongekantelde snede; een gekantelde snede wordt echt beoordeeld. Daarna alle gewone eisen van de toets.

Uitslag lokaal, Blender 5.3.0, MakeHuman base.obj 220 mm (GEZIEN, logs van deze run):

| run | uitslag | lid in de proef |
|---|---|---|
| gewoon (geen CJ_HERKANS) | 9 gewrichten, KLAAR 0 FOUT | gelijk aan main |
| CJ_HERKANS=4, Left shoulder | 9, KLAAR 0 FOUT | gekanteld geplaatst, ±20 (zelfde als gewoon) |
| CJ_HERKANS=4, Right shoulder | 9, KLAAR 0 FOUT | gekanteld geplaatst, ±20 (zelfde als gewoon) |
| CJ_HERKANS=4, Left hip | 9, KLAAR 0 FOUT | gekanteld geplaatst, ±20 (gewoon ±25) |

Bij de schouders gaf de proef 5 weigeringen en 5 gekantelde sneden die bewogen voor het gewricht stond: gekantelde
sneden kunnen nog op een latere eis afvallen (welke heb ik niet gelogd). Elke run duurde ±6 min op 2 kernen.

Wat dit niet bewijst: dat de gekantelde snede op de AMD-processor van CI wel heel is. Volgende stap: in CI de robot van
studio-2 en het studio-figuur draaien met de 0,3 mm-plek eruit en de kantel aan; 9 gewrichten = bewijs.
