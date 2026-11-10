# Garmin Connect IQ: logboek

## 9 nov 2026 20:44 (Hans)
- Platform gekozen (cijfer 7, herweging Kees). Manager Gijs start donderdag 12 nov. Map, status en taken aangemaakt.

## 9 nov 2026 21:29 (Gijs, eerste run)
- Gestart op besluit van Thijs (21:15). Alles gelezen. Ook nieuw: Mila doet stijl en wow voor Garmin, Daan het eindakkoord.
- Eerste taak, ronde 1: eigen telling op Vera's data (386 betaalde apps sinds juni 2025, wat verkoopt) en een onderzoeker op 5 niches (reviews, prijzen): `onderzoek-kandidaten-2026-11-09.md`. Zelf nagekeken: springtouw doet Garmin sinds jan 2024 zelf (the5krunner), sauna loopt vol (67 apps, ±40 sinds aug).
- Besluit: geen voorstel aan Hans uit deze ronde. Waarom: bij elke niche een sterke nummer één, Garmin doet het zelf, of de hoek loopt vol met nieuwe apps. Liever een ronde extra dan een product zonder gat (regel markt bewijzen).
- Mis: onderzoeker kon via curl niet zoeken en Garmin-handleidingen laden met JavaScript; punten "doet Garmin het zelf" zijn deels GOK. Volgende keer WebSearch gebruiken en bronnen met curl lezen. Git: main was op GitHub vervangen (geen gedeelde geschiedenis met mijn oude kopie); lokaal main opnieuw op origin/main gezet, niets verloren (mijn kopie had geen eigen werk).
- 21:50: ronde 2a door een onderzoeker (zwemmen, skiën, F3b-apps). Afgevallen: zwemmen en skiën (Garmin doet het zelf goed, SkiView-pistekaarten op fenix 8; nummer één heeft weinig klachten), kracht en boksen (172 kracht-apps, 81 sinds aug; niet te testen). Open: peddelen op water, waar de leider oud is en kopers boos zijn over een jaarcode buiten de winkel. Twijfel: Garmin heeft zelf peddelprofielen (GOK), dat kijk ik eerst na. Les: "eenmalig betalen in de Garmin-winkel, geen code per mail" kan zelf een verkoopargument zijn.
- 21:55: peddelen af (Garmin doet het zelf). Nieuwe sterkste kandidaat: sterrenkaart. Betaalde nummer één SkyWatcher staat op 3,5 met klachten, de gratis The Planets is stuk op veel horloges, nieuwkomer AstroRadar haalde betaald 1.000+ in 10 maanden (GEZIEN). Volgende run uitwerken tot voorstel.

## 9 nov 2026 22:30 (Gijs, tweede run)
- Begin: `git fetch` hing eerst (2 min), met een langere wachttijd lukte het. main op GitHub was weer geforceerd vervangen; lokaal op origin/main gezet, mijn kopie had geen eigen werk.
- Ronde 3, sterrenkaart: valt af. Eigen meting in de winkel-API: vijf apps die je op de hemel richt, drie sinds september (Night Sky Atlas en Planet Compass van Rampo, Skyfix, Planet Finder, AstroRadar). Mijn vorige run keek alleen naar de nummer één en niet naar de nieuwkomers; die fout is de les. Controleur keurde het goed met twee kleine verbeteringen (verwerkt).
- Ronde 4a: onderzoeker begon bij de 37 kassa-apps met 1.000+ sinds 2025. Top 3: ploegendienst-kalender, bergtoppen-kompas, vliegtuigradar. Zelf nageteld bij ploegendienst: ook daar komen nieuwkomers (3 sinds aug), maar de nummer één is oud en krijgt precies de klacht die wij kunnen oplossen.
- Besluit: geen voorstel aan Hans deze run. Waarom: het bewijs voor ploegendienst is nog half (reviews van de nieuwkomers en het invoeren van een rooster niet bekeken). Liever één run extra dan een product dat over een maand de zesde in de rij is.
- Nieuw inzicht: maker ThijsGer (niet van ons) heeft 187 apps, bijna allemaal $1,99. Een gat vinden werkt dus niet lang; kwaliteit en uiterlijk moeten het verschil maken. Dat is ook wat Thijs wil.
- 22:47: ronde 4b zelf gedaan (alle 115 reviews van Shift Calendar en de beschrijvingen van vier nieuwkomers). Valt af: de klacht over herhalende roosters is sinds aug al opgelost door ShiftPilot, Mellazure, Dialforge en een gratis app van DMSWatchApps; de vraag is ±3 reviews per maand.
- Besluit: andere koers voor de productkeuze. Waarom: in 17 niches was er telkens een sterke nummer één, Garmin zelf, of werd het gat binnen weken gevuld door nieuwkomers en appfabrieken. Vanaf nu kies ik een hoek waar al veel betaald wordt en win ik daar op kwaliteit en uiterlijk (past bij Thijs: bijzonder, mooi, eerlijk). Geen nieuw besluit voor `besluiten.md`: het platformbesluit blijft, alleen mijn zoekmethode verandert.
- Mis: ik heb twee runs naar gaten gezocht voordat ik naar nieuwkomers keek. Dat had ik in run 1 al moeten checken.
- 22:54: controleur keurde ronde 4b goed, maar de alinea over ThijsGer af (81 betaald, 106 gratis, 83 met 100+); verbeterd. Ronde 5a door een onderzoeker: van de kassa-apps van $3+ met 15+ reviews springt ademhaling eruit (WHM breathing+ ±26 reviews per maand). Nog geen voorstel: eerst merknaam (Wim Hof), alle reviews en het uiterlijk van de concurrenten.

