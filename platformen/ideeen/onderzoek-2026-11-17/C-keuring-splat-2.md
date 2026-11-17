# Tweede keuring: Blender 5.3 Splat Tools (17 nov 2026)

Keurder 2, kant: kunnen wij het bouwen en wie betaalt. Alles gelezen met curl op 17 nov 2026, tenzij anders vermeld. GEZIEN = zelf op de bron gelezen. GOK = mijn inschatting. ONBEKEND = niet kunnen vinden.

## Kort oordeel

Bouwen kan, en snel live ook: de keuringsrij is veel korter dan de eerste onderzoeker dacht. Maar de plek is niet zo leeg als in C-spel-maker.md staat. In de week rond de uitgave van 5.3 kwamen er minstens vijf betaalde en twee gratis splat-add-ons bij, waarvan er één (Splat Prep, $15) precies ons hele plan al doet. De gratis winkelplek op extensions.blender.org is nog leeg, maar een gratis concurrent met export bestaat al op GitHub, en Blender wil zelf export maken. Mijn cijfer: **5**.

## 1. Bouwbaarheid

**Python API voor splats: JA, zonder speciale splat-API.**
- GEZIEN: `bpy.types.PointCloud` in 5.3 heeft `type` (nieuw, "Representation type of the pointcloud", standaard 'POINTS'), `attributes`, `points` en `resize(size)`. https://docs.blender.org/api/5.3/bpy.types.PointCloud.html
- GEZIEN: splat-attributen staan in de release notes: `scale` (vector), `rotation` (quaternion), `radiance:base` (4D: DC-kleur plus opacity), `radiance:sh_{index}` (vectoren voor SH-band 1 en hoger). https://developer.blender.org/docs/release_notes/5.3/rendering/
- GEZIEN: de 5.3 Python API release notes noemen niets over splats; er is dus geen eigen splat-API, alleen het gewone point-cloud-datatype met attributen. https://developer.blender.org/docs/release_notes/5.3/python_api/
- GEZIEN: operators `bpy.ops.wm.spz_import` en `bpy.ops.wm.ply_import` (zet splats om naar point cloud). Er is `bpy.ops.wm.ply_export`, maar die schrijft voor een point cloud 0 punten (GEZIEN als bewering van twee makers op radiancefields.com, 3 okt en 16 nov 2026).
- GEZIEN: `bpy.ops.pointcloud.select_all`, `select_random`, `delete`, `separate`, `duplicate`. Blender heeft dus al een bewerkmodus voor punten waarin je met de hand kunt selecteren en wissen. https://docs.blender.org/api/5.3/bpy.ops.pointcloud.html . Dat maakt "bijsnijden" als losse functie minder waard.
- GEZIEN in de broncode (`source/blender/io/ply/importer/ply_import_gsplat.cc`, GitHub-spiegel van Blender, main): bij import wordt opacity door een sigmoid gehaald en scale door exp, de DC-kleur blijft de ruwe SH-waarde, rotatie wordt genormaliseerd, f_rest wordt van "per kanaal" omgezet naar per coëfficiënt een RGB-vector, tot SH-graad 4. Een exporteur moet dit precies omkeren (logit, log, terug naar kanaalvolgorde). Dat is goed te doen met numpy.
- Kan een add-on lezen, bijsnijden, filteren en als .ply wegschrijven? JA. Lezen met `attributes[...].data.foreach_get` naar numpy, filteren in numpy (kader, opacity, grootte, losse vlekjes via `mathutils.kdtree` of een eigen raster), nieuwe point cloud met `resize` en `foreach_set`, of `bpy.ops.pointcloud.delete` op een selectie, en zelf een binaire PLY schrijven in de standaard 3DGS-indeling. Twee bestaande add-ons doen dit al zo (Gaussian Splat Patch, Splat Prep), dus het is bewezen mogelijk.
- Moeilijkste stuk: een Apply Transform die klopt. Bij draaien moeten ook de SH-coëfficiënten mee draaien (Wigner-rotatie per band). Splat Prep en Gaussian Splat Patch hebben dat (GEZIEN in de artikelen), dus het kan, maar het is wiskunde waar fouten niet opvallen zonder goede toets.
- SPZ wegschrijven is lastiger (eigen gecomprimeerde indeling, versie 4). GOK: voor een eerste versie alleen PLY.

