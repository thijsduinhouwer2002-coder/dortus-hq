# Volgende print-add-on: drie kandidaten (Olaf, onderzoeker, 8 nov 2026)

Status: eerste versie, nog niet nagekeken door een controleur. Alles GEZIEN is zelf gemeten op 8 nov 2026 met curl. Ruwe data en scripts in `platformen/blender-2/data/`.

## Samenvatting en advies
- Op Superhive halen in de print-hoek alleen **splitsers met verbinders** aantoonbaar 100+ bij makers zonder eigen publiek (CatPin 400+, Split-3DPrint 400+, Cleave 100+). In elke andere print-niche is er geen enkele nieuwkomer met 100+ (GEZIEN).
- **Nieuw feit:** sinds ±26 dagen zet één maker, Hanru Croucamp, 27 kleine print-add-ons van $1 tot $39 op Superhive (holmaken met afvoergaten, wanddikte, overhang, lithofaan, sokkels, sleutelhangers, tolerantietest, splitsen op bedmaat, plus een bundel van $139). Geen van de 27 heeft al een teller (dus minder dan 10 verkopen elk). Elke kleine print-niche heeft nu dus een goedkope concurrent (GEZIEN).
- Kandidaat 1 (best): **Bed Split**, model splitsen op de maat van jouw printbed met verbinders, op het printerprofiel van Click Joints. Score 25 van 35. Bewezen geld, maar druk.
- Kandidaat 2: **Print Heatmap**, wanddikte en overhang als kleurenkaart op het model. Score 23. Mooi en klein, betaalbewijs dun.
- Kandidaat 3: **Relief Plaque**, 3D-model naar bas-reliëf (plaquette, munt, medaille). Score 22. Eén zwakke betaalde concurrent, maar vraag klein.
- **Eerlijk advies:** alleen kandidaat 1 heeft bewijs dat nieuwkomers verkopen, en ook daar halen de splitsers die na CatPin kwamen nog geen 100+ (SnapSplit 30+ in 8 mnd, CutLink 30+, Split It 10+). Voor 2 en 3 is het bewijs te dun om er nu op te bouwen. Advies: kandidaat 1 als product 2, alleen als Hans de overlap met Click Joints acceptabel vindt; anders eerst over 4 weken de tellers van Hanru opnieuw meten (dat is de proef of kleine print-hulpen zonder publiek verkopen).

## De print-hoek in kaart
Bron per regel: https://superhivemarket.com/products/<slug> (teller, prijs, leeftijd, maker, aantal reviews en gemiddelde, GEZIEN 8 nov) en https://extensions.blender.org/add-ons/<slug>/ (downloads, GEZIEN 8 nov). Data: `data/superhive-print-2026-11-08.jsonl` (934 producten uit 48 zoekwoorden, gefilterd op printwoorden), `data/extensions-print-2026-11-08.jsonl`. "Publiek" = maker heeft een ander product met 100+ (GEZIEN in onze data of in sectie 19 van Bram).

