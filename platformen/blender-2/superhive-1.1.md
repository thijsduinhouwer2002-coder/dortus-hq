# Click Joints Pro 1.1.0 op Superhive: alles klaar voor de hoofdchat (Bram, 19 nov 2026 ±23:30 UTC)

Opdracht hoofdchat 19 nov 23:55 NL: Superhive op 1.1 zetten zodra Thijs vr ochtend de zip kiest. Pagina live sinds 19 nov (Published, GEZIEN 22:35 door de hoofdchat; ik zag hem ook met curl om ±23:15 UTC: nog de tekst van 15 nov, "Hinges that click and stop at 115°", Personal $12, Studio $45, 8 tags). Keuring tekst en beeld 1: Daan (gevraagd).

## 0. Eerst weten (DERDEN, support.superhivemarket.com, gelezen met curl 19 nov ±23:20 UTC)
- **Geen nieuwe keuring na een wijziging:** "Once your product has been accepted for sale, subsequent updates are not monitored" (artikel 37). Tekst, prijs, beelden en bestanden mag je dus gewoon aanpassen en opslaan met **Update**.
- **Nieuwe versie gaat via het tabblad Product Versions**, niet via het bestandsveld: Creator Dashboard, Products, oranje knop **View** bij Click Joints Pro, bovenaan tab **Product Versions**, knop **+Create New Version** (artikel 301). De notities uit dat formulier staan voor kopers op hun bonpagina en voor nieuwe kopers op de productpagina (artikel 336).
- **Pro heeft varianten (Personal en Studio), dan is het veld Variant verplicht** en ziet een nieuwe koper alleen versies die aan een variant hangen (artikel 301). Dus **twee keer** een versie 1.1.0 maken: één voor Personal, één voor Studio, met dezelfde zip (GOK dat het formulier maar één variant per keer toelaat; de tekst zegt "Select which product variant").
- Elk nieuw bestand wordt op malware gescand. Pas als er **Scanned** (of Not fully scanned) staat gaat hij als update naar Blender (artikel 301 en 336). Staat er **Under review**: niet opnieuw uploaden, dan meldt de hoofdchat het aan mij.
- Kopers met Superhive als repository in Blender krijgen 1.1.0 als update met één klik (artikel 336), zolang hun support period loopt. Alle kopers zijn van na 15 nov, dus iedereen.

## 1. De zip
Zelfde als Gumroad (`gumroad-1.1.md` punt 1): `click_joints_pro-1.1.0.zip` uit artefact `click-joints-pro-zip-1.1.0`, uitgave-run 44563401805, sha256 `bcc14122a1b4e599288cc3fe0f6ce3d069bddbec94f042beb362b03b5296a324`. Thijs kiest hem in het Windows-venster (lijst-thijs punt 5). Artefact verloopt zo 22 nov 16:12 UTC.
**Let op:** de Fit test strip (plaatje 20, 20d, 20h) zit **niet** in deze zip; die kwam later op main (commit cc7162d, na de 1.1.0-zip). Dus plaatje 20 niet op de pagina en geen woord over een testkaart tot de zip met die knop er is (1.2).

## 2. Prijs: niets veranderen
Personal **$12**, Studio (up to 5 people) **$45**, tot na de Cyber Sale (besluit 19 nov 14:00). Vinkje "Opt-in to all sitewide sales" staat los hiervan (Sale Campaigns, artikel 300; zie `platformen/blender/superhive/mens-lijst.md` punt 4).

## 3. Welk veld wat krijgt (Edit, panelen openklikken, dan Update)
| Veld in het formulier | Wat erin | Nu (GEZIEN op de pagina) |
|---|---|---|
| Title | `Click Joints Pro` (zo laten, de link blijft dan zeker gelijk) | Click Joints Pro |
| Excerpt | `Rig to printable figure: elbows and knees stop where your rig stops.` | (niet zichtbaar met curl) |
| Description | blok 4 hieronder, in zijn geheel in plaats van de oude tekst | "Hinges that click and stop at 115°" |
| Tags | de 8 van nu laten staan en erbij: `3d printing`, `poseable`, `posable`, `rig to print`, `figure`, `cosplay`, `ball joints`. Geen `print in place` (de delen zijn los, keuring Daan). Laat het formulier er minder toe: in die volgorde tot het vol is. | ball-joint, 3MF, hinge, Joints, action figure, miniatures, STL, articulated figure |
| Category | Modeling laten | Modeling |
| Blender Version | 4.2 tot 5.3 laten (getest op 4.2.23, 5.2.3, 5.3.0, GEZIEN e2e) | 4.2 - 5.3 |
| Render Engine Used | staat nu op Cycles; heeft het formulier "None" of "N/A", dan dat (het is een add-on, rendert niets). Anders laten. | Cycles |
| Images / Gallery | blok 6 hieronder | (oude set van 15 nov) |
| Product files | zie blok 5 | 1.0.1 |
| Support Period | 12 maanden, verlengen 25% laten | zo |

