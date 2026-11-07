# Logboek jetbrains

Nieuwste blok onderaan.

## 6 nov 2026, eerste run
- **Gedaan:** eerste ronde onderzoek, `kandidaten.md` geschreven, blokkade op de lijst voor Thijs gezet.
- **Beslissing:** voorlopig C, de betaalde visuele editor, want alleen daar is nu een gevraagde prijs bekend. Of mensen betalen is onbekend. Geen bouwbesluit, want de Marketplace-cijfers ontbreken.
- **Beslissing:** A afgewezen als eerste keus, want de JetBrains-help (datum 4 nov) noemt zelf diff en terugdraaien voor agentwijzigingen.
- **Nakijken:** controleur keurde de eerste tekst af op te sterke beweringen, ontbrekende link en twee geschrapte feiten. Verbeterd.
- **Misging:** `plugins.jetbrains.com` onleesbaar via curl (403) en leestool (toestemming niet op tijd beantwoord). Maven en Gradle ook geweigerd. Niet opnieuw geprobeerd en geen omweg gezocht.

## 6 nov 2026, 14:52 UTC
- **Gedaan:** bereikbaarheid getest en één echte build van een lege plugin geprobeerd. Beide geweigerd of mislukt, zie `status.md`. Java 21 en Gradle 8.14.3 staan er wel.
- **Beslissing:** gestopt met de kandidaten-controle. WebSearch gaf alleen titels en links, en die pagina's zijn niet te lezen, dus geen bewijs om een keuze op te baseren. Geen omweg gezocht via GitHub Actions: die keuze is aan Thijs, staat op de lijst.
- **Nakijken:** geen controleur ingezet, er is alleen een meting genoteerd en geen werk opgeleverd.

## 6 nov 2026, 15:52 UTC
- **Gedaan:** curl naar `plugins.jetbrains.com` en `plugins.gradle.org` nog steeds 403 (niet herhaald). Daarna de Marketplace-API via de leestool (WebFetch) geprobeerd: dat werkt. Controle uit `kandidaten.md` gedaan, `marktmeting-2026-11-06.md` geschreven.
- **Beslissing:** richting D, betaalde taalondersteuning voor een bestandssoort die de IDE niet goed kent, want in de betaalde top 48 zitten 9 zulke plugins met 37.000 tot 620.000 downloads, tegen 6 betaalde visuele editors met 7.000 tot 89.000 en veel gratis diagramplugins. C blijft reserve. Nog geen bouwbesluit: de soort is niet gekozen.
- **Beslissing:** WebFetch is geen omweg, het is de gewone leestool die de eerste run ook al probeerde. Bouwen via GitHub Actions blijft aan Thijs.
- **Nakijken:** controleur keurde af op het totaal (533 bij zijn telling, 539 bij de mijne), "de grootste groep" zonder telling, "minder gratis concurrentie" zonder meting en een te stellige zin. Alles verbeterd of weggehaald, verschil in totaal staat erbij.
- **Misging:** Gradle nog dicht, dus geen build. Het verschil 539 en 533 is niet verklaard.
- **Later in dezelfde run (16:05 UTC):** bericht van Thijs gelezen, netwerk staat open. Nieuwe regel in CLAUDE.md gezien: Marketplace voortaan met curl, nooit met WebFetch. De meting van vandaag ging nog via WebFetch, voortaan niet meer.
- **Gedaan:** lege plugin gebouwd en getest, 2 tests groen. Recept in `bouwsjabloon.md`.
- **Beslissing:** Gradle 9 via de wrapper en alleen de JetBrains-spiegel voor Maven, want de nieuwste IntelliJ Platform Gradle Plugin eist Gradle 9 en Maven Central gaf twee keer 429.
- **Nakijken:** geen aparte controleur, de build en de tests zelf zijn de controle (exit 0, 2 tests, 0 fouten).
- **Gedaan (16:12 UTC):** meting D deel 1 met curl, ruim 40 taal- en bestandssoorten nagelopen.
- **Beslissing:** kortste lijst Liquid, reserve Caddyfile, want Liquid heeft de meeste gebruikers, een laag cijfer en geen goede gratis plugin ernaast. Nog geen bouwbesluit, want nieuwe betaalde taalplugins halen vaak maar honderden downloads en hun leeftijd is niet gemeten.
- **Nakijken:** controleur keurde af: gratis concurrenten bij Jsonnet, Caddyfile en Nginx weggelaten, "het slechtste cijfer" klopte niet, "oude plugins" en "werkt" zonder bewijs. Alles verbeterd, Jsonnet geschrapt.
- **Gedaan (16:14 UTC):** leeftijd van 11 plugins gemeten via de oudste versie, downloads per maand uitgerekend. Het veld `cdate` van een plugin is niet de startdatum, dat bleek bij BashSupport Pro.
- **Beslissing:** D niet meer de voorkeur, C en D weer naast elkaar, geen bouwbesluit. Reden: de grote betaalde taalplugins bestaan al sinds 2020 en 2021, nieuwe uit 2026 halen 86 tot 567 per maand, Mermaid Studio uit 2026 haalt 1.682. Liquid valt terug omdat de gratis Liquid-plugin van JetBrains zelf is.
- **Nakijken:** controleur akkoord, twee kleine punten verwerkt.
- **Misging:** ik schreef eerst tijden op die niet klopten (16:17, 16:20, 16:25 terwijl het 16:12 en 16:13 was). Verbeterd met `date`. Voortaan de tijd altijd met `date` opvragen.
- **Gedaan (16:16 UTC):** alle betaalde en freemium plugins opgehaald, 102 nieuwe (2025 en 2026) gerangschikt op downloads per maand.
- **Beslissing:** model wordt freemium, want bijna alle nieuwe viewers en veel nieuwe taalplugins zijn freemium en halen zo honderden tot duizenden downloads per maand. Tussen C-breed en D nog geen keuze: de cijfers verschillen niet duidelijk.
- **Nakijken:** controleur keurde af: taallijst en viewerlijst waren selectief ingevuld, en "C-breed" als richting volgde daar niet uit. Lijsten aangevuld, richting teruggezet naar geen voorkeur.
- **Gedaan (16:20 UTC):** uitgezocht waarom BatchCraft snel groeit: de twee gratis batch-plugins (samen ruim 4 miljoen downloads) zijn sinds 2015 en 2021 verlaten.
- **Beslissing:** volgende run zoekt systematisch naar zulke verlaten gratis plugins, want dat is een concreet en meetbaar patroon, en het geeft een kant-en-klaar publiek. Nog één voorbeeld, dus het blijft een GOK tot er meer zijn.
- **Gedaan (16:21 UTC):** lijst gemaakt van 219 verlaten gratis plugins met meer dan 100.000 downloads, eerste drie nagelopen op vervangers. Nog niet nagekeken door een controleur, dus de taak blijft open.
- **Afgesloten om 16:23 UTC** om de volgende run schoon te laten beginnen.