### Betaald op Superhive
| Klus | Add-on (slug) | Maker | Prijs | Teller | Leeftijd | Reviews | Publiek? |
|---|---|---|---|---|---|---|---|
| Splitsen + verbinders | dovetail-key | Milad Kambari | $18 | 800+ | 4 mnd | 13, gem. 4 | ja (Smart Remesh 2.500+) |
| Splitsen + verbinders | catpin | Alex Sokol | $24 | 400+ | 3 mnd | 4, gem. 5 | nee |
| Splitsen + verbinders | split-3dprint | AUER.Blender | $22 | 400+ | 4 mnd | 3, gem. 5 | nee |
| Splitsen + gewrichten | cleave | V4SS3UR | $23 | 100+ | 2 mnd | 3, gem. 5 | nee |
| Splitsen + verbinders | snapsplit | Christoph Medicus | $20 | 30+ | 8 mnd | 0 | nee |
| Splitsen + verbinders | cutlink-studio-... | MOHAN M | $2 | 30+ | 2 mnd | 0 | nee |
| Splitsen + verbinders | split-it | Pamir Bal | $8,40 | 10+ | 26 dagen | 0 | nee |
| Splitsen, tandwielen | oryx-cad | Sebastien Prefol | $14,99 | 10+ | 4 mnd | 0 | nee |
| Splitsen op bedmaat | bed-fit-splitter | Hanru Croucamp | $19 | geen | 26 dagen | 0 | nee |
| Splitsen | printsplitter, regosplit, print-ready-modelling-kit, figurecut | diverse | $6 tot $24 | geen | 7 dagen tot 8 mnd | 0 | nee |
| Gewrichten | jointlab- | Jointlab | $65 | 20+ | 4 mnd | 3, gem. 4 | nee |
| Puzzel/verbinders | puzzleurprint | Björn Eckhardt | $15 | 100+ | 5 jaar | 2, gem. 5 | nee |
| Reliëf uit foto/AI-diepte (ook lithofaan) | truedepth | Lewis Martin | $25 | 6.900+ | ±2 jaar | 57, gem. 5 | ja |
| Reliëf uit foto | ai-depth-modeller | 3d illusions | $24,99 | 600+ | ±2 jaar | 10, gem. 5 | ja (Turbo Tools 2.400+) |
| Bas-reliëf uit model of beeld | bildeform | Jhon Cabezas | $19,60 | 500+ | ±2 jaar | 4, gem. 5 | nee |
| Bas-reliëf uit beeld | bas-relief-sculpt-add-on- | Guillaume Bissieres | $1 (ook gratis) | 300+ | ruim 1 jaar | 1, gem. 5 | nee |
| Lithofaan | lithophane-maker | Hanru Croucamp | $12 | geen | 18 dagen | 0 | nee |
| Mesh-controle (overlay) | mesh-check-gpu-edition | Jérémy Legigan | $3,50 | 200+ | ruim 3 jaar | 7, gem. 5 | nee |
| Mesh-controle | check-mesh | Kewl Sheet | $7,77 | 100+ | 10 mnd | 0 | onbekend |
| Mesh-controle | analyse-mesh | Mark Kingsnorth | $5 | 100+ | ±2 jaar | 8, gem. 5 | ja (Plating Generator 5.100+) |
| Printcontrole | 3d-print--checker ("3D Print Toolbox 4") | Kohdy Mcintyre | $9 | 70+ | ±2 jaar, tot Blender 4.3 | 0 | nee |
| Wanddikte | wall-thickness-checker | Hanru Croucamp | $12 | geen | 18 dagen | 0 | nee |
| Overhang + oriëntatie | overhang-finder-auto-orient | Hanru Croucamp | $15 | geen | 19 dagen | 0 | nee |
| Steunen | printsupportpro | DUCKLABO | $30 | 70+ | ±2 jaar | 0 | nee |
| Holmaken | hollow-object-creator | Arthur Kulyk | $10 | geen | 4 mnd | 0 | nee |
| Holmaken + afvoergaten | resin-hollow-drain-holes | Hanru Croucamp | $12 | geen | 14 dagen | 0 | nee |
| Mallen | mouldcast | Ram | $27 | 60+ | 8 mnd | 0 | nee |
| Export | ultimate-stl-export | James Guard | $10 | 100+ | ruim 2 jaar | 4, gem. 5 | nee |
| 3MF | import-export-3d-manufacturing-file | han yue | $8 | 70+ | ruim 1 jaar | 0 | nee |
| Meerkleuren-3MF | 3mf-magic-solver, chroma-3mf..., ams-splitter, color-layer-splitter | Alessia, Ambiens, J. Hidalgo, Hanru | $12 tot $80 | geen | 19 uur tot 8 mnd | 0 | nee |
| Sokkels miniaturen | mini-base-maker | Hanru Croucamp | $12 | geen | 19 uur | 0 | nee |
| Sleutelhanger/naam | keychain-name-tag-maker | Hanru Croucamp | $9 | geen | 18 dagen | 0 | nee |
| Tekst in reliëf | emboss-deboss-text-tool | Hanru Croucamp | $9 | geen | 18 dagen | 0 | nee |
| Tolerantietest | fit-tolerance-test-generator | Hanru Croucamp | $7 | geen | 14 dagen | 0 | nee |
| Pose naar print | pose-to-print | Arminas Attas | $18 | geen | 6 dagen | 0 | nee |
| AI-mesh naar print | 3dquads-print-ready, printprep, print-fix, ai-mesh-fixer | diverse | $14 tot $20 | 10+ of geen | 26 dagen tot ruim 1 jaar | 0 | nee |
| Alles-in-één | 3d-print-suite-bundle | Hanru Croucamp | $139 | geen | 1 dag | 0 | nee |

Hanru Croucamp heeft in onze data 27 print-producten, allemaal 19 uur tot 26 dagen oud, geen teller (GEZIEN). Eslam Mustafa (LayerMechanic) 5 producten van $12 tot $25, ±1 maand, geen teller. Alessia 9 producten, één met teller 10 (GEZIEN).

