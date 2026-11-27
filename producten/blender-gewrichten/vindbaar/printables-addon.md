# Printables: gratis Click Joints als add-on-model (Bram, 27 nov 2026, issue #257)

**Waarom:** TrailPrint3D (gratis Blender-add-on, Premium op Patreon) staat als model op Printables: 3.885 downloads, 1.201 likes, 14 beoordelingen 5,0, en het is het eerste resultaat op "blender addon" (GEZIEN, api.printables.com 27 nov ±12:20 NL). Wie figuren print, zoekt op Printables, niet op extensions.blender.org. Wij staan daar alleen met de Fit test strip (model 1929497, 0 downloads op 27 nov ±12:20 NL, GEZIEN). Een tweede model met het add-on zelf geeft een tweede ingang bij "ball joint" en "blender addon".

**Plaatsen doet de hoofdchat** met het Printables-account van Dortus, na Daans ja en pas als het hoofdbeeld GESLAAGD is (CLAUDE.md regel 9). Geen geld, geen nieuwe voorwaarden (account staat er sinds 25 nov).

## Besluit punt 4: welke zip, met of zonder Pro-knoppen

**Besluit: de direct-zip met de Pro-knoppen**, `producten/blender-gewrichten/uitgave/click_joints_direct-0.1.2.zip`, sha256 `06f54732f7c9b9da52a1059ef208ecc4db8ce8b543198f5e5cadb9653b10c51c` (GEZIEN, sha256sum 27 nov). Geen nieuwe build nodig.

