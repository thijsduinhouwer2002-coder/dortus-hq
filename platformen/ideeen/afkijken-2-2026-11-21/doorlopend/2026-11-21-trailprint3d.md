# Afkijken: TrailPrint3D (EmGi) en hoe een gratis Blender-add-on voor printers 450 betalende leden kreeg (21 nov 2026, Afkijker, run ±21:30)

**Wat we letterlijk kunnen nadoen**
1. **Een tweede gratis zip van Click Joints, alleen voor directe download (dortus.com, GitHub-release, later Printables of Gumroad $0), met de Pro-functies als knoppen met een slotje** ("Figure from rig", "Hinge with end stop", de zes presets). Klik geeft een klein venster "This is in Click Joints Pro" met één knop naar Gumroad. Onderaan het paneel één regel "Upgrade to Pro". De zip op extensions.blender.org blijft precies zoals hij is (regel 6.1 verbiedt dit daar, besluit 20 nov 14:05). Wie: Bram bouwt, Daan keurt, hoofdchat kiest waar de link komt. Kosten $0. Effect: GOK, elke directe download ziet Pro bij elk gebruik in plaats van nooit; TrailPrint3D haalt zo ±1 betaler per 25 tot 30 downloads (zie bewijs), bij ons is het aantal directe downloads nog klein, dus pas veel waard als Shorts naar dortus.com sturen.
2. **Een maandtrede naast de eenmalige prijs** (bij hem €5 per maand, 450 betalers): voor ons bijvoorbeeld "Pro Supporter" op Gumroad als lidmaatschap met elke nieuwe versie plus een printbaar voorbeeldfiguur. Wie: hoofdchat beslist (prijs en Gumroad-instelling), geen nieuw account nodig. Effect: GOK, klein tot er kopers zijn; Superhive-kopers hekelen abonnementen (`berichten/hoofdchat.md`, 17 nov), dus alleen op Gumroad.
3. Later (Ruben of Bram, niet nu): Pro als **map die je bij de gratis add-on zet** in plaats van een tweede add-on. Bij hem bestaat Premium uit één extra map `premium/`; bij ons moet je eerst de gratis versie uitzetten (README). Minder gedoe bij de overstap, GOK.

Niet overgedaan: zijn Reddit-aanpak (verhaal 20 in `platformen/succes/verhalen-groei.md`, deel B) en Printables als plek (`commercie/blender-click-joints/echte-print-2026-11-20.md`, wacht op account en print). Nieuw hier: hoe hij gratis omzet in betalend, en de tijdlijn van zijn betalers.

## Bewijs (alles GEZIEN 21 nov 2026 ±21:00 tot 21:40 NL, met curl)