## 6 nov 2026, 16:53 UTC
- **Gedaan:** berichten van Thijs van 17:08 en 17:18 verwerkt (curl staat al in taken, WebFetch-regel uit `status.md` gehaald). Meting deel 5 afgemaakt en deel 6 gedaan: van de 219 verlaten gratis plugins werken er 76 niet meer in IDE 2025.2+. KITSS TECH (maker van BatchCraft) bracht in oktober 27 plugins uit, alleen BatchCraft groeide. Gevonden hoe de IDE plugins aanraadt voor onbekende bestanden, en dat BatchCraft daar bij `*.bat` in staat. Testje in IntelliJ 2025.2 en 2026.2 gebouwd dat per bestandsnaam de bestandssoort toont.
- **Beslissing:** werkhypothese "vervang een verlaten plugin" bijgesteld naar "bestand dat overal zit, dat de IDE niet kent, zonder JetBrains-plugin, met verlaten aangeraden plugins". Reden: 1 van 5 vervangers groeide, en alleen die ene staat in de aanraadlijst. Nog geen bouwbesluit, er is geen tweede soort gevonden die aan alle eisen voldoet.
- **Nakijken:** controleur keurde eerst af op 6 punten (git flow fout, 1 van 4 moest 1 van 5, Pascal zonder meting, downloads geen gebruikers, *.cmd, uitlichting). Verwerkt, herkeuring akkoord.
- **Misging:** de testomgeving van de IDE laadt niet alle meegeleverde plugins, dus "onbekend" in die test is niet zeker. Bouwsjabloon miste de spiegel voor de plugin-resolutie, aangevuld.
- **Later in deze run (17:14 UTC):** bouwbesluit stap 1 gedaan, 302 bestandssoorten nagelopen op aanraadlijst, JetBrains-plugin en versheid. Geen tweede batch gevonden. Controleur keurde af op 6 kleine punten (tellingen en te stellige zinnen over downloads), verwerkt. Drie sporen voor de volgende run genoteerd. Geen bouwbesluit, want geen soort voldoet aan alle eisen.
- **Daarna (17:21 UTC):** deel 8, in de echte installatie van IDEA 2026.2 nagezocht welke soorten hij zelf kent. Nog niet nagekeken, staat bovenaan de taken.
- **Afgesloten om 17:22 UTC.**


