# Click Joints Pro 1.2.8: releasenote (1.2.4 tot en met 1.2.8 samen) (Bram, 24 nov 2026)

**Waarom (geld):** 1.2.7 staat nog niet in de winkel (plak do 27 nov). We plakken meteen 1.2.8, zodat een koper die in de saleweek de robot of een figuur met kniekap pakt op het midden van de knie een groen scharnier krijgt in plaats van "Tight". Eén plak, geen tweede ronde. Effect op verkoop: GOK, klein; vooral geen terugbetaling of slechte eerste indruk.

**Verschil met `pro-1.2.7.md` (Daan ja op deel 1 tot 4):** alleen één regel erbij in de note (deel 2, regel 3) en een paar woorden in de update log (deel 3). Kop "1.2.7" wordt "1.2.8". Winkeltekst en blok bovenaan blijven gelijk, op het versienummer na. Alleen die stukken hoeven herkeurd.

## Bewijs
- Knie-fix: Olaf, commits 4e4166a, 23c9bdf, 5090ac8 (nu op main). Oorzaak: de rand van de kniekap telde als onderkant van het been, dus de lip werd te kort en de kleur Tight.
- Code: Daan ja (`platformen/blender/keuring/2026-11-24-pro-1.2.8-knie-daan.md`), toetsregel ja (`platformen/blender/keuring/2026-11-24-pro-1.2.8-toetsregel-daan.md`).
- E2e 45469343573 op 5090ac8: groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN door Olaf in de logs). Nieuwe e2e op main na deze push; de uitgave-run neemt de zip uit die run.
- In 4.2 geeft een knip 12 mm boven het kniemidden van de robot een nette melding ("the mesh is unchanged"); 1.2.7 doet daar precies hetzelfde (GEZIEN door Olaf, lokaal 4.2.23). Geen nieuwe beperking, dus geen zin in de note.

## 1. Winkeltekst (Gumroad én Superhive)
Gelijk aan `pro-1.2.7.md` deel 1.

## 2. Releasenote 1.2.8 (Engels, Gumroad en Superhive)
```
Click Joints Pro 1.2.8
- "More bones" now gives ankles: a hinge from shin to foot that bends 0 to 90 degrees, while the knees keep their own range. Works on human figures and on blocky feet, like a robot. Needs Blender 5.2 or newer for both ankles; in 4.2 one or both may be skipped, each with the reason shown.
- Shift + right click on the skin now works with Knee, Elbow, Ankle and the hinge buttons.
- A knee with a kneecap, like the robot's, now gets a hinge with a good fit right in the middle of the knee. Before, it said Tight there.
- When Figure from rig cannot cut a joint, the list now shows the real reason and what you can do, instead of "Try a spot further from the end".
- Figure from rig on Blender 4.2 LTS now needs far less memory. Before, on some figures it could fill all memory at the elbow and freeze Blender.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Nieuw is alleen regel 3, en sinds 25 nov regel 5 (geheugen in 4.2, issue #14: vóór de fix boven 15 GB in CI, nu piek ±2,5 GB lokaal en 4,6 GB in CI-run 45526260663 op dezelfde figuur, GEZIEN; keuring in #37). De andere regels staan letterlijk zo in `pro-1.2.7.md` (Daan ja).

## 3. Update log Superhive (bovenaan erbij)
```
1.2.8 (<dag van upload> Nov 2026): "More bones" now gives ankles on human figures and blocky feet (Blender 5.2+). Shift + right click on the skin now works with Knee, Elbow, Ankle and the hinge buttons. A knee with a kneecap now gets a good fit in the middle. Clearer reason when Figure from rig cannot cut a joint. Figure from rig needs far less memory on Blender 4.2.
```
Geen aparte regel voor 1.2.7: die stond nooit in de winkel.

## 4. Blok bovenaan Superhive
Als `pro-1.2.7.md` deel 4, met kop "New in Pro 1.2.8" en als regel 3 erbij:
```
- A knee with a kneecap, like the robot's, now gets a good fit in the middle of the knee.
```
(regel "Tested on ..." schuift naar 4).

## Zip
Uitgave-run `click-joints-pro-uitgave.yml` (VERSIE 1.2.8) met de groene e2e-run op main. Zip als artefact `click-joints-pro-zip-1.2.8`, 3 dagen bewaard. Run-nummer: zie de stand hieronder.

## Stand
- 24 nov ±22:40 NL: 1.2.8 op main gezet (cherry-pick van de tak, Daan ja op code en toetsregel). Note klaar, keuring van regel 3 en de update log gevraagd aan Daan.
- 25 nov ±02:45 NL: fix geheugen Rigify-elleboog in 4.2 (ook in 1.2.7 aanwezig) op main, 95a72a4; regel 5 in de note en een zin in de update log erbij, nakeuring M1, M2 en die regel in #37. E2e 45526260663 groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN), army_man KLAAR 0 FOUT in 4.2, piek Rigify 4614 MB.
