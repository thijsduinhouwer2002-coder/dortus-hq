# Click Joints (Blender): verspreidingsplan

Door Chris, 8 nov 2026 (run 13), op opdracht van Thijs (8 nov 18:33). Gemeten met een onderzoeker; steekproef zelf nagemeten met curl (awesome-blender, Discord, SnapSplit, dortus.com). Elk cijfer heeft een label: GEZIEN (zelf gemeten), DERDEN (bron met link) of GOK. De berichten voor r/3Dprinting en r/blender staan al in `lancering.md` (concept A en B, BlenderNation concept C); hier staat het hele plan.

**De belofte (overal gelijk, advies 23, overgenomen):** `See how far it bends, before you print.` Gratis op extensions.blender.org: kogel en pen snijden met speling in mm, passingkleur, gemeten bereik ("Bends ±20°"), rood voorbij de grens, STL en 3MF. Betaald op Superhive ($12): komt later, nog niet gebouwd.

**Voor wie:** mensen die figuren, actiefiguren, poppen met kogelgewrichten (BJD), miniaturen en flexi-modellen ontwerpen in Blender en printen.

## Stand vandaag (8 nov ±19:50 UTC, GEZIEN)
- Niet live: geen Click Joints in de API van extensions.blender.org, geen account van Thijs op extensions.blender.org of Superhive (lijst-thijs, "nu nodig").
- Daan: `Akkoord: nee` alleen omdat Thijs de winkelplaatjes nog niet zag. Add-on zelf klaar (main fa34cde9).
- dortus.com/click-joints/ geeft 404: de productpagina bestaat nog niet.
- Nog geen echte print. Wie print is open (advies 23 punt e).

**Niets plaatsen voordat:** de listing op extensions.blender.org live is (link met curl gezien) en Daan `Akkoord: ja` zette. Voor printplekken (r/3Dprinting, r/PrintedMinis, Printables) ook een foto van een echt geprint gewricht dat buigt.

## Drie vaste regels voor alle plekken
1. **AI eerlijk melden.** Elke tekst zegt dat AI-agents van Dortus de code schrijven en Thijs het werk stuurt. Een plek die door AI gemaakte projecten weert, slaan we over.
2. **Geen beloftes over printen die we niet zelf zagen.** Zolang er geen echte print is, staat er "not printed yet" of we kiezen een plek waar het om Blender gaat, niet om printen.
3. **Geen verwijzing naar de betaalde versie** op extensions.blender.org en in berichten die naar die listing linken (voorwaarden van de site, zie `platformen/blender/kandidaten-2026-11-07.md` sectie 18). Superhive pas noemen als het betaalde deel er is, en dan alleen op plekken die commercieel toestaan.

## De plekken, in volgorde

