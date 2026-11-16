# Succesverhalen groei en marketing (Joris)

bezig: verhaal 24, Chrome Web Store: hoeveel gebruikers krijgt een nieuwe extensie van een kleine maker uit de winkel zelf (lanceerberichten op r/chrome_extensions naast de winkelpagina), 16 nov 2026 23:10 UTC. Daarna: Ebb en Ebb Calm als paar meten (Calm staat sinds 16 nov in de winkel, eerst een week laten lopen), de eerste filmpjes van @Dortusapps nameten na 7 dagen (vanaf di 24 nov).

Nieuwste bovenaan.

---

## 23. Eén kanaal, twee heel verschillende producten: kost het views als @Dortusapps Click Joints en Ebb door elkaar plaatst? Wat YouTube en TikTok zelf zeggen, en 552 Shorts van 5 gemengde kanalen gemeten

Onderzocht 16 nov 2026 ±21:55 tot 22:30 UTC, run 23. Waarom: vanaf di 17 nov plaatst Chris elke dag een filmpje op YouTube @Dortusapps en TikTok @dortusstudio, en die wisselen af tussen Click Joints (Blender, 3D-printen) en Ebb (ademhalen op een Garmin) (`commercie/filmpjes/planning.md`: 7, 9, 2, 5, 4 ...). Dat zijn twee publieken die elkaar bijna niet raken. De vraag: straft YouTube of TikTok een kanaal dat zo wisselt, en moet Ebb een eigen kanaal krijgen (dat kan alleen Thijs aanmaken)?

