# JetBrains: taken (belangrijkste bovenaan)

**Van Hans (6 nov, 20:50):** je meet grondig en elk deel is nagekeken, goed werk. Maar 12 delen in 6 runs, en elke run schuift de beste kandidaat op (Liquid, verlaten plugins, Jenkinsfile, nu Bison en Tcl). Dat dreigt een rondje te worden. Daarom een beslisregel, geen haast: maak de vier stappen voor Bison/Flex en Tcl hieronder af in hoogstens 2 runs (die termijn is vervallen, bericht Thijs 6 nov 21:53; de vier stappen zijn af op 7 nov). Neem daarna het bouwbesluit tussen de beste 2 of 3 soorten die je nu kent, met een kort scoreschema (vraag, betaalbewijs, concurrentie, bouwtijd), en laat het nakijken. Geen nieuw spoor meer voor dat besluit, tenzij alle kandidaten aantoonbaar afvallen; schrijf dan op waarom.

- [ ] **Ontwerp (Daan, 7 nov):** `Akkoord: nee` (alleen skelet). Lees "Oordeel van Daan" onderaan `producten/jetbrains-bison-flex/ontwerp.md`: kleuren alleen via `DefaultLanguageHighlighterColors`, een kleurenpagina, de Pro-melding als balloon, en winkelplaatjes met een gewone projectnaam. Zet ze in de IDE-test op de schermen, licht en donker.

- [x] Stappen om verkoper te worden op JetBrains Marketplace op `organisatie/lijst-thijs.md` gezet, nagekeken (7 nov). Geen vaste kosten, 15% afdracht, beoordeling betaalde plugin binnen 2 werkdagen, geen verplichte aankondigingstermijn (DERDEN).

- [x] Bouwbesluit: Yacc/Bison + Lex/Flex, freemium, voor CLion. Scoreschema nagekeken (7 nov), zie `bouwbesluit-2026-11-07.md` en `organisatie/besluiten.md`.
- [x] Vaste testset van 10 echte bestanden (PostgreSQL, jq, Ruby, OpenBSD, Thrift), nagekeken (7 nov), op de tak `claude/jetbrains-2026-11-07`. Ontbreekt nog: een echte C++-grammatica met ruime licentie.
- [x] Ontwerp `producten/jetbrains-bison-flex/ontwerp.md` geschreven, controleur akkoord na verwerken (7 nov). Oordeel van Daan nog nodig vóór indienen, niet vóór bouwen.
- [x] Plugin-skelet (bestandssoorten `.y`, `.yy`, `.l`, `.ll` met iconen) en IDE-test op GitHub Actions (`.github/workflows/jetbrains-bison-flex-e2e.yml`, Starter + Driver, IDEA Community 2025.2.6.4 vast), schermen licht en donker op de tak `schermen`. 4 unittests en 2 IDE-tests groen (run 42358929005), controleur akkoord, op main (7 nov).
- [ ] Echte lexer en parser voor Bison en Flex (JFlex + Grammar-Kit, of handgeschreven), met kleuren, en eis 2 en 3 uit het ontwerp: de 10 echte bestanden zonder foutmelding, verwachte syntaxfout op de verwachte plek. Op een nieuwe tak `claude/jetbrains-<datum>`.
- [ ] CLion in de IDE-test (eis 1): `IdeProductProvider.CL` met vaste versie proberen; vraagt waarschijnlijk een licentie (GOK). Lukt het niet, zoek een andere weg of zet het op de lijst voor Thijs. Moet af vóór indienen.
- [ ] Daan vragen om een eerste blik op de schermen zodra er kleuren zijn (nu alleen soort en icoon). Let op: in het lichte thema blijft de bovenbalk donker; nagaan of dat de standaard is.
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
- [ ] Bouw de rest van versie 1 in `producten/jetbrains-bison-flex/` (folding, structuur, commentaar, Pro-functies met proefperiode en licentiecontrole), volgens `ontwerp.md`.
- [ ] Zet de betaalde versie op via JetBrains Marketplace (vraagt Thijs: account en sleutel).
- [ ] Lanceren en meten op dag 7 en dag 30.
- [x] Gradle-build van een lege plugin, 2 tests groen (6 nov), zie `bouwsjabloon.md`.
- [x] Controle uit `kandidaten.md` met echte Marketplace-cijfers, nagekeken (6 nov), zie `marktmeting-2026-11-06.md`.
- [x] Eerste ronde onderzoek zonder Marketplace-cijfers: 3 kandidaten en voorlopige keuze (6 nov), zie `kandidaten.md`.
