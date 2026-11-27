# Route B: ons vak naar printers zonder Blender (Afkijker B, 27 nov 2026)

Opdracht: issue #323, route B. Alleen onderzoek, niets gebouwd. Alles gelezen met `curl` op 27 nov 2026 tussen ±21:00 en 22:15 NL, tenzij anders vermeld. Niets geplaatst, niemand benaderd, geen account gemaakt.

**Kort antwoord.** Route B is geen grotere markt voor ons, in elk geval niet als hulpmiddel (tool). Het publiek is wel 30 keer groter dan Superhive, maar het geld van printers gaat naar modellen en verkooplicenties, niet naar gereedschap. De tools die er verkopen, verkopen op het niveau van Cleave of lager (TrestleFDM 268 verkopen à $12, JointLab 20+). Slicers, Bambu en losse sites geven splitsen, verbinders, een tolerantietest en zelfs flexi-figuren al gratis weg. En alles in die wereld verkoopt met foto's van echte prints, die wij niet hebben (Thijs heeft geen printer, besluit 25 nov 23:01). De enige echt nieuwe deur is de **pluginwinkel van OrcaSlicer, open sinds 7 nov 2026**. Daar staat nog geen splitser voor je eigen STL. Dat is kans 1, maar ook die schat ik op hooguit een paar honderd euro per maand na 3 maanden.

