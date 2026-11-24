# Zes Short-scripts Click Cuts, lanceringsweek (vanaf ma 30 nov 2026)

Door Sanne, 24 nov 2026. Waarom: Click Cuts gaat in de week van 30 nov live op Superhive en Gumroad (opdracht hoofdchat aan Chris, 24 nov 04:25) en er lag nog geen enkel filmscript voor. Zonder Shorts op de lanceringsdag missen we de eerste kopers; dit is het werk met de kortste weg naar geld (hoofdzaak 19 nov). Opdracht hoofdchat 23 nov ±12:05 en ±12:45 NL (recept v3: hook eerst).

Bouw zoals week 48 tot 51: zin 1 = hook A of B, max 7 woorden, een vraag (of korte stelling) over het probleem van de kijker, nooit de productnaam; daarna zinnen van 10 tot 16 woorden (4 tot 6 s); printzin altijd; geen AI of stem in titel of beschrijving, alleen het vinkje "Altered content" (besluit Thijs 23 nov 20:28 NL); kop korter dan de gesproken zin; stijl A (Pop) voor Shorts (besluit 23 nov ±17:45: kobalt studio, felle kleur per stuk).

Bron: de kandidaat 1.0.0, GEZIEN op main 8f5db37: `producten/blender-splitser/CHANGELOG.md` en de code in `producten/blender-splitser/split_joints/` (regels per script). Beelden: release `splitser-merk-1` (Lion Head van Poly Haven, CC0, stukken in kleur), release `splitser-kern-1` en tak `schermen` map `blender-splitser/main/` (Suzanne, vaas, schedel in Exploded view, close-up snijvlak, `paneel-x.png`, `paneel-meer.png`, `passing-1.png`, `passing-2.png`).

**Stand: concept, ligt bij Daan voor keuring. Pas na een ja naar de Regisseur. Alleen plaatsen als Click Cuts echt live is (link in de beschrijving moet werken).**

## Vaste regels voor alle zes
- **Prijs niet uitspreken.** De prijzen zet Thijs zelf (voorstel $19 tot 14 dec staat bij Chris, nog niet vast). Eindkaart zonder bedrag.
- **Geen print-belofte.** Wij hebben nog niets met Click Cuts geprint. Printzin: "Measured in Blender, not print tested by us yet. Print the fit test first." (script 2 maakt die zin waar: de fit test is de eerste print).
- **Geen klikverbinders, magneten of "snap"**: de kandidaat maakt alleen ronde pennen (opdracht Chris punt 4). Ook niet "click" als werkwoord: de naam Click Cuts is goed, "it clicks together" niet.
- **Eindkaart** (zin 9): "Click Cuts for Blender. Link in the description." met kop "Click Cuts" en het icoon (`merk/icoon-512.png`). De eerste regel van de beschrijving is de winkellink zodra die er is (de Regisseur vult hem in na de uitgave).
- **Volgorde:** 1, 2, 3, 6, 4, 5. Script 1 op de lanceringsdag (de belofte in één keer), 2 de dag erna (het bezwaar "past het wel"), daarna de rest. 4 en 5 laten allebei zien wat de add-on tegenhoudt; niet op dezelfde dag.
- **Hooksoorten:** probleem (1A, 2A, 3A, 4A, 6A), oude manier (1B, 6B), "al gebeurd?" (2B, 3B, 5A), verrassing (4B, 5B).

---

## 1. Te groot voor je printer? Eén knop
Titel: Model too big for your printer? Split it to fit 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 1A | Model too big for your print bed? | Too big to print? | Lion Head in Blender, het printbed (A1 mini) als doos eromheen, de kop steekt er rood bovenuit |
| 1B | Still cutting big models by hand? | Still cutting by hand? | zelfde kop met één scheef handmatig snijvlak, rood |
| 2 | Pick your printer from the list, or type in your own bed size. | Pick your printer | keuzelijst "Your printer" open, muis op Bambu Lab A1 mini |
| 3 | Then press Split to fit, the one big button in the panel. | Split to fit | muis klikt op de opgelichte knop (`paneel-x.png` als voorbeeld) |
| 4 | It cuts the model into the fewest parts that each fit your bed. | Fewest parts that fit | Exploded view, elk stuk een eigen felle kleur |
| 5 | Every cut gets pins and pin holes, with clearance for your printer. | Pins and holes | close-up snijvlak met gaten, pennen ernaast |
| 6 | The panel tells you in one line: all parts fit the bed. | All fit the bed | uitslagregel "N parts, all fit the bed" en "N pins, 0.20 mm clearance" |
| 7 | Then export every part and the pins as STL or 3MF, in millimeters. | STL or 3MF | knop Export parts, map met piece_01.stl enz. |
| 8 | Measured in Blender, not print tested by us yet. Print the fit test first. | Print the fit test first | stukken weer in elkaar, kleuren zichtbaar |
| 9 | Click Cuts for Blender. Link in the description. | (eindkaart) | eindkaart |

