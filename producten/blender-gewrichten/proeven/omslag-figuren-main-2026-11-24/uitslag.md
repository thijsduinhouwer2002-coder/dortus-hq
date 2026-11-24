# Figure from rig van main (Pro 1.2.3) op de omslagfiguren (24 nov 2026, Olaf)

Waarom: Pro 1.2.3 staat op main (14e6e42). De testset van Betrouwbaarheid draait alleen op zijn tak en heeft de houten
tekenpop niet, terwijl kopers die op de nieuwe omslag zien. Workflow `.github/workflows/cj-rig-main.yml`, run
45295977807 op commit 3974792, script `e2e/meet_rig.py` (figuur `tekenpop` toegevoegd), standaardinstellingen,
elke meting twee keer. JSON en log per meting op de tak `betrouwbaar-uitslag`, map `main-45295977807/<versie>/` (GEZIEN).

| Figuur | 4.2.23 | 5.2.3 | 5.3.0 |
|---|---|---|---|
| tekenpop | 9 en 9 (1 slechte snede onderweg, 104 en 114 s) | 9 en 9 (0, 87 en 54 s) | 9 en 9 (0, 83 en 89 s) |
| kleding (MakeHuman, studio-1) | 8 en 8, rechterknie weg (6 slechte sneden, 207 en 143 s) | 9 en 9 (0, 76 s) | 9 en 9 (0, 65 en 95 s) |

Alle delen gesloten, beide herhalingen gelijk.

## Wat dit zegt
1. De tekenpop van de omslag krijgt in elke versie alle 9 gewrichten: wat de koper op de omslag ziet, krijgt hij ook.
2. Kleding is in 5.x 9 van 9 (was 8 in CI op 1.2.0); in 4.2 blijft de rechterknie weg met "Tight: too little limb past
   this joint" (Exact-solver), gelijk aan de ondergrens 8 in `e2e/meet_drempel.json`. Geen terugval, wel een open punt
   voor 4.2 (zelfde melding als bij de knieën van spacetrooper1, zie `../ai-figuren-tak-rig-2026-11-24/`).
3. De releasenote klopt. Letterlijke regel uit `platformen/blender/pro-1.2.3.md` (r21): "On our test figures in Blender
   5.2 and 5.3 it placed every joint, and the same mesh gave the same joints every time we ran it." Die belooft niets
   voor 4.2, en dat is goed: **in 4.2 geeft kleding 8 van 9** (rechterknie weg). Niet beloven dat elk figuur in 4.2
   alles krijgt.

## Aanvulling 24 nov ±02:30 (kan-punten keuring 97ccf45)
- Commit 3974792 (gemeten) en main 14e6e42 (Pro 1.2.3) zijn voor de add-on gelijk: `git diff 14e6e42 3974792 --
  producten/blender-gewrichten/click_joints` is leeg (GEZIEN). Tussen die twee zitten alleen de spiekbrief van Bram,
  een automatische keuring en deze meting.
- Samenvatting van de tak `betrouwbaar-uitslag` (map `main-45295977807/`), zodat het hier na te gaan is (GEZIEN):

| Versie | Figuur | Run 1 | Run 2 | Ontbreekt |
|---|---|---|---|---|
| 4.2.23 | tekenpop | 9 | 9 | |
| 4.2.23 | kleding | 8 | 8 | Right knee |
| 5.2.3 | tekenpop | 9 | 9 | |
| 5.2.3 | kleding | 9 | 9 | |
| 5.3.0 | tekenpop | 9 | 9 | |
| 5.3.0 | kleding | 9 | 9 | |

- Rechterknie kleding in 4.2, pogingen uit `4.2.23/kleding-1.json` (run 2 gelijk, GEZIEN). De linkerknie lukt op
  (20,9; 10,3; 59,1), de rechterknie op precies het spiegelbeeld niet:
  1. (-20,9; 10,3; 59,1): "The parts overlap before they move" (beweegproef in `scharnier.py`).
  2. (-20,6; 11,3; 59,1): weer "overlap before they move".
  3. (-22,1; 12,7; 54,4): Exact-snede geeft deel A met 623 slechte randen ("no watertight parts").
  4. (-23,7; 14,2; 49,6): "Tight: too little limb past this joint".
  In 5.3 lukt de rechterknie meteen op plek 1. Het verschil zit dus in de eerste twee pogingen (Exact in 4.2, de
  delen overlappen al in rust), niet in de dikte van het been.
- **Misleidende reden voor de koper:** de lijst zegt "Right knee (Tight: too little limb past this joint to click.
  Try a spot further from the end)". Dat is alleen de reden van de laatste noodplek; de echte reden is de overlap op
  de goede plek. Wie het advies volgt (verder van het uiteinde) zoekt op de verkeerde plek. Doorgegeven aan
  Betrouwbaarheid (via de hoofdchat): de reden van de plek op het bot zelf tonen (de eerste kandidaat), niet die van
  de laatste noodplek; nu wint in `rig.py` de melding van de laatste poging (behalve bij `vangnet`).
