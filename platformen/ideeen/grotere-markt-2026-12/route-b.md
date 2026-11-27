# Route B: ons vak naar printers zonder Blender (Afkijker B, 27 nov 2026)

Opdracht: issue #323, route B. Alleen onderzoek, niets gebouwd. Alles gelezen met `curl` op 27 nov 2026 tussen ±21:00 en 22:15 NL, tenzij anders vermeld. Niets geplaatst, niemand benaderd, geen account gemaakt.

**Kort antwoord.** Route B is geen grotere markt voor ons, in elk geval niet als hulpmiddel (tool). Het publiek is wel 30 keer groter dan Superhive, maar het geld van printers gaat naar modellen en verkooplicenties, niet naar gereedschap. De tools die er verkopen, verkopen op het niveau van Cleave of lager (TrestleFDM 268 verkopen à $12, JointLab 20+). Slicers, Bambu en losse sites geven splitsen, verbinders, een tolerantietest en zelfs flexi-figuren al gratis weg. En alles in die wereld verkoopt met foto's van echte prints, die wij niet hebben (Thijs heeft geen printer, besluit 25 nov 23:01). De enige echt nieuwe deur is de **pluginwinkel van OrcaSlicer, open sinds 7 nov 2026**. Of daar al een splitser voor je eigen STL staat, is niet nagekeken (ONBEKEND: de hub heeft 227 plugins en vraagt een login; ik zag er via Reddit en een schermafdruk maar een paar). Dat is kans 1. Het bereik is daar goed, maar geld is lastig: de code van een plugin in de hub is openbaar en de hub heeft geen kassa. Ik schat kans 1 op **±€25 tot €240 per maand na 3 maanden**, eerder bereik voor Click Cuts dan een eigen inkomen.

*Bijgewerkt 27 nov ±23:30 NL na de keuring van Afkijker C (`keuring-route-b-door-c.md`, 4 moet-punten): rekenfout bij kans 1 hersteld, tweede scenario met ons eigen omzetcijfer, plaatsen op de plaat en betalen in de hub eerlijk opgeschreven, "geen splitser in de hub" als ONBEKEND, Embedder als concurrent, bereik uit de trendlijst van de hub. Ruwe JSON nu in `route-b-data/`.*