## 6 nov 2026, 17:53 UTC
- **Gedaan:** berichten van Thijs gelezen, alle drie al verwerkt. Deel 8 laten nakijken door een controleur, die de meting opnieuw deed in IDEA Ultimate 2026.2 (build 262.8665.258) en zocht op echte `<fileType>`-registraties.
- **Uitkomst:** afgekeurd op 6 punten. Mijn eerste versie zocht op losse tekst en zei daardoor ten onrechte dat de IDE `.npmrc` en `*.cpuprofile` kent. Deel 8 herschreven: alle vijf soorten zijn geen bestandssoort in IDEA, alleen heapsnapshot is via een menu te laden. Gevolg omgedraaid: spoor (a) en (c) blijven open.
- **Beslissing:** geen bouwbesluit. Volgende stap is stap 2 (hoe vaak komen deze soorten voor en is er vraag), naast spoor (b). Reden: zonder telling van vraag is een keuze tussen deze vijf niet te onderbouwen.
- **Misging:** de controle duurde ±15 minuten (IDE downloaden). Les: zoek naar registraties, niet naar tekst.
- **Toch nog tijd (18:11 UTC):** deel 9 gedaan, de vijf soorten geteld met GitHub-zoeken en de Marketplace. Podfile komt even vaak voor als `gradlew.bat` maar valt af: CocoaPods gaat op 2 december 2026 op alleen-lezen, dus de soort krimpt. `.npmrc` en `*.webmanifest` veel bestanden maar waarschijnlijk niets om voor te betalen.
- **Beslissing:** spoor (a) levert geen betaald product, volgende run spoor (b). Reden: geld gaat voor bereik, en alleen bij Jenkinsfile en Procfile is er een betaalde plugin voor een veelvoorkomend bestand.
- **Nakijken:** controleur kreeg dezelfde getallen, goedgekeurd mits 4 zinnen minder stellig. Verwerkt.
- **Afgesloten om 18:15 UTC.**


## 6 nov 2026, 18:52 UTC
- **Gedaan:** berichten van Thijs gelezen, alle drie al verwerkt. Spoor (b) gedaan als meting deel 10: prijzen, downloads per versie en reviews van 18 betaalde plugins met curl, plus GitHub-tellingen van grote bestanden. De prijsroute van de Marketplace gevonden (`/api/marketplace/plugin/{id}/prices?countryCode=US`).
- **Uitkomst:** er zijn aantoonbaar kopers (reviews bij Jenkinsfile, IReport 6, BashSupport Pro). Jenkinsfile en Procfile van dezelfde maker komen even vaak voor en worden allebei aangeraden, maar alleen Jenkinsfile groeit; Jenkinsfile-bestanden zijn veel vaker groot (44% tegen 2%).
- **Beslissing:** nieuwe eis voor kandidaten: het bestand moet werk zijn en het publiek moet in JetBrains-IDE's zitten. Reden: zonder dat bleven Procfile en Brew Bundle klein, ook met aanraden en een lage prijs. Geen bouwbesluit, eerst de 302 soorten filteren en op grootte meten.
- **Nakijken:** controleur deed de getallen opnieuw, alles gelijk. Akkoord mits 8 punten (ondergrens rekensom, GOK-label bij de verklaring, publiek als tweede verklaring, eis minder streng). Alle 8 verwerkt.
- **Misging:** het veld `meanRating` van de Marketplace is voor elke plugin gelijk (4,06383), dus geen bruikbaar cijfer. Alleen `votes` gebruiken.
- **Daarna (19:02 UTC):** deel 11, de 302 soorten gefilterd (133 zonder sterke bijgehouden plugin) en 47 handgeschreven soorten op GitHub op grootte gemeten.
- **Beslissing:** Yacc/Bison/Flex als sterkste kandidaat om verder te onderzoeken, Tcl tweede. Reden: grote bestanden, verlaten aangeraden plugins, en ze zitten in C-, C++- en Go-projecten. Tcl zakte omdat er sinds september 2026 een bijgehouden gratis plugin groeit. Geen bouwbesluit: eerst testen of de IDE ze kent en of het publiek JetBrains gebruikt.
- **Nakijken:** controleur akkoord mits 5 punten (filter, dubbelzinnige `.l` en `.y`, Tcl-plugin jong, Tcl vaak gegenereerd). Verwerkt.
- **Daarna (19:18 UTC):** deel 12, YouTrack-stemmen en de bestaande plugins voor Tcl en Yacc/Bison/Flex. Tcl heeft duidelijk vraag (38 stemmen in CLion), maar al een jonge gratis plugin; Bison weinig stemmen (8) en verlaten plugins. Stemmen passen bij Jenkinsfile tegen Procfile. Controleur akkoord mits 7 punten (onder andere GoYacc had twee versies), verwerkt. Geen bouwbesluit.
- **Afgesloten om 19:22 UTC.**


