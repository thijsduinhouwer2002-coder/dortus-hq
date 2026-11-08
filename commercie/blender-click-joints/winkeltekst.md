# Click Joints (Blender): winkeltekst (concept)

Door Chris, 8 nov 2026. Concept, terwijl het product nog gebouwd wordt. De teksten worden definitief als Daan akkoord geeft en de functies vastliggen. Bram zet ze in de winkels.

**Bijgewerkt 8 nov ±09:00 (Chris, run 2) naar ronde h op main (4a9a585c):** Tight is nu geel `#FFEA00` (niet amber of oranje), groen `#00D696`; export STL of 3MF; Auto kiest de grootste kogel met Good fit; Exploded view; de knop heet "Make watertight"; het paneel zegt waarom ("Tight: wall 0.89 mm (aim for 1.5 mm or more)"). Alles nagelezen in de code (`click_joints/passing.py`, `paneel.py`, `eigenschappen.py`, GEZIEN). Nieuw: de beweegproef als betaald onderscheid, zie onder en advies 17.

**Bijgewerkt 8 nov ±10:50 UTC (Chris, run 3) naar het besluit van Bram en vorm v0.3:** Bram zette in de zin "waarom wij" bovenaan `producten/blender-gewrichten/ontwerp.md` (09:35) de beweegproef in de **gratis** versie, omdat het hoofdplaatje en de poster ook op extensions.blender.org moeten mogen (ToS 6.2). Dat is zijn besluit; mijn advies 17 (a) (beweegproef betaald) vervalt daarmee, en deze tekst volgt hem, want de belofte moet overal hetzelfde zijn (regel "Elk product"). Verder nieuw: de bolnaad buigt in de echte Blender 30,0° in alle 8 richtingen (beweegproef run 42470659128, GEZIEN door Bram, tak `-j`), Daan besliste dat Auto per gewricht 30°, 25° of 20° kiest, dat het paneel de gemeten waarde toont ("Bends ±25°") en dat de add-on eerlijk weigert op een te dunne plek of te dicht bij een ander gewricht (reactie op v0.3). Gebouwd zijn tot nu toe alleen de standen 30° en 25° (10:32); 20° en de twee weigerregels nog niet. Alles over buigen blijft gemarkeerd als "pas na bouw": het paneel toont de hoek nog niet en de beweegproef staat nog niet op main.

**Bijgewerkt 8 nov ±17:20 UTC (Chris, run 4) naar main e8602097 (ronde k tot n):** de beweegproef staat op main met groene runs in 4.2.23 en 5.2.3 (ronde k 42485768696, l 42489692585, n 42499399232, GEZIEN door Bram en zijn controleur). Alles wat hieronder "pas na bouw" heette over buigen, is nu gebouwd: hoekstand 30, 25 of 20 graden per kogelgewricht, paneelregel "Bends ±25°" (`paneel.py`), voorbij de grens worden de botsende vlakken van deel A rood, ook bij botsing met het figuur zelf, en de twee eerlijke weigeringen "Too thin here for a ball joint. Try a thicker spot." (`maat.py`) en "Too close to another joint (keep N mm apart)." (`gewricht.py`, N per geval berekend), zelf nagelezen in de code (GEZIEN). Let op: het bereik wordt alleen bij een **kogel** gemeten, niet bij de pen. Wat nog niet vastligt: Daan gaf 16:27 "Akkoord: nee" (beoordeling 3): de waaier wordt een gradenboog met het getal op het model, en de schuif "Pose" heet straks misschien "Bend" (kan-punt 3). Daarom noemt de nieuwe tekst geen "fan" en geen naam van de schuif. Nieuwe beschrijving: zie "Beschrijving run 4 (geldt)" hieronder. Drie dingen die nu nog niet overal gelijk zijn: zie "Wat nog niet overal hetzelfde is (run 4)" en advies 23.

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
- **Beschrijving (concept, ronde h), vervangen door "Beschrijving run 4 (geldt)" hieronder:**
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

  **Pas na bouw (beweegproef op main, groene test, Daan akkoord), dan komt dit erbij.** Als tweede alinea, na "Click where the joint goes ...":
  > Then it tells you how far the joint bends before the parts collide. Auto picks the widest swing that still fits, and the panel shows the measured angle, for example "Bends ±25°". Drag the limb and the spot where it hits turns red.

  En als eerste punt in het lijstje: `- Range of motion: the measured bend per joint, in degrees, before you print`. En als laatste punt: `- Honest limits: a spot too thin for a ball joint, or too close to another joint, is refused with a clear message instead of a broken part`.
  Waarom "for example" en geen vast getal: Auto kiest per gewricht 30°, 25° of 20° (Daan), dus één getal in de tekst zou bij een dun lid niet kloppen. Waarom niet "clicks": de add-on meet wand, speling en hoek, niet of het klikt (zie onder, advies 18).

  Waarom zo: "Auto" en "the panel tells you why" laten zien dat het nadenkt voor de gebruiker (dat heeft geen splitter, GEZIEN vanochtend); "0.1 to 0.3 mm is typical" blijft, want mensen zoeken op tolerance en weten niet welke waarde. "Watertight" is het woord dat printers gebruiken en staat zo ook op de knop. Geen woord over beweging zolang de beweegproef niet gebouwd is.

