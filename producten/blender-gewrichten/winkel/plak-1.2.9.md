# Plakkaart Click Joints Pro 1.2.9 (Bram, 27 nov 2026, issue #299)

**Plakken op ma 30 nov, door de hoofdchat, in de laatste meter.** Niet eerder: de sale loopt op 1.2.8 (Gumroad CYBER25 t/m 1 dec, Superhive 35% t/m 2 dec). Saleregels en prijzen blijven zoals ze staan; deze kaart raakt ze niet.

**Waarom (geld):** nu moet een koper die van de gratis versie komt die eerst zelf uitzetten (GEZIEN, curl 27 nov ±20:10 NL: Gumroad "After you buy", Superhive Docs-tab, Overview en FAQ zeggen alle vier "turn the free one off first" of "Disable the free ... first"). In 1.2.9 doet Pro dat zelf en zegt het in het paneel. Wie de gratis versie probeerde, is precies de koper die we in de saleweek willen; één drempel minder. Effect op verkoop: GOK, klein; vooral minder afhakers, vragen en terugbetalingen.

**Wat de koper ziet na het plakken:** de nieuwe zip, één regel "Coming from the free version? Just enable Pro" op alle vier de plekken, een versieblok en "What's new in 1.2.9", en op Superhive een FAQ die installeren met slepen en de Mac-valkuil uitlegt.

## Volgorde (stopt bij de eerste fout)
1. Zip ophalen (deel 1). Zip op Gumroad en Superhive vervangen.
2. Gumroad: blok 2a, 2b, 2c.
3. Superhive: blok 3a tot 3e.
4. Controle: `bash producten/blender-gewrichten/winkel/controle-1.2.9.sh` moet eindigen op `ALLES GOED` (code 0). Geeft hij FOUT: dat blok opnieuw plakken, dan opnieuw draaien. Superhive geeft soms een lege pagina of 429; dan na 5 minuten opnieuw.
5. Na ALLES GOED: regel in `commercie/geplaatst.md`, en een regel onderaan `berichten/bram.md` met de uitslag.

## 1. De zip

| | |
|---|---|
| Bestand | `click_joints_pro-1.2.9.zip` (179.325 bytes, GEZIEN) |
| Waar | e2e-run **46043092572** op main (commit fea86da), artefact `click-joints-pro-zip-e2e-5.3.0`; ingelogd te downloaden via https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/46043092572 |
| Groen in | Blender 4.2.23, 5.2.3 en 5.3.0 (alle drie de e2e-jobs `success`, GEZIEN via de API op 27 nov ±20:05 NL) |
| sha256 | `b419de10f271805472be5178dbc73f24b58263235ad4c561371135646450b9e7` (GEZIEN: zelf gedownload en nagerekend, gelijk aan het .sha256-bestand in het artefact) |
| Inhoud nagekeken | `blender_manifest.toml`: `version = "1.2.9"`, `name = "Click Joints Pro"`; 49 bestanden; `betaald/__init__.py` heeft de regel "Free Click Joints was turned off; Pro includes everything in it." (GEZIEN) |
| Code gelijk aan main | geen wijziging in `producten/blender-gewrichten/click_joints`, `e2e` of de e2e-workflow tussen fea86da en main 239a5d8 (git diff leeg, GEZIEN). #114 zit erin (op main sinds 99a3c69). |

**Let op de bewaartijd:** het artefact verloopt op **ma 30 nov 18:53 NL** (GitHub `expires_at` 17:53 UTC, GEZIEN). Download de zip dus vóór 18:50, of start ma 30 nov vóór 17:00 een verse e2e (opdrachtbestand met `blender-gewrichten-e2e.yml`, skill `actions`; duurt ±60 minuten) en neem de zip uit die run. Een verse run geeft een andere sha256 (tijdstempels in de zip); zet dan dat runnummer en die sha256 in `commercie/geplaatst.md`. Na het downloaden: `sha256sum click_joints_pro-1.2.9.zip` moet de waarde hierboven geven (of die van de verse run).

Niet uitpakken, niet hernoemen. Op Superhive als nieuwe versie uploaden (versie 1.2.9, Blender 4.2 tot 5.3 zoals nu), op Gumroad in de Content-tab de oude 1.2.8-zip vervangen door deze.

## 2. Gumroad, product Click Joints Pro (beschrijving)
https://duinhouwer8.gumroad.com/l/click-joints-pro

### 2a. Versieblok: vervang de regel "Version 1.2.8 (25 Nov 2026). ..." door
```
Version 1.2.9 (30 Nov 2026). Blender 4.2 or newer, tested on 4.2 LTS, 5.2 LTS and 5.3.
```

