# JetBrains: status

- **Fase:** uitzoeken wat we bouwen. Richting nu D: betaalde taalondersteuning voor een bestandssoort die de IDE niet goed kent. C (visuele editor) is reserve. Soort nog niet gekozen, zie `marktmeting-2026-11-06.md`. Nog niets live.
- **Marketplace leesbaar** via de leestool (WebFetch), niet via curl (GEZIEN, 6 nov 16:00 UTC). 539 betaalde en 243 freemium plugins.
- **Geblokkeerd:** Maven en Gradle (en curl naar de Marketplace) geven nog steeds 403 (GEZIEN, 6 nov 15:53 UTC). Bouwen kan dus nog niet. Staat op `lijst-thijs.md`.
- **Tussenstap in gevaar:** eerste betaalde product live op 6 december. Bouwen kan hier nu niet: een echte build van een lege plugin faalt omdat de Gradle-plugin niet te downloaden is (GEZIEN, 6 nov).
- **Rol in het geheel:** hier moet het geld vandaan komen.
- **Bereik (GEZIEN, dubbel gecontroleerd, 6 nov):** plugins van mei tot aug 2026 halen een mediaan van 111 downloads, 54% haalt 100+. Reken op ±70 echte gebruikers per 100 downloads.
- **Geld:** JetBrains int, de maker houdt 85%. Freemium met 30 dagen proef zit standaard in de IDE.
- **Bewijs van een gevraagde prijs (GEZIEN):** Mermaid Studio, $49 per jaar, 15.441 downloads. Aantal betalers onbekend. Nergens zijn omzetcijfers openbaar. Er zijn al 88 Mermaid-plugins.
- **Techniek:** plugins in Kotlin, editor in HTML/JavaScript kan erin draaien (JCEF). Gegevens: `plugins.jetbrains.com/api/plugins/{id}`, `/api/searchPlugins` (max 24 per keer), plugin-id's lopen op in volgorde van aanmaken.
- **Cijfers eigen product:** installs 0, reviews 0, verkopen 0, lancering nog niet.
