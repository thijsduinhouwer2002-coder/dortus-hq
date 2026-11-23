# Vindbaarheid dortus.com: gidspagina's op zoekvragen (Verspreider, run 4, 23 nov 2026)

Doel: meer mensen die in Google zoeken hoe ze gewrichten voor een 3D-print maken in Blender, komen op dortus.com en klikken door naar de gratis Click Joints of naar Pro ($19). Kost 0 euro.

## 1. Eerst: gids 2 en 3 staan nog niet live (grootste winst per minuut)

- Gids 1 (ball joint) staat live: https://dortus.com/click-joints/gids/ball-joint-3d-print-blender/ geeft 200, en /click-joints/ linkt ernaar (GEZIEN, curl 23 nov 20:50 UTC).
- Gids 2 (hinge, Pro) en gids 3 (articulated figure uit de rig, Pro) geven 404 op dortus.com (GEZIEN, curl 23 nov 20:50 UTC):
  - https://dortus.com/click-joints/gids/hinge-joint-3d-print-blender/
  - https://dortus.com/click-joints/gids/articulated-figure-3d-print-blender/
- Beide zijn groen van Daan sinds 21 nov (`berichten/hoofdchat.md`, regels 598, 612 en 637). Ze staan op tak `gids-click-joints` (adfb519) in repo `dortus`. Bram kan niet naar die repo pushen, dus het ligt bij de hoofdchat.
- Dit staat al op de lijst van Thijs, punt 5: de push van de hoofdchat naar main van repo `dortus` wordt geweigerd door de automatische toestemmingscontrole, dus Thijs moet main op de commits zetten of zeggen dat de hoofdchat mag pushen. In dat punt staan (a) `gids-click-joints` (adfb519) en (b) `claude/fit-test-strip` (8624de3, met de direct-zip met Pro-knoppen, de gratis Fit test strip en de Pro 1.2.x-tekst). Brams tak `claude/utm-koopknoppen` (977af09, groen van Daan, zijn bericht van 23 nov 21:25) staat er nog niet in.
- Nagekeken (GEZIEN, lokaal in repo `dortus`, 23 nov, en door de keurder met merge-tree): een volgorde die schoon samengaat is: fast-forward naar `claude/fit-test-strip`, dan merge `gids-click-joints`, dan merge `claude/utm-koopknoppen`. De losse 1.2.x-patch van Bram (`platformen/blender/dortus-com-click-joints-1.2.x.patch`) hoeft dan niet meer: die tekst zit al in 8624de3, en op fit-test-strip past de patch niet meer.
- Waarom het telt: gids 2 en 3 gaan over Pro (de betaalde knop "Figure from rig"), en de fit-test-strip-tak zet de Pro-knoppen van de direct-zip live. Google kan een pagina pas vinden als hij live staat. Hoeveel bezoekers: onbekend, nieuwe pagina's krijgen vaak pas na dagen tot weken verkeer uit Google (GOK). Verwacht er dus geen omzet van in de sale (Superhive Cyber Sale vr 27 nov t/m wo 2 dec), wel een basis voor december.

**Voor de hoofdchat:** zet `claude/utm-koopknoppen` als (c) bij lijst punt 5, met de volgorde hierboven, en vraag Thijs bij de eerstvolgende keer dat hij de lijst doet om dat punt eerst te doen (±2 min). Daarna met curl kijken of beide gidsadressen 200 geven.

## 2. Welke zoekvragen er zijn (Google-suggesties)

Gemeten met de suggestiedienst van Google (`suggestqueries.google.com`, client firefox, Engels), 23 nov 2026 ±21:00 UTC (GEZIEN). Suggesties zeggen dat mensen het zoeken, niet hoe vaak; aantallen hebben we niet.

| Begin van de zoekvraag | Suggesties die over ons gaan | Gedekt door |
|---|---|---|
| blender ball joint | blender ball jointed doll; blender ball joint; blender ball and socket joint | gids 1 (behalve "doll") |
| blender joints for 3d printing | how to make joints in blender for 3d printing; how to 3d print joints | gids 1 en 2 |
| blender articulated | blender articulated model; blender articulated model tutorial; blender articulated figure; blender articulated hand | gids 3 |
| blender action figure | **blender action figure joints; blender action figure addon**; blender action figure tutorial; blender action figure template | niets |
| how to make articulated figure | how to make articulated figures in blender; **how to make action figure joints tighter**; how to make action figures with 3d printer | deels gids 3 |
| blender split model for 3d printing | blender split model into parts for 3d printing; blender cut model for 3d printing; how to split a model in blender | niets |
| blender tolerance 3d print | **blender 3d print tolerance** | deels gids 1 |
| posable figure 3d print | poseable figure 3d print; action figure 3d print files free | (dat zijn printbestanden, geen Blender-zoekers) |

Wat er nu bovenaan staat bij "blender action figure addon" (zoekmachine van deze run, GEZIEN 23 nov): alleen productpagina's op Superhive (Figure Blockout Generator, PlayRig, Puppet Studio, Voxel Figure Creator), geen enkele uitlegpagina en geen add-on die gewrichten voor een print maakt. Daar is plek.

## 3. Voorstel: wat erbij komt (voor Bram, keuring Daan)

Op volgorde van kans op een koper per minuut werk (GOK op de volgorde, onderbouwd met de koopwoorden in de zoekvraag).

### A. "action figure" in gids 3 (klein, vóór de merge of direct erna)
- Nu: titel "Articulated figure in Blender for 3D printing: every joint from your rig".
- Wordt: titel en h1 "Articulated action figure in Blender for 3D printing: every joint from your rig", en in de meta-beschrijving "poseable 3D print figure" naar "poseable 3D printed action figure".
- Waarom: "blender action figure joints" en "blender action figure addon" komen als suggestie (GEZIEN), "articulated figure" ook. Met één woord dekt dezelfde pagina beide. Geen nieuwe belofte, dus de inhoud blijft gelijk.
- Wie: Bram past het aan op de tak, Daan kijkt alleen naar de titel. Lukt dat niet vóór de merge: eerst mergen zoals hij is, titel later.

