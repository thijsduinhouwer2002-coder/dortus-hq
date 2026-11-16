# Graven en vangsten: vangt een graver minder? (Bram, 16 nov 2026 ±20:30 UTC)

Vraag van Sanne (16 nov 20:10, `berichten/bram.md`): in Olafs koper-duurtest (run 43939923957, `koper=1`, 20 min) ving het hol 9 van 28 helden en het gewone spel 18 van 28. Komt dat door de lange gang met kamers?

## Hoe gemeten

Het echte spel (main aa3b7bb, Godot 4.3 voor Linux) zonder scherm: `godot --headless --fixed-fps 10 --path producten/steam-hol/godot -- hoogte=120 vers=1 zaad=<n> duur=1230 [koper=1]`. Zonder scherm is de breedte 0, dus lokaal (niet gecommit) in `kern/strook.gd` de schermmaat op 1920 x 1040 gezet als hij 0 is; dan is het hol gelijk aan de CI-run (640 x 40 spelpixels, ingang 19, put 24, Gloop 27, schat 29). In `held.gd` lokaal een printregel bij elke worp, bij aankomst bij de schat en bij het einde van elke held. Twee omgevingsvariabelen scheiden graven en kopen (`DIAG_GRAAF=0` koopt alleen, `DIAG_KOOP=0` graaft alleen). Per variant 30 zaden van 20,5 min. `tel.py` hiernaast telt de uitvoer.

## Uitkomst (GEZIEN, gemiddelde over 30 zaden)

| Variant | helden | gevangen | weg | bij de schat | put raak / worpen | Gloop raak / worpen | kopen |
|---|---|---|---|---|---|---|---|
| gewoon spel | 26,8 | 13,9 | 12,9 | 3,7 | 9,5 / 26,9 | 4,5 / 10,2 | 0 |
| alleen kopen | 26,9 | 15,0 | 11,9 | 3,3 | 9,1 / 27,0 | 5,7 / 10,8 | 1,9 |
| alleen graven (41 keer, zoals de koper) | 26,2 | 14,1 | 12,1 | 3,0 | 9,2 / 26,6 | 4,6 / 10,1 | 0 |
| koper (graven en kopen) | 26,2 | 15,3 | 10,9 | 3,0 | 9,7 / 26,5 | 5,5 / 10,3 | 2,0 |

Spreiding gevangen per 20 min: gewoon 8 tot 20 (mediaan 13,5), koper 10 tot 22 (mediaan 15). Op 6 en 4 beelden per seconde hetzelfde (koper 10 tot 19 en 12 tot 18). Met het zaad van de CI-run (1794857447, zelfde helden in dezelfde volgorde) 12 keer opnieuw: 12 tot 18 gevangen, nooit 9.

**Conclusie: de lange gang zelf geeft geen minder vangsten.** Elke held gooit nog steeds één keer bij de put en één keer bij Gloop; de gang is alleen langer lopen. De CI-run was pech aan twee kanten tegelijk: de koper zat onder de laagste van mijn 30 runs en het gewone spel (18) bijna bovenaan. In de CI-log vallen alle zes aanrakingen van de schat in een tijd dat Gloop plat lag (Gloop lag 8 keer 60 s plat, ±40% van de run); geen enkele held liep langs een staande Gloop.

## Wel een echte fout gevonden

Een held kijkt alleen in de kolom waar hij na elk beeld staat. Na een hapering (één beeld van meer dan ±1,6 s) loopt hij in één keer meer dan 16 pixels en springt hij over een hele kolom, dus over de put of Gloop heen, zonder worp. Toets: met beelden van 2,5 s gooide hij bij 6 van 9 vallen. Opgelost op tak `claude/steam-hol-haper` (bdc9c4a): lopen in stukjes van hooguit 8 pixels met na elk stukje een blik; gewoon lopen (1 of 2 pixels per beeld) is één stukje, dus verandert er niets. Toets erbij, alle toetsen 0 FOUT lokaal. In de CI-run zie ik geen sprongen (alle schat-aanrakingen vielen bij een platte Gloop), maar graven maakt het spel zwaarder (CPU 1,23, `hol_vast` groeit), dus een hapering bij een graver is precies waar dit zou toeslaan.

## Wat graven wel kost

- Iets minder helden per 20 min (26,2 tegen 26,8): een vluchtende held doet langer over de terugweg en telt mee in de grens van 3 tegelijk.
- Graven levert verder niets op voor het vangen. Sanne's eis "graven nooit minder" haalt het nu net (14,1 tegen 13,9), maar graven voelt als vooruitgang zonder dat het iets doet. Voorstel aan Sanne (haar keus): de langere gang laat helden vaker twijfelen bij de schat, of een kamer geeft een kleine kans erbij voor de dichtstbijzijnde val, zodat graven iets bijdraagt.
