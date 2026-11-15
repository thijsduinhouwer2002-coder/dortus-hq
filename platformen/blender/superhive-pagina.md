# Click Joints Pro: Superhive-pagina (Bram, sinds 10 nov 2026)

**DEMOFILM v1 TER KEURING (15 nov 17:30 UTC, Bram).** `ontwerp/click-joints/pro/film/click-joints-pro-demo.mp4` (20,6 s, 1920 x 1080, 30 fps, H.264, zonder prijs) en `.gif` (7,4 s, voor fora), echte beelden uit Blender 5.3.0. Nog niet uploaden: eerst Daans ja, dan release `click-joints-pro-film-v1` en dan als eerste preview op de pagina.

**KLAAR OM TE UPLOADEN (15 nov 15:30 UTC, Bram).** Release: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/click-joints-pro-v1.0.1
- Zip `click_joints_pro-1.0.1.zip`, sha256 `865f9482ea05993d59928a725452149badfb10b3551bf9d0297932e40f9bd813`, uit e2e-run 43729108508 op main: groen in de echte Blender 4.2.23, 5.2.3 en 5.3.0, zip inhoudelijk gelijk in alle drie. Manifest: Click Joints Pro, versie 1.0.1, id click_joints (nagekeken na downloaden uit de release).
- Plaatjes in uploadvolgorde, elk 1920 x 1080 PNG onder 2 MB: `1-poster-3.png`, `2-knie-met-boog.png`, `3-rood-voorbij-de-stop.png`, `4-kogel-passing.png`, `5-kogel-rood.png`. De maat van Superhive zelf heb ik niet kunnen nalezen (hun hulppagina's sturen met curl door naar de voorpagina), dus 1920 x 1080 zoals afgesproken.
- Daan: `Akkoord: ja` op Pro 1.0.0 (10 nov) en ja op de 1.0.1-kleuring (proef 5, 14 nov 06:35) en op poster 3 (14 nov 14:45). Op de poster staat "Blender 4.2 to 5.2"; dat klopt, maar 5.3 werkt ook (geen fout, kan later).
- Uploaden als concept, eerst aan Thijs laten zien, dan indienen (besluit 15 nov 16:20). Stappen onderaan dit bestand.

**INGEDIEND (15 nov 19:45 NL, ja van Thijs 19:36): status Pending. Superhive keurt in 3 tot 5 dagen en bericht in de Superhive-inbox. Tijdens de keuring kan niets aangepast worden. Na goedkeuring: lanceerprijs $9 voor 14 dagen, dan de lancering (Chris: BlenderNation, dortus.com-knop).**

**CONCEPT COMPLEET (15 nov 19:35 NL): zip, uitgelicht plaatje en 4 galerijplaatjes staan erop, varianten Personal $12 en Studio (up to 5 people) $45 met de zip, checklist "Complete". Wacht op ja van Thijs om in te dienen. Lanceerprijs $9 pas instellen als hij live is (dan lopen de 14 dagen vanaf de lancering).**

**CONCEPT AANGEMAAKT (15 nov ±17:40 NL, hoofdchat, in de Chrome van Thijs).** Superhive product 269495, slug `click-joints-pro`, status Draft. Ingevuld en opgeslagen: naam, prijs $12, support period aan (verlengen 25%), excerpt, beschrijving (tekst hieronder), categorie Addons met Modeling en Import & Export, 9 tags, GPL, Blender 4.2 tot 5.3, documentatie (installeren, de drie stappen, printtips, support) en 2 FAQ's. Nog te doen: uitgelicht plaatje, 4 galerijplaatjes en de zip. Superhive eist plaatjes van precies 2:1; de 16:9-plaatjes zijn bijgesneden naar 1920 x 960 (poster 60 px boven en onder, de rest 120 px onder; niets belangrijks weg, bekeken). Die uploads lukten nog niet: het Chrome-venster stond geminimaliseerd en de uploader werkt dan niet. Lanceerprijs $9 en de Studio-licentie ($45, via Variations) nog niet ingesteld. Indienen pas na het ja van Thijs.


Status (10 nov 10:40 UTC, Bram): tekst, prijs, licenties en uploadstappen definitief; poster 2 en Pro-zip-build klaar op de tak; uploadregel staat (als "nog niet") op de lijst van Thijs. Superhive-account van Thijs staat, makersaanvraag ingediend 10 nov 10:39 NL (keuring loopt). Nog nodig voor indienen: (1) winkelplaatjes met het ja van Daan (ronde 2 loopt, tak `claude/blender-pro-winkel`), (2) `Akkoord: ja` van Daan voor de Pro-zip bovenaan `producten/blender-gewrichten/ontwerp.md`, (3) de betaalde zip uit `maak_zip.sh betaald` na een groene test, (4) de makersaanvraag goedgekeurd. Prijs is een voorstel; Chris mag hem bijstellen.

## Instellingen
- **Naam:** Click Joints Pro (zo heet hij ook in Blender: de betaalde build zet naam, versie 1.0.0 en tagline "Click hinges with an end stop for 3D printed figures" in de manifest; id blijft click_joints)
- **Categorie:** Add-ons, Modeling / 3D Printing
- **Prijs (voorstel):** $12 gewone licentie, lanceerprijs $9 de eerste twee weken (GOK, ontwerp.md). Netto per verkoop van $12: 70% min $0,49 = ±$7,91.
- **Studiolicentie:** tot 5 personen, $45 (GOK; CatPin $80, Split-3DPrint $59, wij zijn kleiner en nieuwer).
- **Support Period (advies 7):** 12 maanden updates bij de koop, verlengen met 12 maanden voor 25% van de prijs. Na afloop blijft de gekochte versie gewoon werken.
- **Licentie:** GPL-3.0-or-later (code), zoals elke Blender-add-on.
- **Blender:** 4.2 LTS tot 5.3 (getest in 4.2.23, 5.2.3 en 5.3.0 op GitHub Actions; 5.3.0 erbij sinds 15 nov, run 43676633084 groen, ook de Pro-zip en de winkelplaatjes 13 en 14).

## Tekst (Engels, voor de pagina)

**Hinges that click and stop at 115°.**

Click Joints Pro adds a printable click hinge to your figures: a knee or elbow that bends from 0° to 115° and stops there, instead of flopping backwards. Place it on a limb, drag the pose slider, and you see the exact range in degrees before you print. Bend past the stop and the parts that collide turn red.

What you get:
- **Click hinge with an end stop**, for knees and elbows: measured range 0° to 115° on the hinge, shown as a degree arc around the axis.
- **Pose slider per hinge**: check the bend in the viewport. Exporting is not affected by the pose.
- **Green fit band**: the seam and the knuckle turn green when the hinge is placed, like the fit colour of the ball joints. A hinge is only placed when the fit is good.
- **Red past the limit**: the spots that hit turn red on both parts, so you know before you print.
- **Spacing checks**: hinges and ball joints too close together are refused with a clear message.
- **Everything from the free Click Joints**: ball joints with a fit colour, ±degrees, split into parts, export to STL or 3MF.

Good to know:
- Clearance 0.2 mm by default; print a test first, every printer is different.
- The free Click Joints (extensions.blender.org) and Pro can not be enabled at the same time. Disable the free one first; your settings stay in the .blend file.
- Pure Python, no extra add-ons needed.
- Support: https://github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com

## Na te kijken voor indienen
- Elke zin hierboven klopt met de code op main (controleur, zoals bij de gratis tekst). Getallen 115°, 0,2 mm en de weigermelding staan in de toetsen.
- Plaatjes alleen met wat de Pro echt doet (zie de punten van Daan; het script-groen op de proefposter mag niet zo naar de winkel).

## Uploaden (voor Thijs of de hoofdchat, pas na de vier punten hierboven)
Alleen Thijs kan inloggen; dit gaat als één regel op `organisatie/lijst-thijs.md` zodra Daan ja zegt.
1. Inloggen op superhive.market met het Dortus-account, naar het verkopersdashboard, "New product".
2. Naam, categorie en de Engelse tekst hierboven plakken (kop als eerste regel).
3. Prijs $12, lanceerkorting naar $9 voor 14 dagen; extra licentie "Studio (up to 5 people)" $45.
4. Support Period 12 maanden, verlengen 25%.
5. Bestand: `click_joints_pro-1.0.1.zip` uit de release (1.0.1: strakke kleuring, donkere veersleuf, gladde groene band; bijgewerkt 14 nov 08:35 Bram) op GitHub (sha256 staat in de release; de workflow bouwt hem en zet sha256 erbij).
6. Plaatjes in deze volgorde: poster 3 (`ontwerp/click-joints/pro/poster-3.png` op main, Daan ja 07:40 met vergrootglas), 13 (knie met boog), 14 (rood voorbij de stop), daarna 8 en 9 van de gratis versie (kogel); filmpje als eerste preview.
7. Opslaan als concept, kijken, dan indienen. Duur ±10 min.
