# JetBrains: status

- **Fase:** uitzoeken wat we bouwen. Geen bouwbesluit. Kandidaten: C-breed (viewer of editor voor een bestandssoort die de IDE niet kent) en D (betaalde taalondersteuning). Nieuwe plugins uit 2025 en 2026 van beide soorten halen ruwweg 450 tot 4.600 downloads per maand (GEZIEN). Model: freemium. Zie `marktmeting-2026-11-06.md`. Nog niets live.
- **Netwerk open** sinds Thijs het om ±16:00 UTC openzette: curl naar Marketplace, Gradle en Maven geeft 200 (GEZIEN, 6 nov 16:05 UTC). Marketplace lezen voortaan met curl, nooit met WebFetch (regel in CLAUDE.md).
- **Bouwen werkt:** lege plugin gebouwd en getest, 2 tests groen (GEZIEN, 16:11 UTC). Recept in `bouwsjabloon.md`.
- **Nieuw inzicht (6 nov 17:10 UTC, nagekeken):** BatchCraft groeit waarschijnlijk doordat de IDE hem zelf aanraadt bij `gradlew.bat` (GOK, mechanisme GEZIEN). Een verlaten plugin vervangen werkt niet vanzelf: van 5 zulke vervangers van KITSS TECH groeide er 1 (GEZIEN). Zie `marktmeting-2026-11-06.md` deel 6.
- **Deel 8 (nagekeken, 18:10 UTC):** `.npmrc`, `*.cpuprofile`, `*.heapsnapshot`, `Podfile` en `*.webmanifest` kent IDEA Ultimate 2026.2 niet als bestandssoort (GEZIEN). Deel 9 (nagekeken): Podfile valt af, CocoaPods gaat op 2 december 2026 op alleen-lezen (DERDEN). `.npmrc` en `*.webmanifest` veel bestanden, betalen onwaarschijnlijk (GOK). Sterkste spoor nu: bewijs van betalen bij Jenkinsfile en Procfile (Anbora Labs).
- **Deel 10 (nagekeken, 19:00 UTC):** mensen betalen voor plugins voor veelvoorkomende bestanden (reviews van kopers bij Jenkinsfile, IReport 6, BashSupport Pro, GEZIEN). Jenkinsfile ($15 / $50 per jaar) heeft ruwweg 5.000 tot 7.000 bijwerkende gebruikers (GOK). Procfile van dezelfde maker blijft klein; Jenkinsfile-bestanden zijn veel vaker groot (44% tegen 2% boven 2 kB, GEZIEN). Nieuwe eis: bestand dat werk is. Zie deel 10.
- **Deel 11 (nagekeken, 19:17 UTC):** 133 soorten zonder sterke plugin gefilterd, 47 op grootte gemeten. Sterkste kandidaat nu Yacc/Bison met Lex/Flex (`*.y` 72% groot, aangeraden plugins verlaten sinds 2020 en 2023), Tcl tweede (veel bestanden, maar een jonge groeiende gratis plugin). Nog niet getest of de IDE ze kent.
- **Tussenstap:** eerste betaalde product live op 6 december. Bouwen kan nu, de soort moet nog gekozen worden.
- **Rol in het geheel:** hier moet het geld vandaan komen.
- **Bereik (GEZIEN, dubbel gecontroleerd, 6 nov):** plugins van mei tot aug 2026 halen een mediaan van 111 downloads, 54% haalt 100+. Reken op ±70 echte gebruikers per 100 downloads.
- **Geld:** JetBrains int, de maker houdt 85%. Freemium met 30 dagen proef zit standaard in de IDE.
- **Bewijs van een gevraagde prijs (GEZIEN):** Mermaid Studio, $49 per jaar, 15.441 downloads. Aantal betalers onbekend. Nergens zijn omzetcijfers openbaar. Er zijn al 88 Mermaid-plugins.
- **Techniek:** plugins in Kotlin, editor in HTML/JavaScript kan erin draaien (JCEF). Gegevens: `plugins.jetbrains.com/api/plugins/{id}`, `/api/searchPlugins` (max 24 per keer), plugin-id's lopen op in volgorde van aanmaken.
- **Cijfers eigen product:** installs 0, reviews 0, verkopen 0, lancering nog niet.
