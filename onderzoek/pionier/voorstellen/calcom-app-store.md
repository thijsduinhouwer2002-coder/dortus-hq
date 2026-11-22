# Cal.com App Store (9 nov 2026, Noor)

Korte meting, run 9 nov 02:40 UTC. Cijfer 3, advies nee.

## De vijf vragen
1. **Groeit het platform?** Ja, het gebruik groeit hard. npm `@calcom/embed-react` 449.158 downloads in okt 2025 naar 3.012.495 in okt 2026 (x6,7), `@calcom/atoms` 36.507 naar 151.457 (x4,1) (GEZIEN, api.npmjs.org). Dat is vooral het inbouwen van de agenda in andere sites, niet de app store.
2. **Is de winkel jong?** Nee. De app store bestaat sinds 2021. Er staan 93 apps in de broncode (GEZIEN, `packages/app-store/*/config.json` in calcom/cal.com, gekloond 9 nov). Een app toevoegen gaat via een pull request in de monorepo van Cal.com, die zij moeten goedkeuren. Geen aanmaakdatums gemeten (kloon zonder geschiedenis).
3. **Kan er betaald worden?** Niet voor makers. Het blok `paid` (prijs in dollars, abonnement) bestaat in de app-config, maar wordt door precies één app gebruikt: `baa-for-hipaa`, van Cal.com zelf, $300 per maand (GEZIEN). Nergens in de bijdrage-regels (CONTRIBUTING.md) staat hoe een buitenstaander betaald zou worden. Wie geld wil, moet een eigen dienst met eigen abonnement koppelen.
4. **Vraag?** Niet gemeten; de winkel is geen verkoopkanaal, dus vraag naar apps zou ons niet direct geld opleveren.
5. **Eerste plek te pakken?** De apps zijn koppelingen van bedrijven met hun eigen dienst: 37 van Cal.com zelf, 9 van "Cal.diy" (de open-sourcetak), de rest één per bedrijf (Zapier, HubSpot, Salesforce, Granola, Retell AI enzovoort) (GEZIEN). Categorieën: conferencing 25, automation 21, other 15, analytics 13. Het is een koppelingenlijst, geen markt voor kleine makers.

## Risico en oordeel
Cal.com zelf doet het goed, maar de winkel is een gesloten koppelingenlijst van vijf jaar oud zonder betalen voor makers. Dezelfde les als Vercel: hard groeiend platform, maar de eigenaar kiest wie erin mag en een product moet een eigen gehoste dienst zijn.

Cijfer 3. Nee. Opnieuw kijken alleen als Cal.com het `paid`-blok openzet voor makers met uitbetaling (zoek in de changelog op "paid apps" of "revenue share").
