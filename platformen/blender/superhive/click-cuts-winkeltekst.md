# Click Cuts: winkeltekst Superhive en Gumroad (CONCEPT)

Chris, di 24 nov 2026 (eerste versie ±06:40 NL; de tijden ±14:30 en ±14:45 die hier eerder stonden waren een klokfout, keuring 2 B1). Bijgewerkt 24 nov ±09:50 NL. Opdracht hoofdchat 04:25 en 06:25, besluit bundel 07:15. Status: **CONCEPT, keuring 1 nee (M1), herkeuring ja (14a3633), tweede keuring nee (M1 bundel Superhive, M2 pen en nummer); M1, M2, snelheidszin (Daan M1) en kan-punten K1, K2 deels en K3 verwerkt; derde keuring akkoord ja (065f7d7). Klaar om te plakken bij de uitgave.** (skill `keuren`, door een ander). Plakken doet Thijs bij de uitgave (week van ma 30 nov).
Alleen wat kandidaat 1.0.0 doet (`producten/blender-splitser/CHANGELOG.md`, `architectuur.md`). Alleen pennen: geen klikverbinders, geen magneten, geen deuvels, geen zwaluwstaart.

## 1. Titel (85 tekens)
`Click Cuts: Split Models for 3D Printing to Fit Your Printer Bed, with Pin Connectors`

Waarom deze woorden (GEZIEN, curl op `superhivemarket.com/search?search[q]=...`, 24 nov ±06:30 NL, eerste 12 uitkomsten):
- **"split model"**: #1 Cleave ("Model Split"), #2 Bed Fit Splitter, #4 PrintSplitter, #5 CatPin, #7 FigureCut. Wie bovenaan staat heeft "Split" plus "Model(s)" in de titel.
- **"split 3d printing"**: #1 Cleave, #2 SnapSplit, #4 Oryx CAD, #8 FigureCut, #9 PrintSplitter: allemaal "for 3D Printing" in de titel.
- **"printer bed"**: #1 Bed Fit Splitter ("Split Models to Fit Your Printer Bed", $19, nu $14,25), #2 CatPin, daarna geen splitters meer. Weinig buren, dus "Printer Bed" in de titel is goedkope winst.
- **"3d print connectors"**: #1 Cleave, #2 Split It, #3 CatPin: "Connectors" in titel of tekst.
- Bewust **niet** letterlijk de titel van Bed Fit Splitter overgenomen ("to Fit Your Printer Bed" staat bij ons achter "for 3D Printing"), en geen concurrentnaam.
- Het voorstel van de hoofdchat ("Split Big Models to Fit Your 3D Printer Bed, with Pin Connectors") mist de vaste combinatie "for 3D Printing"; daarom deze volgorde.

## 2. Eerste zin (voor de pagina, ook de korte beschrijving op Gumroad)
> Pick your printer, click Split to fit, and Click Cuts cuts your model into parts that fit your bed, with pins, pin holes and part numbers on the cut faces. A small fit test block tells you which clearance fits your printer before you print the big parts.

Tweede zin, voor wie het koopt:
> Made for busts, cosplay props, terrain and statues that are too big for one print.

Wat geen concurrent zo zegt (`producten/blender-splitser/concurrentie.md` punt 1 en 7): de passingproef met je eigen pen zit in de splitser zelf; Dovetail Key past niet zelf op het bed.

## 3. Wat het doet (lijst op de pagina)
- **Split to fit:** one button cuts the selected model into parts that fit your printer bed, with pins, pin holes and part numbers.
- **Your printer:** 9 printers with their usable bed size, or type your own size.
- **Fit test:** print one small block with your own pin at four clearances, pick the one that fits, and Click Cuts keeps it for that printer and material.
- **Check:** every part is green (fits, watertight, enough wall around the holes), orange or red, with the reason.
- **Free cut:** an extra cut at any angle through one part.
- **Make watertight** when the model has holes, on a copy.
- **Export** all parts and pins as STL or 3MF in millimeters. Wrong unit is caught at once, with Convert to mm.
- Blender 4.2 and newer. Tested in Blender 4.2 and 5.3 on every change.

**Where to find it:** press N in the 3D viewport and open the Click Cuts tab.

- **Connectors in 1.0.0 are pins.** Round pins with your own clearance, printed separately.

Oranje: de bouwer heeft het geel echt oranje gemaakt (commit 36912d5, keuring K1), dus "orange" klopt. Spelling Amerikaans zoals de add-on zelf ("millimeters", "color").

**Korte FAQ (Engels, onderaan de pagina):**
- *Which connectors?* Pins only in 1.0.0. No dovetails, magnets or snap keys.
- *Does it fix broken meshes?* Make watertight makes a closed copy (voxel remesh). Very large or detailed models may need to be cleaned first.
- *Do parts lie flat for printing?* Not automatically. You place them in your slicer.
- *Thin or hollow models?* Some joints have no room for a pin; Click Cuts tells you which ones to glue.
- *How fast is it?* Tested on a 1 million face scan in Blender 5.3: about 40 seconds (2-core test machine). In Blender 4.2 it takes about twice as long. Big models show a note under Split to fit.
- *Which Blender?* 4.2 and newer, tested in 4.2 and 5.3 on every change.
- *Does it work with Click Joints Pro?* Yes, side by side. Splitting makes it fit on the bed. Click Joints Pro makes it move.

