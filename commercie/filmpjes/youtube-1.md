# Langere YouTube-video 1: Click Joints (draaiboek)

Door Chris, 16 nov 2026, run 50. Opdracht: hoofdchat 16 nov 01:15 punt 1 en Joris 01:40 punt 3: deze week één gewone liggende video van 2 tot 4 minuten die een echte zoekvraag beantwoordt. Echte beelden, tekst in beeld, geen AI-stem, geen muziek in het bestand. Thijs plaatst.

## Eerst eerlijk: welke zoekvraag mogen wij beantwoorden?
- **Niet "print-in-place".** Click Joints snijdt een figuur in twee delen met een kogel en kom of een pen en gat; je print de delen en klikt ze in elkaar. Bram besloot: "delen worden los geprint en klikken in elkaar ..., geen print-in-place" (`producten/blender-gewrichten/ontwerp.md`, regel 76). Een titel als "How to make print-in-place joints in Blender" klopt dus niet, en de reeksnaam "Print-in-place in Blender, day N" (tip Joris 03:45) ook niet. Voorstel voor de reeks: **"Printable joints in Blender, day N"**.
- **Niet "hinge" in de gratis video.** Het scharnier met eindstop is Pro (nog niet te koop, Superhive keurt nog). Een video over scharnieren wordt pas zinvol als Pro live is.
- **Wel: kogelgewrichten en beweegbare figuren**, want dat doet de gratis versie: snijden, passing zien (groen, geel, rood), buigbereik meten, uit elkaar zien, STL of 3MF exporteren.

## Wat mensen intypen (GEZIEN 16 nov ±03:50 UTC, YouTube-suggesties via suggestqueries.google.com, ds=yt)
- "how to make articulated 3d print" geeft o.a. **"how to make articulated 3d prints in blender"**.
- "3d print ball joint" geeft "3d print ball jointed doll", "3d printed ball and socket joint".
- "poseable figure blender" geeft "action figure blender", "make action figure in blender".
- "print in place blender" geeft "print in place hinge blender" (niet voor ons, zie boven).
- "blender ball joint" en "blender action figure joints" bestaan als suggestie, zonder aanvulling (weinig volume, GOK).

## Wat er nu bovenaan staat (GEZIEN 16 nov ±03:55 UTC, YouTube-zoekpagina met curl)
| Zoekvraag | Bovenaan | Lengte | Views | Leeftijd |
|---|---|---|---|---|
| blender ball joint 3d printing | Ball Joints in Blender (EASY), Blender 3.0+ (Print That Thing) | 4:05 | 28.711 | 4 jaar |
| idem | 3D printed Ball and Socket (Coder-Tronics) | 1:43 | 121.900 | 9 jaar |
| idem | Print-in-Place Ball Joint in Blender (AISLabs AI) | 5:12 | 38 | 2 weken |
| how to make articulated 3d prints in blender | Articulated Dragon 3d print, Blender tutorial (P1lotz) | 35:29 | 142.791 | 4 jaar |
| idem | How To Design Articulating 3D Prints! Blender Tutorial (ZeroDotCMD) | 13:43 | 48.557 | 1 jaar |
| idem | How to Make Articulated Animals in Blender (Benix) | 4:20 | 8.946 | 4 jaar |
| idem | Flexi Articulator Tool ... for Blender (Granite Studio) | 0:15 | 559 | 8 maanden |
| blender articulated figure | Turn ANY 3D Model Into an ACTION FIGURE, Blender Auto Joints Tutorial (Nunn Breakable) | 47:11 | 584 | 4 weken |
| idem | How to Make a Ball Joint for Action Figures (Skillful Toys) | 20:26 | 4.766 | 1 maand |

**Wat dat zegt:** de korte Blender-uitleg over kogelgewrichten die bovenaan staat, is 4 jaar oud en voor Blender 3.0; de recente Blender-video's zijn 13 tot 47 minuten. Een korte, recente video (Blender 4.2 en 5.x, onder 4 minuten) die laat zien hoe je de passing en het buigbereik ziet vóór je print, is er niet (GEZIEN in de eerste 10 resultaten van vier zoekvragen). Let op: er zijn al twee andere Blender-tools met "auto joints" en "flexi articulator" in hun video (zie tabel); wij onderscheiden ons met de passingkleur en het gemeten buigbereik, dat zegt geen van die titels.

## Keuze
- **Titel:** `Ball Joints for 3D Printed Figures in Blender: check the fit and bend before you print (free add-on)` (98 tekens; YouTube toont ±60 in de lijst, dus het begin draagt de zoekvraag).
- **Reserve-titel:** `How to Make Articulated 3D Prints in Blender (ball joints, free add-on)`.
- **Lengte:** 2:30 tot 3:30. Eén figuur, één gewricht helemaal, daarna kort een tweede.
- **Waarom deze:** de zoekvraag bestaat (suggestie), het bovenste korte antwoord is oud, en het is precies wat de gratis versie doet, dus de video kan niets beloven wat niet klopt.

