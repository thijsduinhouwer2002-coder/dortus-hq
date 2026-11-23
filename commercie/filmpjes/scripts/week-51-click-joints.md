# Zes Short-scripts Click Joints, week 51 (14 tot 20 dec 2026)

Door Sanne, 23 nov 2026. Opdracht hoofdchat 23 nov ±12:05 en ±12:45 NL (recept v3: hook eerst). Zelfde bouw als week 48 tot 50: zin 1 = hook A of B, max 7 woorden, een vraag over het probleem van de kijker, nooit de productnaam; daarna zinnen van 10 tot 16 woorden (4 tot 6 s); printzin altijd; geen AI of stem in titel of beschrijving, alleen het vinkje "Altered content" in YouTube Studio (besluit Thijs 23 nov 20:28 NL); kop korter dan de gesproken vraag; getallen als cijfer in de kop en uitgeschreven alleen in het json-veld `uitspraak`. Bronnen: `platformen/blender-2/gumroad-1.1.md`, `platformen/blender/pro-1.2.0.md`, `platformen/blender/pro-1.2.2.md` en de code in `producten/blender-gewrichten/click_joints/` (regels genoemd per script, GEZIEN op main cfac8c0).

**Stand: akkoord (Daan, 23 nov ±22:50 NL, `marketing/keuring/2026-11-23-scripts-week-51-daan.md`), M1 tot M4 en K1, K2 verwerkt door Sanne op 24 nov. Mag naar de Regisseur; de "Let op"-punten gelden als moet. Hooks met een stelling (1B, 3B, 4B) zijn bewust: de Meter noteert per paar of de vraag of de stelling won (K4). Script 2 niet in dezelfde week als een andere knie-post (K3).**

## Wat anders is dan week 50
- **Alles gaat over wat er misgaat bij de snede zelf**, en wat de add-on daar stil voor je oplost: zwaairuimte, één lid, te dicht bij elkaar, snippers, volgende plek, gemeten speling. Dat zijn dingen die een koper anders pas na het printen merkt.
- **Twee tips uit de gratis Click Joints** (script 2 en 6), met een gratis eindkaart (kan van Daan bij week 50). De andere vier zijn Pro.
- **Hooksoorten gewisseld:** probleem (1A, 2A, 3A, 4A, 5A), fout (1B, 4B), "al gedaan?" (2B, 6B), verrassing (3B, 5B, 6A).
- **Beeld:** de robot van studio-2, de Orc van Quaternius of een kaal blok/cilinder. Geen studio-1, geen MakeHuman-figuur in beeld.
- Nieuwe onderwerpen: niets hieronder staat al in week 48 tot 50 of `marketing/wachtrij/` (nagelopen 23 nov: knie, graden, pose, schouderkogel, nek, scharnier of kogel, splitsen, buigen, fit test, schoon zicht, enkels, AI-figuren, te klein, passingkleuren, Mixamo, Rigify, Daz, VRoid, CC, Auto-Rig Pro, monster, waterdicht, Exact, millimeter, Blender 4.2, rig-grenzen, papierdun, gaten, te groot, plat, exploded).

---

## 1. Arm botst op zichzelf voor de stop? Zwaairuimte
Titel: Printed elbow stops too early? This is why 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 1A | Does your elbow stop way too early? | Stops too early? | robot-elleboog die halverwege tegen de bovenarm botst (render, nieuw) |
| 1B | Your hinge is fine. Your arm isn't. | It's the arm | zelfde botsing, rood vlak waar de onderarm de bovenarm raakt |
| 2 | On a real figure, the forearm hits the upper arm before the stop. | Flesh hits flesh | inzoomen op de plek waar de delen elkaar raken |
| 3 | Click Joints Pro swings the forearm through its range, step by step. | Swing, step by step | onderarm draait in stappen (doorzichtig spoor) |
| 4 | Wherever it passes through the upper arm, it trims that bit away. | Trimmed away | bovenarm met de nieuwe holte bij de elleboog |
| 5 | The joint itself stays whole, so the hinge itself is not touched. | Joint untouched | close-up scharnier, knokkel en tong heel |
| 6 | If trimming does not help, the upper arm stays exactly as it was. | Or no change | zelfde bovenarm zonder holte |
| 7 | Then it measures again, so the number you see is the real range. | Measured again | getal bij de boog loopt op |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render robot in delen |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron (code, Pro, GEZIEN): `betaald/scharnier_zwaai.py` r. 1 tot 16 (B in stappen gedraaid en van A afgetrokken; een bol rond het draaipunt blijft buiten de uitsnede "zodat het klikmechaniek (knokkel, tong, wangen, eindstop) heel blijft"; lukt het niet, dan krijgt A zijn oude vorm terug) en r. 18 (STAP 10 graden); `betaald/scharnier.py` r. 221 tot 228 (na de beweegproef uitsnijden, daarna het nieuwe gemeten bereik als `cj_bereik_graden`). In de code gemeten op de MakeHuman-elleboog: rig-stop 115 gaf eerst 82 graden, daarna 115 (r. 4 en 12); dat getal **niet** uitspreken of in beeld zetten (oude meting, en MakeHuman mag niet in beeld). **Let op:** de uitsnede gebeurt alleen als het gemeten bereik meer dan 2 graden onder de stand ligt (r. 19 en 118). De Regisseur kijkt of de robot dat echt laat zien: met het eigenschappenvenster (Object Properties, Custom Properties) staat `cj_zwaai_van` alleen op de delen als er is uitgesneden. Staat het er niet, dan zoek je een elleboog of knie waar het wel zo is, of je schrapt dit script. Geen "click" of "snap" uitspreken (winkeltekst zegt nergens "clicks").