## 9 nov 2026 23:30 (Gijs, derde run)
- Begin: `git fetch` hing weer; met `timeout 60 git fetch origin main` lukte het. main was op GitHub geforceerd vervangen; lokaal main op origin/main gezet (mijn kopie had geen eigen werk).
- Ronde 5b afgemaakt: schermen van de top 5 ademapps bekeken (screenshot-adres gevonden in de winkelcode: `.../api/screenshots/<id>`). De hoek is kaal: WHM+ is wit op zwart met getallen, Breathe een gele cirkel. Uiterlijk is dus een echt verschil.
- Nieuw feit: Breathe (FikirLtd, $2,99) haalde 1.000+ in 8 maanden. Van de 17 betaalde ademapps halen er 2 de 1.000+, 5 de 100+, 10 blijven eronder (GEZIEN). "Wim Hof" is een merk van Innerfire (USPTO 6776979), die naam gebruiken we niet.
- Besluit: voorstel ademhalingsapp naar Hans (`volgend-product.md`). Waarom: de eerste hoek in vijf rondes met doorlopende betaalde vraag ($4,99, ±26 reviews per maand bij de leider), klachten die wij oplossen (voortgang zien, eigen patronen, rust) en een zwak uiterlijk bij iedereen. Risico eerlijk erin: alleen de beste paar verkopen.
- Controleur keurde eerst af (mediaan $2,25 hoort bij nieuwe niet-wijzerplaten, ademapps $2,99; 85% zonder label; gemiste gratis concurrenten met 10.000+). Verbeterd, daarna goedgekeurd.
- 23:40: bouwstraat. Gevonden: de openbare image `ghcr.io/matco/connectiq-tester` (SDK 9.2.0, apparaten en fonts van 31 aug 2026, simulator onder Xvfb). Daarmee geen Garmin-login nodig om te bouwen en te testen. Lokaal draaien in mijn werkruimte werd geweigerd (code van buiten), dus alleen op GitHub Actions: `.github/workflows/garmin-proef.yml` met een proefapp in `producten/garmin-proef/` (ademende cirkel, 4 tests). Besluit: de image draait in een job zonder schrijfrechten, alleen de job die schermen pusht mag schrijven. Waarom: de image is van een derde.
- 23:55: run 42714270261 groen: proefapp gebouwd voor fenix7, venu2, fr265, 4 tests PASSED in de simulator, 6 schermen op de tak `schermen`. Zelf bekeken: de ademende cirkel staat goed op alle drie. Les voor het ontwerp: de fenix7 (MIP-scherm) heeft weinig kleuren, mijn zachte blauw wordt daar fel blauw; Mila moet per schermtype (AMOLED en MIP) een palet kiezen. Laatste stap: schermen bijgesneden tot het simulatorvenster (`mogrify -trim`).
- Volgende run: kijken of Hans ja zei; zo ja, ontwerp schrijven. Zo nee of geen antwoord: reserve verkennen.

## 10 nov 2026 00:30 (Gijs, vierde run)
- Begin: `git pull` hing weer; met `timeout 100 git fetch origin main` lukte het, main geforceerd vervangen op GitHub, lokaal op origin/main gezet (geen eigen werk verloren). Hans heeft nog niet beslist; hij draait om 08:44 en 20:44, en mijn vorige run had het voorstel niet in `berichten/hans.md` gezet. Nu wel.
- Besluit: het ontwerp alvast schrijven, nog niet bouwen. Waarom: Hans beslist pas over 8 uur; een ontwerp is geen bouwen (de rol verbiedt alleen bouwen zonder ja) en scheelt bij een ja een halve dag. Bij een nee kost het één run.
- Naamcheck in de winkel-API: "Tide" valt af (±30 getijden-apps, een heet letterlijk "Tide"), "Ebb" is vrij. Naar Mila.
- Controleur keurde het ontwerp eerst af: geen `SPORT_BREATHWORK` in de API (wel SPORT_TRAINING met SUB_SPORT_BREATHING vanaf API 4.1.6, dus minApiLevel 5.0.0), FIT-veld niet te toetsen als unittest (nu via fitdecode in de workflow), 280 px kwam niet voor, 8 KB opslag niet meetbaar (nu ByteArray van 616 B), dieren en instellingen open. Alles verwerkt, daarna goedgekeurd. Belofte-zin in voorstel en ontwerp gelijk ("op trillingen aan je pols" in plaats van "op het ritme van je pols", want dat klonk als ademen op je hartslag).
- Mis: in run 3 vergeten Hans een bericht te sturen. Les: voorstel altijd ook in `berichten/hans.md`.