Bron (code, GEZIEN): `in_een_klik.py` r. 1 tot 3 en 55 tot 56 (Split to fit doet Make watertight als het nodig is, Plan cuts, Split en de check, met de printer en speling die staan), r. 36 tot 50 (uitslag "{n} parts, all fit the bed" en "{pennen} pins, {speling} mm clearance"); `plan.py` (kiest het rooster met de minste cellen waarvan elke cel past); `printers.py` r. 7 tot 16 plus "Custom size" (9 printers en een eigen maat); `paneel.py` r. 32 tot 53 ("Your printer", knop Split to fit met `depress=True`, "Export parts"); `exporteer.py` r. 41 tot 42 (STL of 3MF in mm, elk stuk en de pennen); `kleuren.py` (kleur per stuk, buren nooit gelijk). **Let op:** "fewest parts" geldt voor het rooster dat Plan cuts kiest (rechte sneden langs de assen), niet voor elke denkbare snede; zeg niet "the fewest possible". Het getal N in de uitslag neem je over uit de opname, niet uitspreken. Met de Lion Head moet de Regisseur zelf zien dat alle stukken groen zijn; is er een oranje of rood stuk, dan een ander model (Suzanne uit de test geeft groen op de A1 mini, `e2e/test_kern.py`).

---

## 2. Pennen die nooit passen? Eerst de fit test
Titel: Printed pins too tight or too loose? Do this first 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 2A | Do your printed pins never fit? | Pins never fit? | twee gesneden stukken die niet in elkaar gaan, pen rood |
| 2B | Pin too tight after a ten hour print? | Too tight? | zelfde, met een klok "10 h" in de hoek |
| 2 | Every printer and filament prints a hole a little different. | Every printer differs | twee gaten naast elkaar, net anders |
| 3 | So Click Cuts makes a small test block with four holes. | Small test block | `passing-1.png`: blok met vier gaten en vier pennen |
| 4 | Each hole has a different clearance, engraved right next to it. | Clearance engraved | `passing-2.png`: bovenaanzicht, 0.15 tot 0.30 leesbaar |
| 5 | Print it, try your pin, and click the hole that fits. | Click the one that fits | paneel "Printed? Click the one that fits:" met vier knoppen |
| 6 | It remembers that clearance for this printer and this filament. | Remembered | melding "Clearance 0.20 mm saved for Bambu Lab A1 mini + PLA" |
| 7 | Switch printer or filament, and the saved clearance comes back by itself. | Comes back | keuzelijst wisselen, speling springt mee |
| 8 | Measured in Blender, not print tested by us yet. That is why you print this first. | Print this first | blok en pennen |
| 9 | Click Cuts for Blender. Link in the description. | (eindkaart) | eindkaart |

Bron (code, GEZIEN): `passing.py` (`spelingen`: 4 waarden in stappen van 0,05 mm, één onder de ingestelde, de ingestelde, twee erboven; bij 0,2 dus 0,15 tot 0,30; `MATERIALEN`: PLA, PETG, ABS / ASA, TPU), `passingproef.py` r. 140 en 182 tot 212 (blok met gaten en gegraveerde speling, plus eigen pennen), r. 218 tot 228 ("This one fits": "Use this clearance and remember it for this printer and material"; melding "Clearance ... saved for ... + ..."), r. 83 (`pas_toe`: andere printer of ander materiaal geeft de bewaarde speling terug), r. 276 tot 292 ("Fit test: print this first", "Printed? Click the one that fits:"). **Let op:** zin 2 is een algemene waarheid uit de 3D-printwereld, geen meting van ons; als Daan dat te stellig vindt: "Printers and filaments rarely print a hole at the exact size." Zin 2B noemt geen echte printtijd van ons, het is de angst van de kijker; schrap de klok als dat als belofte leest. "Filament" zeggen in plaats van "material", de keuzelijst heet Material: kop mag "Printer + material".

---

