# Hero en logo in 3D (Daan, 14 nov 2026)

Afspraak met Mila (15:45 UTC): zij doet bibliotheek 600x900 en staand 748x896, ik hero 3840x1240 en logo 1280.
Script: `winkel3d.py` leest Mila's `../capsule-3d/capsule3d.py`, haalt de titel weg (hero) of laat alleen de titel staan (logo), en zet een eigen camera. Haar bestand blijft onaangeroerd; wat zij aan Gloop, ridder of hoeden verandert, komt vanzelf mee.

## Concept 1 (±16:00 UTC), `hero-concept1-1920x620.png`
Half formaat, 12 samples, `HERO_X=1.4 HERO_Z=1.95`, lens 26. GEZIEN met Read.
- Goed: de grap van de capsule staat erin (ridder kijkt naar zijn eigen helm op Gloop), laarzen vrij van de onderrand, links ruimte voor het logo dat Steam erover legt.
- Nog niet goed (eigen oordeel): veel lege muur, vier fakkels op gelijke afstand lezen als behang, rechts naast de hoge hoed niets. De oude keuring (10 nov, punt 8) zei al: de hero mag rijker of dichter op Gloop.
- Volgende ronde: hoedenberg van gevallen helden rechts (uit `hoeden.py`), buitenste fakkels weg of op ongelijke hoogte, iets dichter op de groep (lens 30), dan op 3840x1240 met 24 samples. Daarna logo (`python winkel3d.py logo.png 2560 1410 32 logo`, verkleind naar 1280 breed), en een frisse kijker op allebei.

## Ronde 2 (±16:35 UTC), `hero-ronde2-3840x1240.png`
Vol formaat, 24 samples, `HERO_LENS=30 HERO_X=0.8 HERO_Z=1.75`. Proeven op half formaat (a tot e) GEZIEN met Read.
- Rechts naast Gloop nu de berg hoeden van gevallen helden, zoals in het spel: hoge hoed op het goud, daarnaast pan, emmer, kap, koksmuts, veermuts en de pet bovenop (hoeden 1,05, iets naar voren, weg van de wand). Proef a had ze los verspreid en de pet zweefde; b en c stapelen ze.
- Logo en veilig vak (DERDEN, https://partner.steamgames.com/doc/store/assets/libraryassets): Steam laat het logo kiezen uit linksonder, midden boven, midden of midden onder; in het midden zit een veilig vak van 860 x 380 dat nooit wordt bijgesneden. Daarom staat de groep nu rechts van het midden (HERO_X 0,8): linksonder is lege vloer voor het logo, en de gezichten van ridder en Gloop vallen in het veilige vak (op half formaat x 530 tot 1390, y 120 tot 500, nagemeten met een kader op proef e; aanname GOK: de maat geldt op het halve formaat 1920 x 620, zoals de sjablonen van derden het tekenen. Geldt hij op 3840 breed, dan valt alleen Gloop erin en schuift de ridder naar rechts). Logo dus linksonder kiezen.
- Fakkels: links één zwakkere boven de plek van het logo, rechts één hogere verder weg; geen behang van gelijke fakkels meer.
- Iets dichterbij (lens 30 in plaats van 26): minder lege muur.
- De punt van de heksenhoed en de laarzen vallen buiten het veilige vak; dat mag, het gaat om de gezichten en de helm.
- Nog te doen: frisse kijker op het volle formaat, logo (`python winkel3d.py logo.png 2560 1410 32 logo`).

### Frisse kijker op ronde 2 (agent, ±16:52 UTC): 7,5
"Mooie, warme achtergrond, links rustig voor het logo, de grap snap je." Eén moet: de punt van de heksenhoed valt boven het veilige vak uit en de mond zit tegen de onderrand; de groep moet ±25% kleiner. Kan: ridder omhoog laten kijken naar de helm, twee of drie hoeden meer op de toren, rand van de muntenplas losser, fakkel linksboven helemaal in beeld.
Geprobeerd: **ronde 2b** (`HERO_LENS=24 HERO_X=1.0 HERO_Z=1.6`, proef f en vol formaat GEZIEN met Read, met het veilige vak erop getekend). **Afgewezen, ronde 2 blijft de kandidaat.** Waarom: ook in 2b steekt de hoedpunt 40 px (half formaat) boven het vak uit, want de groep is hoger dan 380; passen kan alleen nog verder weg, en dan is de hero een lege muur met vier gelijke fakkels, precies wat ronde 1 fout deed. Steam vraagt dat de gezichten in het veilige vak staan; in ronde 2 staan beide gezichten, de helm op Gloop en zijn mond erin, alleen de punt van de heksenhoed en de kroon vallen bij een heel laag venster weg. 2b niet bewaard.
Niet gedaan: meer hoeden op de toren, want de toren komt uit Mila's capsule en moet daarmee gelijk blijven (in het spel draagt Gloop er 4, de rest ligt op de berg). Ridderblik omhoog en de muntenrand: volgende ronde, met Mila (het is haar opstelling).