## 4. Beschrijving (plakken, in deze volgorde)
Zelfde als de Gumroad-tekst 1.1, met drie verschillen (onderaan uitgelegd).

**Rig to printable figure: elbows and knees stop where your rig stops.**

Pick your rigged figure, press one button, and Click Joints Pro cuts it into printable parts with a joint at every shoulder, elbow, hip, knee and neck. Elbows and knees get a hinge with an end stop; shoulders, hips and neck get a ball joint. Next to each joint you see how far it bends, in degrees, before you print.

**From rig to a figure that moves.**
Rigged your character already? Then the hard part is done. Figure from rig reads the bones you made, puts a hinge at every elbow and knee and a ball joint at shoulders, hips and neck, and gives each hinge the limit your rig sets, where it sets one. One button, then you check the list.

**Split with anything. Make it move.**
Already split your model into printable parts with another tool? Keep those parts. Open one, put the 3D cursor on the knee or elbow, and Click Joints Pro cuts a hinge or a ball joint right there, with the clearance you set and the range in degrees. Splitting makes it fit on the bed. Click Joints makes it move.

**Why not a ball joint by hand?**
You can. A sphere, a boolean and some offset get you a joint. What you only find out after the print is that the knee bends backwards, the wall next to the socket is 0.4 mm thin, or the ball is stuck. Click Joints shows all three before you print: an end stop on every hinge, the wall and clearance as a number, and the range in degrees.

**What you get**
- Figure from rig. One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints.
- The end stop comes from your rig. If a bone has a Limit Rotation constraint, the hinge stops at that angle (30° to 150°). No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part.
- Every range in one view. A small degree arc at each joint with its number, and a list in the panel: name, type, range and where the range came from (from rig, mirror or preset).
- Honest when it can not. A joint that does not fit is skipped, and the list tells you why and what to try.
- Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
- No rig? Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle, each with its own icon. Place the 3D cursor and click the body part.
- Everything from Pro 1.0: hinge with end stop and pose slider, red where parts hit past the stop, green fit band, spacing checks, ball joints with a fit colour, split into parts, export to STL or 3MF.

**Good to know**
- Works best on figures with separate arms and legs, at about 200 mm tall or more. On a realistic figure at 150 mm the arms are too thin for a hinge; the list says so.
- On AI-made figures where the legs touch (trousers, tunic), hips are skipped with a reason; knees still work.
- Best in Blender 4.5 and newer. In Blender 4.2 it works, but some joints may need to be placed by hand (the list tells you which).
- Tested in Blender 4.2, 5.2 and 5.3 on a MakeHuman figure, a Rigify metarig and three AI-made figures. Not print tested by us yet: print a test joint first, every printer is different.
- Clearance 0.2 mm by default.
- The free Click Joints (Blender Extensions) and Pro can not be enabled at the same time. Disable the free one first; your settings stay in the .blend file.
- Already bought Pro? 1.1 is a free update: download it from your Orders page on Superhive, or update it inside Blender if you added Superhive as a repository.
- Includes 12 months of updates. Every version you download is yours to keep. After a year you can extend updates for 25% of the price; it is never required.
- Support: the "Contact the creator" link on this page (your Superhive inbox), https://github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com

**Versions**
Personal is for one person. Studio is for a team of up to 5 people. Same download.

**Update log**
- 1.1.0 (20 Nov 2026): Figure from rig, end stop from your rig, degree arc and joint list, six body-part presets.
- 1.0.1 (Nov 2026): first release: hinge with end stop, pose slider, red past the stop, green fit band.

### Wat anders is dan `gumroad-1.1.md`
1. "download it again from your Gumroad library" werd "download it from your Orders page on Superhive, or update it inside Blender if you added Superhive as a repository" (opdracht hoofdchat; Orders-pagina en repository: artikelen 254 en 336).
2. Blok "Versions" zonder Supporter (die bestaat op Superhive niet) en zonder prijzen.
3. Erbij: de regel over gratis en Pro tegelijk (staat nu ook op de pagina, en de weigermelding zit nog in de toetsen), de regel over 12 maanden updates (voorstel Chris, `berichten/hoofdchat.md` regel 152, zonder "$3 today" want de prijs verandert na de sale), Superhive-inbox bij support, en een **Update log** (Superhive raadt dat aan in de beschrijving, artikel 37).