### Gratis op extensions.blender.org (downloads, GEZIEN 8 nov)
| Add-on | Downloads | Sinds | Score |
|---|---|---|---|
| 3D Print Toolbox | 680.642 | mei 2024 (ingebouwd tot 4.1) | 5,0 uit 54 |
| 3MF Import/Export | 118.733 | | 5,0 uit 88 |
| STL format (legacy) | 72.201 | mei 2024 | |
| Export Paper Model | 59.978 | mei 2024 | |
| Easy-Print (splitsen + verbinders) | 7.005 | 29 jul 2026 | 4,0 uit 3 |
| MoldForge (mallen) | 6.663 | 17 jun 2026 | 5,0 uit 5 |
| EasySlice Print (splitsen) | 5.841 | | 1,0 uit 21 |
| Bas Relief (uit beeld) | 5.129 | 16 jun 2026 | 5,0 uit 1 |
| NFC Card and Keychain Generator | 4.307 | | |
| Photo Relief (reliëf, lithofaan, stempel) | 3.085 | | 5,0 |
| Relief Rebake | 3.018 | | 5,0 |
| Keychain Builder | 2.696 | 26 apr 2026 | 5,0 |
| MasterMoldSizer | 1.745 | | 5,0 |
| SnapSplit (gratis versie) | 1.268 | | |
| MiniSlicer (resin) | 811 | 10 jul 2026 | |
| Print Prep | 717 | | |