## Hoe gezocht (voor de keurder)
- Ruwe pagina's opgeslagen in de werkmap van deze run, niet in de repo. Opnieuw te doen met dezelfde `curl`-adressen hieronder.
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
- **De API leest het model alleen**: "orca.host ... gives plugins read-only access ... nothing here mutates the model" (GEZIEN, `developer_reference/plugin_development/api_reference/host.html`). Toch zetten plugins nieuwe delen op de plaat: OrcaCAD ("Send to plate drops the STL into the plater", r/BambuLab 18 nov) en Holes Fixer ("every affected plate is duplicated with the fixed parts", r/OrcaSlicer 25 nov, **186 punten**, 10 reacties) (GEZIEN, Arctic Shift id 1xzaeiy en 1y545ri). Hoe precies: niet gedocumenteerd (GOK: via een bestand dat Orca inleest).
- **Geld:** in de inhoudsopgave van de Orca Cloud-wiki staan alleen "Donation Links" bij je profiel, geen prijs per plugin (GEZIEN, https://cloud.orcaslicer.com/wiki/). Meshy verdient wel: plugin gratis, splitsen en maken "need a Pro plan or higher" bij Meshy zelf (GEZIEN, Meshy-docs). Dus: gratis plugin in de hub, betalen via eigen kassa (Gumroad-sleutel) kan; betalen in de hub zelf: GOK nee.
- **Drukte:** van de 100 nieuwste posts in r/OrcaSlicer (13 tot 27 nov) gaan er 15 over plugins (GEZIEN, Arctic Shift). Spoelhouder, printermonitor, Blender-brug, gaten-fixer, installatie zonder Orca Cloud ("Pluginator", 84 punten: niet iedereen wil inloggen). **Een splitser of gewrichten-plugin voor je eigen STL zag ik er niet tussen** (alleen Meshy, voor eigen Meshy-modellen).
- **Bambu Studio en PrusaSlicer:** geen pluginsysteem gevonden (GOK, gezocht op "Bambu Studio plugin support"; alleen nieuws over printerkoppelingen). Een plugin bereikt dus alleen wie OrcaSlicer 2.5 gebruikt en inlogt. Hoeveel dat er zijn: ONBEKEND (GitHub dicht in deze sessie); r/OrcaSlicer is 28 keer kleiner dan r/BambuLab (7.703 tegen 217.767, DERDEN).

## 5. De 3 sterkste kansen

### Kans 1: "Click Cuts voor OrcaSlicer" (plugin, eigen STL op je bed laten passen)
**Wat:** een Pages-plugin in OrcaSlicer: kies je printer (komt uit het Orca-profiel), één knop, het model wordt in delen gesneden die op het bed passen, met pennen of magneetgaten, nummers op de delen, en de Fit test strip. Gratis in de hub met vlakke sneden en pennen; Pro-sleutel via Gumroad voor automatisch splitsen, magneten, nummers en passing per materiaal. Dat is precies het gat uit deel 2 punt 1, en ons voordeel uit `organisatie/lat/click-cuts.md` ("één knop en alles past op jouw bed").
- **Kopers:** ONBEKEND hoeveel Orca 2.5-gebruikers er zijn. Wat wel vaststaat: 2.501 mensen kochten Split3r (GEZIEN), 268 kochten TrestleFDM (GEZIEN), Holes Fixer haalde 186 punten in een sub van 7.703 leden (GEZIEN). GOK: 1.000 tot 3.000 installaties in 3 maanden.
- **Prijs nu:** $12 (TrestleFDM), €60 tot €95 (Split3r), $150 per jaar (LuBan) (alle GEZIEN).
- **Concurrenten en zwakke plek:**
  1. *De eigen Cut tool van Orca* (gratis): niet automatisch, één vlak tegelijk, geen nummers, geen bed-check (forumantwoord "no fully automatic").
  2. *Split3r* (€60 tot €95): apart programma naast de slicer, duur voor een hobbyist.
  3. *TrestleFDM* ($12): apart programma, alleen Windows en Linux, gericht op minis; heeft wel organisch snijden en een passingbalkje, dus inhoudelijk sterk.
  Ook: 3D Splitter (gratis, maar buiten de slicer) en Meshy (alleen eigen Meshy-modellen).
- **Bouwen:** GOK 3 tot 4 weken. Onze code is Blender (bpy en bmesh); in Orca moet het met gewone Python-pakketten (bijvoorbeeld trimesh en manifold3d via `uv`), dus de snij- en verbindercode opnieuw schrijven, plus een html-paneel. Testen: Orca heeft een Linux-versie (flatpak, GEZIEN in de downloads van 2.5.0), maar of die in onze cloud zonder scherm te draaien is: GOK. Mac en Windows kunnen we niet zelf testen.
- **Euro per maand na 3 maanden (GOK):** 2.000 installaties x 3% koopt Pro x $15 = 90 kopers in 3 maanden, ±$1.350; in maand 3 ±40 kopers = ±$600, ±€550 bruto (wisselkoers GOK $1 = €0,92). Na kosten van Gumroad ±€480. Bandbreedte: €100 tot €700. 3% is GOK, ongeveer wat een gratis-naar-betaald stap bij tools haalt; wij zelf hadden 375 gratis downloads en 1 verkoop (`organisatie/lat/click-joints-pro.md`), dus 3% kan ook veel te hoog zijn.
- **Grootste reden om te mislukken:** iemand zet er gratis een in de hub (de hub staat vol hobbyisten die alles gratis delen) of Orca bouwt het zelf in (open source; ze voegden in 2.4 al meerdere dovetails toe). Daarna: de plugin bereikt alleen Orca-gebruikers die inloggen, niet de grote groep in Bambu Studio.
- **Ideeëntest, vier wetten:** (1) vroeg: ja, hub 3 weken oud; (2) brede basistaak: half, groot printen doet niet iedereen; (3) kassa: niet in de hub, wel eigen Gumroad-sleutel zoals Meshy; (4) platform bouwt het zelf: risico middel.

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
- **Euro per maand na 3 maanden (GOK):** 1.000 accounts in 3 maanden (JointLab-tempo is ±540 per maand, rekensom 18 x 30) x 2% betaalt x $9,99 = ±$200, ±€185 per maand. Bandbreedte €0 tot €400.
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
| 1 | Click Cuts voor OrcaSlicer (plugin) | €100 tot €700, middenschatting ±€480 | 3 tot 4 weken | overlever, cijfer 5 van 10: enige kans die door wet 1 komt; twijfel: gratis namaak en kleine bereikbare groep |
| 2 | Website STL naar gewrichten | €0 tot €400, middenschatting ±€185 | 5 tot 8 weken | zwak: niet vroeg, gratis alternatieven van Bambu en PrintPal, ons voordeel (rig) valt weg |
| 3 | Zelf beweegbare modellen verkopen | €0 tot €50 | 1 tot 2 weken plus prints | dood zolang er geen printer is |

Ter vergelijking (DERDEN, issue #323): de nummer 1 in onze huidige hoek, Cleave, haalt ±150 verkopen per maand; plafond grofweg €2.000 tot €2.500 netto. Geen enkele route B-kans komt daar in 3 maanden in de buurt.

## 7. Advies
**Route B niet kiezen als de grotere markt.** Reden in één zin: printers betalen voor modellen en verkooplicenties, niet voor gereedschap; het gereedschap dat ze wel kopen (splitsen) verkoopt op het niveau van onze huidige markt, kost ons een herbouw buiten Blender, en verkoopt alleen met foto's van echte prints.

Eén uitzondering, alleen als route C ook niets groters vindt: **Click Cuts als OrcaSlicer-plugin**, omdat die winkel 3 weken oud is en er nog geen splitser voor je eigen STL in staat. Dan klein beginnen: eerst de gratis versie in de hub (±2 weken bouwen), installaties meten, en pas een betaalde Pro-sleutel bouwen als er na 4 weken minstens 500 installaties zijn (GOK-drempel, rekensom: 500 x 3% x $15 = ±$225 per maand, het minimum waarvoor een tweede product de moeite is). Wacht niet lang: de hub vult zich snel (15 van de 100 nieuwste posts in r/OrcaSlicer gaan al over plugins).

## Wat ik niet kon meten
- Aantal gebruikers van OrcaSlicer en installaties per plugin in de hub (GitHub dicht, hub-API niet gedocumenteerd).
- Aantal backers en bedrag van FlexySliceSTL op MakerWorld (403).
- Verkopen van flexi- en articulated-modellen op Cults3D (403).
- Leeftijd van TrestleFDM (©2026 op de site, eerste verkoopdatum niet in de Gumroad-data).
