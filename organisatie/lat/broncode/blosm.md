# Broncode: Blosm (Blender-add-on, gratis plus Pro op Gumroad)

Uitgeplozen door de Afkijker, do 26 nov 2026 ±21:30 NL (issue #20). Code gelezen met `git clone --depth 1` in /tmp, niets uitgevoerd, daarna weggegooid. Waarom deze: Blosm verkoopt precies zoals wij op Gumroad (gratis versie met "pay what you want" plus een Pro), en is de Blender-add-on met de meeste beoordelingen die ik op Gumroad zag.

## Wie en hoeveel
- Repo's: https://github.com/vvoovv/blosm (2.180 sterren, alleen een README, GEZIEN zoek-API) en https://github.com/prochitecture/blosm (de code, laatste commit 18 nov 2026, versie 2.8.1, GEZIEN `blender_manifest.toml`). Maker: Vladimir Elistratov (Prochitecture), solo.
- Licentie: GPL-3.0-or-later (GEZIEN `LICENSE` en manifest). Alleen ideeën overnemen, geen code.
- Omvang: 345 Python-bestanden, ±61.600 regels (GEZIEN `wc -l`).
- **Gratis versie op Gumroad:** prijs €0, voorgestelde prijs €10 (pay what you want), **1.633 beoordelingen, gemiddeld 4,9, 94% vijf sterren** (GEZIEN, https://prochitecture.gumroad.com/l/blender-osm, JSON in de pagina).
- **Pro op Gumroad:** €17,80 voor 1 persoon; studio 2 tot 3 mensen +€21,30, 4 tot 10 +€85,40, 11 tot 20 +€241,80, meer dan 20 +€406,00, universiteit +€72,20; geen beoordelingen zichtbaar; geen terugbetaling (GEZIEN, https://prochitecture.gumroad.com/l/blosm). Download: 2 zips, samen 96 MB (GEZIEN `file_summaries`).
- **Niet op extensions.blender.org** (GEZIEN: niet in de 1.715 add-ons van https://extensions.blender.org/api/v1/extensions/). Elke gratis download loopt dus via hun eigen Gumroad-pagina.
- Issues: 708 in totaal, 96 open (GEZIEN, GitHub zoek-API op vvoovv/blosm).

## Wat ze slim doen (bestand en regels)
1. **De gratis pagina vraagt eerlijk om geld.** Tweede alinea: "You can enter zero in the price field to get the addon for free. We would appreciate a donation. However due to high fixed fees (80 cents for each purchase), it does not make sense to donate $1. Please consider a larger donation if you use the addon at work." Daarna meteen "Take look at the Pro version!" (GEZIEN, gratis pagina). Alles wat gratis wordt gedownload, belandt als koper op dezelfde winkel als Pro: beoordelingen en mailadressen komen bij hen, niet bij een ander platform.
2. **Prijs naar teamgrootte.** Zes varianten, van 1 persoon tot meer dan 20 plus universiteit (zie boven). Een studio betaalt tot €423,80 voor hetzelfde bestand.
3. **Eén code, twee uitgaven, met een slotje.** Pro of niet hangt alleen af van of de map `realistic` in de zip zit (`__init__.py` r. 34). In de gratis versie staat de Pro-keuze gewoon in de lijst als "[pro] buildings with more details" (`gui/__init__.py` r. 1074 tot 1076); kies je hem, dan komt een venstertje "This level of detail is available in the Pro version" met de knop "Get the Pro version!" (`__init__.py` r. 418 tot 430). In de voorkeuren staat bij gratis "Unlock more features with Blosm Pro!" en bij Pro "Thank you for purchasing the Pro version!" (r. 110 tot 116). De koopknop gaat naar hun eigen pagina prochitecture.com/blosm/pro/, niet direct naar Gumroad (r. 219 tot 229). Zelfde les als Blendkit.
4. **De zip wordt gekeurd vóór hij de winkel in gaat.** `tests/release_profiles.py` r. 40 tot 46 en 72 tot 90: manifest in de wortel, geen dubbele of onveilige paden, en de gratis zip mag geen enkele Pro-module bevatten. Reden staat in hun issues (hieronder, #523).
5. **De GitHub-README is een etalage.** Alleen twee grote beelden die naar de twee Gumroad-pagina's linken, de Pro-lijst, en "All customers will get the addon source code under GPL license!" (GEZIEN, README vvoovv/blosm).

## Wat gebruikers vragen of klagen (GitHub-issues, GEZIEN zoek-API)
- Bovenaan staan fouten van diensten buiten de add-on: "403 Error when Importing terrain (Premium add-on)" (#351, 62 reacties), Google 3D Tiles 403 (#356, 52; #363, 63). Niet ons soort product; wel weer de les van FLIP Fluids: een fout moet in de add-on zelf uitgelegd worden.
- Instellen is drempel: "A valid directory for a Blender file with materials for buildings isn't set" (#105, 26 reacties).
- Verkeerde zip geïnstalleerd: "Missing manifest" bij installeren, iemand pakte `blender-osm-info.zip` (#523, 13 reacties).
- Koper vindt zijn Pro-functie niet terug (#681, 15 reacties): versieverwarring tussen gratis en Pro.
- "GPL but no source?" (#89, 14 reacties): kopers verwachten de bron bij een GPL-add-on.

## Welk product van ons wordt er beter van
**Click Joints (gratis) en Click Joints Pro, de etalage op Gumroad, dortus.com/click-joints en de README van repo click-joints.**

Bij ons gaat het andersom dan bij Blosm. De gratis Click Joints heeft 406 downloads op extensions.blender.org (GEZIEN, Meter 26 nov 19:43) en 0 op Gumroad (GEZIEN, `organisatie/meten/stand.md`, 24 en 25 nov). De gratis Gumroad-pagina heeft al €10 voorgesteld (GEZIEN, https://duinhouwer8.gumroad.com/l/click-joints-free), maar de tekst vraagt nergens om een gift en zegt "Free, also on Blender Extensions". Pro en gratis staan op Gumroad allebei op 0 beoordelingen (GEZIEN). Gevolg: van ruim 400 mensen die de gratis versie hebben, kennen we geen mailadres en krijgen we geen beoordeling op de winkel waar Pro staat. De Gumroad-mail aan gratis kopers (27 nov) heeft daardoor bijna niemand om naar toe te gaan.

Idee (na de sale, niet nu): extensions.blender.org laten staan (155 downloads per week, onze grootste stroom), maar op dortus.com/click-joints en in de README de knop "Free download (pay what you want)" naar de gratis Gumroad-pagina eerst zetten en Extensions als tweede. Op die gratis pagina één eerlijke zin zoals Blosm: wie hem voor werk gebruikt, mag iets geven; en direct daarna Pro. Wat het oplevert is een GOK: elke gratis Gumroad-download geeft een mailadres en een kans op een beoordeling op onze eigen winkel. Studio-varianten boven 5 mensen zijn klein bij 2 verkopen; pas zinvol als de Meter studio-kopers ziet.

Al bij ons geregeld (geen werk): Pro zet de gratis versie zelf uit (#114, 1.2.9); de gratis zip 0.1.2 bevat geen enkel Pro-bestand (GEZIEN, `unzip -l producten/blender-gewrichten/uitgave/click_joints-0.1.2.zip`); het manifest van 0.1.2 wijst naar dortus.com/click-joints.

Bijvangst: de openbare README van repo click-joints zegt om 21:20 nog "Measured in Blender, not print tested by us yet" (GEZIEN, commit 55bbb30 van 20 nov), tegen besluit 24 nov 15:32 in. De nieuwe tekst staat klaar (`producten/blender-gewrichten/repo-click-joints/README.md`, Daan ja #160) en staat als punt 7 op de plaklijst van de hoofdchat.
