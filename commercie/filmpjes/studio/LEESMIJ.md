# Studio voor de Blender-filmpjes van Click Joints Pro

Gemaakt 23 nov 2026 (opdracht hoofdchat ±11:45 NL, na "onze filmpjes zijn saai, de omgeving in Blender moet ook beter").
Vanaf nu wordt elk Blender-filmpje (Short, TikTok, lange video) in deze studio opgenomen.

**Figuur vanaf studio-2 (23 nov ±16:30): de robot-actiefiguur** (`figuur_robot.py`, zelf gebouwd). Thijs vond het
mensfiguur van studio-1 "super nep" (plastic paspop, stijf gezicht) en koos "een robot of actiefiguur, maar dan goed
gedaan". Laden: `FL.laad_figuur("robot")`. Bewijs: workflow `.github/workflows/studio2.yml`, release `studio-2`.
Het mensfiguur (studio-1, `studio.yml`) blijft laadbaar met `FL.laad_figuur("mens")`, maar gebruik het niet meer.

**Ronde 2 van de robot (studio-3, 23 nov ±21:00, opdracht hoofdchat ±20:35; workflow `studio3.yml`, release
`studio-3`).** Wat er veranderde:
1. **Stoer in plaats van schriel:** dikke antraciet buizen (bovenarm 9, dij 11 mm straal) en pantser dat bijna tot
   het gewricht loopt (bovenarm 24 tot 80 procent van het bot, onderarm 28 procent tot de pols, dij 24 tot 84, scheen
   vanaf 20 procent tot in de laars). Bij de gewrichten blijft alleen een smalle donkere ring. De regel die dat mag:
   pantser hoogstens 1,3 keer de buis (anders schuift de kogel te ver uit de romp), en het bot van elleboog en knie
   blijft 4,4 en 6 mm van de huid aan de buigkant (`ELLEBOOG_R`, `KNIE_R`, `rig_punten`).
2. **Vuisten met vingers:** handpalm, vier vingerblokjes met een groefje en vingertoppen, een duim, blauwe pols
   (`hand()`).
3. **Heldenpose:** breed staan, linkervuist omhoog, rechtervuist klaar, kin omhoog (`HELD`). `poseer()` zet de delen
   als keten: kogels draaien om hun kogelmidden binnen het bereik dat de add-on meldt (schouders en heupen ±30,
   nek ±20), scharnieren buigen met de schuif van de add-on en die draaiing wordt overgenomen.
4. **Uit elkaar:** `poseer(delen, {}, uit=26)`: elk deel 26 mm langs de as van zijn gewricht, bovenop het deel waar
   het aan zit (de knop Exploded view van de add-on schuift 1,5 keer de kogel, ±12 mm, en per deel los).
5. **Kleurgrenzen:** `kleur_herstel()` deelt na Figure from rig de vlakken langs een kleurgrens twee keer in vieren
   en kleurt ze opnieuw per vorm: de grens volgt de vorm op ±0,13 mm in plaats van trapjes van 0,5 mm. Vlakken
   zonder materiaal (naad van de add-on) en binnenvlakken worden antraciet. Alleen voor renders.
6. **Winkelbeelden:** met `CJ_WINKEL=1` maakt `bewijs.py` ook `winkel-<naam>-held-2400.png` en
   `winkel-<naam>-uit-elkaar-2400.png`: 1350 x 2400 px, geen studio, transparante achtergrond, geen tekst.
