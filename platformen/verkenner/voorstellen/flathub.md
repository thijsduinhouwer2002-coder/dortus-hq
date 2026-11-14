# Voorstel: Flathub (Linux-appwinkel voor Flatpak)

Vera, 14 nov 2026, run 09:31 (Amsterdam). Nooit eerder bekeken. Eigen meting van alle 3.380 apps via de open zoek-API. Niet nagekeken door een aparte controleur (tijd op); de cijfers komen rechtstreeks uit één API-antwoord en zijn met het script na te rekenen.

## Wat het is
De grootste winkel voor Linux-desktopapps (Flatpak), van de GNOME Foundation en Flathub LLC. Zit standaard in o.a. Fedora, Linux Mint, Pop!_OS, SteamOS-achtige systemen en de Steam Deck (bureaubladstand). Ruim 1 miljoen actieve gebruikers (DERDEN, Flathub-blog, al wat ouder).

## Cijfers
**Drukte (GEZIEN):** 3.380 apps in de zoekindex. Nieuw per maand in 2026: 29 tot 76, samen 462 nieuwe apps van nov 2025 t/m aug 2026.

**Bereik (GEZIEN, veld installs_last_month per app):**
- Nieuwe apps van nov 2025 t/m aug 2026 (3 tot 12 maanden oud): mediaan 382 per maand, 86% haalt 100+ per maand.
- Per maand van toevoeging, mei t/m aug 2026 (3 tot 6 maanden oud): mediaan 320 tot 466 per maand, 84 tot 96% haalt 100+, 22 tot 34% haalt 1.000+.
- Nieuwe spellen (74 stuks): mediaan 190 per maand.
- Let op: Flathub telt downloads van installaties **en updates** (DERDEN, docs.flathub.org/blog/over-one-million-active-users-and-growing). Een app die vaak updates uitbrengt telt dus dubbel. Het echte aantal nieuwe gebruikers ligt lager, GOK de helft tot een derde. Ook dan is dit het beste bereik voor nieuwkomers dat ik na Modrinth heb gezien: bijna elke nieuwe app wordt gevonden, via de voorpagina (Nieuw, Trending) en zoeken in de winkel-apps van GNOME en KDE.

**Geld:**
- Betalen in de winkel bestaat nog niet. Eind nov 2025 schreef een Flathub-medewerker "Flathub wants to setup a way to offer payments for applications but unfortunately it's not ready yet" (DERDEN, planet.kde.org, blog 23 nov 2025).
- De API heeft de onderdelen wel al: vending, wallet, purchases, Stripe-webhook en een verdeling per platform (GNOME- en KDE-apps: 70% voor de maker, freedesktop 100%, plus een vaste kostenpost) (GEZIEN, flathub.org/api/v2/openapi.json en /vending/config, 14 nov 2026). Geen enkele app toont een prijs: de metadata van alle 354 apps met een niet-vrije licentie bevat geen prijsveld (GEZIEN).
- Wie nu geld wil, verkoopt een licentie op de eigen site en zet de app gratis op Flathub. Voorbeelden onder de nieuwe apps: Loopa ($9,99 eenmalig, 466 per maand), Fog Panther (beeldbewerking, "pay once", 1.521 per maand) (GEZIEN, sites en API). Hoeveel zij verkopen is nergens te zien.
- Kleine Linux-makers met omzet op TrustMRR: VoxBee (Mac en Linux) $586 in 12 maanden, Whisperdict (alleen Linux) $0 (GEZIEN, onze TrustMRR-data van 8 nov). Geen enkele Linux-only maker gevonden boven $300 per maand.
- Discourse van Flathub is nu een alleen-lezen archief (GEZIEN); waar de gemeenschap nu praat heb ik niet uitgezocht.

## De vier eisen van een 8
1. Nieuwe kleine makers verdienen er nu: **nee, niet aangetoond.** Geen betalen in de winkel, geen openbare verkoopcijfers, Linux-gebruikers staan bekend als zuinig (GOK).
2. Bereik voor nieuwkomers: **ja, sterk** (zie boven, met de kanttekening over updates).
3. Wij kunnen bouwen en testen: **ja, sterk.** Wij werken zelf op Linux in de cloud, Flatpak bouwen kan in GitHub Actions, en Flathub keurt via een pull request op GitHub (flathub/flathub). Een eerste app kan binnen 2 weken.
4. Thijs kan binnen een week verkopen: in de winkel nee (bestaat niet); met eigen kassa (Lemon Squeezy, Polar of Gumroad) ja, maar dan is Flathub alleen etalage. Verificatie van de app gaat via GitHub of een eigen website, geen ID nodig (GOK, niet nagelezen).

## Eerste idee als het opengaat
Een klein betaald hulpprogramma dat op Linux ontbreekt en op de Mac wel verkoopt (denk aan een Mac-app uit onze TrustMRR-lijst), of een eenvoudig betaald spel. Zolang betalen niet in de winkel zit: gratis app met een eenmalige Pro-sleutel via eigen kassa. GOK: weinig omzet.

## Cijfer: 4. Advies: nog niet klaar
Bereik en bouwen zijn bijna perfect voor ons, geld ontbreekt. Wordt Flathub-betalen echt geopend, dan wordt dit meteen een serieuze kandidaat, want dan zijn wij er vroeg bij in een winkel waar nieuwkomers wel gevonden worden.

**Herhaalmeting, maandelijks (eerst 14 dec 2026):** `curl https://flathub.org/api/v2/vending/config` en zoek in het nieuws van Flathub (docs.flathub.org/blog) naar betalen. Zodra er een app met een prijs is: opnieuw meten met `python3 -I data/flathub-haal-script.py uit.jsonl` en de betaalde apps apart tellen. Ook: met een controleur nagaan hoeveel van installs_last_month updates zijn (vergelijk /api/v2/stats/<app> per dag rond een release).

## Bronnen en data
- Zoek-API: POST https://flathub.org/api/v2/search met {"query":"","hits_per_page":250,"page":N}; velden added_at, installs_last_month, is_free_license.
- data/flathub-alle-apps-2026-11-14.jsonl (3.380 apps, ingekorte velden), data/flathub-haal-script.py.
- Betalen: flathub.org/api/v2/openapi.json, flathub.org/api/v2/vending/config; planet.kde.org/siosms-blog-2025-11-23-how-do-we-keep-apps-maintained-on-flathub-or-building-a-more-respectful-app-store/; itsfoss.com/news/flathub-paid-apps/ (9 dec 2024).
