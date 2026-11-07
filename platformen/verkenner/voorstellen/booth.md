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