---

## 2. Eén knie snijden, en het andere been is ook door? Eén lid
Titel: Cut one leg, not both 🔥 | Blender tip

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 2A | Cut one knee, and both legs split? | Both legs cut? | figuur met een snijvlak dat door beide benen loopt (render, nieuw) |
| 2B | Cut through the wrong leg? | Wrong leg? | zelfde, het andere been rood |
| 2 | A cut in Blender often runs through the whole object, not just one leg. | Through everything | groot snijvlak door het hele figuur |
| 3 | Click Joints only cuts the limb around your 3D cursor. | Only this limb | cursor op de linkerknie, alleen dat been licht op |
| 4 | It finds the limb on its own, the part that hangs only on that spot. | Finds the limb | onderbeen gemarkeerd |
| 5 | Both feet on one base? Then it stops, and tells you why. | Stops and says why | melding VAST in de statusbalk |
| 6 | Other leg too close? It stops too, and tells you to pick another spot. | Pick another spot | melding DICHT |
| 7 | This is in the free Click Joints, so you can try it today. | Free | paneel |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render figuur met één knie gesneden |
| 9 | Click Joints. Free on Blender Extensions. | (gratis eindkaart) | eindkaart gratis |

Bron (code, gratis deel, GEZIEN): `een_lid.py` r. 1 tot 20 (alleen als het snijvlak het figuur op meer dan één plek raakt; de lus rond de cursor kiezen; het stuk dat alleen aan die lus vastzit is het lid; hangt het aan beide kanten vast: VAST; raakt het omhulsel een ander deel: DICHT), r. 26 tot 29 (meldingen: "for example both feet on one base ... Pick a spot where the limb is free, or split the model first" en "for example the other leg ... Pick another spot, or move the parts a little apart first"), r. 138 en 245. Zin 9: https://extensions.blender.org/add-ons/click-joints/ geeft 200 met titel "Click Joints" (GEZIEN met curl, 23 nov ±21:00 NL). **Let op:** zin 6: de melding zegt "Pick another spot, or move the parts a little apart first", dus in beeld de echte melding laten zien. Geen "only" in de zin over de hele snede als het beeld een los been laat zien: de regel geldt alleen voor een figuur uit één stuk.

---

