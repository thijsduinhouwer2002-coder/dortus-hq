# Figure from rig op de studio-figuren (Pro 1.2.0, 23 nov, Olaf)

Opdracht hoofdchat 23 nov: werkt Figure from rig op de figuren van de nieuwe studio, waar valt een gewricht weg?
Bron: release `studio-1` (workflow `studio.yml`, 23 nov 11:52 UTC): `kandidaten.txt`, `proef-<model>.log`,
`studio-figuur-a.log`, `figuur-a-meting.json` en de beelden (GEZIEN, alles gelezen). Zes kandidaten, elk Make watertight,
eigen rig van het model, alle gewrichten. Alle delen bleven één stuk (GEZIEN, `stukken` in kandidaten.txt), op de robot na.

| Figuur | Hoogte | Gewrichten | Weggevallen (reden van de add-on) | Ligt aan |
|---|---|---|---|---|
| makehuman-kleding (= figuur a en b van de filmpjes) | 220 mm | 8 van 9 | linkerschouder: "The cut gave no watertight parts (bad edges: part A 1, part B 0)" | **add-on** (zie 1) |
| adventurer | 260 mm | 4 (ellebogen, knieën) | nek "not placed"; schouders "no room on this 25 mm bone"; heupen "no room on this 61 mm bone ... next to the knee" | nek: **add-on** (zie 2); schouders: korte arm, terecht; heupen: grensgeval (zie 4) |
| king | 260 mm | 4 | knieën "joined to another part on both sides" (mantel tot de grond); nek "not placed"; schouders 25 mm | knieën: terecht; nek: **add-on** |
| medieval | 260 mm | 4 | nek "not placed"; schouders "only a tiny ball fits"; heupen "too close, keep 46 mm" | nek: **add-on**; knieën geplaatst met wand 0,84 tot 0,98 mm (melding Tight, zie 5) |
| knight | 240 mm | 3 | linkerknie "Tight: cheek too stiff ... Try a thicker spot"; nek 14 mm bot; schouders en heupen geen ruimte | knie: **add-on** (zie 3) |
| robot-expressive | 240 mm | 0 | alle 4 scharnieren "Tight: cheek too stiff ... Try a thicker spot"; schouders, heupen, nek | **add-on** (zie 3), model in 5 stukken |

## Wat Bram moet weten
1. **Linkerschouder valt weg op het filmfiguur** (beeld `figuur-a-lijst-linkerschouder-weg.jpg`: rechts in beeld alleen
   140° bij de elleboog, geen kogel). De rechterschouder lukt wel (±25°). De kern geeft "no watertight parts" en
   `rig.py` probeert dan geen volgende plek: `verder` (r746) gaat alleen door bij "too close" of bij thin/tight op een
   scharnier. Voorstel: ook bij "no watertight parts" de volgende kandidaat van `kogel_schuif` proberen. In elk filmpje
   met figuur a mist nu een schouder.
2. **"Neck (not placed)" zonder reden** op 4 van 6 figuren. `kogel_reden` (r205) maakt alleen voor HIP en SHOULDER een
   leesbare zin van "nothing was cut"; de nek valt erdoorheen en dan zet r767 "not placed". Voorstel: een NECK-zin,
   bijvoorbeeld "no clean spot for a neck ball (neck too short or thin), place it by hand".
3. **"Tight: cheek too stiff ... Try a thicker spot" op dikke ledematen**: nu op robot (4 keer), knight en eerder
   spacetrooper1 (`proeven/ai-figuren-2026-11-23/uitslag.md`). Drie figuren, steeds dikke benen of armen. De tip
   stuurt de koper de verkeerde kant op. GOK: de rek van de wang wordt te hoog als de wang dik is; dan moet de wang
   dunner of de tip anders.
4. Heup op een dij van 61 mm: nodig 49 mm, grens 0,8 x 61 = 48,8 mm in `geen_ruimte`. Net erover, dus "no room". Klopt
   met de regel, maar op een dij van 61 mm verwacht een koper wel een heup. Lage prioriteit.
5. Medieval: knieën geplaatst met wand onder 1 mm en melding "Tight: wall 0.84 mm". Eerlijk gemeld, maar zo'n knie breekt
   bij het printen. Geen fout, wel iets voor de filmpjes: kies dit figuur niet.

## Voor de filmpjes
Alleen makehuman-kleding geeft een vol figuur (8 gewrichten). De Quaternius-figuren (adventurer, king, medieval, knight)
hebben korte armen en krijgen alleen ellebogen en knieën. Robot niet gebruiken.
