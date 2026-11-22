# BOOTH (booth.pm), Unity- en VRChat-tools

Onderzocht: 7 nov 2026, run 22:33 UTC, door Vera. Controleur akkoord, kleine correcties verwerkt.

## Advies: nog niet klaar. Cijfer 6.

Het sterkste signaal tot nu toe dat kleine makers met **code** (Unity-editortools en avatarsystemen voor VRChat) aandacht én geld halen. Bereik is gemeten (likes), verkoop alleen geschat. Uitbetaling buiten Japan kan (PayPal) en Engelse namen doen het bijna even goed. Wat nog ontbreekt: een betere verhouding tussen likes en verkoop bij tools (zie onderaan).

## Wat het is
BOOTH is de winkel van pixiv (Japan). De categorie 3Dモデル (avatars, kleding, tools voor VRChat) groeit hard. In de subcategorie 3Dツール・システム verkopen kleine makers Unity-scripts, editortools, shaders en avatarsystemen, meestal ¥500 tot ¥3.000. BOOTH rekent af.

## Hoe gemeten
- Lijst van de categorie, gesorteerd op nieuw, pagina 25 t/m 56 (1.920 items, 11 mei t/m 30 sep 2026). Per item de open JSON (booth.pm/ja/items/ID.json): publicatiedatum, prijzen per variant, likes (wish_lists_count). Robots.txt verbiedt dit niet.
- De controleur keek de randen na (pagina 24 en 57): de lichting is compleet, de lijst is op publicatiedatum gesorteerd.
- Scripts en data: `data/booth-haal-script.py`, `data/booth-analyse-script.py`, `data/booth-tools-2026-05tot09-2026-11-07.jsonl`.
- BOOTH toont geen verkoopteller. Likes zijn wel openbaar.

## Cijfers (tools gepubliceerd 11 mei t/m 31 aug 2026, nu 2 tot 6 maanden oud)
- GEZIEN, drukte: 1.341 tools uit 714 winkels, ±300 tot 430 per maand (jun 305, jul 428, aug 433). Groeit.
- GEZIEN, echt betaald (laagste prijs boven 0): 770 tools, mediaan **40 likes**, 30% 100+, 10,5% 500+. Mediaanprijs ¥500 (±$3,30).
- GEZIEN: 267 gratis tools met een betaalde steunvariant, 304 helemaal gratis (mediaan 32 likes).
- GEZIEN, top: lilSSRT (13.679 likes, ¥500 tot ¥1.300), Real Sweat System (9.204, ¥9.800), Expression Editor van mokonu (8.436, ¥1.000; dezelfde maker heeft ook BoneScanner met 4.348).
- DERDEN (paper NekoDOS1, VR-conferentie 2024, J-STAGE): aankopen zijn gemiddeld **36% van het aantal likes**, gemeten bij een paar makers (kleding en gimmicks). Steunvarianten bij gratis items leveren bijna niets op (5.000+ likes gaf ±¥50.000 in totaal).
- GOK met die 36%: de middelste betaalde tool verkoopt ±14 keer (±¥7.000, ±$45) in 2 tot 6 maanden. Bij 100+ likes (30% van de tools) ±36+ verkopen. Bij 500+ likes (1 op 10) ±180+ verkopen, ±¥90.000 tot ¥180.000 ($600 tot $1.200). Toppers duizenden verkopen.
- DERDEN (pixiv, BOOTH 3Dモデル 取引白書2026): de hele 3D-categorie had in 2025 ±¥10,4 miljard verkoopvolume (±$70 miljoen), +79% op 2024, 7,74 miljoen orders. Dat is de hele 3D-categorie, niet alleen tools. VRChat Inc. nam in sep 2026 geld op van pixiv.
- DERDEN (GameBusiness, BOOTH-aankondiging 834): kosten 5,6% + ¥45 per verkoop. De maker houdt dus ±85% bij ¥500 en ±94% bij ¥3.000.

## Voor
- Bereik voor nieuwe tools is goed: de middelste betaalde tool heeft 40 likes, en 1 op 10 komt boven 500.
- Lage kosten (±6%), BOOTH rekent af, markt groeit snel.
- Past bij ons: Unity-editortools en avatarsystemen zijn C#-code die Claude kan schrijven en testen. Duidelijke behoeften (niet-destructief werken met Modular Avatar, menu's, kleur en vorm aanpassen).
- Mokonu laat zien dat één maker meerdere tools met duizenden likes kan neerzetten.

## Tegen
- Verkoop is niet zelf te meten, alleen te schatten via likes (één bron, weinig makers, niet specifiek tools).
- Japanse markt: beschrijvingen, support en zoekwoorden in het Japans. Hoe goed Engelstalige makers het doen is niet gemeten.
- Lage prijzen (mediaan ¥500).
- Of BOOTH aan een Nederlandse maker uitbetaalt en wat Thijs daarvoor moet invullen, is nog niet uitgezocht.
- Openheid over AI: in de VRChat-gemeenschap ligt AI gevoelig (er loopt een discussie over AI-regels). Niet verstoppen.

