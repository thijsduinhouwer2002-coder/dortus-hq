# Figure from rig op drie nieuwe AI-figuren (Pro 1.2.0, Blender 5.3.0, 23 nov, Olaf)

Opdracht hoofdchat 23 nov: werkt Figure from rig op AI-gemaakte figuren, waar valt een gewricht weg?
Figuren: Meshy, Hugging Face-set tfnn/MESHY.AI_800 (MIT), map people: `businessman`, `spacetrooper1`,
`man_cap_jeans_jacket` (nog niet in de e2e). Elk 150 mm, Make watertight, rig met Mixamo-namen uit doorsneden
(`e2e/proef_meshy_rig.py`), alle gewrichten. Zip gebouwd van main 2698411 (`PRO_VERSIE=1.2.0`). Lokaal gedraaid,
log in `log.txt` (GEZIEN). Ook gedraaid met `CJ_HEUP_PCT=52` zoals de e2e: zelfde uitslag op de heupen na
(man_cap linkerheup dan "too close to another joint, keep 21 mm apart").

| Figuur | Gewrichten erop | Weggevallen (reden van de add-on) | Ligt aan |
|---|---|---|---|
| spacetrooper1 (dikke pantserbenen) | 1: nek (preset) | beide knieën "Tight: cheek too stiff to click. Try a thicker spot"; beide heupen "no clean spot for a hip ball"; linkerelleboog "joined to another part" (arm ligt tegen de heup, terecht); linkerschouder "outside the mesh" | knieën: **add-on** (zie onder); schouder: onze proefrig; elleboog: terecht |
| man_cap_jeans_jacket | 2: linkerknie 0-120 from rig, rechterknie mirror | nek "too thin"; linkerheup "no room on this 21 mm bone ... next to the knee"; rechterheup "only a tiny ball fits here" | heupen: korte dij plus onze heupplek; nek: dunne nek, terecht |
| businessman (lange jas tot de grond) | geen rig mogelijk | benen zijn één blok tot de voeten (doorsnede op 5 tot 35% is één lus van 50 tot 70 mm) | het model, niet de add-on |

## Wat opvalt
1. **Knie op een dik been geweigerd met een verkeerde tip** (spacetrooper1, beide knieën). `scharnier_neus.maten_neus`
   geeft TIGHT als de rek van de wang te hoog is; met een dik been is de wang `t = wx - tw - s` juist dik. "Try a
   thicker spot" stuurt de koper dan de verkeerde kant op. GOK: hier is de dikte de oorzaak, of een korte sleuf door
   `zaag_diepte`. Beeld: `spacetrooper1_gesloten_rig-voor.jpg` en `-zij.jpg`.
2. **Heupen vallen bij AI-figuren bijna altijd weg** (5 van 6 hier; in de e2e al eerder zo bij korte dijen). Elke
   reden is leesbaar, er gaat niets kapot (alle delen gesloten, elk één stuk, GEZIEN in het log).
3. **Proefscript draaide de figuur fout**: `proef_ai_model.laad` neemt aan dat elke Meshy-figuur naar +x kijkt;
   man_cap keek opzij, dan kwamen de beenbotten midden in de figuur (`man_cap-zonder-draai-voor.jpg`). Nieuw
   `e2e/proef_ai_figuren.py` draait de figuur na Make watertight zo dat de benen op de x-as staan en de tenen naar -y.
   Daarna kreeg man_cap beide knieën. Een koper die zelf rigt, heeft dit probleem niet.

## Opnieuw draaien
```
bash e2e/maak_zip.sh betaald   # met PRO_VERSIE=1.2.0
blender -b --factory-startup --python e2e/proef_ai_figuren.py -- /tmp/click_joints_betaald.zip uit <glb's>
blender -b uit/<naam>_rig.blend --python e2e/kijk_figuur.py -- uit
```