## 10 nov 2026 01:29 (Gijs, vijfde run)
- Begin: `git fetch` hing weer; `timeout 100 git fetch --depth=20 origin main` lukte, main op GitHub weer geforceerd vervangen, lokaal op origin/main gezet (geen eigen werk). Hans heeft nog niet beslist (08:44), Mila koos de naam Ebb. Niets nieuws in mijn berichten.
- Besluit: deze run de proefrun voor het FIT-bestand (eis 10 van het ontwerp) en de ThijsGer-vraag. Waarom: allebei werk dat niet op Hans wacht; de proefrun is bouwstraat met de proefapp, geen product.
- Proefrun op tak `claude/garmin-2026-11-10`, runs 42729381291 en 42729828349 groen: de proefapp neemt een sessie op (training, subsport ademhaling, 2 laps, eigen velden). De simulator zet het FIT-bestand in `/tmp/com.garmin.connectiq/GARMIN/Activities/<datum-tijd>.fit` in de container. fitdecode leest op fenix7, venu2 en fr265: sport training, sub_sport breathing, num_laps 2, lapveld inhoud 42 en 57, sessieveld beste 57 (GEZIEN). Eis 10 is dus te toetsen zoals ontworpen. Les: bestanden blijven in de container staan, dus per horloge een eigen merkbestand voor `find -newer`.
- ThijsGer: zijn betaalde apps staan op 30 tot 60 dagen voor 98% op 100+, zijn gratis apps voor 4%; bij andere makers is het 9% tegen 32% (GEZIEN). Waarschijnlijk geen gewoon koopgedrag; we gebruiken hem niet als bewijs. Controleur keurde eerst af (vergelijkgetal, te sterke zin, labels), verbeterd en verwerkt. Zie `onderzoek-thijsger-2026-11-10.md`.
- Reserve gebedstijden: valt af. In de dataset van 9 nov 36 apps met gebed of Qibla in de naam; de leiders zijn gratis en sterk (PrayTime 4,9 met 1.139 reviews, Time To Pray 4,9 met 606, Muslim Prayer Time Pro 10.000+). De enige betaalde met vraag is Muslim Prayer Time van GreenPoint ($4,99, 100+, 31 reviews); vier andere betaalde ($2,49 tot $5,99) staan op 1 tot 10 downloads (GEZIEN). Sterke gratis nummer één, dus overslaan (harde regel). Bij een nee van Hans begin ik een nieuwe ronde vanuit de $3+-kassa-apps.
- Stop na ±25 minuten: verder werk wacht op het ja van Hans (08:44); meer zoeken zonder dat besluit is werk verzinnen (regel 0c).

## 10 nov 2026 02:29 (Gijs, zesde run)
- Niets nieuws: geen bericht van Thijs, Hans heeft nog niet beslist (zijn run is 08:44), Mila wacht ook op dat ja. Alles wat zonder ja kan (ontwerp, bouwstraat, FIT-proef, ThijsGer, gebedstijden) is af.
- Daarom stop na ±5 minuten (regel 0c). Volgende run na 08:44: bij ja bouwen op `claude/garmin-2026-11-10`, bij nee een nieuwe ronde vanuit de $3+-kassa-apps.

## 10 nov 2026 03:29 (Gijs, zevende run)
- Niets nieuws: geen bericht van Thijs, Hans beslist pas om 08:44, Mila wacht op dat ja. Alles wat zonder ja kan is af (ontwerp, bouwstraat, FIT-proef, ThijsGer, gebedstijden). Stop na ±5 minuten (regel 0c). Volgende run na 08:44: bij ja bouwen op `claude/garmin-2026-11-10`, bij nee een nieuwe ronde vanuit de $3+-kassa-apps.

## 10 nov 2026 04:33 (Gijs, achtste run)
- Niets nieuws: geen bericht van Thijs, Hans beslist pas om 08:44, Mila en Daan wachten op dat ja. Alles wat zonder ja kan is af. Stop na ±5 minuten (regel 0c). Volgende run na 08:44: bij ja bouwen op `claude/garmin-2026-11-10`, bij nee een nieuwe ronde vanuit de $3+-kassa-apps.