## 3. Twee gewrichten te dicht op elkaar? De add-on rekent het voor
Titel: Two joints too close? Check this before you print 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 3A | Two joints crashing into each other? | Joints too close? | korte robotarm met twee gewrichten die overlappen (render, nieuw) |
| 3B | Two joints can break each other. | Two joints, one break | zelfde, rood waar de kom de nek raakt |
| 2 | Put two joints too close, and the socket of one cuts into the other. | Socket cuts socket | doorsnede: kom van het ene in de nek van het andere |
| 3 | Click Joints works out how far apart they need to be, in millimeters. | Distance in mm | doorsnede met een maatlijn |
| 4 | Too close? It does not cut, and says how many millimeters to keep. | Keep N mm apart | statusbalk "Too close to another joint (keep N mm apart)." |
| 5 | Pro also checks a hinge next to a ball joint on the same part. | Hinge + ball | bovenarm met scharnier en kogel |
| 6 | Bone too short for both? Pro says that plainly, and what to try. | Says what to try | lijst met "no room on this ... bone" |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render robot in delen |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron (code, GEZIEN): gratis kern `maat.py` r. 107 tot 113 (`te_dicht`: de bolnaad van het nieuwe gewricht mag niet in kom of trechter van het oude komen; nodige afstand in mm, naar boven afgerond) en `gewricht.py` r. 256 tot 262 (melding "Too close to another joint (keep {nodig} mm apart)." en niet snijden). Pro: `betaald/afstand.py` r. 1 tot 14 (kogel naast scharnier: reik van het scharnier plus reik van de kogel), `betaald/scharnier.py` r. 150 (zelfde melding bij het scharnier), `betaald/rig.py` r. 411 tot 425 (`geen_ruimte`: "no room on this N mm bone for a ball joint next to the elbow, place it by hand or give the elbow a smaller range"). **Let op:** zin 4 is gratis en Pro; zin 5 en 6 alleen Pro. Het getal N neem je over van wat de statusbalk in de opname echt zegt, niet uitspreken. Zin 6 alleen als de opname die melding ook laat zien (die komt alleen bij Figure from rig en een kort bot); anders zin 6 schrappen.

---

## 4. Dunne plaatjes in je scharnier? Weg na de snede
Titel: Tiny slivers after a boolean cut? 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 4A | Paper thin bits stuck inside your hinge? | Slivers inside? | close-up van een dun los plaatje in een sleuf (render, nieuw) |
| 4B | One tiny sliver can lock a joint. | One sliver, locked | zelfde, rood plaatje tussen twee delen |
| 2 | A boolean cut can leave thin plates in a narrow slot. | Thin plates | doorsnede van een smalle sleuf met plaatjes |
| 3 | They touch the other part, so the movement test says the joint can't move. | Joint can't move | boog met 0° |
| 4 | Click Joints Pro removes those loose bits right after the cut. | Removed after the cut | plaatjes verdwijnen |
| 5 | Only small loose pieces thinner than about a third of a millimeter. | Thinner than 0.3 mm | maatlijn bij een plaatje |
| 6 | A real loose part, like an eye or a button, is thicker and stays. | Eyes and buttons stay | figuur met los oog of knoop, groen omcirkeld |
| 7 | Then it measures the joint again, so the range in degrees is real. | Measured again | boog met het echte getal |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render robot in delen |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

`uitspraak` kop zin 5: "zero point three millimeters" (alleen als de stem de kop voorleest; gesproken staat er al "a third of a millimeter").
Bron (code, Pro, GEZIEN): `betaald/snippers.py` r. 20 tot 32 (weg gaat alleen een los stuk dat niet het grootste is, hooguit 5 procent van de punten heeft en volume gedeeld door oppervlak onder 0,15 mm: "een plaatje dunner dan ±0,3 mm, niet te printen"; "Een echt los onderdeel van het figuur (een oog, een knoop) is veel dikker en blijft"; de plaatjes "raken het andere deel, zodat de beweegproef 0 graden meet"); `betaald/rig.py` r. 727 tot 733 (ook bij Figure from rig na elke snede, daarna pas tellen). **Let op:** de plaatjes zijn 0,1 mm en in een render bijna onzichtbaar; de Regisseur mag ze in beeld dikker of in een kleur tonen, met de kop "illustration" klein in de hoek. Zin 7: de beweegproef na de opruiming volgt uit de volgorde in `snippers.register` (omhult `gewricht.snij`); kan de Regisseur dat niet laten zien, dan zin 7 schrappen. Niet zeggen dat het altijd lukt.

---

## 5. Gewricht mist op je figuur? Pro probeert de volgende plek (Pro 1.2.2)
Titel: Missing joint after Figure from rig? It now tries again 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 5A | Missing a joint after the cut? | Missing a joint? | lijst met een gewricht zonder vinkje, figuur met een heel been (opname, nieuw) |
| 5B | One bad spot, one lost joint? | One bad spot | zelfde, rode plek op het bot |
| 2 | Sometimes a cut fails on one spot, because one edge comes out broken. | One broken edge | inzoomen op een slechte rand |
| 3 | Since version 1.2.2, Figure from rig then tries the next spot on that bone. | Next spot | cursor schuift een stukje langs het bot |
| 4 | Also when a joint is too close to another, or too thin for a hinge. | Too close, too thin | lijst met de redenen |
| 5 | A ball joint that would not turn is undone, and it tries again. | Stuck? Undone | kogel met 0°, snede verdwijnt |
| 6 | Still no luck? The list says why, so you can place it by hand. | The list says why | lijst met reden en "place it by hand" |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render robot in delen |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

