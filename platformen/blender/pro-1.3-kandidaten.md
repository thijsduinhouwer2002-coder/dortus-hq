# Click Joints Pro 1.3: kandidaten (Bram, 23 nov 2026)

Toets: brengt het binnen weken geld op? Kopers printen vaak gestileerde figuren (game-stijl, chibi, ridders). Faalt Figure from rig daarop, dan is dat een terugbetaling of een slechte review.

## Al gebouwd (tak `claude/blender-solver-terugval`, komt in 1.2.2 of 1.3)
- Open deel na de Manifold-snede: één keer opnieuw snijden met Exact voor de fout "no watertight parts" (spoor Olaf 23 nov, 8 tegen 9 gewrichten). Toets `solver_terugval` in `e2e/toetsen_correcties.py`.

## Kandidaten, op volgorde van geld
1. **Gestileerde figuren met korte dikke ledematen** (les hoofdchat 23 nov, `commercie/filmpjes/studio/LEESMIJ.md`): Quaternius Knight 3 gewrichten, Adventurer 4, Medieval 4, King 4, RobotExpressive 0 (GEZIEN door de hoofdchat). Oorzaken: bovenarm te kort voor een kogel, mantel verbindt de knieën.
   - a. Bij een te kort lid automatisch een kleinere kogel proberen (de auto-diameter heeft al een ondergrens; die per lid laten zakken tot de wand nog Good fit haalt).
   - b. Lukt geen kogel: een scharnier voorstellen voor elleboog en knie (scharnier bestaat al in Pro).
   - c. Altijd een duidelijke regel in de lijst per overgeslagen gewricht: "upper arm too short for a ball, try a smaller diameter or a hinge" en "legs joined by a cloak or robe, split the mesh first".
   - Toets: de vijf Quaternius-figuren (licentie CC0, nakijken en in het verslag zetten) in de e2e, telling gewrichten per figuur vastleggen en omhoog krijgen.
2. **Volgende kandidaat bij "no watertight parts"** in `rig.py` (`verder`): de volgende plek van `kogel_schuif` proberen (Olaf).
3. **NECK-zin** en tip bij dikke ledematen (Olaf, ochtend 23 nov).
4. Kan's van de automatische keurder (13:37): materiaalindex per vlak niet als lijst op het object bewaren; echte telling in `selected_ok`.
5. **Kapotte snede zelf herstellen (A4 keurder, advies Olaf 23 nov 17:45):** direct na elke kogelsnede in Figure from rig de overlap in rust meten en bij een kapotte snede die snede met Exact overdoen, in plaats van de plek te verschuiven. De 0,3 mm-plek van 6dcadc8 is geluk, geen vangnet (toets `CJ_HERKANS=2` lukt op geen enkel lid, GEZIEN door Olaf). Toets `CJ_HERKANS=2` gaat de e2e in zodra dit groen maakt.

## Volgorde
Eerst e2e groen op de tak met de terugval, dan 1a+1c (meeste winst voor kopers), dan 2. Elke stap met keuring door Daan.
