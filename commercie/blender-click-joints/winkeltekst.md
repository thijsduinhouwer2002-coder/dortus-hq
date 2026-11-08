# Click Joints (Blender): winkeltekst (concept)

Door Chris, 8 nov 2026. Concept, terwijl het product nog gebouwd wordt. De teksten worden definitief als Daan akkoord geeft en de functies vastliggen. Bram zet ze in de winkels.

**Bijgewerkt 8 nov ±09:00 (Chris, run 2) naar ronde h op main (4a9a585c):** Tight is nu geel `#FFEA00` (niet amber of oranje), groen `#00D696`; export STL of 3MF; Auto kiest de grootste kogel met Good fit; Exploded view; de knop heet "Make watertight"; het paneel zegt waarom ("Tight: wall 0.89 mm (aim for 1.5 mm or more)"). Alles nagelezen in de code (`click_joints/passing.py`, `paneel.py`, `eigenschappen.py`, GEZIEN). Nieuw: de beweegproef als betaald onderscheid, zie onder en advies 17.

## Naam
- **"Click Joints" is vrij** (GEZIEN 8 nov): geen extensie met die naam of tagline op extensions.blender.org (alle extensies in de [API](https://extensions.blender.org/api/v1/extensions/), 1.622 op 8 nov), `superhivemarket.com/products/click-joints` en varianten bestaan niet (sturen door naar de voorpagina), 0 GitHub-repo's "clickjoint(s)". Dichtstbij: Click Motion (animatie) en Joint Snapping System (game-assets), andere markt.
- Zwak punt: "click joint" is in de printwereld een beschrijvend woord (flexi-modellen), dus de naam valt in zoekresultaten minder op. Daarom moet de tagline het werk doen. Reserve als Daan toch iets eigens wil: **Socketeer** (geen Blender- of printproduct gevonden, GEZIEN).

Let op: de kleur heet in de tekst "yellow" (Daan koos `#FFEA00`, ontwerp ronde h; in Material Preview wordt hij iets bleker maar blijft geel, GEZIEN door Bram). Het woord in het paneel is "Tight", niet de kleur. "A joint that clicks" en "see if it clicks" schrijven we pas na een echte print: de add-on meet wand en speling, niet of het klikt.

## Zoekwoorden
- Mensen noemen het probleem: **articulated, poseable, jointed, ball joint, ball and socket, action figure, flexi, snap fit, print-in-place**, en "tolerance" terwijl ze **clearance** bedoelen (GEZIEN, vragen op r/Fusion360, r/3Dprinting en blenderartists.org, zie onder).
- Op extensions.blender.org gebruikt **geen enkele** extensie "articulated", "poseable", "ball joint", "tolerance" of "clearance" (GEZIEN, API). De print-add-ons daar zeggen allemaal "cut", "split" en "connectors". Daar kunnen wij dus vooraan staan.
- Er is geen tag "3D Printing" op extensions.blender.org; verwante add-ons hebben de tags Mesh en Modeling (GEZIEN).
- **3MF** is een zoekwoord met bewezen vraag: de gratis extensie "3MF Import/Export" heeft 118.387 downloads (GEZIEN 8 nov, https://extensions.blender.org/add-ons/threemf-io/). Dus 3MF noemen we, maar niet als iets bijzonders: wie 3MF wil, heeft die extensie al. Ons voordeel is alleen gemak (één bestand per deel, altijd in mm, zonder extra extensie).
- Herhaalmeting 8 nov ±09:00 (GEZIEN, API, 1.622 extensies, gelijk aan vanochtend): nog steeds geen extensie met articulated, poseable, ball joint, clearance of tolerance in naam of tagline. Enige met "joint" is Better Ragdoll (physics, andere markt).
- Echte vragen (GEZIEN): "How to Model a poseable figurine?" (2.163 keer bekeken, https://blenderartists.org/t/1491951), "Trying to shape a section of a mesh to insert a 3d printed ball joint" (1.955, boolean geeft een vuile mesh, https://blenderartists.org/t/1112971), "Split & Joints tool from 3D Coat in Blender?" (1.047, nooit een add-on aangeraden, https://blenderartists.org/t/1319383), "Help Creating a Custom Articulated 3D-Printable Figure" (okt 2026, https://blenderartists.org/t/1656400), "We made 5 joint cutters for 3D printing" (r/3Dprinting, 314 punten, https://www.reddit.com/r/3Dprinting/comments/1t6lo3g/).

## Gratis versie op extensions.blender.org
Alleen de gratis functies, geen woord over de betaalde versie (regels 6.1 tot 6.3, `platformen/blender/kandidaten-2026-11-07.md` sectie 18).
- **Naam:** Click Joints
- **Tagline** (hoogstens 64 tekens, de langste op de site is precies 64, GEZIEN): `Articulated ball and pin joints for 3D printing, with clearance` (63 tekens)
- **Tags:** Mesh, Modeling
- **Beschrijving (concept, ronde h):**
  > Turn a sculpt into a poseable, printable figure. Click where the joint goes and Click Joints cuts the mesh into two watertight parts with a ball and socket or a pin, sized with the clearance your printer needs, in millimetres.
  >
  > Before you export, a ring on the cut shows the fit: green is a good fit, yellow is tight, red is too thin or breaks through the surface. Each state has its own icon, and the panel tells you why, for example "Tight: wall 0.89 mm (aim for 1.5 mm or more)".
  >
  > - Ball and socket, or pin and hole
  > - Auto size: picks the largest ball that still fits the mesh
  > - Clearance in mm (0.1 to 0.3 mm is typical)
  > - Exploded view, so you see the ball and socket apart; the export stays in place
  > - "Make watertight" for open or messy meshes, on a copy, your original stays untouched
  > - Export as STL or 3MF, one file per part, in millimetres
  > - Tested on Blender 4.2 LTS and 5.2 LTS
  >
  > Support: thijs@dortus.com

  Waarom zo: "Auto" en "the panel tells you why" laten zien dat het nadenkt voor de gebruiker (dat heeft geen splitter, GEZIEN vanochtend); "0.1 to 0.3 mm is typical" blijft, want mensen zoeken op tolerance en weten niet welke waarde. "Watertight" is het woord dat printers gebruiken en staat zo ook op de knop. Geen woord over beweging zolang de beweegproef niet gebouwd is.

## Betaalde versie op Superhive
- **Titel:** Click Joints
- **Korte regel:** `Articulated joints for 3D printed figures, tuned to your printer`
  (niet "see the fit before you print": Cleave waarschuwt al als een verbinder niet past en Split-3DPrint toont de speling als ghost, dus dat is geen onderscheid; de kleur, de eindstop en het testkaartje zijn het wel)
- **Wat de koper erbij krijgt (concept, alleen wat gebouwd is komt erin):** **range of motion test: see how far each joint bends, in degrees, with the collision shown in red** (voorstel, advies 17; ontwerp van Bram, ronde h; pas in de tekst en op plaatje 4 na bouw, groene test en controle); hinge with an end stop for knees and elbows; printer profiles with a test card (print five clearances, pick the one that clicks, Click Joints remembers it per printer); all limbs in one go; magnet holes and friction ribs. Plus alles van de gratis versie.
- **Eerste alinea (concept):**
  > Cutting a figure into parts is easy. Getting a joint that moves, holds a pose and doesn't snap on the first try is not. Click Joints colours the cut by fit before you print, tells you how far each joint bends before parts collide, adds hinges that stop where a knee should stop, and remembers the clearance that works on your printer.

  (De zin over buigen alleen als de beweegproef in de betaalde versie zit. Anders valt hij weg.)

## Wat de concurrent mist en wij hebben (GEZIEN 8 nov, productpagina's op superhivemarket.com)
- **Kleur op de passing vooraf:** niemand. Cleave kleurt alleen voor de maat van het printbed ("RED WHEN A PIECE IS TOO BIG"), al waarschuwt het paneel wel als een verbinder niet past; Split-3DPrint toont de speling als ghost; LayerMechanic geeft PASS/FAIL voor een beweging. Uniek is dus de kleur op de snede, niet "de passing zien" op zich.
- **Scharnier met eindstop:** niemand. Cut Flex ("Double hinge") en Articulator hebben een scharnier zonder stop.
- **Testkaartje per printer dat de add-on onthoudt:** niemand. Fit & Tolerance Test Generator ($7) maakt een los testkaartje, zonder gewrichten.
- **De best verkopende splitters bewegen niet:** CatPin (400+) zegt letterlijk "Articulated, rotating and movable joints are not currently supported" ("currently": kan veranderen), Split-3DPrint (400+) en Dovetail Key (800+) maken vaste verbindingen.
- **Gemeten bewegingsbereik in graden met de botsplek in rood:** niemand (onderzoek Bram ronde h, GEZIEN op de productpagina's): Cut Flex ($34,99) "Check Pose" toetst één houding per keer, zonder hoekbereik en zonder pennen; LayerMechanic ($25) meet een eerste aanslag in graden, maar alleen voor een scharnier dat je zelf modelleert; Interference Checker ($6,99) kleurt raakvlakken, maar staat stil. Uniek is dus "hoe ver buigt het, meteen na het maken", niet "beweging nakijken" op zich.
- **Eerlijk, wat wij niet als uniek mogen verkopen:** 3MF-export (gratis extensie met 118.387 downloads, GEZIEN). Beweging nakijken op zich (één houding toetsen) heeft Cut Flex al ("Check Pose"), en LayerMechanic meet een scharnier dat je zelf instelt; alleen het vanzelf gemeten bereik van een kogel is van ons. Kogelgewrichten heeft Cleave ook. Zie advies 15 en 17.

## Plaatjes (voorstel voor Daan, hij beslist)
1. Poster: het figuur in Blender met de groene ring op de snede en het opengewerkte gewricht groot (zoals Daan zelf voorstelt, beoordeling 2 punt 4). Een echt geprint figuur erbij pas na de handmatige printproef; geen render die voor een print doorgaat. **Kopregel:** Daan noemde "See if it clicks before you print". Dat belooft een klik die we niet meten; voorstel: **"See the fit before you print"** tot een echte print het bewijst (advies 17). Op extensions.blender.org past die zin wel als kop: daar staat geen enkele gewrichten-extensie, dus is hij daar wel uniek; op Superhive is hij geen onderscheid, daar wordt plaatje 4 (beweegproef) het eerste.
2. Dezelfde snede in groen, geel en rood naast elkaar, met de iconen en de regel uit het paneel ("Tight: wall 0.89 mm ..."). De Tight- en Too thin-schermen komen uit de test met de dunne pop (Bram, ronde g).
3. Exploded view van een arm met kogel en kom, maten in mm in beeld, en STL | 3MF in het paneel.
4. (betaald) Beweegproef: de waaier met de grens per richting en "Bends 40° to 115°", één richting voorbij de grens met de botsplek rood. Dit wordt het hoofdplaatje op Superhive.
5. (betaald) Testkaartje met vijf spelingen en het gekozen profiel in het paneel.
6. (betaald) Knie met eindstop, gebogen tot de stop.
Op extensions.blender.org alleen 1 tot 3. Op Superhive 4 als eerste plaatje, dan 1, 2, 5, 6.

## Naam van concurrenten
Niet in titel of tagline (rol). Ook niet in de beschrijving op extensions.blender.org.
