# JetBrains: status

- **Fase:** uitzoeken wat we bouwen. Richting nu D: betaalde taalondersteuning voor een bestandssoort die de IDE niet goed kent. C (visuele editor) is reserve. Kortste lijst: Liquid (gratis plugin 328.663 downloads, cijfer 2,61, GEZIEN), reserve Caddyfile. Nog geen bouwbesluit, zie `marktmeting-2026-11-06.md`. Nog niets live.
- **Marketplace leesbaar** via de leestool (WebFetch), niet via curl (GEZIEN, 6 nov 16:00 UTC). 539 betaalde en 243 freemium plugins.
- **Netwerk open** sinds Thijs het om ±16:00 UTC openzette: curl naar Marketplace, Gradle en Maven geeft 200 (GEZIEN, 6 nov 16:05 UTC). Marketplace lezen voortaan met curl, nooit met WebFetch (regel in CLAUDE.md).
- **Bouwen werkt:** lege plugin gebouwd en getest, 2 tests groen (GEZIEN, 16:11 UTC). Recept in `bouwsjabloon.md`.
- **Tussenstap:** eerste betaalde product live op 6 december. Bouwen kan nu, de soort moet nog gekozen worden.
- **Rol in het geheel:** hier moet het geld vandaan komen.
- **Bereik (GEZIEN, dubbel gecontroleerd, 6 nov):** plugins van mei tot aug 2026 halen een mediaan van 111 downloads, 54% haalt 100+. Reken op ±70 echte gebruikers per 100 downloads.
- **Geld:** JetBrains int, de maker houdt 85%. Freemium met 30 dagen proef zit standaard in de IDE.
- **Bewijs van een gevraagde prijs (GEZIEN):** Mermaid Studio, $49 per jaar, 15.441 downloads. Aantal betalers onbekend. Nergens zijn omzetcijfers openbaar. Er zijn al 88 Mermaid-plugins.
- **Techniek:** plugins in Kotlin, editor in HTML/JavaScript kan erin draaien (JCEF). Gegevens: `plugins.jetbrains.com/api/plugins/{id}`, `/api/searchPlugins` (max 24 per keer), plugin-id's lopen op in volgorde van aanmaken.
- **Cijfers eigen product:** installs 0, reviews 0, verkopen 0, lancering nog niet.
