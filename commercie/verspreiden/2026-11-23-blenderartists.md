# BlenderArtists: regel voor zelfpromotie en een hulpdraadje (Verspreider, 23 nov 2026)

## De regel (DERDEN, https://blenderartists.org/t/1416473, "New policy on 'self promotion'", 12 nov 2022, staat nog vastgepind)
- "you can make up to one self-promotion post a week", gemiddeld over 30 dagen.
- Telt als zelfpromotie: een topic in Released Add-ons over je eigen add-on, **en** "a link to your YouTube channel, website, or blog in a reply to another topic", **en** een Gumroad- of Superhive-link. Ook reacties in je eigen promotietopic tellen ("these bump your topic back to the top").
- Wat erover gaat, wordt verwijderd.

**Gevolg voor ons plan:** de Pro-post in Released Add-ons and Extensions (lijst-thijs, tekst 7 in `commercie/blender-click-joints/plekken-boost-2026-11-20.md`) is onze ene post van die week. Antwoorden op vragen in dat eigen topic tellen ook. Dus in de week van de sale geen tweede link naar ons elders op het forum. Het hulpdraadje hieronder komt pas de week erna (vanaf ±4 dec), en alleen als het account dan nog niets anders van ons plaatste.

GOK: een nieuw account (Discourse, vertrouwensniveau 0) mag in het begin weinig links en beelden per bericht plaatsen. Zet in de Pro-post daarom één link en het filmpje als bijlage, of lees eerst een paar draadjes zodat het account een niveau stijgt.

## Hulpdraadje: "Help Creating a Custom Articulated 3D-Printable Figure"
https://blenderartists.org/t/1656400 (categorie Modeling, geopend 31 okt 2026, 4 berichten, 109 keer bekeken, open; GEZIEN met curl op de JSON van het topic, 23 nov). Een beginner wil een figuur van 114 mm met kogelgewrichten voor hoofd, armen en benen, printen op een Bambu P1S. Het laatste antwoord (1 nov) zegt alleen "begin gewoon met modelleren".

**Waarom wel:** precies onze koper, met een concrete vraag die de gratis versie beantwoordt. Het draadje blijft in de zoekresultaten van het forum staan op "articulated figure print" en "ball joint 3d print" (daar staat het nu 1e en 2e, GEZIEN via search.json).
**Waarom voorzichtig:** het draadje is drie weken stil. Een antwoord nu is geen grafschennis (het staat open en er is geen regel tegen), maar we openen met hulp, niet met de link.

**Tekst (Engels, onder het account dat de hoofdchat of Thijs gebruikt; zegt eerlijk dat wij het maken):**
```
For a 114 mm figure we'd model it as one closed mesh first (head, torso, arms, legs, no joints yet), then cut the joints in afterwards. Getting the proportions right is the hard part; the joints are easier to add once the shape is there.

A few things that help at that size:
- Keep the limbs roughly 10 mm thick or more where a ball joint goes, or the wall around the socket gets too thin to print.
- Leave about 0.2 mm gap between ball and socket to start with, and print one small test joint before the whole figure. Every printer and filament is a bit different.
- Split the figure so each part prints without heavy supports inside the socket.

Disclosure: we make a free Blender extension for exactly this step, Click Joints. You put the 3D cursor where the joint goes, it cuts the mesh into two parts with a ball and socket at the clearance you set, and shows how far the joint bends before the parts collide. It's on extensions.blender.org (in Blender: Edit > Preferences > Get Extensions, search "Click Joints"). It won't model the figure for you, but it saves the boolean work once the body is done.

Happy to take a look once you have a first blockout.
```
Nagekeken tegen de gratis versie (beschrijving op extensions.blender.org, GEZIEN 23 nov): cursor plaatsen, Place joint, twee waterdichte delen met kogel en kom, speling in mm (0,1 tot 0,3), meet de buiging. "10 to 12 mm thick" is een GOK op basis van onze eigen melding "wall 0.89 mm (aim for 1.5 mm or more)" en een kogel van ±6 mm; laat de keurder dit wegen of schrappen. Geen Pro, geen prijs, geen klik beloofd.

**Wie:** het account dat de Pro-post doet (Thijs maakt het aan, lijst-thijs). Plaatsen: als het account op Dortus staat de hoofdchat na keuring, anders Thijs na zijn ja op de tekst. **Wanneer:** niet vóór de week na de Pro-post (±4 dec).
**Meten:** downloads per dag (scorebord) en verwijzers naar dortus.com in Amami; de link in dit antwoord gaat naar de winkel van Blender, dus vooral via de downloads.

Keuring: zie onderaan, door een aparte keurder.

## Keuring (aparte keurder, 23 nov 2026)
Wat ik keurde: dit bestand. Zelf nagekeken met curl op de JSON van t/1416473 en t/1656400, 23 nov.
Akkoord: ja

Deel A
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | Regel klopt: "up to one self-promotion post a week", "on average", over 30 dagen; telt: link in een antwoord, Gumroad-link, eigen add-on-topic, en antwoorden in je eigen promotietopic; te veel wordt verwijderd. Topic staat vastgepind (ook globaal). De categorie heet in de regel "Resources > Released Scripts and Themes", niet "Released Add-ons"; zelfde bedoeling. | feit | hoog |
| 2 | Topic 1656400 klopt: geopend 31 okt, 4 berichten, 109 keer bekeken, open, 114 mm, Bambu P1S, kogelgewrichten hoofd, armen, benen; laatste antwoord 1 nov "just do it". | feit | hoog |
| 3 | De tekst beantwoordt de echte vraag van de vrager ("body proportions or joints first?") eerst, zonder link. Behulpzaam, niet spammy. | feit | hoog |
| 4 | Disclosure is duidelijk ("we make"), geen URL, geen Pro, geen prijs, geen klik. Wat de gratis versie doet klopt met de winkelpagina (cursor, twee delen, kogel en kom, speling, buiging). | feit | hoog |
| 5 | "10 to 12 mm thick": past bij onze eigen rekensom (kogel ±6 mm + 2 x 1,5 mm wand + speling ≈ 9 tot 10 mm), en de vrager wil juist dikke ledematen. Eerlijk als vuistregel; staat terecht als GOK. 0,2 mm speling past bij 0,1 tot 0,3 mm op de winkelpagina. | vermoeden | midden |
| 6 | Wachten tot na de Pro-post (±4 dec) is de juiste lezing van de regel. | feit | hoog |

Deel B: geen persoonsgegevens (controle OK), cijfers met GEZIEN/DERDEN/GOK, Nederlands zonder gedachtestreepjes, niets geplaatst, plaatsen onder naam van Thijs alleen na zijn ja (staat erin).

Deel C: de vrager krijgt drie bruikbare tips en een uitnodiging om zijn blockout te tonen. Dat voelt als hulp, niet als reclame.

**Moet:** geen.

**Kan:**
1. "I'd model" en daarna "we make" wisselen ik en wij; kies er één (bijv. "we make" laten staan en "I'd" ook houden is gangbaar, maar "Disclosure: I'm part of the small team that makes..." leest soepeler).
2. "at least 10 to 12 mm" is dubbel; "roughly 10 mm or more" zegt hetzelfde en klinkt minder stellig.
3. Categorienaam in de samenvatting gelijkzetten met de regel (Released Scripts and Themes).

**Kan verwerkt (Verspreider, 23 nov):** "we" in de hele tekst, "roughly 10 mm thick or more".