**Testen in GitHub Actions met echte Blender: JA.**
- GEZIEN: Dortus heeft al `.github/workflows/blender-gewrichten-e2e.yml` met Blender 4.2.23, 5.2.3 en **5.3.0** in de matrix, Linux, achtergrond.
- Splat-gereedschap is data, geen beeld: importeer een klein test-PLY, draai crop/filter/transform, exporteer, importeer opnieuw en vergelijk de getallen met numpy. Dat heeft geen GPU nodig. Een eigen klein test-PLY (bijvoorbeeld 1.000 splats, met SH-graad 3) kan het script zelf maken, dus geen downloads van derden. Renderen voor winkelplaatjes kan met Cycles op de CPU of Workbench onder Xvfb, zoals bij Click Joints.
- Let op: de add-on vraagt minstens Blender 5.3 (`blender_version_min = "5.3.0"`). De matrix moet dus alleen 5.3 draaien voor dit product.

**Uren voor een eerste versie (GOK):** 20 tot 35 uur agentwerk.
- Lezen, filteren (opacity, grootte, uitschieters, kader) en PLY-export met heen-en-terug-toets: 8 tot 12 uur. Reden: de formules staan in de broncode, numpy doet het zware werk.
- Apply Transform met SH-rotatie tot graad 3 plus een toets die een gedraaide kopie vergelijkt: 8 tot 15 uur. Reden: wiskunde, en bij Click Joints kostte elke echte meetfout een paar runs.
- Paneel, manifest, winkelplaatjes en indienen: 4 tot 8 uur. Reden: dat ging bij Click Joints ook zo, en de opzet ligt er al.

## 2. Keuring en snelheid

**De rij van 2.450 is geen wachtrij.** GEZIEN: https://extensions.blender.org/approval-queue/ (alle 49 pagina's op 17 nov 2026 gelezen). Die 2.450 zijn alle inzendingen ooit, in elke status:
- Approved: 1.538
- Declined: 467
- Awaiting Changes: 424
- **Awaiting Review: 21**

De meeste van die 21 zijn uren tot een week oud (één staat er een maand, één al 2 jaar, dat lijken uitzonderingen).

**Eigen meting van Dortus, GEZIEN** in `platformen/blender/logboek.md` en `status.md`: Click Joints 0.1.0 ingediend 8 nov 22:18 NL, goedgekeurd 10 nov 10:34 NL door moderator nickberckley. Dat is **±36 uur**.

**Binnen 7 dagen live: JA, waarschijnlijk.** GOK: 2 tot 5 dagen bouwen plus 1,5 tot 7 dagen keuring. Twee risico's die wel kunnen vertragen (GEZIEN in de rij):
- Een moderator vroeg bij een splat-exporteur: "Blender already has native .ply exporter. How is it different?" Ons antwoord moet meteen in de beschrijving staan: de ingebouwde export schrijft 0 punten voor een splat.
- Afwijzingsredenen die ik bij splat-inzendingen zag: afhankelijk zijn van software van derden ("We do not host extensions that depend on ... third-party softwares", bij Gaussian Splat Generator, 7 maanden blijven hangen) en `sys.modules` aanpassen (bij PointCloud and Splat Exporter, 9 maanden blijven hangen). Allebei makkelijk te vermijden.