## Wat we zouden bouwen (eerste idee)
Een kleine Unity-editortool voor VRChat-avatars, niet-destructief en werkend met Modular Avatar, in het Japans en Engels, ¥500 tot ¥1.000. Bijvoorbeeld een helper die een veelgevraagde handeling in één klik doet (de toppers zijn precies dat: menu's ordenen, botten selecteren, vormen passend maken).

## Vervolg in dezelfde run (22:57)
- **Uitbetaling buiten Japan:** GEZIEN (booth.pm/announcements/562): BOOTH betaalt winkels uit naar een PayPal-account als uitbetaaladres, ook buiten Japan (de melding gaat over winkels met een Thaise PayPal). Een buitenlandse maker kan dus uitbetaald krijgen. Nodig voor Thijs, als Hans ja zegt: een pixiv-account, een BOOTH-winkel en een PayPal-account koppelen (inloggen en gegevens invullen doet hij zelf). Wat BOOTH verder vraagt (adres, belasting) is nog niet gelezen; de hulppagina's laden via JavaScript.
- **Engelse namen:** GEZIEN uit dezelfde data: betaalde tools met een naam zonder Japanse tekens (129) mediaan 32 likes, 28% 100+, 10% 500+; met Japanse tekens (641) mediaan 41, 31% 100+, 11% 500+. Engelse namen doen het dus bijna even goed (lilSSRT, RQIConverter, Facial State Editor). Let op: veel van die makers zijn wel Japans en schrijven hun beschrijving in het Japans.

## Wat nog gemeten moet worden voor een ja
1. **Verhouding likes en verkoop bij tools:** meer makers zoeken die cijfers delen (note.com, X, Fanbox).

## Extra bron (geen tool)
- DERDEN (note.com, kg13, 5 apr 2026): een avatar van ¥800 verkocht op BOOTH 23 keer in 4,5 maand (¥14.500 bruto), en in de nieuwe VRChat Avatar Marketplace 85 keer in een maand. De markt in VRChat zelf kan dus voor sommige spullen meer opleveren dan BOOTH. Staat als nieuwe kandidaat in kandidaten.md.

## Herhaling 17 nov 2026 (nachtscan, run 01:31 NL): Blender-add-ons op BOOTH, cijfer 4 als tweede winkel

Vraag van de nachtscan: kunnen wij hier binnen een paar dagen iets betaalds neerzetten met wat we al hebben (Blender)? Dus niet Unity, maar Blender-add-ons.

**Hoe gemeten (GEZIEN, 17 nov, curl):** zoeken op "Blender アドオン", gesorteerd op nieuw, alle 25 pagina's (1.473 items), per item de open JSON. Add-on = naam met アドオン, addon, add-on, プラグイン of スクリプト en geen 3D-model (563 items). Ter controle ook alle items in 3Dツール・システム en ソフトウェア (breder filter). Data: `data/booth-blender-addons-2026-11-17.csv`, scripts `data/booth-blender-haal-script.py` en `data/booth-blender-analyse-script.py`.

**Cijfers, betaalde Blender-add-ons (GEZIEN):**
| Lichting | Betaald | Mediaan likes | 100+ likes | 500+ likes | Mediaanprijs |
|---|---|---|---|---|---|
| 2025 | 34 | 7 | 9% | 9% | ¥399 |
| jan t/m apr 2026 | 33 | 7 | 3% | 3% | ¥300 |
| mei t/m aug 2026 | 56 | 7,5 | 9% | 7% | ¥300 |
| sep t/m nov 2026 (nog jong) | 86 | 2,5 | 5% | 0% | ¥780 |
Breder filter mei t/m aug (n=94): mediaan 7,5 likes, 40% 10+, 12% 100+. Zelfde beeld.

- Aanbod stijgt hard: nieuwe Blender-add-ons per maand jan 14, apr 35, jul 27, okt 43, **1 t/m 16 nov al 61**. GOK: veel met AI gemaakt, zoals bij Elgato.
- Wat verkoopt is bijna alleen **VRChat-avatarwerk**: tussenvormen van shape keys naar FBX (tohawork, 800 likes, ¥1.500), shape keys overzetten (objet, 678, ¥1.500), kleding passend maken (amanoissui, 652, ¥1.000), lattice sneller (fujitsubox, 627, ¥500). Daaronder valt het snel weg: plek 5 heeft 100 likes.
- GOK met de 36% likes naar aankopen (paper NekoDOS1, zie boven): de middelste betaalde add-on ±3 verkopen in 3 tot 6 maanden, ±$6. De top 4 ±220 tot 290 verkopen, ±¥220.000 tot ¥430.000 ($1.400 tot $2.800).
- **Ons idee van plek 1 bestaat hier al twee keer:** Weight Doctor for Blender (aksk-studio, 19 jun 2026, ¥980, 18 likes, GOK ±6 verkopen) en een ウェイト監査アドオン die ontbrekende gewichten, som niet 1 en links-rechts-verschil telt (miyabix-tool, 16 nov 2026, ¥680). Een gewichten-checker alleen is dus niet bijzonder genoeg.
- **Concurrent voor Click Joints Pro 1.1 "Rig to Figure":** Pose to Print (zemia, 3 nov 2026, ¥3.500, 3 likes): figuur met rig omzetten naar een printbare miniatuur. Gemeld aan Ruben.
- 3D-printen is klein op BOOTH: "3Dプリント Blender アドオン" geeft 26 items.

**Tijd tot de winkel:** items van 16 nov staan binnen uren na hun publicatietijd in de zoeklijst (GEZIEN); een keuring vooraf vond ik nergens beschreven (GOK: geen, live binnen een uur). Thijs eenmalig: pixiv-account, BOOTH-winkel, PayPal als uitbetaaladres (booth.pm/announcements/562). Kosten 5,6% + ¥45 per verkoop. Openheid over AI: BOOTH vraagt AI-werk te melden, niet verstoppen.

**Oordeel:** kopers bestaan, maar voor een gewone nieuwe Blender-add-on zijn het er een handvol, tegen 46% 10+ verkopen in de skinning-hoek van Superhive. Waarde voor ons: een **tweede winkel** voor elke add-on die we toch maken, met een Japanse pagina, live in een uur. Een eigen product alleen voor BOOTH alleen als het VRChat-avatarwerk doet (shape keys, kleding passend maken). Cijfer 4.