**3D Print Toolbox (https://extensions.blender.org/add-ons/print3d-toolbox/):** controleert solid, doorsnijdingen, gedegenereerde en vervormde vlakken, dikte, scherpe randen en overhang (resultaat: geselecteerde vlakken), maakt manifold, holt uit (eigen offset, inmiddels ook als geometry-nodes-modifier), lijnt uit, schaalt naar volume of maat, exporteert. 31 issues, allemaal gesloten (GEZIEN, https://projects.blender.org/extensions/print3d_toolbox/issues). Klachten: holmaken gaf fouten in Blender 4.4 en 5.2 (#16, #34), "Make Manifold" haalt soms grote vlakken weg (#12), valse meldingen "zero faces" (#21, #33), export vraagt elke keer een map (#14). Wens: geometry-nodes-versies van de edit-tools (#25, maker: hollow en bisect bestaan al als GN). Niet aanwezig: kleurenkaart van dikte of overhang, afvoergaten, splitsen, verbinders, printerprofiel, 3MF.

### Vraag (forums)
- Holmaken met vaste wanddikte voor resin, buitenkant onaangetast: "Solidify is unsuitable for complex models", de vrager loste het op in de slicer (CHITUBOX) (GEZIEN, https://blenderartists.org/t/1653755, 235 views, sep 2026). Niemand wees op de Toolbox.
- Alles-in-één print-add-on (Handprint Tools, $15 op Gumroad): 2.697 views (GEZIEN, https://blenderartists.org/t/1565136).
- Eigen slicer in Blender: 4.973 views, 33 posts (GEZIEN, https://blenderartists.org/t/1590546), maar dat is te groot.
- Automatisch snijden en lijmloze verbindingen: https://blenderartists.org/t/1635593 (GEZIEN, 5 posts).
- Dovetail Key-kopers: "suffers the pitfalls of many vibe coded tools, interaction model feels buggy", "cutting ... gives mixed results", wens "select a loop and cut based on that" (GEZIEN, https://superhivemarket.com/products/dovetail-key/ratings?page=2).
- Bildeform-kopers: "stable, effortless, fast", "printable, mountable bas relief versions of 3D models" (GEZIEN, https://superhivemarket.com/products/bildeform/ratings).

## Kandidaat 1: Bed Split (score 25)
**Wat:** klik op een model dat te groot is voor je printer en krijg delen die op jouw printbed passen, met pennen of zwaluwstaarten met de speling uit het gedeelde printerprofiel, en een kleurige viewport-weergave van het printbed en elk deel.

- **Wie betaalt:** makers van grote prints (cosplay, beelden, props, terrein), eenmalig $15 tot $19 (GOK, onder CatPin $24 en Split-3DPrint $22).
- **Marktbewijs:** CatPin $24 400+ in 3 mnd, Split-3DPrint $22 400+ in 4 mnd, Cleave $23 100+ in 2 mnd, makers zonder publiek (GEZIEN, superhivemarket.com/products/catpin, /split-3dprint, /cleave). Gratis Easy-Print 7.005 en EasySlice 5.841 downloads in ±3 tot 4 mnd (GEZIEN). Netto per maand CatPin ±$2.000 (GOK op GEZIEN: 400 x ($24 x 0,65 min $0,49) / 3).
- **Top 3 concurrenten:**
  - Dovetail Key: $18, 800+, 4 mnd, gem. 4 uit 13. Zwak: "vibe coded", haperende voorbeeldweergave, wisselende snedes (GEZIEN).
  - CatPin: $24, 400+, 3 mnd, gem. 5 uit 4. Zwak: duurder; niet zelf getest.
  - Split-3DPrint: $22, 400+, 4 mnd, gem. 5 uit 3. Zwak: niet zelf getest.
  - Plus Cleave ($23, 100+, met gewrichten) en ±10 nieuwere splitsers zonder teller, waaronder Bed Fit Splitter van Hanru ($19).
- **Waarom wij beter kunnen zijn:** het printerprofiel van Click Joints kent al bedmaat en speling, dus splitsen "op mijn printer" is één klik; snijlijn sleepbaar in de viewport met live voorbeeld (de klacht bij Dovetail); zelfde passingkleuren als Click Joints; bundel met Click Joints. Smaller en netter dan Cleave (GOK).
- **Bouwtijd:** ±2 weken (GOK): booleans en verbinders bestaan al deels in Click Joints, nieuw is de snijlijn kiezen en de bedmaat.
- **Grootste risico:** te laat. De drie winnaars kwamen 2 tot 4 mnd geleden; van de splitsers daarna haalt nog geen enkele 100+ (SnapSplit 30+ in 8 mnd, CutLink 30+ in 2 mnd, Split It 10+ in 26 dagen, GEZIEN). En overlap met Click Joints en Cleave: kopers zien het misschien als hetzelfde. Bram moet zeggen of dit botst.

## Kandidaat 2: Print Heatmap (score 23)
**Wat:** kleurt het model live in de viewport op wanddikte en overhang, met de grenzen uit het printerprofiel (mondstuk, kleinste wand, overhanghoek), en springt met één klik naar de slechtste plek.

- **Wie betaalt:** iedereen die een model wil printen, vooral van AI-meshes en sculpts; eenmalig $9 tot $12 (GOK).
- **Marktbewijs:** dun. Mesh Check GPU $3,50 200+ in ruim 3 jaar, Check Mesh $7,77 100+ in 10 mnd, Analyse Mesh $5 100+ in ±2 jaar (maker met publiek), 3D Print Toolbox 4 $9 70+ in ±2 jaar (GEZIEN). Gratis Toolbox heeft 680.642 downloads: de vraag naar controleren is groot, de bereidheid te betalen klein (GOK op GEZIEN).
- **Top 3 concurrenten:**
  - 3D Print Toolbox (gratis, 680.642, gem. 5 uit 54, bijgewerkt 2 weken geleden). Zwak: geeft een selectie, geen kleurenkaart; geen printerprofiel.
  - Wall Thickness Checker + Overhang Finder van Hanru ($12 en $15, 18 en 19 dagen, geen teller). Zwak: onbekend, nog niet verkocht.
  - Mesh Check GPU ($3,50, 200+, gem. 5 uit 7). Zwak: alleen topologie (n-gons, niet-manifold), geen dikte.
- **Waarom wij beter kunnen zijn:** kleurenkaart in de viewport is mooi te tonen (voor/na op de winkelpagina), dezelfde passingkleuren en hetzelfde profiel als Click Joints; kan gratis als lokker op extensions.blender.org naast de betaalde versie.
- **Bouwtijd:** ±1 tot 1,5 week (GOK): dikte met raycast in numpy/BVHTree, overhang uit normalen, kleur via vertex-kleuren of een GPU-overlay.
- **Grootste risico:** betaalbewijs te dun en een gratis reus. Waarschijnlijk 10 tot 50 verkopen in 6 mnd (GOK).

## Kandidaat 3: Relief Plaque (score 22)
**Wat:** maakt van een 3D-model (personage, logo, gebouw) een printbaar bas-reliëf in mm, met rand, sokkel of munt-vorm en tekst, en exporteert het waterdicht.

- **Wie betaalt:** makers van muurplaatjes, medailles, munten, prijzen, sieraden en CNC; eenmalig $15 tot $19 (GOK).
- **Marktbewijs:** Bildeform $19,60 500+ in ±2 jaar, maker zonder publiek (beste ander product Texturology 30+), gem. 5 uit 4 (GEZIEN, /products/bildeform). Bas-Relief Sculpt $1 300+ in ruim 1 jaar (ook gratis, 5.129 downloads) (GEZIEN). Dat is ±20 per maand voor de enige betaalde, geen nieuwkomer in de laatste maanden.
- **Top 3 concurrenten:**
  - Bildeform: $19,60, 500+, ±2 jaar, gem. 5 uit 4, Blender 5.1 tot 5.2. Zwak: niet gevonden, kopers zijn tevreden.
  - TrueDepth: $25, 6.900+, ±2 jaar, gem. 5 uit 57. Doet reliëf en lithofaan uit foto's met mm-maat en export voor Bambu en Prusa, niet uit een 3D-model (GEZIEN, /products/truedepth). Sterke nummer één naast ons.
  - Bas Relief (gratis, 5.129) en Bas-Relief Sculpt ($1, 300+), uit beelden.
- **Waarom wij beter kunnen zijn:** een plaquette-kant (rand, sokkel, tekst, munt) bovenop het reliëf, met printerprofiel en waterdichte export; erg mooi te tonen (licht over het reliëf).
- **Bouwtijd:** ±2 weken (GOK): diepte renderen vanuit een camera, hoogtes samendrukken (Poisson met numpy.fft, geen scipy), mesh maken.
- **Grootste risico:** vraag klein en Bildeform is goed; TrueDepth kan uit-model-naar-reliëf zo toevoegen. Past minder bij Click Joints (geen passing).

## Scores (1 tot 5, hoger is beter)
| | Vraag | Betaal | Nieuwkomer verkoopt | Concurrentie | Bouwtijd | Opvallen | Past bij Click Joints | Totaal |
|---|---|---|---|---|---|---|---|---|
| 1 Bed Split | 4 | 4 | 4 | 1 | 3 | 4 | 5 | **25** |
| 2 Print Heatmap | 3 | 2 | 2 | 2 | 4 | 5 | 5 | 23 |
| 3 Relief Plaque | 3 | 3 | 3 | 3 | 3 | 5 | 2 | 22 |

## Afgeschoten en waarom
- **Reliëf en lithofaan uit foto:** sterke nummer één TrueDepth ($25, 6.900+, gem. 5 uit 57, doet nu ook lithofaan met mm en slicer-export) (GEZIEN). Harde regel: overslaan.
- **Mallen:** gratis MoldForge (6.663 downloads in 5 mnd, gem. 5, gisteren bijgewerkt, drie soorten mallen, gietvolume) is sterk; betaald MouldCast $27 60+ in 8 mnd (GEZIEN).
- **Holmaken met afvoergaten (resin):** echte wens (BlenderArtists 1653755), maar Hollow Object Creator $10 verkocht in 4 mnd minder dan 10, Hanru $12 nog geen teller, en de gratis Toolbox holt al uit (GEZIEN). Afvoergaten alleen is te klein; kan wel als functie in kandidaat 2.
- **Meerkleuren-3MF (Bambu AMS):** gratis 3MF Import/Export 118.733 downloads, maar vier betaalde kleurentools ($12 tot $80) hebben geen teller, ook die van 8 mnd (GEZIEN). Geen betaalbewijs.
- **Sokkels voor miniaturen, sleutelhangers, naamplaatjes, koekvormen, Gridfinity, tolerantietest:** geen betaald product met teller; Hanru zette ze er in de laatste 26 dagen allemaal op voor $7 tot $14, gratis Keychain Builder 2.696 en NFC Keychain 4.307 downloads (GEZIEN). Tolerantietest hoort al in de gedeelde basis van Click Joints.
- **Steunen en oriëntatie:** slicers doen dit gratis en beter; Print Support Pro $30 70+ in 2 jaar (GEZIEN).
- **AI-model naar printklaar:** al afgeschoten door Bram (sectie 5), nu nog drukker (Print Fix, AI Mesh Fixer van Hanru).
- **Gewrichten:** is Click Joints.

## Wat dit oordeel kan veranderen
- Over 4 weken de tellers van Hanru opnieuw meten (`data/superhive-print-zoek-script.py`, verwijder eerst het jsonl). Halen zijn $9 tot $15 print-hulpen 10+ tot 50+, dan is er wél geld in kleine print-klussen en worden kandidaat 2 en een sokkel- of holmaak-tool sterker. Blijven ze op 0, dan is splitsen de enige print-klus die verkoopt.
- Een eigen test van CatPin en Split-3DPrint (functies, zwakke plekken) voor kandidaat 1; niet gedaan.

## Beperkingen van deze meting
- Zoeken op Superhive geeft per zoekwoord maximaal 2 pagina's (48 producten), gesorteerd op verkoop; dus niet alle print-add-ons met 0 verkopen staan erin.
- De omschrijving kon het script niet lezen (Superhive zet een algemene tekst in het meta-veld); functies van concurrenten komen uit losse pagina's of de titel.
- Leeftijd is de "Published"-tekst van Superhive ("4 months ago").