| # | Plek | Grootte | Wanneer | Wie | Mag het al? |
|---|---|---|---|---|---|
| 1 | Listing op extensions.blender.org (zoeken op de site en in Blender zelf) | ±1.000 tot 1.500 downloads per nieuwe add-on (GEZIEN 6 nov, Vera) | dag 0, na goedkeuring | Bram dient in (account Thijs nodig) | ja, de lancering zelf |
| 2 | dortus.com/click-joints/ | pagina bestaat nog niet (404, GEZIEN) | vóór dag 0 | Chris | ja, zonder Thijs |
| 3 | awesome-blender (GitHub), kopje "3D Printing" | 7.598 sterren (GEZIEN, zoek-API van GitHub, via onderzoeker) | op zijn vroegst dag 7, na eerste downloads en reacties | pull request onder het GitHub-account van Thijs, via de hoofdchat | ja: Hans besloot 8 nov 20:44 (advies 24) dat lijsten geen apart besluit nodig hebben, altijd via de hoofdchat of Thijs |
| 4 | r/blender | groot (GOK, geen eigen meting) | dag 1 (zonder print) of een dag na r/3Dprinting | hoofdchat of Thijs | ja: Hans liet de keus van de lanceerplekken aan Chris (advies 23, status overgenomen); plaatsen alleen via hoofdchat of Thijs, regels eerst in de browser |
| 5 | r/3Dprinting | eerder bericht over gewrichten-snijders 314 punten (GEZIEN, lancering.md) | pas met echte print | hoofdchat of Thijs | ja (advies 23, zie rij 4), alleen met print |
| 6 | Persmail aan CG Channel (rubriek "New CG software you may have missed") | onbekend; rubriek elke week, noemde op 25 okt een kleine nieuwe Blender-add-on (GEZIEN door onderzoeker, https://www.cgchannel.com/tag/arcbrush/) | dag 3 tot 5, na de meting van Reddit | alleen Thijs, mail vanaf thijs@dortus.com | **nee, besluit Hans nodig** |
| 7 | BlenderNation, gratis nieuws insturen | onbekend (GOK) | dag 3 tot 5, samen met 6 | Thijs of hoofdchat (formulier) | ja (advies 23, zie rij 4): gratis versie, nooit betalen |
| 8 | Printables.com, een printbaar voorbeeldmodel | miljoenen accounts (GOK op profielnummers tot ±4,4 miljoen) | pas met echte print | Thijs (account nodig) | **nee, besluit Hans nodig**, en eerst de richtlijnen in de browser lezen (403 met curl) |
| 9 | YouTube-makers: askNK, daarna PIXXO 3D en CG Boost | 3.630, 272.000 en 414.000 abonnees (GEZIEN door onderzoeker, kanaalpagina's) | na dag 14, als 1 tot 4 werken | alleen Thijs, één mail per maker | **nee**: een ongevraagde mail aan een maker valt onder "geen privéberichten aan vreemden"; alleen als Hans er uitdrukkelijk een uitzondering voor maakt |
| 10 | Persmail aan 80.lv | onbekend | samen met 6 | alleen Thijs | **nee**: zonder zeker nieuwsadres geen mail; daarna besluit Hans |

**De rij in tijd:** dag 0 listing live; dag 1 Reddit (r/blender zonder print, r/3Dprinting met print); dag 3 meting (sprong in downloads, reacties); dag 3 tot 5 BlenderNation en CG Channel; dag 7 of later awesome-blender; dag 14 meting en besluit over de rest. De keuring op extensions.blender.org kan dagen tot weken duren (Hans, lijst-thijs 18:45), dus dag 0 ligt niet vast. Tegen het tussendoel van 20 december (1.000+ gebruikers) is Click Joints geen kandidaat: ±1.000 tot 1.500 downloads per add-on is het gemiddelde over de hele levensduur (GOK op GEZIEN van Vera).

Volgens regel 2 van Thijs: naar de volgende plek alleen als de vorige gelukt is en er geen klacht of verwijdering kwam. Wordt een bericht verwijderd of komt er een waarschuwing: overal stoppen (regel 7). Per plek meet ik de sprong in downloads (API van extensions.blender.org, veld met downloads per extensie) twee dagen erna; een soort plek die niets doet valt af.

### 1. Listing op extensions.blender.org (zonder Thijs, behalve het account)
- Dit is de grootste bron: zoeken op de site en in Blender (Get Extensions). Tagline en beschrijving staan in `winkeltekst.md` run 4: `Ball joints for 3D printed figures that show their bend range` (61 tekens), en de beschrijving noemt articulated, poseable, ball joint, pin, clearance, STL en 3MF.
- Zoekwoorden blijven vrij: op 8 nov noemde geen extensie articulated, poseable of ball joint in naam of tagline (GEZIEN, run 4). **Nieuw gevonden:** SnapSplit staat op de site ("Cut and automate custom connector building for 3D prints", GEZIEN 8 nov) en in awesome-blender. Dat zijn lijmloze klikverbindingen om te grote modellen te splitsen, geen gewrichten die buigen. Geen naam in onze teksten (rol), maar onze beschrijving moet het verschil zelf zeggen: "joints that move", niet "connectors".
- Plaatjes: de poster van Daan als featured image, daarna buigen en paneel (lijst-thijs, wacht op ja van Thijs).

### 2. dortus.com/click-joints/ (zonder Thijs)
- Bestaat nog niet. Ik bouw hem in een volgende run, in de eigen map `click-joints/` van de repo dortus, zoals bij Rollwright en Bison & Flex: de belofte, de drie plaatjes, de knop naar extensions.blender.org (pas na goedkeuring), support thijs@dortus.com, privacy (de add-on stuurt niets over het netwerk; Bram bevestigt dat in het ontwerp). Geen Superhive-knop tot het betaalde deel er is.
- Waarom: de awesome-lijst en persmails hebben een nette pagina nodig om naar te linken, en het manifest kan een website noemen (GOK dat dit helpt bij vertrouwen).

### 3. awesome-blender (op zijn vroegst dag 7, via de hoofdchat of Thijs)
- Regels (GEZIEN, https://github.com/agmmnn/awesome-blender/blob/master/CONTRIBUTING.md): welkom zijn "Official or community-verified extensions listed on the Blender Extensions Platform"; geweerd: "Day-0 or untested repositories ... without ... an approved Blender Extensions listing". Over AI alleen "AI wrappers without a dedicated Blender integration" als spam; door AI geschreven code is niet verboden. Neutrale beschrijving, geen "best" of "ultimate", licentiebadge erachter.
- Leeft: laatste push 4 nov 2026, 0 open pull requests, veel pull requests van onbekenden samengevoegd (GEZIEN door onderzoeker).
- Er is al een kopje "3D Printing" met 3D Print Toolbox en Snapsplit (GEZIEN, README regel 202 tot 204). Wij komen daar als derde.
- Voorstel regel: `- [Click Joints](https://extensions.blender.org/add-ons/click-joints/) : Cuts ball and pin joints into a figure for 3D printing, with clearance in mm, and shows how far each ball joint bends before parts collide. ![][gpl]` (licentie GPL-3.0-or-later volgens het manifest, GEZIEN.)
- In de beschrijving van de pull request: "I made this" en dat AI-agents van Dortus de code schrijven.
- Waarom pas dag 7: de regel weert ook nieuwe projecten zonder "real-world testing" of "community adoption". Een afgewezen pull request onder de naam van Thijs kan als klacht tellen (regel 7) en dan stopt alles. Dus eerst downloads en reacties.
- Mag: Hans besloot bij advies 24 (8 nov 20:44) dat pull requests naar lijsten geen apart besluit nodig hebben. Mijn runs kunnen geen fork maken buiten onze repo's, dus het gaat via de hoofdchat of Thijs.

### 4 en 5. r/blender en r/3Dprinting
- Teksten, voorwaarden en volgorde: `lancering.md` (concept A voor r/3Dprinting met print, concept B voor r/blender). Reddit-regels zijn met curl niet te lezen (403, niet omzeild); de hoofdchat leest ze vlak voor het plaatsen in de browser en volgt flair en zelfpromotieregels precies.
- Zonder print: r/blender eerst, met de zin dat het nog niet geprint is. Met print: r/3Dprinting eerst, minstens een dag later r/blender.

### 6 en 10. Persmail aan CG Channel en 80.lv (besluit Hans nodig)
- CG Channel: adres news@cgchannel.com (GEZIEN door onderzoeker, contactpagina; "send us press releases or suggest news stories"). Regels over AI of zelfpromotie niet gevonden. 80.lv: in de broncode van de contactpagina staan editor@80.lv en andere adressen; welk voor nieuws bedoeld is, is niet te lezen (JavaScript). 80.lv schrijft wel over gratis Blender-add-ons (DERDEN, https://80.lv/articles/simplify-uv-unwrapping-with-this-free-blender-add-on).
- Een mail onder de naam van Thijs, dus alleen hij verstuurt (of niet). Concept:

> Subject: New free Blender add-on: Click Joints, ball joints for 3D printed figures that show their bend range
>
> Hi, I made Click Joints, a free Blender add-on on the Blender Extensions platform: <link>.
> It cuts a ball joint (or a pin) into a sculpted figure for 3D printing, with the clearance you set in mm, and right after the cut it shows how far the joint bends before the parts collide ("Bends ±20°"); past that limit the collision turns red. Export is STL or 3MF, one file per part. Blender 4.2 LTS and 5.2 LTS.
> Images: <link naar poster en winkelplaatjes op dortus.com/click-joints/>
> I haven't printed a full figure with it yet; fit and bend are measured in Blender. (Weglaten zodra er een echte print is, en dan de foto meesturen.)
> Honest note: the code is written by AI agents that my small studio Dortus runs; I direct the work and every version is tested automatically in real Blender.
> Thijs Duinhouwer, Dortus, https://dortus.com/click-joints/

### 7. BlenderNation
- Zie `lancering.md`: een gratis product insturen kost niets, commercieel € 25 (GEZIEN, https://www.blendernation.com/submit-news/). Alleen de gratis versie, nooit betalen, geen Superhive-link.

### 8. Printables (pas met echte print, besluit Hans nodig)
- Voorwaarden (GEZIEN door onderzoeker, https://www.prusa3d.com/page/printables-com-terms-of-service_231249/): de site is voor printbare modellen; verboden zijn dubbele uploads, kunstmatig likes of downloads opdrijven en ongevraagde commerciële berichten aan andere gebruikers. Geen verbod op een link naar een tool gevonden, maar ook geen toestemming; de richtlijnen gaven 403.
- Alleen als echt printbaar model met waarde op zich (een voorbeeldfiguur of testgewricht met de speling in de beschrijving), met één regel "made with Click Joints (free Blender add-on)". Geen losse reclame. Vraagt een account van Thijs.

### 9. YouTube-makers (na dag 14, besluit Hans nodig)
- askNK (3.630 abonnees, team@asknk.info, GEZIEN) is klein maar het adres staat open; PIXXO 3D (272.000, Blender voor printen) en CG Boost (414.000) zijn groot, adres achter een captcha (niet gelezen). InspirationTuts (51.500) en Jayanam (43.200) later (GEZIEN door onderzoeker).
- Eén korte mail per maker, onder de naam van Thijs, pas als er downloads en liefst een print zijn. Geen herhaalmail.

## Risico's en klaargezette antwoorden
- **AI-argwaan** (r/blender, BJD-wereld): bij een negatieve reactie op de AI-melding één kort eerlijk antwoord, geen discussie: "Fair point. It's tested automatically in real Blender 4.2 and 5.2 on every change, and it's free, so you can judge the result yourself." Daarna niet meer reageren.
- **"How is this different from other joint cutters?"** (het bericht met 314 punten was van een ander): "Most tools cut the joint; this one also measures how far the ball joint bends before the parts collide and shows the collision in red, so you can check it before printing." Geen namen van anderen.
- **Jong Reddit-account of weinig karma** kan door automatische filters vallen. De hoofdchat kijkt na het plaatsen met uitgelogd venster of het bericht zichtbaar is; zo niet, niet opnieuw plaatsen maar op de lijst van Thijs.
- **Afwijzing op extensions.blender.org:** dan gaat niets uit dit plan door; Bram verwerkt de reden.

## Ook bekeken, voor later
- MakerWorld (Bambu Lab) en Cults3D als plek voor een printbaar voorbeeldmodel naast Printables: pas met echte print, regels nog niet gelezen.
- Blender Today (Pablo Vazquez) laat nieuwe add-ons zien: nog niet gemeten.
- Een korte demovideo (10 tot 20 seconden, buigen tot rood) zou elke plek sterker maken; concept C vraagt er al om. Advies aan Bram en Daan, geen plek.

## Valt af (nu)
- **BlenderArtists, Released Add-ons:** nieuw account mag daar niet plaatsen tot het eerst meedoet (moderator, https://blenderartists.org/t/1655257); vergelijkbare print-add-on 88 keer bekeken, 0 likes (zie `lancering.md`).
- **awesome-3d-printing (2.080 sterren):** eist dat het project minstens 4 maanden bestaat en 100 sterren of berichtgeving door anderen heeft, en dat de pull request in eigen woorden is geschreven, niet door een agent (GEZIEN door onderzoeker, https://github.com/ad-si/awesome-3d-printing/blob/main/contributing.md). Op zijn vroegst maart 2027, en dan schrijft Thijs zelf.
- **r/PrintedMinis (161k, DERDEN, https://gummysearch.com/r/PrintedMinis, waarschijnlijk oud getal) en r/BJD (39k, DERDEN, https://gummysearch.com/r/BJD/):** de kern van de doelgroep, maar regels niet te lezen (403) en in de BJD-wereld is er argwaan tegen geprinte poppen (DERDEN, https://denofangels.com/threads/thoughts-about-3d-printed-dolls.663917). Later, met print en met de regels in de browser gelezen; dan opnieuw voorstellen.
- **Blender Community Discord (222.880 leden, GEZIEN) en 3DMeltdown (12.816, GEZIEN):** regels alleen voor leden te lezen, en meedoen vraagt een account van Thijs. Later.
- **r/blenderhelp, r/functionalprint, r/resinprinting:** voor hulpvragen, nuttige prints of het printen zelf, niet voor ontwerptools.

## Wat zonder Thijs kan (de ploeg doet het zelf)
1. Productpagina dortus.com/click-joints/ (Chris, volgende run voor Click Joints).
2. Zoekwoorden en beschrijving op de listing scherp houden, ook het verschil met klikverbindingen (Chris en Bram).
3. Na de lancering: downloads per dag uit de API, reacties lezen, antwoorden als concept in `berichten-geplaatst.md`.

## Wat Thijs (of de hoofdchat) doet, samen ±25 minuten (GOK)
Account extensions.blender.org (staat al op zijn lijst), r/blender of r/3Dprinting via de hoofdchat, BlenderNation-formulier, pull request awesome-blender (mag al, advies 24), en na besluit van Hans: persmail, later Printables en YouTube.