### Beschrijving run 4 (geldt, concept tot Daan akkoord geeft)
Nagelezen tegen de code op main e8602097 (GEZIEN). Elke bewering staat in de add-on; geen "clicks", geen getal dat bij een dun lid niet klopt.
- **Tagline** (hoogstens 64 tekens): `Ball joints for 3D printed figures that show their bend range` (61 tekens; de pen staat in de beschrijving, want bij de pen meten we geen bereik). Waarom nieuw: de beweegproef is nu het sterkste wat we hebben en staat bij geen enkele extensie (GEZIEN, API 1.622 extensies, 17:00 UTC: alleen Better Ragdoll noemt "joint", andere markt). "Articulated" en "clearance" staan in de beschrijving, daar zoekt de site ook op (GOK over hoe zwaar de zoekfunctie de beschrijving telt).
- **Beschrijving:**
  > Turn a sculpt into a poseable, printable figure. Set the 3D cursor where the joint goes, click Place joint, and Click Joints cuts the mesh into two watertight parts with a ball and socket or a pin, sized with the clearance your printer needs, in millimetres.
  >
  > For a ball joint it then measures how far the joint bends before the parts collide, in 8 directions, and shows that range in the viewport. Auto picks the widest bend with the best fit (30°, 25° or 20°), and the panel shows the measured angle, for example "Bends ±25°". Tilt the part past that limit and the spot where it hits turns red.
  >
  > A ring on the cut shows the fit: green is a good fit, yellow is tight, red is too thin or breaks through the surface. The panel tells you why, for example "Tight: wall 0.89 mm (aim for 1.5 mm or more)".
  >
  > - Range of motion: the measured bend of every ball joint, in degrees, before you print
  > - Ball and socket, or pin and hole
  > - Auto size: picks the largest ball with a good fit, or tells you when none fits well
  > - Clearance in mm (0.1 to 0.3 mm is typical)
  > - Exploded view, so you see the ball and socket apart; the export stays in place
  > - "Make watertight" for open or messy meshes, on a copy; your original stays untouched
  > - Export as STL or 3MF, one file per part, in millimetres
  > - Honest limits: a spot too thin for a ball joint, or too close to another joint, is refused with a clear message instead of a broken part
  > - Tested on Blender 4.2 LTS and 5.2 LTS
  >
  > Support: thijs@dortus.com

  Waarom zo: het buigen staat nu als tweede alinea, want dat heeft niemand (zie "Wat de concurrent mist"), en Daan wil de gradenboog als hoofdbeeld; tekst en beeld vertellen zo hetzelfde verhaal. "Tilt the part" in plaats van de naam van de schuif, omdat die naam nog kan veranderen. Verandert de stand of de tekst in het paneel nog, dan pas ik deze zinnen aan voor het insturen.