## 7 nov 2026, 07:53 UTC
- **Gedaan:** berichten gelezen; 21:53, 23:45 en 08:30 nog niet verwerkt, nu wel (geen zijpad, IDE-test met schermen als taak na het bouwbesluit). Stappen om verkoper te worden op JetBrains Marketplace uitgezocht en op `organisatie/lijst-thijs.md` gezet, nagekeken (akkoord mits 2 punten, verwerkt). Deel 13: de laatste stappen voor Bison/Flex en Tcl, nagekeken (akkoord mits 4 punten, verwerkt).
- **Beslissing:** de verkoperstappen eerst, omdat de controle van de bedrijfsgegevens door JetBrains tijd kost en niet afhangt van de keuze.
- **Misging:** de lokale kloon liep uit de pas met GitHub (geen gezamenlijke geschiedenis), opgelost door main gelijk te zetten aan origin/main; er ging geen werk verloren, mijn commits stonden al op GitHub. De eerste onderzoeksopdracht werd geweigerd omdat hij een Gradle-test met gedownloade plugins wilde starten ("code van buiten"); opnieuw gedaan met alleen lezen. Dus "werkt nog" voor de Bison-plugins is alleen afgeleid uit gegevens. Testen in de echte IDE moet op GitHub Actions. api.github.com gaf 403 in deze run.
- **Daarna (08:12 UTC):** bouwbesluit genomen met een scoreschema (vraag, betaalbewijs, concurrentie, bouwtijd) tussen Bison/Flex en Tcl, met Jenkinsfile en Procfile als maat. Nagekeken: akkoord mits 7 punten, alle verwerkt, onder andere dat de cijfers alleen gelijk opgaan en de concurrentie de doorslag geeft, en een fout getal in deel 11 (Tcl ±1.300 per maand moest ±450 tot 480 zijn).
- **Beslissing:** Yacc/Bison + Lex/Flex wordt het eerste betaalde product. Reden: geen IDE kent de soorten en er is bijna geen aanbod, terwijl Tcl al een gratis volledige taalserver heeft. Eerlijk vastgelegd dat de markt klein is: dit product bewijst de hele weg, voor het geld is een tweede product nodig (staat als taak).
- **Afgesloten om ±08:20 UTC.**
- **Toch nog tijd (08:13 UTC):** ontwerp voor de plugin geschreven (`producten/jetbrains-bison-flex/ontwerp.md`). Controleur akkoord mits 5 punten, alle verwerkt: geen C/C++-injectie in versie 1 (onder de nieuwe C++-engine van CLion waarschijnlijk niet mogelijk, GOK), syntaxfouten in het gratis deel (de gratis Bison-plugin doet dat ook), product-descriptor `PBISONFLEX` met versie 2026.1.0 concreet, eisen scherper, aanvullen naar 1.1.
- **Beslissing:** aanvullen en C-injectie uit versie 1. Reden: sneller lanceren en het grootste technische risico eruit, zonder dat het gratis deel zwakker wordt dan de concurrent.
- **Daarna (08:17 UTC):** vaste testset van 10 echte Bison- en Flex-bestanden gekozen (PostgreSQL, jq, Ruby, OpenBSD, Apache Thrift; alleen ruime licenties, vast op tag of commit) en op de tak `claude/jetbrains-2026-11-07` gezet. Zelf nagekeken (regels, geen GPL); de controleur doet het de volgende run. Tak gekozen omdat het bij de code van het product hoort.
- **Afgesloten om ±08:19 UTC.**
- **Na het afsluiten nog (08:22 UTC):** testset nagekeken, akkoord mits NOTICE van Thrift en een telling; beide verwerkt op de tak. Volgende run: IDE-test en bouwen beginnen op die tak.
