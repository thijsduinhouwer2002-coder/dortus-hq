# Chrome Web Store met betaling (16 nov 2026, run 23:31)

Gemeten voor de nachtscan (opdracht hoofdchat 16 nov 23:15). Eerder alleen een ruwe telling via TrustMRR (8 tot 9 gebruikers, 10 tot 13%). Google heeft sinds 2021 geen eigen betaling meer; makers rekenen af via ExtensionPay (bovenop Stripe, 5% per betaling), Stripe, Lemon Squeezy of Dodo.

## Cijfers

**Bereik, eigen steekproef (GEZIEN).** 450 willekeurige winkelpagina's uit deel 0 van de 47 delen van de sitemap (chromewebstore.google.com/sitemap), 431 met gegevens. Aanmaakdatum uit een tijdstempel in de paginadata (klopt bij Zoho Assist, 2011, en Tabisto, juni 2026; dat het de aanmaakdatum is, is een afleiding).

| Groep | n | Mediaan gebruikers | 100+ | 1.000+ |
|---|---|---|---|---|
| 3 tot 6 maanden oud (16 mei tot 16 aug 2026) | 48 | 7,5 | 12% | 2% |
| Aangemaakt in 2026 | 155 | 10 | 10% | 2% |
| Alle | 431 | 36 | 36% | 22% |

- Een derde van alle vermeldingen is uit 2026: veel drukte. Maar 6,7% meldt aankopen in de extensie (GEZIEN).
- n=48 is klein, de percentages zijn grof.

**Geld (GEZIEN, TrustMRR, omzet via Stripe of Dodo gekoppeld).** Van ±12 profielen van echte Chrome-extensies gestart in 2025 of 2026 halen er 3 meer dan $100 in de laatste 30 dagen: Zumie (schermopname, 1 maker, Hongarije, gestart okt 2025, $147 laatste 30 dagen, $3.492 totaal, eenmalig $49, 0 X-volgers), Aera Browser ($260, $4.257 totaal, dec 2025), Amazon Reviews Extractor ($200, $861 totaal, apr 2026). De rest $0 tot $45.

**Geld (DERDEN, eigen meldingen van makers op r/chrome_extensions, via Arctic Shift).** Bulk Edit Google Photos $500 per maand na 3 maanden, winkel is de grootste bron; MeetAssist $993 per maand met 232 betalers na ±1 jaar; Locksy Pro $302 in 3,5 maand; Wapes (WhatsApp Web) $217 in week 1, $500 na 2 maanden; Broken Link Checker $174 eerste betaalde maand bij 4.000 gebruikers; DeepRead $25 na 5 maanden. ExtensionPay zegt "over $800k" uitbetaald aan alle makers samen (GEZIEN, github.com/Glench/ExtPay).

**Tijd tot de winkel (GEZIEN, developer.chrome.com/docs/webstore).** Keuring "within a few days, but it can take up to a few weeks". Eenmalige registratie ($5, DERDEN), Google-account, e-mail verifiëren, bij verkopen een fysiek adres (staat bij Thijs, nooit in de repo) en een Stripe-account.

**Bouwen en testen in de cloud (GEZIEN).** Een uitgepakte MV3-extensie laadt in Chromium of Chrome for Testing met Playwright, headless=new; service worker en content script draaiden. Script: `data/chrome-web-store-laadtest-script.py`.

## Leemtes
1. Opvolgers van extensies die met Manifest V2 verdwenen (sinds 31 aug 2026 allemaal uit de winkel, GEZIEN). Al opvolgers voor Selenium IDE en Pushbullet (DERDEN), dus snelheid telt.
2. Bulkacties in Google-producten die dat zelf niet kunnen (Bulk Edit Google Photos, DERDEN).
3. WhatsApp Web-hulp voor kleine bedrijven: veel betalers, maar veel concurrentie en risico met de voorwaarden van WhatsApp.

## Voor en tegen
- Voor: snel in de winkel, alles in de cloud te bouwen en testen, kopers bestaan, eenmalig $5, geen KvK zichtbaar nodig.
- Tegen: een gewone nieuwe extensie haalt na 3 tot 6 maanden 7,5 gebruikers (mediaan), en betaald wordt pas bij honderden tot duizenden gebruikers. Geld komt vooral bij makers die een gat in een groot product (Google, WhatsApp, Amazon) vinden en daar zelf verkeer naar sturen.

## Eerste idee
Een kleine betaalde bulkactie voor een Google-product dat het zelf niet kan, of een snelle opvolger van een verdwenen MV2-extensie met veel gebruikers. Eerst de lijst van verdwenen MV2-extensies met 100.000+ gebruikers zonder opvolger maken.

## Cijfer en advies
**Cijfer 4. Nee als hoofdplatform, wel bruikbaar als snelle kleine proef.** Bereik 3 (mediaan 7,5, 12% 100+), geld 5 (aantoonbaar maar klein en traag), past 7 (in dagen te bouwen en testen). Herhaalmeting rond 16 feb 2027: dezelfde scripts op een nieuw deel van de sitemap, lichting nov 2026 t/m jan 2027.

Data: `data/chrome-web-store-steekproef-2026-11-16.csv`, `data/chrome-web-store-trustmrr-2026-11-16.tsv`, `data/chrome-web-store-analyse-2026-11-16.txt`, scripts `data/chrome-web-store-steekproef-script.py` en `-analyse-script.py`.
