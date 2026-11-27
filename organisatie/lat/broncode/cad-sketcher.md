# CAD Sketcher (Blender-add-on, gratis met "betaal wat je wilt" op Gumroad)

**Uitgeplozen:** vr 27 nov 2026 ±06:30 NL, Afkijker, issue #20. Code gelezen met `git clone --depth 1 https://github.com/hlorus/CAD_Sketcher` (versie 0.32.2 in `blender_manifest.toml`), niets uitgevoerd.

## Waarom dit project
Precies ons soort koper: mensen die in Blender exact willen modelleren, vaak voor 3D-print. En precies ons model: gratis add-on, verkocht en verspreid via Gumroad naast extensions.blender.org.

- **Licentie:** GPL-3.0-or-later (GEZIEN, `LICENSE` en `blender_manifest.toml` regel 12). Onze add-ons zijn ook GPL-3.0-or-later, dus code overnemen mag met naamsvermelding; het idee is genoeg.
- **Sterren:** 3,5k (GEZIEN, img.shields.io 27 nov). Downloads via GitHub-releases: 5,3k (GEZIEN, img.shields.io).
- **extensions.blender.org:** 10.778 downloads, **1 review** (3 sterren, "trekt Blender nog vaak onderuit") (GEZIEN, https://extensions.blender.org/add-ons/cad-sketcher/ en /reviews/, 27 nov).
- **Gumroad:** https://keepmaking.gumroad.com/l/CADsketcher, betaal wat je wilt met **$5 voorgesteld** en "put a 0 in the input to get it for free"; **1.351 beoordelingen, gemiddeld 4,8** (91% vijf sterren, 2% één ster) (GEZIEN, productdata van de pagina, curl 27 nov). 133 beoordelingen met tekst, van 12 jan 2024 tot 12 nov 2026 (GEZIEN, `gumroad.com/product_reviews?product_id=...`, 14 pagina's).
- **README:** "Preferred Download Method: Gumroad (This way we can update you about big updates and ask your opinion on big changes)" (GEZIEN, `README.md` regel 19).

Kern in cijfers: ruim tien keer zoveel downloads op Extensions, maar 1 tegen 1.351 beoordelingen. Wie via Gumroad haalt, laat een mailadres en een beoordeling achter; wie via Extensions haalt, laat niets achter. Dat bevestigt de les van Blosm (`blosm.md`) met harde cijfers.

## Wat ze slim doen (bestand en regels)
1. **"What's New" één keer na elke update, zonder boekhouding.** `base/whats_new.py`:
   - versie uit het manifest, tekst uit de meegeleverde `CHANGELOG.md` via `changelog.extract_section` (`changelog.py` r. 21 tot 41), dezelfde functie die de GitHub-release vult, dus één bron;
   - laatst getoonde versie in een bestandje in `bpy.utils.extension_path_user(...)` (r. 88 tot 107), dat updates overleeft; niets in de voorkeuren;
   - eerste installatie: stil opschrijven, geen popup (r. 165 tot 167); alleen tonen als er voor die versie echt notities zijn (r. 175 tot 176);
   - een popup zonder OK/Annuleren die weggaat als je ernaast klikt (r. 125 tot 127), met knop "Full changelog" en een vinkje "Show on update" (r. 143 tot 148); vinkje uit laat het merkje toch doorschuiven, zodat er nooit een oude popup komt (r. 154 tot 179);
   - getoond via `bpy.app.timers.register(_maybe_show, first_interval=1.0)` (r. 197 tot 200), nooit in achtergrondmodus.
   Wij gebruiken `extension_path_user` al voor het merkje van de beoordeelregel (`producten/blender-gewrichten/click_joints/meld.py` r. 71 tot 76), dus het stuk is bij ons klein.
2. **De Gumroad-pagina begint bij de koper die vastloopt.** "Three things to know before you upgrade" (versienummer lijkt lager, Blender 5.0 nodig, oude bestanden zetten zichzelf om) en installeren in drie stappen: "Download the ZIP from this page. Do not unpack it. Drag the ZIP straight from your file browser into the Blender window. Confirm the install dialog." Daarna een kop "If drag and drop doesn't work" met de Mac-valkuil: "On Mac the ZIP sometimes unpacks itself on download" (GEZIEN, beschrijving Gumroad, 27 nov). Slepen kan al sinds Blender 4.2: "Use the drop-down menu in the top right, or drag-and-drop an extension .zip package into Blender" (DERDEN, https://docs.blender.org/manual/en/4.2/editors/preferences/extensions.html).
3. **Geen losse solver meer installeren.** De solver zit als wheels per platform in de zip (`blender_manifest.toml` r. 15 tot 22, `wheels/`), omdat dat de grootste klacht was (zie hieronder).

## Wat gebruikers klagen (Gumroad-beoordelingen, GEZIEN)
Van de 25 beoordelingen met 3 sterren of minder gaan er **17 over "werkt niet in mijn Blender" of "installeren lukt niet"**, niet over de functies. Voorbeelden:
- "As it stands, it doesnt work on the current version of blender citing incompatibility issues with Python." (1 ster, 28 jul 2026)
- "It doesn't work on blender 5.1 :( ... please update it." (2 sterren, 20 jun 2026)
- "Incompatible refund due" (1 ster, 6 jul 2026)
- "Can't install it for some reason, says Module isn't registered" (1 ster, 10 mei 2025)
- "I tried the free version, did not work, tried the payed version still do not work ... It is because I have a MAC?" (1 ster, 24 nov 2024)
- "Doesn't work. Paid for an add-on that doesn't work. Can you refund me, please?" (1 ster, 1 apr 2024)
- "The instructions ... are written for people who already know Blender but MOST people will not." (1 ster, 27 mrt 2024)
- Twee klagen over de Gumroad-stap zelf: "i do not want see all this spam to just download zip" en "You could have just given a link to the file" (1 ster, mei 2024).

**De maker antwoordde op 0 van de 133 Gumroad-beoordelingen** (GEZIEN, veld `response` overal leeg). Op Extensions antwoordde hij wel op de enige review. Een lage beoordeling op Gumroad blijft dus voor altijd zonder uitleg onder de knop staan.

## Welk product van ons wordt er beter van
**Click Cuts (lancering week van 30 nov), daarna Click Joints Pro.**

Onze add-ons draaien in de e2e al op 4.2, 5.2 en 5.3 (Click Joints Pro) en 4.2 en 5.3 (Click Cuts) (GEZIEN, `producten/blender-gewrichten/KAART.md` en `producten/blender-splitser/KAART.md`), dus het versiegat van CAD Sketcher hebben wij niet. Het installeergat wel: de Docs-tab (`producten/blender-splitser/winkel/docs.md` r. 14) en de FAQ (`winkel/faq.md` r. 15 en 16) van Click Cuts geven alleen de weg via Edit > Preferences > Get Extensions > drop-down > Install from Disk en "do not unzip it". Slepen (één stap) staat er niet, en de Mac die de zip zelf uitpakt ook niet. Juist kopers die nieuw zijn in Blender (onze eigen `concurrentie.md` r. 107) lopen daar vast, en bij een betaalde add-on wordt dat een terugbetaling of 1 ster (zie de citaten). Gezet als issue bij de Productbouwer.

Later (na de sale, voor Bram): een "What's New" zoals hierboven in Click Joints Pro bij 1.2.9, omdat 1.2.9 iets doet wat een koper moet weten (Pro zet de gratis versie zelf uit, nieuw paneel). Wat het oplevert is een GOK: minder vragen en verwarring na een update, geen directe verkoop. Niet als issue gezet; eerst Click Cuts.

Bijvangst voor de Gumroad-pagina van Pro (Bram, na de sale): "After you buy" (`platformen/blender/pro-gumroad-na-kopen-1.2.8.md`) noemt ook alleen de menuweg; dezelfde twee regels (slepen, Mac) passen daar.