### 2b. Kopje "What's new in 1.2.8" met zijn drie regels: vervang door
Kopje (zelfde opmaak als nu), daaronder de regels als opsomming:
```
What's new in 1.2.9
- Coming from the free Click Joints? Just enable Pro: it turns the free version off for you and says so in the panel. Nothing is deleted.
- If your mesh has a rig, "Rig found" and the Figure from rig button are now the first thing in the panel.
- The fit test strip now sits right under Clearance, and the hinge buttons sit under Place joint, so each button sits in the step where you use it.
- After you place a hinge, step 3 says "Hinge placed" and shows its bend range next to the fit.
- After a Good fit and an export, one small line lets you leave a rating. Click a store or the X and it does not ask again. No popups.
```

### 2c. Kopje "After you buy": vervang de hele opsomming eronder door
(Dit neemt ook de sleep- en Mac-regels van #258 mee; staan die er al, dan vervangt dit ze gewoon.)
```
- Install: open Blender 4.2 or newer. Drag click_joints_pro-1.2.9.zip from your Gumroad library into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip.
- Got a folder instead of a zip? Safari on a Mac can unzip downloads by itself, and Blender cannot install a folder. Download it again with another browser, such as Chrome or Firefox, and drag the zip into Blender without opening it.
- Coming from the free version? Just enable Pro: it turns the free Click Joints off for you, and the top of the panel says so. Nothing is deleted, and your joints and settings stay in the .blend file.
- Open the panel: in the 3D viewport press N and open the Click Joints tab.
```
De regel "Already bought Pro? ..." eronder blijft staan.

**Content-tab (boven de zip), alleen als daar tekst staat:** vervang de installeerregels door
```
1. Install: drag the zip below into the Blender window (Blender 4.2 or newer) and confirm. Do not unzip it. Or use Edit > Preferences > Get Extensions, drop-down menu at the top right, Install from Disk.
   Got a folder instead of a zip? Safari on a Mac can unzip downloads by itself. Download it again with another browser and drag the zip into Blender.
   Coming from the free version? Just enable Pro: it turns the free one off for you.
   Then press N in the 3D viewport and open the Click Joints tab.
```

## 3. Superhive, product Click Joints Pro
https://superhivemarket.com/products/click-joints-pro

### 3a. Version History: nieuwe versie 1.2.9 met deze update log
```
1.2.9 (30 Nov 2026): Enabling Pro now turns the free Click Joints off for you. Cleaner panel: with a rig, Figure from rig is now at the top. Fit test strip and hinge buttons moved into step 2, the hinge range into step 3. A small rating line after a good export.
```

### 3b. Overview: blok "New in Pro 1.2.8" met zijn vier regels: vervang door
Kop vet zoals nu, regels eronder zoals nu:
```
New in Pro 1.2.9
Coming from the free Click Joints? Just enable Pro: it turns the free version off for you and says so in the panel. Nothing is deleted.
If your mesh has a rig, "Rig found" and the Figure from rig button are now the first thing in the panel.
The fit test strip now sits right under Clearance, and the hinge buttons sit under Place joint, so each button sits in the step where you use it.
After you place a hinge, step 3 says "Hinge placed" and shows its bend range next to the fit.
Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Het blok "Also new in 1.2" eronder blijft staan.

### 3c. Overview: vervang de zin "The free Click Joints (Blender Extensions) and Pro can not be enabled at the same time. Disable the free one first; your settings stay in the .blend file." door
```
Coming from the free Click Joints (Blender Extensions)? Just enable Pro: it turns the free one off for you. Nothing is deleted, and your settings stay in the .blend file.
```

### 3d. Tab Documentation: vervang alles op de tab door
https://superhivemarket.com/products/click-joints-pro/docs. Opmaak zoals nu: de woorden vóór de dubbele punt aan het begin van een alinea vet. Maak van "See the FAQ" een link naar https://superhivemarket.com/products/click-joints-pro/faq als de editor dat toelaat.
```
Getting started

Install: open Blender 4.2 or newer. Drag click_joints_pro-1.2.9.zip from your Superhive download into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip. Got a folder instead of a zip? See the FAQ. Updating from an older Pro? Install the new zip the same way.

Coming from the free version: just enable Pro. It turns the free Click Joints off for you, and the top of the panel says "Free Click Joints was turned off; Pro includes everything in it." Nothing is deleted, and your joints and settings stay in the .blend file.

Open the panel: in the 3D viewport press N and open the Click Joints tab.

Print the Fit test strip first (step 2): in step 2, under Clearance (mm), click Fit test: ball or Fit test: hinge. You get five joints from 0.10 to 0.30 mm clearance, each with its number, in a collection called Fit test. Print them, pick the one that turns smoothly without wobble, and set Clearance (mm) to that number. Then place your joints.

First click, with a rig: select the mesh that has an armature (Armature modifier or armature parent). "Rig found" appears at the top of the panel: click Figure from rig. Elbows and knees become hinges with an end stop; shoulders, hips and neck become ball joints. More bones (ankles too) adds ankles (Blender 5.2 and newer). The list shows each joint with its type and range. A joint that does not fit is skipped, and the list says why.

First click, no rig: put the 3D cursor on a knee (Shift + right click on the skin). In the Figure joints panel, under "Put the 3D cursor on a joint, then:", click Knee. The other presets: Shoulder, Hip, Neck, Elbow, Ankle.

By hand, on any part: 1 Place: select the mesh, set the 3D cursor, click Check mesh (Make watertight or Convert to mm if it asks). 2 Joint: set Clearance (mm), then Place joint for a ball, or under "Or a hinge that bends up to:" click 90°, 115° or 135°. 3 Fit and export: check the fit (after a hinge it says Hinge placed with its bend range), pick a folder, STL or 3MF, and click Export STL (or Export 3MF).

Figure printing checklist
- Figure about 200 mm tall or more, with separate arms and legs.
- Fit test strip printed, Clearance (mm) set to the joint that fit (default 0.2 mm).
- Every joint in the list placed, or skipped with a reason you have read.
- Show bend range on: drag Bend and check that nothing turns red before the pose you want.
- Exported in millimeters, one file per part.

Support
Questions or bugs: github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com. Please mention your Blender version.
```

### 3e. Tab FAQ: vervang alles op de tab door
https://superhivemarket.com/products/click-joints-pro/faq. Vraag vet, antwoord eronder, zoals nu.
```
How do I install it?
Drag click_joints_pro-1.2.9.zip into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip. Then press N in the 3D viewport and open the Click Joints tab.

The install failed or I got a folder instead of a zip. What now?
Safari on a Mac can unzip downloads by itself, and Blender cannot install a folder. Download it again with another browser, such as Chrome or Firefox, and drag the zip into Blender without opening it. Also check your Blender version: click the Blender logo at the top left, then About Blender. Click Joints Pro needs Blender 4.2 or newer and does not install in older versions. Still stuck? Send a message through Superhive with your Blender version and a screenshot of the error.

Can I use the free Click Joints and Pro at the same time?
You do not need to. Just enable Pro: it turns the free Click Joints off for you, and the top of the panel says "Free Click Joints was turned off; Pro includes everything in it." Pro does everything the free version does, plus the hinges. Nothing is deleted, and your settings stay in the .blend file.

Will the joints fit on my printer?
The default clearance of 0.2 mm works on most well tuned printers, but every printer is different. Print the Fit test strip first: in step 2, under Clearance (mm), click Fit test: ball or Fit test: hinge. You get five joints from 0.10 to 0.30 mm. Pick the one that turns smoothly without wobble and set Clearance (mm) to that number.
```

## Waar elke zin vandaan komt
| Zin | Bron | Keuring |
|---|---|---|
| Releaseregels (2b, 3b, 3a) | `platformen/blender/pro-1.2.9.md` deel 2 en 3; regel 2 met de kan van Daan ("so each button sits in the step where you use it"); de regel over de gratis versie staat nu bovenaan, want die raakt de meeste kopers | Daan ja #93 (8/8/8) en #138/#148 (regel #114) |
| Docs-tab (3d) | `platformen/blender/superhive/docs-tab-1.2.9.md`, met de Install-alinea van #258 (slepen, map, FAQ) en K1 van #157 ("(step 2)") | Daan ja #157 (8) en #262 (8,5) |
| Overview-zin (3c) | `docs-tab-1.2.9.md`, kop "Regel op de productpagina" | Daan ja #157 |
| After you buy (2c), Content-tab | `platformen/blender/pro-installeren-slepen-1.2.8.md` plakken 2 en `pro-gumroad-na-kopen-1.2.8.md`, met de "Na 1.2.9"-regels uit die bestanden | Daan ja #226 (8) en #262 |
| FAQ (3e) | `pro-installeren-slepen-1.2.8.md` plakken 3 met de "Na 1.2.9"-wijzigingen (K1 #262); vraag 3 nieuw, woorden uit de Docs-tab | Daan ja #262; vraag 3 nieuw in deze keuring |
| "Free Click Joints was turned off; Pro includes everything in it." | `click_joints/betaald/__init__.py` regel 24, toets (a) in `e2e/test_betaald.py` | e2e 46043092572 groen |
| "in step 2, under Clearance (mm)" | `betaald/testkaart.py` regels 211 tot 216 | Daan #157 deel A |
| Slepen vanaf 4.2; Safari kan zips uitpakken | DERDEN: https://docs.blender.org/manual/en/4.2/editors/preferences/extensions.html en https://support.apple.com/en-gb/guide/safari/sfri40598/mac (nagelezen voor #258) | Daan #262 |

**Winkeltekst verder:** de verkooptekst zelf (kop, alinea's, "What you get") blijft B3, GESLAAGD in de blinde test (`organisatie/blindtest/uitslag/click-joints-pro-tekst-2026-11-24-2218.md`). Deze kaart verandert alleen versie, wat-is-nieuw en uitleg na het kopen. Nergens "print tested", "we printed" of AI.

## Stand
- 27 nov ±20:20 NL (Bram): kaart klaar, controlescript gedraaid op de pagina's van nu (geeft zoals verwacht overal FOUT op de 1.2.9-regels en GOED op "print tested", GEZIEN). Keuring gevraagd aan Daan.