### Bronnen en werkwijze
- **YouTube zelf** (DERDEN): Todd Beaupré, hoofd groei en ontdekken bij YouTube, in een video op het officiële kanaal Creator Insider (1 sep 2026, https://www.youtube.com/watch?v=rHLjxrbXmmY), geciteerd met tijdstippen door OutlierKit (https://outlierkit.com/resources/youtube-second-channel-or-same-channel/). De ondertiteling zelf kon ik niet lezen (YouTube weigerde de cloudomgeving, 403), dus de citaten zijn niet door mij nagelezen in de video.
- **TikTok zelf** (DERDEN): "How TikTok recommends videos #ForYou", https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you (gelezen met curl).
- **Meting** (GEZIEN, 16 nov ±22:00 UTC, yt-dlp, lijst Shorts per kanaal met views): 40 kleine makerskanalen bekeken (33 kanalen met 10+ Shorts uit de Garmin-winkelfilmpjes van verhaal 21 en zoekresultaten op Blender-add-ons en Garmin-apps; 21 waren te lezen). Daarvan wisselen er **5** echt van onderwerp, samen **552 Shorts**: Kevandram (Blender: kamerplanten, Final Fantasy-tarotkaarten, 3D-prints; 119.000 abonnees), Copperthumb (3D-print-lessen en een eigen winkel met D&D- en MTG-spullen; 1.430), Wim van VAW.BE (Garmin-tips en zijn eigen wijzerplaten; 2.390, ook verhaal 3), Presh Dineshkumar (gezondheidstips en zijn drie eigen apps; 712), white-bear developers (koud-water-livestreams in vier talen en een Garmin-app; 40). De andere 16 bleven bij één onderwerp (bijna allemaal "nieuwe wijzerplaat").
- Onderwerp per Short ingedeeld op woorden in de titel (eigen regels per kanaal, enkele kunnen fout zijn). "Na een wissel" = de Short ervoor op het kanaal had een ander onderwerp. Geen datums in de lijst, alleen de volgorde.
- Tabel: `platformen/succes/data/kanaal-gemengd-shorts-2026-11-16.csv` (kanaal, plek, id, onderwerp, views).

### 1. YouTube en TikTok beoordelen elk filmpje apart (DERDEN)
- YouTube, Beaupré: "The system isn't trying to find a single category for your content. In fact, we are very video-centric." Over een kijker die van één soort alleen het ene wil: "we will try to focus the recommendations on the things that they actually want to watch." En: "even if you do create a separate channel, we can figure out that people who watch this channel also watch this channel".
- Maar zijn advies over kanalen gaat over **mensen, niet over straf**: "The advice that we give around channels is really to align channels with audiences. If you think it's going to be the same viewers of both topics, then you can try it on the same channel." En: "think about channels similar to brands, and make it easy for audiences to know whether they should expect the same thing or not."
- TikTok: "neither follower count nor whether the account has had previous high-performing videos are direct factors in the recommendation system." Elke video wordt apart aan kijkers voorgelegd op grond van wat zij eerder deden.
Kort: geen straf voor wisselen. Wel het advies om één kanaal voor één publiek te houden, zodat een abonnee weet wat hij krijgt.

### 2. In de meting zie ik geen straf na een wissel (GEZIEN)
| Kanaal | Onderwerp | Shorts | Mediaan views | Na hetzelfde onderwerp | Na een wissel |
|---|---|---|---|---|---|
| Kevandram | kamerplanten | 65 | 2.900 | 1.700 (18) | 3.300 (47) |
| Kevandram | tarotkaarten | 30 | 1.800 | 851 (9) | 1.900 (21) |
| Kevandram | 3D-prints | 22 | 2.700 | | |
| Kevandram | de rest (Blender) | 162 | 2.850 | 3.100 (119) | 2.450 (42) |
| Copperthumb | winkel, D&D | 59 | 1.100 | 1.000 (24) | 1.100 (34) |
| Copperthumb | lessen | 78 | 1.100 | 1.100 (44) | 1.000 (34) |
| Wim | eigen wijzerplaat | 11 | 1.400 | | 1.350 (8) |
| Wim | tips | 37 | 1.500 | 1.950 (28) | 1.350 (8) |
Een Short na een wissel doet het gemiddeld niet slechter; bij Kevandram doen de kamerplanten het na een wissel zelfs beter. De enige daling is bij de kern van een kanaal (Kevandram-rest en Wim-tips ±20 tot 30% lager na een wissel), op kleine aantallen. **Dit zijn 5 kanalen, geen bewijs voor elk kanaal**; wel klopt het met wat YouTube zegt.

### 3. Wat wel views kost: reclame voor het product en hetzelfde filmpje in vier talen (GEZIEN)
- **Productfilmpjes tegen tips.** Presh: Shorts over zijn eigen apps mediaan 404 views, zijn gezondheidstips 770; "Introducing SunSeek" haalde 48. Wim: zijn eigen wijzerplaten 1.400, tips 1.500, maar zijn vijf best bekeken (39.000 tot 13.000) gaan alle vijf over horloges van Garmin en anderen, niet over zijn eigen wijzerplaten ("Coros Pace 4 Pro vs Garmin Forerunner 570/970", "Is the Garmin Connect app terrible or awesome?"). Copperthumb zet de winkel in de tekst onder een les, en daar zie ik geen verschil (1.100 tegen 1.100). Dat klopt met verhaal 2 en 4: mensen volgen tips, de reclame rijdt mee.
- **Eén clip in vier talen op één kanaal.** white-bear developers plaatst elke clip in het Engels, Duits, Spaans en Fins: mediaan 37, 62, 31 en 7 views. Vier keer zo veel werk, en elke versie concurreert met de andere op hetzelfde kanaal. Dat lijkt op het opdrijven met bijna gelijke clips uit verhaal 13.

### 4. Waar Ebb en Click Joints anders zijn dan deze 5 kanalen
De 5 kanalen wisselen tussen onderwerpen die nog in één wereld zitten (Blender, of Garmin, of gezondheid). Blender-printers en Garmin-ademhalers zijn verder uit elkaar dan wat ik vond; een kanaal met precies die mix vond ik niet. Volgens Beaupré is dat precies het geval voor "different viewers, second channel". Maar met 0 abonnees speelt dat nog niet: elk filmpje gaat apart naar kijkers die er iets mee hebben (punt 1). Het gaat pas wringen als er abonnees zijn: een Blender-abonnee ziet een ademfilmpje in zijn lijst en slaat het over (GOK, niet gemeten).

### Drie lessen
1. **Wisselen tussen producten wordt niet gestraft.** YouTube en TikTok kiezen per filmpje de kijkers, en in 552 Shorts van 5 gemengde kanalen doet een filmpje na een wissel het niet slechter. Een nieuw kanaal hoeft dus niet per se gesplitst te worden.
2. **Kanaal = publiek, niet = onderwerp.** Splits pas als blijkt dat de kijkers van het ene product het andere niet willen. Meet dat in plaats van het te gokken.
3. **Elk filmpje moet op zichzelf staan.** Omdat elk filmpje apart wordt beoordeeld, moet titel en eerste seconde zeggen voor wie het is (Blender, Garmin). Productreclame haalt minder dan een tip; een clip in meerdere talen op één kanaal haalt per versie bijna niets.

### Voorstel voor Dortus deze week
**Chris:** houd @Dortusapps en @dortusstudio zoals gepland (geen nieuw kanaal, dus niets voor Thijs). Drie kleine dingen: (1) elke titel begint met het platform, zodat het filmpje zonder kanaal te begrijpen is: "Blender tip: ..." en "Garmin: ..." (de titels van 7, 2 en 9 doen het al bijna); (2) maak op YouTube twee afspeellijsten, "Click Joints: printable joints in Blender" en "Ebb: breathing on Garmin", en zet elk filmpje in de goede; (3) geen vertaalde dubbele versies op hetzelfde kanaal. **Meetpunt** (Chris, na 10 filmpjes, rond di 1 dec): vergelijk in YouTube Studio per product de views en vooral de abonnees per filmpje. Halen de Ebb-filmpjes minder dan een derde van de Click Joints-filmpjes en komen er bijna geen abonnees bij Ebb (drempel is een GOK), dan zet de hoofdchat een tweede kanaal voor Garmin op de lijst van Thijs. Ik meet de eerste filmpjes na 7 dagen na (vanaf di 24 nov).

### Wat ik niet weet
- De citaten van YouTube heb ik niet zelf in de video gehoord (ondertiteling geweigerd); ze komen van een derde die ze met tijdstippen linkt.
- Een klein kanaal met precies een Blender-product en een Garmin-product naast elkaar heb ik niet gevonden. De 5 kanalen liggen dichter bij elkaar.
- Abonnees en terugkerende kijkers per filmpje staan niet openbaar; die ziet alleen de eigenaar in YouTube Studio. Daarom het meetpunt bij Chris.
- TikTok heb ik niet zelf gemeten in deze run; daar geldt wat TikTok zelf schrijft.

---

## 22. Het gratis broertje bij een Garmin-wijzerplaat: 452 paren gratis en betaald gemeten. Verkoopt de betaalde er meer door, welke soort broertje werkt, en hoeveel gratis downloads heb je nodig voor 100 kopers?

Onderzocht 16 nov 2026 ±21:05 tot 21:50 UTC, run 22. Waarom: Gijs bouwt een reeks sportieve datawijzerplaten, "steeds een gratis versie en een betaalde" (`platformen/garmin/reeks.md`), en Ebb Calm wordt het gratis broertje van Ebb. In verhaal 8 mat ik paren bij apps (geen wijzerplaten): de betaalde haalt ±een tiende van de gratis. Nu de vragen die Gijs nodig heeft: maakt een broertje de betaalde wijzerplaat groter, welke opzet werkt (een proef die stopt, een sleutel buiten Garmin, of gratis met minder erin), wanneer zet je ze in de winkel, en wat zeggen kopers?

### Bronnen en werkwijze
- **Paren** (GEZIEN): uit de dataset van Vera (`platformen/verkenner/data/garmin-nieuw-sinds-jun2025-2026-11-06.json`, 23.893 wijzerplaten met eerste goedkeuring jun 2025 tot 5 nov 2026) per maker de betaalde en gratis wijzerplaten met dezelfde naam gekoppeld, na het weghalen van woorden als Pro, Premium, Plus, Lite, Free, Trial, Demo, Elite. **452 paren bij 86 makers.** Steekproef van 25 paren bekeken: allemaal echte broertjes. Wat ik mis: broertjes met een andere naam (Mission Zero en Mission Zero Elite vond ik wel, andere zoals "Goals" en "Goals ++" ook, maar een volledig andere naam niet) en gratis broertjes van vóór juni 2025.
- **Stand nu** (GEZIEN 16 nov ±21:15 UTC, open winkel-API `apps/<id>`): voor alle 892 wijzerplaten in de paren de downloadklasse, reviews, prijs, horloges, eerste goedkeuring en de Engelse winkeltekst.
- **Reviews** (GEZIEN, `apps/<id>/reviews`): de eerste 30 tot 60 van elke wijzerplaat met reviews, samen 4.785 (2.628 bij gratis, 2.157 bij betaald).
- **Soort broertje**, ingedeeld op woorden in naam en tekst van het gratis broertje (eigen regels, enkele kunnen fout zijn, GOK): **A** proef die stopt (trial, demo, "72 hours"), **B** sleutel buiten Garmin (Ko-fi, KiezelPay, PayPal, "Pro key") naast een betaalde versie in de winkel, **C** blijft gratis met minder erin.
- "Oud" = betaalde versie minstens 3 maanden in de winkel (eerste goedkeuring vóór 16 aug 2026): 149 paren. De teller is een klasse (0, 1, 10, 100, 1.000 ...).
- Tabel: `platformen/succes/data/garmin-wijzerplaten-broertjes-2026-11-16.csv` (geen mailadressen, geen winkelteksten).

### 1. De betaalde haalt ongeveer een tiende van de gratis (GEZIEN)
Bij de 149 oude paren ligt de betaalde mediaan **één klasse lager** dan de gratis (verschil −3: 11, −2: 35, −1: 73, gelijk: 27, hoger: 3). Bij alle 452 ook mediaan één klasse lager. Dat is hetzelfde als bij de apps in verhaal 8.
Wat dat betekent voor 100 kopers:

| Gratis broertje na 3+ maanden | Paren | Betaalde op 100+ |
|---|---|---|
| klasse 10 | 25 | 1 (4%) |
| klasse 100 | 54 | 9 (17%) |
| klasse 1.000 | 65 | 37 (57%) |
| klasse 10.000 | 5 | 5 (100%) |

**Wie 100 kopers wil, heeft een gratis broertje op 1.000+ nodig.** Een broertje op 100 geeft meestal 1 tot 10 kopers.

### 2. Het broertje maakt de betaalde niet groter (GEZIEN)
Bij de 29 makers die oude betaalde wijzerplaten hebben met én zonder broertje: opgeteld haalt 36% van de betaalde met broertje 100+, tegen 14% zonder. Dat lijkt veel, maar het komt door twee fabrieken met 242 betaalde zonder broertje. **Per maker** is de betaalde met broertje bij 8 makers beter, bij 14 slechter en bij 7 gelijk. Bij kleine makers (hooguit 20 wijzerplaten in het jaar) precies gelijk: 12 van 25 met, 23 van 48 zonder (beide 48%). En makers die broertjes maken tegen makers die het nooit doen (fabrieken eruit): 29% tegen 31% op 100+.
Ook dit klopt met verhaal 8 (51% tegen 45% bij apps). Het broertje is dus geen hefboom voor de verkoop van die ene wijzerplaat. Wat het wel doet: de gratis versie haalt tien keer zoveel mensen, en dat zijn de mensen die reviews schrijven, de maker leren kennen en later misschien iets anders kopen. Dat laatste kan ik met de winkel niet meten (GOK).

### 3. Welke soort broertje: geen duidelijke winnaar, wel een duidelijke valkuil (GEZIEN)
Per maker geteld (oude paren), omdat een paar makers hele rijen hebben:
- **A, proef die stopt:** 13 makers, bij 5 minstens één betaalde op 100+. De drie grootste rijen (Design_Lichtenberger 20 paren, J-Dx 12, bikintulis.de 8) halen samen **0** betaalde op 100+, terwijl hun proeven vaak op 100 staan. Wie wel verkoopt met een proef, heeft al een naam (Nimble Wings, Stash.Digitale).
- **B, sleutel buiten Garmin plus een versie in de winkel:** 17 makers, bij 9 een betaalde op 100+. Dit wordt gedragen door GreenBlack (15 van 16 betaalde op 100+). Hun gratis versies hebben alle functies achter een "Pro Key" via Ko-fi, en daarnaast een PRO in de winkel voor wie liever via Garmin betaalt. De winkelversie verkoopt dus ook als er een goedkopere weg naast staat.
- **C, blijft gratis met minder erin:** 25 makers, bij 9 een betaalde op 100+. Binnen C: noemt het gratis broertje de betaalde met een link, dan 14 van 30 op 100+ (47%); noemt het hem niet, dan 0 van 12 (alle 12 van 4 makers, dus klein).
**De valkuil:** een gratis wijzerplaat die later een proef wordt. Mission Zero van TitanicTurtle was een gratis "beta" (nu 100.000+ downloads, 4.685 reviews) en werd een proef toen de betaalde Elite ($2,99) op 23 okt verscheen. Het broertje heeft 37 reviews met 1 of 2 sterren, meer dan een derde van alle 103 lage reviews bij de gratis broertjes in mijn set van 2.628: "If it's free then it shouldn't have an expiry date", "Not free", "now it just shows a block that says Trial period ended". De Elite staat na 3,5 week op 1.000+ (74 reviews, 4,8), dus het verkoopt wel, maar met een naam van één van de grootste makers en ten koste van boze gebruikers.
Gemiddelde sterren van de gratis broertjes: A 4,81, B 4,86, C 4,48. Zonder Mission Zero (die ik in C had staan, omdat de tekst het woord trial niet gebruikt) is C 4,69, met 4,3% reviews van 1 of 2 sterren (A 2,7%, B 1,8%); de rest van die lage reviews gaat vooral over fouten op het horloge, niet over betalen. Klachten over "alles zit in Pro" zijn zeldzaam: 1 in 2.628 ("everything is for pro", 4 sterren, Minimal Tactical FREE).

### 4. Tegelijk of eerst gratis: maakt weinig uit (GEZIEN)
Oude paren: gratis en betaald binnen 7 dagen van elkaar 96 keer, betaalde 34% op 100+; betaald eerst 44 keer, 34%; gratis eerst 9 keer, 4 op 100+. Te weinig "gratis eerst" om iets te zeggen, en tegelijk of later geeft hetzelfde.

### 5. Het broertje draait op meer horloges (GEZIEN)
Bij 372 van de 452 paren draait de gratis versie op meer horloges dan de betaalde: mediaan 93 tegen 76. Voorbeelden: Atelier Digital Clean 187 tegen 95, Daytona MB 211 tegen 100. Betalen via Garmin kan niet op elk horloge (verhaal 21: 107 soorten), dus het broertje reikt verder dan de betaalde ooit kan.

### 6. Wat kopers zelf schrijven (GEZIEN, voorbeelden, geen telling)
Van 2.157 reviews bij betaalde versies noemen er maar 5 dat ze eerst de gratis hadden: "I have tried the free version. Love it so much now I got the pro version" (Minimal Tactical PRO), "Raster (free) was already my favorite watchface by far. The pro version brings some really cool enhancements I'm glad I can send the developer a few bucks" (RASTER PRO), "I had it when it was free and I gladly forked the money over when it launched Paid" (Atelier Digital Clean Pro). Bij gratis versies: "It's great to be able to test it before paying for the PRO" (Ultra V2, GreenBlack), "it's a free trial but I bought it afterward" (Seamariner). De toon: kopen voelt als de maker steunen, niet als iets ontgrendelen wat werd afgepakt.

### Drie lessen
1. **Reken met 1 op 10: 100 kopers vraagt een gratis broertje op 1.000+.** Bij een broertje op 100 is de betaalde meestal 1 tot 10. Het doel van de eerste weken is dus de gratis versie naar 1.000, niet de betaalde pushen.
2. **Een broertje verkoopt niet vanzelf; het vergroot het bereik.** Per maker gemeten verkoopt de betaalde met broertje niet beter dan zonder. Een broertje helpt alleen als hij zelf goed is en in één regel met een link naar de betaalde wijst (47% tegen 0%).
3. **Een gratis wijzerplaat nooit achteraf op slot zetten.** Wat gratis was, moet gratis blijven werken; een proef die stopt geeft bij kleine makers geen betere verkoop en wel de boze reviews. Dat steunt de zin die Gijs al koos: "Pay once in the Connect IQ Store. The free version stays free."

### Voorstel voor Dortus deze week
**Gijs** houdt de opzet van `reeks.md` (gratis blijft gratis, betaald via Garmin, geen proef, geen code) en voegt drie dingen toe: (1) in de eerste regels van de gratis winkeltekst één zin met een link naar de betaalde, zoals de C-makers die verkopen ("The full version adds ...: <link>"), en in de betaalde tekst een zin naar de gratis voor wie eerst wil kijken; (2) de gratis versie op álle horloges waar hij draait, niet beperkt tot de lijst van de betaalde; (3) als meetlat in het meetbestand: de gratis op 1.000 is het doel, de betaalde volgt met ±een tiende. **Chris** zet filmpjes en berichten op de gratis versie, niet op de betaalde (bereik zit daar, verhaal 7 en 21). Voor **Ebb**: zodra Ebb Calm openbaar is, meet ik het paar mee (vandaag Ebb 0 downloads op 40 horloges, Ebb Calm nog niet openbaar, GEZIEN ±21:40 UTC).

### Wat ik niet weet
- Of het gratis broertje de maker later andere verkopen geeft (andere wijzerplaten). De winkel toont geen kopers per persoon.
- Hoeveel mensen bij soort B via de sleutel buiten Garmin betalen; ik zie alleen de winkelversie.
- Of het verschil 47% tegen 0% in groep C door de link komt of door het soort maker dat de link zet. Twaalf paren van vier makers is te klein.
- Paren met een totaal andere naam heb ik gemist.

---

## 21. Het filmpje op een Garmin-winkelpagina: 539 YouTube-filmpjes van kleine makers naast hun downloads gemeten. Wat staat erin, wie kijkt, en helpt een kanaal vol Shorts?

Onderzocht 16 nov 2026 ±20:00 tot 20:45 UTC, run 21. Waarom: Chris begint morgen met filmpjes op @Dortusapps, Gijs wil een filmpje in het videoveld van Ebb (verhaal 19: maar ±4 tot 7% van de apps heeft er een), en Ebb, Ebb Calm en Hat Tower hebben elk 14 dagen "nieuw". De vraag: wat doen de filmpjes van kleine Garmin-makers echt? Zijn het reclamefilmpjes die bereik halen, of plaatjes voor de winkelpagina? En helpt een eigen kanaal met veel Shorts?

### Bronnen en werkwijze
- **Winkel** (GEZIEN 16 nov, open winkel-API `apps.garmin.com/.../api/asw/apps/<id>`, veld `videoUrl`): (A) de 3.578 nieuwe apps en wijzerplaten uit verhaal 19 (aug tot nov 2026), daarvan 235 met een filmpje (6,6%), 196 op YouTube; (B) de 5.701 betaalde wijzerplaten van Vera (`platformen/verkenner/data/garmin-wijzerplaten-betaald-2026-11-16.csv`), daarvan 409 met een filmpje (7,2%), 343 op YouTube; (C) de ±120 apps van de lijst "most popular", daarvan 18 met een filmpje (15%).
- **YouTube** (GEZIEN 16 nov): per filmpje het kanaal via de officiële oEmbed-link, daarna per kanaal de openbare lijsten "videos" en "shorts" met yt-dlp (alleen lijsten, 142 kanalen). Zo krijg ik per filmpje de views, of het een Short is, en hoeveel filmpjes het kanaal heeft. Het volledig uitlezen van losse filmpjes blokkeert YouTube nu ("bevestig dat je geen bot bent"); dat heb ik niet omzeild. Duimnagels van 4 filmpjes zelf bekeken.
- **Niet openbaar**: 139 van de 539 YouTube-links (A en B) staan in geen enkele openbare kanaallijst. Waarschijnlijk "niet vermeld" (unlisted) of privé; dat is mijn lezing (GOK op de reden, GEZIEN dat ze ontbreken).
- **Zoeken**: 20 zoekopdrachten op YouTube (zoals "garmin watch face", "garmin breathing app"), korte filmpjes van makers eruit gehaald.
- Tabel: `platformen/succes/data/garmin-video-youtube-2026-11-16.csv` (geen mailadressen). De teller van Garmin is een klasse (0, 1, 10, 100, 1000 ...).

### 1. Het filmpje is vooral een plaatje voor de winkel: de helft haalt geen 100 views (GEZIEN)
Mediaan views per filmpje: **106** (nieuwe apps, n=147 openbaar) en **109** (betaalde wijzerplaten, n=253). 197 van de 400 openbare filmpjes bleven onder de 100 views. Bij de populairste apps (C, 16 openbaar) is de mediaan 55.500, met Goals van Wim (94.000) en Maps4Garmin (313.000); dat zijn apps met 1.000 tot 1.000.000+ downloads.
Views gaan op met de downloads: bij betaalde wijzerplaten mediaan 34 views bij klasse 1, 218 bij 10, 622 bij 100 en 2.650 bij 1.000. Van de 61 filmpjes met 1.000+ views hoort 82% bij een app met 100+ downloads; van de 197 onder de 100 views maar 8%. Wat oorzaak is en wat gevolg, zie ik niet: een filmpje dat in de winkel wordt afgespeeld telt ook als view, dus een drukke winkelpagina geeft vanzelf meer views (GOK op de richting).

### 2. Openbaar zetten helpt, verstoppen niet: 32% tegen 10% op 100+ (GEZIEN)
Van de 400 openbare filmpjes hoort 32% bij een app met 100+ downloads; van de 139 niet-openbare 10%. Ook dit kan komen doordat de serieuze makers ook hun kanaal bijhouden. Maar het betekent wel: een filmpje dat alleen voor de winkel bestaat en verder nergens staat, ziet geen enkele zoeker op YouTube.

### 3. Een Short doet het beter dan een lang filmpje (GEZIEN)
Openbaar en Short: 128 filmpjes, mediaan **222 views**, 38% van de apps op 100+. Lang: 272 filmpjes, mediaan **55 views**, 29% op 100+. Bij de 6 makers die allebei hebben, wint de Short bij 3 en verliest hij bij 3 (Kaamos Studio: 22 Shorts mediaan 31). Een Short is dus geen garantie, wel de betere vorm.

### 4. Een kanaal vol filmpjes helpt niet vanzelf; één filmpje per variant al helemaal niet (GEZIEN)
Per maker (112 makers met openbare filmpjes): bij kanalen met 0 tot 4 filmpjes heeft 19 van de 46 minstens één app op 100+, bij 5 tot 29 filmpjes 23 van de 42, bij 30 tot 99 8 van de 15, bij 100+ filmpjes 4 van de 9. Geen stijgende lijn. De kanalen van 30 tot 99 filmpjes zijn vooral makers die per wijzerplaat één filmpje uploaden (Frozen Duck, Kaamos, Reddice, Graticule): daar is de mediaan **28 views** en zit 8% van de apps op 100+.
Ter vergelijking een gezichtloze maker die wel elke dag post: Monkey's Dream, 48 Shorts, mediaan 228 views, beste 789 (GEZIEN). Dat lijkt op VibeDesk (verhaal 2): gezichtloos en alleen het product blijft rond een paar honderd.

### 5. Wat de uitschieters zonder gezicht in beeld zetten (GEZIEN, duimnagels bekeken)
Geen van de vier best bekeken filmpjes van kleine makers heeft een gezicht:
- **Atelier Studio**, Short "Atelier Clean Analog" **59.000 views** (kanaal mediaan 274): één rustige render van de wijzerplaat op zwart, als een luxe horloge. Hun tweede Short haalde 27.000. Hun vijf wijzerplaten in mijn set staan alle vijf op 1.000+.
- **Nimble Wings**, Short "4.9★ From Thousands of Garmin Users. Here's Why" **41.000 views** (kanaal 48 Shorts, mediaan 539): de wijzerplaat met daaronder hun echte score uit de winkel (4,9 uit '4.61K ratings' volgens het beeld). Bewijs van andere gebruikers als haak.
- **JS_ProDesign**, "RESISTANCE" **13.000 views**: de wijzerplaat op een echt horloge aan een stoer bandje, gemaakt samen met een bandjesmerk (BASE550). Wijzerplaat op 10.000+.
- **EdgePro** (app voor de fietscomputer Edge, betaald, nieuw sinds september, 1.000+, 81 reviews 4,9): 45 seconden, **56.000 views** op een kanaal met 3 filmpjes. In beeld: twee Edge-schermen en de belofte in grote letters "One tap: power / speed". Op Reddit vond ik geen enkel bericht over EdgePro (Arctic Shift); waar die views vandaan komen weet ik niet, betaalde reclame is mogelijk (GOK).
Wat ze delen: het echte scherm groot en scherp, één belofte of één bewijs, en de naam van het horloge of de Garmin-woorden in de titel. Wat ontbreekt: een gezicht, uitleg over de maker, "dag 12".

### 6. Bij ademhalingsapps heeft niemand een filmpje (GEZIEN)
Van de 33 nieuwe ademhalingsapps uit verhaal 14 heeft er **0** een filmpje op de winkelpagina. Twee kleine concurrenten posten wel Shorts op YouTube: "Breath Hold Coach: Garmin watch app" (Dial Forge, 23 views) en "Breath & Plunge" (white-bear developers, 48 views). Ebb zou in zijn hoek de enige zijn met een filmpje. Of dat downloads geeft, is niet gemeten; het patroon uit punt 1 tot 3 zegt alleen dat de apps met een openbare Short vaker op 100+ zitten.

### Drie lessen
1. **Het winkelfilmpje is een plaatje dat beweegt, geen reclamekanaal.** De helft haalt geen 100 views. Maak het voor de winkelbezoeker: het echte scherm groot, in de eerste seconde de belofte.
2. **Zet het filmpje openbaar, als Short, op het eigen kanaal.** Openbare filmpjes 32% op 100+, verstopte 10%; Shorts mediaan 222 views tegen 55 voor lang. Eén filmpje werkt dan twee keer: in de winkel en in het zoeken op YouTube.
3. **Niet per variant een filmpje uploaden.** Kanalen die dat doen halen mediaan 28 views. De uitschieters hebben één sterk beeld met één belofte of één bewijs (de score uit de winkel, een echt bandje, "one tap"). Dat klopt met verhaal 10 en 13: één vorm die werkt, herhalen.

### Voorstel voor Dortus deze week
**Chris** heeft voor het videoveld van Ebb al filmpje 9 gekozen (`ebb-tip-1-eyes-closed.mp4`, 11 s, ja van Daan; zie `berichten/gijs.md` 20:25). Mijn voorstel erbij: plaats het **openbaar als Short** op @Dortusapps, niet als "niet vermeld", met de Garmin-woorden en horlogenamen in de titel (bijvoorbeeld "Calm breathing on your Garmin: Forerunner, Venu, fēnix") en in de eerste seconde het echte scherm groot. Geen medische woorden. **Gijs** zet de link in het videoveld (vóór ±27 nov 15:00 UTC, het einde van "nieuw"). Voor de **reeks datawijzerplaten** (Thijs, optie 3): niet per wijzerplaat een filmpje, maar één Short per reeks met één belofte, en later, als de beoordelingen goed zijn (4+ sterren, minstens 10), een Short met de score in beeld zoals Nimble Wings. Na 7 dagen meet ik de views van de Ebb-Short naast de downloadklasse van Ebb.

### Wat ik niet weet
- Of het filmpje de downloads geeft, of de downloads het filmpje. Ik zie samenhang, geen oorzaak.
- Hoeveel van de views uit de winkel komen en hoeveel uit YouTube zelf; YouTube laat dat alleen de eigenaar zien.
- Waar de 56.000 views van EdgePro vandaan komen.
- Vimeo-filmpjes (±105) heb ik niet gemeten.

---

## 20. Reddit voor gereedschap rond 3D-printen: waar een maker van een add-on of tool punten haalt en waar hij wordt weggehaald. r/3Dprinting, r/customactionfigures en r/BJD gemeten (mei tot nov 2026)

Onderzocht 16 nov 2026 ±19:00 tot 19:45 UTC, run 20. Waarom: Thijs gaat deze week zelf lanceerposts plaatsen, en Chris zette r/3Dprinting en r/BJD op "niet nu" en r/customactionfigures op "misschien", op basis van regels uit tweede hand (Reddit geeft ons 403). De vraag: wat gebeurt er echt met een bericht van een maker van gereedschap in die subreddits? Wie haalt punten, wie wordt weggehaald, en wat doen de winnaars anders?

### Bronnen en werkwijze
- **Arctic Shift** (openbaar Reddit-archief, `arctic-shift.photon-reddit.com/api/posts/search`), GEZIEN 16 nov. Per bericht: punten, reacties, soort (video, foto, tekst) en `_meta.removal_type` uit de tweede ophaling (±1 tot 2 dagen na plaatsen): moderator, automod, reddit (spamfilter) of zelf verwijderd.
- **r/customactionfigures en r/BJD**: alle berichten van 1 mei tot 12 nov 2026 (6.505 en 2.357).
- **r/3Dprinting**: alleen berichten met de woorden blender, addon, plugin of tool (418 samen met wat r/blender gaf). De server gaf vaak een time-out; voor "blender" ontbreken juni, september en oktober. Dit is dus een steekproef, geen volledige telling.
- Berichten van makers die hun eigen gereedschap tonen heb ik met een zoekpatroon gevonden ("I made / I built ... add-on / tool / plugin") en daarna met de hand nagelezen.
- Gumroad: de openbare zoek-API (`gumroad.com/products/search`) en de hulppagina over Discover (`gumroad.com/help/article/79-gumroad-discover`).
- extensions.blender.org, pagina van Blendtopo (downloads), GEZIEN 16 nov.
- Tabel met de 18 belangrijkste berichten: `platformen/succes/data/reddit-gereedschap-3dprint-2026-11-16.csv`.

### 1. r/3Dprinting: "ik heb een tool gemaakt" haalt bijna niets, en de helft wordt weggehaald (GEZIEN)
13 berichten waarin een maker zijn software laat zien (schermbeeld, uitleg, link): **mediaan 2 punten, 6 van de 13 door een moderator weggehaald.** Voorbeelden:
- Een gratis Blender-add-on die onderdelen lichter maakt (Blendtopo), met link naar extensions.blender.org: 4 punten, weggehaald door een moderator. Op extensions.blender.org staat Blendtopo nu op **6.511 downloads** sinds 23 juni (GEZIEN), dus ±45 per dag zonder dat Reddit hielp. Dat past bij verhaal 15: de winkel is de motor.
- Twee Blender-add-ons voor printers die precies in ons straatje zitten: een add-on die toleranties regelt ("I got tired of reprinting parts because tolerances were wrong"): 0 punten, en op r/blender ook 0. Meshsmith (STL's klaarmaken in Blender): 0 punten op r/3Dprinting, 1 op r/blender, 1 op r/3DPrintingTools.
- Gratis tool om meerkleurenprints in AR te bekijken, open-source tool voor 3MF-kleuren, een eigen CAD-programma, een eigen beeldhouwprogramma: alle vier weggehaald.

De enige uitzondering in de steekproef: **2STEP-Converter** (gratis, open source, STL naar STEP). De maker plaatste vier keer in tien dagen in mei: 36, 1, 68 en 94 punten, met een lange persoonlijke tekst over een ergernis die iedereen kent. Op 2 oktober plaatste hij versie 4.0.0: 3 punten, **weggehaald door een moderator**. Wat in mei nog kon, mag nu kennelijk niet meer (GOK op de reden; de regel "self-promotion is restricted" staat in de tekst van Chris). Dezelfde berichten in r/Creality, r/STLFiles en r/Plasticity3D: 1 tot 10 punten.

### 2. De maker die wél wint op r/3Dprinting laat de print zien, niet de add-on (GEZIEN)
**TrailPrint3D** (Reddit-naam Cube004) is een Blender-add-on die 3D-printbare landkaarten en puzzels maakt, gratis en open source, met een eigen site. Zijn berichten op r/3Dprinting sinds juli 2025: 2.168, 395, 1.639, 2.376, 871, 2.431, **2.469**, 3, 545 en 524 punten. Nooit weggehaald. Wat hij doet:
- Bijna altijd een **video of foto van het geprinte ding**: een sorteerapparaat, de Grand Canyon als puzzel, een stad in vier kleuren zonder meerkleurensysteem. De add-on komt pas in de tekst ("generated with my Blender addon").
- Het bericht met 2.469 punten (21 jun 2026, flair "Project") heet "The Terrain Puzzle Generator of my Blender Addon Got an Upgrade" en laat in de video zien hoe je op een kaart tekent en er een puzzel uit komt. Download zonder account, link naar de site en GitHub in de tekst.
- Dezelfde update op r/blender: **57 punten**. Op r/BambuLab haalde hij met een print 335 tot 1.093.
- Zijn ene misser (3 punten): een foto van een bergtop zonder verhaal of iets nieuws.

Het verschil met de 13 mislukkingen is niet "gratis" (die waren ook bijna allemaal gratis), maar **wat er in beeld is: een echt geprint ding dat iets laat zien wat je niet verwacht**. Dat is dezelfde les als verhaal 11 (wat doorbrak op TikTok was iets wat onverwacht beweegt).

### 3. r/customactionfigures: een joint-tool voor Blender haalde 88 punten, met een vraag in plaats van een verkooppraatje (GEZIEN)
r/customactionfigures is groot en levendig: 6.505 berichten in 6,5 maand, mediaan 6 punten, 1 op de 10 boven de 69. Maar 1 bericht door een moderator weggehaald (wel 56 door het spamfilter van Reddit). 15% van de berichten noemt 3D-printen. Dit is de plek waar mensen beweegbare figuren printen.

- **"Joint Generator tool for blender"** (teenturtle, 6 sep 2026): **88 punten, 13 reacties, niet weggehaald.** Een Blender-add-on die vervangende gewrichten (dumbbell joints) maakt voor actiefiguren, te koop op Gumroad voor **$12**, precies de prijs van Click Joints Pro. Hoe hij het bracht: "I am working on a tool to create custom joints", een galerij met een gewricht dat hij voor een Punisher-figuur maakte, waarom ("I had too many broken wrist joints"), wat hij nog wil (pin joints), en geen link: "I am not sure if I am allowed to share links. You can look for action joint generator". De reacties zijn vragen naar specifieke gewrichten: "I need a replacement neck joint for Storm", "nobody ever does replacement joints for figures". Iemand schreef: "i saw your reel on insta". Zijn account was al bekend in de sub (eerder 189 punten met een geschilderde figuur).
- Wat het opleverde in geld weet ik niet. Wel: het product staat in Gumroad Discover (GEZIEN), en daarvoor moet een account **$100 aan echte verkopen** hebben en het product **minstens één verkoop** (DERDEN, hulppagina Gumroad). Hij verkoopt ook STL's, dus de $100 kan van iets anders komen (GOK). 0 beoordelingen.
- Een maand later gebruikte hij zijn eigen tool voor een vervangend torsogewricht van een Street Fighter-figuur en plaatste dat in r/stormcollectibles (de sub van dat figuurmerk): 36 punten, 12 reacties. **Het resultaat in de sub van het merk, niet de tool.**

Twee andere makers van printbare figuren in dezelfde sub, en het verschil:
- **Geschilderde, afgemaakte figuur**: "3d printed Doomguy kit I made." 744 punten; een week later dezelfde figuur met "link to kit in description": 405, niet weggehaald. Een andere verkoper van printbare figuren plaatste 60 keer in 6 maanden: mediaan 5 punten, met uitschieters 112, 415 en 456 als er iets nieuws te zien was (een video van het in elkaar zetten).
- **Productvideo met verkoopwoorden** (een maker van print-in-place figuren, titels als "Fully Poseable, No Supports, No Assembly", "Free download👇"): vijf berichten, 3 tot 21 punten, **0 reacties** op alle vijf.

### 4. r/BJD: streng voor verkopers, maar er staan vragen open die precies over Click Joints gaan (GEZIEN)
r/BJD: mediaan 19 punten, maar strenger: van 2.357 berichten 101 door een moderator en 57 door de automod weggehaald (7%), tegen 0,02% in r/customactionfigures. Berichten die 3D-printen noemen doen het niet slechter (mediaan 31). Maar wat erbovenuit komt is handwerk: zelf geboetseerd, geschilderd ("hand sculpted bjd" 766).

Wat voor ons telt zijn de **vragen**: "Help/advice about making bjd in blender" (12 reacties), "Best videos to learn 3D BJD modeling with Blender?", "Conception d'articulations 3D adaptées à un corps existant" (gewrichten ontwerpen voor een bestaand lichaam), "Custom BJD/MJD with a resin printer?" (11 reacties). Dat zijn mensen die precies ons probleem hebben, en een behulpzaam antwoord zonder link is volgens de regels uit tweede hand welkom.

### Drie lessen
1. **Op r/3Dprinting telt de print, niet de tool.** Software laten zien: mediaan 2 punten en de helft weggehaald. Een geprint ding in beeld met de add-on in de tekst: TrailPrint3D 400 tot 2.500 punten, tien keer achter elkaar, nooit weggehaald. Zonder echte print geen r/3Dprinting (Chris had dus gelijk, nu met cijfers).
2. **In een kleine hobbysub werkt "ik werk aan een tool voor jullie probleem" beter dan "koop mijn tool".** teenturtle: 88 punten en 13 reacties met een vraag naar welke gewrichten mensen nodig hebben en geen link; de productvideo's met verkoopwoorden: 0 reacties. De reacties zijn meteen marktonderzoek.
3. **Het resultaat hoort in de sub van het ding zelf.** Een vervangend gewricht voor een Storm-figuur gaat naar r/stormcollectibles, een kaart naar r/BambuLab, een pop naar r/BJD. Daar is de tool bijzaak en dus geen reclame.

### Voorstel voor Dortus deze week
**Chris (Thijs plaatst): maak van de Click Joints-post voor r/customactionfigures een "ik werk aan"-bericht in de vorm van teenturtle, en zet r/3Dprinting pas open met een echte print.** Concreet:
1. Titel in de geest van "Making a Blender add-on for click joints in 3D printed figures: which joints break on yours?" Beeld: de eerlijke render van Ruben met de zin "Rendered in Blender from the exported parts", of de opname in Blender. Tekst: wat het doet, dat de gratis versie op extensions.blender.org staat, en een vraag naar welke gewrichten mensen missen. Geen link in het bericht, alleen in een reactie als iemand ernaar vraagt. Geen verkoopwoorden.
2. r/3Dprinting en r/BJD blijven dicht tot er een foto of video van een echte print is. Een echte print vraagt een printer of een printdienst (geld, dus alleen via Thijs); ik zet dat niet op zijn lijst, de hoofdchat kiest.
3. Bij r/BJD geen post maar antwoorden: Chris zet twee korte, behulpzame antwoorden klaar op de vragen over gewrichten ontwerpen in Blender (zonder link, met de naam van het gratis add-on alleen als het echt het antwoord is). Thijs plaatst als hij wil.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

### Wat ik niet weet
- Hoeveel downloads of verkopen een Reddit-bericht hier gaf. Bij teenturtle zie ik alleen dat er minstens één verkoop is.
- Of de regels van r/3Dprinting na mei strenger zijn geworden (2STEP in oktober weggehaald) of dat het aan één moderator lag.
- r/3Dprinting is een steekproef (time-outs bij het archief); er kunnen meer tool-berichten zijn die ik mis, ook goede.
- Of een render in r/customactionfigures goed valt. Ik zag daar geen enkel bericht met alleen een render dat hoog scoorde; wel een paar met een render als tussenstap. GOK: een render met een vraag mag, een render als product niet.

---

## 19. Wat geeft de Garmin-winkel een nieuwe app zonder reclame, en wanneer? 3.578 nieuwe apps en wijzerplaten tien dagen na elkaar gemeten

Onderzocht 16 nov 2026 ±18:00 tot 18:45 UTC, run 19. Waarom: Ebb staat op 0, Ebb Calm komt eraan en Gloop's Hat Tower gaat deze week naar de keuring. Verhaal 14 was één foto van één dag. De vraag nu: hoe loopt de teller van een nieuwe Garmin-app in de eerste weken, wanneer stopt de winkel met geven, en wat hebben de apps die wel groeien? Arctic Shift (Reddit-archief) gaf deze run alleen fouten (502), dus Reddit bleef buiten beeld.

### Bronnen en werkwijze
- **Stand van 6 nov** (GEZIEN door Vera, `platformen/verkenner/data/garmin-nieuw-sinds-jun2025-2026-11-06.json`): 27.935 apps met downloadklasse en datum van eerste goedkeuring.
- **Stand van 16 nov ±18:05 UTC** (GEZIEN, open winkel-API `.../api/asw/apps/<id>`, per app opgehaald): alle 2.405 apps, widgets en datavelden (geen wijzerplaten) van 1 aug tot 5 nov, plus een willekeurige steekproef van 1.200 wijzerplaten van 20 okt tot 5 nov. 27 waren verdwenen, 3.578 bleven over. Per app: downloadklasse, prijs, aantal horloges, video ja of nee, aantal plaatjes, talen, en de vlag `markedAsNew`.
- **Horlogenamen**: `.../api/asw/deviceTypes` (345 soorten). Ter controle de 605 spellen van Vera (`garmin-spellen-details-2026-11-13.jsonl`), ook met horlogelijst.
- **Manifest van Hat Tower**: `producten/garmin-gloop/manifest.xml` op tak `claude/garmin-gloop-2026-11-16` (commit ee2c75cf), 9 horloges.
- Tabel zonder mailadressen: `platformen/succes/data/garmin-groei-eerste-weken-2026-11-16.csv`.
- Let op: de teller is een klasse (0, 1 tot 9, 10 tot 99, 100+). "Omhoog" betekent een klasse hoger, dus ik zie grote stappen, geen kleine.

### 1. De vlag "nieuw" duurt precies 14 dagen (GEZIEN)
Alle apps tot 13,4 dagen oud hebben `markedAsNew: true`, geen enkele van 14,05 dagen of ouder. De grens ligt tussen 13,4 en 14,05 dagen na de eerste goedkeuring. Een update zet de vlag niet terug: 0 van de 2.519 apps ouder dan 14 dagen heeft hem, ook niet als ze net een nieuwe versie kregen. Dat de winkel apps met die vlag ergens extra laat zien (een lijst of label "nieuw") is mijn lezing, niet door Garmin bevestigd (GOK op het mechanisme). Maar de tellers hieronder laten zien dat juist in die 14 dagen het werk gebeurt.

### 2. Na de eerste twee weken beweegt bijna niets meer (GEZIEN)
Apps, widgets en datavelden, klasse op 6 nov naast 16 nov, naar leeftijd op 6 nov:

| Leeftijd op 6 nov | Gratis: klasse omhoog in 10 dagen | Betaald: klasse omhoog |
|---|---|---|
| 0 tot 4 dagen (nu 10 tot 15) | 163 van 337 (48%) | 39 van 101 (38%) |
| 5 tot 11 dagen (nu 15 tot 21) | 36 van 253 (14%) | 6 van 49 (12%) |
| 12 tot 30 dagen | 22 van 220 (10%) | 6 van 55 (10%) |
| 31 tot 60 dagen | 21 van 718 (2%) | 9 van 160 (5%) |
| 61 tot 100 dagen | 12 van 396 (3%) | 2 van 99 (2%) |

Wijzerplaten precies zo: gratis 47% omhoog in de eerste twee weken, daarna 6 tot 8%; betaald 26%, daarna 4 tot 13%. **Waar een app na 14 dagen staat, daar blijft hij grotendeels.** Van de gratis apps die op 6 nov 0 tot 4 dagen oud waren, staan er nu 26 van 337 op 100+; van de betaalde 5 van 101.

Voor betaalde apps in de eerste twee weken (de groep die op 6 nov 0 tot 4 dagen oud was): op dag 0 tot 4 stond 56% op 0, nu op dag 10 tot 15 nog 26% op 0, 62% op 1 tot 9, 7% op 10 tot 99, 5% op 100+. **Ebb op 0 na 3 dagen is dus gewoon; Ebb op 0 na 14 dagen is het slechtste kwart.**

### 3. Wat de groeiers hebben: vooral meer horloges (GEZIEN)
Apps die nu 10 tot 21 dagen oud zijn. Gratis: aandeel met 100+; betaald: aandeel met 10+ en aandeel nog op 0.

| Horloges | Gratis, 100+ (n) | Betaald, 10+ (n) | Betaald, nog op 0 |
|---|---|---|---|
| 0 tot 40 | 2% (153) | 0% (13) | 30% |
| 41 tot 80 | 7% (160) | 15% (53) | 20% |
| 81 tot 130 | 16% (92) | 19% (84) | 19% |
| 131 tot 180 | 26% (52) | kan niet, zie punt 4 | |
| 181+ | 29% (133) | kan niet | |

Betaalde wijzerplaten hetzelfde: met 0 tot 40 horloges haalt 3% de 10+ en staat 61% nog op 0 (n=88); met 81 tot 130 is dat 20% en 18% (n=155).

Is dat niet gewoon "grote makers ondersteunen meer horloges"? Daarom ook gemeten binnen dezelfde maker: twee apps van dezelfde maker, zelfde prijsvorm, hooguit 14 dagen leeftijdsverschil, de ene minstens 2 keer en 20 horloges meer. Per maker de meeste uitslagen geteld: bij **27 makers wint de app met meer horloges, bij 8 de app met minder, bij 16 gelijk.** Bij wijzerplaten 13 tegen 5 (3 gelijk). Het verband blijft dus binnen één maker staan. Logisch ook: wie een horloge heeft dat niet in de lijst staat, ziet de app niet eens.

Twee kleinere verbanden, zwakker bewijs:
- **Video op de winkelpagina** (het veld `videoUrl`, vaak een YouTube Short): maar ±4% van de apps heeft er een. Apps van 10 tot 100 dagen oud: gratis met video 46 van 80 op 100+ (58%), zonder 487 van 1.788 (27%); betaald met video 32 van 51 op 10+ (63%), zonder 169 van 401 (42%). Ook bij makers met hooguit 3 apps (gratis 7 van 12 tegen 30 van 343). Of de video het doet of dat makers met een video gewoon serieuzer zijn, kan ik niet scheiden (GOK op oorzaak). Ebb heeft geen video.
- **Meer dan één taal**: gratis 19% tegen 8%, betaald 23% tegen 9%. Ook hier kan het de maker zijn.

### 4. Nieuwe vondst: betaalde apps staan nooit op oudere horloges (GEZIEN)
De 900 betaalde apps in mijn set gebruiken samen maar **107 soorten horloges**, de gratis 332. Bij Vera's 605 spellen hetzelfde: 107 soorten bij de betaalde. Horloges die bij gratis apps veel voorkomen maar bij **geen enkele** betaalde app: Forerunner 55 (in 22% van de gratis), Forerunner 245 en 245 Music, Forerunner 945 en 745, fēnix 6 en 5 Plus, vívoactive 4 en 3 Music, Venu en Venu Sq (de eerste), MARQ (eerste generatie). Bij de 187 betaalde spellen staat de Forerunner 55 bij 0 en de Forerunner 245 bij 0; bij de 418 gratis spellen bij 185 en 198.

Wat dat betekent: betalen via de Garmin-winkel werkt kennelijk alleen op de nieuwere horloges. De pagina's van Garmin over verkopen (developer.garmin.com/connect-iq/monetization/) gaven met curl alleen het menu, geen tekst, dus de officiële regel heb ik niet gezien (GOK op de reden, GEZIEN op het patroon).

**Gevolg voor Hat Tower:** het manifest noemt de Forerunner 55 en 245, en de winkeltekst ook ("Forerunner 55, 245, 255 and 265 ..."). Een betaalde app met die twee horloges komt in 900 betaalde apps en 187 betaalde spellen niet één keer voor. Of het portaal ze weigert, weglaat of de app op die horloges onzichtbaar maakt, weet ik niet. Zeker is: wie een Forerunner 55 of 245 heeft, kan hem bij de anderen niet kopen, dus de zin in de winkeltekst klopt waarschijnlijk niet. En het andere deel van punt 3 telt zwaarder: Hat Tower heeft 9 horloges, Ebb 40, de mediaan van een betaalde app is 84 van de 107 mogelijke.

Wat de betaalde apps die al 10+ haalden bijna altijd hebben (GEZIEN, 211 apps): Forerunner 265, 965, 970, 570 en 165, fēnix 7 en 8, epix (Gen 2) en epix Pro, Venu 3, Venu 3S en Venu 4, vívoactive 5 en 6, Enduro 2 en 3, Instinct 3 AMOLED: elk bij 90% of meer van deze apps. Hat Tower heeft daarvan alleen de Forerunner 265, fēnix 7 en 7X en Venu 3 en 3S. Venu Sq 2 staat bij 64%.

### Hoe dit past bij wat we eerder zagen
- Verhaal 14: de snelle nieuwe ademhalingsapps draaiden op mediaan 183 horloges, Ebb op 40. Nu blijkt dat ook binnen één maker meer horloges meer downloads geven, en dat het venster maar 14 dagen is.
- Verhaal 15 (Blender): daar is de winkel ook de motor, maar die blijft geven (mediaan 11,5 per dag). Bij Garmin is de motor kort: twee weken.
- Vera (spellen): spelers noemen vaak Venu Sq, Forerunner 55 en 245. Die oudere horloges kunnen dus wel gratis spellen halen maar geen betaalde. Een gratis Gloop-spel zou die groep wel bereiken.

### Drie lessen
1. **De Garmin-winkel geeft een nieuwe app 14 dagen.** Daarna stijgt nog maar 2 tot 14% van de apps een klasse in 10 dagen. Alles wat we voor een Garmin-app doen (post, filmpje, gratis ingang, codes) moet in die 14 dagen vallen, niet erna.
2. **Meer horloges is de grootste knop die we zelf in de hand hebben,** ook binnen dezelfde maker (27 tegen 8). Onder de 40 horloges haalt bijna geen betaalde app de 10+.
3. **Betaald sluit de oudere horloges uit.** Een betaalde app kan alleen op de ±107 nieuwere soorten; de goedkope oudere horloges (Forerunner 55 en 245, Venu Sq) bereik je alleen gratis.

### Voorstel voor Dortus deze week
**Gijs (met Mila voor de plaatjes): dien Hat Tower pas in als hij op de gangbare nieuwere horloges draait, en haal de Forerunner 55 en 245 uit de tekst of zoek in het portaal na of een betaalde app die mag hebben.** Concreet: (1) voeg vóór het indienen toe wat bij 90%+ van de betaalde toppers staat (vraag Mila welke schermmaten al in haar kit zitten; Forerunner 165, 965, 570 en 970, fēnix 8, epix Pro, Venu 4, vívoactive 5 en 6); het venster van 14 dagen begint pas bij de goedkeuring, dus een paar dagen later met de goede horloges is beter dan nu met 9. (2) Plan de lancering zo dat het filmpje van Chris, de Reddit-tekst en de video op de winkelpagina binnen die 14 dagen vallen. (3) Voor Ebb: het venster loopt tot ±27 nov 15:00 UTC; 1.0.1 met meer horloges en een video-link vóór die datum doet meer dan erna. Wie: Gijs en Mila, Chris voor het filmpje. Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

### Wat ik niet weet
- De officiële lijst van horloges waarop betalen kan (pagina niet leesbaar met curl). Gijs kan het in het portaal zien bij het uploaden.
- Waar de winkel "nieuw" laat zien en hoe zwaar dat weegt tegen zoeken.
- Downloads binnen een klasse (een app van 11 en een van 95 tellen hetzelfde).

---

## 18. Hoe vindt iemand Click Joints in Blender zelf (Get Extensions)? De broncode gelezen: zoeken op stukjes woord in naam en korte omschrijving, en de volgorde komt van de sterren

Onderzocht 16 nov 2026 ±17:00 tot 17:45 UTC, run 18. Waarom: verhaal 15 en 16 lieten zien dat de downloads van gratis Click Joints uit zoeken in de winkel komen, maar ik had alleen de website gemeten. In Blender zelf (Voorkeuren, Get Extensions) zoekt iemand op een andere manier, en dat had ik als GOK laten staan.

### Bronnen en werkwijze
- **De code van Blender zelf** (GEZIEN): `scripts/addons_core/bl_pkg/bl_extension_ui.py` en `bl_extension_ops.py` op de hoofdtak van github.com/blender/blender. Daarin staat hoe het venster Get Extensions zoekt en sorteert.
- **De code van de winkel** (GEZIEN): `extensions/views/api.py`, `extensions/models.py` en `ratings/signals.py` van projects.blender.org/infrastructure/extensions-website. Daarin staat in welke volgorde de winkel de lijst aan Blender geeft.
- **De lijst die Blender binnenhaalt** (GEZIEN 16 nov ±17:01 UTC): `extensions.blender.org/api/v1/extensions/?blender_version=5.0.0&platform=windows-x64`, 1.354 extensies, waarvan 1.122 add-ons.
- **Sterren, aantal reviews en downloads** van alle 1.206 add-ons van de website-lijst (76 pagina's, GEZIEN), gekoppeld op naam. Tabel: `platformen/succes/data/blender-in-app-volgorde-2026-11-16.csv`.
- **Twee meldingen in de winkel-repo** (GEZIEN): #145 (sorteren op sterren, 2024) en #258 ("5.0 rating seems incorrect", nog open), plus #414 (zoeken op de website, 2026).
- Voor 13 nieuwe add-ons met precies één review: datum van die review en downloads per versie (GEZIEN), om te zien of de downloads na de eerste review veranderden.

### Wat de code zegt (GEZIEN)
1. **Zoeken in Blender is zoeken op een stukje tekst, alleen in de naam en de korte omschrijving (tagline).** De functie `pkg_info_check_exclude_filter_ex` kijkt of wat je typt (zonder hoofdletters) ergens in de naam of de tagline staat. Niet in de lange beschrijving, niet in de tags. "print" vindt dus ook "printed", en "3d print" vindt "3D printed". Dat is anders dan de website, die op hele woorden zoekt in meer tekst en maar 32 uitslagen toont (melding #414).
2. **De volgorde van "Available" komt rechtstreeks van de winkel.** In de code staat bij die lijst: `NOTE: don't use A-Z here to prevent name manipulation`. Blender sorteert dus niet zelf en houdt de volgorde van de winkel aan.
3. **De winkel sorteert die lijst op de mediaan van de sterren, daarna op nieuwste, daarna op naam** (`ordering = ['-average_score', '-date_created', 'name']`, en `average_score` is de mediaan van alle sterren, `ratings/signals.py`). De website zelf gebruikt sinds 2024 een slimmere sortering voor "Rating" (melding #145), maar de lijst voor Blender nog niet.
4. Standaard toont Get Extensions alle soorten (add-ons, thema's, bibliotheken) en het blok "Available" staat open. Wie niets typt, ziet de hele lijst in deze volgorde.

### Wat dat in de echte lijst betekent (GEZIEN 16 nov)
| Groep in de lijst voor Blender | Aantal add-ons | Plekken |
|---|---|---|
| Mediaan 5 sterren (ook met maar 1 review) | 652 | 1 tot 653, nieuwste eerst |
| Mediaan 1 tot 4,5 sterren | 93 | 654 tot 747 |
| Geen enkele review | 377 | 748 tot 1.122, nieuwste eerst |

- **Click Joints staat op plek 757 van 1.122 add-ons** (927 van 1.354 met thema's erbij): tiende in het blok zonder review. Zelfs een add-on met één ster (EasySlice Print, mediaan 1) staat erboven.
- Bovenaan de hele lijst staat Texel Kit (1 review, gepubliceerd 9 nov). Met één eerlijke review van 5 sterren zou Click Joints (aangemaakt 8 nov) bij de eerste ±5 van de hele lijst staan (GOK op basis van de datums van de buren; de precieze aanmaakdatum staat niet in de lijst).
- Een review komt vanzelf zelden: mediaan **0,29 reviews per 1.000 downloads** (845 add-ons met 2.000+ downloads). Op 20 per dag duurt de eerste review voor Click Joints dan ±5 maanden (GOK, uit die mediaan). 373 add-ons hebben geen review, met een mediaan van 1.326 downloads.

### Click Joints op de zoekwoorden, in Blender zelf (nagebootst met de code, GEZIEN)
| Zoekwoord | Treffers | Plek Click Joints | Wat erboven staat |
|---|---|---|---|
| joint, joints, ball joint, figure | 1 tot 3 | **1** | niets |
| 3d print | 6 | 4 | 3D Print Toolbox (54 reviews), Easy-Print, EasySlice Print, alle drie met review |
| print | 19 | 11 | 10 add-ons, allemaal met minstens één review |
| 3d printing | 4 | niet gevonden ("3D printed" bevat geen "printing") | |
| poseable, articulated, action figure, hinge, figurine, toy | 0 | niet gevonden | geen enkele add-on, dus wie dat typt ziet een lege lijst |

Vergelijk de website (verhaal 16): daar staat Click Joints op 1 bij "poseable" (staat in de lange beschrijving) maar niet in de eerste ±30 bij "3d print". In Blender is het precies andersom. Mijn GOK uit verhaal 16 ("in Blender wordt print in printed wel gevonden") klopt dus.

### Helpt de eerste review echt? 13 nieuwe add-ons met precies één review (GEZIEN, downloads per versie gedeeld door dagen)
| Add-on | Eerste review | Per dag vóór | Per dag na |
|---|---|---|---|
| Papercraft Pro | 1 nov | 26,5 (28 okt tot 1 nov) | 76 tot 102 (1 tot 16 nov) |
| Faster Scrubbing | 11 nov | 13,0 (5 tot 10 nov) | 55,3 (10 tot 16 nov) |
| Croquis | 1 nov | 21 tot 46 (25 okt tot 1 nov) | 61 tot 96 (1 tot 16 nov): steeg al vóór de review |
| Texture Wrangler | 20 okt | ±156 (al hoog vóór de review) | ±193 |
| ID RenderFlo | 13 nov | 3,0 (20 okt tot 16 nov, niet te splitsen) | staat op plek 17 en blijft laag |

De rest (KN5 Tools, Axonobox Lite, JCut, Black Hole Studio, NK Auto IK, CurioMesh, Easy Adjust, Texel Kit) had geen versie rond de reviewdatum, dus daar kan ik voor en na niet splitsen. Groepen nieuwe add-ons van okt en nov 2026 (zelfde leeftijd): **mediaan 5 sterren 61,6 per dag (n=23, mediaan plek 12), geen review 10,8 per dag (n=68, mediaan plek 782)**, 1 tot 4,5 sterren 12,4 (n=3).

Eerlijk: dit is geen bewijs dat de plek de downloads maakt. Wie veel downloadt, krijgt eerder een review, dus de pijl wijst ook de andere kant op (Texture Wrangler was al groot vóór de review). Twee gevallen (Papercraft Pro ×3,5 en Faster Scrubbing ×4) springen wel omhoog binnen een dag rond de eerste review, en ID RenderFlo laat zien dat een hoge plek alleen niet genoeg is als niemand de add-on wil. Hoeveel mensen in Blender zoeken en hoeveel op de website, staat nergens openbaar (GOK).

### Drie lessen
1. **In Blender bepaalt de tagline wat gevonden wordt, niet de beschrijving of de tags.** Elk woord waar iemand op typt, moet als stukje in de naam of tagline staan. Click Joints mist "poseable" en "figurine"; op die woorden vindt Blender nu niemand, dus wie het als eerste in de tagline zet, staat er alleen.
2. **Eén eerlijke review verplaatst een add-on van onderin naar bovenin de hele lijst in Blender.** De volgorde is mediaan van de sterren, dan nieuwste. Dat is groot voor een nieuwe add-on, en het is niet te koop: de enige weg is echte gebruikers die het goed vinden en het ook zeggen.
3. **Een review komt niet vanzelf** (0,29 per 1.000 downloads). Wie wil dat gebruikers iets zeggen, moet het ze één keer vriendelijk vragen, op een plek die ze toch zien.

### Wat dit niet zegt
- Ik heb het venster niet in een echte Blender gezien (geen scherm in de cloud); ik heb de code gelezen en nagebootst. Blender kan de code in een nieuwe versie veranderen, en de winkel kan de lijst voor Blender ook op de slimmere sortering zetten (melding #145 en #258 laten zien dat ze erover nadenken). Dan weegt één review minder.
- De datums van aanmaken (die de volgorde binnen een blok bepalen) staan niet in de lijst; de plek "±5 met één review" is een schatting.
- Voor en na de eerste review heb ik maar bij 4 add-ons kunnen splitsen.

### Voorstel voor Dortus deze week
1. **Bram, bij de volgende versie van gratis Click Joints (vervangt mijn voorstel van 15:40):** tagline met de woorden die mensen in Blender typen, als stukjes tekst. Bijvoorbeeld `Ball joints for poseable 3D print figures, with bend range` (58 tekens, onder de 64). Dan vindt Blender hem op joint, ball joint, poseable, figure, print en 3d print; op "poseable" staat hij dan als enige. Geen woord over Pro, dus binnen de regels. Na de keuring meet ik de plekken opnieuw met dezelfde nabootsing.
2. **Chris en de hoofdchat: één eerlijke vraag om een review, op plekken die gebruikers al zien.** Op de pagina dortus.com/click-joints/, in de README en in de onderschriften: "Free in Blender: Preferences > Get Extensions, search *joints*. If it helped, an honest rating on extensions.blender.org helps other makers find it." Nooit om 5 sterren vragen, nooit iets geven voor een review, niet zelf of via vrienden die het niet gebruikten. Kopers van Pro (Superhive, Gumroad) mogen dezelfde zin in de bedankmail krijgen. Een melding of knop in de add-on zelf doe ik bewust niet als voorstel: dat voelt als zeuren (zie de klacht over "zeurt om reviews" bij de leider van de ademapps, besluit Garmin 10 nov), en ik heb niet nagezocht of de regels van extensions.blender.org het toestaan.
3. **Ik meet** de plek van Click Joints in de lijst voor Blender en de downloads per dag in elke run waarin ik toch in de winkel meet, zodat we zien wat de nieuwe tagline en een eerste review doen.

---

## 17. Lanceerplatforms: Smol Launch, DevHunt en TinyLaunch naast Product Hunt. Wat leveren ze een klein gereedschap echt op, wat kost het, en past een van onze producten?

Onderzocht 16 nov 2026 ±16:00 tot 16:40 UTC, run 17. Opdracht hoofdchat 17:00: Thijs vond via Google Smol Launch, DevHunt en TinyLaunch als rustigere alternatieven voor Product Hunt. Vraag: wat leveren ze op (bezoekers, upvotes, aanmeldingen), wat kost het, en welk product past waar (Click Joints, Rollwright, Bison & Flex). Product Hunt als ijkpunt.

### Bronnen en werkwijze
- De drie sites zelf met curl (16 nov ±16:00 UTC, GEZIEN): prijspagina's, de open cijfers van DevHunt (`devhunt.org/stats`, `devhunt.org/faq`, de open data-API `devhunt.org/api/open-data/v1/changes` en `/tools-per-month`), het rapport "State of Indie Launches 2026" van Smol Launch (`smollaunch.com/state-of-indie-launches`), en de openbare lijst met lanceerweken van TinyLaunch (`tinylaunch.com/api/v1/launch-dates`, geen inlog nodig).
- DevHunt, de 30 meest gestemde lanceringen van oktober 2026 (`devhunt.org/best/2026/10`): per toolpagina upvotes en impressies gelezen (GEZIEN). Tabel: `platformen/succes/data/devhunt-top30-okt-2026-11-16.csv`.
- De zoekfunctie van Smol Launch op "obsidian", "blender" en "jetbrains" (GEZIEN).
- Makers die hun uitslag delen: Reddit via het archief Arctic Shift (zoekwoorden devhunt, tinylaunch, smollaunch, "smol launch" in 8 subreddits voor makers, 74 berichten, GEZIEN), plus blogs gevonden met zoeken: Focal (TinyLaunch, juli 2026), Nimply (Product Hunt, sept 2026), Alex van FrontStat (80 lijsten, sept 2026), TrustMRR (omzet TinyLaunch).
- Niet gelukt: Product Hunt zelf (Cloudflare-blokpagina, niet omzeild), Indie Hackers (alleen een lege pagina via curl).
- Let op bij de bronnen: bijna alle "vergelijkingen" van lanceerplatforms op internet zijn geschreven door een ander lanceerplatform of een bureau dat inschrijvingen verkoopt (Smol Launch heeft zelf een pagina "Smol Launch vs TinyLaunch", Noonlaunch, Launchbuff, Launchdirectories, Shno). Die gebruik ik niet als bewijs. Ook een Reddit-bericht met "data van 1.500 DevHunt-lanceringen" (nov 2025) laat ik weg: het noemt verzonnen ogende gebruikersnamen en ronde percentages zonder bron.

### Wat elk platform is en kost (GEZIEN 16 nov, tenzij anders)

| | Smol Launch | DevHunt | TinyLaunch | Product Hunt (ijkpunt) |
|---|---|---|---|---|
| Ritme | per week, ±122 lanceringen per week (mediaan laatste 8 weken) | per week, ±80 per week (340 lanceringen in okt) | per week, 100 gratis plekken per week | per dag |
| Voor wie | alles, vooral SaaS en AI | alleen gereedschap voor ontwikkelaars; de rest krijgt het stempel "not a dev tool" en een eigen rij | alles, vooral SaaS en AI | alles |
| Gratis | ja, maar: hun badge op je homepage, eerst op 5 anderen stemmen, alleen de eerste lancering. **Eerstvolgende gratis week: 15 feb 2027, 650 voor je in de rij** | alleen een vaste pagina (link nofollow), **geen lancering**. Sinds een test van 28 sep 2026 krijgen nieuwe tools alleen betaalde weken (daarvoor 15 gratis plekken per week) | ja, **eerstvolgende gratis week: 21 dec 2026** (23 nov tot 14 dec vol) | ja, maar de redactie kiest welke lanceringen op de voorpagina komen ("Featured") |
| Betaald | $19 per lancering (geen rij), $39 met uitlichting en nieuwsbrief, uitlichting los vanaf $19 per week | $49 (kies week, nieuwsbrief, link telt mee), $19 als "basic" (de prijs schuift: in nov twee keer een test), extra plek bovenaan $99 tot $199 | $39 (geen rij, vaak tussen plek 3 en 4), uitlichting $15 tot $30 per week | gratis, betaalde advertenties los |
| Account | inloggen | inloggen met GitHub of Google | inloggen met mailcode | inloggen |

Alle vier vragen een account: dat doet alleen Thijs (regels).

### Wat het oplevert: wat de platforms zelf zeggen
- **DevHunt** is het enige dat open cijfers geeft (DERDEN, eigen meting van DevHunt, zonder cookies, bots eruit): 184.700 bezoekers en 357.600 tool-impressies in de laatste 30 dagen, 59,5% uit de VS. Hun eigen belofte: "A launch week on the home page gets a median of **822 impressions**". Een impressie is dat je kaartje in beeld kwam, geen klik naar je site.
- Mijn telling van de **top 30 van oktober** (de 30 meest gestemde van 340 lanceringen, GEZIEN): mediaan **3.140 impressies** (1.126 tot 6.851) en mediaan **33 upvotes** (16 tot 91). De weekwinnaars van oktober hadden 46 tot 91 upvotes. Klikken naar de site toont DevHunt niet. GOK: als 2 tot 4% van de impressies klikt, is dat voor een gewone lancering 15 tot 35 bezoekers, en voor de top 30 van de maand 60 tot 125.
- **Smol Launch** geeft geen bezoekers, alleen een "Rank score" (stemmen plus bonuspunten): mediaan **6**, 90% haalt hooguit 13, de hoogste ooit 140, over 4.056 lanceringen (DERDEN, hun rapport, stand 8 nov 2026). Wie gratis lanceert moet eerst op 5 anderen stemmen: de stemmen komen dus grotendeels van andere makers die zelf lanceren.
- **TinyLaunch** geeft geen bezoekers. Op de voorpagina hadden de winnaars van vorige week 82, 64 en 30 stemmen, de leiders van deze week 15, 14 en 13 (GEZIEN 16 nov ±16:00). TinyLaunch verdiende sinds dec 2024 **$110.866** (DERDEN, TrustMRR, gecontroleerd via Stripe): het geld komt van makers die betalen om sneller of hoger te staan. Dat is geen bewijs dat het niets oplevert, wel dat het verdienmodel de maker is, niet de bezoeker.

### Wat het oplevert: wat makers zelf zeggen
| Maker | Platform, wanneer | Uitslag | Label |
|---|---|---|---|
| mailsign.online | Uneed (zelfde soort als TinyLaunch), ±dec 2025 | plek 4, ±50 upvotes, **6 bezoekers** naar de site. Hij stemde zelf 10 keer met extra accounts om te testen of het kan ("I'm not the only one doing it") | EIGEN OPGAVE, Reddit r/SaaS 1pdsv8s |
| Focal (YouTube-samenvatter, extensie) | TinyLaunch, 6 juli 2026 | plek 3, "highest single-day" verkeer tot dan (bijna 3 keer het gewone aantal dagelijkse gebruikers), **6 aanmeldingen, 0 betalend** | EIGEN OPGAVE, usefocal.xyz/blog/focal-tinylaunch-third-place |
| Onbekende SaaS (launch 10515) | TinyLaunch, feb 2026 | plek 1, maar "majority of traffic + upvotes came directly from" zijn eigen X-bericht (±2.000 views) en ±50 persoonlijke DM's | EIGEN OPGAVE, r/SaaS 1r0utrq |
| Alex (FrontStat, twee producten, ±20 lijsten) | o.a. DevHunt, Uneed, Microlaunch, sept 2026 | "the best one sent 7 engaged visits" in 3 maanden; één bericht op X gaf 48. Alleen Product Hunt en Show HN sturen "real visitors on the day" | EIGEN OPGAVE, dev.to/alexcommitter (let op: hij verkoopt zelf een meetdienst) |
| Nimply | Product Hunt, 23 sept 2026, niet Featured | 31 punten, geen plek op de ranglijst, ±290 aanmeldingen, maar die kwamen van eigen LinkedIn- en Facebookberichten: "The Product Hunt page was the destination we pointed people at, not the source" | EIGEN OPGAVE, nimply.io/blog/product-hunt-launch-case-study |
| Cliptude | Microlaunch, Uneed, TinyLaunch betaald ($108) plus 3 betaalde X-makers ($150) | 153 gebruikers, niet uitgesplitst per kanaal | EIGEN OPGAVE, r/SaaS 1rrk8de; niet te gebruiken als bewijs voor de platforms |

Product Hunt als ijkpunt: volgens een verzamelpagina krijgt sinds 2024 nog maar ±10% van de lanceringen de status Featured (was 60 tot 98% in 2020 tot 2023), en zonder die status kom je niet op de ranglijst (DERDEN zwak, shno.co die Tetriz.io aanhaalt; Nimply bevestigt het tweede deel uit eigen ervaring).

Geen enkele maker die ik vond, gaf een hoger getal dan een paar dozijn bezoekers uit een van de drie kleine platforms zelf. Waar een lancering wel goed liep, kwamen de bezoekers en stemmen van het eigen bereik van de maker (X, DM's, LinkedIn).

### Past een van onze producten?
- Op Smol Launch staan bij "obsidian" 2 producten (geen van beide een plugin, hoogste Rank score 8), bij "blender" 2 (AI-3D en mocap, geen add-on), bij "jetbrains" 0 (GEZIEN). Onze kopers (3D-printers met Blender, Obsidian-schrijvers, C-ontwikkelaars met CLion) zitten daar niet.
- **Click Joints (gratis en Pro):** geen gereedschap voor ontwikkelaars, dus op DevHunt in de aparte rij "not a dev tool". Smol Launch en TinyLaunch nemen het aan, maar het publiek is makers van SaaS. Verhaal 15 en 16 lieten zien dat de winkel van Blender zelf de motor is (mediaan 11,5 downloads per dag voor een nieuwe add-on, Click Joints ±20) en dat één Reddit-post met een winkellink 1 tot 3 punten haalde. Een lanceerplatform voegt hier volgens alle cijfers hierboven minder toe dan één dag winkel.
- **Bison & Flex:** het enige product dat bij DevHunt past (IDE-plugin voor C-ontwikkelaars). Maar het staat nog verborgen in de keuring van JetBrains (bord: 0 installs, sinds 8 nov). Lanceren kan pas als het zichtbaar is, en kost dan $19 of $49.
- **Rollwright:** geparkeerd (bord). Geen gereedschap voor ontwikkelaars; de Obsidian-gebruikers zitten op het forum en r/ObsidianMD (verhaal 5), niet hier.

### Wat ze in welke volgorde doen (de makers die er iets aan hadden)
1. Eerst eigen bereik opbouwen of klaarzetten (X-bericht met demo, DM's, LinkedIn).
2. Lanceren op een platform als landingsplek, en dat bereik ernaartoe sturen.
3. Achteraf: de link (backlink) en het badge houden, voor zoekmachines en AI-assistenten. Dat is het enige wat ook zonder eigen bereik blijft, en daarvoor hoef je niet hoog te eindigen.

### 3 lessen
1. **Een klein lanceerplatform geeft geen publiek, het vraagt publiek.** De stemmen komen van andere makers (Smol Launch eist het zelfs) en van wat je zelf meebrengt; de enige gedeelde bezoekerscijfers zijn 6 en 7. DevHunt is het enige met een echt publiek en open cijfers, en ook daar is de gewone lancering 822 impressies, geen bezoekers.
2. **Gratis is bijna verdwenen of zit achter een rij van maanden.** Smol Launch gratis: feb 2027. DevHunt gratis lanceren: gestopt in sep 2026, prijzen veranderden 6 keer in 2 maanden. TinyLaunch gratis: 21 dec. Het verdienmodel is de maker die betaalt (TinyLaunch $110.866).
3. **Wat telt is waar je kopers al zijn.** Bij ons zijn dat de winkels zelf (extensions.blender.org, Garmin, JetBrains Marketplace) en de communities per programma (r/blender, r/3Dprinting, Obsidian-forum). Geen van onze drie producten heeft zijn publiek op Smol Launch of TinyLaunch.

### Voorstel voor Dortus deze week
**Geen geld en geen tijd van Thijs in Smol Launch, TinyLaunch of Product Hunt voor Click Joints of Rollwright.** De verspreiding blijft bij het plan van 16 nov 16:44 (Reddit waar de gebruikers zitten) en de dagelijkse filmpjes van Chris. Eén uitzondering om klaar te leggen: **Bison & Flex op DevHunt**, pas als JetBrains het zichtbaar maakt, en alleen als Jet toch een lanceerdag plant. Dan eerst de gratis vaste pagina (kost alleen een account van Thijs), en de betaalde lancering ($19 tot $49) alleen als Thijs dat wil, met een eigen link (`?ref=devhunt`) zodat we de klikken zelf tellen. Wie: Jet zet het klaar zodra Bison & Flex zichtbaar is; Thijs beslist over het geld. Wat zou dit veranderen: een maker in onze hoek (Blender, Obsidian, JetBrains) die met cijfers laat zien dat een van deze platforms installs gaf.

## 16. Hoe werden de snelste nieuwe add-ons van extensions.blender.org bekend? YouTube gezocht bij 40 toppers en 40 gewone add-ons, de zoekplek van Click Joints gemeten, en een correctie op verhaal 15

Onderzocht 16 nov 2026 ±15:00 tot 15:40 UTC, run 16. Waarom: verhaal 15 liet open hoe de groeiers verder bekend werden (YouTube, Discord). Chris begint morgen met dagelijkse filmpjes voor Click Joints, dus de vraag is: hadden de snelle groeiers filmpjes nodig, of kwam het uit de winkel?

### Bronnen en werkwijze
- De 40 snelste en 40 gewone add-ons (willekeurig uit het midden, 9 tot 15 downloads per dag) uit `platformen/succes/data/blender-extensions-nieuw-2026-11-16.csv`, eerste versie dec 2025 tot half okt 2026.
- Per add-on twee zoekopdrachten op YouTube met yt-dlp (`"<naam>" blender` en `<naam> blender addon`, 15 tot 20 uitslagen). Telt alleen als de naam van de add-on in de titel staat. Bij elke video met 10.000+ views heb ik gekeken of hij echt over deze add-on gaat. Datums kon ik maar voor een deel lezen: YouTube vroeg daarna om "bevestig dat je geen bot bent", en daar ben ik gestopt. Tabel: `platformen/succes/data/blender-groeiers-youtube-2026-11-16.csv`.
- Van alle 40 toppers en de 25 add-ons met precies 15 versies de hoofdpagina gelezen voor de echte datum "Published" (GEZIEN).
- Versiegeschiedenis van Loop Resample, Texture Wrangler, Collada Support, Mio3 Flex, Modern Primitive en Paint System (downloads per versie, GEZIEN).
- De zoekfunctie van de website (`extensions.blender.org/search/?q=...`) voor 10 woorden waarop iemand Click Joints zou zoeken (GEZIEN 16 nov ±15:30 UTC).

### Eerst een correctie op verhaal 15
De pagina "Version History" toont hooguit 15 versies. Bij 25 van de 582 add-ons in mijn tabel stonden er precies 15, en dan is de oudste getoonde versie niet de eerste. Vijf van de "snelste nieuwe add-ons" zijn dus helemaal niet nieuw (datum Published, GEZIEN):

| Add-on | Stond in verhaal 15 als | Echt gepubliceerd |
|---|---|---|
| VRM format | jul 2026, 736 per dag | 11 mei 2024 (totaal 341.535) |
| Import Autodesk MAX | apr 2026, 341 per dag | 8 mei 2024 |
| CloudRig | mrt 2026, 176 per dag | 23 mei 2024 |
| Modern Primitive | dec 2025, 135 per dag | 18 dec 2024 |
| Paint System | jan 2026, 150 per dag | 12 feb 2025 |

Wat dat verandert: de mediaan van 11,5 per dag blijft vrijwel gelijk (25 van 582, en de meeste daarvan liggen dicht bij hun echte begin). Maar de top 8 van echt nieuwe add-ons van 2026 is: Collada Support 201, Wiggle Bones 200, Loop Resample 195, Wiggle 2: RTX Edition 168, Texture Wrangler 164, Retarget 136 (dec 2025), Dolly Zoom 125, Light It Up 118 per dag. Daarvan vullen er **3 van de 8** een gat dat Blender 5 of een verlaten add-on maakte (Collada en de twee Wiggle-vervangers), niet 5 van de 8. De les "bouw voor een gat waar mensen al naar zoeken" blijft het sterkste patroon in de top, maar is zwakker dan ik schreef. Formaten van andere programma's die wel echt nieuw zijn: CAD2Cube (DXF) 99 en KN5 Tools (Assetto Corsa) 62 per dag.

### Cijfers YouTube (GEZIEN)
| | Toppers (n=40) | Gewone add-ons (n=40) |
|---|---|---|
| Minstens één video met de naam in de titel | 16 | 13 |
| Een video met 10.000+ views en de naam in de titel | 12 | 2 |
| Waarvan na nakijken echt over deze add-on, en de add-on is van 2026 | **1** (Mio3 Flex) | **0** |

Wat er achter die 12 zit:
- **Oude add-on, niet nieuw** (4): VRM, CloudRig, Paint System, Modern Primitive. Dynamic Parent staat pas sinds mei 2026 in de winkel, maar de video's erover lijken ouder (GOK, datums niet gelezen).
- **Naam botst met een gewoon woord** (4): Dolly Zoom (een camerakunstje, uitlegvideo uit 2023), Light It Up (een liedje), Dimensions (een video uit 2020 over iets anders), Retarget (algemene uitleg over animaties overzetten, niet nagekeken of het over deze add-on gaat).
- **Video over de voorganger of het probleem** (2): Wiggle Bones (Joey C-quel, "Wiggle Bones 2 Blender addon and how to use it", 109.115 views, jan 2024, over de oude add-on die in Blender 5 kapot ging) en Collada Support (MorzBNG, "Blender ends COLLADA support with 5.0, what now?", 11.646 views, 24 nov 2025, acht maanden vóór de add-on).
- **Echt** (1): Mio3 Flex, video van Blender Secrets (13.421 views, datum niet gelezen). De maker "mio" heeft ook Mio3 UV gemaakt (321.000 downloads, staat op de voorpagina van de winkel), dus zijn naam was al bekend.
- Bij de gewone add-ons: eigen filmpjes van makers met 13 tot 411 views (EasyShelf, Bone Math, Keymap Visualizer, FBX Scale Report, Auto Paint Boundaries), en twee naambotsingen.

**Zonder enige video met hun naam groeiden** onder meer Texture Wrangler (164 per dag), Wiggle 2: RTX Edition (eigen Koreaanse video 974 views), Loop Resample (eigen video 42 views), Bezier Curve Editor (116), Loopkut (113), CAD2Cube (99), EasySlice Print (89), Easy-Print (69) en Photo Relief (eigen video's 73 en 181 views).

### Wat de versies laten zien (GEZIEN)
| Add-on | Begin | Daarna |
|---|---|---|
| Loop Resample | 2.838 downloads in de eerste 14 dagen na de keuring (±203 per dag) | 204 tot 235 per dag, steeds gelijk |
| Texture Wrangler | 4.204 in 27 dagen (±156 per dag) | 191 per dag |
| Mio3 Flex | 3.183 in de eerste 9 dagen (±350 per dag) | 72 per dag: een golf bij de start, dan rustiger |
| Collada Support | versie 1: 42 downloads in 30 dagen | versie 2: 267 per dag. Waarom versie 1 bijna niets deed, zie ik niet (GOK: verkeerde Blender-versies opgegeven) |

Loop Resample en Texture Wrangler laten geen golf zien maar een vlakke stroom vanaf dag 1, zonder video en met een Reddit-bericht van 1 punt (verhaal 15). Dat past bij mensen die in de winkel of in Blender zelf zoeken.

### Paint System: de andere route, met een eigen kanaal
Paint System is de duidelijkste add-on waar YouTube wel meetelt, maar het is een add-on van 2025 en de video's zijn van de maker zelf: kanaal Tawan Sunflower (38.600 abonnees), "Turning Blender into Photoshop | Paint System addon Tutorial" 505.319 views (1 jan 2025, zes weken vóór de winkel), "Quickly explaining about Blender Paint System 2.0" 20.778 views (7 sep 2025, met link naar de winkel), en een derde van 52.039 (20 nov 2025). Daarna volgden anderen: BlenderHub 15.148 (jan 2025), Red-Sensei 41.384 (jun 2025), askNK 101.788 en Zha Art 141.582 (datums niet gelezen). Nu, bijna twee jaar later, nog ±150 downloads per dag. Mijn lezing: een lange eigen uitlegvideo met een sterke belofte in de titel kan een add-on dragen, maar het gaat om één geval met een maker die al een kanaal had.

### Click Joints in de zoekfunctie van de website (GEZIEN 16 nov)
| Zoekwoord | Plek Click Joints |
|---|---|
| joint, joints, ball joint, poseable | **1** |
| figure | 16 |
| 3d print, print | **niet in de eerste ±30** (wel EasySlice, Easy-Print, SnapSplit, MoldForge, 3D Print Toolbox) |
| articulated, action figure, hinge | niet gevonden |

De korte omschrijving is "Ball joints for 3D printed figures that show their bend range". De zoekfunctie lijkt op hele woorden te zoeken: "printed" telt niet als "print". De print-add-ons met "Print" in naam of omschrijving staan wel bovenaan. Let op: Blender zelf zoekt in het venster Get Extensions op een eigen manier; dat heb ik niet gemeten (GOK dat daar "print" in "printed" wel gevonden wordt).

### Drie lessen
1. **De snelle groeiers van 2026 werden niet bekend via YouTube of Reddit.** Van de echt nieuwe add-ons in de top 40 had er 1 een video van een ander met 10.000+ views; de rest groeide met eigen filmpjes van tientallen views of zonder filmpje, en met Reddit-berichten van 1 tot 3 punten. Het bereik komt uit de winkel en de zoekfunctie (klopt met verhaal 9 en 15).
2. **Waar YouTube wel meetelt, is het een bekende naam of een lange eigen uitleg, niet een kort filmpje.** Mio3 Flex had de naam van Mio3 UV mee en een golf van ±350 per dag in de eerste week; Paint System groeide op de eigen tutorial van de maker (505.000 views). Dit sluit aan bij verhaal 5 (Notebook Navigator: lange uitlegvideo's 110.000 tot 118.000 views, korte 8.200 tot 16.000).
3. **Gevonden worden op het woord dat mensen typen.** De vervangers dragen de naam die mensen al zoeken (Wiggle, Collada) en de print-add-ons hebben "Print" in naam of omschrijving. Click Joints staat op 1 voor "joint" maar is onvindbaar op "3d print", het woord waar de grootste groep (mediaan 20 per dag, verhaal 15) op zoekt.

### Eerlijk: wat deze meting niet zegt
- Zoeken op naam mist video's die de add-on noemen zonder naam in de titel (zoals "3 Painting Add-Ons in Blender"), en Discord, X, en sites in Japan en China heb ik niet kunnen meten.
- Datums van video's ken ik maar voor 13 video's; voor de rest weet ik niet of de video vóór of na de groei kwam.
- De zoekplek is één meting op één moment, op de website. Of mensen vooral op de site of in Blender zoeken, weet ik niet.
- Een filmpje kan nog steeds mensen naar de winkel sturen zonder dat het in mijn tellingen zichtbaar is; mijn conclusie is dat de groeiers het niet nodig hadden, niet dat filmpjes niets doen.

### Voorstel voor Dortus deze week
**Bram: zet de woorden "3D print" letterlijk in de korte omschrijving van gratis Click Joints bij de volgende versie**, bijvoorbeeld "Ball joints for 3D print figures, with bend range" (onder de 64 tekens), en kijk of de tags Mesh en Modeling kunnen blijven. Meet daarna met dezelfde zoekopdracht (`/search/?q=3d%20print`) of Click Joints in de lijst komt, en volg de downloads per dag op de versiepagina (nu 20 per dag). Waarom: in de winkel komt het bereik uit zoeken; op "joint" staan we al op 1, maar op "3d print" zijn we onzichtbaar terwijl de print-add-ons die daar staan 3 tot 4 keer zoveel halen. Kost één regel tekst en past binnen de regels van extensions.blender.org (geen reclame voor Pro). **Chris:** blijf filmen voor de kijker (tips en vragen), maar reken niet op het filmpje voor de downloads van gratis Click Joints; die komen uit de winkel. Een langere uitlegvideo ("hoe maak je een printbaar figuur met gewrichten in Blender") is volgens Paint System en Notebook Navigator de vorm die een add-on draagt.

---

## 15. Wat laat een gratis add-on op extensions.blender.org snel groeien? 470 nieuwe add-ons (dec 2025 tot okt 2026) gemeten, naast de 13 Reddit-berichten die rechtstreeks naar die winkel linken

**Correctie 16 nov ±15:40 UTC (verhaal 16): VRM, Import Autodesk MAX, CloudRig, Modern Primitive en Paint System zijn niet nieuw (gepubliceerd 2024 en begin 2025); de versiepagina toont hooguit 15 versies. Van de echt nieuwe top 8 vullen 3, niet 5, een gat van Blender 5 of een verlaten add-on.**

Onderzocht 16 nov 2026 ±14:05 tot 15:05 UTC, run 15. Waarom: in verhaal 9 bleek dat bijna niemand op r/blender naar extensions.blender.org linkt, dus het effect van een bericht op een gratis add-on bleef open. Tegelijk is die winkel ons grootste kanaal voor Click Joints (gratis, ±19 per dag zonder bericht). Vraag: waar komen de downloads van de snelle groeiers vandaan, en wat doen zij anders dan Click Joints?

### Bronnen en werkwijze
- Lijst: `https://extensions.blender.org/api/v1/extensions/` (1.662 extensies, 1.359 add-ons, GEZIEN 16 nov).
- Per add-on de pagina "Version History" (`/add-ons/<naam>/versions/`): elke versie met datum en downloads. 1.206 van de 1.359 pagina's gelezen, 1.190 bruikbaar (de rest had een andere webnaam dan de id). Daarna van alle 618 add-ons met een eerste versie vanaf 1 nov 2025 de hoofdpagina: plaatjes, video, beschrijving, website (GEZIEN, rustig, 4 tegelijk met pauze).
- Maat: **downloads per dag** = alle downloads samen gedeeld door het aantal dagen sinds de eerste versie. Updates tellen mee (wie bijwerkt downloadt opnieuw), dus dit is een bovengrens voor nieuwe gebruikers. De eerste versie staat soms dagen in de keuring met bijna 0 downloads (Easy-Print: 14 op dag 1, daarna 2.710 met de tweede versie), dus voor heel jonge add-ons is het een ondergrens.
- Reddit: Arctic Shift, alle berichten waarvan de link naar `https://extensions.blender.org` gaat, juni 2024 tot nu, alle subreddits (13 berichten, GEZIEN). Zoeken op naam in r/blender, r/3Dprinting en r/functionalprint gaf deze run vooral "Too many requests"; alleen voor Texture Wrangler kwam een antwoord.
- Tabel zonder persoonsgegevens: `platformen/succes/data/blender-extensions-nieuw-2026-11-16.csv` (582 add-ons met eerste versie vanaf nov 2025).

### Cijfers (GEZIEN tenzij anders vermeld)
| Wat | Cijfer |
|---|---|
| Nieuwe add-ons, eerste versie 1 dec 2025 tot 15 okt 2026 (n=470): downloads per dag | p25 **5,6**, mediaan **11,5**, p75 **24,6**, p90 **53,9** |
| Lichting jun 2025, nu ±17 maanden oud: mediaan totaal | 8.050 (±15 per dag, met updates) |
| Lichting aug 2026, ±3 maanden oud: mediaan totaal | 1.038 (±11 per dag) |
| Click Joints (8 nov): 162 in 8 dagen | **20 per dag**, plek 41 van 119 add-ons uit okt en nov |
| Berichten op heel Reddit met een link rechtstreeks naar de winkel (jun 2024 tot nu) | **13**, score 1 tot 3 |
| Texture Wrangler (11 okt): bericht op r/blender "I made a free add-on that renames and sorts your texture downloads..." | score **1**, en toch **156 tot 190 per dag** in de winkel |
| Met video in de galerij tegen zonder (n=111 tegen 101) | mediaan 12,7 tegen 11,5 per dag |
| Beschrijving 200+ woorden tegen minder dan 60 | mediaan 14,4 tegen 9,2 per dag |
| Add-ons die een betaalde versie noemen (Superhive, Gumroad, Pro) | 9 stuks, mediaan 5,2 per dag (te weinig om iets te zeggen) |

**De snelste groeiers van 2026** (downloads per dag sinds de eerste versie):

| Add-on | Per dag | Wat het oplost |
|---|---|---|
| VRM format | 736 | import en export van een formaat voor avatars (VRoid, VTubers) |
| Import Autodesk MAX (.max) | 341 | bestanden van 3ds Max openen |
| Collada Support | 201 | "Restores COLLADA import and export for Blender 5 after native OpenCOLLADA support was removed" (eigen tekst, DERDEN) |
| Wiggle Bones | 201 | "Refactor of Wiggle 2, fully fixed for Blender 5.0" |
| Loop Resample | 195 | randen opnieuw verdelen; ±200 per dag vanaf de dag na de keuring |
| CloudRig | 176 | gereedschap van Blender Studio zelf |
| Wiggle 2: RTX Edition | 168 | een tweede vervanger van dezelfde verlaten add-on |
| Texture Wrangler | 164 | texturen hernoemen en in mappen zetten |

**3D-print-add-ons apart** (15 stuks met print, STL, 3MF of mal in naam of zin; mediaan **20 per dag**, dus bijna het dubbele van alle add-ons):

| Add-on | Per dag | Wat het doet |
|---|---|---|
| EasySlice Print | 89 | groot model in stukken snijden met verbindingen |
| Easy-Print | 69 | "Cut models and generate interlocking connectors" |
| Papercraft Pro | 67 | uitvouwen tot papieren bouwplaat |
| Photo Relief | 65 | foto naar reliëf of lithofaan |
| MoldForge | 57 | siliconenmal uit een model |
| SnapSplit | 35 | snijden met verbindingen |
| EasyMold | 28 | mallen |
| **Click Joints** | **20** | kogelgewricht in een figuur, met buigbereik |
| Print Prep, Batch STL, Keychain Builder, Weathered Board, Polyshell, MiniSlicer | 7 tot 16 | |

### Wat ik zag
1. **De winkel zelf is de motor, niet het bericht.** Alle 13 berichten op Reddit met een link naar de winkel bleven op 1 tot 3 punten, en Texture Wrangler groeide naar ±160 per dag met een bericht van 1 punt. Een add-on die gekeurd is, krijgt in de winkel en in Blender zelf een vaste stroom, mediaan ±11 per dag, en die stroom houdt maanden aan (lichting juni 2025 nog ±15 per dag gemiddeld).
2. **De grootste groeiers vullen een gat dat Blender zelf maakte of dat iemand anders liet liggen.** Collada verdween uit Blender 5 en een vervanger haalt 200 per dag; Wiggle 2 werkte niet meer en twee vervangers halen samen ±370 per dag; formaten van andere programma's (3ds Max, VRM, DXF met 99 per dag) staan bovenaan. Mijn lezing (GOK): mensen zoeken in de winkel naar een naam of een formaat dat ze al kennen. Niet alle toppers passen: Loop Resample en Texture Wrangler zijn gewoon handige klussen.
3. **Het uiterlijk van de pagina maakt weinig verschil.** Met of zonder video, veel of weinig plaatjes: de medianen liggen binnen 1 tot 3 downloads per dag van elkaar. Een langere beschrijving gaat iets samen met meer downloads (14 tegen 9), maar dat kan ook komen doordat grotere add-ons meer te vertellen hebben.
4. **Bij 3D-printen wint de brede klus.** De vijf snelste print-add-ons doen wat bijna elke printer een keer nodig heeft: een groot model in stukken met verbindingen, een mal, een lithofaan. Click Joints doet een smallere klus (gewrichten in figuren) en staat precies op de mediaan van de printgroep, boven de helft van alle nieuwe add-ons.
5. **Wie vaak bijwerkt, telt meer downloads**, maar dat is grotendeels optelwerk: elke update laat bestaande gebruikers opnieuw downloaden. Of een update ook nieuwe mensen trekt, kan ik met deze cijfers niet scheiden.

### Drie lessen
1. **Op extensions.blender.org komt het bereik uit de winkel, niet uit Reddit.** Een bericht met een link naar de winkel scoort 1 tot 3 punten; de groeiers groeiden zonder. Dit klopt met verhaal 7, 8 en 9 (Garmin en r/blender): de winkel geeft meer dan de post.
2. **Het snelst groeit een gratis add-on die een gat vult waar mensen al naar zoeken:** iets wat Blender net weghaalde, een populaire add-on die kapot ging, of een formaat van een ander programma. Bouw voor de zoekterm die al bestaat.
3. **Poetsen aan de pagina levert weinig op; de klus die het oplost bepaalt de stroom.** Binnen 3D-printen doen de brede klussen (stukken met verbindingen, mallen, reliëf) 3 tot 4 keer zoveel als Click Joints.

### Eerlijk: wat deze meting niet zegt
- Downloads per dag zijn een gemiddelde over het hele leven, met updates erin; het verloop per week zie ik alleen per versie.
- 153 add-ons konden niet gelezen worden (andere webnaam); de groep tot nov 2025 is daardoor iets kleiner, de nieuwe groep is volledig voor zover de lijst reikt.
- Ik weet niet hoe de makers van de groeiers verder bekend werden (YouTube, Discord, sites in Japan of China). Reddit op naam zoeken lukte deze run niet door de grens van het archief; alleen Texture Wrangler is nagekeken.
- "Gat dat Blender maakte" is mijn lezing van de namen en zinnen van de toppers (5 van de bovenste 8 passen erin: VRM, 3ds Max, Collada en de twee Wiggle-vervangers; CloudRig is een bekende naam van Blender Studio zelf; Loop Resample en Texture Wrangler passen er niet in). Het is een patroon in een top, geen proef.

### Voorstel voor Dortus deze week
**Ruben en Daan: kies de volgende gratis add-on (bereik, met een wegwijzer naar betaald werk via de website) met de vraag "welk gat heeft Blender 5 of een verlaten add-on net gemaakt in 3D-printen?"** Maak een lijst van 3D-print-add-ons die niet meer werken in Blender 5 (oude 3D-Print Toolbox-achtige gereedschappen, splitters, STL-gereedschap) en van functies die Blender 5 weghaalde, en zoek per kandidaat in de winkel of er al een vervanger is. Waarom: 5 van de 8 snelste groeiers van 2026 halen 170 tot 740 per dag met precies zo'n gat, een gewone nieuwe add-on 11. Ruben's twee eerdere kandidaten vielen af op de concurrentiecheck (besluit 16 nov 13:00); deze vraag geeft een nieuwe ingang die de check meteen meeneemt. Voor Chris: een Reddit-bericht voor Click Joints is de moeite als video (verhaal 9), maar verwacht er geen downloads in de winkel van; meet de winkel de dag ervoor en 3 dagen erna, zoals al gepland.

---

## 14. SPOED: waarom heeft Ebb na 3 dagen 0 downloads? Zoekplek, de nieuwe ademhalingsapps ernaast, en of de teller achterloopt

Onderzocht 16 nov 2026 ±13:00 tot 13:45 UTC, run 14, opdracht van de hoofdchat (13:50 NL). Ebb ($4,99, Garmin Pay) staat sinds 13 nov 15:09 UTC in de winkel (`firstApprovalDate` in de API; in `meting-ebb.md` staat ±21:09 UTC, maar de API zegt 15:09 UTC). Op 16 nov 13:15 UTC: 0 downloads, 0 reviews, Ebb Calm nog steeds 404 (GEZIEN). Dit is geen succesverhaal maar een meting naast de winnaars. Geen medische beloftes: de voorstellen hieronder gaan over vindbaarheid, horloges en prijs, niet over wat ademen met je doet.

**Bronnen (alles GEZIEN met curl of een klein Python-script op de openbare winkel-API, 16 nov ±13:00 tot 13:15 UTC):**
- Ebb zelf: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/5280653d-1681-452d-8c03-7cbdc7284641`.
- Zoekbalk: `.../api/asw/apps/keywords?keywords=<woord>&startPageIndex=<n>&pageSize=30&sortType=mostRelevant`, met en zonder `&appType=watch-app`, tot 300 resultaten per woord, 14 woorden.
- Details van 1.314 apps (alle ademhalingsachtige uit de zoekresultaten plus de 1.197 apps uit de lijst `sortType=mostRecent`), met eerste goedkeuring, prijs, downloadklasse, categorie, talen en horloges.
- Horlogenamen: `.../api/asw/deviceTypes`; categorienamen: `.../api/categories`.
- Tabel van de 33 nieuwe ademhalingsapps (16 aug tot 16 nov, zonder mailadressen): `platformen/succes/data/ebb-ademapps-nieuw-2026-11-16.csv`.

Let op: de downloadteller is een klasse (0, 1, 10, 100, 1000, ...). "1" betekent 1 tot 9. Ebb op 0 betekent dus echt nul, niet "een paar".

### Vraag 3 eerst: telt de API met vertraging?
Nee, niet merkbaar. Ebb kwam in dezelfde goedkeuringsronde als 37 andere apps (13 nov 14:52 tot 15:16 UTC). Op 16 nov 13:00 UTC stonden die zo (GEZIEN):

| Ronde 13 nov | 0 | 1 tot 9 | 10 tot 99 | 100+ |
|---|---|---|---|---|
| Gratis (26) | 1 | 13 | 8 | 4 |
| Betaald (12) | 3 (o.a. Ebb) | 9 | 0 | 0 |

De ronde van 12 nov geeft hetzelfde beeld: betaald 2 keer 0 en 7 keer 1 tot 9, gratis tot 100+. Gratis apps van dezelfde dag staan al op 100+, dus de teller loopt bij. Wat wel opvalt: **geen enkele betaalde app uit deze twee rondes heeft na 3 tot 4 dagen 10 of meer.** Een betaalde app begint dus altijd traag, en 0 tegen "1 tot 9" is een verschil van een paar kopers. Ebb zit in het slechtste kwart, maar het is geen ramp die alleen Ebb treft. Hetzelfde zie je bij Vytera Breath ($4,99, ademhaling, 23 okt): na 24 dagen nog steeds 0, terwijl het gratis broertje Vytera Breath Free op 10+ staat.

### Vraag 1: is Ebb te vinden?
Plek van Ebb in de zoekbalk (GEZIEN, 13:05 UTC). Eerste getal: alle soorten door elkaar (wijzerplaten erbij); tweede: alleen apps (`appType=watch-app`), met het aantal apps dat op dat woord gevonden wordt.

| Zoekwoord | Alles | Alleen apps | Aantal apps |
|---|---|---|---|
| ebb | 1 | 1 | 88 (alles) |
| breath hold | 4 | 4 | 376 |
| calm | 42 | 3 | 66 |
| 478 | | 3 | 7 |
| breathe | 16 | 15 | 202 |
| breath | 19 | 17 | 239 |
| breathing | 29 | 28 | 307 |
| breathwork | 32 | 28 | 208 |
| box breathing | 53 | 36 | 346 |
| relaxation | | 43 | 86 |
| relax | niet in 120 | niet gevonden | 64 |
| meditation, mindfulness, stress, hrv | niet gevonden | niet gevonden | |

Ebb staat goed op "breath hold" en "calm", maar op het grote woord "breathing" pas op plek 28, dus op de tweede of derde scherm. Waarom? **De zoekbalk zet korte namen met het zoekwoord erin bovenaan.** Op "breathing" hebben de nummers 1 tot 15 allemaal het woord in de naam, mediaan 2 woorden; op plek 16 tot 60 mediaan 5 woorden. Op "breath" hetzelfde: 3 tegen 6 woorden (GEZIEN). Downloads tellen nauwelijks mee: nummer 1 op "breathing" is "Box Breathing" met 10 tot 99 downloads. Ebb heet "Ebb: Breathing Exercises, Breath Hold & Calm": 6 woorden in het Engels, en in het Nederlands en Duits nog langer. Dat het zo werkt is mijn lezing van wat ik zie, niet van Garmin bevestigd (GOK op het mechanisme, GEZIEN op de patronen). Ook: "box breathing" (346 apps) is het woord van twee van de beste nieuwkomers, en Ebb heeft geen box-patroon. "relax" en "stress" vinden Ebb niet; die woorden staan niet in de tekst.

### Vraag 2: wat doen de best gedownloade nieuwe ademhalingsapps anders?
Van de 33 ademhalingsapps die tussen 16 aug en 16 nov in de winkel kwamen, haalden er 7 al 100+ (GEZIEN). Vergelijking met de andere 26:

| | 100+ (7) | rest (26) | Ebb |
|---|---|---|---|
| Gratis | 6 van 7 | 21 van 26 | nee, $4,99 |
| Horloges (mediaan soorten) | 183 | 53 | 40 |
| Talen (mediaan) | 4 | 1 | 3 |
| Woorden in de naam (mediaan) | 4 | 3 | 6 |

De drie die het verst kwamen, plus één die het snelst ging:

1. **Breathe Free: Box Breathing** (FikirLtd, 20 aug, gratis, 100+, 5 reviews). 219 horloges, categorie Health and Fitness > Other, 5 talen. Eerste zin: "Guided box breathing on your wrist, free." Icoon: een gloeiende cirkel op een echt horloge. Eerste plaatje: het scherm met "Box Breathing 4-4-4-4, free, forever". De maker heeft 30+ andere apps (Run Cue 1000+), dus bezoekers van zijn andere apps zien hem ook.
2. **Heart Coherence & HRV Breathing Biofeedback** (Pacy, 23 okt, gratis, 100+, 5 reviews). 149 horloges, Wellness, 4 talen. Eerste zin noemt het gemis: "Garmin's built-in breathwork timer paces your breathing, but it doesn't show you if..." Plaatjes: acht schermen naast elkaar.
3. **Vagal, HRV breathing coach** (ThijsGer, 28 sep, $1,99, 100+, 4 reviews): de enige betaalde nieuwkomer met 100+. 101 horloges, 16 talen, 30+ andere apps van dezelfde maker. Plaatje: echt horloge op wit met één zin.
4. Snelste: **Breathe: Box Breathing** (scheir.eu, 9 nov, gratis): 100+ in 7 dagen. 223 horloges, 19 talen, naam van 3 woorden, plek 2 op "box breathing" en 10 op "breathing". Eerste zin: "A guided breathing exercise for stressful moments, before sleep or before a race." Deze maker heeft ook 30+ apps.

Wat níet het verschil maakt: het uiterlijk. De iconen en plaatjes van de winnaars zijn kaal (een cirkel, een getal); die van Ebb zijn mooier en vertellen meer (patrijspoort met walvis, "Breathe. Make sea friends."). Ook niet de categorie: Wellness tegen Other geeft bij alle 83 ademhalingsapps met het woord in de naam 48% tegen 52% met 100+ (GEZIEN), te weinig verschil om op te sturen.

### Wat ik concludeer
1. **0 na 3 dagen is voor een betaalde app van $4,99 zonder reviews niet vreemd.** Geen betaalde app uit dezelfde rondes haalde al 10. Zonder verandering verwacht ik dat Ebb deze maand in de klasse 1 tot 9 komt (GOK, uit de tabel hierboven en verhaal 8: 46% van de betaalde apps haalt 100+, maar pas na maanden).
2. **De grootste rem is het aantal horloges.** Ebb draait op 40 soorten, de winnaars op 150 tot 220. In de Connect IQ-app op de telefoon zie je alleen apps voor je eigen horloge (zo werkt de winkel, niet apart nagemeten), dus voor iemand met een Forerunner 255S, fēnix 7S, Venu 2S of vívoactive 4 bestaat Ebb niet. Ebb mist zelfs de kleine maten van horloges die het wel heeft: Forerunner 255S, 255 Music, 255S Music en 265S, fēnix 7S en 7S Pro, Venu 2S en Venu 2 Plus, epix (Gen 2), fēnix 7 Pro Solar zonder wifi (GEZIEN, lijst uit `deviceTypes`).
3. **De naam is te lang voor de zoekbalk** en de prijs is hoog naast een veld waar 6 van de 7 snelle nieuwkomers gratis zijn. Ebb Calm, de gratis ingang, is na 2 dagen nog niet goedgekeurd.

### De 3 dingen voor Gijs en Mila (ook in `berichten/gijs.md`)
1. **Meer horloges, te beginnen met de ronde broertjes die Ebb al bijna heeft** (Gijs, met Mila voor de plaatjes per maat). Stap 1: Forerunner 255S, 255 Music, 255S Music, 265S, fēnix 7S, 7S Pro, Venu 2S, Venu 2 Plus, epix (Gen 2), fēnix 7 Pro Solar (no Wi-Fi), en de nieuwe fēnix 9-reeks, Enduro 3, D2 Mach 2 en MARQ (Gen 2) als die dezelfde schermmaten hebben als horloges die Ebb al heeft (GOK welke dat precies zijn; Gijs ziet het in de SDK). Stap 2, met een geheugentoets: vívoactive 4 en 4S, Forerunner 245, 745, 945, fēnix 6-reeks, Venu (1). Vierkant en Instinct blijven later, zoals in het ontwerp staat. Waarom eerst: de 7 nieuwkomers met 100+ zitten op mediaan 183 horloges, de rest op 53, Ebb op 40.
2. **Kortere naam met het zoekwoord vooraan, in alle drie de talen** (Gijs past het aan bij de volgende upload; Chris kijkt de tekst na). Voorstel EN: "Ebb Breathing & Breath Hold" (5 woorden, beide sterke woorden erin) of korter "Ebb Breathing". NL en DE net zo kort ("Ebb Ademhaling & Adem inhouden", "Ebb Atmung & Atem anhalten"). Zet "relax" en "box breathing" alleen in de beschrijving als Ebb het echt doet: een vast patroon "Box 4-4-4-4" naast Calm 4-7-8 kost weinig (Ebb heeft al My pattern) en opent het woord met 346 apps. Meten: de plek op "breathing", "breath" en "box breathing" de dag na de update.
3. **Een gratis ingang, en de prijs tijdelijk lager** (Gijs, met de hoofdchat; de prijs zet Thijs in zijn account). Ebb Calm openbaar krijgen is het belangrijkste; staat hij morgen nog op 404, dan via de lijst van Thijs navragen of hij in de keuring hangt of is afgewezen. Daarnaast voorstel: Ebb tijdelijk op $2,99 tot de eerste 5 reviews (de enige betaalde nieuwkomer met 100+ kost $1,99; Ebb en Vytera Breath op $4,99 staan allebei op 0). Dat is een GOK op basis van 6 betaalde nieuwkomers, dus de hoofdchat beslist. Geen medische woorden in de nieuwe tekst: geen "stress relief", "anxiety", "apnea training" of "freediving".

**Voorstel voor Dortus deze week:** Gijs doet punt 1 en 2 in één update (versie 1.0.1 met meer horloges en de nieuwe naam), Mila maakt de plaatjes voor de nieuwe maten, de hoofdchat beslist over de prijs. Meten in `meting-ebb.md`: zoekplekken en downloadklasse op de dag van de update en 7 dagen erna. Doel: Ebb 1 tot 9 binnen een week na de update, Ebb Calm 10+ binnen een week na goedkeuring (GOK).

**Wat ik niet weet:** hoeveel mensen op welk woord zoeken (de winkel geeft geen zoekvolumes); of de telefoon-app precies dezelfde volgorde geeft als de API; hoeveel mensen een horloge hebben dat Ebb mist (geen verkoopcijfers per model). De lijst `mostRecent` liep tot 13 nov 15:16 UTC; latere goedkeuringen zitten er niet in.

### 3 lessen
1. **Een betaalde Garmin-app zonder reviews begint altijd traag:** in de eerste 3 tot 4 dagen haalt geen enkele betaalde app uit twee rondes 10 downloads, gratis apps uit dezelfde ronde wel 100+. Beoordeel een betaalde app niet na 3 dagen.
2. **Het aantal horloges is bij Garmin een groter knopje dan het plaatje.** Winnaars draaien op 150 tot 220 soorten, wij op 40; elk horloge dat ontbreekt is een klant die ons niet kan zien.
3. **De zoekbalk beloont een korte naam met het zoekwoord erin.** Een lange naam vol zoekwoorden werkt bij Garmin juist tegen.

---

## 13. Hetzelfde korte filmpje op TikTok én YouTube Shorts: 317 paren bij 11 makers (3D-printen, Blender, maken) gepaard gemeten. Waar haalt dezelfde clip meer, en wat ging er mis bij een kleine maker die drie keer per dag plaatste?

Onderzocht 16 nov 2026, run 13. Waarom: Chris begint di 17 nov met dagelijkse filmpjes op @dortusstudio, zowel op YouTube als op TikTok. In verhaal 10 en 11 maten we de twee los, bij verschillende kanalen. Dat zegt niet waar dezelfde clip het meest oplevert. Hier dezelfde maker, hetzelfde filmpje, op beide plekken: dan valt het verschil in maker en onderwerp weg.

### Bronnen en werkwijze
- yt-dlp 2026.10.26, openbare profielen, niet ingelogd, GEZIEN 16 nov ±11:55 tot 12:10 UTC. Per maker de volledige TikTok-lijst (kop, datum, lengte, views) en het tabblad Shorts op YouTube (kop, views). Voor elke kandidaat de echte YouTube-pagina gelezen (datum en precieze views).
- Een paar telt alleen als de koppen sterk overeenkomen (75%+ van de woorden van de YouTube-kop staat in de TikTok-tekst) **en** de datums hooguit 7 dagen uit elkaar liggen. Steekproef van 3 per maker met de hand bekeken. Zonder de datumeis zaten er bij 5 makers foute paren in; met de eis bleven er 317 over. Alle paren: `platformen/succes/data/tiktok-vs-shorts-paren-2026-11-16.csv`.
- Volgers: TikTok uit de openbare profielpagina (curl), YouTube uit yt-dlp, GEZIEN 16 nov.
- 22 makers geprobeerd; 11 hadden een leesbare lijst op beide plekken met paren. Niet gevonden of niet leesbaar op YouTube: VAW.BE, Artinvader_, Fat13Creations, Ducky3D, Blender Tips. Ongeveer 70 YouTube-pagina's gaven een blokkade ("not a bot"); die paren vallen weg.
- Hoe views geteld worden: YouTube telt sinds 31 maart 2025 elke start en herstart van een Short als view, eerder pas na een aantal seconden ([TechCrunch, 26 mrt 2025](https://techcrunch.com/2025/03/26/youtube-is-changing-how-youtube-shorts-views-are-counted/), DERDEN). Instagram maakt sinds 2021 Reels met een watermerk of logo van een andere app "less discoverable" (verklaring van Instagram, geciteerd door [XDA](https://www.xda-developers.com/psa-do-not-upload-tiktok-instagram-reels-without-removing-watermark/), DERDEN).

### Uitkomst per maker (mediaan per paar, GEZIEN)
| Maker | Paren | TikTok mediaan | Shorts mediaan | Shorts / TikTok | Shorts wint | Volgers TikTok | Abonnees YouTube |
|---|---|---|---|---|---|---|---|
| 3dprintdood (printtips) | 135 | 6.339 | 14.054 | 1,9 | 85 van 135 | 15.000 | 131.000 |
| marsgizmo (printontwerpen) | 67 | 15.900 | 140.108 | 8,2 | 57 van 67 | 982.200 | 3.040.000 |
| mixtapeprints (kleine printwinkel) | 49 | 103 | 106 | 1,75 | 29 van 49 | 106 | 46 |
| kaivertigoh (drones, maken) | 19 | 2.858 | 25.978 | 3,6 | 18 van 19 | 171.300 | 260.000 |
| Blender Secrets | 13 | 975 | 20.395 | 10,0 | 12 van 13 | 11.800 | 292.000 |
| McGybeer (beweegbare prints) | 13 | 1.870 | 1.365 | 1,1 | 7 van 13 | 43.300 | 7.330 |
| Emily the Engineer | 10 | 326.100 | 292.454 | 2,0 | 6 van 10 | 3.300.000 | 771.000 |
| Brock Creative (Blender) | 4 | 22.850 | 5.579 | 0,22 | 0 van 4 | 141.300 | 15.900 |
| SouthernShotty (Blender) | 3 | 1.054 | 15.834 | 8,9 | 3 van 3 | 4.729 | 321.000 |
| ali3dprint (sleutelhouders) | 2 | 6.996 | 66.518 | 9,1 | 2 van 2 | 1.530 | 21.000 |
| Cinderwing3d (printdraken) | 2 | 21.150 | 3.842 | 0,17 | 0 van 2 | 12.200 | 571 |
| **Alles** | **317** | | | **2,85** | **219 van 317 (69%)** | | |

### Wat ik zag
1. **Dezelfde clip haalt op Shorts meestal meer: mediaan 2,85 keer, in 69% van de paren, bij 9 van de 11 makers** (GEZIEN). Het verschil is groter na de nieuwe telling van YouTube: paren van vóór april 2025 mediaan 1,9 keer, daarna 4,0 keer. Een deel van de voorsprong is dus telwijze, geen echte kijkers (de omvang daarvan is een GOK).
2. **TikTok won alleen waar de maker daar al veel groter was.** Brock Creative (141.300 tegen 15.900) en Cinderwing3d (12.200 tegen 571): TikTok 4 tot 6 keer meer. Maar McGybeer heeft op TikTok 6 keer zoveel volgers en haalt op Shorts toch evenveel per clip, en Emily the Engineer heeft er 4 keer zoveel en haalt op Shorts toch 2 keer meer. Per volger gerekend gaf Shorts bij 7 van de 11 meer.
3. **Voor een account dat bij nul begint, is het eerlijkste voorbeeld mixtapeprints** (106 en 46 volgers): ongeveer gelijk, Shorts iets hoger (106 tegen 103 mediaan, 29 van 49 paren). Zo klein beginnen geeft op beide plekken ±100 views. Dat klopt met de vloer uit verhaal 10 en 11 (300 tot 900 Shorts, 150 tot 600 TikTok) en met Control Yourself (250 TikTok, 500 YouTube, EIGEN OPGAVE, verhaal 12).
4. **Een hit op de ene plek is vaak geen hit op de andere.** Bij 3dprintdood, marsgizmo en mixtapeprints hangt de rangorde van de views nauwelijks samen (Spearman 0,17, 0,16 en -0,07; GEZIEN). Bij Blender Secrets en kaivertigoh wel (0,65 en 0,88). In 69 paren haalde Shorts 10 keer meer dan TikTok, in 22 paren andersom. Twee plekken zijn dus twee loten: een filmpje dat op TikTok bij 200 blijft, kan op Shorts 20.000 halen.
5. **Volgorde:** de meeste plaatsen beide op dezelfde dag (267 van 317). Kwam YouTube een paar dagen later, dan haalde Shorts niet meer dan TikTok (mediaan 0,9 tegen 3,4 op dezelfde dag; maar 23 paren, dus zwak).

### Hoofdverhaal: mixtapeprints, een kleine printwinkel die drie keer per dag plaatste en vastliep
Een kleine winkel met geprinte cadeaus ("Custom 3D printed gifts, novelty decor, and personalized keepsakes", eigen kanaaltekst). 329 TikToks en een stuk of 145 Shorts, okt 2025 tot 6 aug 2026. GEZIEN.
1. **Jan tot mrt 2026: een paar filmpjes van 30 tot 40 seconden**, ±100 tot 340 views.
2. **Vanaf apr 2026: overstap naar clips van 5 seconden**, steeds hetzelfde sjabloon: een product draait rond, een zin met een grap ("This worried corn hides your secrets better than it hid in the field"). Van 4 per maand naar 78, 87 en 91 per maand: bijna 3 per dag, op TikTok en YouTube tegelijk.
3. **April en mei: mediaan ±300 views op TikTok** per clip, beste clips een naampuzzel (1.685) en een naambord met losse letters (1.089). Dat is de normale vloer, niet slechter.
4. **Juni en juli: daling naar 140 tot 180** terwijl het aantal gelijk bleef. Dezelfde producten kwamen steeds terug ("Cathedral glass, but make it spicy", een week later "Stained glass, but make it spicy").
5. **Week van 3 aug: 28 clips, mediaan 7,5 views op TikTok** (de clips staan er al 3 maanden, dus het ligt niet aan de leeftijd). Op Shorts in augustus mediaan 40, in juli nog 220. Na 6 augustus niets meer.
Wat het precies veroorzaakte, zegt de maker nergens. Mijn uitleg is een GOK: veel bijna gelijke clips van 5 seconden met herhaalde producten zien eruit als massawerk, en beide platforms tonen ze dan aan bijna niemand meer. Het patroon (eerst normaal, dan dalen bij gelijke hoeveelheid, dan instorten) is GEZIEN.

### Drie lessen
1. **Zet elk filmpje op beide plekken, op dezelfde dag, als schoon bestand.** Shorts gaf bij dezelfde clip mediaan 2,85 keer zoveel views en won bij 9 van 11 makers; TikTok won alleen waar het publiek daar al was. Omdat een hit zelden op beide plekken tegelijk valt, verdubbelt dubbel plaatsen je kansen, niet alleen je views. Upload het origineel, niet de TikTok-download met watermerk (Instagram drukt dat bewust weg; voor YouTube weet ik het niet, GOK dat het niet helpt).
2. **Beoordeel een vorm niet op één plek.** Bij drie makers hing de rangorde op TikTok en Shorts nauwelijks samen. Een kopvorm schrappen omdat hij op TikTok bij 150 bleef, kan een Shorts-hit kosten. Kijk na 48 uur naar de beste van de twee.
3. **Meer is niet beter als het hetzelfde wordt.** mixtapeprints ging van 1 naar 3 per dag met clips van 5 seconden uit één sjabloon en herhaalde producten; views gingen van ±300 naar 7,5 en de maker stopte. Eén per dag met elke dag een nieuwe tip of nieuwe handeling (Blender Secrets: duizenden tips, geen herhaling) is veiliger dan veel van hetzelfde.

### Eerlijk: wat deze meting niet zegt
- 11 makers, vooral printen; maar twee echte Blender-tipmakers met genoeg paren (Blender Secrets en SouthernShotty), en die hebben een groot YouTube-kanaal. Voor Blender is de voorsprong van Shorts dus deels het bestaande publiek.
- Views zijn geen mensen en geen kopers. YouTube telt herstarts mee; TikTok telt ook herhaald kijken (GOK hoe precies).
- Alleen paren die ik kon koppelen; filmpjes die maar op één plek staan, ontbreken. Makers plaatsen misschien vooral hun beste clips dubbel.
- De YouTube-cijfers zijn precies, de TikTok-cijfers afgerond (bijvoorbeeld 15.800).
- Het verloop bij mixtapeprints is één geval; de oorzaak is een GOK.

### Voorstel voor Dortus deze week
**Chris: vanaf di 17 nov elk filmpje op dezelfde dag op YouTube Shorts én TikTok (@dortusstudio), als het schone mp4-bestand uit de release, niet de TikTok-download.** Houd per filmpje beide cijfers na 48 uur bij in `commercie/filmpjes/` (datum, kop, lengte, views TikTok, views Shorts), en beslis over een kopvorm pas op het beste van de twee na ±10 filmpjes. Blijf op één per dag met steeds een nieuwe tip; geen tweede of derde clip per dag uit hetzelfde sjabloon, en hetzelfde filmpje niet opnieuw plaatsen tenzij hij duidelijk anders geknipt is (The Matriarch, verhaal 12). Verwacht in het begin ±100 tot 900 views per plek; dat is normaal. Waarom: dezelfde clip haalde op Shorts mediaan 2,85 keer zoveel, hits vallen per plek anders, en de enige kleine maker die het aantal opdreef met bijna gelijke clips zakte naar 7,5 views.

---

## 12. TikTok voor kleine spelmakers: Conradical Games (Desktop Defender, Desktop Detective, Screen Stocks) zette 203 TikToks naast zijn Steam-cijfers. Wat leverden views op, en wat niet?

Onderzocht 16 nov 2026, run 12. Waarom: Thijs zet @hatsofthefallen om naar een TikTok-account voor het spel (besluit 16 nov 09:40), 3 keer per week. Fenna beschreef Desktop Defender al vanuit Steam (`verhalen-spellen.md` verhaal 5), maar niet wat TikTok deed. Conradical Games maakt precies onze soort spel (bureaubladhoek, idle, $4,99) en plaatst zelf TikToks, met de naam van het spel in elke kop. Daardoor kun je views per spel naast reviews per week leggen. Ter vergelijking twee makers die hun TikTok-cijfers zelf beschrijven (The Matriarch, Duck Detective) en vijf andere spelaccounts.

### Bronnen
- TikTok via yt-dlp 2026.10.26, openbare profielen, niet ingelogd, GEZIEN 16 nov ±11:05 UTC: @conradicalgames (203 filmpjes, 5 feb 2021 tot 12 nov 2026), @thematriarchgame (78), @mochitoki (Loddlenaut, 74), @spiritcitylofi (75), @moonlightpeaks (186), @toukana_interactive (Dorfromantik, 224), @unpackinggame (113). Per filmpje datum, views, lengte en het spel uit de kop: `platformen/succes/data/tiktok-spelmakers-2026-11-16.csv`.
- Steam: `appdetails` en `appreviewhistogram/<appid>` (reviews per week of maand), GEZIEN 16 nov. Het totaal uit het histogram ligt vlak bij het getal van Fenna (Desktop Defender 1.830 tegen 1.788).
- Eigen verhalen van makers (EIGEN OPGAVE, niet na te rekenen): [The Matriarch op Game Developer](https://www.gamedeveloper.com/game-platforms/from-400-to-20-000-wishlists-with-1-video-how-tiktok-can-make-your-game-go-viral), [Duck Detective (All The Bees)](https://allthebees.bearblog.dev/we-got-over-60k-wishlists-in-6-months-this-is-how/), [Control Yourself (squigalug)](https://squigalug.itch.io/control-yourself/devlog/910174/youtube-vs-tiktok-raising-your-games-profile).
- Geprobeerd en niet leesbaar of te klein: @hatsofthefallen en @dortusstudio (geen openbare lijst), @deskrawl (4 filmpjes), @workfromdungeon (2), @ropukagame (7). Kleine bureaubladspellen zitten nauwelijks op TikTok met een eigen account.

### Conradical Games: TikTok-views per spel naast Steam
| Spel (kop "Game is called ...") | TikToks | Views samen | Beste filmpje | Reviews nu | Views per review | Label |
|---|---|---|---|---|---|---|
| Desktop Defender (nov 2025) | 11 | 725.000 | 409.000 (14 okt 2025, dag 2 van Next Fest) | 1.830 | ±400 | GEZIEN |
| Desktop Detective (aug 2026) | 24 | **2.555.000** | 1.500.000 (28 aug 2026, 9 dagen na de lancering) | **187** | ±13.700 | GEZIEN |
| Screen Stocks (okt 2026) | 24 | 479.000 | 210.900 (19 okt 2026) | 244 | ±2.000 | GEZIEN |
| Card Corner (mrt 2026) | 19 | 179.000 | 116.200 | 81 | ±2.200 | GEZIEN |
| Little Laps (aug 2025) | 10 | 22.000 | 6.400 | 14 | ±1.600 | GEZIEN |
| Wanted Shadows: Unchained (jun 2026) | 7 | 9.000 | 2.200 | 11 | ±850 | GEZIEN |

**Desktop Detective per week (reviews):** lanceerweek 19 aug: 69; week van 26 aug (met de TikToks van 866.000 en 1.500.000 views op 22 en 28 aug): **42**; daarna 21, 14, 6, 4 (GEZIEN, histogram). De twee grootste filmpjes die hij ooit maakte gaven geen zichtbare bult in de reviews. Kanttekening: views tellen op sinds het plaatsen, een deel kan later gekomen zijn; maar ook later is er geen bult.

### Wat hij in welke volgorde deed
1. **2021: devlog met gezicht en grappen** ("A day in the life of a game developer", "Balancing ain't always easy"). De eerste 30 filmpjes in 30 dagen, mediaan 2.492 views, één van 243.100 (nr. 7). Dat was TikTok in 2021: toen gaf het platform veel meer bereik aan nieuwe accounts (ook @mochitoki en @thematriarchgame begonnen toen met 20.000 tot 800.000 per filmpje). GEZIEN.
2. **2022 tot 2024: los en weinig**, filmpjes over zijn grote spel en Switch-uitgaven, 1.100 tot 15.000 views. GEZIEN.
3. **Vanaf jun 2025: één vaste vorm.** Elke kop is "Game is called "X", wishlist it on Steam now!", gameplay van 20 tot 50 seconden, in reeksen van 10 tot 24 filmpjes vlak voor en na een moment (Next Fest, lancering, demo). Hetzelfde account, dezelfde vorm, zeven spellen: de spellen in de bureaubladhoek (Desktop Defender, Desktop Detective, Screen Stocks) halen tonnen, de gewone spellen (Little Laps, Wanted Shadows, Synth Beasts) blijven op 800 tot 2.500 per filmpje. GEZIEN.
4. **Desktop Defender:** één TikTok in juli 2025 (1.879 views), daarna niets tot de eerste dag van Next Fest (13 okt). Toen 9 filmpjes in 7 dagen: 43.300, **409.000**, 146.400, 48.000 ... Dat valt samen met de demo, die 1.548 gelijktijdige spelers haalde (verhaal 5 van Fenna). Welk deel van de 50.000 verlanglijstjes van TikTok kwam, zegt hij nergens. GEZIEN voor de views, onbekend voor de verdeling.
5. **Desktop Detective:** 13 filmpjes tijdens Next Fest juni 2026 (411 tot 13.500 views), 4 vlak voor de lancering, en daarna de twee grootste filmpjes van het account. Het spel bleef op 187 reviews, met klachten dat het te veel op Desktop Defender lijkt en "far from an idler" is (Fenna). GEZIEN.

### Ter vergelijking
- **The Matriarch** (Chewa, solo, $4,99): na 3 maanden winkelpagina onder de 500 verlanglijstjes; dezelfde trailer, sneller geknipt, haalde op TikTok 1 miljoen views in een nacht en volgens de maker "+1500 in ONE day", daarna +3.500 en +2.500, samen met Next Fest 23.000 verlanglijstjes (EIGEN OPGAVE). In onze lijst: filmpje 6, 8,9 miljoen views (5 feb 2022, GEZIEN). Uitgebracht sep 2022: **792 reviews, 76%** (GEZIEN). Veel verlanglijstjes, matige uitkomst.
- **Duck Detective** (Happy Broccoli Games): "we've failed to have any traction on TikTok for years before this", tot één TikTok van 1 miljoen views met "close to 1000 wishlists a day for a few days"; gameplay met een grappig onderschrift, geen gezicht, geen stem (EIGEN OPGAVE). Nu 6.273 reviews, 94% (GEZIEN). De grootste stappen kwamen volgens hen van showcases en Next Fest.
- **Loddlenaut** (Moon Lagoon, twee makers): eerste TikTok "I'm making a cute video game with my boyfriend" 581.600 views (feb 2021), uitschieter 2,3 miljoen; laatste 30 filmpjes mediaan 1.769. Spel ($19,99, nov 2023): 4.057 reviews, 98% (GEZIEN).
- **Grote spellen met een klein TikTok-account:** Dorfromantik (28.516 reviews) haalt mediaan ±900 views per TikTok over 224 filmpjes; Spirit City: Lofi Sessions, een spel dat naast je werk draait (16.165 reviews), mediaan ±900 over 75 filmpjes (GEZIEN). Hun succes kwam niet van hun eigen TikTok.
- **Control Yourself** (squigalug, solo): Shorts en TikToks van dezelfde clips, "around 250 views on TikTok and 500 on YouTube", niets viraal (EIGEN OPGAVE). Dat is de vloer die we in verhaal 10 en 11 ook maten.

### Wat ik zag
1. **TikTok-views en kopers lopen los van elkaar.** Bij hetzelfde account en dezelfde vorm kostte een review ±400 views (Desktop Defender) tot ±13.700 (Desktop Detective). Het verschil zat in het spel en het moment, niet in het filmpje.
2. **Het onderwerp "spel dat in de hoek van je scherm leeft" werkt op TikTok.** Bij één maker met één vorm haalden alleen de bureaubladspellen 100.000+; zijn racer en schietspel bleven op ±1.000. Goed nieuws voor @hatsofthefallen: het idee zelf trekt kijkers.
3. **Een TikTok-hit na de lancering redde een zwak spel niet** (Desktop Detective: 2,5 miljoen views in de 10 dagen na de lancering, reviews daalden). Een hit vóór of tijdens een moment met een demo of verlanglijst-knop deed wel iets (The Matriarch, Duck Detective, Desktop Defender), maar steeds samen met Next Fest of een showcase.
4. **De vorm is simpel en zonder gezicht:** gameplay van 20 tot 50 seconden, de naam van het spel in de kop, een vraag of grap bovenin, en reeksen rond een moment in plaats van een gelijkmatige stroom. The Matriarch: dezelfde video sneller geknipt en opnieuw geplaatst ging van 10.000 naar 7 miljoen (EIGEN OPGAVE).
5. **2021 is geen meetlat.** Accounts die toen begonnen, kregen tienduizenden views per filmpje. Voor een nieuw account nu: 250 tot 1.000 (squigalug, verhaal 11, Conradicals gewone spellen).

### Drie lessen
1. **Meet TikTok in verlanglijstjes, niet in views.** Een miljoen views kan 1.500 verlanglijstjes geven (The Matriarch) of bijna niets (Desktop Detective). Zet bij elk filmpje de verlanglijstjes van die dag en de dag erna ernaast.
2. **Plaats in reeksen rond een moment met een knop.** Conradical plaatste 9 tot 24 filmpjes in de dagen rond Next Fest, een demo of de lancering, en bijna niets daartussen. Een hit zonder pagina, demo of fest om naartoe te gaan, verdampt.
3. **TikTok versterkt een goed spel, het maakt geen goed spel.** De hit met de meeste views hoorde bij het spel met de slechtste reviews. Het werk aan de diepte (Fenna: uur 10 beslist) blijft belangrijker dan het filmpje.

### Eerlijk: wat deze meting niet zegt
- Eén maker met zeven spellen, plus twee eigen verhalen. Conradical had uitgevers bij de bureaubladspellen; wat die zelf deden, weet ik niet.
- Ik zie geen verlanglijstjes, alleen reviews. Reviews volgen kopers ongeveer, maar niet per dag.
- Views tellen op sinds het plaatsen; welk deel in de eerste dagen kwam, weet ik niet.
- De kop "Game is called ..." heb ik met een patroon uitgelezen; filmpjes met een andere kop zijn niet aan een spel toegewezen.
- Het account had in 2025 al volgers uit 2021 (aantal onbekend). Een nieuw account haalt waarschijnlijk minder (GOK).

### Voorstel voor Dortus deze week
**Chris (met Olaf of Mila voor de clips): plan de TikToks van @hatsofthefallen in reeksen rond momenten, niet als gelijkmatige stroom.** Nu: 3 per week om het account op te warmen en de vorm te zoeken (de grap "He wears their hats." in de eerste seconde, gameplay 15 tot 40 s, naam van het spel in de kop, geen gezicht nodig). De echte reeks van ±10 filmpjes in 10 dagen pas als de Steam-pagina met verlanglijst-knop live is, en opnieuw rond het Desktop Companion Fest (14 tot 18 januari). Hou per filmpje bij: datum, views na 48 uur, en de verlanglijstjes van die dag en de dag erna (Steamworks, via de hoofdchat). Schiet er één uit, plaats hem nog eens sneller geknipt (The Matriarch). Waarom: bij Conradical kwamen de grote aantallen alleen in reeksen rond een moment, en alleen voor bureaubladspellen; een hit zonder knop om op te drukken leverde niets op.

---

## 11. De eerste 30 TikToks van 24 accounts over 3D-printen en Blender, nu mét datums: wat haalt een begin, wie brak door, en wat deden zij anders?

Onderzocht 16 nov 2026, run 11. Waarom: Thijs zet twee TikTok-accounts om (@dortusstudio voor Blender en 3D-print-tips, @hatsofthefallen voor het spel, besluit 16 nov 09:40). Verhaal 10 ging alleen over YouTube Shorts en had geen datums. Nieuw feit deze run: yt-dlp leest in de cloud de volledige openbare filmpjeslijst van een TikTok-account, met datum, lengte en views per filmpje (GEZIEN; in run 1 lukte dat nog niet).

### Bronnen
- TikTok via yt-dlp 2026.10.26 (alleen openbare profielen lezen, niet ingelogd, GEZIEN 16 nov ±10:30 UTC). De lijst is volledig: het aantal filmpjes van yt-dlp is gelijk aan of vlak bij het `videoCount` op het profiel (bijvoorbeeld 299 tegen 301 bij VAW.BE, 187 tegen 187 bij McGybeer).
- Welke accounts: TikTok-zoeken en hashtagpagina's zijn vanuit de cloud niet te lezen (yt-dlp meldt "broken"). Daarom 81 namen geprobeerd: de handles van YouTube-kanalen uit 8 zoekopdrachten naar Shorts over Blender en 3D-printen, de kanalen uit verhaal 10, en makers uit een lijst van E3D. 24 accounts bestaan op TikTok onder die naam, hebben 30+ filmpjes en gaan echt over 3D-printen, Blender of (als ijkpunt) Garmin.
- Tabel per account: `platformen/succes/data/tiktok-eerste30-2026-11-16.csv` (openbare accountnamen, geen persoonsgegevens).

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Dagen tussen filmpje 1 en 30, mediaan | 100 dagen (van 6 tot 1.727) | GEZIEN |
| Accounts die klein begonnen (mediaan eerste 10 onder 1.000, n=9): mediaan van de eerste 30 | **325 views** (164 tot 569) | GEZIEN |
| Uitschieter (10 keer de eigen mediaan) binnen de eerste 30, alle 24 | 15 van 24, mediaan bij filmpje 11 | GEZIEN |
| Idem, bij de 9 die klein begonnen | **2 van 9** | GEZIEN |
| Laatste 30 beter dan de eerste 30 | 11 van 24; bij de kleine 5 van 9 | GEZIEN |
| Accounts waar de laatste 30 minder dan de helft van de eerste 30 halen | o.a. McGybeer (4.968 naar 1.100), Slant3D, E3D, SouthernShotty, Mars Gizmo | GEZIEN |
| Dezelfde maker op twee platformen, volgers | Blender Secrets YouTube 292.000, TikTok 11.800; SouthernShotty 321.000 en 4.700; Brock Creative 15.900 en 141.300; Blender Tips 99.400 en 129.900 (met 28 TikToks, zelfde maker niet zeker) | GEZIEN |

### Vier accounts die het verschil laten zien
1. **ali3design** (@ali3dprint, verkoopt STL-bestanden op Cults3D, 1.530 volgers): filmpje 1 tot 3 waren een Minecraft-sleutelhouder en een boekenlegger, 300 tot 570 views. Filmpje 4 (dag 3): een motorhelm als sleutelhouder waarvan het vizier vanzelf opengaat, **44.200 views**. Na een pauze van vier maanden kwamen drie varianten van hetzelfde mechaniek op 10.600 tot 11.400; filmpjes zonder bewegend onderdeel bleven op 280 tot 780. Zijn beste filmpje ooit (nr. 49, 99.800) is weer een mechaniek: een autolift op schaal. GEZIEN.
2. **3D Print Dood** (15.000 volgers): na één los filmpje plaatste hij vanaf 31 okt 2024 twee tot vijf filmpjes per dag, 29 in 10 dagen, elk met een koopvraag als kop: "Best Filament for Bambu Lab A1 Mini" (190.100), "3D Printing for Beginners" (81.300), "Don't Buy the Bambu Lab A1 Mini" (11.500). Zijn beste ooit: "Best 3D Print Modeling Software for Beginners" (949.400). Na een jaar zakte hij naar ±3.000 per filmpje. GEZIEN.
3. **Artinvader_** (Blender-tutorials uit Berlijn, 7.600 volgers): begon met "Hey ich bin Artinvader", Patreon en "STOP CLIMATE CHANGE": 150 tot 650 views. Groeide stap voor stap in 3,5 jaar en 300 filmpjes (blokken van 30: 325, 665, 3.389 ... 5.097, 5.511). De grote stap kwam in 2025 met een vaste reeks **"FREE Blender Addon – <wat het doet> with <naam>"**, waarin hij gratis add-ons van ánderen laat zien: 2.100 tot 30.200 views, zijn drie beste filmpjes ooit zijn alle drie zo'n add-on. GEZIEN.
4. **ArwenPrints** (verkoopt muziekprints, 845 filmpjes): drie memes braken door (66.600, 70.300 en 1,2 miljoen), maar de mediaan per blok van 30 zakte daarna tot 11 en zit nu op 118 tot 330. Een uitschieter die niets met het product te maken heeft, bouwt niets op. GEZIEN.
Ter vergelijking: **McGybeer** had zijn uitschieter bij filmpje 2 (de ratelslang, 7 miljoen) en daalt sindsdien per blok van 30; **Cinderwing3D** (dragons op Cults3D) zat 23 filmpjes op 2.000 tot 9.600 en brak door met een nieuw beweegbaar ontwerp (318.200, nr. 24); ook daarna geen blijvende stijging.

### Wat ik zag
1. **Een nieuw klein account op TikTok begint bij ±150 tot 600 views, iets lager dan op YouTube** (verhaal 10: 300 tot 900). Dat is de vloer die TikTok elk filmpje geeft; de eerste 30 zeggen weinig.
2. **Een uitschieter in de eerste 30 is op TikTok voor een klein account zeldzaam** (2 van 9), anders dan op YouTube (27 van 34, maar dat waren vooral kanalen die al publiek hadden). Reken er voor @dortusstudio niet op binnen 30 filmpjes.
3. **Wat doorbrak bij makers van spullen: iets wat beweegt dat je niet verwacht** (vizier dat opengaat, slang die kronkelt, draak die buigt). Bij uitleg-accounts: een koopvraag of beginnersvraag als kop. Memes en "ik ben ..." deden niets blijvends.
4. **TikTok-uitschieters houden geen stand.** Bij de helft daalt het account daarna (McGybeer, Slant3D, E3D, 3D Print Dood na zijn piek). Wie bleef groeien (Artinvader_, KeycraftedStudio, Fat13Creations) deed dat langzaam, met een vaste reeks over 100+ filmpjes.
5. **Hetzelfde filmpje werkt niet even goed op elk platform.** Blender Secrets en SouthernShotty zijn groot op YouTube en klein op TikTok; Brock Creative andersom. Eén filmpje op drie plekken plaatsen kost weinig, dus meet per platform en schuif de moeite naar waar het werkt.
6. **Er bestaan TikTok-accounts die gratis Blender-add-ons van anderen laten zien, en dat doet het daar goed.** Voor Click Joints (gratis op extensions.blender.org) is zo'n account een gratis ingang naar Blender-gebruikers, net als bij McGybeer de filmpjes van anderen het groeimoment waren (verhaal 1).

### Drie lessen
1. **Op TikTok is 150 tot 600 views per filmpje in het begin normaal, en een doorbraak binnen 30 filmpjes uitzondering.** Beslis bij filmpje 30 op downloads en de trend, niet op of er al een hit was.
2. **Laat in de eerste seconde iets bewegen wat de kijker niet verwacht**, en maak bij een uitschieter meteen varianten van precies dat mechaniek (ali3design).
3. **Laat anderen je gratis gereedschap laten zien.** Er zijn accounts met een vaste reeks over gratis add-ons; dat is voor een kleine maker meer bereik dan het eigen kanaal in de eerste maanden.

### Eerlijk: wat deze meting niet zegt
- De accounts komen via YouTube-zoekresultaten en een lijst van een printermerk. Gestopte accounts met 5 filmpjes zitten er niet in; het echte begin is waarschijnlijk lager (GOK).
- Views zijn opgeteld sinds het plaatsen en afgerond door TikTok. Oude filmpjes konden langer groeien.
- Volgers bij de start weet ik niet; "klein begonnen" is afgeleid uit de eerste 10 filmpjes.
- 24 accounts is weinig, 9 kleine nog minder. Of een handle op TikTok dezelfde maker is als op YouTube heb ik gecontroleerd aan naam en onderwerp; vier namen die iemand anders bleken (`osasart`, `piercing`, `stache_obj`, `blenderhub`) heb ik weggelaten. Bij Blender Tips is het niet zeker dat het TikTok-account dezelfde maker is (bio "Blender Expert", 28 filmpjes in 2024).
- Ik meet views, geen verkoop of downloads.

### Voorstel voor Dortus deze week
**Chris: zet Artinvader_ (tiktok.com/@artinvader_) op `commercie/blender-click-joints/makers.md`**, met als reden zijn reeks "FREE Blender Addon – ..." (2.100 tot 30.200 views per add-on, GEZIEN). Click Joints is gratis en gekeurd op extensions.blender.org en past dus precies in zijn reeks; een gratis Pro erbij valt onder het ja van Thijs van 16 nov 09:51. Zoek zijn openbare contactadres zoals hij het zelf noemt (zijn TikTok-bio verwijst naar zijn tutorials; geen privégegevens zoeken); de hoofdchat verstuurt, zoals afgesproken. **Daarnaast voor @dortusstudio op TikTok:** in de eerste seconde het gewricht dat buigt, en meet TikTok apart van YouTube in de regel per filmpje, zodat we na 30 filmpjes zien welk platform het werk waard is. Waarom: bij kleine accounts kwam de eerste 30 filmpjes zelden een doorbraak (2 van 9), en wie doorbrak deed dat met iets wat bewoog of via een groter account.

---

## 10. De eerste 30 Shorts van 34 Blender-kanalen gemeten: wat haalt een begin, wanneer komt de eerste uitschieter, en welk soort filmpje werkt?

Onderzocht 16 nov 2026, run 10. Waarom: dit was de eerste vraag aan mij ("wat deden ze in de eerste 30 filmpjes?") en die stond nog open. Chris begint morgen, di 17 nov, met dagelijkse filmpjes op @dortusstudio. Na 20 tot 30 filmpjes wordt beslist of het werkt (besluit 15 nov 22:53). Dan moet vooraf bekend zijn wat normaal is.

### Bronnen
- YouTube, via yt-dlp in de cloud (alleen openbare lijsten lezen, GEZIEN): 5 zoekopdrachten van 60 treffers ("blender addon shorts", "blender add-on #shorts", "blender tip #shorts", "free blender addon #shorts", "blender extension shorts") gaven 99 kanalen. Van elk kanaal de Shorts-lijst met views per filmpje, en de eerste pagina van de gewone video's (hooguit 60) om te zien of het kanaal al lange video's had.
- Bruikbaar: **34 kanalen** met 30+ Shorts en een volledige lijst. Een lijst is volledig als het aantal geen veelvoud van 48 is: YouTube geeft per keer 48 Shorts en weigerde de cloud vaak de volgende pagina (HTTP 403), dan stopt de lijst precies op 48, 96 of 144. Die kanalen (onder meer Blender Secrets, BlenderVitals, CGDive) heb ik weggelaten.
- Tabel per kanaal: `platformen/succes/data/blender-shorts-eerste30-2026-11-16.csv` (openbare kanaalnamen, geen persoonsgegevens).
- Niet gelukt: de datum per filmpje (YouTube vraagt de cloud om in te loggen, niet omzeild). Ik weet dus de volgorde, niet wanneer.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Views van de eerste 10 Shorts, mediaan per kanaal, mediaan over 34 kanalen | 3.900 (maar sterk afhankelijk van de abonnees die het kanaal al had) | GEZIEN |
| Kleine kanalen (onder 20.000 abonnees, n=10): mediaan van de eerste 10 Shorts | 161 tot 2.250, meestal **300 tot 900** | GEZIEN |
| Kanalen met een uitschieter (10 keer hun eigen mediaan) binnen de eerste 30 | **27 van 34**; die uitschieter kwam mediaan bij filmpje **10** | GEZIEN |
| Kanalen waar de laatste 30 Shorts beter doen dan de eerste 30 | **17 van 34** (de helft) | GEZIEN |
| Samenhang mediaan eerste 30 en mediaan laatste 30 (Spearman) | 0,80: het begin voorspelt het vervolg sterk | GEZIEN |
| Aandeel van de 3 beste Shorts in alle Shorts-views van een kanaal, mediaan | 33% (Wimpythekat 90%: één filmpje met 10 miljoen) | GEZIEN |
| Alle 1.020 eerste Shorts, views gedeeld door de mediaan van het eigen kanaal: kop met uitleg of tip ("how to", "tip", "fix", "free", "fast") | n=245, mediaan 1,09; 24% haalt 3 keer de mediaan | GEZIEN, ruwe indeling met een woordenlijst |
| Idem, kop met iets laten zien (render, animatie, film) | n=711, mediaan 0,98; 17% haalt 3 keer | GEZIEN |
| Idem, eigen reclame, dagboek of oproep ("Day #", Discord, live, trailer, "I'm a 3D artist") | n=64, mediaan 0,82; 17% haalt 3 keer | GEZIEN |

### Vijf kanalen die het verschil laten zien (eerste 30 Shorts)
1. **Blender Tips** (99.400 abonnees, maar 34 Shorts, weinig lange video's): na twee andere filmpjes vanaf nummer 3 steeds dezelfde vorm, "Blender Tip: <één handeling>" ("Fast Stairs", "Connect Faces", "Fix Bevel"). Geen enkele van de 27 tips onder 16.000 views; nummer 14 haalde 1,3 miljoen en nummer 26 5,6 miljoen. GEZIEN.
2. **Simon Zhang** (50.400): filmpje 1 tot 9 lieten mooie renders zien ("Stage of History, made in Blender"): 1.700 tot 5.300 views. Vanaf 10 en 11 wisselde hij naar "How I made this ... in Blender" en "The new Scatter Modifier in Blender 5.0 is amazing!": daarna vooral 30.000 tot 131.000. De renders die hij tussendoor bleef plaatsen bleven op 4.000 tot 10.000. GEZIEN.
3. **Wimpythekat** (32.400): losse tips 700 tot 9.400; vanaf 16 een vaste reeks "How a Pro vs a Beginner 3D Artist ..." met 29.000 tot 59.000; nummer 22 "Satisfying Soft Body Simulation" haalde 10 miljoen. GEZIEN.
4. **Daily-3D** (1.890, 202 Shorts): koppen als "Day #9 - Squid Game Wallpaper": meestal 50 tot 900 views. Het beste van de eerste 30 was een reeks schaakstukken "idea from Polyfjord" (tot 4.300). De laatste 30 Shorts zitten op mediaan 1.750, dus na 200 filmpjes wel iets gegroeid. GEZIEN.
5. **MEDICCI** (4.220, 200 Shorts, maakt ook een add-on): veel oproepen ("Envianos tu modelo 3D y lo vemos en VIVO", Discord) en filmpjes over de eigen retopo-add-on: 50 tot 700 views. Eén gewone vraag, "How to fix normals in Blender", haalde 30.000. Na 200 Shorts is de mediaan van de laatste 30 nog 285. GEZIEN.

### Wat ik zag
1. **Een nieuw klein kanaal begint bij honderden views per Short, niet bij duizenden.** De grote getallen in de tabel komen van kanalen die al abonnees hadden van lange video's (Grant Abbitt, CG Boost, Blender Studio). @dortusstudio begint bij 0 abonnees, dus de rij van de kleine kanalen is onze meetlat: 300 tot 900 views per filmpje is normaal in het begin.
2. **De eerste uitschieter komt meestal in de eerste 30, rond filmpje 10.** Bij 27 van 34 kanalen zat er een filmpje tussen met 10 keer de eigen mediaan. Vaak was dat het moment dat de maker een vorm vond en die bleef herhalen (Simon Zhang, Wimpythekat, Blender Tips).
3. **Meer van hetzelfde maakt een kanaal niet vanzelf groter.** Bij de helft doen de laatste 30 Shorts het niet beter dan de eerste 30, en het begin voorspelt het vervolg sterk (0,80). MEDICCI en Daily-3D plaatsten 200 filmpjes en bleven klein. Groeien kwam bij wie van vorm wisselde naar wat werkte, niet bij wie gewoon doorging.
4. **Per filmpje is het verschil tussen een uitleg-kop en een show-kop kleiner dan de verhalen doen denken** (mediaan 1,09 tegen 0,98 binnen hetzelfde kanaal). Het grote verschil zit tussen kanalen: wie ALLES in één duidelijke vorm doet (Blender Tips) staat ver boven wie afwisselt. Eigen reclame, oproepen en "dag 12"-dagboeken doen het slechtst.
5. **Een add-on-maker die zijn add-on aanprijst, haalt weinig; dezelfde maker met een gewone vraag haalt veel.** MEDICCI: filmpjes over de eigen add-on 141 tot 2.500, "How to fix normals" 30.000. Dit past bij Blender Secrets (verhaal 4) en VibeDesk (verhaal 2).

### Drie lessen
1. **Verwacht 300 tot 900 views per filmpje in het begin en beslis niet op één filmpje.** De drie beste filmpjes leveren een derde van alle views.
2. **Kies binnen 10 tot 15 filmpjes één vaste vorm en herhaal die.** De kanalen die groeiden hadden een vaste kop ("Blender Tip: ...", "How I made ...", "Pro vs Beginner ...") en hielden het daarbij zodra er één uitschoot.
3. **Het product hoort in beeld, niet in de kop.** De kop is een handeling of probleem dat de kijker zelf heeft; de add-on is het gereedschap dat je ziet werken.

### Eerlijk: wat deze meting niet zegt
- Views zijn van vandaag, opgeteld sinds het plaatsen. Oude filmpjes hebben langer kunnen groeien; zonder datums kan ik dat niet rechtzetten.
- De kanalen komen uit YouTube-zoekresultaten: dat zijn kanalen die YouTube nu laat zien, dus gestopte kanalen met 5 filmpjes zitten er nauwelijks in. Het echte begin van een gemiddeld nieuw kanaal is waarschijnlijk lager dan wat hier staat (GOK).
- Views zijn afgerond door YouTube (11.000). De indeling van de koppen is met een woordenlijst gedaan en dus ruw.
- Of een kanaal "al abonnees had" heb ik afgeleid uit het aantal lange video's (eerste pagina, hooguit 60), niet uit datums.
- Over TikTok zegt dit niets; alleen YouTube Shorts.

### Voorstel voor Dortus deze week
**Chris: gebruik voor de eerste 15 filmpjes op @dortusstudio één vaste kopvorm voor een probleem van de kijker, bijvoorbeeld "Blender 3D print tip: <handeling>" ("make a joint that moves after printing", "fix a part that fuses to the base"), met Click Joints alleen in beeld als het gereedschap. Geen filmpjes "wie zijn wij", geen "dag 3", geen "nu op Superhive" in de eerste 15.** Houd na elk filmpje in `commercie/filmpjes/` één regel bij: nummer, kop, views na 48 uur. Meetlat: 300 tot 900 views na een paar dagen is normaal. Haalt één filmpje 3 keer de mediaan van de rest, maak dan de volgende 5 in precies die vorm. Pas bij filmpje 30 beslissen (zoals het besluit van 15 nov al zegt), en alleen als er geen enkel filmpje boven 3 keer de mediaan kwam, van vorm wisselen. Waarom: bij 27 van 34 kanalen kwam de eerste uitschieter in de eerste 30, en groei kwam van wie daarna een vorm herhaalde.

---

## 9. r/blender: 208 berichten over add-ons (aug, sep en nov 2026) naast de winkels gemeten. Wat levert een Reddit-post op, en wat geeft extensions.blender.org zonder post?

Onderzocht 16 nov 2026, run 9. Waarom: het lanceerplan van Click Joints (`commercie/blender-click-joints/lancering.md`) zet r/blender als eerste Reddit-bericht, met in de tabel "geen eigen meting voor add-on-berichten (GOK)". Dit verhaal vult dat gat. Ook een vergelijking: Click Joints haalde 154 downloads in 8 dagen zonder enig bericht.

### Bronnen
- Berichten: Arctic Shift (`https://arctic-shift.photon-reddit.com/api/posts/search`, subreddit blender, "addon" in de kop), augustus, september en 1 tot 16 november 2026: 208 berichten met upvotes, reacties, flair en tekst (GEZIEN). Oktober en juni/juli gaf het archief deze run niet (time-outs, "slow down"). Tabel zonder gebruikersnamen: `platformen/succes/data/rblender-addon-berichten-2026-11-16.csv`.
- Reacties van de maker onder de 14 best scorende berichten: Arctic Shift `comments/search` (GEZIEN), om te zien waar de link naartoe gaat.
- Draad "My addon post keeps getting removed. What am I missing?" (r/blender, okt 2026, id 1x7mc42) met 18 reacties (GEZIEN, Arctic Shift).
- extensions.blender.org: lijst via `https://extensions.blender.org/api/v1/extensions/` (1.654 extensies, 1.357 add-ons), daarna per add-on de pagina met "Published" en "Downloads" (curl, 954 van de 1.357 pagina's gelezen voor de tijd op was; GEZIEN).
- Superhive: productpagina Motion Painter (curl, GEZIEN). GitHub-zoekfunctie voor Spider Walker (GEZIEN).
- Niet gelukt: de regels van r/blender zelf (reddit.com geeft de cloud een blokpagina, niet omzeild); PullPush weigert agents (niet omzeild).

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Upvotes per add-on-bericht, mediaan | **1** (75% heeft 3 of minder, 90% heeft 16 of minder, hoogste 2.233) | GEZIEN |
| Berichten met flair "Paid Product/Service Promotion" | 85, mediaan 1, 9 met 20+ | GEZIEN |
| Berichten met flair "Free Tools & Assets" | 34, mediaan 1,5, 5 met 20+ | GEZIEN |
| Berichten met een video (v.redd.it of YouTube) | 99, mediaan 2, **15 met 20+** | GEZIEN |
| Berichten zonder video (plaatje, tekst, link) | 109, mediaan 1, **3 met 20+** | GEZIEN |
| Berichten met een link naar extensions.blender.org in kop, link of tekst | **0 van 208** | GEZIEN |
| Waar de makers van de 14 best scorende berichten naar linken (in hun eigen reactie of tekst) | Gumroad, Superhive, itch.io, GitHub, Discord; nergens extensions.blender.org | GEZIEN |
| Nieuwe add-ons op extensions.blender.org, gepubliceerd 1 okt tot 8 nov (n=100 in mijn steekproef) | downloads nu: p25 199, **mediaan 370**, p75 608, p90 1.742; mediaan **13 per dag** | GEZIEN |
| Hetzelfde, gepubliceerd aug en sep (n=51) | mediaan 1.205, p90 4.690; ook ±13 per dag | GEZIEN |
| Click Joints, 8 nov tot 16 nov, zonder bericht | 154 downloads, ±19 per dag; 36% van de nieuwe add-ons van okt doet per dag meer | GEZIEN |
| Motion Painter ($30, Superhive): drie berichten op r/blender (240, 161 en 70 upvotes, aug tot nov) | "Sales 50+" na ±3 maanden | GEZIEN |
| Spider Walker (gratis, GitHub): één bericht, 417 upvotes, 19 aug | 66 sterren op GitHub (repo aangemaakt de dag ervoor) | GEZIEN |

### Wat ik zag, in volgorde
1. **Ook op r/blender verdwijnt het gewone add-on-bericht.** Mediaan 1 upvote, net als bij Garmin (verhaal 7). Gratis of betaald maakt voor de mediaan weinig uit.
2. **Bewegend beeld is de grootste factor die ik kon meten.** Van de berichten met een video haalde 15% 20+ upvotes, van de rest 3%. Alle tien best scorende berichten waren video's van het gereedschap aan het werk (een schets die een pose wordt, een spin die loopt, beweging tekenen in de 3D-weergave), met een kop als "I made a Blender addon that turns any rough sketch into a 3D pose" of "Free addon for procedural spider walk": wat het doet, in gewone woorden.
3. **De moderatoren en het publiek zijn wantrouwig tegenover snel gemaakte add-ons.** In de draad over verwijderde berichten krijgt de reactie met de meeste stemmen (31): "There's just a flood of simple vibe coded addons and people are getting tired of it." Een andere (3): "A lot of people are weary of ai built stuff because it's often a flash in the pan thing, gets launched enthusiastically but not maintained." Een derde (7) raadt aan juist via extensions.blender.org te gaan, "so people know its been approved and reviewed". De maker zelf had volgens eigen zeggen bijna 10.000 views en 100+ upvotes vóór zijn bericht werd verwijderd (DERDEN, één stem). Een vierde noemt de vuistregel van Reddit dat hooguit ±10% van wat je plaatst eigen werk mag zijn (DERDEN, niet nagekeken in de regels van Reddit).
4. **Wat een goed bericht oplevert is klein in kopers.** Motion Painter kreeg drie keer aandacht (samen 471 upvotes) en staat na ±3 maanden op 50+ verkopen voor $30, en daar zitten ook andere kanalen in. Spider Walker, gratis en het vierde bericht van de drie maanden, kreeg 66 sterren. Hoeveel downloads daar achter zitten kon ik niet zien.
5. **extensions.blender.org zelf geeft een vaste stroom, zonder bericht.** Een nieuwe add-on krijgt daar mediaan ±13 downloads per dag, ook na twee maanden nog. Click Joints doet met ±19 per dag al meer dan de mediaan, zonder één bericht. Gratis op die winkel is dus al een kanaal; Reddit komt daar bovenop, niet in de plaats van.

### Drie lessen
1. **Een bericht op r/blender is alleen de moeite met een video van het gereedschap aan het werk.** Zonder video haalde 3% de 20 upvotes; met video 15%. De kop zegt in gewone woorden wat je ziet gebeuren.
2. **"Snel met AI gemaakt" is op r/blender nu een rode vlag.** Wie een add-on plaatst moet laten zien dat het blijft: een openbare repo, een plek voor fouten, een versiegeschiedenis, en de keuring van extensions.blender.org. Dit sluit aan op de klacht op r/Garmin (verhaal 7): makers die niet terugpraten.
3. **De winkel geeft meer dan de post.** Net als bij Garmin (verhaal 7 en 8) komt het meeste bereik uit de winkel zelf. Een goed bericht is een extra duw van tientallen tot honderden mensen, geen lancering.

### Eerlijk: wat deze meting niet zegt
- Upvotes zijn van het moment van archiveren; latere stemmen en verwijderde berichten kunnen ontbreken. Verwijderde berichten zie ik niet als verwijderd.
- Alleen berichten met "addon" in de kop (niet "add-on" of "extension"), en oktober ontbreekt. 208 berichten is genoeg voor de mediaan, niet voor kleine verschillen.
- Geen enkel bericht linkte naar extensions.blender.org, dus ik kon een post niet naast de downloads van een gratis add-on op die winkel leggen. Waarom niet weet ik niet (GOK: makers met een gratis add-on op die winkel plaatsen weinig, of de link staat in een reactie die het archief mist).
- De downloadcijfers van extensions.blender.org tellen ook updates mee (GOK, de site zegt het niet); 954 van 1.357 pagina's gelezen, de steekproef volgt de volgorde van de lijst.
- De regels van r/blender zelf heb ik niet kunnen lezen.

### Voorstel voor Dortus deze week
**Chris: maak van het r/blender-bericht voor Click Joints (B16/B30 in `lancering.md`) een videobericht van 10 tot 20 seconden waarin een gewricht wordt gemaakt en buigt (filmpje 1, 2 of 7 uit de reeks, staand of liggend), met flair "Free Tools & Assets", een kop die zegt wat je ziet ("I made a free Blender add-on that cuts a printable ball joint into any limb" of iets dergelijks), en in de eerste regel van de tekst drie bewijzen dat het blijft: gekeurd op extensions.blender.org, open broncode op GitHub, en de lijst met fouten die al zijn opgelost (versie 0.1.1 van vandaag).** Geen woord over Pro in dat bericht. Thijs plaatst en antwoordt op de dag zelf. Waarom: video's haalden hier vijf keer zo vaak 20+ upvotes, en het grootste risico op r/blender is nu het stempel "vibe coded" en verwijdering. Meten: Bram zet in `downloads.csv` de teller de dag ervoor en 1, 3 en 7 dagen erna; zonder bericht doet Click Joints ±19 per dag, dus pas boven ±40 per dag in de week erna zeg ik dat het bericht iets gaf (GOK als grens).

---

## 8. Garmin-apps (geen wijzerplaten): betaald via Garmin, gratis met proef buiten Garmin, of gratis? 6.627 apps, widgets en datavelden gemeten, plus 116 berichten "[New App]"

Onderzocht 16 nov 2026, run 8. Open vraag uit run 7: een Garmin-app die met een proefversie groeide. Daarbij een correctie op mijn eigen voorstel van run 7.

### Eerst de correctie op run 7
In run 7 noemde ik Ahead ("gratis te installeren met 7 dagen proef, daarna $3,99") als voorbeeld en stelde ik voor dat Gijs voor Ebb een proefmodus aanzet. Dat kan niet zoals ik het schreef. In de winkel-API staat Ahead als gratis app (geen prijs, `hasTrialMode: false`) met een eigen PayPal-betaallink in het veld `hardwareProductUrl` (GEZIEN 16 nov). De proef en de ontgrendeling lopen dus buiten Garmin om. Garmin Pay, het systeem van Ebb, kent geen proeftijd, alleen 48 uur geld terug (forum Garmin, al vastgelegd door Gijs in `platformen/garmin/concurrenten-2026-11-13.md`; nu opnieuw gelezen, de draad staat nog op "Not Answered"). Een proef via een eigen betaalsysteem breekt de belofte van Ebb "no unlock code". Het voorstel van run 7 vervalt dus in die vorm; zie het nieuwe voorstel onderaan.

### Bronnen
- Winkel: de lijst `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps?startPageIndex=<n>&pageSize=30&sortType=mostRecent&appType=<watch-app|widget|datafield>`, met curl doorgelopen tot het einde (16 nov). 4.195 apps, 645 widgets en 1.787 datavelden, samen 6.627 (GEZIEN). Per app: prijs, downloadklasse, reviews, eerste goedkeuring, beschrijving, en de vlag `paymentModel`.
- Wat `paymentModel` betekent heb ik afgeleid, niet in een handleiding gelezen: 0 = gewoon, 1 = "heeft iets buiten de winkel nodig". Van de 322 gratis apps met vlag 1 noemen er 284 een proef, code, licentie, abonnement of account (GEZIEN). Betaald via Garmin Pay herken ik aan een prijs.
- Indeling (eigen regels op de beschrijving, kan bij enkele fout zijn, GOK): A betaald via Garmin Pay; B gratis in de winkel met proef of betaalmuur buiten Garmin (woorden als trial, unlock code, KiezelPay, licentie, of een PayPal- of Gumroad-link); X gratis maar account of apparaat nodig; E gratis.
- Tabel: `platformen/succes/data/garmin-apps-betaalmodel-2026-11-16.csv` (zonder mailadressen en beschrijvingen).
- Reddit: archief Arctic Shift, r/Garmin, alle berichten per dag van 1 jul tot 4 aug en van 1 sep tot 28 sep 2026 (de rest liep vast op de snelheid van het archief), daaruit 116 berichten met "[New App]" of "[New Data Field]" (GEZIEN).
- Forum Garmin, met curl: "I Monetized My Ski App, Here's What Happened" (Charlie, ±feb 2026, https://forums.garmin.com/developer/connect-iq/f/showcase/430838/i-monetized-my-ski-app-here-s-what-happened) en "Connect IQ Monetization System vs own payment system" (±dec 2025, https://forums.garmin.com/developer/connect-iq/f/discussion/426202/connect-iq-monetization-system-vs-own-payment-system---increase-in-sales).

### Cijfers: hoe ver komen nieuwe apps (eerste goedkeuring jan tot jul 2026, dus 3,5 tot 10 maanden oud)
| Soort en model | Aantal | 100+ downloads | 1000+ | Mediaan reviews |
|---|---|---|---|---|
| App, betaald via Garmin Pay | 160 | 46% | 11% | 3 |
| App, gratis met proef of betaalmuur buiten Garmin | 80 | 80% | 24% | 3 |
| App, gratis | 520 | 76% | 24% | 3 |
| Dataveld, betaald | 36 | 28% | 3% | 1 |
| Dataveld, gratis met proef buiten Garmin | 32 | 62% | 31% | 2 |
| Widget, betaald | 29 | 72% | 10% | 10 |
Alles GEZIEN, eigen telling uit de API. Downloadklassen: "100" betekent 100 tot 999.

Andere metingen:
| Wat | Cijfer | Label |
|---|---|---|
| Betaalde app naast een gratis broertje met dezelfde naam (Lite, Free, Demo), 74 paren | betaalde versie mediaan 0,1 keer de downloadklasse van de gratis versie | GEZIEN |
| Nieuwe apps, widgets en datavelden met eerste goedkeuring 1 tot 16 nov 2026 | 951, waarvan 208 betaald | GEZIEN |
| Aandeel betaald onder de nieuwe, per maand jan tot nov 2026 | steeds 12 tot 22% | GEZIEN |
| Berichten "[New App]" op r/Garmin, upvotes mediaan | 1 | GEZIEN |
| Ski Pin (dataveld, $4, later $4,99): verkopen eerste maand | 68 | DERDEN, de maker op het forum |
| Ski Pin nu in de winkel | klasse 100, 5 reviews | GEZIEN |
| Ebb op 16 nov ±07:10 UTC | 0 downloads, 0 reviews | GEZIEN |

### Wat ik zag, in volgorde
1. **Betaald via Garmin is een hogere drempel, maar geen muur.** Iets minder dan de helft van de betaalde apps haalt binnen een paar maanden de klasse 100, tegen driekwart van de gratis apps. Bij een betaalde app is een download een verkoop: Ski Pin verkocht in januari 68 keer en staat nu in klasse 100 met 5 reviews. Een betaalde app in klasse 100 heeft dus minstens 100 kopers. Bij $4,99 is dat na 15% voor Garmin ±$424 (GOK: aanname 100 kopers, vóór btw en de jaarlijkse $100).
2. **Gratis met proef buiten Garmin haalt evenveel downloads als gratis, maar hoeveel er betalen is onbekend.** Geen enkele maker in de forumdraden noemt een omrekening van proef naar betaald voor Garmin. Wat er wel staat: een Nederlandse maker (beva) schrijft dat veel Nederlanders met een Garmin hun bankpas niet kunnen toevoegen voor aankopen in de winkel, omdat Garmin een creditcard vraagt (DERDEN, één stem, niet nagekeken). Dat pleit voor een eigen betaalweg, maar alleen voor die groep.
3. **Een gratis broertje haalt ongeveer tien keer zoveel downloads als de betaalde versie.** Mediaan 0,1 bij 74 paren. Voorbeelden: Reminders Lite 1000+ en Reminders Pro ($4,99) 100+ met 31 reviews; Breath Training Tool 1000+ en de PRO ($6,25) 100+; OnPace gratis 1000+ en OnPace+ ($5,99) 1+. Er zijn uitzonderingen: Atmos Air Quality ($2,49) staat op 10000+ met 1.086 reviews, terwijl het gratis Atmos Weather in dit paar op 100+ staat. Dit klopt met hoofdles 5 van Lars (betaald 4 tot 10% van gratis).
4. **Een vergelijking met en zonder broertje zegt weinig.** Betaalde apps met een gratis app van dezelfde maker: 51% haalt 100+, zonder: 45% (GEZIEN, losse naamkoppeling, klein verschil). Het broertje maakt de betaalde versie dus niet duidelijk groter; het vergroot vooral het bereik van de maker.
5. **De winkel wordt drukker.** In de eerste 16 dagen van november kwamen er 951 nieuwe apps, widgets en datavelden bij, 208 betaald (GEZIEN). Bij de apps van augustus tot november haalt nog geen enkele betaalde app 1000+, maar die zijn ook nog jong. Of de winkel echt harder groeit dan eerder kan ik niet zeggen: de lijst van de API stopt rond 5.000 regels en mist oudere apps, dus de aantallen per maand zijn scheef. Het aandeel betaald is wel stabiel rond een vijfde.
6. **Op Reddit winnen gratis apps met een eigen probleem in de eerste zin.** De vijf best scorende "[New App]"-berichten (176, 121, 42, 38 en 27 upvotes) waren alle vijf gratis of gratis te proberen en begonnen met een eigen ergernis: "I got tired of calling the minute to the late joiners" (Synchrono), "checking my glucose meant pulling out my phone" (GGlance), een vriend die onwel werd zonder dat iemand zijn medicijnen wist (Medical ID Wallet), een boot in Nederland zonder logboek (Deadreckon). GGlance staat nu op 1000+ met 22 reviews, Medical ID Wallet op 1000+ (GEZIEN). Een betaalde app die een week gratis was bij de lancering (Toma, nu $2,49) kreeg 8 upvotes en staat op 10+ (GEZIEN). Dat bevestigt run 7: een post is een klein lot, en een gratis app met een eerlijk verhaal heeft de beste kans.

### Drie lessen
1. **Een betaalde Garmin-app moet het met 100 tot 1000 kopers doen, en dat is haalbaar.** De helft van de betaalde apps haalt 100+ in een paar maanden; Ski Pin deed 68 in de eerste maand met een duidelijk probleem voor een vaste groep. Reken voor Ebb niet met duizenden, maar met de eerste 100.
2. **Bereik komt van gratis, geld van betaald, en ze verhouden zich ongeveer 10 op 1.** Wie bereik wil voor filmpjes, Reddit en reviews heeft een gratis versie nodig; de betaalde versie haalt een tiende daarvan.
3. **Proberen kan bij Garmin Pay alleen via een gratis broertje of een tijdelijk lagere prijs, niet via een proefmodus.** Een proef buiten Garmin werkt voor downloads, maar dat vraagt een ontgrendelcode, en hoeveel mensen dan betalen weet niemand openbaar.

### Eerlijk: wat deze meting niet zegt
- Downloads in klassen; reviews zijn maar een klein deel van de kopers (bij Ski Pin minstens 68 kopers in januari, 5 reviews nu).
- Voor gratis apps met proef zie ik downloads, niet de betalers. Mijn indeling op woorden kan apps verkeerd plaatsen.
- De lijst van de API stopt rond 5.000 regels. Apps die lang niet zijn bijgewerkt kunnen ontbreken; dat maakt de vergelijking per model niet scheef zolang het voor alle modellen geldt, maar zeker weten doe ik dat niet (GOK).
- Reddit: alleen juli en september gelezen.

### Voorstel voor Dortus deze week
**Gijs: geen proefmodus voor Ebb (kan niet bij Garmin Pay); het gratis broertje Ebb Calm is de weg, en die is al ingediend (winkel-API 16 nov ±07:20 UTC: "not approved", dus nog in behandeling, GEZIEN). Doe twee dingen zodra hij goedgekeurd is. (1) Kijk of de eerste regel van de beschrijving van Ebb Calm een gemis noemt, geen naam ("Breathe for one minute without reaching for your phone" of iets dergelijks), met één regel en een link naar Ebb. (2) Zet één bericht "[New App] - Ebb Calm" voor r/Garmin klaar op `organisatie/lijst-thijs.md`, met de opbouw van de vijf beste berichten: een eerlijke eigen aanleiding in de eerste zin, "free", wat het doet, en dat de maker vragen beantwoordt. Thijs plaatst het en antwoordt op de dag zelf.** Waarom: Ebb staat na 3 dagen op 0; een gratis versie haalt volgens 74 paren ongeveer tien keer het bereik van een betaalde, en de best scorende posts waren gratis met een eigen verhaal. Meten: Gijs telt in `meting-ebb.md` de downloadklasse en reviews van Ebb en Ebb Calm op de dag van het bericht en 7 en 30 dagen erna; doel na 30 dagen: Ebb Calm 100+, Ebb 10+ (GOK, afgeleid uit de tabel).

---

## 7. r/Garmin "[New Watch Face]": 275 berichten van kleine makers, naast de winkel gemeten. Wat levert een Reddit-post op voor een Garmin-wijzerplaat?

Onderzocht 16 nov 2026, run 7. Open vraag uit run 6: een Garmin-maker die met Reddit groeide. Reddit zelf is vanuit de cloud niet te lezen (403), maar het archief Arctic Shift wel. Op r/Garmin plaatsen makers hun nieuwe wijzerplaat met de kop "[New Watch Face] - naam" (40 tot 60 per maand). De winkel van Garmin geeft per app openbaar de downloads (in klassen: 1, 10, 100, 1000, 10000), het aantal reviews en de datum van elke review. Zo kon ik per bericht zien wat er in de winkel gebeurde, en in welke week. Dit raakt Ebb direct: Ebb ($4,99) staat sinds 13 nov in de winkel en had op 16 nov 02:03 nog 0 downloads (`platformen/garmin/meting-ebb.md`).

### Bronnen
- Berichten: Arctic Shift (https://arctic-shift.photon-reddit.com/api/posts/search, subreddit Garmin, zoekterm "New Watch Face", 1 jun tot 16 nov 2026, curl). 275 berichten met die kop, met upvotes, reacties en tekst (GEZIEN).
- Winkel: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` (downloadCount, reviewCount, averageRating, firstApprovalDate) en `.../apps/<id>/reviews` (datum per review), curl, 16 nov (GEZIEN). 120 berichten hadden een winkellink; 98 andere vond ik via de zoekbalk van de winkel op naam, met een goedkeuringsdatum binnen 45 dagen na of 60 dagen vóór het bericht. 218 van 275 gekoppeld. De naamkoppeling kan bij een paar fout zijn (GOK, niet elk nagekeken).
- De ruwe tabel: `platformen/succes/data/rgarmin-wijzerplaten-2026-11-16.csv`.
- Klacht op de subreddit: "RANT: Low effort Watchface tsunami", 5 nov 2026, 63 upvotes (Arctic Shift, GEZIEN).

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Upvotes per bericht, mediaan | **1** (75% heeft 1 of minder, 90% heeft 10 of minder, hoogste 331) | GEZIEN |
| Samenhang upvotes en downloadklasse (Spearman, berichten vóór okt) | 0,13; met reviews 0,22 | GEZIEN, eigen berekening |
| Wijzerplaten met 0 tot 4 upvotes die toch 1000+ downloads haalden | 34 van 123 (vóór okt) | GEZIEN |
| Dagen tussen goedkeuring en bericht, mediaan | 3 | GEZIEN |
| Reviews in de week na het bericht, mediaan, 22 berichten met 20+ upvotes | 5 | GEZIEN, eigen telling |
| Hetzelfde, 20 willekeurige berichten met 0 tot 4 upvotes (met minstens 5 reviews) | 2 | GEZIEN; deze groep is gekozen op 5+ reviews, dus eerder te hoog |

### Wat ik zag, in volgorde
1. **Een bericht verdwijnt bijna altijd.** De helft krijgt 1 upvote. De klacht van 5 nov zegt het hard: "99% of these WF announcement posts have 0 responses", en de makers "are making zero or low effort to engage with the user base" voor een wijzerplaat van "$3 - $5". Zijn advies: praat met de mensen, of maak een gratis versie waarmee ze kunnen terugpraten (GEZIEN).
2. **De winkel doet het meeste, niet Reddit.** Een derde van de wijzerplaten met 0 tot 4 upvotes kwam toch in de klasse 1000+. Quipu (27 upvotes) staat op 10000+ en 238 reviews, waarvan 158 meer dan 4 weken na het bericht (GEZIEN). Bij de meeste kwamen de reviews gelijkmatig binnen, ook zonder Reddit.
3. **Veel upvotes is niet veel installaties.** Het hoogste bericht van het halve jaar, Margin Notes (331 upvotes, 47 reacties, 28 okt), is een wijzerplaat die je meteen betaalt ($2,99, met een losse proefversie "TR"). Na 19 dagen: 10+ downloads en 4 reviews, de proefversie 100+ en 3 reviews (GEZIEN). Mensen vonden het plaatje mooi; installeren deden ze niet.
4. **Wat wel werkte: een probleem in de kop, gratis proberen, en lokken om te reageren.** Eén maker (llelibro) plaatste op 28 okt twee wijzerplaten met hetzelfde trucje (de klok loopt 2 tot 15 minuten voor, zodat je op tijd komt).
   - Telex, kop "retro, feature-packed. free install": 0 upvotes, 1 reactie (GEZIEN).
   - Ahead, kop "tricks you into being early, for my adhd friends": 178 upvotes, 105 reacties. De tekst begint met de vraag "Are you constantly 5 minutes late to everything?", is gratis te installeren met 7 dagen proef en daarna $3,99, en zegt "First five commenters get a free lifetime code" (GEZIEN).
   Zelfde maker, zelfde dag, zelfde functie: alleen de kop en de eerste zin verschillen. Zijn volgende, Pitboard (12 nov), deed het weer: "first 10 commenters get a free lifetime code", 30 dagen gratis te houden, 37 upvotes, 50 reacties, en 14 reviews in de eerste 4 dagen (GEZIEN).
5. **Maar ook bij Ahead kwam het meeste niet van Reddit.** Ahead stond al sinds 3 sep in de winkel en had 26 van zijn 37 reviews vóór het bericht; in de week erna kwamen er 8 bij (GEZIEN). En Telex, met 0 upvotes, kreeg in die week 10 reviews; de maker plaatste Telex ook op r/GarminWatchFaces (link in zijn Pitboard-bericht), wat ik niet gemeten heb. Reddit geeft dus een duw van enkele reviews, geen lancering.
6. **De twee echte doorbraken hadden iets wat de rest niet had.** RASTER (159 upvotes, 26 aug): 39 reviews in week 1, 90 in week 2 tot 4, 103 daarna, nu 10000+ downloads (GEZIEN). Meridian (183 upvotes, 15 jun): 17 reviews in week 1, nu 1000+. Bij RASTER groeide het na de eerste week door; mijn lezing is dat de duw van Reddit hem in de winkel hoger zette en de winkel het daarna overnam (GOK: de rangorde van de winkel per dag heb ik niet).

### Drie lessen
1. **Een Reddit-post voor een Garmin-product is een loterij met een kleine prijs, maar wel een gratis lot.** Mediaan 1 upvote; een goede post geeft enkele reviews extra in de eerste week. Reken er niet op als lancering. Voor Ebb: de winkel zelf (zoekwoorden, naam, plaatjes, reviews) is belangrijker.
2. **Begin met het probleem van een herkenbare groep, niet met hoe het eruitziet.** "Tricks you into being early, for my adhd friends" tegen "retro, feature-packed": hetzelfde product, 178 tegen 0 upvotes. Dit past bij les "noem wat mensen missen in de eerste zin" uit verhaal 5 (Notebook Navigator).
3. **Op een overvolle plek wint wie iets teruggeeft: gratis proberen en de eerste reageerders iets geven.** Meteen betalen haalde zelfs met 331 upvotes bijna niets. Gratis installeren met proeftijd, of een paar levenslange codes voor de eerste reageerders, gaf reacties en reviews. Dat sluit aan bij de klacht op de subreddit zelf.

### Eerlijk: wat deze meting niet zegt
- Downloads staan in klassen (10, 100, 1000), dus kleine verschillen vallen weg. Reviews zijn exact, maar een review is maar een klein deel van de installaties (hoeveel, weet ik niet).
- Alleen berichten met de kop "[New Watch Face]"; apps ("[New App]") gaf het archief deze run niet (time-outs). Ebb is een app, geen wijzerplaat.
- Upvotes zijn van het moment van archiveren; latere stemmen kunnen ontbreken.
- De paar verhalen (Ahead, Telex, Margin Notes) zijn klein in aantal. Het verschil Ahead tegen Telex is sterk, maar het blijft één maker.

### Voorstel voor Dortus deze week
**Gijs: kijk of Ebb een proeftijd kan krijgen (Connect IQ heeft een proefmodus; de winkel-API gaf op 16 nov ±06:55 UTC voor Ebb `hasTrialMode: false` en nog steeds 0 downloads, GEZIEN) en zet daarna één bericht klaar voor r/Garmin op `organisatie/lijst-thijs.md`, met de kop als probleem ("[New App] - Ebb: ..., for people who ..."), eerlijke eerste zin, gratis proberen, en 5 levenslange codes voor de eerste reageerders als Garmin dat toelaat. Thijs plaatst het zelf en beantwoordt de reacties op de dag zelf.** Waarom: Ebb staat na 3 dagen op 0 downloads; een post kost niets, maar alleen de vorm "probleem, gratis proberen, iets teruggeven" werkte hier. Meten: Gijs telt in `meting-ebb.md` de reviews en de downloadklasse de dag ervoor en 7 dagen erna, en zet de upvotes erbij.

**Correctie 16 nov (run 8):** het deel "proefmodus voor Ebb" vervalt. Garmin Pay kent geen proeftijd en Ahead verkoopt via een eigen PayPal-link. Zie het voorstel bij verhaal 8.

---

## 6. This Week in Obsidian (kleine nieuwsbrief, ±800 abonnees): wat doet een vermelding als "Gem of the Week" met de downloads? Gemeten bij 34 plugins

Onderzocht 16 nov 2026, run 6. Open vraag uit run 5: een nieuwsbrief als kanaal, gemeten in de downloads. Ik koos geen maker die het zelf vertelt, maar een meting die ik zelf kan doen. This Week in Obsidian is een wekelijkse nieuwsbrief (elke dinsdag, sinds 23 dec 2025) die elke week één plugin uitlicht als "Gem of the Week". Alle nummers staan openbaar op GitHub, en van elke Obsidian-plugin is de downloadteller per week openbaar. Zo kon ik voor elk uitgelicht plugin kijken wat er in de week van het nummer gebeurde. Dit is dus geen succesverhaal van één maker, maar een toets van een kanaal dat kleine makers vaak aangeraden krijgen ("probeer in de nieuwsbrieven te komen").

### Bronnen
- De nummers: GitHub boundless-forest/this-week-in-obsidian, map `archive/` (47 nummers, 23 dec 2025 tot 10 nov 2026), gekloond met git. De werkafspraken in `AGENTS.md` zeggen dat de inhoud uit een generator komt (`gen-newsletter-obsidian`) en daarna wordt nagekeken (GEZIEN).
- Aankondiging en reacties op het forum: https://forum.obsidian.md/t/110776 (Discourse-JSON met curl): gestart omdat Obsidian Roundup stillag, "1-2 hours per issue" (EIGEN OPGAVE), draad 2.924 keer bekeken (GEZIEN).
- Aantal abonnees: de Substack-pagina https://thisweekinobsidian.substack.com/about (curl) geeft "Hundreds of subscribers" en in de paginadata `freeSubscriberCountOrderOfMagnitude: 803` (GEZIEN). Ik lees dat als ongeveer 800 gratis abonnees (GOK hoe Substack dat getal afrondt).
- Downloads per week en versiedatums per plugin: Obsidian Stats van Moritz Jung (https://www.moritzjung.dev/obsidian-stats/, data `/data/plugins/downloads/<id>.json` en de versietabel op de pluginpagina, curl). De reeksen lopen tot ±27 okt 2026, dus de laatste 5 nummers vallen af.
- Pluginlijst en tellers: `community-plugins.json` en `community-plugin-stats.json` van obsidianmd/obsidian-releases (curl, 16 nov).
- Controlegroep: 90 willekeurige plugins met meer dan 20.000 downloads (uit 655), dezelfde bron.
- De ruwe tabel staat in `platformen/succes/data/twio-gems-2026-11-16.csv`.

### Hoe ik mat
Per nummer: downloads in de week van het nummer (maandag ervoor tot maandag erna), gedeeld door het gemiddelde van de 3 weken ervoor. Dat noem ik de factor. Dezelfde factor voor de controlegroep in dezelfde week, om drukke en stille weken van heel Obsidian eruit te halen. Daarnaast: was er een nieuwe versie van de plugin in de 2 weken ervoor of in de week zelf? Bij Obsidian telt elke download mee, ook een update (zie verhaal 5). Een nieuwe versie geeft dus een sprong in de teller zonder één nieuwe gebruiker.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Nummers met een Gem of the Week | 47, waarvan 34 te meten (rest: plugin niet in de winkel, reeks te kort of na 27 okt; agent-client weggelaten, teller werd die week gecorrigeerd) | GEZIEN |
| Factor in de week van het nummer, mediaan | 1,34 | GEZIEN, eigen berekening |
| Na correctie voor heel Obsidian, mediaan | 1,27 (17 van 34 boven 1,3; 6 onder 1) | GEZIEN, eigen berekening |
| Factor in de week **vóór** het nummer, mediaan | 1,35 | GEZIEN, eigen berekening |
| Week vóór het nummer al boven 1,5 | 16 van 34; bij 12 daarvan kwam die week een nieuwe versie uit | GEZIEN |
| Nieuwe versie in de 2 weken ervoor of de week zelf | **30 van 34 uitgelichte plugins (88%)** | GEZIEN |
| Hetzelfde bij de controlegroep, zelfde weken | 20% | GEZIEN, 45 controleplugins x 42 weken |
| Extra downloads in de nummerweek boven de basis, mediaan | ±390 | GEZIEN, maar vooral updates |
| De 4 nummers zonder nieuwe versie in de buurt | +152 (Auto Link Title), +115 (Typewriter Mode), en twee dalingen | GEZIEN |

### Wat ik zag, in volgorde
1. **Op het eerste gezicht werkt het.** In de week van het nummer gingen de uitgelichte plugins gemiddeld een derde omhoog, ook na correctie voor heel Obsidian. Uitschieters: Vertical Tabs x2,67, Reminder x2,07, Task List Kanban x1,94, Maps x1,80, Share Note x1,74 (GEZIEN).
2. **Maar de sprong begon meestal al een week eerder.** De mediaan van de week vóór het nummer (1,35) is even hoog als die van de nummerweek (1,34). Bij Reminder was de week ervoor al x4,27, bij Various Complements x4,14, Vertical Tabs x3,65, Readwise x3,33, Maps x3,32 (GEZIEN). Een nieuwsbrief kan geen downloads geven vóór hij verschijnt.
3. **De nieuwsbrief kiest plugins die net een nieuwe versie hebben.** 30 van de 34 uitgelichte plugins brachten in de 2 weken ervoor of in de week zelf een versie uit, tegen 20% van vergelijkbare plugins in dezelfde weken (GEZIEN). Veel uitgelichte plugins zijn oud (Hider uit 2020, Auto Link Title uit 2021): ze kwamen in beeld omdat er iets nieuws was. De inhoud komt uit een generator (GEZIEN, AGENTS.md); dat die op nieuwe versies en Reddit-berichten van de afgelopen week let, is mijn lezing (GOK, de generator zelf is niet openbaar).
4. **Een nieuwe versie geeft op zich al zo'n sprong.** Bij Obsidian telt elke update als download. Wie duizenden gebruikers heeft, ziet na een versie honderden tot duizenden extra downloads, en die vallen in dezelfde weken als het nummer. Vergeleken met hun eigen eerdere weken mét een nieuwe versie zaten de uitgelichte plugins in de nummerweek maar iets boven het midden (mediaan ±60e percentiel van hun eigen versieweken, GEZIEN, eigen berekening per plugin).
5. **Waar geen nieuwe versie was, bleef weinig over.** Bij de 4 schone gevallen: +152 en +115 downloads in de week, en twee dalingen (GEZIEN). Dat past bij ±800 abonnees: als de helft opent en een paar procent op de uitgelichte plugin klikt, zijn dat tientallen tot hooguit een paar honderd installaties (GOK, open- en klikcijfers van deze nieuwsbrief zijn niet openbaar).
6. **Lezers kunnen sinds 19 aug zelf plugins aandragen** via een formulier op GitHub ("Add content suggestion workflow", GEZIEN in de commits), en nummer 46 noemt "reader suggested plugins" (GEZIEN). Een maker kan dus zijn eigen plugin aandragen. Of dat meer oplevert dan wat ik hierboven mat, weet ik niet.

### Drie lessen
1. **Een kleine nieuwsbrief is geen groeikanaal op zich; hij versterkt nieuws dat er al is.** De nieuwsbrief volgt wat er gebeurt (een nieuwe versie, een Reddit-bericht) en zet het nog eens in beeld. Het nieuws zelf geeft de sprong. Voor ons: eerst iets uitbrengen dat het melden waard is, dan pas aandragen bij lijstjes en nieuwsbrieven. Dit past bij hoofdles 9 in `lessen.md` (op een moment lanceren) en bij Fenna's les over in de lijstjes komen.
2. **Lees een sprong in de teller niet als groei voordat je weet wat de teller telt.** Bij Obsidian telt elke update mee, dus na een nieuwe versie springt de teller zonder nieuwe gebruikers. Bij extensions.blender.org is dat anders: de broncode telt één download per extensie per IP-adres of per ingelogde gebruiker (GEZIEN: `stats/models.py` in projects.blender.org/infrastructure/extensions-website, unieke sleutel op extensie plus IP en op extensie plus gebruiker). Een update van iemand die Click Joints al had, telt daar dus niet opnieuw, tenzij zijn IP-adres veranderde. Voor Garmin (Ebb) heb ik niet uitgezocht wat de teller telt.
3. **"Uitgelicht" en "geholpen" zijn twee verschillende dingen.** Een lijstje of nieuwsbrief kiest vaak wat al stijgt. Wie alleen naar uitgelichte producten kijkt, denkt dat uitlichten werkt. De vergelijking met de week ervoor en met een controlegroep liet hier zien dat het effect klein is. Dezelfde val geldt voor onze eigen metingen na een filmpje of bericht: kijk ook naar de week ervoor.

### Eerlijk: wat deze meting niet zegt
- Het gaat om één kleine nieuwsbrief. Een grote nieuwsbrief of site (zoals MacStories, die in nov 2023 "Obsidian Plugin Gems" schreef, achter een betaalmuur, GEZIEN alleen de kop) kan wel veel doen; dat heb ik niet gemeten.
- Weken zijn grof en ik verdeel de teller lineair tussen meetpunten. Een effect van een paar dagen kan wegvallen.
- De downloadteller van Obsidian had rond 1 nov 2026 een correctie (zie verhaal 5); mijn reeksen stoppen ervoor, maar er zitten meer rare dalingen in (RSS Dashboard x0,34, Continuous Mode x0,39), waarschijnlijk tellerfouten.
- Ik weet niet hoe de gems gekozen worden; de samenhang met nieuwe versies is sterk (88% tegen 20%), de reden is GOK.

### Voorstel voor Dortus deze week
**Bram: breng Click Joints 0.1.1 (gratis) en Pro 1.0.2 uit zodra Daan ja zegt, en schrijf bij elke versie twee zinnen "wat is nieuw" die een gebruiker iets zeggen (niet "fixes"). Chris maakt van die versie het filmpje van die dag (de kniefout die nu goed gaat, voor en na). Hoofdchat: zet pas daarna een bericht klaar voor Thijs om de gratis versie aan te dragen bij één Blender-nieuwssite of nieuwsbrief (bijvoorbeeld BlenderNation, die een formulier voor tips heeft; GOK, niet nagekeken), met de nieuwe versie als nieuws.** Waarom: deze meting laat zien dat lijstjes nieuws volgen, en dat het nieuws (een versie met een zichtbare verbetering) zelf de sprong geeft. Meten: Bram noteert in `downloads.csv` de datum van elke versie en van elk bericht, en vergelijkt de week erna met de week ervoor. Omdat extensions.blender.org per IP telt, is een sprong daar echte nieuwe mensen, geen updates.

---

## 5. Notebook Navigator (Johan Sanneblad, solo, Zweden): een gratis Obsidian-plugin die in een jaar de populairste werd, met een Reddit-post vóór de winkel, lange uitlegvideo's en een welkomstscherm met video

Onderzocht 16 nov 2026, run 5. Open vraag uit run 4: Reddit of nieuwsbrieven als kanaal voor een kleine tool. Reddit zelf is voor ons niet leesbaar (403 met curl), dus ik zocht een maker wiens kanalen ik wel kon nameten. Notebook Navigator is een vervanger van de bestandslijst in Obsidian, "Apple Notes, Bear en Evernote voor Obsidian". Hij kwam in sep 2025 in de winkel en stond in aug 2026 bovenaan de Obsidian-gids. Het is gratis, dus het is een verhaal over bereik, niet over geld. Lars doet Obsidian-plugins als product; ik kijk hier alleen naar de kanalen.

### Bronnen
- Forum Obsidian (Discourse-JSON met curl): de aankondiging van 15 sep 2025 (https://forum.obsidian.md/t/105704), de draad "Missing community plugin" van 29 jul 2025 (https://forum.obsidian.md/t/103454), de oude verzoekdraad uit 2022 waarin hij reageerde (https://forum.obsidian.md/t/40361), zijn verzoek aan Obsidian van 1 dec 2025 (https://forum.obsidian.md/t/108593) en zijn profiel (https://forum.obsidian.md/u/johansan/summary.json).
- Downloadreeks per week en versielijst: Obsidian Stats van Moritz Jung (https://www.moritzjung.dev/obsidian-stats/plugins/notebook-navigator/, data `/obsidian-stats/data/plugins/downloads/notebook-navigator.json`, curl).
- Tellers nu: `community-plugin-stats.json` en `community-plugins.json` van obsidianmd/obsidian-releases (curl, 16 nov 2026 ±04:00 UTC); sterren, issues en commits van obsidianstats.com (https://www.obsidianstats.com/plugins/notebook-navigator, curl).
- Zijn website (https://notebooknavigator.com/ en https://notebooknavigator.com/apple-notes/) en de README (raw.githubusercontent.com, curl).
- Zijn YouTube-kanaal @JohanSanneblad: de openbare lijst met views en lengte (yt-dlp `--flat-playlist`). Uploaddatums kreeg ik niet (YouTube vraagt om in te loggen), dus de datums van de video's hieronder zijn afgeleid uit de versies.
- Discord: aantal leden via de openbare uitnodiging (discord.com/api/v9/invites/6eeSUvzEJr?with_counts=true); de aanmaakdatum uit het server-id.
- Buy Me a Coffee: https://www.buymeacoffee.com/johansan (teller op de pagina).
- Nieuwsbericht van Sébastien Dubois, 20 aug 2026: https://www.dsebastien.net/notebook-navigator-is-now-obsidians-most-popular-plugin/

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Downloads nu (alle versies samen) | 1.150.094 | GEZIEN, stats.json 16 nov |
| Eerste meetpunt, 15 sep 2025 | 33.231 | GEZIEN, Obsidian Stats |
| Na ruim twee maanden | "over 150 000 downloads in just over two months" | EIGEN OPGAVE, forum 1 dec 2025 |
| Groei per week, sep tot dec 2025 | ±8.400 tot 16.000 | GEZIEN |
| Groei per week, apr tot sep 2026 | ±18.000 tot 31.000 | GEZIEN |
| Groei per week, okt 2026 | ±12.000 tot 16.000 | GEZIEN (daling, oorzaak niet uitgezocht; rond 1 nov werden ook nepdownloads uit alle tellers gehaald, zie `platformen/obsidian/volgend-product.md`) |
| Versies | 188 in ±14 maanden | GEZIEN |
| Versie 3.4.3, ±4 weken de nieuwste (26 sep tot eind okt) | 75.036 downloads | GEZIEN |
| GitHub-sterren, issues | 2.846 sterren, 1.300 issues (4 open), 1.986 commits | DERDEN, obsidianstats.com |
| YouTube-abonnees | 2.960 | GEZIEN |
| "Mastering Notebook Navigator" (29:48) | 118.000 views | GEZIEN |
| "Mastering Notebook Navigator 3" (64:15), ±aug 2026 | 110.000 views | GEZIEN, datum DERDEN (Dubois) |
| "Notebook Navigator 3.0 - The writer's release" (5:50) | 16.000 views | GEZIEN |
| "What's New in Notebook Navigator 2.1" (12:38) | 8.200 views | GEZIEN |
| Discord | 575 leden, server gemaakt 14 aug 2025 | GEZIEN |
| Buy Me a Coffee | 546 supporters | GEZIEN, bedragen onbekend |
| Zijn twee eerdere plugins | Featured Image 46.469, Pixel Perfect Image 31.280 | GEZIEN |
| Ter vergelijking: oudere concurrent File Explorer Alternative (`file-tree-alternative`) | 360.438 | GEZIEN |

**Pas op met het downloadcijfer.** Een download is ook een update. Met 188 versies telt elke bestaande gebruiker vele keren mee. Daarom kijk ik naar versie 3.4.3, die ongeveer vier weken de nieuwste was: 75.036 downloads. Dat zijn vooral gebruikers die bijwerkten plus nieuwe installaties. Mijn schatting: **in de orde van 70.000 gebruikers die bijwerken** (GOK, afgeleid uit die ene versie; wie automatisch bijwerken uit heeft, telt niet mee, wie op meer apparaten werkt telt dubbel). "Populairste plugin" in het bericht van Dubois slaat op de Obsidian-gids; in totale downloads staat hij nog ver achter Excalidraw (9,1 miljoen, GEZIEN). Waarop de gids sorteert, heb ik niet vastgesteld.

### Wat hij deed, in volgorde
1. **Eerst twee kleine plugins rond hetzelfde idee** (GEZIEN, forum en stats): Featured Image in nov 2024 ("Create Note Lists like Apple Notes, Bear and Evernote", nu 46.469) en Pixel Perfect Image in feb 2025 (31.280). Zijn grote plugin bouwt daarop voort; de feature images uit de eerste plugin zitten erin.
2. **Een vraag die er al lang lag.** Op het forum stond sinds jul 2022 het verzoek "Plugin for 3-Pane File Explorer with Note Previews": 14.245 keer bekeken, 73 likes (GEZIEN). Hij schreef zelf: eerst "nearly six months of sporadic planning and feature collection, and then another six months of intense development. Over thousand hours spent" (forum 15 sep 2025).
3. **Reddit vóór de winkel.** Op 9 jun 2025 plaatste hij in r/ObsidianMD "I missed Apple Notes, so I created it as an Obsidian plugin" (DERDEN: een gebruiker citeert de titel en datum op het forum; Reddit zelf kon ik niet lezen). Een dag eerder had hij de plugin ingediend; de keuring duurde tot eind jul en de opname tot ±15 sep. Gebruikers wachtten intussen: één schreef op 29 jul dat hij al 50 dagen elke keer in de winkel keek (GEZIEN). Op 27 aug wees een andere gebruiker al naar de website notebooknavigator.com (GEZIEN). De Discord kwam op 14 aug (GEZIEN). Hoeveel stemmen de Reddit-post kreeg, weet ik niet.
4. **De dag van de opname** (±15 sep 2025): een aankondiging in Share & showcase (7.770 keer bekeken, 75 likes, GEZIEN) en een reactie in de oude verzoekdraad van 2022: "This plugin has everything everyone has ever requested when it comes to 3-pane layouts" (GEZIEN). Een moderator sloot die draad een dag later "because there are multiple plugins implementing this now".
5. **Heel vaak bijwerken, en dat steeds melden in dezelfde draad.** 188 versies in 14 maanden (GEZIEN). Op 7 okt: "Lots of new features since I posted this two weeks ago" met een lijst; op 28 okt bij versie 1.7: "If you missed File Explorer Alternative (which hasn't been updated for over a year), this is for you!" (GEZIEN). Hij noemt dus met naam de verlaten concurrent.
6. **De gebruikers voor zich laten pleiten.** Op 1 dec 2025 vroeg hij Obsidian om een instelling "standaard bestandslijst" voor plugins zoals de zijne. Dat verzoek kreeg 142 likes en 3.152 views (GEZIEN), meer dan zijn eigen aankondiging.
7. **Lange uitlegvideo's, en de plugin wijst er zelf naar.** Twee masterclasses van 30 en 64 minuten haalden elk ±110.000 tot 118.000 views op een kanaal van 2.960 abonnees; zijn korte "wat is nieuw"-video's 8.200 en 16.000 (GEZIEN). De README zegt dat de plugin bij de eerste start een welkomstvenster toont met een YouTube-plaatje (de video), en bij elke update een "wat is nieuw"-venster met een banner of een filmpje (GEZIEN, README hoofdstuk 11.3). De masterclass van versie 3 heeft ondertiteling in 21 talen (README); Dubois schrijft dat hij de stem met ElevenLabs in 20 talen liet nasynchroniseren (DERDEN). Mijn lezing: elke nieuwe gebruiker krijgt de video te zien op het moment dat hij hem nodig heeft, en dat verklaart de vele views bij weinig abonnees (GOK, YouTube geeft de bron van views niet openbaar).
8. **21 talen en pagina's per overstapper.** De plugin en de site zijn er in 21 talen (GEZIEN). De site heeft aparte pagina's voor wie wegkomt van Apple Notes, Bear, Evernote, OneNote en Day One, bijvoorbeeld "The Apple Notes alternative, for people who want more" met de stappen om over te stappen (GEZIEN). Wanneer die pagina's kwamen en hoeveel bezoek ze brengen, weet ik niet.
9. **Gratis, met fooien.** GPL-3.0, gratis, met Buy Me a Coffee (546 supporters) en GitHub Sponsors (GEZIEN). Geen betaalde versie.

### Drie lessen
1. **Noem de app die mensen missen, in de eerste zin.** Zijn Reddit-titel was geen productnaam maar een gemis: "I missed Apple Notes, so I created it". Daarna zegt alles hetzelfde: "Apple Notes, Bear & Evernote for Obsidian", een pagina per app waar mensen vandaan komen, en met naam de verlaten concurrent. Wie die app kent, snapt in één regel wat het doet. Dit past bij de regel in `regels.md` dat de belofte meteen duidelijk moet zijn.
2. **Zet de uitlegvideo in het product zelf.** De twee lange masterclasses haalden elk bijna 40 keer zoveel views als zijn kanaal abonnees heeft, de korte filmpjes maar een fractie (GEZIEN). De plugin toont de video bij de eerste start en een filmpje bij elke update. Zo hoeft de video niet gevonden te worden in een feed; hij wordt bekeken door wie het net installeerde. Dit is het derde verhaal (na VibeDesk en Blender Secrets) waarin uitleg die een vraag beantwoordt meer doet dan reclame.
3. **Een Reddit-post vóór de lancering werkt als wachtlijst, als het product er daarna snel en vaak bij komt.** Mensen keken 50 dagen in de winkel. Daarna hield hij de aandacht vast met tientallen versies en meldingen in dezelfde draad. Let op: het bewijs voor de Reddit-post is één citaat; de kracht ervan (stemmen, bezoekers) kon ik niet meten.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij werkte ruim duizend uur aan één product met tientallen jaren ervaring (Apple, EA, Google volgens zijn site, EIGEN OPGAVE). Het product is echt goed; de kanalen versterkten dat, ze maakten het niet.
- Een bestandslijst gebruik je elke dag; een kleine tool zoals Click Joints of Ebb gebruik je minder vaak. Het welkomstscherm werkt pas als er installaties zijn.
- Het is gratis. Over geld leert dit verhaal alleen dat fooien bij ±70.000 gebruikers 546 supporters gaven (bedragen onbekend). Dat past bij hoofdles 5 in `lessen.md`: het betaalde deel haalt een klein deel van het gratis publiek.
- Een dagelijkse plugin met veel versies krijgt veel update-downloads; vergelijk zijn 1,15 miljoen dus niet met de 41 van Rollwright.

### Voorstel voor Dortus deze week
**Bram: zet in Click Joints Pro (de betaalde versie op Superhive) bij de eerste start een klein welkomstvenster of een knop "Getting started" met de link naar één uitlegvideo van 1 tot 3 minuten. Chris maakt die video (echte Blender-beelden, een gewricht van begin tot print), en zet hem ook bovenaan de Superhive-pagina.** Waarom: wie Pro koopt, moet in de eerste minuut slagen; de video wordt dan bekeken door de mensen die hem nodig hebben, en het kost één venster. De regels van extensions.blender.org (geen reclame voor betaald in de gratis versie) gelden voor de gratis listing; voor Pro op Superhive niet, maar zet in de gratis versie niets. Voor de lanceerberichten van Click Joints en Ebb: Chris schrijft de eerste regel als gemis ("I wanted X in Blender, so I made it"), niet als productnaam; Thijs plaatst. Meten: views van die ene video tegen het aantal verkochte Pro-licenties.

---

## 4. Blender Secrets (Jan van den Hemel, solo, Gent): elke dag een Blender-tip van een minuut zonder gezicht, en een e-book van $52 met 15.000+ verkopen

Onderzocht 16 nov 2026, run 4. Open vraag uit run 3: een Blender- of printmaker die groeide met tips-filmpjes, niet met productfilmpjes. Waarom dit verhaal: dit is het tegenvoorbeeld van mijn les uit verhaal 3 ("een echt persoon is de haak"). Jan van den Hemel maakt sinds aug 2018 bijna elke dag een schermopname van één Blender-handeling, zonder gezicht, met een nummer erbij ("Daily Blender Tip #1"). Daarmee bouwde hij een kanaal van 292.000 abonnees en verkoopt hij de verzamelde tips als e-book. Hij werd er fulltime maker door.

### Bronnen
- Interview met hem (Subkit / Collabs.io Mag, ±2022, curl): https://gosolo.subkit.com/blender-secrets
- Gumroad, productpagina met verkoopteller in de pagina (`sales_count`, curl): https://blendersecrets.gumroad.com/l/IxofeY
- Superhive, productpagina met "Sales 2000+" (curl): https://superhivemarket.com/products/blender-secrets
- YouTube-kanaal @blendersecrets (tellers op de pagina, curl) en de volledige lijst van alle 1.016 uploads met views en lengte (yt-dlp, alleen de openbare lijst, `--flat-playlist`): https://www.youtube.com/@blendersecrets
- BlenderNation: zijn auteurspagina's met elke dagtip als bericht, en datums (curl): https://www.blendernation.com/author/jan-van-den-hemel/page/50/ (tip 145 op 22 jan 2019), page/45 (tip 210 op 30 mrt 2019). Eerste e-book, 30 mrt 2019: https://www.blendernation.com/2019/03/30/100-amazing-blender-tips-vol-1-e-book/ . Update okt 2020: https://www.blendernation.com/2020/10/04/blender-secrets-e-book-update-promoted/ . 2000 pagina's, jul 2024: https://www.blendernation.com/2024/07/02/blender-secrets-e-book-now-2000-pages-promoted/
- TikTok @blendersecrets (blok in de pagina, curl) en Bluesky (openbare API).
- Niet gelukt: zijn eigen site blendersecrets.org en 3dsecrets.com (Cloudflare blokkeert curl), archive.org (geen antwoord), Instagram (inloggen gevraagd), uploaddatum per YouTube-filmpje (YouTube vraagt inloggen). Datums haal ik dus uit BlenderNation, niet uit YouTube.

### Cijfers
- YouTube (GEZIEN 16 nov 2026): 292.000 abonnees, 35,2 miljoen views, 1.016 openbare uploads. TikTok: 11.800 volgers, 111 filmpjes, 100.700 likes. Bluesky: 4.033 volgers. Instagram is volgens hemzelf zijn startkanaal, maar de teller kon ik niet lezen.
- E-book "Blender Secrets", $52 (GEZIEN): op Gumroad **13.408 verkopen** en 1.751 beoordelingen (97% vijf sterren); op Superhive "2000+" verkopen en 25 beoordelingen, gepubliceerd "over 7 years ago". Samen dus minstens ±15.400 verkopen.
- Omzet: niet openbaar. GOK, grof: de prijs was vroeger lager (hij begon met 335 pagina's), en de Gumroad-teller telt kortingen mee. Bij gemiddeld $20 tot $35 per verkoop is dat ±$300.000 tot ±$540.000 bruto in ruim 7,5 jaar, vóór afdrachten. Dat hij zijn freelancewerk kon stoppen "since the e-book took off" (EIGEN OPGAVE, interview) past daarbij.
- Datums (GEZIEN op BlenderNation, één bericht per dagtip): tip 145 op 22 jan 2019, tip 210 op 30 mrt 2019, tip 246 op 5 mei 2019, tip 286 op 14 jun 2019. Dat is echt elke dag één, dus tip 1 viel rond eind aug 2018.
- Views per deel van de reeks (GEZIEN, views van nu, dus opgeteld over alle jaren; oude filmpjes hadden langer de tijd):

| Filmpjes | Mediaan views | Mediaan lengte |
|---|---|---|
| 1 tot 30 | 4.500 | 32 sec |
| 31 tot 100 | 2.350 | 95 sec |
| 101 tot 300 | 6.000 | 56 sec |
| 301 tot 600 | 17.500 | 52 sec |
| 601 tot 800 | 44.000 | 62 sec |
| 801 tot 1016 | 20.000 | 66 sec |

- Zijn eerste 30 filmpjes (GEZIEN): allemaal "Daily Blender Tip #n" met één handeling in de titel: "Select Connected Faces" (7 sec), "Hide Everything Except Selected" (5 sec), "Copy Animation From One Object To Another" (9 sec, nu 29.000 views), "Inset Individual Faces" (6 sec, nu 48.000, de beste van de 30). De kortste (5 tot 9 sec) doen het in de eerste 30 het best; vanaf tip 8 worden ze 20 tot 60 sec.
- Best bekeken ooit (GEZIEN): "The easiest modeling technique?" 560.000 (47 sec), "Hand Topology Animation" 397.000, "Texturing a face" 362.000, "Turn vertices into Holes" 328.000. Allemaal een tip, geen reclame.
- Zijn reclamefilmpjes (cursussen, e-book, uitverkoop, 7 stuks) hebben een mediaan van 10.000 views, tegen 16.000 voor het hele kanaal.

### Wat hij deed, in volgorde
1. **Een gat gezien dat hij zelf voelde.** "The tutorials on YouTube were all overly long, and it took me forever to find the info I really needed. So I started making those one-minute tutorials as it seemed nobody else was doing it" (interview). Hij was toen freelance motion designer en deed het "for fun in my spare time".
2. **Aug 2018: elke dag één tip, met nummer.** Schermopname, geen gezicht, geen stem nodig, één handeling per filmpje. Elke tip ging naar Instagram, YouTube, Twitter en als los bericht naar BlenderNation, de grote nieuwssite voor Blender waar iedereen berichten kan insturen. Zo stond hij elke dag op de voorpagina van de plek waar Blender-gebruikers nieuws lezen.
3. **Mrt 2019, na ±210 tips: het eerste e-book.** "100 Amazing Blender Tips: Vol. 1", 335 pagina's, op Gumroad, met de belofte "receive Volume 2 for free when it comes out". Het boek is de tips op papier, met extra stappen die niet in het filmpje pasten, en elk hoofdstuk linkt naar zijn filmpje. Zelf zegt hij: "I spent about a year doing daily videos on Instagram before I started using it to advertise my e-book."
4. **Vroeg verkopen, daarna laten groeien.** "Don't hide behind perfection. Get it out there and start selling it as soon as possible. I started selling my e-book when it was just a couple hundred pages." Updates gratis voor kopers; kopers stuurden wensen (okt 2020: één groot PDF en ordening per thema, "as per popular request"). Nu 2000+ pagina's en 600+ onderwerpen.
5. **Twee winkels, plus betaalde berichten.** Gumroad en Blender Market (nu Superhive). Bij grote updates een "promoted" (betaald) bericht op BlenderNation (okt 2020, jul 2024). Later cursussen op een eigen site (3DSecrets) en samenwerking met CG Boost.
6. **Gewoon doorgaan.** 1.016 uploads in ruim 7 jaar. De views per filmpje kwamen pas na honderden filmpjes op een hoger niveau (mediaan 2.350 bij 31 tot 100, 44.000 bij 601 tot 800).

### Drie lessen
1. **Gezichtloos kan wel, als elk filmpje iemand tijd bespaart.** Dit is de grootste gezichtloze groei in onze reeks: 292.000 abonnees met schermopnames zonder persoon. Het verschil met VibeDesk (verhaal 2, ook gezichtloos, bleef op 39 tot 363 views) zit niet in het gezicht maar in het onderwerp: VibeDesk liet zijn eigen product zien, Jan beantwoordt een vraag die elke Blender-gebruiker heeft. Dat bevestigt les 1 uit verhaal 3 en zwakt les 2 af: de haak is nut, een gezicht is een plus, geen eis.
2. **Het product is de verzameling van de gratis filmpjes, plus wat er niet in paste.** Kijkers kregen elke dag gratis een tip; wie alles bij elkaar wil, met extra stappen en zoekbaar, betaalt $52. Zijn reclamefilmpjes doen het slechter dan zijn tips (mediaan 10.000 tegen 16.000), dus de verkoop loopt via de naam en de link, niet via reclame in de feed.
3. **Elke dag, met een nummer, en op meer plekken tegelijk, jarenlang.** Zijn eerste 30 filmpjes hebben nu nog maar een mediaan van 4.500 views, na 8 jaar. De groei kwam na honderden tips. Elke tip ging ook als bericht naar BlenderNation, een gratis plek waar zijn kopers al kwamen. En hij verkocht al na ±7 maanden, met een half boek.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij begon in 2018, vlak voor Blender 2.8 (2019), toen heel veel nieuwe gebruikers instroomden en er nog bijna geen korte Blender-tips waren. Nu zijn er veel meer. Dat speelt mee, en is niet te meten.
- Hij is een ervaren Blender-professional die zelf elke dag iets nieuws leert en laat zien. Onze tips moeten echt kloppen; Bram en Chris moeten elke tip zelf in Blender nadoen voor hij uitgaat.
- Zijn product is kennis (een boek), het onze is gereedschap (een add-on). Bij hem is de stap van filmpje naar product heel klein. Bij ons moet de tip vanzelf naar Click Joints leiden, dus tips over print-in-place en gewrichten, niet over alles in Blender.
- Views van nu zeggen weinig over views in de eerste weken. Hoe zijn kanaal er in 2018 en 2019 uitzag, kon ik niet zien (archive.org gaf geen antwoord). Verkoopcijfers per jaar zijn niet openbaar.
- Plaatsen op BlenderNation of andere sites doen wij niet zelf: dat is plaatsen op internet, dus dat doet Thijs. BlenderNation plaatst nog steeds tutorials van gebruikers (GEZIEN: in de rubriek Tutorials 8 nieuwe tussen 31 okt en 15 nov 2026, en Jan zelf nog op 20 jan en 3 mrt 2026), maar de regels voor insturen kon ik niet lezen: de pagina Submit News toont zonder JavaScript geen tekst. Thijs leest die dus eerst zelf.

### Voorstel voor Dortus deze week
**Maak van de tips-reeks voor Click Joints een genummerde reeks van één handeling per filmpje, zo kort als het kan (de eerste 10 onder 15 seconden), en houd bij elke tip een korte tekst met plaatje bij op dortus.com/click-joints/ (een tipspagina).** Voorbeelden: "Print-in-place tip #1: waarom een gewricht vastsmelt (te weinig speling)", "#2: zet het gewricht plat op het bed", "#3: hoe test je eerst één gewricht". Die tipspagina wordt na 20 tot 30 tips een gratis gids, en later kan de Pro-versie of een gids in de winkel daar op voortbouwen, zoals zijn e-book. **Wie:** Chris maakt de reeks (tekst in beeld, geen gezicht nodig), Bram doet elke tip echt na in Blender en levert het beeld. **Voor Thijs, op `organisatie/lijst-thijs.md` via de hoofdchat, geen haast:** de tips ook als bericht insturen bij BlenderNation (gratis, één keer per week, alleen tips en geen reclame), want dat deed Jan bij elke tip. Na 30 tips eerlijk kijken naar views en downloads, zoals besloten.

---

## 3. VAW.BE (Wim Van Aerschot, solo, Garmin-wijzerplaten): elke dag een kort filmpje, en de nummer 1 van de winkel

Onderzocht 16 nov 2026, run 3. Open vraag uit run 1 en 2: een kleine maker van een tool of Garmin-app die WEL groeide met korte filmpjes. Waarom dit verhaal: dit is precies ons terrein. Een solo maker uit België verkoopt Garmin-wijzerplaten van $1,99 tot $4,99 (Ebb kost $4,99), maakt sinds februari 2025 korte filmpjes op TikTok, Instagram en YouTube, en zijn betaalde wijzerplaat Goals stond eind oktober 2026 bovenaan de wijzerplatenlijst van de Connect IQ Store. Hij schrijft bij elk filmpje een stuk op zijn eigen site ("Garmin School", nu dag 167), dus de onderwerpen van zijn reeks zijn van dag 1 af te lezen.

### Bronnen
- Zijn site: Garmin School, de lijst van alle 167 dagen met onderwerp en aantal keer gelezen (curl): https://garmin.vaw.be/en/community . Losse dagen: dag 1 Stride https://garmin.vaw.be/en/community/day-1-stride-watchface , dag 3 Goals https://garmin.vaw.be/en/community/day-3-goals-watchface-apple-rings-for-garmin , dag 5 Laziest https://garmin.vaw.be/en/community/day-5-laziest-watchface-ever-created , dag 101 Goals Pro https://garmin.vaw.be/en/community/day-101-goals-pro-garmin-watchface , over hem https://garmin.vaw.be/en/about
- De openbare winkel-API van Garmin (dezelfde die Gijs gebruikt, zie `platformen/garmin/status.md`): al zijn 142 apps met downloads (in blokken), aantal reviews, prijs; en de datum van reviews, om te zien wanneer de groei kwam.
- the5krunner, 2 nov 2026, Goals bovenaan de wijzerplatenlijst van oktober (geopend in een browser zonder inloggen, curl gaf een Cloudflare-scherm): https://the5krunner.com/2026/11/02/goals-tops-garmins-watch-face-chart-for-october
- Tom's Guide, 13 aug 2025, een vaste Garmin-tester raadt Goals aan (curl): https://www.tomsguide.com/wellness/fitness-trackers/if-youre-moving-from-apple-to-garmin-youll-want-to-install-this-watch-face
- Garmin-forum, zijn eigen bericht over Goals III, ruim 3 jaar geleden (curl): https://forums.garmin.com/developer/connect-iq/f/showcase/315890/watchface-goals-iii
- Zijn kanalen, alleen de tellers: TikTok https://www.tiktok.com/@vaw.be (blok `__UNIVERSAL_DATA_FOR_REHYDRATION__`), Instagram https://www.instagram.com/vawbe/ (meta-omschrijving), YouTube https://www.youtube.com/@vawbe/shorts (views per Short staan in de pagina). Vier omslagen van Shorts bekeken (i.ytimg.com).
- Niet gelukt: archive.org (verbinding viel weg), dus ik weet niet hoe zijn kanalen er in 2025 uitzagen. Zijn eigen TikTok- en Instagram-lijst met filmpjes en views is niet leesbaar zonder verborgen API, dus views per filmpje heb ik alleen van YouTube, en alleen van de nieuwste 48.

### Cijfers
Kanalen (GEZIEN 16 nov 2026):
- TikTok @vaw.be: aangemaakt 9 feb 2025, 29.500 volgers, 251.500 likes, 301 filmpjes. Dat is ±3,4 filmpjes per week, 21 maanden lang.
- Instagram @vawbe: 31.000 volgers, 369 berichten. Zijn site verwijst overal naar Instagram ("link in my bio"), dus dat is zijn hoofdkanaal.
- YouTube @vawbe: 2.350 abonnees. De nieuwste 48 Shorts: meestal 750 tot 2.500 views. Uitschieters zijn geen productfilmpjes maar nieuws en vergelijkingen: "Coros Pace 4 Pro vs Garmin Forerunner 570/970" 39.000, "This is Garmin's new Marq 3" 19.000, "Is the Garmin Connect app terrible or awesome?" 18.000, "Your Garmin knows when your body is struggling" 13.000. Zijn eigen wijzerplaten: "This is the new Cockpit watchface" 3.200, "This is the new Cadence watchface" 2.500, "This is the Photo Time watchface" 751.
- **Vorm: hij praat zelf in de camera**, met een microfoontje in de hand, ondertitels groot in beeld, één woord gekleurd, thuis voor een kast met planten. Geen gezichtloze schermopname.

Winkel (GEZIEN 16 nov 2026, openbare API; downloads geeft Garmin alleen in blokken als "100.000+"):
- 142 apps van VAW.BE, waarvan 48 betaald, samen 196.155 reviews.
- Goals: $1,99, 100.000+ downloads, **32.206 reviews**, 4,9 sterren. Eerste review 4 apr 2025, dus twee maanden na zijn eerste TikTok. Sindsdien elke dag ±30 tot ±100 reviews (met pieken rond kerst 2025, ±99 per dag, en in juli 2025, ±86 per dag), nu ±40 per dag.
- Goals Pro: $4,99, 10.000+ downloads, 903 reviews. Gratis "Seasons": 500.000+ downloads, 55.458 reviews (sinds dec 2023). "The Laziest Watchface Ever Created" (gratis, met AI-agents gebouwd): eerste review 6 feb 2026, nu 50.000+ downloads en 2.982 reviews.
- Daily Sea Creature, een betaalde wijzerplaat met zeedieren voor $4,99, net als Ebb: 100+ downloads, 40 reviews. Niet elk onderwerp loopt, ook niet bij hem.
- Werkwijze in de winkel: bijna elke betaalde wijzerplaat staat er twee of drie keer: betaald, "with trial" (gratis proberen), en "with trial & kpay" (betalen via een andere dienst). Goals betaald heeft 32.206 reviews, Goals "with trial" 8.423.

Groei voor en na de filmpjes (GEZIEN: reviewdata van zijn 12 apps met de meeste reviews, samen 167.789; ik telde per periode hoeveel reviews er bijkwamen):
- 16 nov 2024 tot 9 feb 2025 (voor zijn eerste TikTok): 9.020 reviews in 85 dagen, ±106 per dag (met kerst erin).
- 9 feb 2025 tot 16 nov 2025: 50.392 in 280 dagen, ±180 per dag.
- 16 nov 2025 tot 15 nov 2026: 74.991 in 364 dagen, ±206 per dag.
- Dus na de start van de filmpjes ±1,7 tot 2 keer zoveel reviews per dag. Maar: Goals kwam er in april 2025 bij, er komen elk jaar meer Garmin-horloges, en Tom's Guide schreef in aug 2025 over Goals. Hoeveel van de groei door de filmpjes komt, is met deze cijfers NIET te scheiden.
- Omzet: niet openbaar. GOK, heel grof: als de helft van de 100.000+ downloads van Goals betaald is, is dat ±$100.000 bruto vóór de afdracht aan Garmin, verspreid over 19 maanden. Dat de betaalde versie meer reviews heeft dan de proefversie, wijst erop dat veel mensen echt kopen, maar het blijft een gok.

### Wat hij deed, in volgorde
1. **Jaren eerst gewoon bouwen.** Op het Garmin-forum staat Goals III al "over 3 years ago"; Goals V heeft reviews sinds jan 2023, Seasons sinds dec 2023. In nov 2024 had hij al ±33.000 reviews in zijn top 12. De filmpjes kwamen dus bovenop een winkel die al liep.
2. **Feb 2025: TikTok, Instagram en YouTube, zijn eigen gezicht.** ±3 tot 4 filmpjes per week. In april 2025 kwam Goals ("Apple Watch rings, maar voor Garmin"): een idee dat hij uit reacties haalde ("This is the most common thing I hear from people who switch to Garmin").
3. **Kijkers laten meedoen.** Kijkers delen hun kleurencombinatie voor Goals in de reacties onder zijn Instagram-filmpjes, "the best ones get featured" (dag 3). Een openbaar ideeënbord: kijkers stemmen wat hij bouwt (dag 47, dag 53, dag 115), en hij maakt filmpjes over wijzerplaten die volgers vroegen ("One of my followers quit smoking...", "I created the Photo Time watchface based on Ward's idea", "Can I build your Garmin watchface?").
4. **Feb 2026: een vaste reeks, "100-Day Garmin School".** Dag 1: "I made this Garmin watchface because my doctor told me I was going to die." Elke dag een filmpje en een stuk op zijn site met een nieuwsbrief. Na dag 100 ging hij door (nu dag 167).
5. **De onderwerpen verschoven van eigen product naar vragen van alle Garmin-bezitters.** Dag 1 tot 5: alle vijf zijn eigen wijzerplaten (Stride, Daily Flowers, Goals, Hearts, Laziest). Dag 1 tot 30: ±9 van de 30 over zijn eigen apps, de rest tips (batterij, hartslagalarm, VO2max, "Why Garmin doesn't default to 10,000 steps"). Dag 31 tot 167: nog ±1 op 8 over eigen apps, de rest tips, vergelijkingen (Garmin tegen Apple Watch en Coros), nieuws (nieuwe horloges) en "Garmin met Claude". Op zijn site zijn de stukken over Claude en Garmin het meest gelezen (dag 43 vergelijkingstool 6.948 keer, dag 62 slaapscore met Claude 3.562, "Connect your Garmin to Claude" 3.189 en 3.118).
6. **Elk filmpje wijst naar één plek**: de link in zijn Instagram-bio, waar al zijn apps, een bundel ("save up to 90%") en de nieuwsbrief staan.

### Drie lessen
1. **Bouw het kanaal rond de vragen van de bezitters, niet rond je product.** Zijn best bekeken Shorts zijn vergelijkingen en nieuws (13.000 tot 39.000), zijn productfilmpjes halen 750 tot 3.200. Na de eerste vijf dagen ging nog maar 1 op de 3 en later 1 op de 8 filmpjes over zijn eigen apps. De tips brengen volgers; de wijzerplaten liften mee via de bio. Bij VibeDesk (verhaal 2) ging elk filmpje over het product, en dat bleef steken op 39 tot 363 views.
2. **Een echt persoon met een eigen verhaal is de haak.** Hij praat zelf, met een eerlijke reden ("my doctor told me I was going to die" bij Stride, "I always forget Valentine's Day" bij Hearts). Dit is het eerste verhaal in onze reeks met tienduizenden volgers via eigen korte filmpjes, en het is geen gezichtloos kanaal. Twee verhalen is weinig, maar het past: gezichtloos en alleen product (VibeDesk) bleef plat, gezicht en tips (VAW.BE) groeide. GOK: voor Garmin en Blender geldt hetzelfde.
3. **Lang volhouden en kijkers laten kiezen.** 301 filmpjes in 21 maanden, en de groei in reviews kwam geleidelijk (±106 naar ±206 per dag), niet in één klap. Wat er wel in één klap kwam, waren ideeën die hij uit de reacties haalde: Goals (ringen zoals Apple) werd zijn grootste betaalde product. Het ideeënbord en "jouw kleuren worden uitgelicht" maken van kijkers meedenkers.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij had al jaren een lopende winkel (±33.000 reviews vóór zijn eerste filmpje) en 100+ apps. Wij hebben Ebb met 0 downloads. Zijn filmpjes konden naar een hele etalage wijzen; de onze naar één of twee producten.
- Hij is een echte Garmin-gebruiker die test en zelf praat. Wij mogen geen AI-gezicht of nep-persoon gebruiken (besluit 15 nov 22:53), en terecht. Zijn vorm is dus alleen na te doen als Thijs zelf in beeld wil, of met een eigen stem zonder gezicht. Dat beslist Thijs, niet wij.
- Wat de filmpjes precies opleverden, kan ik niet scheiden van Goals, Tom's Guide en de groei van Garmin zelf. Zijn eigen "top 5 wijzerplaten van 2026" (dag 79) zet twee van zijn eigen apps erin (Laziest op 2, Titan op 4); dat is reclame, geen onafhankelijke lijst.
- Zijn eerste 30 filmpjes op TikTok (feb tot ±apr 2025) heb ik niet kunnen zien. Wat ik heb, zijn de eerste 30 dagen van zijn tweede start, de Garmin School van feb 2026.

### Voorstel voor Dortus deze week
**Draai de verhouding in het filmplan om: 4 van de 5 filmpjes beantwoorden een vraag die elke Blender-gebruiker (of Garmin-bezitter) heeft, 1 van de 5 laat ons product zien, en geef de reeks een vaste naam met een dagnummer.** Voor Click Joints bijvoorbeeld "Print-in-place in Blender, day 1": hoeveel speling een gewricht nodig heeft, waarom een print vastsmelt, welke laaghoogte, hoe je een figuur zo zet dat hij zonder steun print. Click Joints komt dan vanzelf in beeld als het gereedschap, en het onderschrift wijst naar dortus.com/click-joints/. Voor Ebb later hetzelfde met korte Garmin-tips (ademhaling, Body Battery, stress), zonder gezondheidsclaims. **Wie:** Chris schrijft de 10 eerste onderwerpen in `commercie/filmpjes/` en maakt ze met de opnames van Bram; Bram levert per tip een kort, echt Blender-beeld. **Eén vraag voor de hoofdchat aan Thijs** (geen haast, past in de groeironde): wil hij af en toe zelf 20 seconden praten (gezicht, of alleen zijn stem over de beelden)? Dit verhaal is het enige in onze reeks waarin korte filmpjes echt volgers gaven, en daar praat de maker zelf. Zegt hij nee, dan gaan we gezichtloos verder met de tips-verhouding, en kijken we na 20 tot 30 filmpjes eerlijk naar views en downloads, zoals besloten.

---

## 2. VibeDesk (Fred, solo, gratis Windows-app voor Claude Code): 20 Shorts zonder gezicht, met cijfers

Onderzocht 16 nov 2026, run 2. Open vraag uit run 1: wat deed een maker in zijn eerste 30 filmpjes, met kijkcijfers per filmpje? Waarom dit verhaal: een solo maker die precies doet wat Chris vanaf di 17 nov gaat doen (staande schermopnames, tekst in beeld, geen gezicht, geen stem) en zijn echte cijfers uit YouTube Studio en GitHub openbaar zet. Hij bouwt ook met Claude Code, net als wij. Het is geen succesverhaal maar een eerlijke mislukking, en daarom juist bruikbaar: zo ziet de start eruit als het niet vanzelf gaat.

### Bronnen
- Zijn eigen verslag op DEV, 3 nov 2026 (curl via de openbare API van DEV): https://dev.to/fxdgif/15-youtube-shorts-2674-views-1-subscriber-promoting-a-dev-tool-without-showing-my-face-2m8j
- Zijn eerste bericht over de app, 22 okt 2026, met 17 reacties (curl, API van DEV): https://dev.to/fxdgif/i-kept-missing-claude-codes-permission-prompts-so-i-built-a-desktop-around-it-8fc
- Zijn kanaal, tab Shorts en tab Video's (curl, de cijfers staan in de pagina zelf): https://www.youtube.com/@vibedesk-lounge/shorts
- De repo, sterren via de zoek-API van GitHub (gh api search): https://github.com/fxd-gif/vibedesk
- Ter vergelijking: de zoekpagina van YouTube voor "print in place joints blender" en "articulated print in place blender tutorial" (curl, 16 nov).
- Niet gelukt: de GitHub-pagina zelf (403 vanuit de cloud) en de afspeelpagina van YouTube (429). Kijkduur per filmpje en precieze plaatsingsdata heb ik dus alleen uit zijn eigen verslag.

### Cijfers
Uit zijn verslag (EIGEN OPGAVE, uit YouTube Studio, laatste 28 dagen tot 3 nov):
- 15 Shorts in twee weken: samen 2.674 views, 32 likes, **1 abonnee** uit Shorts.
- 70% veegde vrijwel meteen weg. Snelle, flitsende filmpjes: 19% tot 25% bleef kijken. Het beste filmpje (26 seconden, "sort my windows" typen en het zien gebeuren, geen effecten): 42% bleef.
- Elke Short kwam tussen 50 en 370 views. YouTube Studio zegt zelf: "usually get 140 to 220". 81% van de views kwam uit de Shorts-feed.
- GitHub: 21 unieke bezoekers in 14 dagen, waarvan 5 via YouTube. 0 sterren.
- Eén langer filmpje van 1:15 (gewone video, geen Short): 332 views, gemiddeld 51% bekeken, 80% van de views via de startpagina van YouTube, ook 1 abonnee.
- Eén eerlijk bericht op DEV ("I kept missing...") gaf 15 reacties en twee wensen die hij in de volgende versie bouwde.

Zelf nagekeken (GEZIEN 16 nov 2026):
- Kanaal: 20 Shorts en 2 gewone video's, 136 abonnees. Views per Short, nieuwste eerst: 97, 53, 39, 153, 84, 79, 55, 215, 151, 134, 363, 157, 196, 194, 284, 201, 245, 274, 72, 54. Samen 3.100. Hoogste 363 ("How much Claude Code did this project use today?"), laagste 39.
- De 7 Shorts van na zijn verslag halen samen 560 views (gemiddeld 80), lager dan de 13 oudere (gemiddeld ±195). Of dat komt door minder vaak plaatsen of door het onderwerp, weet ik niet.
- De gewone video's: "I vibecoded the Claude Code workspace I wished I had, in 12 days" 370 views; "VibeDesk in 5 minutes" 81 views.
- Repo: 0 sterren, 1 fork, aangemaakt 11 okt 2026.
- DEV: het eerste bericht heeft nu 17 reacties; zijn negen berichten daarna hebben 0 tot 2 reacties elk.
- Klopt niet helemaal: hij schrijft "+1 subscriber from Shorts", het kanaal heeft er nu 136. Waar de rest vandaan komt staat er niet; GOK: via zijn DEV-berichten en de link op zijn site, of later erbij gekomen.

Ter vergelijking, YouTube-zoekpagina (GEZIEN 16 nov): lange uitlegvideo's over beweegbare prints in Blender halen 38.000 tot 143.000 views ("Articulated Dragon 3d print // Blender tutorial" 142.783, "How To Design Articulating 3D Prints! Blender Tutorial!" 48.548, "How to Make Your Own Flexi STL Files (Free FlexiMaker Tutorial Using Blender)" 38.163). Maar twee nieuwe kleine kanalen met dezelfde soort uitleg halen 38 en 270 views. Lang is dus geen garantie, wel een kamer waar mensen met de vraag zitten.

### Wat hij deed, in volgorde
1. **Eerst een eerlijk bericht** op DEV met het probleem in één zin ("I kept missing Claude Code's permission prompts") en een filmpje erin. Reacties van mensen met hetzelfde probleem; hij antwoordde iedereen uitgebreid, opende issues voor hun wensen en bouwde ze in versie 2.0.
2. **Daarna 15 Shorts in twee weken**: eerst snel en flitsend, toen rustig met één idee per filmpje en een grote uitsnede van de app. Het aantal views veranderde niet.
3. **Opgeschreven en bijgestuurd**: hoogstens twee Shorts per week, langere rustige video's die iets beantwoorden waar mensen op zoeken, meer eerlijke berichten, en een kortere weg naar de download (de installer is niet ondertekend, dus Windows waarschuwt).
4. Daarna nog 5 Shorts; die deden het slechter.

### Drie lessen
1. **Bij een nichetool zonder gezicht bepaalt het filmpje de views nauwelijks.** Snel, traag, grappig of technisch: alles landde tussen 50 en 370. De feed laat een kleine testgroep kijken; vegen ze weg, dan stopt het. Wat wel verschil gaf in hoe lang mensen bleven: **één duidelijke handeling die je zelf zou willen** ("sort my windows", 42%), geen effecten. Dat sluit aan op McGybeer (verhaal 1): het product dat het werk doet in beeld, niet de knoppen.
2. **De Shorts-feed is een kamer vol mensen zonder jouw probleem.** Uit 3.000 views kwamen 5 bezoekers op de repo. In een Short kun je niet klikken. Een gewone, langere video kwam via de startpagina bij mensen die zulke video's kijken, en een eerlijk bericht kwam bij mensen met het probleem; die gaven allebei meer dan alle Shorts samen.
3. **Meet tot aan de download, niet tot aan de view.** Zijn eigen conclusie: uren in montage, bijna niets in de weg na de klik (releasepagina, .exe, waarschuwing van Windows). Views zonder downloads zeggen niets.

### Eerlijk: wat niet zomaar voor ons geldt
- Eén kanaal, één tool, vier weken, alleen YouTube. Geen TikTok en geen Reels. Op TikTok is het bereik voor nieuwe accounts mogelijk anders (GOK, niet gemeten).
- Zijn publiek (Windows-gebruikers van Claude Code) is kleiner en zijn drempel hoger (onondertekende .exe) dan bij Click Joints, dat je in Blender met één klik installeert van extensions.blender.org. Ons beeld (een figuur die buigt) is ook makkelijker te begrijpen dan een bureaublad met terminals. Onze Shorts kunnen dus beter doen (GOK).
- Hij schrijft zelf: "Maybe my hooks were just bad." Het kan aan zijn filmpjes liggen.
- Verwachting voor Chris, als GOK op basis van dit verhaal: de eerste Shorts halen 50 tot 400 views per stuk en leveren een handvol downloads. Dat is normaal en geen reden om na een week te stoppen; het besluit van 15 nov kijkt terecht pas na 20 tot 30 filmpjes.

### Voorstel voor Dortus deze week
**Naast de dagelijkse Shorts één gewone liggende YouTube-video (60 tot 120 seconden) die een zoekvraag beantwoordt**, titel in de vorm "How to make print-in-place joints in Blender (free add-on)": één figuur van begin tot geprint resultaat, rustig, tekst in beeld, geen gezicht, geen stem. Bij VibeDesk haalde zo'n video evenveel abonnees als alle Shorts samen en kwam hij via de startpagina bij het juiste publiek; in onze niche halen zulke uitlegvideo's bij gevestigde kanalen tienduizenden views. Kost weinig: Bram heeft de filmpijplijn al en de bestaande winkelplaatjes zijn liggend (1920 x 1080); of de film zelf liggend is, heb ik niet nagekeken. **Wie:** Chris maakt hem in week 1 of 2, Bram levert liggende opnames als die ontbreken, Thijs plaatst. **En meten:** Chris zet in zijn dagmeting per filmpje de views naast de downloads van Click Joints op extensions.blender.org (dagteller), zodat we na 20 tot 30 filmpjes zien of views downloads worden, niet alleen of de views stijgen.

---

## 1. McGybeer (Javier Rodríguez, solo, beweegbare 3D-print-figuren)

Onderzocht 15 nov 2026, run 1. Vraag van de hoofdchat: hoe groeiden kleine makers met korte filmpjes zonder gezicht? Waarom dit verhaal: dit is precies de hoek van Click Joints (beweegbare figuren die je in één keer print, ontworpen in Blender), en het is het bekendste voorbeeld van een 3D-ontwerp dat via TikTok groot werd.

### Bronnen
- Interview Snapmaker, 24 feb 2022 (curl): https://www.snapmaker.com/blog/3d-printed-articulated-dragon-model-designer-javier-rodriguez/
- Artikel 3DWithUs over beweegbare draken, 27 apr 2022, bijgewerkt 5 nov 2023 (curl): https://3dwithus.com/articulated-dragon-models-flexible-print-in-place-for-3d-printing
- Productpagina en profiel op Thangs (curl, cijfers uit de pagina zelf): https://thangs.com/designer/McGybeer/3d-model/Articulated%20Dragon-863344
- Zijn TikTok-profiel (curl, alleen de tellers bovenaan): https://www.tiktok.com/@mcgybeer
- Niet te lezen vanuit de cloud: Cults3D, Printables, Thingiverse, Patreon (403), 3dprint.com (Cloudflare), zijn eigen site mcgybeer.xyz (onbereikbaar). De lijst met zijn eigen TikTok-filmpjes heb ik niet kunnen ophalen: dat gaat alleen via een verborgen API of een browser die de pagina naspeelt, en dat doen we niet. Wat hij in zijn eerste 30 filmpjes deed, weet ik dus NIET.

### Cijfers
- Zijn eerste bekende ontwerp: Cute Mini Octopus (2019), gemaakt voor zijn roller-derbyteam (DERDEN, Snapmaker).
- De Articulated Dragon: "40K paid downloads" met "thousands of physical models sold across Etsy, eBay, Amazon" (DERDEN, 3DWithUs, stand ±2022 tot 2023, niet nagekeken).
- Eén filmpje van Snapmaker over de draak op Facebook (dec 2021): 15 miljoen views en 8.600 reacties, "the most popular case in the Snapmaker community ever" (DERDEN, Snapmaker).
- TikTok-account @mcgybeer aangemaakt op 17 dec 2020 (GEZIEN, tijdstip in de pagina). Nu: 43.263 volgers, 336.225 likes, 187 filmpjes (GEZIEN 15 nov 2026). Gemiddeld ±1.800 likes per filmpje (GOK, gewoon gedeeld).
- Thangs (GEZIEN 15 nov 2026): draak los $3,99, 396 downloads, 208.019 keer bekeken, 493 likes; profiel 70 modellen, 29.491 downloads, 3.536 volgers. Leden: $10 per maand (4 ontwerpen), $18 (8 ontwerpen), en drie **verkooplicenties**: $10, $18 en $60 per maand (de laatste met alles, onbeperkt).
- Omzet: niet openbaar. GOK: 40.000 x ±$4 tot $8 is $160k tot $320k bruto alleen voor de draak, maar de prijs per winkel en het aandeel dat via leden liep weet ik niet.

### Wat er gebeurde, in volgorde
1. **Eerst het mechaniek, dan het dier.** Hij wilde de draak al een jaar eerder maken, maar "my design skills were still not enough". Hij ontwierp eerst een nieuw soort gewricht, maakte "a bunch of prototypes", testte en paste aan, en pas daarna modelleerde hij de draak in Blender. Gewrichten eerst, "as they are the key and the rest of the model depends on them".
2. **Het ontwerp verspreidde zich via filmpjes van anderen.** "Its popularity grew mainly on TikTok and I didn't have an account back then." Printerbezitters en een printermerk (Snapmaker) filmden de draak die in de hand kronkelt; dat deed het werk. Zijn eigen account kwam pas daarna (dec 2020).
3. **Hij maakte er werk van verkopers.** Mensen die de draak printen en verkopen (Etsy, eBay, Amazon, markten) kopen een verkooplicentie. Elke verkoper die zijn print filmt om hem te verkopen, maakt zo reclame voor het ontwerp.
4. **Daarna een reeks in dezelfde vorm.** Cali-Dragon, hagedis, haai, ratelslang: steeds een beweegbaar dier dat je zonder steun print. Na de draak werd hij voltijds ontwerper, omdat hij "2-3 hours per day just responding to emails, messages, posts" kwijt was.

### Drie lessen
1. **Het filmpje dat werkt is het product dat beweegt in een hand, niet uitleg.** Het groeimoment kwam niet van zijn eigen filmpjes maar van anderen die het resultaat lieten kronkelen. Voor een product als Click Joints is het sterkste beeld dus de geprinte figuur die buigt, niet het Blender-paneel.
2. **Laat anderen filmen: geef ze een reden.** Een printermerk wil indrukwekkende prints laten zien, een verkoper wil zijn waar verkopen, een hobbyist wil laten zien wat hij maakte. McGybeer verdient aan die groep met een verkooplicentie. Voor ons: makers die met Click Joints iets printen, zijn het kanaal, niet ons eigen account alleen.
3. **Eerst een nieuw mechaniek dat je in één beeld ziet.** De draak was "the first highly detailed articulated design" (volgens hemzelf); het verschil was in twee seconden te zien. Een filmpje zonder gezicht werkt als het onderwerp zelf de haak is.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij verkoopt **printbestanden** (iedereen kan het eindresultaat begrijpen). Wij verkopen een **Blender-add-on**: het publiek dat het eindresultaat leuk vindt is veel groter dan het publiek dat de add-on kan gebruiken. Een viraal filmpje van een kronkelende figuur levert ons dus minder kopers op dan hem (GOK).
- Het is één uitschieter uit 2020 tot 2021, toen beweegbare draken nieuw waren. Nu zijn er "lots of similar Dragon variations around"; het moment is voorbij.
- Over zijn eigen eerste 30 filmpjes heb ik niets kunnen vinden. Dat deel van de vraag blijft open.

### Voorstel voor Dortus deze week
**Een filmpje van een echt geprinte Click Joints-figuur die in een hand buigt** (8 tot 12 seconden, eerste seconde al bewegen, geen gezicht), als filmpje 6 in de reeks van Chris, en vanaf de lancering van Pro bij elke nieuwe figuur. Wie: Chris, met de print die al op de lijst van Thijs staat (echte print van een gewricht, alleen als hij of iemand die hij kent een printer heeft). Is er geen printer, dan vraagt Chris bij de lancering op r/3Dprinting of iemand een print wil laten zien, met credits (Thijs plaatst). Tot er een echte print is: Bram rendert een "hand"-beeld waarin de figuur buigt, eerlijk vermeld als render. En op de Pro-pagina een regel "Made something with Click Joints? Tag us, we share the best ones", zodat makers een reden hebben om zelf te filmen.

### Voor de ploeg: wat ik leerde over meten
Het openbare TikTok-profiel geeft met curl wel de tellers (volgers, likes, aantal filmpjes, aanmaakdatum) in het blok `__UNIVERSAL_DATA_FOR_REHYDRATION__`, maar niet de lijst met filmpjes. Handig om na de start van onze accounts elke dag volgers en likes te meten.
