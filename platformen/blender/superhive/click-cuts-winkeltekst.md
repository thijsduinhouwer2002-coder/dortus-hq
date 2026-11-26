# Click Cuts: winkeltekst Superhive en Gumroad (CONCEPT)

Chris, di 24 nov 2026 (eerste versie ±06:40 NL). Opdracht hoofdchat 04:25 en 06:25, besluit bundel 07:15. Status: CONCEPT. Keuringen 1 tot 3 verwerkt, derde akkoord ja (065f7d7). 24 nov ±12:45 NL: 4.2-snelheid naar meting, geheugen-FAQ en slicer-FAQ erbij; **vierde keuring akkoord ja (b62c304)**, kan-punten K1, K2 en K4 daarna verwerkt. **Klaar om te plakken bij de uitgave** (skill `keuren`, door een ander). Plakken doet Thijs bij de uitgave (week van ma 30 nov). **25 nov ±22:30 NL (issue #104):** Lay parts flat en Free cut in lijst en FAQ, oude zin "Not automatically" weg; keuring Daan #110 akkoord ja, kan-punten K1 ("Partly.", "a character's face") en K2 (lange tekst Amerikaanse spelling) verwerkt 26 nov. **Weer klaar om te plakken.** 26 nov ±00:40 NL (issue #117, op tak `claude/click-cuts-magneet`): magneten in lijst en FAQ; deze versie geldt pas als de magneetcode in de zip zit, anders de versie op main.
Alleen wat kandidaat 1.0.0 doet (`producten/blender-splitser/CHANGELOG.md`, `architectuur.md`). Pennen of magneetgaten (tak `claude/click-cuts-magneet`, issue #117, alleen geldig als die in de zip zit): geen klikverbinders, geen deuvels, geen zwaluwstaart.

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
- **Lay parts flat:** on export, every part is turned so a flat face, usually a cut face, lies on the bed, if it still fits your printer. On by default.
- **Make watertight** when the model has holes, on a copy.
- **Export** all parts and pins as STL or 3MF in millimeters. Wrong unit is caught at once, with Convert to mm.
- Blender 4.2 and newer. Tested in Blender 4.2 and 5.3 on every change.
- **Pins or magnets.** Round pins with your own clearance, printed separately. Or switch Joint to Magnets: a hole for a disc magnet on both sides of every cut (5x2, 6x2, 6x3, 8x3 or 10x3 mm), with at least 1.2 mm wall around it. Magnets are not included.

**Where to find it:** press N in the 3D viewport and open the Click Cuts tab.

Oranje: de bouwer heeft het geel echt oranje gemaakt (commit 36912d5, keuring K1), dus "orange" klopt. Spelling Amerikaans zoals de add-on zelf ("millimeters", "color").

**Korte FAQ (Engels, onderaan de pagina):**
- *Why not just use my slicer's cut tool?* A slicer cuts one plane at a time, and you set every cut and connector yourself. Click Cuts plans all the cuts so every part fits your bed, checks each part (green fits, orange or red tells you why), numbers the parts, and uses the clearance from your own fit test print.
- *Which connectors?* Round pins, or holes for disc magnets (5x2, 6x2, 6x3, 8x3 or 10x3 mm; you buy the magnets). The magnet hole gets your clearance on the diameter and 0.3 mm extra depth for glue. No dovetails or snap keys.
- *How do I glue the magnets?* Glue the magnets with matching poles: stick a magnet to the one already glued before you press it in.
- *Does it fix broken meshes?* Make watertight makes a closed copy (voxel remesh). Very large or detailed models may need to be cleaned first.
- *Do parts lie flat for printing?* Yes. Lay parts flat (on by default) turns every part on export so a flat face, usually a cut face, lies on the bed, if it still fits your printer. Otherwise the part keeps its own way up.
- *Can I choose where it cuts, so it does not go through a character's face?* Partly. Split to fit cuts along the X, Y and Z axes. After splitting, Free cut adds a cut at any angle through one part, for example an arm at the shoulder, with pins and numbers like the other cuts.
- *Thin or hollow models?* Some joints have no room for a pin or magnet; Click Cuts tells you which ones to glue.
- *How fast is it?* Tested on a 1 million face scan in Blender 5.3: about 40 seconds (2-core test machine). In Blender 4.2 to 4.4 the same scan takes about 3 minutes. Big models show a time estimate under Split to fit.
- *How much memory?* Very large models (3 million faces) need a lot of memory in Blender 4.2 to 4.4: about 9 GB. Blender 5.3 needs about 5 GB. With 8 GB of memory, use Blender 5.3 for models that big.
- *Which Blender?* 4.2 and newer.
- *Does it work with Click Joints Pro?* Yes, side by side. Splitting makes it fit on the bed. Click Joints Pro makes it move.

Bronnen FAQ (bijgewerkt 24 nov ±12:45 NL, Chris, opdrachten Productbouwer 10:50, hoofdchat 10:45 en kwartier 12:25):
- **4.2-snelheid:** "about 3 minutes" rust op de 1M-schedel in 4.2.23: 106 s in CI (run 45349335526) en 186 s op een machine met 2 kernen (GEZIEN, `producten/blender-splitser/ontwerp.md` deel 14b). Zelfde machine als de 40 s in 5.3 (2 kernen) geeft 186 s, dus 3 minuten. De paneelregel zegt in 4.2 bij 1M ook "about 3 min" (`in_een_klik.SEC_PER_MILJOEN`, Exact 190 s per miljoen). Let op: sinds de Productbouwer (24 nov ±13:00) rondt het paneel naar boven en zegt het bij 1M in 4.2 "about 4 min"; "about 3 minutes" in de FAQ mag volgens hem blijven (153 tot 186 s gemeten, CI 106 s). Zijn voorstel "use Blender 4.5 or newer" niet overgenomen: 4.5 zelf is niet gemeten en het zou een vijfde keuring vragen. De oude zin "about twice as long" is weg: gemeten is 2,4 tot 4,4 keer (Daan B1, keuring run 10).
- **Time estimate:** de paneelregel onder de knop is nu een tijdschatting per versie ("1.0M faces: Split takes about 1 min" in 5.3), `in_een_klik.schatting_tekst`, getoond in `paneel.py` r. 40 tot 41. Daarmee is ook K4 van de derde keuring (twee verhalen) opgelost.
- **Geheugen:** piek bij 3,04M vlakken 9.220 MB in 4.2.23 en 4.741 MB in 5.3.0 (GEZIEN, CI run 45367520845; `producten/blender-splitser/keuring/2026-11-24-run10-daan.md` r. 7 en C1). "About half" klopt (51%).
- **Slicer-vraag:** Bambu Studio, OrcaSlicer en PrusaSlicer snijden per vlak met Plug, Dowel of Snap (DERDEN, `producten/blender-splitser/concurrentie.md` r. 77 en 78, links naar de Bambu-wiki en Prusa-help). Elk deel van ons antwoord nagekeken in 1.0.0: alle sneden in één klik tot alles op het bed past (Split to fit), groen, oranje of rood per stuk met reden (Check), onderdeelnummers, speling uit de Fit test per printer en materiaal. Geen concurrentnaam in de Engelse tekst.
- **Niet in de tekst, wel om te weten:** in 4.2 kwam op de 1M-schedel 1 van 8 stukken rood terug ("not watertight", 2 randen in het snijvlak met 4 vlakken; in 5.3 8 van 8 groen). De Productbouwer herstelt dat. Het paneel zegt het zelf eerlijk; geen belofte in de winkel geraakt.
- **4.2 to 4.4** (vierde keuring K2): ook 4.3 en 4.4 nemen de trage Exact-weg; Manifold pas vanaf 4.5 (`splitsen.solver_naam`). Gemeten is alleen 4.2 (GEZIEN); 4.3 en 4.4 volgen uit de code. "About 5 GB" in 5.3 = 4.741 MB (GEZIEN). Het advies voor 8 GB is niet op zo'n machine getest (GOK, 4,7 GB past onder 8).
- Kan-punten derde keuring C1 (Where to find it onder de lijst) en C2 (dubbele testzin in de FAQ) meteen meegenomen.

Oudere bronnen FAQ: dunne vlakken krijgen "too small for a pin ... Glue this joint" (`verbinders.py`, `verbind_3d.py`); snelheid GEZIEN in `producten/blender-splitser/ontwerp.md` deel 14 (1M 42 s in 5.3), versiezin op aanwijzing van Daan (`ontwerp/keuringen/2026-11-24-click-cuts-snelheid-daan.md` M1). "Twice as long" in 4.2 is afgeleid (GOK) uit Daans meting: op 0,5M vlakken was 4.2 1,8 keer zo traag als 5.3 (GEZIEN, Daan B1); de 1M-meting in 4.2 volgt (Daan K1). Die 1M-meting is er nu (zie hierboven); de GOK is vervangen door GEZIEN.

Bronnen Lay parts flat en Free cut (Productbouwer, 25 nov ±22:30 NL, issue #104, lat gat 2 en 3):
- **Lay parts flat:** knopnaam letterlijk uit `eigenschappen.py` (`plat`, name "Lay parts flat", default True), staat in het paneel boven Export (`paneel.py` r. 162). Werkt bij export (`exporteer.py` r. 123 tot 132): elk stuk draait zo dat het grootste platte vlak onder ligt (`plat.py`: meestal een snijvlak, bij een stuk met een eigen platte bodem kan die winnen, daarom "usually a cut face"), alleen als het dan nog op het bed past; anders houdt het stuk zijn eigen stand (description in `eigenschappen.py`). Pennenplaten liggen al plat. In 1.0.0 sinds 25 nov (keuring `producten/blender-splitser/keuring/2026-11-25-plat-in-1.0.0-daan.md`).
- **Free cut:** `vrije_snede.py` r. 1 tot 12 (elke hoek, één stuk, pennen en nummers uit dezelfde planner `verbind_3d.plan_alles`), paneel "Free cut (one piece, any angle)" (`paneel.py` r. 152). Rasterneden langs X, Y en Z: `ontwerp.md` deel 3.
- Geen belofte over passen, klikken of printen.

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
- **Superhive: bundels bestaan, maar niet bij de uitgave** (aparte adressen onder `/bundles/`). Een add-onmaker doet het al: "Lazy3D Bestselling Add-ons Bundle", 7 producten, Sales 20+ (GEZIEN, [Superhive](https://superhivemarket.com/bundles/lazy3d-bestselling-add-ons-bundle)). Hoe je hem aanmaakt staat niet in de openbare hulp die ik met curl kon lezen.

Om op te letten:
0. **Pas na di 1 dec live zetten (keuring M1).** Tot en met 1 dec geeft CYBER25 25% op Pro op Gumroad (`commercie/blender-click-joints/black-friday.md`): los $14,25 + $19 = $33,25, goedkoper dan de bundel van $34. Dus de bundel gaat op **wo 2 dec** live, niet eerder. Click Cuts zelf kan gewoon in de week van 30 nov.
1. **Tot en met 14 dec is de korting klein:** $19 + $19 = $38 tegen $34. Dat is goed (de bundel wordt na 14 dec vanzelf aantrekkelijker), maar noem in posts tot 14 dec de losse startprijs, niet de bundel.
2. **Geen bundel op Superhive bij de uitgave** (besluit hoofdchat 07:15). Pro kost daar $12 (GEZIEN 24 nov): los $12 + $19 = $31 tot en met 14 dec, dus $34 zou daar duurder zijn dan los. Na 14 dec bekijken we een Superhive-bundel onder de losse som ($36), bijvoorbeeld $29.
3. **Wie de bundel instelt, kijkt die dag de prijs van Pro in beide winkels na.**

## 6. Wat we niet beloven (staat niet in 1.0.0)
Geen klikverbinders, deuvels, zwaluwstaart of kogels; geen automatische onderdelenherkenning; geen uithollen of steun; geen sneden die zelf de vorm volgen (alleen assen plus Free cut met de hand); geen "repairs any AI model" (Make watertight is een voxelkopie die boven 3000 voxels weigert).

Na 14 dec nakijken dat Gumroad bij de bundel $43 doorgestreept toont: die waarde ligt vast op het moment dat je de bundel bouwt (keuring K4). Tags en hoofdbeeld horen bij Daan en Sanne (K5).

Bronnen magneten (Productbouwer, 26 nov ±00:40 NL, issue #117): Joint Pins/Magnets en de maten in `eigenschappen.py` (`verbinder`, `magneet`) en `verbinders.MAGNETEN`; speling op de diameter, 0,3 mm lucht (Daan #120 M1) en minstens 1,2 mm wand in `verbinders.magneet_opties`; geen penplaatjes en geen magneten bij de levering (`verbind_3d.plan_alles`, paneelregel "magnets not included"). Gemeten in de e2e `toetsen_magneet.py`.