### Wat nog niet overal hetzelfde is (run 4)
Regel "Elk product": de belofte moet overal precies hetzelfde zijn. Nu (GEZIEN 17:10 UTC):
1. **Tagline in `click_joints/blender_manifest.toml`:** `Cut a figure into two printable parts with a ball joint`, en tags `Mesh, Modeling, Import-Export`. Mijn tekst: zie hierboven, tags Mesh en Modeling. Het manifest is wat de site toont, dus dat moet gelijk worden (Bram). Import-Export mag blijven als Bram de export als zoekingang wil; ik zie geen bewijs voor of tegen (GOK).
2. **Winkelzin bovenaan `ontwerp.md`:** nog `See if it clicks, and how far it bends, before you print.` Advies 18 (open) vraagt `See the fit, and how far it bends, before you print.`
3. **Poster van Daan (beoordeling 3):** `See how far it bends, before you print.` Dat past bij advies 18 (geen klik) en is korter. Voorstel: dit wordt de ene zin overal (poster, winkelzin, eerste regel op Superhive en in de lanceerberichten), met daarachter `Ball and pin joints free; hinges, printer profiles and full-figure setup for $12.` zodra het betaalde deel gebouwd is. Bram en Daan beslissen; zie advies 23.
4. **Rest van de zin "waarom wij" in `ontwerp.md`:** "de enige Blender-add-on" (niet te bewijzen, we kochten de concurrenten niet) en "kogel en pen met die controle" (bij de pen wordt geen bereik gemeten). Ook advies 18.
5. **Bestandstoestemming in het manifest** noemt alleen STL, de add-on schrijft ook 3MF (al genoemd als kan-punt in advies 17).

## Betaalde versie op Superhive
- **Titel:** Click Joints
- **Korte regel:** `Articulated joints for 3D printed figures, tuned to your printer`
  (niet "see the fit before you print": Cleave waarschuwt al als een verbinder niet past en Split-3DPrint toont de speling als ghost, dus dat is geen onderscheid; de kleur, de eindstop en het testkaartje zijn het wel)
**Let op: het hele Superhive-deel is pas na bouw.** Geen van de betaalde functies is gebouwd (de bouw gaat nu nog over vorm v0.3). Elke functie komt pas in de tekst als hij op main staat met een groene test.
- **Wat de koper erbij krijgt (concept, alleen wat gebouwd is komt erin):** hinge with an end stop for knees and elbows (bends from straight to where a knee should stop, for example 0° to 115°); printer profiles with a test card (print five clearances, pick the one that fits best, Click Joints remembers it per printer); all limbs in one go; magnet holes and friction ribs. Plus alles van de gratis versie, ook de beweegproef (besluit Bram, run 3 hierboven).
- **Eerste alinea (concept, run 3):**
  > Cutting a figure into parts is easy. Getting a whole figure that moves, holds a pose and doesn't snap on the first try is not. Click Joints colours every cut by fit and tells you how far each joint bends before you print. This version adds what a full figure needs: hinges that stop where a knee or elbow should stop, all limbs in one go, and the clearance that works on your printer, remembered per printer.

  Waarom zo: de koper op Superhive ziet de gratis functies ook (kleur, bereik) als reden om Click Joints te kiezen boven Cleave of Cut Flex, en de betaalde functies als reden om te betalen in plaats van de gratis versie te houden. Het verschil is "één gewricht" tegen "een heel figuur". De zinnen over buigen pas na bouw.

## De belofte in één zin (overal gelijk)
Van Bram (ontwerp), met de wijziging uit advies 18: `See the fit, and how far it bends, before you print. Ball and pin joints free; hinges, printer profiles and full-figure setup for $12.` Het deel "and how far it bends" pas na bouw van de beweegproef; tot dan: `See the fit before you print. Ball and pin joints free; hinges, printer profiles and full-figure setup for $12.`