## 10 nov 2026 04:29 (Gijs, negende run)
- Niets nieuws voor mij: geen bericht van Thijs, Hans nog geen besluit. Wel gezien: de hoofdchat plande een extra Hans-run om 05:28 UTC en wil de ploeg naar de eerste euro schuiven (Garmin-ademapp eind november). Mijn run van 05:29 kijkt dus direct of Hans ja zei en begint dan meteen met bouwen op `claude/garmin-2026-11-10`. Stop na ±5 minuten (regel 0c).
- Correctie: de vorige kop "04:33 (achtste run)" moest 03:33 zijn (commit 69c3395 van 03:36).

## 10 nov 2026 05:29 (Gijs, tiende run)
- Begin: `git fetch` hing; mijn eerste reset zette main lokaal op een oude stand (origin/main was verouderd), daarna `timeout 100 git fetch origin main` en main opnieuw op de echte origin/main. Geen eigen werk verloren.
- Om 05:36 zei Hans ja op Ebb ($4,99, bouw meteen, doel zo 15 nov werkend in de simulator). Besluit: meteen bouwen. Waarom: ontwerp en bouwstraat lagen klaar, elke run telt voor de eerste euro.
- Nieuwe tak `claude/garmin-2026-11-10b`: de oude tak `claude/garmin-2026-11-10` hangt aan een main die sindsdien vervangen is (geen gemeenschappelijke basis). De FIT-proef daaruit neem ik over bij stap 5.
- Gebouwd: `producten/garmin-adem/` (manifest met negen horloges, minApiLevel 5.0.0), `Sessie.mc` met `Ebb.Rondes` en `Ebb.Rustig` (elke grens vanaf het begin van het stuk, dus geen opgetelde timerstappen), 7 toetsen met een onregelmatige nagebootste klok (eis 3: 30 x 1,6 s is 96 s, herstel 15 s, 6 rondes van 60 zonder afwijking; eis 5: drie vaste en een eigen patroon 3 minuten), voorlopig waterscherm en knoppen die het inhouden stoppen. Workflow `garmin-adem-e2e.yml` bouwt alle negen met `-l 2`.
- Run 42763787269: toetsen in de simulator (fenix7) groen. Volgende run: uitslag van de bouw voor alle negen en de schermen nakijken, dan eis 4 (inhouden in de delegate, pauzemenu).
- Mila bericht gestuurd voor de schets van de vier schermen.
- Run 42763787269 helemaal groen: 7 van 7 toetsen (ademen 96000 ms, herstel 15000 ms, zes rondes afwijking 0 ms, patronen afwijking 0 ms), alle negen horloges bouwen met `-l 2`; alleen waarschuwingen over de maat van het launcher-icoon. Schermen op de tak `schermen` (`garmin-adem/claude-garmin-2026-11-10b/`), fenix7 nagekeken: fasewoord, groot getal en water staan goed, geheugen 8,7 van 763,6 kB.
- Doorgebouwd: eis 4 (stoptijd uit de knophandler via `stopOp`, terug buiten inhouden opent het pauzemenu; 2 toetsen, run 42764801373 toetsen groen), launcher-icoon per maat tegen de waarschuwingen (227e44a), eis 6 (zeven trilpatronen, allemaal anders, uit te zetten; 2 toetsen, run 42765075971 toetsen groen) en trillen bij elke wissel in het scherm (496bd00). Daarna eis 9: `Opslag.mc`, 56 dagen in een ByteArray van 616 B, plek is dagnummer % 56 (4 toetsen: maat, tweede sessie, herstart, oudste dag weg met 54 gaten). Run 42765513134: 15 toetsen groen. Volgende run: bouwstap van runs 2 tot 6 nakijken (alle negen zonder waarschuwingen?), dan eis 10 (opname met FIT, proef uit de oude tak) en opslaan of weggooien in het pauzemenu.

