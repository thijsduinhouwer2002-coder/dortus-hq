# Keuring: Blender 5.3 Splat Tools (was cijfer 7)

Keurder: afschieter 1, 17 nov 2026. Alles met curl gelezen op 17 nov 2026, tenzij anders vermeld. GEZIEN = zelf op de bron gelezen. GOK = mijn inschatting.

## 1. Wat kan Blender 5.3 zelf, en wat komt er

GEZIEN, https://developer.blender.org/docs/release_notes/5.3/rendering/ :
- "Blender can now import them from PLY and SPZ files, store them in point clouds, process them with Geometry Nodes, and render them with all render engines."
- "Import from PLY and SPZ files is supported. There is currently no export support."
- "Apply Transform on a Gaussian splat does not work correctly as it does not yet handle the new scale, rotation and spherical harmonics attributes."
- "Performance is not ideal." Ook: "rudimentary support for making the splat relightable" door de Emission-node te vervangen door een Diffuse BSDF. Relight zit dus al een beetje in Blender zelf.
- glTF- en USD-import van splats staat op https://developer.blender.org/docs/release_notes/5.3/pipeline_io/ .

Bewerken kan al deels zonder add-on. GEZIEN, https://developer.blender.org/docs/release_notes/4.5/modeling/ : point cloud edit mode met "transform, the selection overlay, and the "Set Attribute" operator". Plus Geometry Nodes (splats zijn gewone point clouds). GOK: grof bijsnijden met een Delete Geometry-node of selecteren in edit mode kan dus al, alleen niet handig.

Wat Blender zelf gepland heeft (dit is wet 4):
- GEZIEN, ontwerptaak #159470 "Integration of gaussian splats for IO and rendering" van Sergey (modulebaas), bijgewerkt 11 nov 2026, https://projects.blender.org/blender/blender/issues/159470 . Onder "Improvement (planned for later development)": "Implement gsplat PLY exporter", "Implement gsplat SPZ exporter", USD "Export support", glTF export, en onder "Editing tools": "Point selection / isolation ... split single point cloud into multiple ones, based on user selection" en "Better integration with rotation/scaling operations". Dat is bijna precies ons productlijstje.
- GEZIEN, PR #165845 "WIP: glTF: Manage KHR_gaussian_splats at export", 29 okt 2026, Julien Duroure (glTF-onderhouder): https://projects.blender.org/blender/blender/pulls/165845 . Werk aan export is al begonnen.
- GEZIEN, PR #164258 "Geometry: Transform gaussian splat attributes" (lost Apply Transform op), 23 sep 2026. Staat stil: Sergey wees hem af op het AI-beleid ("I am a bit hesitant here"), de maker stopte op 9 okt. Dus de fix bestaat al als voorbeeld, maar is niet binnen.
- GEZIEN, 5.4 alpha-notes https://developer.blender.org/docs/release_notes/5.4/ : "in Alpha until February 3, 2027". Nog niets over splat-export in de 5.4-notes.
- GEZIEN, mijlpaal 5.4 op projects.blender.org (API milestones): einddatum 11 mei 2027.

Oordeel punt 1: binnen 3 maanden (tot half februari 2027) komt er geen stabiele Blender met splat-export. Wet 4 haalt het dus formeel. Maar Blender heeft export en selectie-tools officieel gepland en glTF-export is al in de maak. GOK: in 5.4 (mei 2027) zit minstens glTF-export, misschien PLY. Onze gratis kern (export, Apply Transform, selectie) leeft dan ongeveer 6 maanden.

## 2. extensions.blender.org: wat staat er al

GEZIEN via de API https://extensions.blender.org/api/v1/extensions/ (1.680 regels) en zoeken op splat, gaussian, 3dgs, point cloud, ply, spz, gsplat:
- "Splats" (Dev.Patel): maakt trainingsbeelden voor splats, geen bewerking. 3.953 downloads, gepubliceerd 10 dec 2025, laatste update 11 maanden geleden. https://extensions.blender.org/add-ons/splats/
- "Point Cloud I/O" (StudioMedio): import en export van PLY, E57, LAS en meer als point cloud, "any custom scalar fields" gaan mee. 5.304 downloads, 28 mei 2026, Blender 5.1+. https://extensions.blender.org/add-ons/point-cloud-io/ . GOK: geen echte splat-export (namen en waarden van Blender 5.3 kloppen niet met 3DGS PLY), maar deze maker kan dat snel toevoegen.
- "E57 Point Cloud Importer": 2.684 downloads, geen splats.
- "Universal Multi Importer" noemt spz alleen als importformaat.
- Geen enkele extensie die splats bijsnijdt, opruimt of als splat exporteert. Dat klopt met de eerste onderzoeker.