## 3. Tien stukken, welke hoort waar? Nummers in elk snijvlak
Titel: Which printed part goes where? Number every cut 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 3A | Twelve printed parts, and no idea where? | Which goes where? | hoop losse grijze stukken op tafel (render, alle stukken één kleur) |
| 3B | Ever glued a part in the wrong spot? | Wrong spot? | twee stukken verkeerd tegen elkaar, rood |
| 2 | Click Cuts engraves a number into every cut face. | A number on every cut | close-up snijvlak met verdiept nummer (`splitser-kern-1`) |
| 3 | Each face shows its own part number and the part it joins. | 2-3 meets 3-2 | twee buren naast elkaar, "2-3" en "3-2" leesbaar |
| 4 | It is sunk into the cut, so the outside of your model stays clean. | Outside stays clean | buitenkant van het stuk, geen tekst |
| 5 | And it sits where there is room, not on top of a pin hole. | Not on a hole | snijvlak met twee gaten en het nummer ertussen |
| 6 | Parts are numbered from bottom to top, so you build up in order. | Bottom to top | Exploded view, nummers lopen op van onder naar boven |
| 7 | Measured in Blender, not print tested by us yet. Print the fit test first. | Print the fit test first | gekleurde stukken in elkaar |
| 8 | Click Cuts for Blender. Link in the description. | (eindkaart) | eindkaart |

Bron (code, GEZIEN): `splitsen.py` (nummers van onder naar boven: z, dan y, dan x; per stuk eerst de doos min de nummers, zo komt de tekst nooit op een al gesneden stuk), `verbinders.py` (`kies_label`: punt met de meeste ruimte buiten de gaten, hoogte 8 tot 2,5 mm), `vormen.py` (nummer als plaat tot de diepte binnen het vlak, leesbaar van buiten het snijvlak), `eigenschappen.py` (nummers aan, diepte 0,6 mm). Test: `e2e/test_kern.py` (op elk snijvlak met een buur een nummer dat met het eigen nummer begint en echt verdiept is). `verbind_3d.py` r. 137 (tekst op het vlak is "eigen-buur": "2-3" op stuk 2, "3-2" op stuk 3). **Let op:** zin 3: in de kop de echte nummers uit de opname, niet uitspreken als "two dash three". "Twelve" in 3A alleen als het model in beeld echt 12 stukken geeft; anders het echte getal (kop in cijfers). Zin 4 klopt omdat het nummer alleen op het snijvlak zit; nummers kun je uitzetten, niet nodig om te noemen.

---

## 4. Gat dwars door de wand? Elk stuk groen, oranje of rood
Titel: Pin hole breaks through the wall? Check before you print 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 4A | Pin hole broke right through the wall? | Hole through the wall? | doorsnede van een dun stuk waar het gat de buitenkant raakt, rood |
| 4B | One thin wall can ruin the whole print. | One thin wall | zelfde, kleiner |
| 2 | Click Cuts measures the wall around every pin hole in every part. | Wall around every hole | close-up gat met maatlijn naar de buitenkant |
| 3 | It also checks that each part fits the bed and is watertight. | Fits and watertight | lijst in More settings, stap 4 |
| 4 | Green is good. Orange means the wall is thinner than you set. | Green, orange | lijst met groene en een oranje regel "wall 1.0" |
| 5 | Red means too thin, too big for the bed, or not watertight. | Red: fix it first | rode regel "too big" of "not watertight" |
| 6 | Each line says why, so you know what to change before printing. | It says why | muis wijst op de reden achter het icoon |
| 7 | Measured in Blender, not print tested by us yet. Print the fit test first. | Print the fit test first | alle stukken groen in Exploded view |
| 8 | Click Cuts for Blender. Link in the description. | (eindkaart) | eindkaart |

Bron (code, GEZIEN): `controle.py` r. 84 tot 90 (`status_uit`: rood als het niet past, niet waterdicht is of de wand onder 0,8 mm (`ROOD_WAND_MM`, r. 21) ligt; oranje als de wand onder de ingestelde minimale wand min 0,05 mm ligt; anders groen), r. 93 tot 96 (`wand_rond_gaten`: kleinste wand van gatwand en gatbodem tot de buitenkant, en tussen de gaten), r. 150 tot 161 (`tekst`: maat, "too big", "not watertight", "wall x.x"); `eigenschappen.py` (minimale wand standaard 1,2 mm); `in_een_klik.py` r. 48 ("{n} parts, {m} need attention (see More settings, step 4)"); CHANGELOG ("Check: every part is green ..., orange or red, with the reason"). **Let op:** zin 5 klopt alleen met "too thin" als rood bij een wand onder 0,8 mm; zeg niet "any thin wall". Voor zin 4 en 5 moet de opname echt een oranje en een rood stuk tonen; maak er een met een kleine minimale wand of een te klein printbed (Custom size). Lukt dat niet in beeld, dan zin 4 en 5 samen tot "Green is good. Orange and red tell you what to fix." De add-on houdt een rood stuk niet tegen bij export; niet zeggen dat het "blocks" of "stops".

---