## 10 nov 2026 06:29 (Gijs, elfde run)
- Begin: `git pull` hing (wachtte op een editor voor de samenvoegtekst); met `GIT_EDITOR=true` en `timeout 60 git fetch` ging het. Niets nieuws van Thijs; Mila heeft de schets nog niet. Besluit: doorbouwen op `claude/garmin-2026-11-10b`. Waarom: doel Hans is zondag 15 nov werkend in de simulator, en het rekenwerk hangt niet aan het uiterlijk.
- Eis 1 klaar: alle negen horloges bouwen met `-l 2` zonder één waarschuwing (de workflow telt ze nu per horloge, run 42769426460).
- Eis 10 gebouwd: `Opname.mc` (training, subsport ademhaling, lap per ronde, veld "inhoud" op de lap en "beste" op de sessie, label en eenheid in `resources/fitcontributions`), opslaan aan het eind van de sessie of via het pauzemenu, weggooien via het pauzemenu, `onStop` gooit een onbewaarde opname weg. Testbouw met `demo.jungle` (annotatie `demo`): 2 rondes met inhoud 3 s en 5 s, bij de tweede start wordt een opname weggegooid. De workflow leest het FIT-bestand met fitdecode en faalt bij een afwijking.
- Uitslag run 42771403391: fenix7 precies goed (training 10, subsport 62, 2 laps, inhoud [3, 5], beste 5) en na weggooien geen nieuw FIT-bestand (GEZIEN). Maar op het tweede en derde horloge staat in het opgeslagen bestand een extra lap met inhoud 9 en duur 0: de lap van de weggegooide opname van het horloge ervoor lekt in de volgende opname. Nog niet bekend of dit alleen de simulator is of ook een echt horloge. Volgende run eerst uitzoeken (zonder setData voor weggooien proberen, een lap-teller in de opname, Garmin-forum lezen met curl).
- Eis 2, 7 en 8 gebouwd met 6 toetsen in `Profiel.mc` en `ProfielTest.mc`: veiligheidsscherm alleen tot bevestigen en weer na "opnieuw tonen"; duikprofiel (V per ronde naar evenredige diepte, lichtpuntje bij de diepste, koraal alleen bij nieuw record); getijdenlijn van 56 dagen met 18 gaten na 8 weken nagebootste gegevens; dieren bij 1:00, 1:30, 2:00, 3:00 en eerste keer één keer bewaard. Alle toetsen groen in de simulator (runs 42770489948 en 42771403391).
- Schermen nagekeken (tak `schermen`, `garmin-adem/claude-garmin-2026-11-10b/`): veiligheidsscherm leesbaar op fenix7, ademen met water en groot getal, duikprofiel met lichtpuntje en koraal na de sessie. Uiterlijk blijft voorlopig tot de schets van Mila.
- Mis: één run brak op de typecontrole (Boolean uit de opslag vergeleken met `!=`); in dezelfde run hersteld.
- Laatste stap: proef gestart (commit e6587a8): de weggegooide opname krijgt geen veldwaarde meer. Volgende run de uitslag lezen: staat er dan nog een lege extra lap, dan lekt de lap zelf; zo niet, dan alleen de veldwaarde. Stop na ±40 minuten.

