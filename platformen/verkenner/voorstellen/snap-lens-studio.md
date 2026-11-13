# Voorstel: Snap Lens Studio (AR-lenzen voor Snapchat)

Vera, 13 nov 2026, run 18:31 (Amsterdam). Nagekeken door een controleur: akkoord, 3 correcties verwerkt.

## Kort
**Cijfer 4, nee voor nu.** Snap betaalt makers van lenzen aantoonbaar, en meer dan de meeste winkels die we zagen. Maar het bereik van een nieuwe lens is van buitenaf niet te meten, het geld zit bij een kleine bovenlaag, en het past slecht bij ons: Lens Studio draait niet op Linux, publiceren en uitbetalen lopen via het persoonlijke Snapchat-account van Thijs, en wij kunnen een lens niet zelf op een telefoon testen. Geen 8.

## Wat het is
Makers bouwen AR-lenzen (filters, spelletjes, 3D-figuren op je gezicht of in de kamer) in Lens Studio of in Easy Lens (lens maken met tekstopdrachten, app en web). Snap betaalt via Lens Creator Rewards, sinds 16 okt 2025 in twee delen (GEZIEN, developers.snap.com/lens-studio/monetization/lens-creator-rewards):
- **Top Performer Payouts:** een lens die binnen 90 dagen 15.000 unieke plaatsers haalt uit 11 landen (Nederland erbij), krijgt een bedrag na afloop van die 90 dagen. Hoe hoog staat nergens ("proprietary payment formula"). GEZIEN
- **Lens+ Payouts:** alleen voor goedgekeurde makers (aanmelden). De lens wordt Exclusive, alleen voor betalende abonnees van Lens+ en Platinum. Per maand een Lens+ score van minstens 100, geld naar rato uit een vaste pot, geen maximum, kan maandenlang lopen. GEZIEN
- Meedoen vanaf 18 jaar in 42 landen, Nederland erbij. Uitbetalen aan een privépersoon mag, geen KvK nodig. Lenzen van een Business Account krijgen niets. Opnemen vanaf $100; uitbetaling via een betaaldienst (volgens een helppagina Hyperwallet), buiten de VS met een W-8BEN. GEZIEN (voorwaarden Top Performer, geldig vanaf 9 jan 2026)
- De voorwaarden zeggen zelf in hoofdletters: "ONLY A SMALL PERCENTAGE OF CREATORS ... WILL RECEIVE PAYMENTS". GEZIEN

## Cijfers
| Wat | Waarde | Label |
|---|---|---|
| Uitbetaald via Top Performer, totaal tot 21 nov 2025 | meer dan $1 miljoen | GEZIEN (ar.snap.com/blog/monetizing-with-snap) |
| Uitbetaald via Lens+ in juni 2026 | bijna $1 miljoen aan meer dan 1.000 makers; ruim 100 boven $1.000, toppers boven $10.000 in één maand; honderden eerste betalingen | DERDEN (influencermarketinghub.com, 29 jul 2026, zonder link naar Snap; eigen bericht van Snap niet gevonden) |
| Makers en lenzen | 400.000+ makers, 4 miljoen+ lenzen (maart 2025); 350 miljoen mensen per dag gebruiken lenzen | DERDEN (Snap zelf, ar.snap.com) |
| Lenzen in de openbare lens-sitemap | 624.071 unieke | GEZIEN |
| Steekproef van 300 willekeurige lenzen uit die sitemap | 91 (30%) geven nu 404, 5 zijn van Snap zelf | GEZIEN |
| Van 193 makers in die steekproef | 145 (75%) tonen 0 volgers op hun openbare profiel; 51 profielen tegelijk aangemaakt in sep en okt 2024 (lijkt automatisch) | GEZIEN; of 0 een echte nul is, is niet te bewijzen |
| Gebruik per lens (views, plaatsers) | staat nergens openbaar | niet te meten |
| Nieuwe lenzen per maand | geen officieel cijfer; ±33.000 als gemiddelde over 10 jaar | GOK |
| Kans op geld | ±1.000 ontvangers per maand van 400.000+ makers, dus ±0,25% | GOK op DERDEN |

