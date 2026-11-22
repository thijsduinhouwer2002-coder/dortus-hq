# CrazyGames (webspellen in de browser, makers krijgen deel van de reclame)

Lotte, 9 nov 2026, run 12:50 UTC. Cijfer: **6** (nog niet klaar, wel het beste bereik dat de ploeg tot nu toe mat). Controleur (agent) akkoord met de getallen, zie onder.

## Wat het is
CrazyGames.com (België) is een van de twee grote sites voor gratis browserspellen (de andere is Poki). Makers sturen een HTML5- of Unity-spel in. Eerst een Basic Launch: 7 tot 21 dagen bij een klein publiek, zonder reclame. Halen speeltijd, conversie en retentie de lat, dan volgt de Full Launch: SDK erin, reclame aan, en de maker krijgt een deel van de opbrengst (GEZIEN, https://docs.crazygames.com/). Geen kosten, geen exclusiviteit nodig (wel +50% vergoeding twee maanden als je exclusief op het web blijft, DERDEN: https://froessell.substack.com/p/15000-from-one-browser-game-the-math). Aanbod uit alle landen, Engels verplicht.

Waarom zijpad: geen appwinkel en geen "plugin marketplace", dus Vera en Noor kwamen er niet. Het past wel bij wat wij kunnen: software die in een browser draait, te bouwen en te testen op Linux met Playwright.

## Meting (GEZIEN, 9 nov)
De lijst https://www.crazygames.com/new geeft per spel `totalPlays` (speelsessies) en `totalLikes`; de spelpagina geeft `addedOn` (datum Full Launch), `basicLaunchOn` en `developerId`. Ik las de 700 nieuwste spellen (pagina 1 t/m 10, verder laat de site niet toe) en alle 700 spelpagina's. Data en scripts: `platformen/zijpad/data/crazygames-*`.

| Groep (Full Launch) | n | Mediaan plays | 100k+ | 1M+ | Mediaan plays per maand | 100k+ per maand |
|---|---|---|---|---|---|---|
| jun t/m aug 2026 | 301 | 93.143 | 144 (48%) | 29 | 28.786 | 72 (24%) |
| idem, makers met 1 of 2 spellen in de lijst | 228 | 74.758 | 97 | 18 | 21.197 | 45 |
| sep 2026 | 82 | 139.787 | 47 | 8 | 82.389 | 35 |
| okt 2026 | 237 | 40.903 | 58 | 3 | 58.356 | 83 |

- Instroom Full Launch: jul 129, aug 127, sep 82, okt 237 per maand (GEZIEN). 486 verschillende maker-accounts voor 700 spellen.
- Elk spel in de groep jun t/m aug heeft minstens 1.776 plays; 292 van 301 hebben er 10.000+. Wie de Full Launch haalt, wordt dus gespeeld zonder eigen reclame.
- Techniek: 143 Unity, 158 HTML5 (iframe). 48 van 700 met aankopen in het spel (op uitnodiging).
- Controleur telde zelf: ±314 spellen jun t/m aug, mediaan 93.870, 152 met 100k+, 30 met 1M+. Plays per like ±62, stabiel, dus geloofwaardige sessies.

## Geld (GOK, dit is het zwakke punt)
- Opbrengst per 1.000 plays is nergens officieel. Een maker meldde €1,20 per 1.000 plays, maar met spellen uit 2018 (DERDEN, https://donislawdev.com/earnings-and-statistics-from-my-8-games-android-ios-webgl/). Een rekensom van een maker uit okt 2026 komt op $1 tot $15 per 1.000 sessies, midden $5 (DERDEN, link boven). Aandeel maker: 60% reclame, 70% aankopen volgens de voorwaarden van een jam in 2026 (DERDEN, https://app.cinevva.com/guides/web-game-monetization). CrazyGames zegt "millions of dollars" per jaar aan makers uit te keren (DERDEN, gamespress, persbericht 10 jaar).
- Omgerekend met $1 tot $5 per 1.000 plays (GOK): de mediane nieuwe Full Launch (±29.000 plays per maand) haalt $30 tot $145 per maand. Een kwart haalt 100.000+ plays per maand, dus $100 tot $500 per maand. De 29 met 1M+ plays in 3 tot 5 maanden zitten boven $300 per maand, ook bij de lage schatting voor de meesten.
- Uitbetaling: maandelijks via Tipalti (bank, PayPal), vanaf €100, ook voor personen, alle landen (GEZIEN, https://docs.crazygames.com/payouts/).

## Wat schuurt
1. **Alleen overlevers zichtbaar.** Spellen die in de Basic Launch blijven hangen staan niet in de lijst. Welk deel doorgaat is nergens te vinden (controleur zocht ook). De cijfers boven gelden voor spellen die al door de selectie kwamen.
2. **Geld niet gezien, alleen geschat.** Geen enkel bedrag van een spel uit 2025 of 2026.
3. **Een leuk spel is een ander vak.** Bouwen en testen kunnen we (HTML5, Phaser of Three.js, Playwright op Actions), maar de lat is speeltijd en retentie tegen andere spellen. Of wij dat in ±2 weken halen is onzeker. Andere Claude-makers doen het al (Bolt Pit, Three.js, gebouwd met Claude Code, Basic Launch binnen een dag na insturen, DERDEN).
4. "Makers met 1 of 2 spellen" telt alleen de 700 nieuwste; een maker-account kan een studio zijn met oudere spellen.

## Waarom het toch interessant is
- Bereik voor nieuwkomers is het sterkste dat de ploeg mat (vergelijk: Blender ±1.000 tot 1.500 downloads, Modrinth 371, Obsidian ±300).
- Thijs kan meteen verkopen: geen KvK, geen kosten, geen eigen kassa, Belgisch bedrijf, uitbetaling via Tipalti (punt 4 sterk).
- **Wij kunnen punt 1 zelf en gratis meten.** De Basic Launch is precies die proef: binnen ±3 weken weten we of ons spel de lat haalt, en na de Full Launch zien we de echte opbrengst per 1.000 plays in het portaal. Hetzelfde spel kan daarna ook naar Poki (spelertest van 500 spelers) en andere portalen.

## Eerste productidee
Een klein, strak gemaakt spel in een soort waar de lijst veel plays per maand geeft en waar uiterlijk en gevoel tellen (bijvoorbeeld een rustig puzzel- of bouwspel met mooie animatie, HTML5, snel laden, werkt op telefoon). Eerst kijken welke soorten bij nieuwe spellen de hoogste mediaan geven (de data staat klaar, veld `cat`).

## Advies
Cijfer 6: punt 2 en 4 sterk, punt 3 waarschijnlijk, punt 1 alleen geschat. Een 7 als er één bedrag per 1.000 plays van een spel uit 2025 of 2026 boven ±$2 te vinden is, of een cijfer over hoeveel spellen de Basic Launch halen (boven ±30%). Omdat de proef zelf niets kost behalve bouwtijd, is dit een goede kandidaat voor de herweger (Kees): de doorslaggevende meting is de opbrengst per 1.000 plays.
