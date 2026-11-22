# Fit test strip: gratis STL en tekst (Bram, 22 nov 2026 ±13:20 UTC)

Opdracht Afkijker 22 nov 12:50; plek gekozen door hoofdchat 12:40 (gratis op dortus.com bij Click Joints). Nog niet online: eerst keuring Daan, dan op een tak vanaf b1050f4 in repo dortus.

## Bestanden (in `commercie/blender-click-joints/testprint/`)
- `fit-test-strip.stl`: 10 delen, vijf kogelgewrichten bij 0.10 / 0.15 / 0.20 / 0.25 / 0.30 mm speling. Gemaakt met de echte Pro-code (knop "Fit test: ball", standaardwaarden) in Blender 5.3.0, script `maak_strip.py`. 140 x 52,1 x 44,5 mm, 90,2 cm³ (GEZIEN, trimesh).
- `fit-test-strip-plus-testset.stl`: dezelfde strip plus de 4 delen van `testset-4-delen.stl` erachter, 14 delen, 140 x 84,1 x 44,5 mm (GEZIEN). Voor de echte testprint (keuring C3: één bestand, één keer startgeld).
- Beelden: `beeld/strip-plus-testset-schuin.png` en `-onder.png`.

## Anders dan de knop in Pro (met reden)
- Pro zet het getal in reliëf bovenop deel B. In een printbestand ligt dat eind op het bed, dan hangt het hele deel op 0,6 mm hoge cijfers. Daarom hier het getal 0,6 mm **ingegraveerd**, in het platte eind van **beide** delen (anders weet je na het printen niet welke A bij welke B hoort).
- Klaar om te printen: A staat zoals hij is, B 180 graden gekanteld met het platte eind op het bed (les A4 van de keuring echte print: anders support in de kom). Alle 14 delen waterdicht en op z = 0; overhang per B-deel 4,5 tot 5,4 mm² (alleen de plafonds van de cijfers), per A-deel 47 tot 51 mm² (onderkant van de bol, 44 mm², plus cijfers) (GEZIEN, trimesh).
- Alleen de kogel. Een scharnierstrip kan met dezelfde code (`soort="SCHARNIER"`), als Daan of de hoofdchat dat wil.

## Tekst voor dortus.com (Engels, concept)
**Print this first: which clearance fits your printer?** (De opdracht noemde "±15 min"; weggelaten, want niet gemeten en bij 90 cm³ vast langer, GOK.)

Five ball joints, from 0.10 to 0.30 mm clearance. The number on the flat end of both parts is the clearance in hundredths of a millimetre: 10 means 0.10 mm. Print them as they are in the file, flat end down. No supports. Click each pair together. Use the clearance of the one that turns smoothly without wobble.

Got your number? Click Joints Pro puts that clearance in every joint, with bend range and figures from your rig: [Click Joints Pro](link naar Pro).

Printed it? Email a photo to thijs@dortus.com (subject: Fit test photo) and get a free Pro code.

*Not print tested by us yet.*

## Open
- Printtijd invullen zodra iemand hem slicet.
- Keuring Daan: bestand (vorm, opleggen, cijfers leesbaar) en tekst.

## Na keuring Daan (22 nov, ±15:00 UTC)
- Moet 1 (A3): cijfers nu "10" tot "30" (zonder "0."), Bfont maat 11: 7,6 tot 7,7 mm hoog, 8 tot 10 mm breed op een schijf van 20 mm. Smalste groef in de eerste laag 0,82 mm, geen enkele onder 0,8 mm (was 8 van 40 onder 0,4) (GEZIEN, `meet_strip.py`, doorsnede op 0,3 mm). Beeld: `beeld/strip-cijfers-eerste-laag.png`. Lijnen dikker maken met `offset` in Blender breekt de vorm van de "3" (niet gesloten), daarom groter in plaats van vetter.
- Moet 2 (C1): foto naar thijs@dortus.com, onderwerp "Fit test photo", je krijgt een gratis Pro-code (besluit hoofdchat 13:40).
- Kan C2 meegenomen: "flat end down. No supports." Kan C3 (groeven zijkant) en C4 (beeld in elkaar) nog niet.
- Maat strip nu 140 x 52,4 x 44,5 mm; alle 10 delen waterdicht, op z = 0 (GEZIEN).