Bronnen FAQ: dunne vlakken krijgen "too small for a pin ... Glue this joint" (`verbinders.py`, `verbind_3d.py`); snelheid GEZIEN in `producten/blender-splitser/ontwerp.md` deel 14 (1M 42 s in 5.3), versiezin op aanwijzing van Daan (`ontwerp/keuringen/2026-11-24-click-cuts-snelheid-daan.md` M1). "Twice as long" in 4.2 is afgeleid (GOK) uit Daans meting: op 0,5M vlakken was 4.2 1,8 keer zo traag als 5.3 (GEZIEN, Daan B1); de 1M-meting in 4.2 volgt (Daan K1). Komt die boven 2,5 keer, dan gaat de zin vóór het plakken om; komt de meting anders uit, dan past de zin zich aan. Wil de keurder geen GOK in de winkel, dan valt de 4.2-zin weg en blijft "in Blender 5.3" staan.

## 4. Varianten en prijs (voorstel; de prijs zet Thijs zelf, geld uitgeven is het niet)
| Variant | Prijs | Wat |
|---|---|---|
| Standard | **basisprijs $24, lanceerkorting naar $19 tot en met 14 dec** (op Superhive zo zichtbaar doorgestreept, keuring 2 C2) | alle functies, 1 persoon |
| Supporter | $29 | dezelfde functies, steunt de updates |

Onderbouwing: `concurrentie.md` punt 5. Cleave $23 en $28, Split $22 en $28 (GEZIEN 23 nov in `concurrentie.md`), CatPin $24 en $36 (DERDEN, keuring 23 nov). Of hun Supporter-variant precies dezelfde functies heeft, is niet nagekeken (GOK). Wat Supporter de koper geeft, op de pagina: "Same add-on. Pick Supporter if you want to support updates."

## 5. Bundel: "Figure Print Kit: Click Joints Pro + Click Cuts"
**Alleen op Gumroad** (besluit hoofdchat 24 nov 07:15). **Prijs voorstel: $34.** Los op Gumroad $19 (Pro) + $24 (Cuts) = $43, dus $9 minder (21%).
**Zin alleen voor de Gumroad-pagina's** (niet op Superhive):
> Joints that move and parts that fit your bed: get Click Joints Pro and Click Cuts together in the Figure Print Kit for $34.

Kan het?
- **Gumroad: ja.** Product type "Bundle", kies je eigen producten, eigen prijs; de koper ziet de losse waarde doorgestreept. Maar één variant per product in een bundel, en een bundel kan niet in een bundel (DERDEN, [Gumroad help: Product bundles](https://gumroad.com/help/article/339-product-bundles)). Instellen: Products, New Product, type Bundle, prijs $34, Click Joints Pro (Standard) en Click Cuts (Standard) kiezen.
- **Superhive: bundels bestaan, maar niet bij de uitgave** (aparte adressen onder `/bundles/`). Een add-onmaker doet het al: "Lazy3D Bestselling Add-ons Bundle", 7 producten, Sales 20+ (GEZIEN, [Superhive](https://superhivemarket.com/bundles/lazy3d-bestselling-add-ons-bundle)). Hoe je hem aanmaakt staat niet in de openbare hulp die ik met curl kon lezen; dat ziet Thijs in zijn verkopersomgeving. Kan het daar niet, dan alleen Gumroad.

Twee dingen om op te letten:
0. **Pas na di 1 dec live zetten (keuring M1).** Tot en met 1 dec geeft CYBER25 25% op Pro op Gumroad (`commercie/blender-click-joints/black-friday.md`): los $14,25 + $19 = $33,25, goedkoper dan de bundel van $34. Dus de bundel gaat op **wo 2 dec** live, niet eerder. Click Cuts zelf kan gewoon in de week van 30 nov.
1. **Tot en met 14 dec is de korting klein:** $19 + $19 = $38 tegen $34. Dat is goed (de bundel wordt na 14 dec vanzelf aantrekkelijker), maar noem in posts tot 14 dec de losse startprijs, niet de bundel.
2. **Geen bundel op Superhive bij de uitgave** (besluit hoofdchat 07:15). Pro kost daar $12 (GEZIEN 24 nov): los $12 + $19 = $31 tot en met 14 dec, dus $34 zou daar duurder zijn dan los. Na 14 dec bekijken we een Superhive-bundel onder de losse som ($36), bijvoorbeeld $29.
3. **Wie de bundel instelt, kijkt die dag de prijs van Pro in beide winkels na.**

## 6. Wat we niet beloven (staat niet in 1.0.0)
Geen klikverbinders, magneten, deuvels, zwaluwstaart of kogels; geen automatische onderdelenherkenning; geen uithollen of steun; delen worden niet vanzelf plat neergelegd; geen "repairs any AI model" (Make watertight is een voxelkopie die boven 3000 voxels weigert).

Na 14 dec nakijken dat Gumroad bij de bundel $43 doorgestreept toont: die waarde ligt vast op het moment dat je de bundel bouwt (keuring K4). Tags en hoofdbeeld horen bij Daan en Sanne (K5).
