# Click Joints (Blender): lancering

Door Chris, run 4, 8 nov 2026 ±17:00 tot 17:30 UTC. Concept: Click Joints is nog niet live en heeft nog geen akkoord van Daan. Niets hiervan wordt geplaatst voordat de voorwaarden hieronder kloppen en Hans over de plekken heeft beslist (advies 23). Plaatsen gaat via de hoofdchat (een geplande run kan niet bij Chrome).

## Stand (GEZIEN 8 nov ±17:10 UTC)
- Product op main e8602097, ronde n. Beweegproef, rood voorbij de grens en de weigeringen zijn gebouwd en groen in Blender 4.2.23 en 5.2.3 (runs van Bram, zie `platformen/blender/status.md`).
- `producten/blender-gewrichten/ontwerp.md`: "Akkoord: nee" van Daan, 16:27 (beoordeling 3: gradenboog in plaats van waaier, smalle naadband).
- Niet live: geen extensie "click joints" op extensions.blender.org (API, 1.622 extensies), geen pagina op Superhive. De accounts op beide plekken zijn een stap voor Thijs (staat op lijst-thijs, niet dringend).
- Het betaalde deel (scharnier met eindstop, printerprofielen, alle ledematen) is nog niet gebouwd. Deze berichten gaan daarom alleen over de gratis versie.

## Voorwaarden voor het eerste bericht
1. Daan zet `Akkoord: ja` en de lijstplaatjes staan (de gradenboog is ons beeld; zonder dat plaatje geen bericht).
2. De gratis versie staat live op extensions.blender.org (link werkt, met curl gezien).
3. **Een echte print.** Bram noemt in het ontwerp een handmatige printproef. Wie print, is nog open: of Thijs een printer heeft, staat nergens in de repo; Bram schreef op de lijst van Thijs (8 nov 01:35) dat hij later misschien vraagt of Thijs of iemand die hij kent één testgewricht kan printen; de vraag staat ook in advies 23. Op een printforum is de eerste vraag "did you print it?". Zonder foto van een geprint gewricht dat buigt, plaatsen we niet op r/3Dprinting. Op r/blender mag het wel zonder, maar dan staat er eerlijk dat het nog niet geprint is.
4. Hans heeft over de plekken beslist in `berichten/chris.md` (de toestemming van Thijs noemt alleen de drie Obsidian-plekken).
5. De hoofdchat leest vlak voor het plaatsen de regels van de plek in de browser (Reddit-regels zijn met curl niet te lezen, zie onder).

## Plekken en hun regels

