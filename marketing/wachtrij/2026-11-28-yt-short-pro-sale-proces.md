# Sale-Short Click Joints Pro (procesvorm): From rig to poseable figure in Blender 🤖

- status: GEKEURD, Daan ja 8 (#199, 26 nov 16:55 NL); klaar om te plakken na het zien door Thijs en alleen als CYBER25 aanstaat. Versie v6b (Regisseur 26 nov ±17:30 NL): alleen Daans kan-punt verwerkt, pilletje 'Figure from rig' staat tot 7,0 s in plaats van 7,3 s; beelden 7,0 tot 7,27 s veranderd, de andere 726 beelden gelijk aan de gekeurde v6 (GEZIEN, vergelijking per beeld). Eigen controle (GEZIEN): 24,5 s, 1080x1920, 30 bps, 735 beelden elk 1/30 s uit elkaar, geluid_check GOED (gemiddeld -14,0 dB, piek -1,5 dB), 16 beelden plus het eerste groot bekeken. Eerste beeld ongewijzigd, GESLAAGD (`organisatie/blindtest/uitslag/pro-sale-proces-2026-11-26-1519.md`)
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- issue: #159
- bestand: `marketing/wachtrij/2026-11-28-yt-short-pro-sale-proces.mp4` (1080x1920, 30 beelden per seconde)
- vorm: opbouw en tempo van het voorbeeld dat Thijs stuurde (26 nov 08:48): seconde 0 al in Blender met een grijze robot die beweegt, dan elke ±0,5 tot 1,4 s een echte stap (rig, Figure from rig, Exploded view, knie tot de stop en rood erna, kleuren met de shader-editor, tijdlijn, Render Animation), daarna 7 s de mooie eindfilm met de saleregel. Hun beelden en hun geluid zitten er niet in, alleen de opbouw.
- beeld: echte schermopname van Blender 5.3.0 met Click Joints Pro 1.2.8 en de eigen robot, workflow `regisseur-28` run 45831687011 (release regisseur-28), script `commercie/filmpjes/regisseur-28/proces.py`. Opgenomen beeld voor beeld op een eigen klok: per 1/30 s zet het script de echte muis (xdotool), tekent Blender het hele venster echt en wordt dat scherm gepakt; echte kliks op robot, Figure from rig, Exploded view, onderbeen, Bend (typen), tabblad Shading, tabblad Layout, sleep van de afspeelkop, Render > Render Animation (alles gevonden, geen vangnet in film.json). Eindfilm: Cycles-render door de studiocamera uit dezelfde scène (210 beelden), langzaam ingezoomd in de montage. Montage: `commercie/filmpjes/regisseur-28/proces-v6.json` met `montage_proces.py`, 14 stukken, staptekst in beeld: Figure from rig, Exploded view, Ball joints, Hinge from your rig, Knee stops at 120°, Past the stop: red, Add color, Pose it, Render
- geluid: geen stem; alleen muziek met vrije licentie (Kevin MacLeod, incompetech.com, CC BY 4.0, naam van het stuk hieronder in de tekst) en zachte klikjes op de echte kliks
- slot: "Click Joints Pro, 25% off this week, on Gumroad" in beeld
- plaatsen: alleen tussen vr 27 nov en di 1 dec, en alleen als CYBER25 aanstaat (`bash platformen/blender/sale-controle.sh`); Thijs ziet hem voor hij online gaat (issue #159)

## Titel
From rig to poseable figure in Blender 🤖 | Click Joints Pro

## Tekst
```
Rig in, poseable figure out. Click Figure from rig in Click Joints Pro: knees and elbows get a hinge that stops at the rotation limit of your rig, shoulders, hips and neck get a ball joint. Exploded view shows how the parts fit; past the end stop, red shows where parts would hit.

Print the Fit test strip first: every printer is different.
Click Joints Pro, 25% off this week (until Tuesday December 1, 23:59 CET):
https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25?utm_source=yt&utm_medium=video

Music: "Inspired" Kevin MacLeod (incompetech.com), licensed under Creative Commons: By Attribution 4.0, https://creativecommons.org/licenses/by/4.0/
```
