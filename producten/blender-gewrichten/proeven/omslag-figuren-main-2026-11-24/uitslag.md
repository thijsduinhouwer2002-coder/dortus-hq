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
3. De releasenote "on our test figures" klopt; voor 4.2 niet beloven dat elk figuur alles krijgt.