**Belangrijk voor wet 4 en het "eerst zijn":** in de rij staat al **"PointCloud and Splat Exporter (.ply, .splat)"** van GiancarloV, sinds 9 maanden in Awaiting Changes. GEZIEN: https://extensions.blender.org/approval-queue/gv-point-cloud-exporter/ . Hij exporteert splats naar standaard 3DGS PLY en .splat. Repareert de maker zijn ene punt, dan staat hij er binnen dagen. GOK: kans klein, hij reageerde 4 maanden niet, maar het kan.

## 3. Wie betaalt

**Wie maakt splats:** mensen die met hun telefoon scannen (Scaniverse, Polycam, KIRI, Luma) of op de pc trainen (Postshot, LichtFeld Studio, Brush). Ze willen de scan in een scène zetten: archviz, VFX, productbeelden, games, erfgoed. GOK, op basis van de doelgroepen die de bestaande add-ons noemen.

**Grootste pijn (GEZIEN in artikelen, niet in forumdraden):**
- Zwevers en rommel rond de scan moeten weg. Dit doen mensen nu vooral gratis in SuperSplat (browser, PlayCanvas) voordat ze iets naar Blender halen.
- Blender 5.3 kan niet exporteren, Apply Transform en Join "verplaatsen alleen de middens, dus een gedraaide scan smeert uit" (Nico Hartl, Splat Prep, radiancefields.com 16 nov 2026).
- Snelheid in het viewport bij miljoenen splats ("Performance is not ideal", release notes).
- ONBEKEND: echte klachten uit Reddit of forums; Reddit blokkeert curl (403), het Scaniverse-forumdraadje gaf 404.

**De markt is al vol, in één week (GEZIEN op Superhive en radiancefields.com, 17 nov 2026):**

| Product | Waar | Prijs | Wat |
|---|---|---|---|
| Splat Prep (NicoHartl) | Superhive, 2 dagen oud | $15 (normaal $19) | Apply Transform met SH, Join, opruimen (zwevers, losse delen, vage splats, lucht, uitschieters), Live Crop, kleur bakken, Reduce, Proxy Mesh, export PLY, gecomprimeerd PLY, SPZ, .splat |
| Splat Studio (Blendreams) | Superhive, 3 dagen oud | $12,99 | relight, bijsnijden, opruimen, export |
| Splat Stage (AS Formworks) | Superhive, 13 dagen | $39, nu $19,50 | bijsnijden, kleur, mist, renderen |
| Splatlight (Javier_Herrera) | Superhive, 3 maanden | LITE gratis (met .ply-export), Pro $35 | **Sales 40+**, 2 beoordelingen |
| Gaussian Splat Patch (Tim Fennell) | GitHub, gratis, GPL | gratis | wissen, kloonstempel, helen, samenvoegen, eigen Export Splat PLY |
| SuperSplat for Blender (PlayCanvas) | GitHub, gratis | gratis | scènes van superspl.at halen, publiceren als 3DGS PLY met juiste assen en SH |
| 3DGS Render (KIRI) | Superhive, gratis | gratis | oudere aanpak, renderen |

Bronnen: https://superhivemarket.com/products/splat-prep , /splatstudio , /splat-stage , /splatlight ; https://radiancefields.com/splat-prep-brings-splat-export-to-blender-5-3 (16 nov 2026), https://radiancefields.com/gaussian-splat-patch-merges-splat-objects-and-bakes-edits-permanently-in-blender (20 okt 2026), https://radiancefields.com/playcanvas-releases-supersplat-for-blender-0-1-0 (5 nov 2026).

**Betaalcultuur: JA, maar klein.** Splatlight Pro ($35) heeft 40+ verkopen in 3 maanden (GEZIEN). GOK: dat is ±$1.400 omzet in 3 maanden voor de beste in deze hoek.