## Hoe gezocht (voor de keurder)
- De belangrijkste ruwe uitslagen staan in `route-b-data/` (teruggeknipt tot de velden die als bron dienen): Kickstarter-stats van Split3r, Gumroad-data van TrestleFDM, Patreon-tellers, de forumdraadjes van Bambu, de 100 nieuwste posts van r/OrcaSlicer. De rest is opnieuw te doen met dezelfde `curl`-adressen hieronder.
- Hulpje om tekst uit html te halen: `re.sub` op tags, daarna zoeken op een woord (geen bijzondere tools).
- **Niet te lezen (403):** makerworld.com (webpagina's), cults3d.com, all3dp.com, producthunt.com, fabbaloo.com, 3printr.com, meshy.ai (site; de docs wel). GitHub-API is in deze sessie afgeschermd, dus downloadcijfers van OrcaSlicer heb ik niet. De interne API van Orca Cloud heb ik niet aangeroepen (niet gedocumenteerd); wat er in de hub staat komt uit Reddit-posts van de makers zelf.
- Openbare JSON die ik wel las: Arctic Shift (kopie van Reddit), Discourse-JSON van forum.bambulab.com (`/t/<id>.json`), Patreon (`/api/campaigns?filter[vanity]=...`), Gumroad (data in de productpagina), Kickstarter (`/stats.json` van het project), Printables GraphQL (de query uit `commercie/verspreiden/2026-11-23-printables.md`), Semrush (cw.semrush.com).

## 1. Hoe groot is de groep?
| Site | Bezoeken oktober 2026 | Bron |
|---|---|---|
| MakerWorld (Bambu) | 53,09 mln | DERDEN, https://cw.semrush.com/website/makerworld.com/overview/ |
| Printables (Prusa) | 15,9 mln | DERDEN, https://cw.semrush.com/website/printables.com/overview/ |
| Thingiverse | 15,46 mln | DERDEN, https://cw.semrush.com/website/thingiverse.com/overview/ |
| Cults3D | 14,66 mln | DERDEN, https://cw.semrush.com/website/cults3d.com/overview/ |
| Superhive (onze winkel nu) | 1,69 mln | DERDEN, https://cw.semrush.com/website/superhivemarket.com/overview/ |

Reddit (DERDEN, Arctic Shift `api/subreddits/search`, kan achterlopen): r/3Dprinting 3.465.158 leden, r/BambuLab 217.767, r/prusa3d 113.989, **r/OrcaSlicer 7.703**.

Het publiek is dus 30 keer zo groot als Superhive (53,09 / 1,69, alleen MakerWorld). Maar dat zegt niets over wie voor een tool betaalt; zie deel 3.

## 2. Wat doen slicers en platforms al gratis?
| Wie | Wat gratis | Bron (GEZIEN tenzij anders) |
|---|---|---|
| **Bambu Studio** | Cut tool met vlakke snede en **dovetail** (diepte, breedte, hoek instelbaar), verbinders **Plug, Dowel en Snap**, delen kleuren, plat leggen ("Place on cut") | https://wiki.bambulab.com/en/software/bambu-studio/cut-tool |
| **PrusaSlicer** | Cut tool met Plug, Dowel en Snap (stijl, vorm, diepte, draaiing), dovetail-modus, plat leggen | https://help.prusa3d.com/article/cut-tool_1779 |
| **OrcaSlicer 2.4 en 2.5** | Zelfde cut tool, sinds 2.4 **meerdere dovetails in één snede**; ingebouwd **tolerantietestmodel** (gaten 0,0 tot 0,4 mm, "Add Handy Model"); sinds 2.5 een eigen ontwerptab (parametrisch) en **Python-plugins** | https://www.orcaslicer.com/wiki/releases/release_2_4_0_alpha.html, https://www.orcaslicer.com/wiki/calibration/tolerance_calib.html, https://www.orcaslicer.com/wiki/releases/release_2_5_0.html |
| **Bambu MakerLab: Flexi Toy Maker** | Van een plaatje een persoonlijk beweegbaar (flexi) speeltje, met voorbeeld van het buigen; live sinds 24 apr 2025, 7.377 keer bekeken | https://forum.bambulab.com/t/164063.json. Of het onbeperkt gratis is: GOK ja (MakerLab-hulpmiddelen) |
| **PrintPal Flexi / Articulated Model Creator** | Website: STL erin, klik waar een flexi-gewricht moet, snijdt het uit, STL eruit. Gratis, sinds 26 feb 2026 | https://printpal.io/tools/flexi-model-creator, https://blog.printpal.io/introducing-printpal-tools-a-free-suite-of-3d-printing-selling-tools-2/ |
| **3D Splitter** | Website: groot model in delen, met puzzelverbinding, "100% free", alles lokaal in de browser; nieuws 12 dec 2025 | https://www.3dsplitter.com/, https://www.notebookcheck.net/3D-printing-big-stuff-on-small-printers-made-easy-with-new-free-browser-based-tool.1184411.0.html |
| **Flexifier** | Plaatje naar flexi-model, gratis op Printables; 2.515 downloads, 1.044 likes, sinds 17 jun 2023 | Printables GraphQL, model 505713 |
| **Meshy** (betaald) | "Auto Split" met verbinders (kubus of cilinder), ook als plugin in OrcaSlicer. **Alleen op modellen die in Meshy zelf gemaakt zijn**: "Uploaded and remeshed models can't be split" | https://docs.meshy.ai/en/webapp/guides/3d-model/auto-split, https://docs.meshy.ai/en/webapp/plugins/orcaslicer/use-the-plugin |

**Waar zit nog een gat?**
1. **Automatisch splitsen tot alles op je bed past, met nummers, voor je eigen STL, in de slicer.** Geen enkele slicer doet het. Bambu-forum, 22 feb 2026: vraag om "automatically split a large 3D print into multiple smaller parts with automatic connector placement ... similar to Luban"; antwoord: "sadly, no fully automatic no" (GEZIEN, https://forum.bambulab.com/t/236266.json, 177 keer bekeken). En: LuBan is "ridiculously expensive for hobbyists" (2 sep 2025) en "Lubans is a ripoff" (16 apr 2026) (GEZIEN, https://forum.bambulab.com/t/193172.json, 143 keer bekeken). Kleine draadjes, maar het gat is echt.
2. **Echte kogel- en scharniergewrichten in een gedownload figuur, zonder Blender.** Alleen JointLab (web) doet dit; de gratis tools maken alleen flexi-ringen (PrintPal) of flexi uit een plaatje (Bambu, Flexifier). Let op: ons sterkste punt, de rig lezen, bestaat niet bij een STL. Een STL heeft geen rig.
3. **Passing per materiaal en per printer onthouden.** Orca heeft een tolerantietest, maar die stelt de slicer bij, niet de maat van een pen of gewricht. Klein gat, geen product op zich.

## 3. Bewijs dat printers voor zoiets betalen
| Wat | Cijfer | Bron |
|---|---|---|
| **Split3r** (automatisch splitsen van grote prints, Frans bedrijf Qualup SAS) | Kickstarter geslaagd, **2.501 backers, 114.405** opgehaald (valuta niet in de JSON; GOK euro), afgesloten 9 okt 2025. Nu Basic €60, Add-ons €35, Full €95, levenslang | GEZIEN, https://www.kickstarter.com/projects/1492464013/split3r-automatically-split-your-3d-files/stats.json en https://split3r.com/ |
| **LuBan** (automatisch splitsen, Windows) | $30 per maand, $150 per jaar, $750 voor altijd | GEZIEN, https://www.luban3d.com/license |
| **TrestleFDM** (losse app voor FDM-minis: boomsteunen plus **snijden met pennen, deuvels, magneetgaten, passingbalkje**) | **268 verkopen** op Gumroad, vanaf $12 (betaal wat je wilt), 8 beoordelingen gemiddeld 5,0; snijden zit erin sinds versie 1.5; Windows en Linux, geen Mac | GEZIEN, https://diogom3d.gumroad.com/l/TrestleFDM en https://trestlefdm.pages.dev; Reddit-post 23 nov 2026, 27 punten (GEZIEN, Arctic Shift id 1y3qau0) |
| **JointLab** (web en Blender, gewrichten) | Web: **1.537 accounts** (24 nov in de lat: 1.483, dus ±18 per dag); Pro $9,99 per maand, $89,99 per jaar; hoeveel er betalen is niet openbaar. Superhive: 20+ verkopen in 4 maanden | GEZIEN, https://jointlab3d.com/api/stats, https://jointlab3d.com/planos/?lang=EN, `organisatie/lat/click-joints-pro.md` |
| **FlexySliceSTL** (programma: STL naar flexi-model) | Crowdfunding op MakerWorld, "the initial funding target has already been reached" (maker, 28 sep 2026). Aantal backers niet te lezen (403) | DERDEN, https://forum.bambulab.com/t/259062.json (436 keer bekeken) |
| **HueForge** (programma voor printers) | $24 eenmalig tot $350; verkoopcijfers niet openbaar | `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-24-hueforge.md` |
| **Flexi Factory** (flexi-modellen, Patreon) | **7.377 betalende leden** van 45.738 | GEZIEN, Patreon-API vanity `flexifactory` |
| **Cinderwing3D** (beweegbare draken, Patreon) | **6.306 betalend** van 48.145; commerciële licentie $10 per maand (21 nov) | GEZIEN, Patreon-API vanity `cinderwing3d`; prijs uit `afkijken-2-2026-11-21/B-print-publiek.md` |
| **Painted4Combat** (Resin2FDM, Blender-add-on voor printers) | 1.334 betalend vanaf $2 | GEZIEN, Patreon-API vanity `Painted4Combat` |
| **NunnBreakable** (NB Figure Joints, gewrichten-tool achter Patreon) | **7 betalend** van 311 | GEZIEN, Patreon-API vanity `NunnBreakable` |
| **Jopek Design** (gratis toppers, Patreon) | 122 betalend van 936, bij 386.448 gratis downloads | GEZIEN, Patreon-API; downloads uit `B-print-publiek.md` |
| Betaalde modellen op Printables | Van 3.812 betaalde modellen (mei tot aug 2026) kreeg **3% ooit één beoordeling**; aankopen zijn verborgen | `onderzoek/verkenner/voorstellen/printables.md` (eigen meting 8 nov) |
| Betaalde modellen op MakerWorld | Bestaan niet; gebruikers vragen erom (27 mei 2026), anderen willen het niet ("I have zero interest in paying for models") | GEZIEN, https://forum.bambulab.com/t/253854.json |

**Wat dit zegt:**
- **Het grote geld zit in modellen en licenties, niet in tools.** Flexi Factory en Cinderwing3D hebben elk ruim 6.000 betalers. Een gewrichten-tool achter Patreon heeft er 7 (NunnBreakable).
- **Tools voor printers verkopen ongeveer zoals Cleave of minder**: TrestleFDM 268, JointLab 20+ op Superhive. De uitzondering is Split3r: één keer 2.501 backers (gemiddeld ±46 per backer, rekensom 114.405 / 2.501), met filmpjes van gigantische prints (op hun site: een Deadpool van 1,85 m).
- **Automatisch splitsen is het enige printerprobleem waar aantoonbaar honderden tot duizenden mensen een tool voor kochten** (Split3r, LuBan, TrestleFDM). Gewrichten in een figuur als tool: weinig bewijs (JointLab, NunnBreakable).

## 4. Nieuw: plugins in OrcaSlicer (sinds 7 nov 2026)
- **OrcaSlicer 2.5.0 kwam uit op 7 nov 2026** (GEZIEN, https://newreleases.io/project/github/OrcaSlicer/OrcaSlicer/release/v2.5.0, tijdstempel 2026-11-07), 2.5.1 op 14 nov. "You can now add features with Python plugins ... The community has already created and shared lots of plugins on the Orca Cloud plugin hub" (GEZIEN, release notes 2.5.0).
- **Hoe het werkt** (GEZIEN, https://www.orcaslicer.com/wiki/plugins/plugins_cloud.html en `plugins_types.html`): inloggen bij Orca Cloud, Plugins, Browse plugins, Subscribe, Activate. Soorten: Script (knop Run), Pages (eigen tab), Slicing pipeline, textuurpakketten. Python, met eigen pakketten via `uv`.
- **De API leest het model alleen**: "orca.host ... gives plugins read-only access ... nothing here mutates the model" (GEZIEN, `developer_reference/plugin_development/api_reference/host.html`). Er is geen functie om nieuwe delen op de plaat te zetten. OrcaCAD ("Send to plate", r/BambuLab 18 nov, GEZIEN Arctic Shift id 1xzaeiy) doet het met een **omweg**: STL naar schijf schrijven en die via een Windows-bericht (`WM_COPYDATA`) aan Orca geven, of Orca opnieuw starten met het bestand; de eigen melding zegt "the plate import itself cannot be confirmed ... drag the saved STL from exports if missing" (DERDEN, code `orcad.py` r. 678 tot 730 van https://github.com/yazdannl/orcad-plugin, gelezen door Afkijker C in `keuring-route-b-door-c.md`; GitHub is in mijn sessie dicht). Holes Fixer maakt een kopie van het project ("every affected plate is duplicated with the fixed parts", r/OrcaSlicer 25 nov, **186 punten**, GEZIEN id 1y545ri). Voor een splitser is "de delen op de plaat" het hart van het product, en die omweg is per besturingssysteem anders en vraagt de toestemming om andere programma's te starten.
- **Geld:** de hub heeft geen kassa. In de Orca Cloud-wiki staan alleen "Donation Links" bij je profiel (GEZIEN, https://cloud.orcaslicer.com/wiki/), en de FAQ zegt "Core Orca Cloud features for individual OrcaSlicer users will remain free" (DERDEN, keuring C). **De code van een openbare plugin is openbaar**: je uploadt `.py` of `.whl`, en "the uploaded files ... follow the plugin's visibility" (DERDEN, Orca Cloud-wiki volgens keuring C). Een sleutelcontrole in Python haal je er met één regel uit. Meshy verdient wel, maar daar gebeurt het werk op hun eigen server (GEZIEN, Meshy-docs: splitsen "need a Pro plan or higher"). Eerlijke opties voor ons: (a) gratis plugin met donatielink, (b) het zware werk op een eigen server (kost geld en een account: alleen Thijs), (c) een betaalde versie als los bestand buiten de hub verkopen (lokaal installeren kan, "Install local plugin"; maar ook die code is te delen).
- **Drukte en bereik:** de hub telt **227 plugins** (GEZIEN, schermafdruk in de eigen wiki van Orca, https://cloud.orcaslicer.com/wiki/OrcaCloud-plugins-assets/20-plugin-hub-home.png, gemaakt na 20 nov want "Blender Studio" staat erop). Op die schermafdruk: "Trending now, Subscribers 7d": BumpMesh Textures +2.283, ModelFinder +1.946, OrcaCAD +1.326, Support Fins +1.236, Print Calculator +1.226; gewone plugins hebben 5 tot 417 abonnees. En **Embedder** ("puts magnets and NFC stickers inside your prints", 192 abonnees) van een maker met er minstens 7 in beeld (Embedder, Kobra Control, Organizer, Print Calculator, U1 Control, Spooler). Van de 100 nieuwste posts in r/OrcaSlicer (13 tot 27 nov) gaan er 15 over plugins (GEZIEN, Arctic Shift); "Pluginator" (84 punten) laat zien dat niet iedereen wil inloggen. **Of er al een splitser of gewrichten-plugin voor je eigen STL in de hub staat: ONBEKEND.** Ik zag er geen in de 16 plugins op de schermafdruk en in de Reddit-posts (alleen Meshy, voor eigen Meshy-modellen), maar de andere ±211 kon ik niet zien zonder login. Open punt voor de hoofdchat, zie onderaan.
- **Bambu Studio en PrusaSlicer:** geen pluginsysteem gevonden (GOK, gezocht op "Bambu Studio plugin support"; alleen nieuws over printerkoppelingen). Een plugin bereikt dus alleen wie OrcaSlicer 2.5 gebruikt en inlogt. Hoeveel dat er zijn: ONBEKEND (GitHub dicht in deze sessie); r/OrcaSlicer is 28 keer kleiner dan r/BambuLab (7.703 tegen 217.767, DERDEN).

## 5. De 3 sterkste kansen

### Kans 1: "Click Cuts voor OrcaSlicer" (plugin, eigen STL op je bed laten passen)
**Wat:** een Pages-plugin in OrcaSlicer: kies je printer (komt uit het Orca-profiel), één knop, het model wordt in delen gesneden die op het bed passen, met pennen of magneetgaten, nummers op de delen, en de Fit test strip. Dat is het gat uit deel 2 punt 1 (geen slicer doet het automatisch), en ons voordeel uit `organisatie/lat/click-cuts.md` ("één knop en alles past op jouw bed"). Of iemand dit al in de hub zette: ONBEKEND (deel 4).
- **Kopers en bereik:** ONBEKEND hoeveel Orca 2.5-gebruikers er zijn. Wel vast: 2.501 mensen kochten Split3r, 268 kochten TrestleFDM, Holes Fixer haalde 186 punten in een sub van 7.703 leden (alle GEZIEN). In de hub zelf groeien de vijf drukste plugins met +1.226 tot +2.283 abonnees per week; gewone plugins staan op 5 tot 417 abonnees (GEZIEN, schermafdruk hub, deel 4). GOK: 300 installaties in 3 maanden als we een gewone plugin worden, 2.000 als we in de trendlijst komen.
- **Prijs nu:** $12 (TrestleFDM), €60 tot €95 (Split3r), $150 per jaar (LuBan) (alle GEZIEN). In de hub zelf: €0, er is geen kassa (deel 4).
- **Concurrenten en zwakke plek:**
  1. *De eigen Cut tool van Orca* (gratis): niet automatisch, één vlak tegelijk, geen nummers, geen bed-check (forumantwoord "no fully automatic").
  2. *TrestleFDM* ($12): apart programma, alleen Windows en Linux, gericht op minis; heeft wel organisch snijden, magneetgaten en een passingbalkje, dus inhoudelijk sterk.
  3. *Embedder* (gratis plugin in de hub, 192 abonnees): zet magneten en NFC-stickers in je print; splitst niet, maar zit al op onze magneetgaten, en de maker heeft er minstens 7 en vult snel gaten (GEZIEN, schermafdruk hub).
  Ook: Split3r (€60 tot €95, apart programma, duur voor een hobbyist), 3D Splitter (gratis, buiten de slicer) en Meshy (alleen eigen Meshy-modellen).
- **Bouwen:** GOK **4 tot 6 weken** (was 3 tot 4). Onze code is Blender (bpy en bmesh); in Orca moet het met gewone Python-pakketten (bijvoorbeeld trimesh en manifold3d via `uv`), dus de snij- en verbindercode opnieuw schrijven, plus een html-paneel. Daar bovenop: **de delen op de plaat krijgen**. De API kan dat niet; het enige voorbeeld (OrcaCAD) doet het met een omweg per besturingssysteem en kan zelf niet bevestigen dat het lukte (deel 4). Wij kunnen alleen Linux proberen (flatpak bestaat, GEZIEN in de downloads van 2.5.0; of die in onze cloud zonder scherm draait: GOK). Windows en Mac, waar bijna alle kopers zitten (GOK), kunnen wij niet testen. Dat is het grootste bouwrisico.
- **Verdienmodel:** een Gumroad-sleutel in een openbare plugin is met één regel weg te halen (deel 4). Realistisch: (a) gratis plugin met donatielink en een link naar Click Cuts op Gumroad en Superhive; (b) een betaalde versie als los bestand buiten de hub, wetend dat die gedeeld kan worden; (c) het werk op een eigen server zoals Meshy (geld en account: alleen Thijs, nu niet). De rekensom hieronder gaat uit van (b), dus is eerder te hoog dan te laag.
- **Euro per maand na 3 maanden (GOK, twee scenario's, wisselkoers GOK $1 = €0,92, kosten Gumroad GOK 10% plus $0,50 per verkoop, zie `commercie/blender-click-joints/echte-print-KEURING.md` A13):**
  - *Scenario 3% van gratis naar betaald* (gangbaar bij tools, GOK): 2.000 installaties x 3% = **60 kopers in 3 maanden**, gemiddeld 20 per maand. Per verkoop $15 min 10% min $0,50 = $13,00. 20 x $13,00 = $260, **±€240 per maand**.
  - *Scenario 0,3%, ons eigen cijfer* (Click Joints: 375 gratis downloads, 1 verkoop = 0,27%, `organisatie/lat/click-joints-pro.md`): 2.000 x 0,3% = 6 kopers in 3 maanden, 2 per maand x $13,00 = $26, **±€24 per maand**.
  - Bij maar 300 installaties (gewone plugin) is het €4 tot €36 per maand.
  - Middenschatting: **±€75 per maand** (GOK, het midden van beide scenario's op een schaal van keer tien: wortel van 24 x 240). Bandbreedte €4 tot €240.
- **Grootste reden om te mislukken:** geld. De hub heeft geen kassa en de code is openbaar, dus een sleutel helpt weinig; daarbij kan iemand er gratis een neerzetten (Embedder laat zien hoe snel) of bouwt Orca het zelf in (open source; in 2.4 al meerdere dovetails). Tweede reden: de delen betrouwbaar op de plaat krijgen op Windows en Mac, wat wij niet kunnen testen.
- **Ideeëntest, vier wetten:** (1) vroeg: ja, hub 3 weken oud; (2) brede basistaak: half, groot printen doet niet iedereen; (3) kassa: **nee** in de hub, en een eigen sleutel is in openbare code zwak; volgens de test mag dat alleen als het bereik groot is (nummer één in een snel groeiende winkel), en dat kan hier wel; (4) platform bouwt het zelf: risico middel.

### Kans 2: website "STL erin, gewrichten eruit" (Click Joints in de browser)
**Wat:** een site op dortus.com: sleep een figuur-STL erin, klik waar een kogel of scharnier moet, kies de hoek waar het scharnier stopt, krijg printbare delen plus de Fit test strip. Gratis proberen, betalen per maand of eenmalig.
- **Kopers:** JointLab web 1.537 accounts, ±18 nieuwe per dag (GEZIEN); hoeveel betalen ONBEKEND. De vraag naar beweegbare figuren is groot (Flexi Factory 7.377 betalers, Dummy 13 332.177 downloads, `B-print-publiek.md`), maar dat zijn modellen, geen tool.
- **Prijs nu:** JointLab Pro $9,99 per maand of $159,99 levenslang (lat); PrintPal en Bambu gratis.
- **Concurrenten en zwakke plek:**
  1. *JointLab web* (gratis plus Pro): één ster op Superhive "Hard to use" (lat); wel kogels en scharnieren.
  2. *PrintPal Flexi Creator* (gratis): alleen flexi-ringen, geen kogel, geen scharnier met eindstop.
  3. *Bambu Flexi Toy Maker* (gratis): alleen van een plaatje, niet je eigen STL.
  Ook: FlexySliceSTL (crowdfunding gehaald), NB Figure Joints en SlicerJoint Pro (Blender).
- **Bouwen:** GOK 5 tot 8 weken. Alles opnieuw in JavaScript en WebAssembly (bijvoorbeeld three.js en manifold-3d), plus een kassa en een login. **Ons echte voordeel valt weg**: de rig lezen werkt niet op een STL, dus wij worden een JointLab-kopie met een eindstop.
- **Euro per maand na 3 maanden (GOK, zelfde kosten en wisselkoers als kans 1):** 1.000 accounts in 3 maanden (JointLab-tempo is ±540 per maand, rekensom 18 x 30). Scenario 2% betaalt: 20 abonnees x ($9,99 min 10% min $0,50 = $8,49) = $170, **±€155 per maand**. Scenario 0,3% (ons eigen cijfer): 3 x $8,49 = $25, **±€23 per maand**. Middenschatting ±€60 (wortel van 23 x 155). Bandbreedte €0 tot €300.
- **Grootste reden om te mislukken:** drie gratis alternatieven, waarvan één van Bambu zelf; vinden via Google kost maanden; zonder foto van een geprint figuur gelooft de printer het niet.
- **Ideeëntest:** (1) vroeg: nee, PrintPal en JointLab zijn er al maanden; (2) brede taak: nee, nis; (4) Bambu doet flexi al zelf. Volgens de test: **zwak tot dood**.

### Kans 3: zelf beweegbare modellen verkopen (Patreon, MakerWorld-licentie, Printables Store)
**Wat:** met onze eigen Click Joints Pro CC0-figuren beweegbaar maken en die als betaalde STL of als lidmaatschap met verkooplicentie aanbieden, zoals Flexi Factory, Cinderwing3D en Lucky 13 Toys.
- **Kopers:** het meeste bewijs van alle drie: Flexi Factory 7.377 en Cinderwing3D 6.306 betalers (GEZIEN); Lucky 13 Seller License $25 en $50 per maand (`afkijken-2-2026-11-21/doorlopend/2026-11-22-lucky13-toys.md`).
- **Prijs nu:** $10 per maand verkooplicentie (Cinderwing3D), losse figuren 4,9 tot 8,4 op Printables (lat en `B-print-publiek.md`).
- **Concurrenten en zwakke plek:** Flexi Factory, Cinderwing3D, Lucky 13 Toys. Zwakke plek: nauwelijks; zij hebben jaren gratis toppers met 100.000+ downloads en duizenden "makes" (foto's van kopers).
- **Bouwen:** 1 tot 2 weken voor een eerste set (de tool hebben we al), maar elk model moet geprint worden voordat je er geld voor vraagt.
- **Euro per maand na 3 maanden (GOK):** €0 tot €50. Rekensom: van de betaalde Printables-modellen krijgt 3% ooit één beoordeling; Jopek haalt 122 betalers op 386.448 gratis downloads (±0,03%), en wij beginnen op 0 volgers. Lucky 13 gaf ±2,5 jaar alles gratis voor hij iets verkocht.
- **Grootste reden om te mislukken:** geen printer. Wij mogen niet zeggen dat het geprint is (besluiten 19 en 24 nov), en een betaald model dat niet past geeft openbare slechte reviews. Ook de regel geen beelden die doen alsof het een print is.
- **Ideeëntest:** (1) vroeg: nee; (2) brede taak: ja voor de koper; (3) kassa: ja (Printables Store, Patreon); harde nee op 8 voor ons: het kan wel, maar niet zonder printer.

## 6. Ranglijst
| Plek | Kans | Euro per maand na 3 maanden (GOK) | Bouwen (GOK) | Ideeëntest |
|---|---|---|---|---|
| 1 | Click Cuts voor OrcaSlicer (plugin) | €4 tot €240, middenschatting ±€75 | 4 tot 6 weken | overlever, cijfer 4 van 10: enige kans die door wet 1 komt en het beste bereik heeft (trendlijst hub); twijfel: geen kassa en openbare code, delen op de plaat niet te testen op Windows en Mac, gratis namaak |
| 2 | Website STL naar gewrichten | €0 tot €300, middenschatting ±€60 | 5 tot 8 weken | zwak: niet vroeg, gratis alternatieven van Bambu en PrintPal, ons voordeel (rig) valt weg |
| 3 | Zelf beweegbare modellen verkopen | €0 tot €50 | 1 tot 2 weken plus prints | dood zolang er geen printer is |

Ter vergelijking (DERDEN, issue #323): de nummer 1 in onze huidige hoek, Cleave, haalt ±150 verkopen per maand; plafond grofweg €2.000 tot €2.500 netto. Geen enkele route B-kans komt daar in 3 maanden in de buurt.

## 7. Advies
**Route B niet kiezen als de grotere markt.** Reden in één zin: printers betalen voor modellen en verkooplicenties, niet voor gereedschap; het gereedschap dat ze wel kopen (splitsen) verkoopt op het niveau van onze huidige markt, kost ons een herbouw buiten Blender, en verkoopt alleen met foto's van echte prints.

Eén uitzondering, alleen als route C ook niets groters vindt: **Click Cuts als gratis OrcaSlicer-plugin, als etalage voor Click Cuts, niet als eigen inkomen.** Na de keuring van C verwacht ik er zelf ±€75 per maand van (GOK), want de hub heeft geen kassa en de code is openbaar; de winst zit in bereik (de drukste plugins halen +1.200 tot +2.300 abonnees per week) en kopers die doorklikken naar Click Cuts op Gumroad of Superhive. Alleen beginnen als twee dingen eerst kloppen:
1. **De hoofdchat zoekt in de hub** (open punt hieronder) en er staat nog geen splitser voor je eigen STL.
2. **Een proef van 2 tot 3 dagen** laat zien dat we gesneden delen op de plaat krijgen (in de Linux-versie van Orca, met de omweg van OrcaCAD). Lukt dat niet, dan niet bouwen.
Kloppen beide: gratis versie bouwen (GOK 4 tot 6 weken), daarna 4 weken abonnees en doorkliks naar Click Cuts meten. Geen betaalde sleutel in de plugin bouwen: die is in openbare code met één regel weg te halen. Wacht niet lang met de zoekvraag: de hub groeide in 3 weken naar 227 plugins.

## Open punt voor de hoofdchat
**Zoek in de Orca Cloud-hub op "split", "cut", "connector", "dowel" en "joint"** (±2 minuten, alleen met een Orca Cloud-account; dat hebben wij niet, de API gaf Afkijker C `401 missing_authorization`). Een account maken is een nieuw account en dus aan Thijs (CLAUDE.md regel 4). De uitslag beslist of kans 1 nog een gat dicht. Ook handig om te noteren: het aantal abonnees van Embedder en van de drukste plugin in dezelfde hoek.

## Wat ik niet kon meten
- Aantal gebruikers van OrcaSlicer en installaties per plugin in de hub (GitHub dicht, hub-API niet gedocumenteerd).
- Aantal backers en bedrag van FlexySliceSTL op MakerWorld (403).
- Verkopen van flexi- en articulated-modellen op Cults3D (403).
- Leeftijd van TrestleFDM (©2026 op de site, eerste verkoopdatum niet in de Gumroad-data).
