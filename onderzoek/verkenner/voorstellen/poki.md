# Poki, webspelportal uit Amsterdam

Onderzocht door Vera, 15 nov 2026 run 12:31 (Amsterdam). Eigen meting van alle 1.513 spelpagina's uit de sitemap (JSON-LD: maker, datePublished, ratingCount), plus een onderzoeker die de voorwaarden las en 10 willekeurige rijen nakeek (10 van 10 goed). Data: `data/poki-spellen-2026-11-15.csv`, script: `data/poki-haal-script.py`.

## Cijfers
- **Drukte:** ±14 tot 37 nieuwe spellen per maand die live staan, 241 in 2026 tot nu (GEZIEN, eigen meting). Poki noemt 227 releases in 2025 uit "countless reviews" (GEZIEN, poki.com/blog/2025-at-poki-a-year-in-review; DERDEN pocketgamer.biz). 442 makers in de catalogus, grootste Nitrome met 40 spellen.
- **Bereik (stemmen, geen plays):** spellen van 3 tot 6 maanden oud (mei tot half aug 2026, n=76): mediaan 16.721 stemmen, 75 van 76 boven 1.000, 50 boven 10.000, 11 boven 100.000. 6 tot 12 maanden (n=109): mediaan 35.378. Makers met maar 1 of 2 spellen op Poki, 3 tot 12 maanden oud (n=50): mediaan 26.550 (GEZIEN, eigen meting).
- **Stemmen naar plays:** ruwweg 1 stem per 50 tot 150 plays (DERDEN, oude Poki-cijfers naast de stemmen van nu, GOK voor de vuistregel). Een mediaan spel van 3 tot 6 maanden heeft dan ±0,8 tot 2,5 miljoen plays. Ter vergelijking: CrazyGames Full Launch mediaan 93.000 plays.
- **Valkuil:** de sitemap toont alleen spellen die live staan. Afgewezen spellen zie je niet, en spellen die alleen de web fit test haalden staan soms online zonder promotie en zonder inkomsten (GEZIEN, developers.poki.com/guide/how-testing-works). Oude datums kloppen niet (94 spellen op 2019-03-11), daarom alleen 2025 en 2026 gebruikt.
- **Geld:** maker krijgt 50% van de reclame-inkomsten bij spelers via Poki, 100% bij spelers die rechtstreeks komen (GEZIEN, developers.poki.com/guide/revenue-deal-types). Uitbetaling per bank of PayPal (GEZIEN, /payouts-billing). Bewijs van kleine makers: Steelpan Interactive, twee spellen samen "bijna zes cijfers" (DERDEN, exputer.com 13 okt 2026); Playrea, 67 miljoen plays met 5 spellen in 2025, hoofdinkomen (DERDEN). Geen openbaar bedrag per 1000 plays.
- **Toegang:** gratis indienen via een formulier, dan playtests (10 video's), player fit test (500 spelers, gemiddeld 3+ minuten), web fit test (±10.000 spelers, 3 tot 7 dagen), eindkeuring 1 tot 2 weken, daarna 2 tot 3 maanden tot de wereldwijde release (GEZIEN, developers.poki.com). Kans om live te komen niet bekend; GOK 5 tot 15% van de serieuze inzendingen.
- **Exclusiviteit:** web-exclusief, standaard 5 jaar, ook YouTube Playables en Discord vallen eronder; Steam en appwinkels blijven vrij (GEZIEN, /working-with-poki). Een spel dat al op andere sites staat krijgt alleen een eenmalig bedrag.
- **Open:** of een privépersoon zonder KvK mag tekenen. Staat niet in de openbare gids.

## Voor en tegen
- Voor: het grootste bereik dat ik tot nu toe mat voor wie erdoor komt, ook voor makers met één spel; 50% is een goed aandeel; Nederlands bedrijf; HTML5 past bij ons; de tests zijn gratis en herhaalbaar, dus we weten snel of een spel kansloos is.
- Tegen: streng filter (±230 releases per jaar); 2 tot 3 maanden tot geld; vijf jaar web-exclusief botst met de Playables-proef via Playgama voor hetzelfde spel; geen hard bedrag per 1000 plays; KvK-vraag open.

## Wat we zouden bouwen
Eén klein origineel spel met de figuren uit Het Hol (bijvoorbeeld het Gloop-arcadespel dat voor Garmin bedacht is, als webversie), sterk op de eerste 3 minuten, en dat eerst door de gratis player fit test halen. Haalt het die niet, dan gaat hetzelfde spel naar Playgama en CrazyGames. Dan is er niets verloren.

## Cijfer en advies
**Cijfer 6. Ja als kleine proef, vóór de Playables-proef met hetzelfde spel.** Volgorde: eerst Poki (gratis test, beste bereik en 50%), pas bij een nee naar Playgama of CrazyGames, omdat Poki geen spellen wil die al elders staan. Thijs hoeft voor de test niets te doen; pas bij een contract is hij nodig (en dan moet de KvK-vraag beantwoord zijn). Herhaalmeting van de catalogus kan met het script, bijvoorbeeld 15 jan 2027.