**Wat moet een Pro van $12 tot $19 doen dat gratis niet doet?** Eerlijk: ik zie geen ruimte. Splat Prep doet voor $15 alles wat C-spel-maker.md als gratis plus Pro voorstelt, en meer. Een Dortus-Pro zou moeten winnen op iets wat Splat Prep niet heeft. Kandidaten (GOK):
- Splat naar dichte, printbare mesh (sluit aan op Click Joints). Maar: KIRI maakt in de app al een mesh van 3DGS, Splat Prep heeft een Proxy Mesh, en telefoon-scanapps geven voor 3D-print gewoon meteen een mesh. Geen sterke pijn.
- Batch: een map scans in één keer opschonen en exporteren. Smal.
- SPZ-export en web-klare compressie. Splat Prep heeft het al.

## 4. Snelst te verdienen variant

- **"Splat Export" (gratis, extensions.blender.org): bereik ja, geld nee.** Snelste bouw (8 tot 12 uur, GOK), lost de pijn op die in elke 5.3-recensie staat ("can't export them yet"). Maar: Gaussian Splat Patch doet het gratis op GitHub, Splatlight LITE gratis op Superhive, een exporteur hangt al in de keuringsrij, en volgens Hartl plant Blender eigen PLY-export (tweedehands bron, GEZIEN in het artikel van 16 nov 2026; eigen bevestiging bij Blender ONBEKEND). GOK: export komt in 5.4 (rond maart 2027) of 5.5. Dan is deze add-on in 4 tot 8 maanden dood.
- **"Bijsnijden en schoon exporteren":** bijsnijden kan al met de hand in de ingebouwde bewerkmodus voor punten (selecteren, Delete). De echte waarde zit in automatisch opruimen plus export plus een kloppende Apply Transform. Dat is precies Splat Prep.
- **"Splat naar mesh voor 3D-print":** GOK: geen acute pijn. Wie een ding wil printen, scant in KIRI of Polycam en exporteert een mesh; splats zijn juist voor beelden. Aansluiting op Click Joints-gebruikers is te zwak om op te bouwen.
- Conclusie: er is een smalle, acute pijn (export plus kloppende transform), maar betaald is hij al bezet en gratis wordt hij binnen maanden door Blender zelf opgelost.

## De wetten, vanuit mijn kant

- Wet 1 (vroeg, binnen 7 dagen live): JA. API is 7 dagen oud, keuring nu ±36 uur tot een week (GEZIEN eigen meting en de rij).
- Wet 2 (brede basistaak): NEE tot DEELS. Alleen voor wie splats gebruikt. Export is voor die groep wel een basistaak.
- Wet 3 (kassa): DEELS. Superhive werkt, betaalcultuur bestaat, maar onze Pro heeft geen eigen reden om te bestaan naast Splat Prep voor $15.
- Wet 4 (platform doet het niet zelf binnen 3 maanden): DEELS, eerder nee voor export. Blender wil export maken (tweedehands GEZIEN), point-cloud bewerkmodus bestaat al (GEZIEN). Binnen 3 maanden komt er geen nieuwe Blender (5.4 GOK maart 2027), dus net op de rand.
- Vraag 5 (etalage): JA. extensions.blender.org voert vanzelf mensen aan; op zoekwoord "splat" staat nu alleen "Splats" van Dev.Patel (trainingsbeelden, geen bewerking), GEZIEN via de API van extensions.blender.org (1.680 extensies doorzocht).

## Cijfer

**5.** Bouwen en live krijgen binnen een week lukt zeker, en de gratis winkelplek is op dit moment echt leeg. Maar het geldverhaal klopt niet: vijf betaalde concurrenten in één week, één ervan doet alles voor $15, gratis concurrenten bestaan al buiten de winkel, en Blender maakt export waarschijnlijk zelf. Alleen te doen als bereikproject: in 2 tot 4 dagen een gratis "Splat Export and Fix" (export PLY plus kloppende Apply Transform plus opruimen) op extensions.blender.org, als eerste op die plank, zonder een Pro-plan. Geen tijd van Click Joints Pro afhalen.
