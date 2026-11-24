# Pro-Short: Already split your figure? Add a working knee in Blender 🦿

- status: open
- kanaal: yt-short
- soort: video
- soort_reeks: Pro (eigen onderwerp: model dat al in delen is, knie op de 3D-cursor; geen Short van de laatste 14 dagen over losse delen of Shift + rechtsklik)
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-24/pro-al-gesplitst-geluid.mp4 (workflow regisseur-24, run 45454633029, commit ca93244)
- saleversie: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-24/pro-al-gesplitst-sale-geluid.mp4, slotzin "Click Joints Pro, 25% off this week, on Gumroad." Alleen do 26 nov avond tot en met di 1 dec en alleen als CYBER25 aanstaat; daarna de gewone versie.
- stem: nu Kokoro (Apache 2.0) als proef. **Niet plaatsen zonder Max** (hoofdchat 24 nov 18:05): de opname staat op de lijst `commercie/filmpjes/stem/opnames-vanavond.md`; zodra `pro-al-gesplitst-elevenlabs.mp3` in deze map staat bouwt de workflow beide versies opnieuw (saleversie via `stem/slotzin-sale-elevenlabs.mp3`). Beeld kan de Keurder nu al keuren.
- stem_tekst: `commercie/filmpjes/regisseur-24/pro-al-gesplitst-stem.txt` (sale: `pro-al-gesplitst-sale-stem.txt`)
- figuur: eigen robot van studio-3 (`commercie/filmpjes/studio/figuur_robot.py`), in losse delen gesneden in Blender; geen licentie van derden
- lengte: 45,6 s gewoon, 47,4 s sale (ffprobe, GEZIEN)
- geluid_check: GOED, -16,4 dB, piek -1,4 dB (GEZIEN, ook in CI)
- synchroon: 12 van 13 binnen 0,3 s volgens whisper; zin 9 meet -0,6 s, maar dat is een fout van whisper: met RMS nagemeten stopt zin 8 op 28,9 s, stilte tot 29,45 s, zin 9 begint op 29,5 s en de scène op 29,4 s, dus 0,1 s (GEZIEN, run 27). Zelfde -0,6 s met twee verschillende teksten voor zin 9, dus het ligt aan het uitgesproken getal in zin 8. Met de Max-opname wordt opnieuw gemeten.
- beelden: 14 zelf bekeken (GEZIEN). Eerste beeld groot: studio-render van de robot met de knie gebogen, kop "Can it still bend?", geen getallen. Daarna echte Blender: robot in drie delen, klik op het been, opzij, Shift + rechtsklik zet de cursor op de knie, Knee in Figure joints, scharnier met "Knee 0-135°", Show bend range met de groene boog, render als slot. Scène 11 was een te krappe close-up met de kop op de donkere robot; nu de hele robot.
- tijd: voorstel in de saleweek, bijvoorbeeld 2026-11-28T17:00:00+01:00 met de saleversie (Pro-Short, geld nu). De hoofdchat kiest.
- doel: Gumroad via de naam in beeld en stem (geen link uitgesproken)
- gemaakt_door: Regisseur run 26 en 27 (24 nov 2026)

## Titel
Already split your figure? Add a working knee in Blender 🦿

## Tekst
```
Already cut your figure into parts with another tool? Keep the parts.
1. Click the leg you want to bend.
2. Look from the side, then Shift + right click on the knee to put the 3D cursor there.
3. In Click Joints Pro, open Figure joints and click Knee. Show bend range shows how far it swings.
Elbow and Ankle work the same way.

Every printer is different. Print a test joint first.
Click Joints Pro, on Gumroad.
```

## Voice-over (zin voor zin, Engels)
1. Already split your figure? Can that knee still bend?
2. This robot is already in parts: a body and two separate legs.
3. Click the leg you want to bend.
4. Turn the view to the side. The hinge turns around the way you look.
5. Shift and right click on the knee. The 3D cursor jumps there.
6. In Click Joints Pro, go to Figure joints and click Knee.
7. It cuts the leg in two and builds a hinge right at the cursor.
8. The panel shows how far it bends: zero to one hundred and thirty-five degrees.
9. Next, turn on Show bend range to see the whole swing.
10. Elbow and Ankle work the same way.
11. Your parts stay just as they are. Now that knee can bend.
12. Every printer is different. Print a test joint first.
13. Click Joints Pro, on Gumroad.

## Bronnen (alleen voor de keurder, niet voor kijkers)
- Zin 1, 2, 11: "Already split your model into printable parts with another tool? Keep those parts. Open one, put the 3D cursor on the knee or elbow, and Click Joints Pro cuts a hinge or a ball joint right there" (`platformen/blender-2/gumroad-1.1.md` r. 31). In beeld: de robot in drie losse objecten (Body, Leg.L, Leg.R), elk gesloten (film.json `delen_na_splitsen`, GEZIEN).
- Zin 4 en 5: "Shift + right click on the skin now works with Knee, Elbow, Ankle and the hinge buttons" (`platformen/blender/pro-1.2.7.md` r. 23); de scharnieras is de kijkrichting (bericht Olaf 24 nov 16:50 in `berichten/regisseur.md`; eigenschap "Axis: View direction" in `producten/blender-gewrichten/click_joints/eigenschappen.py`).
- Zin 6 en 7: knop Knee onder Figure joints (`betaald/figuur.py`, PRESETS); uitkomst in de opname: MELDING (film.json, GEZIEN).
- Zin 8 en 9: knop "Show bend range" in de opname aangeklikt, `toon_bereik` aan (film.json, GEZIEN).
- Zin 10: Elbow en Ankle: pro-1.2.7.md r. 23 en gumroad-1.1.md r. 42 (zes presets).
- Zin 12: vaste eerlijkheidszin (besluit Thijs 24 nov 15:32, geen "not print tested").
- Zin 13: slotzin (opdracht hoofdchat 24 nov 16:05, ja Thijs 15:59).
- Geen prijs, geen "holds a pose", geen bewering dat wij geprint hebben of dat het klikt. Opname met Pro 1.2.7 van main (de versie die naar de winkels gaat, pro-1.2.7.md).

## Licenties
- Stem: Kokoro-82M v1.0, stem af_heart (Apache-2.0, hexgrad/Kokoro-82M; kokoro-onnx MIT).
- Figuur: eigen robot (studio-3), geen licentie van derden. Software in beeld: Blender 5.3.0 (GPL) met Click Joints Pro 1.2.7 (van ons).