## 5. De versie (tab Product Versions, twee keer: Personal en Studio)
| Veld | Wat |
|---|---|
| Variant | eerst `Personal`, daarna nog een keer `Studio (up to 5 people)` |
| Version Name | `1.1.0` |
| Release Date | vandaag (vr 20 nov 2026) |
| Changelog / Notes | het blok hieronder |
| Version Files | `click_joints_pro-1.1.0.zip` (bij de tweede keer uit de lijst kiezen, niet opnieuw uploaden: een tweede gelijke upload kan een tweede scan geven) |

```
Click Joints Pro 1.1.0 "Rig to Figure"
- New: Figure from rig. One button turns a rigged figure into printable parts: hinges with an end stop at elbows and knees, ball joints at shoulders, hips and neck.
- New: the end stop comes from Limit Rotation in your rig (30° to 150°); a side without a limit takes the other side.
- New: a degree arc and number at every joint, and a joint list with where each range came from.
- New: six body-part presets with icons for figures without a rig.
- New: recognises Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz bone names.
- Fixed: a hinge on a one-piece figure no longer leaves the rest of the limb behind as a loose piece.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
(Woord voor woord gelijk aan de Gumroad-notes; er stond al niets over Gumroad in.)

Daarna in het paneel met bestanden van het product kijken: staat daar nog `click_joints_pro-1.0.1.zip` als losse download, dan vervangen door 1.1.0, zodat een nieuwe koper niet de oude krijgt (GOK hoe Superhive de eerste upload toont; 1.0.1 niet als versie wissen, kopers mogen terug naar een oude versie, artikel 329).
Klaar als: bij beide versies **Scanned** staat, en de productpagina (uitgelogd, curl of browser) de nieuwe kop en "1.1.0" toont.
Let op: de datum bij 1.1.0 in de update log moet de echte livedag zijn. Gaat hij later live dan vr 20 nov, pas die datum aan (en de Release Date in blok 5).

Een mail aan bestaande kopers (Creator emails, artikel 336) gaat naar buiten: alleen na keuring van die tekst door een ander, en de hoofdchat verstuurt. Er is nog geen tekst voor; niet nodig voor de sale.

## 6. Beelden (2:1, geen Blender-logo, minstens 5: artikelen 41 en 253)
De zes plaatjes van de Gumroad-release zijn 16:9 (1920 x 1080, GEZIEN) en plaatje 1 daar heeft het Blender-logo linksboven, dus die passen niet op Superhive. Daarom de 2:1-set uit `platformen/blender/superhive/beelden/` (Daan ja op 4cffa33), met één nieuw eerste beeld:

| # | Bestand | Wat |
|---|---|---|
| 1 (uitgelicht) | `1-figuur-uit-rig-1.1.png` **nieuw** | uitsnede 2:1 van Gumroad-plaatje 1 (`1-figuur-uit-rig.png`, Daan ja): menubalk met logo en statusbalk eraf, 1920 x 960. Toont de lijst "9 joints · 2 rig · 2 mirror · 5 preset", waar de tekst naar verwijst. Zelf bekeken (GEZIEN): figuur, alle getallen en de lijst heel in beeld. |
| 2 | `2-knie-boog-0-115.png` | knie met gradenboog 0° tot 115° |
| 3 | `3-rood-voorbij-de-stop.png` | rood, "+3° past limit" |
| 4 | `4-groene-passing.png` | groene passingband |
| 5 | `5-kogel-rood-gratis-deel.png` | kogel rood voorbij 20° |
| 6 | `6-figuur-rig-scharnieren.png` | hele figuur na één knop (achteraan: blokpop met oud paneel, zwakker dan beeld 1; mag ook weg, vijf is genoeg) |

Niet gebruiken: `2-poster-3.png` (zegt "click" en "Pro on Superhive", opdracht hoofdchat) en het oude `1-figuur-van-rig.png` (oud paneel en de zin "in one click"). Plaatje 20, 20d en 20h pas met de zip die de Fit test strip heeft. De demofilm (release `click-joints-pro-film-v1`) mag als preview blijven als hij er nu op staat: hij toont de knie, niets wat 1.1 tegenspreekt.

Kan-punten van Daan (keuring 19 nov ±23:30 UTC) verwerkt 20 nov ±00:15 UTC door Bram: beeld 5 en 6 gewisseld, datumregel bij de update log, support noemt nu de knop "Contact the creator" (DERDEN: https://support.superhivemarket.com/article/20-how-to-get-product-support, gelezen met curl: het bericht komt in de inbox van de maker).

## Na het zetten (hoofdchat)
Regel op het bord, en in `platformen/blender/superhive-pagina.md` onderaan: datum, wat er nu op staat (GEZIEN). Mij een bericht als iets in het formulier anders heet dan hierboven, dan pas ik dit bestand aan.
