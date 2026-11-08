# Click Joints (Blender): winkeltekst (concept)

Door Chris, 8 nov 2026. Eerste concept, terwijl het product nog gebouwd wordt (ronde c op main, Daan nog akkoord nee). De teksten worden definitief als Daan akkoord geeft en de functies vastliggen. Bram zet ze in de winkels.

## Naam
- **"Click Joints" is vrij** (GEZIEN 8 nov): geen extensie met die naam of tagline op extensions.blender.org (alle extensies in de [API](https://extensions.blender.org/api/v1/extensions/), 1.622 op 8 nov), `superhivemarket.com/products/click-joints` en varianten bestaan niet (sturen door naar de voorpagina), 0 GitHub-repo's "clickjoint(s)". Dichtstbij: Click Motion (animatie) en Joint Snapping System (game-assets), andere markt.
- Zwak punt: "click joint" is in de printwereld een beschrijvend woord (flexi-modellen), dus de naam valt in zoekresultaten minder op. Daarom moet de tagline het werk doen. Reserve als Daan toch iets eigens wil: **Socketeer** (geen Blender- of printproduct gevonden, GEZIEN).

Let op: "amber" volgt het voorstel van Daan (Krap wordt amber, `producten/blender-gewrichten/ontwerp.md` beoordeling); blijft het oranje, dan hier ook "orange". "A joint that clicks" schrijven we pas na een echte print.

## Zoekwoorden
- Mensen noemen het probleem: **articulated, poseable, jointed, ball joint, ball and socket, action figure, flexi, snap fit, print-in-place**, en "tolerance" terwijl ze **clearance** bedoelen (GEZIEN, vragen op r/Fusion360, r/3Dprinting en blenderartists.org, zie onder).
- Op extensions.blender.org gebruikt **geen enkele** extensie "articulated", "poseable", "ball joint", "tolerance" of "clearance" (GEZIEN, API). De print-add-ons daar zeggen allemaal "cut", "split" en "connectors". Daar kunnen wij dus vooraan staan.
- Er is geen tag "3D Printing" op extensions.blender.org; verwante add-ons hebben de tags Mesh en Modeling (GEZIEN).
- Echte vragen (GEZIEN): "How to Model a poseable figurine?" (2.163 keer bekeken, https://blenderartists.org/t/1491951), "Trying to shape a section of a mesh to insert a 3d printed ball joint" (1.955, boolean geeft een vuile mesh, https://blenderartists.org/t/1112971), "Split & Joints tool from 3D Coat in Blender?" (1.047, nooit een add-on aangeraden, https://blenderartists.org/t/1319383), "Help Creating a Custom Articulated 3D-Printable Figure" (okt 2026, https://blenderartists.org/t/1656400), "We made 5 joint cutters for 3D printing" (r/3Dprinting, 314 punten, https://www.reddit.com/r/3Dprinting/comments/1t6lo3g/).

## Gratis versie op extensions.blender.org
Alleen de gratis functies, geen woord over de betaalde versie (regels 6.1 tot 6.3, `platformen/blender/kandidaten-2026-11-07.md` sectie 18).
- **Naam:** Click Joints
- **Tagline** (hoogstens 64 tekens, de langste op de site is precies 64, GEZIEN): `Articulated ball and pin joints for 3D printing, with clearance` (63 tekens)
- **Tags:** Mesh, Modeling
- **Beschrijving (concept):**
  > Turn a sculpt into a poseable, printable figure. Click where the joint goes and Click Joints cuts the mesh into two closed, watertight parts with a ball and socket or a pin, sized with the clearance your printer needs, in millimetres.
  >
  > Before you print, the cut shows you whether it fits: green is a good fit, amber is tight, red is too thin or breaks through the surface. Each state also has its own icon, so you don't need to tell red from green.
  >
  > - Ball and socket, or pin and hole
  > - Clearance in mm (0.1 to 0.3 mm is typical)
  > - Fit check on the cut before you export
  > - "Make closed" for open or messy meshes, on a copy, your original stays untouched
  > - Export as STL in millimetres
  > - Tested on Blender 4.2 LTS and 5.2 LTS
  >
  > Support: thijs@dortus.com

## Betaalde versie op Superhive
- **Titel:** Click Joints
- **Korte regel:** `Articulated joints for 3D printed figures, tuned to your printer`
  (niet "see the fit before you print": Cleave waarschuwt al als een verbinder niet past en Split-3DPrint toont de speling als ghost, dus dat is geen onderscheid; de kleur, de eindstop en het testkaartje zijn het wel)
- **Wat de koper erbij krijgt (concept, alleen wat gebouwd is komt erin):** hinge with an end stop for knees and elbows; printer profiles with a test card (print five clearances, pick the one that clicks, Click Joints remembers it per printer); all limbs in one go; magnet holes and friction ribs. Plus alles van de gratis versie.
- **Eerste alinea (concept):**
  > Cutting a figure into parts is easy. Getting a joint that moves, holds a pose and doesn't snap on the first try is not. Click Joints colours the cut by fit before you print, adds hinges that stop where a knee should stop, and remembers the clearance that works on your printer.

## Wat de concurrent mist en wij hebben (GEZIEN 8 nov, productpagina's op superhivemarket.com)
- **Kleur op de passing vooraf:** niemand. Cleave kleurt alleen voor de maat van het printbed ("RED WHEN A PIECE IS TOO BIG"), al waarschuwt het paneel wel als een verbinder niet past; Split-3DPrint toont de speling als ghost; LayerMechanic geeft PASS/FAIL voor een beweging. Uniek is dus de kleur op de snede, niet "de passing zien" op zich.
- **Scharnier met eindstop:** niemand. Cut Flex ("Double hinge") en Articulator hebben een scharnier zonder stop.
- **Testkaartje per printer dat de add-on onthoudt:** niemand. Fit & Tolerance Test Generator ($7) maakt een los testkaartje, zonder gewrichten.
- **De best verkopende splitters bewegen niet:** CatPin (400+) zegt letterlijk "Articulated, rotating and movable joints are not currently supported" ("currently": kan veranderen), Split-3DPrint (400+) en Dovetail Key (800+) maken vaste verbindingen.
- **Eerlijk, wat wij niet als uniek mogen verkopen:** een beweegproef (ledemaat rondtrekken en zien waar hij botst) heeft Cut Flex al ("Check Pose") en LayerMechanic ook. Kogelgewrichten heeft Cleave ook. Zie advies 15.

## Plaatjes (voorstel voor Daan, hij beslist)
1. Poster: het figuur in Blender met de groene ring op de snede. Het moment "het past" moet op het eerste plaatje staan. Een echt geprint figuur erbij pas na de handmatige printproef; geen render die voor een print doorgaat.
2. Dezelfde snede in groen, oranje en rood naast elkaar, met de iconen.
3. Exploded view van een arm met kogel en kom, maten in mm in beeld.
4. (betaald) Testkaartje met vijf spelingen en het gekozen profiel in het paneel.
5. (betaald) Knie met eindstop, gebogen tot de stop.
Op extensions.blender.org alleen 1 tot 3.

## Naam van concurrenten
Niet in titel of tagline (rol). Ook niet in de beschrijving op extensions.blender.org.
