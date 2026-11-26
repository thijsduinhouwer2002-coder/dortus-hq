# Click Cuts 1.0.0: lanceerbundel voor Superhive en Gumroad

Productbouwer, do 26 nov 2026 ±15:00 NL, issue #188. Voor de hoofdchat (die plakt in de Chrome van Thijs; inloggen en voorwaarden alleen Thijs). Alles wat al gekeurd is, op één plek, in de volgorde van de formulieren. Hier staat geen nieuwe tekst: elk blok komt letterlijk uit een gekeurd bestand (bron erbij), en `winkel/controleer_lancering.py` kijkt dat na, samen met elk pad.

## 0. Eerst: Superhive moet nu ingediend worden, niet op 30 nov
- **Superhive keurt elk product, ook als je al een product hebt.** "Reviews typically take 3–5 days", en tijdens de keuring kan niets veranderen (DERDEN, [Checking Your Product Status](https://support.superhivemarket.com/article/195-checking-your-product-status), curl 26 nov ±14:45 NL).
- **Publicatiedatum:** in de rechterkolom van het formulier kies je "Publish on". Superhive schrijft: "You must set your publication date at least 2 weeks in the future ... Setting a date less than two weeks away may result in missing your planned publication date" (DERDEN, [How to Upload Your Products](https://support.superhivemarket.com/article/41-how-to-upload-products)). Of het formulier een eerdere datum weigert: GOK, niet gezien. Mijn advies: indienen vandaag of vrijdag, en de vroegste datum kiezen die het formulier toelaat, liefst ma 30 nov. Na goedkeuring gaat hij op die datum live; is die datum al voorbij, dan kort na goedkeuring.
- **Gumroad heeft geen keuring vooraf:** daar kan Click Cuts op ma 30 nov meteen live. Discover pas na de eerste verkoop (zoals bij Pro, `platformen/blender/superhive-pagina.md`).
- Dus als Superhive pas na 30 nov goedkeurt: Gumroad gaat gewoon live, Superhive volgt vanzelf.

## 1. De zip (beide winkels dezelfde)
- **Gebruik:** artefact `click-cuts-kandidaat` uit e2e-run [45810355179](https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/45810355179) (groen, commit 26cb36c). Het artefact is een zip om de zip heen: uitpakken en `click_cuts-1.0.0.zip` uploaden.
- **sha256:** `90f4da5607dccc48488e9ec618e88df7923648efd6da4635ec8d7aeac21bcba7`, 24 bestanden, SHA256SUMS klopt (GEZIEN, zelf gedownload 26 nov ±14:30 NL). De inhoud is bestand voor bestand gelijk aan `producten/blender-splitser/split_joints/` op main (GEZIEN, `diff -r`), dus dezelfde add-on als kandidaat 6ed3951d van #117 (de hash verschilt alleen door de tijd in de zip).
- **Moet nog:** vastzetten voor 30 dagen (tag `click-cuts-uitgave-45810355179` of de knop in `click-cuts-uitgave.yml`). Het kandidaat-artefact verloopt **zo 29 nov ±12:27 NL** (GEZIEN, `expires_at`).
- **Niet gebruiken:** het vastgezette artefact `click-cuts-zip-1.0.0` uit run 45682766859 (sha256 6049f5ce...). Daar zitten de magneten nog niet in, en de winkeltekst belooft ze wel.
- Extensie-id `click_cuts` (`split_joints/blender_manifest.toml`): geen ander product "Click Cuts" op Superhive of extensions.blender.org gevonden (GEZIEN, curl 26 nov). Superhive weigert een id die van een andere maker is (DERDEN, [Why Products Get Rejected](https://support.superhivemarket.com/article/186-why-products-get-rejected) punt 7).

## 2. Superhive, in de volgorde van het formulier
Bron voor de volgorde: [How to Upload Your Products](https://support.superhivemarket.com/article/41-how-to-upload-products) (DERDEN).

**Primary Information**

Title (blinde test plek 1 bij beide rechters als "Pin Connectors", "or Magnet" erbij in #144, Daan ja #158; bron `producten/blender-splitser/galerij.md`):
```
Click Cuts: Split Models for 3D Printing to Fit Your Printer Bed (One Click, Pin or Magnet Connectors, Fit Test, Part Numbers)
```
Te lang voor het veld? Dan de korte titel van Chris (`platformen/blender/superhive/click-cuts-winkeltekst.md` punt 1, Daan #110 en #131):
```
Click Cuts: Split Models for 3D Printing to Fit Your Printer Bed, with Pin or Magnet Connectors
```

Excerpt (korte regel; de haak, GESLAAGD in dezelfde blinde test, bron `galerij.md`):
```
Pick your printer. Click once. Every part fits.
```

Description. Volgorde zoals de geteste tekst B: haak, eerste alinea (bron `galerij.md`, met M1 van Daan #12 "the cut faces"), dan wat Chris al gekeurd had (`click-cuts-winkeltekst.md` punt 2 tweede zin, punt 3 en de korte FAQ). De koppen in vet; de lange tekst `click-cuts-winkeltekst-lang.md` niet gebruiken, want die zegt nog "a number on every cut face" (oud, vóór M1).
```
**Pick your printer. Click once. Every part fits.**

Press Split to fit and Click Cuts plans every cut for you, so each part fits your bed, with pins, pin holes and an engraved part number on the cut faces. Each part turns green when it fits, is watertight and has enough wall around its holes, or orange or red with the reason. Print the small fit test block first and you know which clearance fits your printer, so pins are not loose or stuck.

Made for busts, cosplay props, terrain and statues that are too big for one print.

- **Split to fit:** one button cuts the selected model into parts that fit your printer bed, with pins, pin holes and part numbers.
- **Your printer:** 9 printers with their usable bed size, or type your own size.
- **Fit test:** print one small block with your own pin at four clearances, pick the one that fits, and Click Cuts keeps it for that printer and material.
- **Check:** every part is green (fits, watertight, enough wall around the holes), orange or red, with the reason.
- **Free cut:** an extra cut at any angle through one part.
- **Lay parts flat:** on export, every part is turned so a flat face, usually a cut face, lies on the bed, if it still fits your printer. On by default.
- **Make watertight** when the model has holes, on a copy.
- **Export** all parts and pins as STL or 3MF in millimeters. Wrong unit is caught at once, with Convert to mm.
- Blender 4.2 and newer. Tested in Blender 4.2 and 5.3 on every change.
- **Pins or magnets.** Round pins with your own clearance, printed separately. Or switch Joint to Magnets: a hole for a disc magnet on both sides of every cut (5x2, 6x2, 6x3, 8x3 or 10x3 mm), with at least 1.2 mm wall around it. Magnets are not included.

**Where to find it:** press N in the 3D viewport and open the Click Cuts tab.
```
De korte FAQ van Chris laat ik hier weg: die vragen staan woord voor woord in de FAQ-tab (punt "Documentation & FAQs" hieronder), en Superhive toont die tab op de pagina.

**Publish on** (rechterkolom): zie punt 0.

**Featured Image** (2:1, minstens 1200 x 600, JPG, onder 5 MB):
- `ontwerp/cuts-hoofdbeeld/beelden/paard-2400x1200.jpg` (307 KB). GESLAAGD Gemini 1,0 en ChatGPT 1,0 (`organisatie/blindtest/uitslag/click-cuts-hoofdbeeld-2026-11-25-0059.md`), Daan ja (#34, nakeuring #44).
- Superhive: "Overlays on featured images are discouraged but will be permitted in some cases" (DERDEN, artikel 41). Vraagt de keurder om minder tekst: `paard-kort-2400x1200.jpg` (alleen naam en haak), ook GESLAAGD in dezelfde test.

**Product Images** (minstens 5 beelden in totaal, alle 2:1, minstens 1200 breed; DERDEN, artikel 41 en 186), in deze volgorde:

| # | Bestand | Blinde test | Keuring |
|---|---|---|---|
| 1 | `ontwerp/cuts-galerij/beelden/nummer-paard-2400x1200.jpg` | GESLAAGD 2,0 en 1,5 (`click-cuts-galerij-nummer-paard-2026-11-26-0200.md`) | Daan #129 (M1 verwerkt, geen nieuwe test) |
| 2 | `ontwerp/cuts-galerij/beelden/passend-2400x1200.jpg` | GESLAAGD 1,0 en 1,0 (`click-cuts-galerij-passend-2026-11-25-1258.md`) | Daan #78 |
| 3 | `ontwerp/cuts-galerij/beelden/paneel-2400x1200.jpg` | GESLAAGD 1,0 en 1,0 (`click-cuts-galerij-paneel-2026-11-25-1446.md`) | Daan #82 en nakeuring #90 (opnieuw gemaakt met "Horse (closed)") |
| 4 | `ontwerp/cuts-galerij/beelden/magneet-2400x1200.jpg` | GESLAAGD 2,0 en 2,0 (`click-cuts-galerij-magneet-2026-11-26-0526.md`) | Daan #141 |

Met het hoofdbeeld zijn dat 5. Niet gebruiken: `nummer-2400x1200.jpg` (vervangen door `nummer-paard`, Thijs vroeg "wat moet het voorstellen?", #105). Bijschriften per beeld (als het formulier ze vraagt): onderschrift 4, 6, 7 en 8 uit `galerij.md`.

**Demo Video, Categories & Tags**
- Demo Video: leeg laten tot de lanceer-Short klaar is (#135, Regisseur). Later toevoegen kan.
- Category: Add-ons, sub-category Modeling (zoals Cleave en Click Joints Pro, GEZIEN op hun pagina's, curl 26 nov).
- Tags (de woorden waarop kopers zoeken en die Cleave gebruikt, GEZIEN op `superhivemarket.com/products/cleave`; alleen wat 1.0.0 doet, dus geen dovetail, press-fit of ball joints): `3d printing`, `3d model for printing`, `split`, `split model`, `connectors`, `magnet`, `pins`, `printer bed`, `cosplay`, `statue`, `stl`, `3mf`. Haalt het formulier minder: de eerste 6.

**Software Version, Files, Variations & License**
- Blender-versie: 4.2 en nieuwer (manifest `blender_version_min = "4.2.0"`; e2e groen in 4.2.23 en 5.3.0).
- File: `click_cuts-1.0.0.zip` uit punt 1.
- License: GPL (manifest `GPL-3.0-or-later`).
- Variations en prijs (besluit Thijs 25 nov 22:03 in `organisatie/besluiten.md`: introprijs $19 tot en met 14 dec; varianten uit `click-cuts-winkeltekst.md` punt 4):
  - **Standard: $19** tot en met zo 14 dec, daarna $24 (herinnering zetten voor ma 15 dec).
  - **Supporter: $29**, tekst: `Same add-on. Pick Supporter if you want to support updates.`
  - Een doorgestreepte introprijs via een eigen Shop Sale Campaign werkt niet tijdens een sitebrede sale (DERDEN, artikel 315 in `platformen/blender/superhive/README.md`), en de Superhive Cyber Sale loopt t/m wo 2 dec (`besluiten.md` r. 28). Daarom gewoon $19 als prijs, zonder doorstreping.
  - Let op: staat de winkel op "Opt-in to all sitewide sales", dan doet Click Cuts mee aan de Cyber Sale als hij vóór 3 dec live is (35% van $19 = $12,35; GOK dat de opt-in per winkel ook nieuwe producten raakt). Dat mag; wie dat niet wil, haalt Click Cuts uit de campagne.

**Documentation & FAQs**
- Documentation: blok "Tekst voor de tab" uit `producten/blender-splitser/winkel/docs.md` (Daan ja #169, nakeuring #176). Superhive eist dat de uitleg op de pagina zelf staat, niet alleen een link (DERDEN, artikel 186 punt 4): dat doet deze tekst.
- FAQ: blok "Tekst voor de tab" uit `producten/blender-splitser/winkel/faq.md`, één vraag per vak (Daan nakeuring #176, 8,5).

**Collaborators & Dev Fund:** leeg laten.

**Submit for review** (niet alleen opslaan). Status wordt Pending. Daarna niets meer aanpassen tot Approved.

## 3. Gumroad (ma 30 nov live)
- **Name:** dezelfde titel als Superhive (punt 2), met dezelfde reserve als het veld te kort is.
- **Description:** hetzelfde blok als Superhive (punt 2), met daaronder de korte FAQ uit `click-cuts-winkeltekst.md` (Gumroad heeft geen FAQ-tab).
- **Summary (korte regel):** eerste zin uit `click-cuts-winkeltekst.md` punt 2: "Pick your printer, click Split to fit, and Click Cuts cuts your model into parts that fit your bed, with pins, pin holes and part numbers on the cut faces. A small fit test block tells you which clearance fits your printer before you print the big parts."
- **Cover** (16:9), in deze volgorde: `ontwerp/cuts-hoofdbeeld/beelden/paard-1920x1080.jpg`, dan `ontwerp/cuts-galerij/beelden/nummer-paard-1920x1080.jpg`, `passend-1920x1080.jpg`, `paneel-1920x1080.jpg`, `magneet-1920x1080.jpg`. Zelfde tests en keuringen als punt 2.
- **Thumbnail** (vierkant): `ontwerp/cuts-hoofdbeeld/beelden/paard-vierkant-1200x1200.jpg` (of `paard-vierkant-600x600.jpg`). GESLAAGD 1,0 en 1,0 in twee rondes (`click-cuts-vierkant-gumroad-r2-2026-11-26-0656.md`), Daan ja 8,5 (#151).
- **Prijs:** $19 tot en met 14 dec, daarna $24. Versie **Supporter $29** (zelfde zip, zelfde tekst als Superhive).
- **Content (wat de koper na het kopen ziet):** de zip uit punt 1, plus het blok "Tekst voor de tab" uit `winkel/docs.md`.
- **Category:** 3D > 3D Assets > Blender (zoals Pro). **Tags:** dezelfde als Superhive.
- **Bundel Figure Print Kit:** pas **wo 2 dec**, niet bij de lancering (`click-cuts-winkeltekst.md` punt 5, keuring M1: tot en met 1 dec is los goedkoper door CYBER25).

## 4. Na het live gaan (hoofdchat)
- Link van beide pagina's in `producten/blender-splitser/KAART.md` en het bord.
- Zin over Click Cuts op de Pro-pagina's (bundelzin) pas op 2 dec, met de bundel.
- Marketing blijft stil tot `marketing/STOP` weg is.

## 5. Wat ik niet kon nakijken
- Of Superhive een titel van 117 tekens toelaat (GOK; Cleave heeft ±110 en staat er zo op). Daarom de korte titel als reserve.
- Of het formulier een publicatiedatum binnen 2 weken weigert (GOK).
- Inloggen mag ik niet, dus het formulier zelf heb ik niet gezien; de volgorde komt uit artikel 41.
