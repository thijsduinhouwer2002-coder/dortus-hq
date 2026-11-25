# Broncode: 3D Print Toolbox (Blender-add-on)

Uitgeplozen door de Afkijker op 25 nov 2026 ±04:00 NL, voor issue #20. Code gelezen uit het zip-pakket van versie 1.5.0 (alleen gelezen, niets uitgevoerd), pagina's met curl.

## Waarom dit project
- De meest gebruikte add-on voor 3D-print in Blender, dus precies onze kopers: **700.759 downloads, 54 reviews, 51 keer 5 sterren, 1 keer 4, 2 keer 2** (GEZIEN, https://extensions.blender.org/add-ons/print3d-toolbox/ en /reviews/, 25 nov).
- Ter vergelijking in dezelfde winkel (GEZIEN, 25 nov): Easy-Print 7.946 downloads, EasySlice Print 7.275 (21 ratings), SnapSplit 1.973, onze gratis Click Joints 382.
- Licentie: GPL-3.0-or-later, net als onze add-on (manifest, `blender_manifest.toml`). Code overnemen mag dus, mét hun copyrightregel erbij; het idee nabouwen in eigen code is het schoonst.
- Makers: Campbell Barton (2013), sinds 2016 Mikhail Rachinskiy. Klein: ±1.700 regels Python plus 6 vertalingen.

## Wat ze slim doen (bestand en regels)
1. **Uitslag die je kunt aanklikken.** Elke controle (open randen, dunne wanden, overhang, scherpe randen) zet een regel in een lijstje in het zijpaneel: naam plus aantal. In Edit Mode is het aantal een knop: klik en precies die foute randen of vlakken worden geselecteerd. Code: `report.py` (heel bestand, 42 regels: een `_Item` met naam, waarde, indexen, selectiemodus), `ui.py` regels 70 tot 91 (`draw_report`), `operators/analyze.py` regels 418 tot 446 (`MESH_OT_report_select`, met de melding "Report is out of date, re-run check" als de mesh intussen veranderde). Een review zegt waarom dit werkt: "it helps you grok how to make things printable" (Johan-Althoff).
2. **Eén knop "Check All"** die alle controles na elkaar draait en één lijst geeft (`analyze.py` regels 387 tot 416).
3. **Dunne wanden vinden met stralen.** Per vlak 6 willekeurige punten, vanaf elk punt een straal naar binnen over de minimale dikte; raakt hij de andere kant, dan is de wand te dun (`lib.py` regels 146 tot 206). Instelbaar getal naast de knop.
4. **Losse stukken tellen** met een tijdelijke Geometry Nodes-groep (Mesh Island plus een Warning-node die het aantal teruggeeft), daarna alles weer opgeruimd (`analyze.py` regels 186 tot 250).
5. **Getal naast de knop.** Elke controle met een drempel staat op één rij met zijn instelling (`ui.py` regels 112 tot 128): geen apart instellingenscherm nodig.
6. **Ook vanuit een menu en als zwevend paneel** (`ui.py` regels 19 tot 41, `wm.call_panel`): wie het zijpaneel niet vindt, vindt het in het Object-menu.
7. **Exporteren in één klik met de juiste instellingen** (`operators/export.py`). Meerdere reviews gebruiken de add-on vooral hiervoor (adabru: "I'm only using the export button", BlueNeon: "quick 1 click exports").
8. **Zes vertalingen** (es, fr, ja, pt_BR, ru, zh) als gewone `.po`-bestanden, ingelezen in `localization/__init__.py` en aangemeld met `bpy.app.translations.register` (`__init__.py` regel 34).
9. **De maker antwoordt op elke vraag of klacht in de reviews**, kort en met waar het staat ("it's called Align XY located in Edit panel").

## Wat gebruikers vragen of klagen (reviews, GEZIEN 25 nov)
- "Please add feature: Volume Total for multi object" (LeBang).
- 3MF-export gevraagd (Francesca-4); de maker weigert: "does not implement exporters". Wij hebben 3MF wel (`drie_mf.py`).
- Tabblad niet zichtbaar na installeren (rachelcenter); oorzaak "Filter Add-ons" in de werkruimte. Komt bij ons ook voor: zet het in onze FAQ.
- "It can only clean out minor errors. With large errors it will produce very unpredictable results" (MarkusKruse, beroeps).
- "Pretends to be a magic wand ... too little functionality to really prepare the model" (fgfg-4, 2 sterren).
- Foutmelding bij aanzetten in 4.2.2 en sneltoets op de Export-knop kwijt na een update: kleine dingen na een update kosten hier sterren.

## Wat Dortus ervan leert
- **Click Joints Pro (Bram, `click_joints/gesloten.py`):** onze "Check mesh" geeft nu alleen een melding in de statusbalk met een aantal ("not watertight: N edges"), regels 52 tot 70. Beter: een lijstje in het paneel per gewrichtsdeel (open randen, losse stukken, wand rond kom of pin dunner dan X mm), waarin je op een regel klikt en de foute plek geselecteerd wordt. Dat maakt ons voordeel "je weet vóór de print of het past" groter, en past bij de toets op losse stukken die Bram op 25 nov bouwde. Issue bij Bram, na het weekdoel etalage.
- **Click Joints Pro, etalage:** de kopers van 3D-print willen vooral "het werkt in één klik". Zet in de winkeltekst dat wij STL én 3MF in millimeters per deel exporteren (de grootste add-on doet geen 3MF, een koper vroeg erom).
- **Click Joints Pro en Click Cuts, FAQ:** "tabblad niet zichtbaar? Zet Filter Add-ons uit in de werkruimte".
- **Alle Blender-producten:** antwoord op elke review binnen een dag, met waar de functie staat (hoofdchat, zodra er reviews zijn).
- **Later, niet nu:** vertalingen via `.po` (Japans en Chinees zitten bij de grootste); pas als er verkopen uit die landen komen.