Waarom dit mag:
- Regels 6.1 tot 6.3 van extensions.blender.org gaan over "the extension" en "the platform": wat daar geüpload staat. Opnieuw gelezen met curl op 27 nov ±12:25 NL, nog steeds "Last updated: 10 August 2026" (GEZIEN). Er staat geen regel in over versies die je elders verspreidt.
- De zip die op Extensions staat, verandert niet. De extensions-zip noemt Pro nergens; `click-joints-uitgave.yml` stopt als er `direct.py` of `betaald/` in zit. Die scheiding blijft.
- Precedent: deze direct-zip is sinds 21 nov de download op dortus.com (besluit hoofdchat 21 nov 22:45) en is gekeurd voor Gumroad gratis en Superhive Lite (Olaf #115, Daan ja #127). Printables valt net als die plekken niet onder de regels van Blender. TrailPrint3D doet hetzelfde: knoppen "Patreon" en "Thangs" in het paneel van de Printables-versie (`panels.py` r. 149 tot 153, Afkijker).
- Wat erin zit: drie Pro-knoppen op slot plus "Upgrade to Pro" met link naar `dortus.com/click-joints/?from=addon#pro`. Geen prijs, geen popup. De regel naar de reviews (na een Good fit en een export) wijst naar Blender Extensions; dat laat ik zo, daar tellen de reviews.
- Wat het zou veranderen: zegt een moderator van Extensions dat een build elders met dezelfde id niet mag, dan gaat op Printables de extensions-zip `click_joints-0.1.2.zip` (sha256 `f1c77eb8dccc55d7d1908e17629cb9eecec213ad01787c8ce6abf5d6a13ffd12`) erop. De pagina linkt dan nog steeds naar Pro.

## Bestanden

| Waar op Printables | Bestand in de repo | Waarom |
|---|---|---|
| Model files (STL) | `commercie/blender-click-joints/testprint/kogel-deel-A.stl` (44,5 mm hoog) en `kogel-deel-B.stl` (29 mm hoog), staaf 20 mm dik | Een kogelgewricht zoals Click Joints het maakt (automatische maat). Gemaakt met de echte add-oncode in Blender 5.3 (`testprint/maak.py`, 17 nov). Printables wil een printbaar bestand; dit is precies wat de download doet. |
| Other files | `producten/blender-gewrichten/uitgave/click_joints_direct-0.1.2.zip` | Het add-on zelf (zie besluit hierboven). Bij een nieuwe gratis versie: de nieuwe direct-zip erbij zetten, de oude laten staan (zoals TrailPrint3D). |

**De Fit test strip gaat er niet bij als STL**, anders dan het issue voorstelt. Reden: hij staat al als eigen model (1929497), en Printables verbiedt dubbele uploads (voorwaarden, `commercie/blender-click-joints/verspreiding.md` regel 81; DERDEN). Twee keer hetzelfde bestand kan het account kosten. In de tekst staat een link naar het strip-model; zo helpen de twee pagina's elkaar.

## Beelden

Printables-regel: "Preview images must accurately depict what users will download and print" (DERDEN, https://help.prusa3d.com/article/printables-ai-tag-rules-guidelines_1306155). Dus alleen echte beelden uit Blender van het gratis add-on en van het kogelpaar. Geen figuur met scharnieren (dat is Pro), geen foto van een print (wij hebben er geen).

1. **Hoofdbeeld:** in de blinde test, set `organisatie/blindtest/sets/click-joints-printables-addon.json` (twee kandidaten: de twee echte Blender-beelden van onze Extensions-pagina, tegen TrailPrint3D en de twee best gedownloade "ball joint"-modellen). Uitslag in `organisatie/blindtest/uitslag/`. Pas bij GESLAAGD en Daans ja mag het erop. Niet geslaagd: de Beeldmaker maakt een beeld voor Printables met hun opmerkingen.
2. Tweede beeld: het andere Extensions-beeld ("Drag the bend. Red means too far." of "Good fit, measured in mm.", paneel met maten).
3. Derde beeld: render van het kogelpaar uit de twee STL's (kan de Beeldmaker of ik maken met `commercie/verspreiden/beeld/render_stl.py`, zoals bij de strip).

## Categorie, tags, licentie

- **Categorie:** Hobby & Makers > Other Ideas. Daar staan de twee best gedownloade kogelgewrichten (Snap-fit ball joint 11.047, Universal Ball Joint 4.753; GEZIEN, API 27 nov). TrailPrint3D staat in Art & Design > Other Art & Designs, maar dat past niet bij een kogelgewricht.
- **Tags:** blender, addon, balljoint, ball joint, articulated, figure, poseable, customizable, generator, joint. (TrailPrint3D: blender, addon, generator, customizable; kogelmodellen gebruiken "balljoint" als één woord; GEZIEN, API.)
- **Licentie:** add-on GPL (zoals op Extensions); voor de pagina kiest de hoofdchat "Creative Commons Attribution", net als de strip en TrailPrint3D.
- **AI-vraag van Printables:** dezelfde keuze als bij de strip (hoofdchat 25 nov, `commercie/geplaatst.md` regel 61). In de tekst staat niets over AI.

## Tekst (Engels, plakken)

**Name:**
```
Click Joints: Free Blender Add-on for Ball Joints in Poseable Prints
```

**Summary (onder 120 tekens):**
```
Free Blender add-on: cut ball joints into your own figure, see how far each one bends, export STL or 3MF per part.
```

**Description:**
```
Click Joints is a free Blender add-on for people who print their own poseable figures. Set the 3D cursor where the joint goes, click Place joint, and it cuts your mesh into two watertight parts with a ball and socket or a pin, sized with the clearance your printer needs, in millimetres.

For a ball joint it measures how far the joint bends before the parts collide, in 8 directions, and shows that range on the model, for example "Bends ±20°". Bend past it and the spot where it hits turns red. A ring on the cut shows the fit: green is good, yellow is tight, red is too thin, and the panel says why.

What you get
- Ball and socket, or pin and hole
- Auto size: the largest ball with a good fit, or a clear message when none fits
- Clearance in mm (0.1 to 0.3 mm is typical)
- Exploded view to see the ball and socket apart
- "Make watertight" for open or messy meshes, on a copy
- Export as STL or 3MF, one file per part, in millimetres
- Blender 4.2 or newer

Files
- click_joints_direct-0.1.2.zip (other files): the add-on. Install it in Blender: drag the zip onto the Blender window, or Edit > Preferences > Get Extensions > Install from Disk. Do not unzip it. The tab "Click Joints" appears in the sidebar (N).
- kogel-deel-A.stl and kogel-deel-B.stl: a ball joint the add-on made on a 20 mm bar, auto size. Print both flat end down and push them together.

Not sure which clearance fits your printer? Print the Ball Joint Tolerance Test first: https://www.printables.com/model/1929497-ball-joint-tolerance-test-010-to-030-mm

Click Joints is free and stays free. The same add-on is on Blender Extensions: https://extensions.blender.org/add-ons/click-joints/

Need knees and elbows that stop?
Click Joints Pro builds a whole figure from your rig in one click and adds click hinges with an end stop. It includes everything in the free version. https://duinhouwer8.gumroad.com/l/click-joints-pro?utm_source=printables

Questions or a bug? Use "Report a problem" at the bottom of the Click Joints tab, or comment here.
```

Waarom zo:
- Zinnen uit de gekeurde Extensions-beschrijving (`platformen/blender/indienen.md`, "Description") en de installzin van #258 (Daan ja #262); niets nieuws beloofd.
- Geen zin over wel of niet geprint, geen prijs, geen saleregel: de pagina moet na 1 dec blijven kloppen. Wie doorklikt, ziet op Gumroad de saleregel (staat live tot 1 dec, salecontrole 09:00 GEZIEN).
- Pro in twee zinnen onderaan, alleen wat in 1.2.8 zit (rig, scharnier met eindstop). De gratis functies staan bovenaan, zoals TrailPrint3D het doet.
- "Blender 4.2 or newer" in plaats van een rijtje geteste versies: de gratis versie staat op Extensions als getest op 4.2 LTS en 5.2 LTS; dat hoeft hier niet herhaald.

## Meten na het plaatsen

Downloads, likes en reacties via de Printables-API (zelfde query als de Afkijker). Gumroad-verwijzers met bron printables (utm). Na 7 dagen: minder dan 20 downloads en 0 klikken naar Gumroad = niets meer aan doen (GOK op de drempel). Verwachting eerste 30 dagen: 30 tot 300 downloads (GOK; TrailPrint3D haalde 3.885, met reacties vanaf maart 2025, GEZIEN; een nieuw account met 0 volgers haalt meestal veel minder).