Ter vergelijking (wat is groot): LoopTools 2M, Extra Mesh Objects 1M, Bool Tool 1M downloads (https://extensions.blender.org/add-ons/?sort_by=-download_count). Click Joints: 206 in 9 dagen.

Keuringsrij, GEZIEN https://extensions.blender.org/approval-queue/ (alle 2.450 regels doorgelopen): 1.538 goedgekeurd, 467 afgewezen, 424 "Awaiting Changes", maar maar 21 "Awaiting Review". De meeste wachten een paar dagen tot ruim een week. Wet 1 qua tijd is dus haalbaar. In de rij staan al: "PointCloud and Splat Exporter (.ply, .splat)" van GiancarloV (9 maanden, Awaiting Changes), "Gauss Cannon" en "Gaussian Splat Generator". Een splat-exporter kan dus elk moment goedgekeurd worden.

Buiten de winkel, gratis (GitHub, GEZIEN via GitHub-zoeken en README's):
- KIRI "3DGS Render": 1.265 sterren, laatst bijgewerkt 11 nov 2026. README: "Edit splats using Blender selections, modifiers, cropping and colour tools" en "Export edited 3DGS files". Bovenaan: "Release supporting blender 5.3 coming soon". https://github.com/Kiri-Innovation/3dgs-render-blender-addon
- PlayCanvas "SuperSplat for Blender": MIT, Blender 5.3+, gemaakt door het bedrijf achter SuperSplat. "Exports the selected splat as a standard 3DGS PLY", met "Convert Axes ... applies the object's transform". Dus export plus Apply Transform bestaat al gratis voor 5.3, alleen nog niet in de winkel. https://github.com/playcanvas/supersplat-blender-extension
- Verder kleine: ReshotAI (592 sterren, sinds 2024 stil), blender-splat-exporter (15 sterren).

Grootste splat-add-on: KIRI 3DGS Render (10.800+ downloads op Superhive, zie punt 3, en 1.265 sterren). Grootste in de winkel: Splats met 3.953.

## 3. Superhive

Zoeken op Superhive gaf HTTP 500; productpagina's werken wel met curl. Slugs gevonden via WebSearch. GEZIEN op 17 nov 2026:

| Product | Prijs | Verkopen/downloads | Gepubliceerd | Blender | Wat |
|---|---|---|---|---|---|
| Splat Studio (Blendreams) https://superhivemarket.com/products/splatstudio | $12,99 | niet getoond | 3 dagen geleden | 5.3 | bijsnijden (box, bol, cilinder), "Fit Tight ... drops stray floaters", relight, "Export a standard 3DGS .ply" |
| Splat Stage (AS Formworks) https://superhivemarket.com/products/splat-stage | $39, nu $19,50 | niet getoond | 13 dagen geleden | 5.3, "Verified on official Blender 5.3.0" | voorbereiden, bijsnijden, look, animatie, render, export |
| Splatlight (Javier_Herrera) https://superhivemarket.com/products/splatlight | LITE gratis, Pro $35 | 40+ verkopen, 200+ downloads, 2 beoordelingen | 3 maanden geleden | 4.2 tot 5.2 | LITE: "relight ... and export standard .ply" gratis |
| SplatPilot (Pilot Studio) https://superhivemarket.com/products/splatpilot | $19 | niet getoond | 7 dagen geleden | 5.3 | splat trainen uit scène, export "PLY, SOG or SPZ" |
| SplatGen https://superhivemarket.com/products/splatgen | $1 / Pro $25 | 90+ | 3 maanden geleden | 5.2 | trainen, PLY/SOG-export in Pro |
| SplatWorks https://superhivemarket.com/products/splatworks | $19,99 | 20+ | 6 maanden geleden | 4.2 tot 5.2 | trainingsdata |
| DataSplat https://superhivemarket.com/products/datasplat---blender-to-gaussian | $15 | 10 | 3 maanden geleden | 4.5 tot 5.2 | trainingsdata |
| 3DGS Render by KIRI https://superhivemarket.com/products/3dgs-render-by-kiri-engine | gratis | 10.800+ downloads, 4 beoordelingen | ongeveer 2 jaar geleden | 5.1 tot 5.2 | bijsnijden, opruimen, kleur, export |

Wat dit zegt: binnen 2 weken na 5.3 staan er al 3 betaalde 5.3-tools met bijsnijden en export (Splat Studio, Splat Stage, SplatPilot). De betaalde splat-tools die er al maanden staan verkopen weinig: 10 tot 90 stuks, en de 90 is voor $1. Betaalcultuur is er, maar dun.

## 4. Brede basistaak? (wet 2)

- Veel pers: Blender 5.3 splats kwam op 80.lv, CG Channel, Creative Bloq, Digital Production, radiancefields.com (WebSearch, sep tot nov 2026). Er is dus aandacht.
- Maar het gebruik is klein. De beste splat-extensie in de winkel heeft 3.953 downloads in 11 maanden; de bekendste gratis splat-add-on (KIRI) 10.800+ in ongeveer 2 jaar. Betaalde splat-tools: 10 tot 90 verkopen. Basistools in dezelfde winkel zitten op 1 tot 2 miljoen.
- Iemand die een splat bijsnijdt en exporteert is een 3D-scanner, archviz- of VFX-maker. Dat is een groeiende groep, maar geen "iedere Blender-gebruiker". GOK: ruwweg 1 tot 3 procent van de Blender-gebruikers doet iets met splats.
- Wet 2: NEE. Het is een groeiende nis, geen basistaak.

## Wetten opnieuw

- Wet 1: JA. 5.3 is 7 dagen oud, de keuringsrij is kort (21 wachten op keuring). Bouwen is klein: PLY-export is GOK een paar honderd regels numpy.
- Wet 2: NEE. Nis van scanners en VFX. Downloadcijfers bevestigen dat (duizenden, geen honderdduizenden).
- Wet 3: DEELS. Superhive is een kassa (Dortus staat er al). Maar betaalde splat-tools halen 10 tot 90 verkopen, en er zijn al 3 betaalde 5.3-concurrenten plus 2 gratis tools die hetzelfde doen (KIRI, Splatlight LITE).
- Wet 4: DEELS. Niet binnen 3 maanden (5.4 komt 11 mei 2027), maar Blender heeft export en selectie-tools letterlijk in de planning en glTF-export is al in de maak. Relight zit al rudimentair in 5.3.
- Vraag 5: JA. De winkel zit in Blender en voert vanzelf mensen aan, maar in deze nis zijn dat er weinig.

## Wat ik afschiet aan het oude oordeel

1. "Plek op de gratis winkel nog leeg" klopt alleen op papier. Gratis en al werkend: KIRI (10.800+ downloads, 5.3-versie "coming soon"), Splatlight LITE (gratis export .ply), PlayCanvas SuperSplat (MIT, export plus transform, 5.3). Elk van die drie kan morgen in de winkel staan, en een splat-exporter staat al in de keuringsrij.
2. Op Superhive is het geen "1 week bezet", maar al vol: Splat Studio doet precies onze Pro-lijst (bijsnijden, zwevers, relight, export) voor $12,99.
3. Het bereik is klein. Zelfs als we de eerste in de winkel zijn: GOK 2.000 tot 5.000 downloads per jaar, als Splats. Click Joints-recept werkt, maar de vijver is klein.
4. Blender heeft het zelf gepland. Ons sterkste stuk (export) verliest zijn waarde rond mei 2027.

Wat overeind blijft: snel te bouwen, winkel voert aan, eerste splat-bewerker in de gratis winkel geeft wat naam. Als bereik-project van 2 dagen is het verdedigbaar, niet als hoofdinzet met omzet.

## Mijn cijfer: 4

Het idee blijft geen 7. Wet 2 is een nee, wet 3 en 4 zijn zwak, en de gratis plek wordt door KIRI, PlayCanvas en de exporter in de rij elk moment ingenomen. Alleen doen als klein bereik-klusje (gratis export plus Apply Transform-fix, 2 dagen), niet als product om geld mee te verdienen.
