# Broncode: Blendkit (vroeger BlenderKit), gratis add-on met betaald abonnement

Uitgeplozen door de Afkijker op do 26 nov 2026 (±09:30 NL), voor issue #20. Code gelezen uit `git clone --depth 1` van https://github.com/BlenderKit/BlenderKit (laatste commit 3cfcbd7, 23 nov 2026, versie 3.21.7; niets uitgevoerd). Site, verkoopvoorwaarden en de openbare zoek-API met curl gelezen.

## Waarom dit project
- **13 miljoen downloads van de add-on via GitHub-releases** (GEZIEN, badge https://img.shields.io/github/downloads/blenderkit/blenderkit/total, 26 nov). Gratis plan 72.911 assets, Full Plan 152.670 assets (GEZIEN, https://www.blenderkit.com/, 26 nov).
- Het is het bekendste voorbeeld van **gratis in Blender, betalen voor meer**. Precies ons probleem: 393 gratis downloads van Click Joints, bijna niemand stapt over naar Pro (`organisatie/plan-tot-half-december.md`). En het is het enige grote open project met een eigen code voor **vragen om een beoordeling**, ons andere grote gat (Pro 0 beoordelingen, CatPin 85).
- Licentie: GPL-2.0 of later (GEZIEN, `LICENSE` en de kop van elk bestand). Code overnemen mag met hun copyrightregels; het idee nabouwen is het schoonst.

## Wat ze slim doen (bestand en regels)
1. **Het betaalde staat gewoon in de gratis winkel, met een slotje, en de vraag komt op het moment dat je het wilt.** Een Full Plan-asset zie je tussen de gratis. Sleep je hem de scène in, dan stopt het slepen en opent een venster: kop "This asset is included in Full Plan.", knop "Get Full Plan" (`asset_bar/asset_drag_op.py` r. 2207 tot 2220). In het detailpaneel staat op die plek in plaats van "Click / Drag from Here" de knop met een open slotje (`ui_panels.py` r. 3966 tot 3980). Geen reclameregel die er altijd staat: de vraag komt alleen als je het betaalde ding probeert te gebruiken.
2. **Drie teksten voor de koopknop, wisselend, en elke link zegt welke tekst en welke plek.** `unlock_options.py` r. 68 tot 91: "support", "now" en "join" ("Join thousands of artists. Your subscription funds the creators and keeps Blendkit open-source."). Per keer een andere dan de vorige (r. 106 tot 113). De link krijgt `ab_variant=<tekst>` en een utm-plek mee, bijvoorbeeld `asset_unlock_drag` of `asset_unlock_panel` (`paths.py` r. 155 tot 167). Zo weten ze welke zin en welke plek kopers oplevert.
3. **Vragen om een beoordeling: alleen aan wie veel gebruikt, pas na een tijd, met een rustpauze, en alleen waar het telt.** Hele bestand `rating_nudge.py` (319 regels), getallen bovenaan (r. 46 tot 57):
   - pas 30 minuten na het downloaden (`NUDGE_DELAY_MINUTES = 30`), dus als je het al gebruikt hebt;
   - alleen bij wie 50 of meer downloads in 7 dagen heeft; makers die zelf iets uploadden al vanaf 5;
   - daarna 3 dagen niets (makers 1 dag);
   - alleen voor assets met minder dan 3 beoordelingen: daar doet een beoordeling het meest;
   - nooit voor wat je zelf maakte, al beoordeelde, of niet mocht downloaden (r. 165 tot 184);
   - alles blijft op de computer van de gebruiker, er gaat niets naar de server (r. 30 tot 31);
   - het venster is het gewone beoordelingsvenster met een vriendelijke zin "How do you like this asset? Please help us by rating." en een vinkje in de voorkeuren "Ask me to rate downloaded assets" (`__init__.py` r. 2598 tot 2602).
4. **Tips bij het starten als balk die vanzelf verdwijnt.** Bovenaan het 3D-scherm een smalle balk met een tip en link, weg na 8 seconden (`disclaimer_op.py` r. 272, `fadeout_time=8`), uit te zetten in de voorkeuren ("Show tips when starting Blender"). Tips staan in `global_vars.py` r. 91 en verder, bijvoorbeeld "Ratings help us distribute funds to creators." Ze leggen dus uit waarom een beoordeling helpt.
5. **De README zegt in één zin wat gratis is en wat betaald** (`README.md` r. 22): gratis zonder account, gratis account voor bladwijzers en beoordelen, Full Plan voor 150.000+ assets.

## Wat gebruikers vragen of klagen
De issues op GitHub kan ik niet lezen: projecten buiten onze repo's geven 403, ook met curl (zelfde als vorige runs). De add-on staat niet op extensions.blender.org (zoeken op "blenderkit" geeft niets, GEZIEN), dus daar zijn geen reviews. Uit de code zelf blijkt wel waar ze last van hadden: elke vraag-functie heeft een vinkje om hem uit te zetten (tips, aankondigingen, beoordelen), en de beoordelingsvraag is met een rustpauze en een drempel gebouwd. Dat wijst op klachten over opdringerig (GOK, niet gezien in issues).

## Bijvangst: Blendkit verkoopt ook add-ons, en daar staan al vier knip-voor-print-add-ons
- **Voorwaarden voor betaalde add-ons** (GEZIEN, https://www.blenderkit.com/add-ons-upload-beta/, 26 nov): maker krijgt 75%, plus 4% betaalkosten en $0,50 per verkoop. Tot nader bericht verkoopt Blendkit alle betaalde add-ons met 15% korting die Blendkit zelf betaalt. Een paar keer per jaar sale, meedoen mag je kiezen. Kopers vinden en installeren de add-on vanuit Blender zelf.
- **1.209 add-ons in hun zoekindex** (GEZIEN, `api/v1/search/?query=asset_type:addon`, 26 nov). Beoordelingen zijn zeldzaam: de bovenste tien op downloads hebben er 1 of 2 (GEZIEN).
- **Knippen voor 3D-print, allemaal nieuw in de laatste vier weken** (GEZIEN, zoek-API, veld `created` en `basePrice`): Print Ready Modelling Kit ($24, 26 okt), Printwright ($19, 2 nov), RegoSplit ($24, 13 nov), BedSplit met zwaluwstaart en deuvels ($22, 16 nov). Alle vier 0 beoordelingen. Voor gewrichten: alleen "Bevel Joints" ($17,85, iets anders: lassen van meshes) en "Dovetail Key" ($15). **Een add-on die een figuur beweegbaar maakt staat er niet** (GEZIEN, zoeken op "joint" geeft 3 treffers, geen enkele voor figuren).
- Verkoopcijfers per add-on toont de API niet. Hoeveel er daar verkocht wordt: onbekend.

## Wat wordt er bij ons beter van
1. **Click Joints gratis (direct-zip van dortus.com, Gumroad, Superhive Lite): de weg naar Pro op het moment dat iemand het wil, niet alleen onderaan.** Nu staat sinds 0.1.2 één vaste regel onder in het paneel (#115). Les 1: als iemand een mesh met een armature kiest, of meer dan één gewricht in één figuur zet, is dat het moment voor "Pro reads your rig: whole figure in one click". Alleen in de direct-zip; de versie op extensions.blender.org blijft zonder (hun regels).
2. **Elke link in de add-on naar een winkel krijgt een utm met de plek.** Nu zonder: `click_joints/betaald/__init__.py` r. 152 tot 153 (Superhive en Gumroad, kaal). De Meter ziet bij de ene verkoop "herkomst direct, geen utm" (`organisatie/meten/stand.md`). Met `?utm_source=blender&utm_content=paneel` (of `beoordeling`, `gratis-regel`) weet de Meter of kopers uit Blender zelf komen. Of Gumroad en Superhive utm in hun verkoopcijfers tonen: GOK, eerst nagaan.
3. **De beoordelingsvraag van Pro 1.2.9 (#100) zit al dicht bij Blendkit** (pas na Good fit en export, weg na een klik). Wat Blendkit nog meer doet: een paar minuten wachten in plaats van meteen, en een vinkje in de voorkeuren om het uit te zetten. Klein, voor na de sale.
4. **Click Cuts en Click Joints Pro op Blendkit als derde winkel.** 75% voor ons, koper vindt het in Blender, vier knip-concurrenten van hooguit vier weken oud zonder beoordelingen, en voor gewrichten niemand. Een account maken mag alleen Thijs; gemeld bij de hoofdchat.
