# Figure from rig op drie AI-figuren: tak betrouwbaar-rig tegen main (Blender 5.3.0, 24 nov, Olaf)

Waarom: tweede bewijs voor Pro 1.2.3, op figuren buiten de testset van Betrouwbaarheid. Zelfde drie Meshy-figuren als
`../ai-figuren-2026-11-23/` (businessman, spacetrooper1, man_cap_jeans_jacket), zelfde script `e2e/proef_ai_figuren.py`.
Zips: tak `claude/betrouwbaar-rig` op 25efd95 (`PRO_VERSIE=1.2.3`) en main op e5d8dc4 (`PRO_VERSIE=1.2.0`). Lokaal,
Blender 5.3.0, elk een eigen gebruikersmap. Logs: `log-tak.txt`, `log-main.txt` (GEZIEN).

| Figuur | main | tak | Verschil |
|---|---|---|---|
| spacetrooper1 | 1 gewricht (nek), 6 overgeslagen | 1 gewricht (nek), 6 overgeslagen, zelfde redenen | geen |
| man_cap_jeans_jacket | 2 (beide knieën), 3 overgeslagen | 2 (beide knieën), 3 overgeslagen, zelfde redenen | geen |
| businessman | geen rig (benen één blok, ligt aan het model) | idem | geen |

Alle delen gesloten en elk één stuk, op beide.

## Wat dit zegt
1. **Geen achteruitgang** op deze drie figuren: elk overgeslagen gewricht en elke reden is gelijk.
2. **Ook geen winst** hier: de winst van de tak zit in armen en benen dicht tegen het lijf (testset); deze figuren vallen
   om andere redenen weg (heupplek, dik pantser, de proefrig). Dus in de releasenote "on our test figures" laten staan;
   niet beloven dat elk figuur nu alle gewrichten krijgt. Past bij het concept van Bram.
3. Open punt van 23 nov blijft: de knieën van spacetrooper1 (dik pantserbeen) vallen weg met "Tight: too little limb
   past this joint"; het onderbeen is lang genoeg, dus de tip klopt hier GOK niet. Niet voor 1.2.3, wel voor later.