| Plek | Regels gelezen | Bewijs voor bereik | Oordeel |
|---|---|---|---|
| extensions.blender.org (de listing zelf) | ToS 6.1 tot 6.3, zie `platformen/blender/kandidaten-2026-11-07.md` sectie 18: geen verwijzing naar de betaalde versie | ±1.000 tot 1.500 downloads per nieuwe add-on (GEZIEN 6 nov, Vera) | ja, dit is de lancering zelf |
| r/3Dprinting | niet te lezen met curl (403, inlogmuur), niet omzeild; ook niet via spiegelsites | "We made 5 joint cutters for 3D printing", 314 punten (GEZIEN 8 nov, https://www.reddit.com/r/3Dprinting/comments/1t6lo3g/) | ja, eerste bericht na de listing, alleen met echte print |
| r/blender | idem, 403 | groot publiek, geen eigen meting voor add-on-berichten (GOK) | ja, minstens één dag na r/3Dprinting |
| BlenderNation (nieuwssite) | GEZIEN, https://www.blendernation.com/submit-news/: een bericht over iets commercieels kost € 25 of een Patreon-lidmaatschap; een gratis product niet | GOK | alleen de gratis versie, zonder Superhive, na besluit Hans; nooit betalen |
| BlenderArtists, Released Add-ons and Extensions | GEZIEN: hoogstens één bericht over eigen werk per week, updates in dezelfde draad, tag `free` of `commercial` verplicht (https://blenderartists.org/t/1276424, https://blenderartists.org/t/1416473); een nieuw account kan daar niet plaatsen tot het "some time engaging with the community" heeft meegedaan (moderator, 17 okt 2026, https://blenderartists.org/t/1655257) | zwak: "Bed Fit Splitter", een print-add-on, 88 keer bekeken en 0 likes in 7 weken (GEZIEN, https://blenderartists.org/t/1653313) | nee bij de lancering: eerst meedoen op het forum, en dat zou posten onder de naam van Thijs zijn buiten een lanceerbericht |
| Superhive (de listing zelf) | pas als het betaalde deel gebouwd is | 31% van nieuwe betaalde add-ons 10+ verkopen (Vera) | later |

## Eerlijk over wie het maakte
Zelfde vorm als bij Rollwright: "I made Click Joints", en één zin dat AI-agents van Dortus de code schrijven, Thijs stuurt het werk, en dat elke versie automatisch in de echte Blender 4.2 en 5.2 getest wordt. Slotregel "Made by Thijs at Dortus". Geen persoonlijke printverhalen die niet van Thijs zijn ("I print a lot of figures" schrijven we niet).

## Concept A: r/3Dprinting (na echte print; nagekeken door controleur, akkoord mits, moet-punten verwerkt)
**Titel:** `I made a free Blender add-on that cuts a ball joint into your figure and tells you how far it bends before you print`

**Tekst:**
> I made Click Joints, a free Blender add-on for turning a sculpt into a poseable print.
>
> You set the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket (or a pin and hole), with the clearance you set in mm (0.1 to 0.3 mm is typical).
>
> Right after the cut it shows two things:
> - How far the ball joint bends before the parts collide, measured in 8 directions, for example "Bends ±25°". Tilt the part past that and the spot where it hits turns red.
> - The fit: a ring on the cut is green (good), yellow (tight) or red (too thin), and the panel gives the wall thickness in mm.
>
> If a spot is too thin for a ball joint, it says so instead of giving you a broken part. Export is STL or 3MF, one file per part, in mm.
>
> [foto: het geprinte gewricht, gebogen] [plaatje: de gradenboog in Blender]
>
> Free on the Blender Extensions platform: <link>. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> Honest note: the code is written by AI agents that my small studio, Dortus, runs. I direct the work; every version is tested automatically in real Blender 4.2 and 5.2.
>
> A question for people who print jointed figures: which clearance works for ball joints on your printer?
>
> Made by Thijs at Dortus

Waarom zo: de titel zegt wat het doet en wat je eraan hebt, zonder "the only" (we hebben de concurrenten niet gekocht). Het buigen staat bovenaan, want dat laat de gradenboog zien. De vraag aan het eind geeft reacties waar wij van leren (welke speling), en die kunnen we met feiten beantwoorden.

## Concept B: r/blender (minstens één dag later)
**Titel:** `I made Click Joints: cut a printable ball joint into a mesh and see how far it bends (free extension)`

**Tekst:**
> I made Click Joints, a free extension for 3D printing poseable figures from Blender.
>
> Set the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket or a pin, with clearance in mm. For a ball joint it measures the bend range in 8 directions and shows it in the viewport ("Bends ±25°"); past the limit the colliding spot turns red. A ring on the cut shows the fit in green, yellow or red, with the reason in the panel.
>
> Tested on Blender 4.2 LTS and 5.2 LTS. Exploded view, "Make watertight" on a copy, export to STL or 3MF in mm.
>
> <link>
>
> Honest note: the code is written by AI agents that my small studio, Dortus, runs. I direct the work; every version is tested automatically in real Blender 4.2 and 5.2.
>
> Made by Thijs at Dortus

Zonder echte print: zin erbij "I haven't printed a full figure with it yet; the fit and bend are measured in Blender." Dan geen beweringen over hoe het geprint aanvoelt.

## Concept C: BlenderNation (alleen na besluit Hans, alleen de gratis versie)
Vraag "Is your post about a commercial product?": **No**, alleen als de tekst niets over Superhive zegt. Zodra het betaalde deel bestaat en genoemd wordt, is het commercieel en kost het geld: dan niet.
> **Click Joints: printable ball joints that show how far they bend (free)**
>
> Thijs writes: I made Click Joints, a free extension that cuts a ball and socket or a pin joint into a mesh for 3D printing. For a ball joint it measures how far the joint bends in 8 directions before the parts collide, and shows the angle in the viewport. A ring on the cut shows whether the wall is thick enough. Export to STL or 3MF in millimetres. Tested on Blender 4.2 LTS and 5.2 LTS.
>
> <link naar extensions.blender.org> <link naar korte video>

## Volgorde
1. Listing op extensions.blender.org live (Thijs doet de eerste aanmelding, Bram stuurt in).
2. r/3Dprinting, alleen met echte print.
3. Minstens één dag later, en alleen als 2 niet verwijderd is en geen moderator waarschuwde: r/blender.
   Kan niemand printen: dan r/blender als eerste bericht na de listing (met de zin "I haven't printed a full figure with it yet"), en r/3Dprinting pas na een echte print.
4. BlenderNation na besluit Hans.
5. BlenderArtists niet bij de lancering.
Per plek één bericht. Reageren alleen in de eigen draad, als concept in `berichten-geplaatst.md` (nog niet aangemaakt, komt bij het eerste bericht).

## Wat dit plan zou veranderen
- De regels van r/3Dprinting of r/blender verbieden eigen add-ons of eisen iets wat we niet kunnen (bijvoorbeeld minimaal karma): die plek valt af, zet het op de lijst van Thijs.
- De printproef mislukt (het gewricht klikt niet of breekt): geen r/3Dprinting, eerst de vorm repareren (Bram).
- Een gratis gewrichten-extensie verschijnt eerder op extensions.blender.org: de titel en de eerste zin opnieuw toetsen.
