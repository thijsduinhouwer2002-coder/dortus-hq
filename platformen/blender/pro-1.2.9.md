# Click Joints Pro 1.2.9: releasenote (Bram, 25 nov 2026) CONCEPT

**Uitbrengen niet vóór ma 30 nov.** Eerst gaat 1.2.8 vanavond live en loopt de sale (27 nov t/m 1 en 2 dec) op een rustige versie. 1.2.9 voegt geen functies toe: het paneel staat in dezelfde volgorde als bij Cleave en Split 3D Print (vergelijking in `organisatie/lat/click-joints-pro.md`, kop Paneel). Effect op verkoop: GOK, klein; vooral een betere eerste klik voor wie Try it free of een salekoop opent.

## Bewijs
- Code: tak `claude/blender-paneel-1.2.9` (a3c1ea1 t/m c393c55), op 25 nov ±18:20 NL samengevoegd op main.
- Keuring: Daan #83 (punt 2 en 3 ja) en #89 "Akkoord: ja op 1.2.9" (punt 1 beeld 16a, plus "Hinge placed"), cijfer 8 naast Cleave en CatPin.
- E2e 45644233399 op c393c55 groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN, Daan en Bram). Nieuwe e2e op main na deze push; het runnummer voor de zip komt in de stand hieronder.
- Beelden: `producten/blender-gewrichten/keuring/2026-11-25-1.2.8-paneel-voor.png`, `2026-11-25-1.2.9-paneel-na-figuur.png`, `2026-11-25-1.2.9-paneel-rig-boven.png`.

## 1. Winkeltekst (Gumroad én Superhive)
Gelijk aan B3 (`platformen/blender/pro-winkeltekst-b3.md`), alleen versienummer 1.2.8 wordt 1.2.9.

## 2. Releasenote 1.2.9 (Engels, Gumroad en Superhive)
```
Click Joints Pro 1.2.9
- If your mesh has a rig, "Rig found" and the Figure from rig button are now the first thing in the panel.
- The fit test strip now sits right under Clearance, and the hinge buttons sit under Place joint, so every button is in its own step.
- After you place a hinge, step 3 says "Hinge placed" and shows its bend range next to the fit.
- After a Good fit and an export, one small line lets you leave a rating. Click a store or the X and it does not ask again. No popups.
- Coming from the free Click Joints? Just enable Pro: it turns the free version off for you and says so in the panel. Nothing is deleted.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Elke regel zit in de build en heeft een toets in `e2e/toetsen_paneel.py` of een schermbeeld (regel 1: beeld 16a; regel 3: `OK scharnier geplaatst: stap 3 zegt Hinge placed`).

## 3. Update log Superhive (bovenaan erbij)
```
1.2.9 (<dag van upload> Nov 2026): Cleaner panel. Enabling Pro now turns the free Click Joints off for you. With a rig, Figure from rig is now at the top. Fit test strip and hinge buttons moved into step 2, the hinge range into step 3. A small rating line after a good export.
```

## 4. Blok bovenaan Superhive
Kop "New in Pro 1.2.9" met regel 1 tot 3 uit deel 2, daarna "Tested on Blender 4.2 LTS, 5.2 LTS and 5.3."

## Zip
Op 30 nov: `VERSIE` in `.github/workflows/click-joints-pro-uitgave.yml` naar 1.2.9 (nu bewust nog 1.2.8, zodat de plak van vanavond met run 45526260663 werkt), dan de uitgave-run met de groene e2e-run op main. Zware keuring volgens skill `uitbrengen` vóór het plakken.

## Stand
- 25 nov ±18:20 NL: tak op main (11323f7), note concept, keuring van de tekst gevraagd aan Daan (#93).
- 25 nov ±19:05 NL: e2e 45662127816 op main (11323f7) groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN). Dit is de run voor de uitgave-run van 1.2.9, als het artefact op 30 nov nog bestaat; anders een verse run op main.
- 26 nov ±04:40 NL (Bram, #114): regel "Coming from the free Click Joints?" erbij in deel 2 en 3. Code op tak `claude/blender-114` (f43c3c6), toets `(a)` in `e2e/test_betaald.py`, e2e 45747312096 groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN), keuring Daan #138. Na 1.2.9 kan de zin "turn the free one off first" uit de Docs-tab (`superhive/docs-tab-1.2.8.md`).
- 26 nov ±08:50 NL (Bram, #114): op main in 99a3c69, e2e 45773325191 op main groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN). Dit is nu de run voor de uitgave-run van 1.2.9 (vervangt 45662127816). Docs-tab: `superhive/docs-tab-1.2.9.md`, keuring #157.
