# Easy-Print (gratis Blender-add-on: model doorsnijden en verbinders maken)

Afkijker, za 28 nov 2026 ±03:30 NL, issue #20. Waarom deze: bij de split-termen op extensions.blender.org staat Easy-Print bovenaan, en daar loopt een koper van Click Cuts nu naar een gratis concurrent (`organisatie/lat/vindbaar-zoektermen.md`).

## Feiten (alles curl, GEZIEN 28 nov 03:30)
- Pagina: https://extensions.blender.org/add-ons/easy-print/ , maker "Dagnia", versie 0.1.2 (31 aug 2026), gepubliceerd 29 juli 2026.
- **8.111 downloads in 4 maanden**, 3 reviews, gemiddeld 4,0. Dat is ±67 downloads per dag (GOK, gemiddelde uit GEZIEN-cijfers).
- Licentie GPL-3.0-or-later (`LICENSE` en `blender_manifest.toml` in de zip). Code gelezen uit de zip van de Extensions-pagina (200 kB), niets uitgevoerd. GitHub-issues (github.com/fzhe5124-cmyk/easy-print) niet te lezen: buiten de toegang van deze run, api 403.
- Tagline: "Cut models and generate interlocking connectors for 3D printing". Tags alleen "Modeling" en "Mesh".
- In het paneel drie verbinders: Tab & Slot, Peg & Hole, Dovetail (`__init__.py` r. 102 tot 106). De code heeft er al vijf: ook Ball & Socket en Bolt & Nut met schroefdraad (`core/connectors.py` r. 124 tot 128, en de README in de zip noemt ze). De maker schrijft in een review-antwoord dat "version 2 is almost ready" (reviewpagina, GEZIEN). Een gratis splitser met zwaluwstaart, kogel en schroef komt er dus aan (GOK op de datum).

## Wat ze slim doen (bestand en regels)
1. **Uitleg in beeld tijdens het bijstellen.** Na "Generate Connectors" staan vier regels linksonder in de 3D-weergave: "LMB: Confirm  Esc: Cancel  F: Flip", "Wheel: Height  Shift+Wheel: Size" (`operators/connector_op.py` r. 75 tot 101, blf met schaduw zodat het op licht en donker leesbaar is). De koper hoeft niets te onthouden.
2. **Bijstellen met het muiswiel, met live voorbeeld.** Wiel = hoogte van de pen, Shift+wiel = maat, F = mannelijk en vrouwelijk wisselen; het voorbeeld wordt pas 0,25 s na de laatste draai opnieuw berekend (r. 282 tot 293 en 405 tot 430), dus het blijft vlot.
3. **Röntgen aan tijdens het bijstellen** en daarna terug zoals het was (r. 226 tot 227, 324). Voorbeeldkleuren: mannelijk blauw, vrouwelijk oranje (r. 710).
4. **Maat volgt het snijvlak:** breedte en hoogte 15% van de wortel van het snijoppervlak, nooit dieper dan de halve dikte van het deel (`core/connectors.py` r. 432 tot 470). Werkt zo in elke eenheid; de commentaarregel zegt dat een oudere versie met vaste millimeters op meterschaal ontplofte.
5. **Ctrl tijdens het trekken = snappen op 5 graden** (paneeltekst, `panels/main_panel.py`).

## Wat gebruikers klagen (reviewpagina, alle 3 reviews, GEZIEN)
- "Nice idea, but I just get the message '1 closed face(s) detected. Hover to select.' I am stuck" (SHARK, 0.1.2). De melding zegt niet wat je nu moet doen.
- De snijlijn wordt een oneindig vlak en snijdt ook op plekken die je niet wilde (hyzhyz, 0.1.1). De maker geeft een omweg van vijf stappen en belooft versie 2.
- Eén korte lof: "quick and easy to use".

## Wat dit betekent voor ons
- **Click Cuts doet de twee klachten al beter:** bij Draw cut licht het deel dat eraf gaat wit op met "comes off" en een knop Flip side (`producten/blender-splitser/split_joints/vrije_snede.py`, kaart 26 nov 20:38). Dat mag vooraan in beelden en video: "you see which part comes off before you cut".
- **Het geld zit in hun bereik, niet in hun functies.** Een gratis add-on van 0.1.2 met 3 reviews haalt ±67 downloads per dag op Extensions (GOK uit GEZIEN). Click Cuts staat daar niet. Dat is precies route C van #323 (gratis Click Cuts Lite op Extensions die naar de betaalde versie wijst); geen nieuw issue, wel een reactie daar.
- **Na de lancering (geen nieuwe functie nu, regel uit #319):** de uitlegregels in beeld en het muiswiel voor de penmaat (punt 1 en 2) zijn klein en zouden het bijstellen na de split even makkelijk maken als bij Easy-Print. Bestanden bij ons: `split_joints/vrije_snede.py` heeft al een tekenhandler met blf (r. 401, 705 tot 750), dus de uitlegregels passen daar. Zwaluwstaart staat al als open gat in `organisatie/lat/click-cuts.md` (Cleave heeft hem); als Easy-Print 2 hem gratis geeft, wordt dat gat groter.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