## Bereik
Van buitenaf niet te meten. Lenspagina's tonen geen gebruik, profielen alleen volgers, en bij de meeste makers staat daar niets. Wel zien we dat 30% van de lenzen in de sitemap inmiddels weg is: veel lenzen verdwijnen weer. Nieuwe lenzen worden gevonden via zoeken en Lens Explorer (tags, naam, icoon, preview; kleiner dan 8 MB krijgt meer verspreiding), en Lens+-lenzen krijgen 48 uur proefpubliek. Echt meten kan alleen met een makersaccount (statistieken in My Lenses), dus via Thijs.

## Geld
Beter dan bijna alles wat we zagen: een vaste pot van rond $1 miljoen per maand (DERDEN) en ruim 100 makers met meer dan $1.000 in een maand. Maar het is een pot, geen verkoop: Snap bepaalt de verdeling, kan hem verkleinen, en de meeste makers krijgen niets.

## Past het bij ons
Slecht.
- Lens Studio draait alleen op Windows 11 en macOS 12+, niet op Linux (GEZIEN, ar.snap.com/download, versie 5.24.1). Er is een MCP-server zodat Claude Code Lens Studio kan besturen, maar Lens Studio moet dan op een Windows- of Mac-computer draaien.
- Easy Lens werkt op het web, maar met tekstopdrachten in een ingelogd account: dat is Thijs die klikt, niet de ploeg. Easy Lens-lenzen kun je na publicatie niet meer bijwerken.
- Publiceren, statistieken en uitbetalen gaan via het persoonlijke Snapchat-account van Thijs, met identiteitscontrole.
- Testen in de echte app kan alleen op een telefoon met Snapchat. Onze GitHub Actions-test kan dat niet.
- Wel goed: onze Blender-figuren (Gloop en de dieren van Ebb) passen bij 3D-lenzen, AI-hulp is toegestaan (Snap moedigt het aan), en er is geen KvK nodig.

## Eerste idee als het ooit ja wordt
Een kleine reeks 3D-lenzen met Gloop uit Het Hol (Gloop op je hoofd, Gloop die je gezicht opeet), gebouwd in Blender en Lens Studio, als reclame voor Het Hol en met kans op Top Performer. Lens+ alleen als we merken dat mensen ze gebruiken.

## Advies
Nee voor nu, cijfer 4 (geld 6, bereik niet te meten, past 2). Zou omhoog gaan als:
1. Snap een Lens Studio-versie of command line voor Linux of de cloud uitbrengt, of een manier om zonder ingelogde app te publiceren; of
2. Thijs een Windows-computer wil laten gebruiken door een manager (dat besluit ligt bij Hans en Thijs); en
3. er openbare gebruikscijfers per lens komen.
Herhaalmeting: na Lens Fest 2026 (meestal december) de nieuwsberichten van Snap lezen: nieuwe uitbetaalcijfers, Linux of web.

## Bronnen (gelezen 13 nov 2026)
- https://developers.snap.com/lens-studio/monetization/lens-creator-rewards
- https://developers.snap.com/lens-studio/monetization/lens-creator-rewards/top-performer-payouts
- https://developers.snap.com/lens-studio/monetization/lens-creator-rewards/lens-plus-payouts
- https://www.snap.com/terms/lens-creator-rewards-terms
- https://ar.snap.com/lens-creator-rewards
- https://ar.snap.com/blog/monetizing-with-snap
- https://influencermarketinghub.com/snapchat-makes-lens-creators-the-foundation-of-its-ar-strategy/
- https://ar.snap.com/download
- https://developers.snap.com/lens-studio/features/lens-studio-ai/developer-mode/with-claude-code
- https://developers.snap.com/lens-studio/features/lens-studio-ai/easy-lens/creator-growth-and-discovery
- Eigen steekproef: `data/snap-lenzen-steekproef-script.py` (300 lenzen uit www.snapchat.com/lens/sitemap-0 t/m 12; robots.txt staat Claude-User toe, ClaudeBot niet; rustig, 2 tegelijk). De ruwe uitkomst met gebruikersnamen van anderen staat niet in de repo.
