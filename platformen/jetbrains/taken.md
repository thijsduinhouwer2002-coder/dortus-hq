# JetBrains: taken (belangrijkste bovenaan)

**Van Hans (6 nov, 20:50):** je meet grondig en elk deel is nagekeken, goed werk. Maar 12 delen in 6 runs, en elke run schuift de beste kandidaat op (Liquid, verlaten plugins, Jenkinsfile, nu Bison en Tcl). Dat dreigt een rondje te worden. Daarom een beslisregel, geen haast: maak de vier stappen voor Bison/Flex en Tcl hieronder af in hoogstens 2 runs. Neem daarna het bouwbesluit tussen de beste 2 of 3 soorten die je nu kent, met een kort scoreschema (vraag, betaalbewijs, concurrentie, bouwtijd), en laat het nakijken. Geen nieuw spoor meer voor dat besluit, tenzij alle kandidaten aantoonbaar afvallen; schrijf dan op waarom.

- [ ] Zet nu al de stappen voor een betaalde plugin klaar op `organisatie/lijst-thijs.md`: wat Thijs moet doen om verkoper te worden op JetBrains Marketplace (account, overeenkomst, uitbetaling), met links en hoe lang JetBrains erover doet. Waarom: die stappen hangen niet af van de keuze en kunnen de tussenstap van 6 december ophouden als ze pas na de bouw beginnen.

- [ ] Bouwbesluit, freemium, met curl (nooit WebFetch). Deel 10, 11 en 12 gedaan (nagekeken). Volgende voor Yacc/Bison/Flex en Tcl: (1) testen of IDEA en CLion ze kennen (zoek op `<fileType>`-registraties, zie deel 8), (2) Tcl Language Support installeren en bekijken wat hij kan, (3) testen of Bison Language Support in 2026.2 nog werkt, (4) laten nakijken. Daarna stap 3: kiezen, onderbouwen, laten nakijken. Voor cpuprofile en heapsnapshot nog een andere maat voor vraag. Geen haast (bericht Thijs 6 nov 17:18).
- [x] Meting deel 12: YouTrack-vraag Tcl (38 stemmen) en Bison (8), bestaande plugins, nagekeken (6 nov).
- [x] Meting deel 11: 302 soorten gefilterd, 47 op grootte gemeten, nagekeken (6 nov).
- [x] Meting deel 10: spoor (b), betalen mensen voor plugins voor veelvoorkomende bestanden, nagekeken (6 nov).
- [x] Meting deel 8: kent IDEA deze soorten zelf, nagekeken en verbeterd (6 nov).
- [x] Meting deel 5 en 6: 219 verlaten gratis plugins nagelopen op werkt-nog en vervangers, KITSS TECH-portfolio gemeten, aanraden door de IDE gevonden, nagekeken (6 nov).
- [x] Meting deel 4: mogelijke reden BatchCraft, nagekeken, werkhypothese verlaten plugin vervangen (6 nov).
- [x] Meting deel 3: nieuwe betaalde en freemium plugins op downloads per maand, nagekeken (6 nov).
- [x] Meting D deel 2: leeftijd en downloads per maand, nagekeken (6 nov). Uitkomst: D niet meer de voorkeur.
- [x] Meting D deel 1: taalsoorten nagelopen, kortste lijst Liquid en Caddyfile, nagekeken (6 nov).
- [ ] Bouw een eerste versie in `producten/jetbrains-<naam>/` vanuit `bouwsjabloon.md`, met tests en meteen met proefperiode en betaalde functies.
- [ ] Zet de betaalde versie op via JetBrains Marketplace (vraagt Thijs: account en sleutel).
- [ ] Lanceren en meten op dag 7 en dag 30.
- [x] Gradle-build van een lege plugin, 2 tests groen (6 nov), zie `bouwsjabloon.md`.
- [x] Controle uit `kandidaten.md` met echte Marketplace-cijfers, nagekeken (6 nov), zie `marktmeting-2026-11-06.md`.
- [x] Eerste ronde onderzoek zonder Marketplace-cijfers: 3 kandidaten en voorlopige keuze (6 nov), zie `kandidaten.md`.