## Wat de concurrent mist en wij hebben (GEZIEN 8 nov, productpagina's op superhivemarket.com)
- **De wand in mm per gewricht:** niemand op de productpagina (GEZIEN 8 nov ±10:50, curl, run 3, open vraag van Bram in de zin "waarom wij"). Cleave: "The panel warns when a connector does not fit" (een waarschuwing, geen maat); FigureCut: "warnings when a cut needs attention"; Cut Flex: "very thin areas may need repair or a different cut position" (advies in de FAQ over welke mesh geschikt is, geen melding in de add-on); LayerMechanic meet speling tijdens een beweging, geen wand. Let op: dit is wat de pagina's beloven, niet wat de add-ons zelf tonen; we hebben ze niet gekocht. Dus "shows the wall in mm" mag als feit over ons, niet als "nobody else does".
- **Kleur op de passing vooraf:** niemand. Cleave kleurt alleen voor de maat van het printbed ("RED WHEN A PIECE IS TOO BIG"), al waarschuwt het paneel wel als een verbinder niet past; Split-3DPrint toont de speling als ghost; LayerMechanic geeft PASS/FAIL voor een beweging. Uniek is dus de kleur op de snede, niet "de passing zien" op zich.
- **Scharnier met eindstop:** niemand. Cut Flex ("Double hinge") en Articulator hebben een scharnier zonder stop.
- **Testkaartje per printer dat de add-on onthoudt:** niemand. Fit & Tolerance Test Generator ($7) maakt een los testkaartje, zonder gewrichten.
- **De best verkopende splitters bewegen niet:** CatPin (400+) zegt letterlijk "Articulated, rotating and movable joints are not currently supported" ("currently": kan veranderen), Split-3DPrint (400+) en Dovetail Key (800+) maken vaste verbindingen.
- **Gemeten bewegingsbereik in graden met de botsplek in rood:** niemand (onderzoek Bram ronde h, GEZIEN op de productpagina's): Cut Flex ($34,99) "Check Pose" toetst één houding per keer, zonder hoekbereik en zonder pennen; LayerMechanic ($25) meet een eerste aanslag in graden, maar alleen voor een scharnier dat je zelf modelleert; Interference Checker ($6,99) kleurt raakvlakken, maar staat stil. Uniek is dus "hoe ver buigt het, meteen na het maken", niet "beweging nakijken" op zich.
- **Eerlijk, wat wij niet als uniek mogen verkopen:** 3MF-export (gratis extensie met 118.387 downloads, GEZIEN). Beweging nakijken op zich (één houding toetsen) heeft Cut Flex al ("Check Pose"), en LayerMechanic meet een scharnier dat je zelf instelt; alleen het vanzelf gemeten bereik van een kogel is van ons. Kogelgewrichten heeft Cleave ook. Zie advies 15 en 17.

## Plaatjes (voorstel voor Daan, hij beslist)
**Bijgewerkt run 3:** de beweegproef is gratis (Bram), dus het buigende gewricht mag nu op de poster en op extensions.blender.org. Dat is het sterkste beeld en past bij Daan ("het buigende gewricht als hoofdbeeld"). Op Superhive wordt het betaalde plaatje dan de knie met eindstop (mijn reserve uit advies 17).
1. Poster: het figuur in Blender met de groene ring op de snede en het opengewerkte gewricht groot (zoals Daan zelf voorstelt, beoordeling 2 punt 4). Een echt geprint figuur erbij pas na de handmatige printproef; geen render die voor een print doorgaat. **Kopregel:** Daan noemde "See if it clicks before you print". Dat belooft een klik die we niet meten; voorstel: **"See the fit before you print"** tot een echte print het bewijst (advies 17). Op extensions.blender.org past die zin wel als kop: daar staat geen enkele gewrichten-extensie, dus is hij daar wel uniek; op Superhive is hij geen onderscheid, daar wordt plaatje 7 of 6 het eerste (bijgewerkt run 3, zie onder).
2. Dezelfde snede in groen, geel en rood naast elkaar, met de iconen en de regel uit het paneel ("Tight: wall 0.89 mm ..."). De Tight- en Too thin-schermen komen uit de test met de dunne pop (Bram, ronde g).
3. Exploded view van een arm met kogel en kom, maten in mm in beeld, en STL | 3MF in het paneel.
4. (gratis, pas na bouw) Beweegproef: de waaier met de grens per richting en de echte regel uit het paneel ("Bends ±30°" of wat Auto meet), één richting voorbij de grens met de botsplek rood. ~~"Bends 40° to 115°"~~: dat getal klopt niet voor een kogel (standen 20°, 25° en 30° volgens Daan, gemeten 30,0° in alle 8 richtingen, GEZIEN door Bram), zulke hoeken horen bij het scharnier.
5. (betaald) Testkaartje met vijf spelingen en het gekozen profiel in het paneel.
6. (betaald) Knie met eindstop, gebogen tot de stop, met de hoek ("0° to 115°" of wat gebouwd wordt).
7. (betaald) Een heel figuur met alle ledematen in één keer, elk gewricht met zijn ring.
Op extensions.blender.org 4 (zodra gebouwd), 1, 2, 3. Op Superhive 7 of 6 als eerste plaatje (wat Daan het sterkst vindt), dan 4, 1, 5. Advies: het getal ±20° of ±25° niet groot op de poster; de waaier met rood laat het verschil zien, en op een dun lid is 20° eerlijk maar klinkt het klein (GOK over hoe kopers dat lezen).

## Naam van concurrenten
Niet in titel of tagline (rol). Ook niet in de beschrijving op extensions.blender.org.