## 5. Je STL is duizend keer te klein? Verkeerde eenheid
Titel: Imported STL is tiny in Blender? It is the unit 🔥 | Blender tip

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 5A | Imported STL suddenly a thousand times off? | 1000x off? | STL in een lege scene, een stipje of een reus, maatlijn "0.33 m" |
| 5B | Your model is not too small. Blender is. | It's the unit | zelfde, eenheid "m" omcirkeld |
| 2 | STL files are usually in millimeters, but a new Blender scene is in meters. | mm vs meters | Scene Properties, Units, Unit Scale 1.0 |
| 3 | So a 330 millimeter bust can read as 330 meters, or the other way round. | 330 mm or 330 m? | maat in het N-paneel |
| 4 | Click Cuts sees it at once, and shows a red line in the panel. | Red line | paneel: "Model is ... mm in size", "Wrong unit? (mm model in a meter scene)" |
| 5 | Press Convert to mm, and only the scene unit changes. | Convert to mm | muis op de knop |
| 6 | Your model itself stays exactly the same, so nothing gets scaled by accident. | Model unchanged | maat na de knop: 330 mm |
| 7 | Measured in Blender, not print tested by us yet. Print the fit test first. | Print the fit test first | Split to fit op het model, stukken in kleur |
| 8 | Click Cuts for Blender. Link in the description. | (eindkaart) | eindkaart |

Bron (code, GEZIEN): `schaal.py` r. 1 tot 11 (onder 10 of boven 3000 mm is de eenheid waarschijnlijk fout; "meters (the Blender default) is 1000 times too big"), r. 38 tot 39 ("Convert to mm": "Set the scene unit scale so the model measures between 10 and 3000 mm. The model does not change"); `paneel.py` r. 77 tot 78 (rode regels); `in_een_klik.py` r. 75 (Split to fit weigert met "Wrong unit? Open More settings and use Convert to mm"); test `e2e/toetsen_extra.py` (doos als STL in mm in een scene in meters: Plan weigert, Convert to mm, daarna gewoon 3 stukken). **Let op:** zin 2 "usually" laten staan (STL heeft geen eenheid; de meeste slicers lezen mm). Zin 3: kies in de opname een model van 330 mm (Suzanne uit de test is 330 mm breed), anders het getal en de kop aanpassen. Welke kant het opvalt hangt van de importinstellingen af; laat in beeld zien wat er echt gebeurt en kies 5A of 5B daarop. Dit is half een tip (ook zonder add-on bruikbaar: Unit Scale), dus goed voor opslagen.

---

## 6. Rechte sneden door het gezicht? Eén vrije snede
Titel: Need one cut at an angle? Free cut in Blender 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 6A | Straight cut right through the face? | Cut through the face? | Lion Head met een rechte snede dwars door neus of oog, rood |
| 6B | Still fixing cut lines in your slicer? | Still fixing it later? | slicer-achtig beeld met een lelijke naad (alleen eigen render, geen echte slicer-UI van anderen) |
| 2 | After the split, pick one part and add a free cut. | Add free cut | More settings, knop "Add free cut" |
| 3 | Move it, turn it and scale it, to any angle you like. | Any angle | vlak draait met R, schuift met G |
| 4 | It only cuts inside its rectangle, so the rest of the part stays whole. | Only inside the rectangle | vlak dat alleen het oor raakt |
| 5 | Press Cut piece, and the new cut gets pins and numbers too. | Pins and numbers too | nieuw stuk met gaten en nummer, nieuw penplaatje |
| 6 | Too close to a pin hole? It stops and tells you how far to move. | Says how far | melding "Move it at least 1.2 mm away from the hole" |
| 7 | Measured in Blender, not print tested by us yet. Print the fit test first. | Print the fit test first | Lion Head in kleur, schuine naad langs de manen |
| 8 | Click Cuts for Blender. Link in the description. | (eindkaart) | eindkaart |

Bron (code, GEZIEN): `vrije_snede.py` r. 308 tot 310 ("Add free cut": "move (G), turn (R) and scale (S). It only cuts what lies inside its rectangle, on the side its arrow (local Z) points to"), r. 336 tot 337 ("Cut piece": "Cut the piece in two along the free cut, with pins and numbers, only inside the rectangle"), r. 173 tot 174 (melding "goes through a pin hole ... Move it at least {wand} mm away from the hole", met de standaardwand 1,2 mm), r. 155 en 168 (te klein, gaat er niet door), r. 287 (eigen penplaatje); `paneel.py` r. 134 tot 137 ("Free cut (one piece, any angle)"). Test: `e2e/toetsen_vrij.py` (torso met arm). **Let op:** de vrije snede werkt op één stuk na Split, niet op het hele model voor de split; zin 2 zegt dat. 6A belooft niet dat Click Cuts zelf het gezicht ontwijkt: het plan kiest rechte sneden, de vrije snede is de manier om er zelf een schuine bij te zetten. Kies in de opname een snede die echt lukt; het getal in de melding (zin 6) overnemen uit de opname.