## Draaiboek (liggend 1920 x 1080, schermopname van de echte Blender, tekst in beeld, geen stem)
| Tijd | Beeld | Tekst in beeld |
|---|---|---|
| 0:00 tot 0:08 | Eindresultaat eerst: het figuur met het gewricht dat buigt, ring groen, dan uit elkaar; uit de nieuwe opname van Bram met de gratis zip (niet uit film v3: dat is de Pro-film met het scharnier) | "Ball joints for a 3D printed figure. In Blender, in about 3 minutes." |
| 0:08 tot 0:20 | Lege Blender, figuur in beeld, add-on aan in Preferences, paneel Click Joints in de zijbalk (N) | "Free add-on: Click Joints, from extensions.blender.org. Blender 4.2 or newer." |
| 0:20 tot 0:40 | 3D-cursor op de elleboog zetten (Shift + rechtsklik), dan Place joint | "Put the 3D cursor where the joint goes. Click Place joint." |
| 0:40 tot 1:05 | Mesh wordt twee delen, kogel en kom, ring op de snede wordt groen; paneel in close-up | "Green ring: good fit. Yellow: tight. Red: too thin, nothing is cut." |
| 1:05 tot 1:30 | Ongedaan maken, Auto aan, opnieuw Place joint (Auto en de maat werken pas bij Place joint, een geplaatst gewricht verandert niet mee) | "Clearance in mm. 0.1 to 0.3 mm is typical. Auto picks the largest ball with a good fit." |
| 1:30 tot 1:55 | Deel kantelen tot de grens, paneel "Bends ±N°" (wat de opname echt toont), voorbij de grens kleurt de botsing rood | "It measures how far the joint bends before the parts collide. Past the limit, the spot turns red." |
| 1:55 tot 2:15 | Een te dunne plek proberen, de weigering in beeld | "Too thin here? It says so, instead of giving you a broken part." |
| 2:15 tot 2:35 | Exploded view aan en uit | "Exploded view: see the ball and socket apart. The export stays in place." |
| 2:35 tot 2:55 | Export STL of 3MF, twee bestanden in de map, kort in een slicer of alleen de bestandsnamen | "Export as STL or 3MF, one file per part, in millimetres." |
| 2:55 tot 3:10 | Tweede gewricht (knie) in versneld tempo, beide groen | "Same steps for every joint." |
| 3:10 tot 3:20 | Eindbeeld met de link | "Free on extensions.blender.org. More: dortus.com/click-joints. Printed one? Show me: #clickjoints" |

Regels voor het beeld: elke zin staat minstens 3 seconden in beeld; muis rustig, geen snelle sneden (tip 2 van Joris: één duidelijke handeling houdt mensen het langst vast). Waarom de AI-zin zo: `winkeltekst.md` regel 174 zegt dat "with help from AI" de rol van AI kleiner maakt dan hij is. Wat in beeld komt, moet Bram in de echte Blender zo hebben gedaan; geen versnelde of geknipte tussenstap die doet alsof iets sneller gaat dan het gaat (versneld mag, met "2x" in de hoek).

## Wat er nodig is aan beeld
- **Al aanwezig (GEZIEN in de repo):** renders van film v2 en v3 (`ontwerp/click-joints/film/`, workflow `click-joints-pro-film.yml`); winkelschermen 1920 x 1080 van het hele Blender-venster op tak `schermen` (map `blender-gewrichten/`); de vijf staande opnames van Bram (1080 x 1920, niet bruikbaar voor liggend).
- **Nieuw nodig, door Bram (advies 40):** één doorlopende liggende schermopname 1920 x 1080, 30 fps, in Blender 5.2 met de gratis Click Joints 0.1.0 van extensions.blender.org, van de stappen in de tabel (cursor zetten tot export, plus de weigering). Zonder tekst; de tekst zet ik er met `maak.py` overheen, zoals bij de Shorts. Het mag als losse stukken per regel van de tabel.
- Zonder die opname is een video van stilstaande schermen mogelijk, maar dan geen echte uitleg; dat maak ik niet, want een uitlegvideo die je niet kunt nadoen, kost meer dan hij oplevert (GOK).

## Beschrijving bij de video (concept, Engels)
> How to add ball joints to a 3D printed figure in Blender, and check the fit and the bend range before you print. Made with Click Joints, a free add-on on extensions.blender.org (Blender 4.2 or newer, tested in 4.2 LTS and 5.2 LTS).
>
> 0:00 Result
> 0:20 Place a joint
> 0:40 Fit: green, yellow, red
> 1:05 Clearance and Auto
> 1:30 Bend range
> 2:15 Exploded view
> 2:35 Export STL or 3MF
>
> I direct the work; Claude (an AI) writes and tests the code. Printed a figure with it? Tag #clickjoints, I'd love to see it.
> Made by Thijs at Dortus. dortus.com/click-joints

Tags: blender, 3d printing, ball joint, articulated, action figure, blender add-on.
Omslag: het figuur met groene ring en de hoek die het paneel bij de opname echt toont (30, 25 of 20) groot in beeld, tekst "FIT + BEND before you print". Geen gezicht, geen pijlen naar dingen die er niet zijn.

## Meten
Na plaatsen: views op dag 1, 7 en 30 naast de downloads van Click Joints op extensions.blender.org (Bram meet ze). Ter vergelijking: Print That Thing haalde 28.711 views in 4 jaar met dezelfde vraag (GEZIEN), dus ±600 per maand is een redelijke verwachting na een paar maanden (GOK).

## Controle
Controleur (16 nov ±04:10 UTC): akkoord mits. Moet: (1) openingsbeeld niet uit film v3 (Pro, scharnier), (2) "4.2 and 5.x" wordt "4.2 or newer" zoals de winkeltekst. Beide verwerkt. Kan-punten verwerkt: Auto pas bij Place joint, rood snijdt niet, AI-zin uit winkeltekst regel 174, betere bron (regel 76), hoek op de omslag volgens de opname. Zes YouTube-cijfers opnieuw met curl nagekeken: gelijk.
Opgemerkt door de controleur: filmpje 2 in `week-1.md` heeft de hashtag #printinplace; die past niet bij Click Joints en is in run 50 vervangen door #articulated.