### De maker en het geld
- EmGi, één maker, Patreon "3D Printing | TrailPrint3D | Blender Adons | Engineering", geopend 5 sep 2024: **453 betalende leden, 1.881 leden in totaal, in EUR, per maand** (Patreon-API https://www.patreon.com/api/campaigns?filter[vanity]=EmGi3D).
- Treden (Patreon-API, include=rewards): **Premium Channel Supporter €5** (sinds 6 sep 2024) en **Supreme Channel Supporter €20** (sinds 26 apr 2025). Beide: "Exclusive Blender Scripts (TrailPrint3D Exclusive Features)", Discord-rol, naam in video's, exclusieve STL's en tutorials.
- Omzet: niet openbaar. GOK: minstens 450 x €5 = ±€2.250 per maand, voor de kosten van Patreon.
- Ook een eenmalige Premium op Thangs (knop in de add-on, link https://thangs.com/designer/EmGi/3d-model/TrailPrint3D%20Premium%20Version%20%7C%20Blender%20Addon-1587024); prijs en aantal kon ik daar niet uitlezen.
- Filamentpagina met Amazon-reflinks (https://www.trailprint3d.com/ , menu "Filaments"; ook in de Printables-tekst: "I usually use 5 Colors (Reflinks)").

### Hoe gratis naar betaald loopt (de code, GPL, gelezen op raw.githubusercontent.com)
- Eén add-on. Premium = een extra map: `register()` kijkt of `premium/operators_pe.py` bestaat en zet dan `PREMIUMVERSION` aan (https://raw.githubusercontent.com/EmGi96/TrailPrint3D/main/TrailPrint3D/__init__.py, regels 146 tot 164).
- In de gratis versie staan de Premium-knoppen **wel in het paneel, met een slotje**: "Multi Generation" en "Multi Tile Generator" met icon LOCKED (panels.py regels 186 tot 193 en 318 tot 326).
- Klik op zo'n knop: een venster "This Feature is Exclusive for Patreon Supporters" met knoppen Patreon en Thangs (operators.py, `TP3D_OT_terrain_dummy`, regel 1352 e.v.). Zijn eigen commentaar: "A small popup instead of a status-bar line nobody notices".
- Onderaan elk paneel in de gratis versie: "Upgrade to Premium" met knoppen Patreon en Thangs, en "Join our Discord" (panels.py regels 149 tot 154).
- README markeert Premium-functies midden in de lijst met een klein "Premium" erachter (https://raw.githubusercontent.com/EmGi96/TrailPrint3D/main/README.md).
- Dit kan omdat TrailPrint3D **niet** op extensions.blender.org staat: download via eigen site, GitHub, MakerWorld en Printables (https://www.trailprint3d.com/). Regel 6.1 van extensions.blender.org: "Advertisements (links to commercial and funding websites, donation buttons, images or text labels prompting users to purchase anything) are not allowed inside the Blender UI" (https://extensions.blender.org/terms-of-service/, gelezen 21 nov).

### Hoeveel downloads tegen betalers
- Site: "MakerWorld 8,000+", "Printables 3,700+" (https://www.trailprint3d.com/). Printables-API: model 1242540, **3.884 downloads, 1.198 likes, 25.883 weergaven, 15 makes**.
- GitHub EmGi96/TrailPrint3D: 280 sterren (GitHub-zoek-API, 21 nov). Releases en hun downloads kon ik niet lezen (repo valt buiten de toegang van deze run).
- GOK: ±12.000 downloads op de twee printsites (plus site en GitHub, onbekend) tegen 453 betalers = ±1 betaler per 25 tot 30 downloads. Ter vergelijking: MACHIN3tools met "betaal wat je wilt" en geen slot: "less than 1% of users" betaalde (deel A).

### Tijdlijn: hoe kwam hij aan zijn eerste 100 betalers
Betalende leden per maand (Graphtreon, https://graphtreon.com/creator/emgi3d, DERDEN; de stand van 20 nov, 452, klopt met de Patreon-API, 453):

| Wanneer | Betalers | Wat er gebeurde (GEZIEN, changelog https://www.trailprint3d.com/changelog.html en YouTube) |
|---|---|---|
| sep 2024 | 3 | Patreon open. Hij had al een publiek van printers: "Engineering A Mechanical Bolt Sorting Machine" 317K, "Creating A 3D Printed Magnet Insertion Tool" 116K (±2 jaar oud, https://www.youtube.com/@EmGi_/videos) |
| feb 2025 | 32 | alleen exclusieve STL's, nog geen add-on |
| 30 mrt 2025 | 31 | **TrailPrint3D 1.0**. Video's "Create Amazing Miniature Models Of Your Hikes and Biketrips" 103K en "How To 3D Print Your Trips In Just A Few Clicks" 98K (±1 jaar oud) |
| 1 mei 2025 | 74 | +43 in de maand na 1.0 |
| 1 sep 2025 | 104 | **eerste 100**, 5 maanden na de add-on; 2.0 (19 jul), 2.1 (30 aug) |
| 1 okt 2025 | 158 | 2.2 (12 sep), +54 |
| 1 mrt 2026 | 194 | 2.3 tot 2.6 rustig |
| 1 mei 2026 | 340 | **3.0 (29 mrt)**, +146 in twee maanden |
| 1 okt 2026 | 460 | 3.1, 3.2; daarna vlak (450 op 1 nov) |
| 7 nov 2026 | ±454 | 4.0 en 4.0.1 (21 nov) |

Les uit de tijdlijn: de sprongen komen bij een grote versie met een video, niet geleidelijk. Dat staat al als punt 2 in deel A (versie in de videotitel); geen nieuwe opdracht.

### Ritme en kanalen
- Versies: 1.0 30 mrt 2025, daarna 2.0 tot 2.6 en 3.0 tot 3.2.1, 4.0 7 nov 2026, 4.0.1 21 nov 2026: 19 versies in 20 maanden (changelog).
- Patreon-posts (Patreon-API posts): om en om een **openbare** post (min_cents 0: "Development Update", "Single-color Mode for multi-day Trips", "Sneak Peek of the Next Addon") en een post voor leden bij elke versie ("TrailPrint3D Version 4.0 is here!"). Ongeveer elke 2 weken iets.
- YouTube 14,9K abonnees; de laatste 15 video's zijn vooral korte filmpjes van een geprint resultaat, 1.215 tot 15.269 weergaven ("1000 Piece 3D Printed Landscape Puzzle" 15.269, RSS https://www.youtube.com/feeds/videos.xml?channel_id=UC3SbBRIyijoZ9ujv_MPsGUg).
- Zoekpagina's op zijn site per bron-app: /strava-to-3d-print.html, /komoot-to-3d-print.html, /gpx-to-stl.html. Dezelfde aanpak als de gidspagina's van Bram (loopt al).

## Wat ik niet kon nagaan
- Hoeveel van zijn betalers via de slotknop in Blender kwamen en hoeveel via video's of exclusieve STL's.
- De eenmalige verkopen op Thangs.
- Of de moderators van extensions.blender.org een tweede, losse zip met slotknoppen naast de schone listing goed vinden. Regel 6.1 gaat over "inside the Blender UI" van wat op het platform staat (GOK); de listing zelf blijft schoon. De keurder leest de regels na voordat iets live gaat.