`uitspraak` zin 3: "one point two point two".
Bron: releasenotes 1.2.2 "Figure from rig: when a cut fails at one spot, it now tries the next spot on that bone instead of skipping the joint." (`platformen/blender/pro-1.2.2.md`, akkoord Daan; live op Gumroad en Superhive sinds 23 nov ±20:45 volgens het bord). Code `betaald/rig.py` r. 756 tot 764 (volgende plek bij "too close", "no watertight parts", en bij een scharnier ook "too thin" en "tight"), r. 735 tot 739 (kogel die volgens de beweegproef niet beweegt: terugdraaien, volgende plek), r. 772 tot 775 (de echte reden blijft in de lijst). **Let op:** niet zeggen dat er nu nooit meer een gewricht mist; Olaf vond dat de extra plek op andere leden net zo vaak kapot is (`pro-1.2.2.md`, Stand punt 3). Zin 2 is een vereenvoudiging van "één slechte rand uit de booleaanse snede" (rig.py r. 757); mag zo. Niet vlak na week 50 script 3 (Exact) plaatsen: allebei 1.2.2.

---

## 6. Is je speling echt 0,2 mm? Gemeten na de snede
Titel: Your ball joint gap, measured, not guessed 🔥 | Blender tip

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 6A | Is your gap really what you set? | Really 0.2 mm? | doorsnede kogel en kom met een maatlijn met vraagteken (nieuw) |
| 6B | Printed a ball joint that's stuck? | Stuck ball? | kogel die niet draait (render, rood) |
| 2 | Set a gap, cut, and the real gap can come out a bit different. | Set vs real | twee getallen naast elkaar |
| 3 | So Click Joints measures the gap between ball and socket after the cut. | Measured after the cut | stralen van de kogel naar de kom |
| 4 | It averages many points around the ball, and shows that in the panel. | Clearance (measured) | paneel: "Clearance: 0.20 mm (measured)" |
| 5 | Next to it you see the wall thickness, so a thin socket shows too. | Wall in mm | paneel: "Wall: N mm" |
| 6 | Not sure which gap your printer likes? Print a fit test first. | Fit test first | fit test strip (Pro) of testkogel |
| 7 | The measured gap is in the free Click Joints, for every ball joint. | Free | paneel |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render kogel en kom |
| 9 | Click Joints. Free on Blender Extensions. | (gratis eindkaart) | eindkaart gratis |
Bron (code, gratis deel, GEZIEN): `gewricht.py` r. 303 tot 310 (bij een kogel na de snede `passing.meet_speling` tussen deel A en deel B rond het kogelmidden, gemiddelde als `cj_speling_gemeten_mm`); `paneel.py` r. 99 tot 102 ("Wall: N mm" en "Clearance: N mm (measured)"); standaard speling 0,2 mm (gumroad-1.1.md "Clearance 0.2 mm by default"). Fit test strip is Pro 1.2.0 (`pro-1.2.0.md`). **Let op:** alleen bij een kogel, niet bij een scharnier (r. 303); dus in beeld een kogel. Zin 2 is voorzichtig ("can come out a bit different"): ik weet niet hoe groot het verschil op de robot is. Laat het paneel echt 0.20 zien, dan wordt zin 2 "Set a gap, cut, and check that the real gap matches." De Wall-regel staat er niet bij Tight (dan staat de wand in de reden, r. 99): neem een kogel met Good fit. Hook 6A: als de gemeten waarde in de opname gelijk is aan de ingestelde, is het antwoord eerlijk "yes"; dat is goed, het gaat om controleren.

---

## Volgorde voorstel (geld eerst)
Volgorde: **5, 2, 1, 6, 3, 4.** 5 eerst: nieuw in 1.2.2 en precies de angst van een koper van Figure from rig ("mist er straks een gewricht?"). 2 en 6 zijn gratis tips die mensen bewaren en brengen bereik bij 3D-printers, met een Pro-script ertussen. 1 laat zien waarom het getal te vertrouwen is (verkoopt het hoofdbeloofde "stopt waar je rig stopt"). 3 en 4 zijn kleiner. Niet 1 en 4 vlak na elkaar (allebei "daarna opnieuw gemeten"). De Regisseur kiest.
