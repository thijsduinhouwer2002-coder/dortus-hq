# Blender Stack Exchange: antwoord op "Trying to shape a section of a mesh to insert a 3d printed ball joint" (gratis Click Joints)

Door de Verspreider, do 26 nov 2026 ±19:00 NL (run 31, A). Niets geplaatst. **Daan ja (8, #211); M1 letterlijk verwerkt ("Tested on Blender 4.2 LTS and 5.2 LTS:") en kan-punt ring ("shows the fit: yellow when tight, red when the wall is too thin"), run 33. In `commercie/outreach/bundel-2026-11-30.md`.** Keuring: Daan (issue "Keur: Stack Exchange-antwoord kogelgewricht"). Plaatsen: Thijs, met zijn eigen Stack Exchange-account (account maken en plaatsen kan alleen hij). Staat onder zijn naam, dus na Daans ja in de bundel voor Thijs. Telt niet als Reddit-ding.

## De plek
- Vraag: https://blender.stackexchange.com/questions/109488 (mei 2018, tags modeling, modifiers, 3d-printing). Iemand wil kogelgewrichten in zijn eigen figuur zetten (naar een geprinte octopus met kogelgewrichten), maakt een vorm om uit te snijden, en krijgt met Boolean en "Auto Boolean" steeds lelijke randen; "it looks horrible smoothed, but sort of ok flat". Vraagt ook hoe hij de ogen bij het lichaam krijgt voor het printen.
- 323 weergaven, score 2, **0 antwoorden**, niet gesloten (GEZIEN, api.stackexchange.com, 26 nov ±19:00 NL). Weinig bereik; een eerste antwoord op een open vraag zet hem wel even bovenaan "active" en blijft vindbaar (GOK).
- Waarom gratis Click Joints en niet Pro: hij wil per plek een kogel en kom in een eigen figuur. Precies wat de gratis add-on doet (cursor zetten, Place joint). Geen verkooppraatje: de link gaat naar de gratis versie op extensions.blender.org, waar Pro al op de pagina staat.
- Regels (DERDEN, https://blender.stackexchange.com/help/promotion, curl 26 nov): eigen product noemen mag in een goed antwoord, "you must disclose your affiliation in your post", en "If you respond only to questions where the answer can be something you're selling, they'll assume you're just here to sell." Daarom: het antwoord lost het probleem volledig op zonder add-on, het product staat in één alinea met "Disclosure".
- **Volgorde met het Click Cuts-antwoord (#166):** dit wordt het eerste antwoord van Thijs op Stack Exchange, want het gaat over een gratis tool en kan nu al. Het Click Cuts-antwoord (betaald) komt bij de lancering, minstens een paar dagen later. Twee antwoorden die allebei een eigen product noemen is de grens; daarna geen derde zonder eerst gewone antwoorden (GOK, afgeleid uit de regel hierboven).
- Wanneer: ma 30 nov of later (vr 27 r/blender, za 28 r/NomadSculpting, zo 29 Blender Artists staan al voor Thijs). Geen sale-zin nodig: het gaat over de gratis versie.

## Tekst om te kopiëren (Engels, Markdown zoals Stack Exchange het leest)

```
The messy edges usually come from three things: the order of the modifiers, a cutter that isn't a clean closed shape, and scale. Here's a way that keeps the socket exact.

**1. Cut the smooth surface, not the low-poly cage**

"Horrible smoothed, OK flat" is the Subdivision Surface modifier smoothing the cut after the Boolean. Either apply the Subdivision Surface modifier first, or move the Boolean below it in the modifier stack, so the socket is cut into the final surface and stays sharp and round.

**2. Make the cutter a clean, closed sphere**

- Add a UV Sphere with enough segments for a round socket (for example 64 segments, 32 rings).
- Its radius is the ball radius plus your clearance (the gap between ball and socket, a few tenths of a millimetre, depending on your printer).
- Don't smooth or subdivide the cutter, and keep its surface clear of faces that lie exactly on the leg's surface: let it stick out a little where the opening is.
- If you want the socket to hold the ball, set the sphere's center a bit inside the body, so the opening ends up narrower than the ball. How much depends on how much your material flexes.

**3. Check both meshes before the Boolean**

- Apply scale on both objects (Ctrl+A > Scale), or the cut can land in the wrong size.
- Both must be closed: in Edit Mode, Select > Select All by Trait > Non Manifold should select nothing. Fix holes with F or Grid Fill.
- Recalculate normals (Shift+N) so they point outward.
- Use the Boolean modifier with Difference and the Exact solver. If the body overlaps itself, tick Self Intersection under Solver Options.

**4. Eyes and other separate parts**

For printing, join them into one solid shell: Boolean modifier on the body, Union, with the eye as the object (Exact solver), then apply. Check the result with the 3D Print Toolbox extension (Checks > Solid) before export.

Set the scene to millimetres (Scene Properties > Units: Unit Scale 0.001, Length Millimeters) so the clearance you type matches your slicer, and print a small test of one joint first: every printer and filament is different.

**If you do this a lot**

Disclosure: I'm Thijs from Dortus, and we make Click Joints, a free add-on on the Blender Extensions site for exactly this step. Put the 3D cursor where the joint goes and click Place joint: it cuts the mesh into two watertight parts with a ball and socket (or a pin), with the clearance you set in millimetres, and shows in the viewport how far the joint bends before the parts collide. A ring on the cut shows the fit: yellow when tight, red when the wall is too thin. "Make watertight" fixes open or messy meshes on a copy. Tested on Blender 4.2 LTS and 5.2 LTS: https://extensions.blender.org/add-ons/click-joints/
```

## Nagekeken
- Elke bewering over Click Joints staat letterlijk op de live pagina https://extensions.blender.org/add-ons/click-joints/ (GEZIEN, curl 26 nov ±19:00 NL): 3D cursor, Place joint, two watertight parts, ball and socket or a pin, clearance in millimetres, measures how far the joint bends before the parts collide and shows it in the viewport, ring green/yellow/red with "too thin", "Make watertight" on a copy, "Tested on Blender 4.2 LTS and 5.2 LTS" (dus "works in Blender 4.2 and newer" is wat ruimer dan "tested on"; keurder mag "tested on Blender 4.2 and 5.2" eisen). Gratis: "This free add-on stays free".
- Geen belofte dat het past of klikt, niets over zelf printen, geen "not print tested", geen AI. De testzin staat erbij. "a few tenths of a millimetre" bewust zonder getal als belofte (de pagina zegt "0.1 to 0.3 mm is typical"; mag er ook in).
- Blender-stappen: Subdivision Surface boven of onder Boolean in de stapel, UV Sphere segments en rings, Ctrl+A > Scale, Select All by Trait > Non Manifold, Shift+N, Boolean Difference en Union met Exact solver en Solver Options > Self Intersection, Unit Scale 0.001, 3D Print Toolbox als extensie: gewone Blender-functies (4.2 en nieuwer). Niet in een draaiende Blender nagelopen (GOK op de precieze menunamen; de keurder mag dat checken).
- Geen persoonsgegevens; de naam Thijs staat al openbaar op de extensiepagina ("Add-on by Thijs-Dortus") en in het gekeurde Click Cuts-antwoord.

## Ook gewogen deze run, en waarom niet
- **Blender Artists, Black Friday-draadjes:** verkopers zetten hun korting in hun eigen add-on-draadje (bijvoorbeeld "50% OFF! Shader Shaper", GEZIEN search.json). Ons Pro-draadje voor zo 29 nov heeft CYBER25 al in de tekst (`2026-11-26-blenderartists-pro.md`). Geen gezamenlijk dealdraadje voor 2026 gevonden.
- **r/blenderhelp, nov 2026 (Arctic Shift, titel "print"):** 6 posts, geen enkele over gewrichten. "Setting up a hollow rigged character to 3d print" (1 nov) gaat over één statisch geposeerd beeldje, niet over beweegbare delen: past niet bij Pro. Arctic Shift gaf weer "Timeout" bij zoeken op tekst; reddit.com zelf 403.
- **Stack Exchange, andere vragen (zoekwoorden ball joint, articulated, hinge, action figure):** alleen 209724 (al gebruikt, #166) en deze 109488 passen.
