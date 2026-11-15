# Kleur H in hol.py (Mila, 15 nov 2026)

Opdracht: Daan 15 nov 13:05 (punt 1 van Thijs, minder paars en donker). Tak `claude/steam-hol-kleur-h`.

Wat er in `producten/steam-hol/modellen/hol.py` veranderde, precies de kolom "doel H" uit `ontwerp/steam/kleur-warm/LEESMIJ.md`:
aarde 684033 / 8e5949, achterwand a26a58, pruim_d 5a3227, steen c69383, schachtwand 8a5342, vloer d0947c, kamerwand b88168, putrand 6e4e44.

Eén eigen keus: **het kamerhout (STUT: stutten, ton, houweelsteel, kistje) van 6e4632 naar 34180e**, donkerder en roder. Waarom: in de eerste render met H verdween het hout bijna in de lichte warme kamerwand (de stutten lazen als een vage tekening op de muur). Met 4e2818 nog te zwak, met 34180e staat het los. De ladder (HOUT_F) en de kist (HOUT) blijven, die lezen tegen de schacht en de schatkamer.

GEZIEN met Read, lokale render (Blender 5.2.4, 16 samples, 1920x320, zelfde camera):
- `oud-boven-H-onder-1920.png`: main nu boven, H onder.
- `H-ware-grootte-120.png`: H verkleind naar 720x120. Gloop springt eruit, de gang blijft een trede lichter dan de aarde, de stekels in de zwarte put lezen.
- `H-kamer-hout-uitsnede.png`: kamer met het donkere hout.

Eerst gezien: de schatkamer is met het warme licht erg licht geel geworden (de gouden berg valt minder op tegen de wand dan bij pruim). Eerst keurt Daan op 96, 120 en 160 uit de Windows-build; is de schat te zwak, dan maak ik de schatkamerwand een trede donkerder.

**Daarna (15 nov ±15:05): schatkamerwand 9e6a56 in plaats van b88168.** Lokaal gerenderd en blind voorgelegd aan een frisse kijker (`schatkamer-links-9e6a56-rechts-b88168.png`, plus beide op 720x120): 9e6a56 eruit springen 7, rijk en warm 9 (samen 16); b88168 8 en 6 (samen 14, "bleker en wat poederig"). Gekozen: 9e6a56. De wand blijft het lichtste vlak door de gloed achter Gloop.