7. **Gewrichten: 9 in CI** (GEZIEN, release `studio-3`, `kandidaten.txt` en `robot-a-meting.json`): ellebogen 0 tot
   140, knieën 0 tot 120, nek ±20, schouders ±30, linkerheup ±22, rechterheup ±30, elk deel één stuk. Gemeten in
   6 CI-jobs op dezelfde mesh (runs op 42376c66, a28d0116 en a67de4fd): 5 keer 9, 1 keer 8 (rechterschouder "it would
   be blocked"). Lokaal op dezelfde mesh en dezelfde machine: 8, 9, 9. **De add-on geeft dus niet altijd dezelfde
   uitkomst op dezelfde mesh** (iets voor de makers van de add-on). Beide heupen lukten in alle 6 CI-jobs.
   De linkerheup lukte in studio-2 niet: met alleen heupen en knieën (of plus ellebogen, of plus schouders, of plus
   nek) lukte hij wel, alleen in de volledige reeks niet. Met de dikkere ledematen lukt hij nu ook in de volledige
   reeks (GOK waarom: grotere kogel, meer ruimte in de beweegproef).
8. **Schermafbeeldingen met het paneel** (`robot-a-scherm-1/2/3`, 1920 x 1080) tonen de nieuwe robot; op scherm 2 de
   lijst "9 joints". In het Blender-scherm staan de kleuren zoals de add-on ze laat (kern op de borst half oranje,
   groene passingkleuren); alleen de renders gaan door `kleur_herstel`.

**Eerlijk oordeel ronde 2 (zelf gekeken, ook op ware grootte):** stevig en stoer in plaats van schriel, vuisten
met vingers lezen als handen, de pose (breed staan, vuist omhoog) is leesbaar, uit elkaar zie je in één tel de
kogels en de opbouw, kleurgrenzen zijn glad op 2400 px. Wat nog minder is: de schouderkogels blijven grote donkere
bollen; bij knie en elleboog zie je de snede van het scharnier (in uit elkaar een groot plat donker vlak aan de
binnenkant van de onderarm, dat is de stopvlakte van het scharnier); de helm heeft lichte facetten op de grote
rondingen; de vuist omhoog komt niet hoger dan schouderhoogte (kogel ±30). Zou een koper op Gumroad stoppen met
scrollen? Op het beeld uit elkaar waarschijnlijk wel, op de pose alleen minder (GOK).

## Wat erin zit
| Bestand | Wat |
|---|---|
| `figuur_robot.py` | `laad_robot(220)`: de robot-actiefiguur, gebouwd uit afgeronde vormen, één gesloten mesh (Make watertight), rig met Mixamo-namen. Kleurstellingen `STIJL` (wit, oranje, blauw) en `STIJL_B` (geel, rood, nachtblauw). |
| `figuur_laden.py` | `laad_figuur(keuze)`: één ingang, keuze `"robot"` (standaard), `"mens"` of een pad naar een glb/blend. Daaronder `laad_mens_kleding(obj)`: MakeHuman (CC0) aangekleed, met rig (studio-1). `laad(glb)`: elk ander figuur met eigen rig als één mesh voor Figure from rig. |
| `studio.py` | `bouw()`: gebogen achterwand in muntgroen, wit podium met gele rand, 3 vlakke lampen plus een zon zonder schaduw, EEVEE. `plastic(delen)`: geprint plastic. `camera()`, `richt()`: staand 9:16 of liggend 16:9. `render()`: door de camera. `rustig_scherm()`: opnamescherm. |
| `bewijs.py` | Het hele verloop als voorbeeld: figuur, studio, 3 schermafbeeldingen, Figure from rig, 3 renders. `CJ_FIGUUR=robot` voor de robot, `CJ_STIJL=b` voor de tweede kleurstelling, `CJ_ALLEEN_STAAND=1` voor alleen de eerste render. |
| `proef_figuur.py` | Proef per kandidaat-figuur: hoeveel gewrichten maakt Figure from rig? Model `robot` = de robot. |
| `modellen/robot-dortus.glb` | Kijkmodel van de robot (losse vormen met kleuren, geen rig), met `robot-dortus-LICENTIE.md` (eigen werk van Dortus). GitHub laat het draaien. De studio laadt het niet: die bouwt de robot uit het script. |
| `modellen/makehuman-base.obj` | Het model van studio-1, ongewijzigd van MakeHuman, met `makehuman-base-LICENTIE.md` (CC0 1.0). |

## De robot-actiefiguur (studio-2)
Zelf gebouwd met `figuur_robot.py` (geen download, geen AI-model, geen merk of bekend personage), 220 mm hoog:
- **Vormen:** helm als afgeronde doos met een donker vizier, twee lichtblauwe oog-leds, oren en een oranje kam;
  borstkas smal naar de taille met een oranje borstplaat en een lichtblauwe kern; geribde metalen buik; blauw bekken
  met oranje gesp; wit pantser op bovenarm, dij en scheen; oranje onderarmen; oranje kniestukken; stevige blauwe
  laarzen met oranje neus; grijze vuisten. Gewrichten (schouder, elleboog, heup, knie, nek) zijn gladde
  antraciet buizen: daar zet de add-on zijn kogels en scharnieren.
- **Kleuren (sRGB), `STIJL`:** wit F3F1EA, oranje FF6A1F, blauw 1F44B0, metaal 8E95A3 (zijdeglans in de renders),
  antraciet 3A404D, vizier 15171E, led 4DF0FF (gloeit zacht in de renders). **`STIJL_B`:** geel FFD23F, rood E8364F,
  nachtblauw 1B1F3B, led groen 7CFF6B.
- **Mesh:** alle vormen samen, dan Make watertight van de add-on (voxel 0,5 mm) en de kleuren per vlak terug. Een
  echte vereniging (Boolean Exact) is strakker, maar daarop gaf Figure from rig maar 4 gewrichten ("parts overlap");
  daarom voxel (`CJ_ROBOT_MESH=boolean` om het te proberen).
- **Rig:** dezelfde als het mensfiguur (`maak_rig` uit `producten/blender-gewrichten/e2e/proef_mens.py`, Mixamo-namen,
  linkerknie 120 en linkerelleboog 140 in Limit Rotation), maar elleboog en knie liggen dicht bij de huid aan de
  buigkant (zie hieronder).

### Wat de add-on van een figuur nodig heeft (geleerd met de robot, Pro 1.2.0, GEZIEN in de proeven van 23 nov)
1. **Elleboog en knie dicht bij de buigkant.** Het scharnier meet zijn stopvlakken vanaf het bot schuin naar de
   buigkant (wig van ±70° bij 140°, ±60° bij 120°) tot ze de huid raken. Met het bot midden in een buis van 6,4 mm
   straal reikte de elleboog 35 mm langs de arm (`cj_reik`), en dan past de schouderkogel niet meer op een bovenarm
   van 41 mm ("no room on this 41 mm bone ... next to the elbow"). Met het bot 4,4 mm van de huid aan de buigkant:
   elleboog 16,6 mm, knie ±29 mm. De knie niet nog dichter bij de huid: bij 4,4 mm gaf hij "parts overlap".
2. **Pantser niet op de schouder en niet tegen de romp.** Een kogel schuift uit de romp tot de doorsnede van het lid
   niet breder is dan 1,3 keer de dunste straal. Alles wat daar dwars uitsteekt (een as van de romp naar de schouder,
   een schouderstuk) maakt de doorsnede breed: "only a tiny ball fits here". Een bol aan de bovenarm die net de zijkant
   van de borst raakt werkt wel (schouders ±30°).
3. **Ruimte tussen de benen en onder het bekken.** Met de heupen op x = ±15 en dik pantser op de dijen: "it would be
   blocked". Op ±17 met smaller pantser lukt het (±27 tot ±30°). Het heupbot op 113 mm in plaats van 116 maakte het
   slechter (beide heupen geblokkeerd).
4. **Uitkomst hangt aan de voxelmaat:** op 0,5 mm 9 gewrichten, op 0,35 mm 8 (linkerheup geblokkeerd). Daarom blijft
   0,5 mm de standaard.

### Gewrichten van de robot
- **CI (job kandidaten en studio van `studio2.yml`, release `studio-2`, GEZIEN): 8 gewrichten** (beide ellebogen en knieën als scharnier met eindstop 140 en 120, nek ±20°, beide schouders ±30°,
  rechterheup ±27°), elk deel één stuk, in beide kleurstellingen (run 45197874364 en de run op 1306ec6f, 23 nov).
  Overgeslagen: linkerheup "no room for a ball joint that can move here (it would be blocked)".
- Lokaal (zelfde Blender 5.3.0 en zip, 2 kernen): 9 gewrichten bij voxel 0,5 mm, elk deel één stuk. Net als bij het
  mensfiguur geeft CI één minder; daar faalt de linkerheup ("it would be blocked"), net als lokaal bij voxel 0,35 mm.
  Vijf pogingen om dat te verhelpen (heupen breder of smaller, bekken hoger of breder, heupbot lager) maakten het
  slechter (7). Noem in een filmpje alleen wat de lijst in beeld zegt.
- Figure from rig kost ±45 tot 65 s op de robot (GEZIEN, `knop_s` in `robot-a-meting.json`).

### Eerlijk oordeel over het uiterlijk (zelf gekeken naar de renders in `studio-2`)
- **Veel beter dan studio-1.** Het is duidelijk speelgoed: een vrolijke robot met een vizier en lichtblauwe ogen,
  wit pantser, oranje en blauw. Geen mensengezicht, dus niets wat "nep" kan ogen. In uit elkaar zie je de kogels en
  kommen als antraciet mechaniek, dat past bij een robot. De gevonden mechs zijn wit (textuur valt weg), dun en
  krijgen 0 tot 4 gewrichten.
- **Geen "wauw" zoals het oceaanfilmpje van Malikose** (81.000 weergaven op TikTok, GEZIEN 21 nov, zie
  `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-21-malikose-tip-format.md`). Dat is een realistisch
  natuurbeeld; dit is een nette productfoto van een speelgoedrobot. De haak zit in het uit elkaar vallen en weer
  klikken, niet in het beeld zelf (GOK).
- **Veel antraciet buis.** Bij elk gewricht blijft 10 tot 20 mm kale buis over (de add-on heeft daar ruimte nodig),
  vooral boven de dij en onder de knie. Het oogt daardoor wat slank en mechanisch, minder als een stevig actiefiguur.
- **Kleurgrenzen met kleine trapjes** (voxel 0,5 mm) op de randen van platen en het vizier, op ware grootte te zien.
  De kleuren komen nu per vorm (geen witte snippers meer) en na Figure from rig zet `kleur_herstel` ze terug: de
  add-on zelf schuift na elke snede de kleur van kleine details een beetje (kern op de borst werd half oranje).
  Dat is iets voor de makers van de add-on.
- **In het Blender-scherm** (schermafbeeldingen) staan de kleuren zoals de add-on ze laat: daar is de kern op de
  borst wel half oranje, plus de groene passingkleuren. Alleen de renders gaan door `kleur_herstel`.
- **Bij een gebogen knie of elleboog** zie je de snede: een stukje van het pantser of het kniestuk zit dan aan het
  andere deel. Dat is echt wat de add-on maakt.
- **De pose blijft stijf in de schouders:** kogels van ±30°, de armen hangen in de houding van het model (licht
  gespreid). Poseren gaat vooral met knieën en ellebogen.

### Zoektocht naar een gevonden robot (23 nov, studio-2): niets goed genoeg, dus zelf gebouwd
Gezocht op GitHub (zoekfunctie: robot, mech, rigged robot, mannequin, CC0 characters), in quaternius-showcase (alle
1545 modellen), Khronos glTF-Sample-Assets en OpenGameArt (3D, CC0, "robot"). Niet doorzocht: Poly Pizza (de API wil
een sleutel), Kenney (alleen blokkige mini-figuren met korte ledematen), Blender-demobestanden, NASA en Smithsonian
(echte robots en ruimtevaart, met logo's). Licenties zelf gelezen met curl op 23 nov (GEZIEN):

| Kandidaat | Bron en licentie | Uitslag |
|---|---|---|
| Stan (Animated Mech Pack) | [Quaternius](https://quaternius.com/packs/animatedmech.html), CC0 (pakketpagina) | CI 240 mm: 4 gewrichten (ellebogen, heupen). Knieën "too thin", schouders "only a tiny ball". In de studio wit (textuur valt weg), dunne poten |
| Mike (Animated Mech Pack) | idem, CC0 | CI: 4 gewrichten. Linkerelleboog "parts overlap", heupen geblokkeerd |
| George (Animated Mech Pack) | idem, CC0 | CI: 0 gewrichten, 9 losse stukken (ledematen raken elkaar, drie delen per been) |
| Character (Cyberpunk Game Kit) | [Quaternius](https://quaternius.com/packs/cyberpunkgamekit.html), CC0 | CI: 2 gewrichten. Dunne ledematen, knieën "cheek too stiff" |
| Mechs met dieren (Ultimate Space Kit) | [Quaternius](https://quaternius.com/packs/ultimatespacekit.html), CC0 | niet getest: dier in een cabine, korte dikke poten, geen armen |
| Godot-robot | [AGChow, GitHub](https://github.com/AGChow/3D-Godot-Robot-Platformer-Character), CC0 | afgewezen: het hoofd is het Godot-logo (merk), korte stripverhoudingen |
| BrainStem | [Khronos glTF-Sample-Assets](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/BrainStem), Poser EULA | afgewezen: geen vrije licentie |
| 7 robots op OpenGameArt (Gum Bot, BA-2, Sentry-2, Robot pack 3D, ...) | [OpenGameArt](https://opengameart.org/art-search-advanced?keys=robot), CC0 | afgewezen op het voorbeeldplaatje: geen armen en benen (wielen, rupsen, zwevend) of klein en stomp |

Let op: Quaternius heeft sinds 28 aug 2026 een eigen licentie op de site ([QAL](https://quaternius.com/license.html):
gebruik vrij, de bestanden zelf niet doorgeven). De pakketpagina's hierboven zeggen nog CC0. Wij zetten geen
Quaternius-bestanden in de repo; de workflow haalt ze op.

## Het mensfiguur (studio-1, niet meer gebruiken)
MakeHuman `base.obj` (CC0 1.0, bron en licentietekst in `modellen/`), door ons aangekleed in `laad_mens_kleding`:
borst plat en romp glad (zoals de e2e-figuur), dan per stuk kleding het oppervlak een fractie naar buiten zodat zomen in
de vorm zitten: shirt met korte mouwen (0,45 mm), broek (0,45 mm), riem (0,9 mm), schoenen (bolle schil om de voet, platte zool, geen tenen),
haar (2,2 mm). Ogen, wenkbrauwen en mond zijn kleur. Daarna Make watertight van de add-on en de rig uit
`producten/blender-gewrichten/e2e/proef_mens.py` (linkerknie 120 en linkerelleboog 140 in Limit Rotation).
Geen AI-model, geen merk of bekend personage.

Waar het niet mag: op de schouders en mouwen en aan de binnenkant van de dijen geen extra dikte. Daar komen de kogels
van schouder en heup; met dikte erbij werden ze geblokkeerd (proef: 6 of 7 gewrichten in plaats van 9).

Kleurstellingen (sRGB): **a** oranje shirt FF6B3D, blauwe broek 2F6BFF, gele schoenen FFD23F, bruin haar 4A2C1D.
**b** paars shirt 7B5CFF, donkere broek 2B2D42, roze schoenen en riem FF4F79, blond haar F4B942
(`STIJLEN` in `bewijs.py`, `stijl=` in `laad_mens_kleding`).

## Kandidaten (Figure from rig, Pro 1.2.0, Blender 5.3.0)
Uitslag uit CI, job `kandidaten` van `studio.yml`, bestanden `<naam>-<hoogte>.json` en `proef-<naam>.log` in release
`studio-1` (GEZIEN). Eis: minstens 7 gewrichten, elk deel één stuk (geen losse snippers). Alle kandidaten CC0.

| Kandidaat | Bron | Hoogte | Gewrichten | Wat de add-on meldt |
|---|---|---|---|---|
| **MakeHuman met kleding (gekozen)** | [makehuman base.obj](https://github.com/makehumancommunity/makehuman/blob/master/makehuman/data/3dobjs/base.obj), CC0 1.0, aangekleed door ons | 220 mm | **8** in CI (ellebogen en knieën als scharnier met eindstop, nek, rechterschouder en beide heupen als kogel); lokaal 9 | in CI: linkerschouder "The cut gave no watertight parts", mesh daar onveranderd; lokaal (zelfde Blender en zip) geen meldingen. Elk deel één stuk |
| Knight (Animated Knight Pack) | [Quaternius](https://quaternius.com/packs/knightcharacter.html) via [quaternius-showcase](https://github.com/trebeljahr/quaternius-showcase), CC0 | 240 mm | 3 (2 ellebogen, rechterknie) | schouders, heupen en nek: geen ruimte (bovenarm 40 tot 44 mm, dij 41 mm, korte stripverhoudingen); linkerknie te stijf |
| Adventurer (Ultimate Modular Men), zonder rugzak, armen 40° omlaag | idem, CC0 | 260 mm | 4 (ellebogen, knieën) | schouders: bovenarm 25 mm te kort; heupen: geen ruimte naast de knie; nek niet geplaatst |
| Medieval (Ultimate Modular Women), armen 40° omlaag | idem, CC0 | 260 mm | 4 (ellebogen, knieën) | schouders: alleen een heel kleine kogel past; heupen te dicht bij de knie (46 mm nodig) |
| King (Ultimate Modular Men), armen 40° omlaag | idem, CC0 | 260 mm | 4 (ellebogen, heupen) | knieën: de mantel verbindt de benen; schouders: bovenarm 25 mm |
| RobotExpressive | [three.js](https://github.com/mrdoob/three.js/tree/r170/examples/models/gltf/RobotExpressive), model van Tomás Laulhé (Quaternius), CC0 | 240 mm | 0 | scharnieren te stijf, schouders en heupen geen plek (losse onderdelen aan botten, dunne ledematen) |
| CesiumMan (KhronosGroup) | glTF-Sample-Assets, CC-BY 4.0 | | niet getest | het Cesium-logo staat op het figuur: een merk |

Waarom de Quaternius-figuren afvallen: korte bovenarmen en dijen naast dikke kleding (of een mantel); de kogel van
schouder of heup past dan niet naast de elleboog of knie. Dat ligt aan de verhoudingen, niet aan de grootte
(op 225 tot 260 mm hetzelfde beeld, ook bij Chris op 22 nov). De MakeHuman-figuur heeft echte verhoudingen.

## Zo laad je de studio in een opname-workflow
In de workflow (zie `studio.yml`): Blender 5.3.0, de Pro-zip 1.2.0 (`PRO_COMMIT` f8dfbd3, `PRO_VERSIE=1.2.0 bash
e2e/maak_zip.sh betaald`) en `xvfb-run` met `--gpu-backend opengl`. In het opnamescript:
```python
import sys; sys.path.insert(0, "commercie/filmpjes/studio")
import figuur_laden as FL, studio as S
arm, ob, punten = FL.laad_figuur("robot", 220.0)   # de robot; stijl=R.STIJL_B (import figuur_robot as R) voor geel en rood
arm.hide_set(True)
S.bouw(220.0)                  # studio rond het figuur (voeten op z=0, podium eronder)
S.rustig_scherm(ui=1.35)       # alleen 3D-weergave en paneel, groter lettertype, studiolicht in beeld
# ... echte klikken: figuur kiezen, Figure from rig, schuiven (zoals youtube-shorts-4/opname.py) ...
delen = [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_figuur") == ob.name and o.visible_get()]
S.plastic(delen)               # alleen voor de renders: plastic en de passingkleuren van de add-on weg
cam = S.camera(); S.richt(cam, delen, "staand", draai=-32, kantel=7, vul=0.74, midden_y=0.56)
S.render("/tmp/uit/eind.png")  # door de 3D-weergave, dus met de buiging van de add-on
```
- In `youtube-shorts-4/opname.py` vervang je `figuur()` door `FL.laad_figuur("robot")` en `zet_render_scene()` door
  `S.bouw` plus `S.plastic` en `S.camera`. Het scherm: `S.rustig_scherm` in plaats van `kijk_breed` (de zijbalk breed
  slepen en de echte muis blijven werken zoals ze waren).
- Poseren alleen via de add-on: scharnieren met `wm.cj_scharnier_pose` op deel B (knie 0 tot 120, elleboog 0 tot 140).
  De kogels (schouder, heup, nek) zijn ±20 tot ±30° en draaien in de add-on allemaal tegelijk; laat ze in de renders op 0.
- Zijbalk scrollen gaat met het muiswiel (xdotool klik 5 omlaag, 4 omhoog, boven het paneel); klikken op de kop van
  het paneel om in te klappen werkte in de proef niet betrouwbaar.
- Renders gaan door de 3D-weergave (`bpy.ops.render.opengl`, Material Preview met de lampen van de scene). EEVEE in
  software-OpenGL is traag en zwaar: reken op ±1 minuut en 4 tot 6 GB geheugen per render. `CJ_TEST=1` geeft 40% en
  weinig samples om snel te kijken.

## Licht en kleur (in `studio.py`, bovenaan)
Achterwand: verloop van E4F6EF (vloer) naar 86D9C2 (wand), loopt rond over zonder naad. Podium FFFFFF met rand FFD23F.
Lampen (scene in mm, kracht op het oog gezet): sleutel links voor (schijf 1,1 keer de figuurhoogte), vul rechts,
rand achter, plus een zon zonder schaduw voor de wand. AgX, look Punchy. Plastic: ruwheid 0,36,
laklaag 0,25, laaglijnen 0,4 mm als licht reliëf.

## Wat nog niet mooi is
Eerlijk, na zelf kijken naar de renders en schermen in release `studio-1` (GEZIEN):
- **Geen "wauw" zoals het oceaanfilmpje van Malikose.** Het is een nette productfoto: aangekleed figuur met gezicht,
  zacht licht, rustige muntgroene achtergrond, podium. Veel beter dan de kale oranje pop van shorts-4 (geen gezicht,
  geen kleding, bleke effen achtergrond), maar een scroller stopt hier vooral als hij 3D print of figuren maakt (GOK).
- **Haarlijn, wenkbrauwen en mond hebben trapjes**: de kleur gaat per vlakje van de remesh (0,5 mm). Op een telefoon
  klein, op volle grootte goed te zien. Beter: kleur als vloeiende overgang (kleurlaag per punt) of fijnere voxels.
- **Schoenen zijn hoekig** (bolle schil om de voet) en **handen hebben losse vingers** (MakeHuman), wat bij een
  speelgoedfiguur wat vreemd oogt.
- **Armen staan altijd half wijd**: de schouders zijn kogels van ±20°, dus de A-houding van het model blijft. Poses
  gaan alleen met knieën (0 tot 120°) en ellebogen (0 tot 140°); de pose in de renders is een looppas.
- **Naden bij de gewrichten**: lichte ringen bij hals, schouders en heupen (randen van kogel en kom) en een blokje bij
  de elleboog. Dat is echt wat de add-on maakt; in de renders zijn alleen de passingkleuren weggehaald.
- **Gewrichten wisselen per machine**: met precies dezelfde mesh gaf CI 8 en lokaal 9 (de snede van de
  linkerschouder geeft soms "The cut gave no watertight parts"). Noem in een filmpje alleen wat de lijst in beeld zegt.
- **Traag**: een render kost in CI ±5 minuten (EEVEE in software-OpenGL), de hele bewijs-run ±25 minuten per kleurstelling.
- In het scherm staan de groene passingkleuren van de add-on met wat korrel op de heupbanden; zo ziet de add-on eruit.

## De houten tekenpop (tekenpop-1, 23 nov ±22:35, tekenpop-agent)
Thijs vond dat een mooie "ragdoll" beter zou werken dan de robot; wij lezen dat als de klassieke houten tekenpop.
Laden: `FL.laad_figuur("tekenpop")` (`figuur_tekenpop.py`, eigen werk, herkomst in `modellen/tekenpop-dortus-LICENTIE.md`).
Bewijs: workflow `.github/workflows/tekenpop.yml`, release `tekenpop-1`.
- **Vormen:** eivormig hoofd zonder gezicht (iets naar voren gekanteld), hals, borstkas als afgeronde superellipsoïde
  (breed bij de schouders), bal in de taille, bekken, ovale ledematen die bij elk gewricht smal worden (`lid()`),
  peddelhanden met een duimpje en peddelvoeten met een platte zool. Eén gesloten mesh met Make watertight (voxel 0,5 mm).
- **Wat de add-on nodig had:** de eerste versie gaf 3 losse stukken (armen raakten de borst niet): borstkas breder
  (21,5 mm) en de schouder op x = 27,5, zodat de bol van de bovenarm de zijkant van de borst net raakt. Verder de lessen
  van de robot: elleboog 4,4 mm en knie 6 mm van de huid aan de buigkant (`rig_punten`), heupen op x = +-17.
- **Gewrichten: 9 in CI** (alle vier de render-jobs van `tekenpop.yml`, run 45275349089 op 585d32cf, GEZIEN in
  `b-*.json`): ellebogen 0 tot 140, knieën 0 tot 120, nek +-20, schouders +-30, linkerheup +-25, rechterheup +-30,
  10 delen, elk één stuk. Lokaal (Blender 5.3.0, 2 kernen) ook 9.
- **Materiaal (alleen renders, `T.materialen(delen)`):** hout met nodes (ringen om de lengteas van elk deel, vervormd
  met ruis, poriën, vlekken, laklaag 0,35); messing (FFC24A, metaal 0,85) voor alles wat de add-on aan een gewricht
  kleurt plus elk vlak dat verder dan 0,35 mm van de oude buitenkant ligt (kogels, binnenkant van de kom). Let op:
  `materials.clear()` zet alle materiaalindexen op 0, dus eerst onthouden.
- **Renders:** `tekenpop_beelden.py` leest `ontwerp/click-joints-pro-v2/bron/pro_beelden.py` in zonder zijn main()
  (camera, studio B, buigen, kogels, uit elkaar). Shots `staand` (loophouding, 0,45 keer de Exploded view zodat je het
  messing ziet), `uit`, `pop169` (cover B), `dyn169` (delen schuin uit elkaar, alleen voor het beeld). Tekst:
  `tekenpop_cover.py` (hergebruikt `maak_beelden.py`; label -25% alleen in de saleweek, CYBER25 op Gumroad).
- Lokaal sneller proberen: `TP_BEWAAR=/tmp/fig.blend` bewaart het figuur na Figure from rig, `TP_LAAD=/tmp/fig.blend`
  slaat de knop over (20 s per render in plaats van 2,5 minuut).
