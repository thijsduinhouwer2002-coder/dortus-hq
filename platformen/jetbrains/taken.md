# JetBrains: taken (belangrijkste bovenaan)

**Van Hans (6 nov, 20:50):** je meet grondig en elk deel is nagekeken, goed werk. Maar 12 delen in 6 runs, en elke run schuift de beste kandidaat op (Liquid, verlaten plugins, Jenkinsfile, nu Bison en Tcl). Dat dreigt een rondje te worden. Daarom een beslisregel, geen haast: maak de vier stappen voor Bison/Flex en Tcl hieronder af in hoogstens 2 runs (die termijn is vervallen, bericht Thijs 6 nov 21:53; de vier stappen zijn af op 7 nov). Neem daarna het bouwbesluit tussen de beste 2 of 3 soorten die je nu kent, met een kort scoreschema (vraag, betaalbewijs, concurrentie, bouwtijd), en laat het nakijken. Geen nieuw spoor meer voor dat besluit, tenzij alle kandidaten aantoonbaar afvallen; schrijf dan op waarom.

- [x] Stappen om verkoper te worden op JetBrains Marketplace op `organisatie/lijst-thijs.md` gezet, nagekeken (7 nov). Geen vaste kosten, 15% afdracht, beoordeling betaalde plugin binnen 2 werkdagen, geen verplichte aankondigingstermijn (DERDEN).

- [x] Bouwbesluit: Yacc/Bison + Lex/Flex, freemium, voor CLion. Scoreschema nagekeken (7 nov), zie `bouwbesluit-2026-11-07.md` en `organisatie/besluiten.md`.
- [ ] Testset laten nakijken door een controleur: staat op de tak `claude/jetbrains-2026-11-07` in `producten/jetbrains-bison-flex/testdata/` (10 bestanden van PostgreSQL, jq, Ruby, OpenBSD, Thrift, met `BRONNEN.md` en licenties). Controleren: URL's en tags, licenties (geen GPL), regels. Ontbreekt: een echte C++-grammatica (`%language "c++"`) met ruime licentie.
- [x] Vaste testset van 10 echte bestanden gekozen (7 nov), zelf gecontroleerd op regels en GPL, controleur nog nodig.
- [x] Ontwerp `producten/jetbrains-bison-flex/ontwerp.md` geschreven, controleur akkoord na verwerken (7 nov). Oordeel van Daan nog nodig vóór indienen, niet vóór bouwen.
- [ ] IDE-test opzetten: en een IDE-test op GitHub Actions (`.github/workflows/jetbrains-bison-flex-e2e.yml`, UI-test van het IntelliJ Platform Gradle Plugin), met schermafbeeldingen licht en donker naar de tak `schermen` (kopieer die stap uit `rollwright-e2e.yml`). Ook bouwen daar, want in de cloud mocht een Gradle-test met gedownloade plugins op 7 nov niet starten. Indienen pas na groene test en `Akkoord: ja` van Daan.
- [x] Meting deel 13: CLion en IDEA 2026.3 kennen `.y`, `.l`, `.tcl` niet; wat Tcl Language Support kan; Bison-plugins nog compatibel volgens gegevens; nagekeken (7 nov).
- [x] Meting deel 12: YouTrack-vraag Tcl (38 stemmen) en Bison (8), bestaande plugins, nagekeken (6 nov).
- [x] Meting deel 11: 302 soorten gefilterd, 47 op grootte gemeten, nagekeken (6 nov).
- [x] Meting deel 10: spoor (b), betalen mensen voor plugins voor veelvoorkomende bestanden, nagekeken (6 nov).
- [x] Meting deel 8: kent IDEA deze soorten zelf, nagekeken en verbeterd (6 nov).
- [x] Meting deel 5 en 6: 219 verlaten gratis plugins nagelopen op werkt-nog en vervangers, KITSS TECH-portfolio gemeten, aanraden door de IDE gevonden, nagekeken (6 nov).
- [x] Meting deel 4: mogelijke reden BatchCraft, nagekeken, werkhypothese verlaten plugin vervangen (6 nov).
- [x] Meting deel 3: nieuwe betaalde en freemium plugins op downloads per maand, nagekeken (6 nov).
- [x] Meting D deel 2: leeftijd en downloads per maand, nagekeken (6 nov). Uitkomst: D niet meer de voorkeur.
- [x] Meting D deel 1: taalsoorten nagelopen, kortste lijst Liquid en Caddyfile, nagekeken (6 nov).
- [ ] Tweede, grotere kandidaat zoeken binnen wat al gemeten is (Tcl met een kleinere insteek, soorten zoals Jenkinsfile), zodat er na de eerste lancering een tweede product klaarligt. Geen nieuwe zijpaden vóór het eerste product loopt.
- [ ] Bouw een eerste versie in `producten/jetbrains-bison-flex/` vanuit `bouwsjabloon.md`, met tests en meteen met proefperiode en betaalde functies.
- [ ] Zet de betaalde versie op via JetBrains Marketplace (vraagt Thijs: account en sleutel).
- [ ] Lanceren en meten op dag 7 en dag 30.
- [x] Gradle-build van een lege plugin, 2 tests groen (6 nov), zie `bouwsjabloon.md`.
- [x] Controle uit `kandidaten.md` met echte Marketplace-cijfers, nagekeken (6 nov), zie `marktmeting-2026-11-06.md`.
- [x] Eerste ronde onderzoek zonder Marketplace-cijfers: 3 kandidaten en voorlopige keuze (6 nov), zie `kandidaten.md`.
