# Kopersreis Click Joints Pro als mailontvanger met gratis code (issue #404)

Iris, za 28 nov 2026 avond NL. Nagespeeld: wat een ontvanger van mail 5, 7 of 8 (`bundel-2026-11-29-codes.md`) ziet van de Gumroad-pagina tot het eerste kogelgewricht op een eigen figuur en een STL. Scripts naast dit bestand: `kopersreis_pro_iris.py` (hele reis, achtergrond), `kopersreis_pro_huid_iris.py` (Shift + rechtsklik in een echte 3D-viewport onder xvfb), `kopersreis_pro_as_iris.py` (cursor op de as). De code zelf niet gebruikt.

**Uitslag in één regel:** installeren 0 fouten in 4 van 4 (zip 1.2.8 live en 1.2.9, Blender 4.2.23 en 5.3.0, GEZIEN); eerste kogel en STL lukken, maar alleen met de cursor midden in de arm. 3 drempels als issue bij Bram: **#410** (groot), #411, #412 (klein).

## Wat getest is
| | |
|---|---|
| Gumroad-pagina | https://duinhouwer8.gumroad.com/l/click-joints-pro met curl: 200, price_cents 1900, Personal, Supporter (+$5), Studio (+$40), 1 ZIP van 176.000 bytes per versie (GEZIEN) |
| Zip die nu live staat | 1.2.8 opnieuw gebouwd uit de bron van e2e 45526260663 (95a72a4) met `maak_zip.sh betaald`: 176.000 bytes, precies wat Gumroad toont (GEZIEN). Het artefact zelf staat niet meer in die run |
| Zip na de plak van ma 30 nov | 1.2.9 uit e2e 46120199131, artefact 4.2.23, sha256 `92506b0e...` (GEZIEN); de plakkaart noemt `ebafe214...`, dat is vermoedelijk een ander been van de matrix (GOK) |
| Blender | 4.2.23 LTS en 5.3.0, schone gebruikersmap per run |
| Eigen figuur | gesloten figuur van 238 x 98 x 238 mm (lijf, hoofd, armen 36 mm dik, benen 42 mm), als STL in mm, zonder rig; daarna dezelfde met een eenvoudige rig met Mixamo-namen |
| Gevolgde tekst | mail 5 (sjabloon Pro) en de Gumroad-tekst: "After you buy", "No rig? Place the 3D cursor and click the body part", "Print the Fit test strip first" |

## Per stap (cijfer van 10 voor een nieuwe ontvanger, GOK; uitslag GEZIEN)
| # | Stap | Cijfer | Uitslag |
|---|---|---|---|
| 1 | Gumroad-pagina openen | 8 | 200; haak, prijs, sale, versie 1.2.8 en "After you buy" staan er. Links: extensions.blender.org, GitHub-issues, mail. Geen handleiding voor Pro gelinkt (dortus.com/click-joints/ bestaat, 200) |
| 2 | Installeren (Install from Disk) | 9 | FINISHED, tab "Click Joints", paneel "Figure joints", 4 van 4. "After you buy" noemt slepen nog niet: dat plakbestand ligt al klaar (#258), geen nieuwe drempel |
| 3 | STL in mm importeren in een nieuwe scene | 6 | paneel: "Mesh is 2.38e+05 mm in size" plus "Expected 5 to 500 mm: is the unit right?" en de knop Convert to mm eronder. Getal onleesbaar: **#412** |
| 4 | Convert to mm | 9 | 238 mm, scene in mm, alles daarna klopt |
| 5 | Fit test: ball, exporteren | 9 | vijf paren 0,10 tot 0,30, "Print all five. Use the clearance of the one that turns without wobble."; 10 STL, A 44,5 mm, B 29,5 mm (teruggelezen). Zonder opslaan naar de tijdelijke map, maar de regel "Saves to a temporary folder" staat vlak boven de knop en de melding noemt de map: beter dan bij Click Cuts (#387) |
| 6 | Eerste kogel: Shift + rechtsklik op de huid van de schouder, Shoulder | **3** | "Too thin here for a ball joint. Try a thicker spot." op een arm van 36 mm, in 1.2.8 en 1.2.9, 4.2.23 en 5.3.0. Heup zelfde. Knie en elleboog op dezelfde manier wel goed ("Cursor on the surface: limb axis from the mesh and centred in the limb"). **#410** |
| 7 | Shoulder met de cursor midden in de arm | 9 | "Joint placed. Good fit.", twee delen groen, 4 van 4 |
| 8 | Knee met de cursor precies op de as (Cursor to Selected) | 4 | "Put the 3D cursor inside the mesh to place a hinge"; 0,3 mm ernaast wel goed. **#411** |
| 9 | Export STL na opslaan | 9 | `click_joints/` naast de .blend, my_figure_A 81 mm en my_figure_B 238 mm teruggelezen |
| 10 | Figure from rig (Mixamo-namen) | 7 | 5.3.0: 4 gewrichten, 4.2.23: 3; de rest overgeslagen met een reden per gewricht ("no room on this 35 mm bone ... place it by hand"). Eerlijk, zoals de tekst belooft; mijn figuur is grof. Export 4 en 5 STL |
| 11 | Knee op de huid in 4.2.23 | 6 | "The cut gave no watertight parts" op 1.2.8; de Gumroad-tekst zegt al dat in 4.2 sommige gewrichten met de hand moeten. Geen nieuwe drempel |

## Wat ik niet kon zien
- De Content-tab na aankoop en of de code de prijs naar $0 zet: achter inloggen. Voorwaarde V1 (hoofdchat opent de link één keer) blijft.
- Een echte figuur van een maker (ZBrush, met kleren). Mijn figuur is van bollen en cilinders; drempel #411 hoort juist bij zulke strakke ledematen.

## Belangrijkste voor de outreach
Een ontvanger zonder rig die de schouder eerst probeert, krijgt nu "too thin". Tot #410 dicht is, helpt één regel in "After you buy" of in de mail (bijvoorbeeld "For a shoulder or hip, put the 3D cursor inside the arm or leg, not on the surface"): beslissing voor Bram en de Verspreider.