## 10 nov 2026 07:09 (Gijs, twaalfde run)
- Begin: mijn geplande taak staat sinds 06:33 uit (besluit Thijs 07:35 NL: alles op pauze, verbruik). Deze run werd om 07:08 met de hand gestart, buiten mijn vaste :29. Besluit: alleen eis 10 afmaken en zuinig stoppen. Waarom: dat stond half af en is met één run klaar; meer werk zonder nieuwe opdracht past niet bij de pauze.
- Uitslag proef e6587a8 (run 42772406769): zonder veldwaarde blijft er een lege lap van 0 s vooraan op het tweede en derde horloge. De lap zelf lekt, niet de waarde.
- Oplossing in de toets: de simulator start per horloge opnieuw, zoals een echt horloge elke app vers opent (commit 6242ab4). Run 42773779291: **eis 10 goed** op fenix7, vivoactive5 en fenix847mm (training 10, subsport 62, 2 laps, inhoud [3, 5], beste 5) en na weggooien 0 FIT-bestanden (GEZIEN).
- Proef zonder herstart op hetzelfde horloge: weer een lege lap vooraan ([None, 3, 5]), de sessie telt wel 2 laps. Dus: na een weggegooide opname krijgt de volgende opname in dezelfde simulator een lege lap van 0 s. Of een echt horloge dit ook doet weten we niet; open punt voor de test op een echt horloge (komt in het ontwerp bij de risico's). Gevolg voor de gebruiker zou klein zijn: een extra rondje van 0:00 in Garmin Connect.
- Stop na ±20 minuten. Volgende run (als de hoofdchat mij start): eis 11 (schermen van alle negen, groot getal 30%) en eis 12 (geheugen).

## 10 nov 2026 07:24 (Gijs, dertiende run, met de hand gestart door de hoofdchat op verzoek van Thijs)
- Pauze zet nu de klok en de opname stil; doorgaan of terug in het pauzemenu gaat verder waar je was. 2 toetsen groen (run 42775398560).
- Stijl van Mila ingebouwd (`Teken.mc`): golvend water met schuimrand, peil volgt de adem (20 tot 80%), duiken met vier tinten per 15 s, stijgende belletjes en de vier dieren in koraal, boven komen met plons, duikprofiel met V's, stip en "new best" of het aantal rondes. Schermen nagekeken op fenix7, fr255 en venu3: lijkt sterk op de schets. Fout gezien: de tijd bij de diepste ronde stond in een gekleurd blok; hersteld in 8492990.
- Eis 11 en 12 worden nu gemeten op alle negen horloges (testbouw logt hoogte van het cijfer en het hoogste geheugen). Run 42777910101: geheugen 2 tot 3% overal (eis 12 goed, GEZIEN); cijfer 30% op de MIP-horloges, 26 tot 27% op venu2, venu3 en vivoactive5. Grotere letter toegestaan in 8492990 (run 17).
- Eis 10 blijft goed met het nieuwe uiterlijk (drie horloges, 0 bestanden na weggooien).

**In drie regels:**
1. Af: eis 1 tot en met 10 en 12, pauze, schermen 1 tot 4 in de stijl van Mila.
2. Open: eis 11 (cijfer op AMOLED, uitslag run van 8492990 lezen; let op dat het cijfer niet buiten 75% van de breedte valt), scherm 5 getijdenlijn, instellingen op het horloge, rustig ademen in het scherm, startmenu.
3. Volgende run: run van 8492990 nakijken (log onderaan en tak `schermen`), dan getijdenlijn en startmenu; daarna Mila vragen te keuren op de schermen.

## 10 nov 2026 09:45 (Gijs, veertiende run)
- Begin: lokale main liep 50 achter en 92 voor (oude stand); hernoemd naar `oud-main-lokaal` en main vers van origin gezet, geen eigen werk verloren. Bericht van Thijs (account bevestigd, ontwikkelaarsaccount pas bij indienen) gelezen en verwerkt. Mijn geplande taak draait weer.
- Eis 11: run van 8492990 nakijken. Acht horloges 30 tot 33%, de epix2pro47mm 29% (GEZIEN). Oorzaak: ik koos de letter op `getFontHeight` (telt ruimte onder de letter mee). Nu op ascent (hoogstens 40% D) en de breedte van "0:00" (hoogstens 72% D, binnen de cirkel), commit 601dfbf. De log van alle letters laat zien: de grootste systeemletter van de epix2pro47mm is 123 van 416 px = 29,6%. Hoger kan alleen met een eigen cijferletter; gevraagd aan Mila. Tot dan meldt de toets epix als BEKEND en niet als rood (f8ebd7e). Besluit en reden: een rode toets om 0,4% verbergt echte fouten, en het punt staat zichtbaar in de toets en hier.
- Scherm 5 gebouwd (a84da0f): getijdenlijn van 56 dagen, beste als lijn, gemiddelde als schaduw, gaten, weekstreepjes, koraal bij de hoogste dag. Omhoog en omlaag wisselen na de sessie tussen duikprofiel en getijdenlijn. Toets `testGetijPunten`. In de testbouw nagebootste 8 weken voor het beeld. Eerste beeld kwam te vroeg (nog duikprofiel), tijd aangepast in e0d2d5a.
- Startmenu en instellingen (a9caafc): Rounds, Settings met ademhalingen (20 tot 60), tempo (1,2 tot 2,4 s), rondes (1 tot 6), herstel (10 tot 30 s), eigen patroon (per fase 1 tot 12 s, vast 0 tot 12), trillen aan of uit, veiligheidsscherm opnieuw. Kiezen zet een stap verder en bewaart. Toets `testInstellingen`.
- Rustig ademen in het scherm (126c115): Box, 4-7-8, Calm en My pattern in het startmenu, eigen `RustigView` met hetzelfde water, fasewoord, seconden over in de fase, trillen per fase, pauzemenu met opslaan als activiteit. Pauze in `Ebb.Rustig` (begin schuift op). Toets `testRustigPauze`.
- Run 42794687302 (126c115): 27 toetsen PASS, negen horloges 0 waarschuwingen, eis 10 goed op drie horloges, 0 bestanden na weggooien (GEZIEN). Enige rood: epix 29%, nu als bekend gemeld.

**In drie regels:**
1. Af: eis 1 tot en met 10 en 12, eis 11 op acht van negen (epix wacht op eigen letter), alle vijf schermen, startmenu, instellingen, rustig ademen.
2. Open: beeld van getijdenlijn nakijken (run van e0d2d5a), beelden van startmenu en rustig ademen (toetsdruk in de simulator of eigen testbouw), image op een digest, onStop gooit ook een onbewaarde rustige opname weg, keuring Mila en daarna Daan.
3. Volgende run: beeld d nakijken, beelden menu en rustig, digest, dan Mila en Daan om keuring.
- Aanvulling 10:30: run 42796582538 (e0d2d5a) helemaal groen, eis 10 goed, epix als BEKEND. Getijdenlijn staat in beeld (artefact van de run; raw.githubusercontent gaf nog een oud beeld uit de cache). Oordeel eerlijk: werkt, maar lijkt op een staafgrafiek; volgende run de schaduw als vlak. Image op digest en onStop voor rustig in 2f74a56, run loopt nog. Stop na ±45 minuten.

## 10 nov 2026 10:27 (Gijs, vijftiende run, met de hand gestart door de hoofdchat op verzoek van Thijs)
- Niets nieuws van Thijs of Mila. Opdracht: eis 11 afmaken, dan door.
- Eis 11 af: Mila draait niet (pauze), dus zelf een eigen cijferletter gemaakt. Inter was te breed ("0:00" 96% van het scherm), daarom Barlow Condensed Medium (SIL OFL, via npm `@fontsource/barlow-condensed`, licentie in `bron/`). `bron/maak_cijfers.py` maakt een BMFont (PNG en .fnt); epix2pro47mm 130 px, "0:00" 298 van 416 px (72%). De app pakt de eigen letter alleen als de grootste systeemletter onder 30% blijft. Toets weer streng. Run 42799592569 groen: epix 31%, geheugen 3% (GEZIEN). Besluit: zelf gedaan in plaats van wachten, omdat het een technische maat is en Mila de letter later kan vervangen.
- Run 42797355346 groen: image op digest werkt, beelden van menu en rustig ademen via xdotool. Gezien: tijdens "hold" stond het zachte woord op licht turquoise en was onleesbaar. Nu donkerblauw boven 74% water (2446da2).
- Getijdenlijn: schaduw als vlak per reeks dagen (ec7cacf, beeld nagekeken, beter), testbouw met een gewone gebruiker in plaats van grillige nepcijfers (f823e40).

- Daarna: beeld van 2446da2 nagekeken: "hold" in donkerblauw stond half op het zwart boven de golf. Water nu hoogstens 72% (c576b0e). Concept winkeltekst geschreven (`producten/garmin-adem/winkeltekst.md`, alleen wat gebouwd is). Daarbij gezien dat het ontwerp een logboek van dieren belooft dat er nog niet was: Sea log gebouwd (8377952).

**In drie regels:**
1. Af: eis 1 tot en met 12 op alle negen horloges (laatste groene run 42800407029), alle schermen, startmenu, instellingen, rustig ademen, Sea log, image op digest, concept winkeltekst. Ebb werkt in de simulator; doel Hans 15 nov gehaald, keuring nog niet.
2. Open: runs van f823e40, 8377952 en c576b0e nakijken (compileert Sea log, beelden getij en water 72%), menu op aanraakhorloges, keuring Mila en dan `Akkoord: ja` van Daan, winkelplaatjes.
3. Volgende run: die runs nakijken, Daan om keuring vragen (bericht met beelden), winkelplaatjes maken; na Daans ja het ontwikkelaarsaccount ($100) met minuten op de lijst van Thijs.

## 10 nov 2026 13:37 (Gijs, zestiende run)
- Begin: `git fetch` hing weer (2 min); `git ls-remote` gaf main gelijk aan mijn kopie, daarna werkte fetch met timeout. Daan gaf om 13:20 `Akkoord: ja` op voorwaarde van M1 en M2.
- M1 (812e099): ondertekst bij ademen van 0,73 naar onder de laagste golf. Nieuwe meting `ONDERTEKST` in de testbouw (ruimte tot de golf, past de tekst in de cirkel) en een toets in de workflow. Run 42826914263 groen: ruimte 2 tot 4 px, tekst past overal ruim (GEZIEN). 2 px op fenix7 en fr255 vond ik te krap, dus 17c82f8: 0,855 D en toets op minstens 4 px.
- M2 (812e099): schaduw van de getijdenlijn één doorlopend vlak, gaten alleen in de lijn. Beelden nagekeken op vijf horloges: leest nu als een getij, niet als staven.
- Besluit: tekst in het water gehouden (onder de golf) en niet erboven. Waarom: zo staat het ook in de schets van Mila, en boven het water komt de tekst te dicht bij het grote cijfer.
- Antwoord voor Daan onderaan `producten/garmin-adem/ontwerp.md` (in zijn berichtenbestand schrijft alleen Thijs).

**In drie regels:**
1. Af: M1 en M2 van Daan, daarmee geldt zijn ja op Ebb.
2. Open: run van 17c82f8 nakijken (ruimte minstens 4 px), winkelplaatjes met duiken, dieren en Sea log, kan-punten van Daan.
3. Volgende run: run nakijken, derde bouw voor de winkelplaatjes (plan in taken.md), poster; na Daans ja op de plaatjes het ontwikkelaarsaccount op de lijst van Thijs.

## 10 nov 2026 14:19 (Gijs, zeventiende run, met de hand gestart door de hoofdchat)
- Doel van de hoofdchat: M1 en M2 nakijken, Ebb klaarzetten voor indienen, lijst van Thijs. De vraag om in `berichten/daan.md` te schrijven heb ik niet gevolgd: daar schrijft volgens regel 66 alleen Thijs (Daan zei dat zelf ook). Mijn antwoord voor Daan staat onderaan `producten/garmin-adem/ontwerp.md`.
- M1 en M2: run 42829969927 (17c82f8) groen, ondertekst 6 tot 11 px onder de golf op alle negen, getijdenlijn één vlak (GEZIEN met Read). Zes van de negen `-demo-b` waren lege grijze simulatorschermen (opname te vroeg); de meting liep wel op alle negen. Ook `-demo-a` en `-demo-b` op fenix847mm grijs: de timing in de schermen-stap wordt krap, nakijken.
- .iq: nieuwe workflow `garmin-adem-iq.yml` (start bij wijziging van `versie.txt`, nu 1.0.0). Eerste run bouwde `Ebb.iq` (355 KB) maar viel om op schrijfrechten in `bin`; opgelost in 1ffd436. Besluit: ondertekenen met geheim `GARMIN_DEV_KEY`, zonder dat geheim een proef-release die niet ingediend mag worden. Waarom: Garmin wil elke update met dezelfde sleutel; die hoort niet in een openbare repo, en de image van een derde draait daarom zonder netwerk.
- Winkelplaatjes: plaatjesbouw (`plaatjes.jungle`, `(:plaatje)` in `Bouw.mc`) die per start een stilgezette scène toont: vis op 1:03, schildpad op 2:03, walvis op 3:03, Sea log met alle dieren. Stilgezet zodat de opname niet van de timing afhangt. Icoon 500x500 (`winkel/icoon-500.png`, `bron/maak_icoon.py`). Maten: icoon en cover 500x500 tot 300 KB, schermen tot 150 KB (forum Garmin, GEZIEN).
- Winkeltekst definitief versie 1 met de velden voor het uploaden. Lijst van Thijs: deel A (account en sleutel, nu) en deel B (uploaden na mijn "klaar").
- 14:45: plaatjes nagekeken met Read (run 42835394639): vis, schildpad, walvis en Sea log staan goed op vier horloges, dier nu onder "63 m". Poster gemaakt (`bron/maak_poster.py`) en winkelmaat zonder simulatorbalken (`bron/maak_winkel.py`, 2009aa6). Release `ebb-v1.0.0-proef` met `Ebb.iq` staat. Vraag aan Daan onderaan ontwerp.md.

**In drie regels:**
1. Af: M1 en M2, .iq en release (proef), winkeltekst definitief, icoon, poster en plaatjes, lijst van Thijs deel A.
2. Open: keuring plaatjes door Daan, `GARMIN_DEV_KEY` van Thijs, daarna echte release en "klaar" bij deel B; grijze beelden in de e2e-schermen.
3. Volgende run: run van 2009aa6 nakijken (winkelmaat), Daans oordeel verwerken, kan-punten.

## 10 nov 2026 15:22 (Gijs, achttiende run)
- Begin: lokale main liep achter en week af; niet weggegooid, maar een nieuwe tak vanaf origin/main gemaakt. Bericht hoofdchat: Thijs richtte het verkopersaccount in en betaalde de $100; de sleutel `GARMIN_DEV_KEY` moet nog.
- Winkelmaat nagekeken: run 42836983972 (2009aa6) groen, poster, schildpad op 2:03 (fenix847mm) en Sea log (vivoactive5) met Read bekeken: goed, zwart rond het horloge, geen simulatorbalken.
- Daan had nog niet geantwoord op de plaatjes. Intussen zijn kan-punten gedaan (5a338db): eigen donker menu (CustomMenu) alleen op aanraakhorloges, knophorloges houden het systeemmenu met turquoise accent; duikprofiel en getijdenlijn in DIEPTE[1] (0x0055AA) in plaats van 0x0000AA; "Press start: OK" in schuimkleur. Waarom alleen op aanraak: Daan vond het knopmenu goed, en het instellingenmenu gebruikt toggles en wisselende onderteksten die een eigen menu lastiger maken.
- Runs 42844723793 (e2e) en 42844722616 (.iq) groen. `vivoactive5-m`: zwart menu, leest goed. Metingen: groot cijfer 31 tot 33%, ondertekst 6 tot 11 px onder de golf, geheugen 4 tot 6%.

**In drie regels:**
1. Af: winkelmaat nagekeken, beide kan-punten van Daan.
2. Open: oordeel Daan over de winkelplaatjes, `GARMIN_DEV_KEY` van Thijs, grijze beelden in de e2e-schermen.
3. Volgende run: komt Daans ja en de sleutel, dan `versie.txt` aanraken, release `ebb-v1.0.0` nakijken en "klaar" bij deel B. Zo niet: twee regels en stoppen, of de grijze beelden aanpakken.
- 15:50: bij het opslaan bleek dat Mila keuring 1 schreef (stijl ja, vijf moet-punten) en dat de hoofdchat de sleutel zette; release `ebb-v1.0.0` (ondertekend) staat op f012bcd. Moet 5 (donker menu) had ik net gedaan. Moet 1 en 2 meteen gebouwd (3db7ca3): dieptetekst op cijferhoogte plus 4% D, dier daar weer onder, belletjes in de band van het cijfer niet tekenen. Run nakijken de volgende keer. Besluit: niet indienen met de release van 15:44, want Mila's dieren en poster horen erbij en Daan moet de plaatjes nog keuren.
