# Voorstel: Mac App Store, kleine hulpprogramma's

Vera, verkenner, 7 nov 2026 run 21:33 UTC (derde stuk). Advies: **nee. Cijfer 2.** Nagekeken door een controleur: akkoord, 3 kleine correcties verwerkt (steekproef 5 van 5 gelijk).

## Waarom bekeken
Kleine Mac-hulpprogramma's (menubalk-apps, klembord, focus) zijn een bekende plek voor solo-makers, Apple rekent af en houdt 15% voor makers onder $1 miljoen per jaar (DERDEN, Apple Small Business Program, algemeen bekend, niet opnieuw gelezen). Niet eerder onderzocht.

## Hoe gemeten (GEZIEN)
- Open iTunes-zoek-API (`itunes.apple.com/search`, entity macSoftware, winkel VS), 52 zoekwoorden (menubalk, klembord, focus, timer, notes, pdf, ai, vpn, ...), 200 resultaten per woord. 6 woorden gaven 403 (te snel achter elkaar). Samen **5.769 verschillende Mac-apps**. Script `data/macappstore-haal-script.py`, data `data/macappstore-zoek-2026-11-07.json`.
- Per app: prijs, releasedatum, aantal ratings in de VS (userRatingCount), maker.
- **Grenzen:** (1) De zoek-API geeft eerst populaire apps, dus nieuwe apps met weinig ratings vallen er eerder uit: de cijfers zijn eerder te goed dan te slecht. (2) Mac-gebruikers geven weinig ratings; een app met 0 ratings kan toch iets verkopen. Een omrekening van ratings naar verkopen voor de Mac vond ik niet. (3) "Gratis" bevat apps met een abonnement in de app; dat ziet de API niet. (4) Alleen de VS.

## Cijfers (GEZIEN)
Lichting uitgekomen mei t/m aug 2026:
| | Aantal | Mediaan ratings | 75% | 90% | 1+ | 10+ |
|---|---|---|---|---|---|---|
| Betaald (vooraf betalen) | 72 | 0 | 0 | 1 | 15% | 0% |
| Gratis (soms met abonnement) | 684 | 0 | 1 | 5 | 34% | 6% |

Mediaanprijs betaald: $3,99. Ter vergelijking mei t/m aug 2025, die een jaar langer de tijd had: betaald 33 apps, mediaan 0, 3% met 10+ (hoogste 10); gratis 11,6% met 10+. Ook met meer tijd blijft het dus laag.

De beste nieuwe apps zijn gratis: een notitie-app (Mononote, 422), een takenapp (Unforgetful, 252), en verder vooral VPN's en AI-apps.

## Drukte (GEZIEN, binnen deze zoekresultaten)
Nieuwe apps per maand in de steekproef: 2025 ±35 tot 80, 2026 jan 102, apr 167, jul 214, okt 164. Ruim verdubbeld in een jaar (deels door AI-apps). Voor de hele winkel ligt het hoger; dit is alleen wat de zoekwoorden vonden.

## Vindbaarheid
Zoeken in de winkel en Apple-uitlichting. Bij Mac-apps komt bereik in de praktijk vooral van buiten de winkel (eigen site, Product Hunt, Reddit, Setapp) (GOK, gangbaar beeld bij Mac-makers). Dat is het omgekeerde van wat Dortus nodig heeft.

## Past het bij ons
Bouwen in Swift kan, maar we hebben geen Mac om te bouwen en te testen buiten GitHub Actions (macOS-runners bestaan). Apple vraagt $99 per jaar en een ontwikkelaarsaccount van Thijs.

## Cijfer en advies
**Cijfer 2. Nee.** Zelfs met een steekproef die nieuwe apps te gunstig laat zien, haalt geen enkele nieuwe betaalde Mac-app uit mei t/m aug 10 ratings, en 85% heeft er nul. Let wel: 0 ratings op de Mac betekent niet 0 verkopen, want Mac-gebruikers geven weinig ratings. Maar er is ook geen bewijs van geld bij kleine makers binnen de winkel. Vergelijk Steam bureaublad-apps: 54% met 10+ reviews (GEZIEN, `voorstellen/steam-bureaublad.md`; reviews op Steam en ratings op de Mac zijn wel een ander soort maat).

Wat dit verandert: een betrouwbare verhouding ratings naar verkopen voor Mac-apps die laat zien dat 0 tot 1 rating toch honderden verkopen betekent, of openbare omzetcijfers van kleine Mac App Store-makers uit 2026.