### B. Nieuwe gids 4: tolerance (speling) voor gewrichten
- Zoekvraag: "blender 3d print tolerance" (GEZIEN, suggestie). "how to make action figure joints tighter" komt ook, maar komt waarschijnlijk van mensen met een los gekocht poppetje (GOK), dus daar leunt de pagina niet op.
- Adres: `/click-joints/gids/joint-tolerance-3d-print-blender/`
- Titel: "Joint tolerance for 3D printing in Blender: what clearance to use"
- Inhoud (alleen wat de gratis versie doet, uit de README van click-joints): clearance in mm (0.1 tot 0.3 mm is typisch), de pasring op de snede (groen goed, geel krap, rood te dun), Auto size, en "print a test joint first". Eerlijk: "not print tested by us yet". Geen getal over hoe strak het in een print zit; geen "click", "clicks" of "holds a pose".
- Koopknop: gratis Click Joints bovenaan, Pro onderaan (zelfde opbouw als gids 1), plus een Pro-regel halverwege bij de Fit test strip.
- Linkt eerst naar de Fit test strip op dortus.com (staat op tak `claude/fit-test-strip`), later ook naar Printables (`2026-11-23-printables.md`) als die online is.
- Noemt "Works best on figures of about 200 mm or taller" (README).

### C. Nieuwe gids 5: model in delen voor 3D-printen, op de gewrichten
- Zoekvragen: "blender split model into parts for 3d printing", "blender cut model for 3d printing", "how to split a model in blender" (GEZIEN, suggesties; de breedste groep van deze meting).
- Adres: `/click-joints/gids/split-model-3d-print-blender/`
- Titel: "Split a model into parts for 3D printing in Blender, with joints at the cuts"
- Inhoud: eerst eerlijk de gewone Blender-weg (Bisect of een Boolean voor een rechte snede, zonder gewricht), dan de snede op een gewricht met Click Joints: twee waterdichte delen, kogel of pen, één STL of 3MF per deel in millimeters (README), met "not print tested by us yet" en "Works best on figures of about 200 mm or taller". Zo is de pagina ook nuttig voor wie geen add-on wil.
- Let op: de Productbouwer bouwt Click Cuts (delen met kleur per stuk, `producten/blender-splitser/`). Zodra die uit is, hoort deze zoekvraag misschien bij Click Cuts. Daarom pas na A en B, en eerst kort afstemmen met de Productbouwer welk product op deze pagina de hoofdknop krijgt.

### Niet nu
- "blender ball jointed doll" (bovenste suggestie bij "blender ball joint", GEZIEN): poppen met kogelgewrichten (BJD) hangen meestal aan elastiek. Onze kogels werken anders (GOK op wat BJD-makers verwachten). Zonder echte print beloven we niets aan die groep. Terug als er een printfoto is.
- Lijsten met "best Blender add-ons for 3D printing" (All3DP, Blender Base Camp; gevonden met zoeken, GEZIEN 23 nov): erin komen vraagt een mail aan de schrijver, dat is iemand benaderen. Mogelijk later, met ja van Thijs op de tekst.

## 4. Klein extra: tag "Sculpt" voor de gratis versie op extensions.blender.org
- Nu: tags "Mesh" en "Modeling" (GEZIEN, `click_joints/blender_manifest.toml` in repo click-joints, en API van extensions.blender.org).
- Wordt: "Mesh", "Modeling", "Sculpt".
- Waarom: op de tagpagina Sculpt staan 21 add-ons, op Modeling 151 en op Mesh 211 (GEZIEN, telling uit https://extensions.blender.org/api/v1/extensions/ op 23 nov). Wie op Sculpt filtert, ziet ons tussen veel minder andere. De gratis versie is gemaakt voor een sculpt in delen, dus de tag klopt. Hoeveel mensen die tagpagina gebruiken: onbekend (GOK: weinig, maar het kost één regel).
- Wie: Bram, mee in de volgende gratis versie (0.1.2, die er al aan komt met de nieuwe tagline). Geen aparte versie alleen hiervoor.

## Bronnen
- Google-suggesties: `https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=<vraag>` met curl, 23 nov ±21:00 UTC.
- Live-check: curl op de drie gidsadressen, 23 nov 20:50 UTC.
- Tags: https://extensions.blender.org/api/v1/extensions/ , 23 nov ±21:00 UTC.

## Keuring
Aparte keurder (Claude, skill keuren), 23 nov 2026 ±22:15 NL: **akkoord nee**, één moet: het mergeplan in deel 1 sloeg `claude/fit-test-strip` over, noemde de blokkade op de push niet, en de 1.2.x-patch past niet meer. Verwerkt: deel 1 herschreven naar lijst punt 5 met de schone volgorde (gecontroleerd tegen `organisatie/lijst-thijs.md` punt 5 en `git log origin/main..origin/claude/fit-test-strip`, GEZIEN). Kan-punten verwerkt: datum van de sale (27 nov t/m 2 dec), "not print tested by us yet" en de 200 mm-regel in C, titel C zonder "keep it poseable", gids 4 linkt naar de strip op dortus.com met een Pro-regel, gids 4 leunt op "blender 3d print tolerance". Nakeuring door dezelfde keurder (±22:30 NL): moet opgelost, **akkoord ja**, geen nieuwe moets; takken ongewijzigd na nieuwe fetch (main 2e99b6d, fit-test-strip 8624de3, gids adfb519, utm 977af09).
