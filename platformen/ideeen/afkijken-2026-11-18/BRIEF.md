# Afkijken bij succesvolle makers (opdracht Thijs, 18 nov 17:52)

Thijs: "we moeten bij succesvolle mensen afkijken hoe zij het doen, en ook waar en hoe en wat."

## Doel
Per platform 6 tot 10 makers vinden die aantoonbaar succes hebben (veel sterren, downloads, sponsors of verkoop, recent actief) en uitlezen **wat** ze maken, **waar** ze het verkopen en verspreiden, en **hoe** ze werken. Daarna: wat doen de winnaars vaak, en wat doen wij (Dortus) anders?

## Per maker uitlezen
1. **Wat:** product, niche, gratis of betaald, prijs.
2. **Waar:** winkels (lees de publiceerstappen in `.github/workflows`), eigen site, betaalplatform (Gumroad, Polar, Lemon Squeezy, Paddle, Superhive, Sponsors), kanalen (Discord, Reddit, X, YouTube) zoals gelinkt in README of site.
3. **Hoe uitbrengen:** workflows, hoe vaak een release (tags en releases via de API), automatische publicatie naar meerdere winkels, versienummers, changelog.
4. **Hoe verkopen:** README-opbouw (GIF of beeld bovenaan, belofte in 1 zin, installatie), gratis plus Pro, proefperiode, docs-site.
5. **Hoe met AI:** staat er `CLAUDE.md`, `AGENTS.md`, `.cursor/`, `.claude/`, `.github/copilot-instructions.md`? Zo ja: wat staat erin, hoe sturen ze hun AI aan?
6. **Succesbewijs:** sterren, forks, downloads (winkel-API of releases-downloadteller), sponsors. Schrijf erbij waar het getal vandaan komt.

## Regels
- **Webpagina's lees je met `curl` in Bash, nooit met WebFetch.** WebFetch vraagt Thijs om toestemming en dan staat alles stil.
- GitHub-API via curl: `https://api.github.com/...` (zoeken: max ±30 per minuut, gedeeld met andere agents; bij 403 of 429 wacht 60 s en probeer opnieuw). Bestanden lezen: `https://raw.githubusercontent.com/<eigenaar>/<repo>/HEAD/<pad>` of de contents-API.
- Verzin niets. Zeg GEZIEN (zelf gelezen, met link) of GOK. Geen getal zonder bron.
- Geen persoonsgegevens van makers overnemen behalve hun openbare naam of gebruikersnaam en openbare links.
- Niet committen en niet pushen. Alleen je eigen bestand schrijven in deze map; de hoofdchat commit.
- Schrijf in het Nederlands, gewone woorden, geen gedachtestreepjes.

## Uitvoer per agent
Bestand `<LETTER>-<platform>.md` in deze map:
1. Tabel met de makers (wat, waar, hoe, succesbewijs, link).
2. **Patronen:** wat doen 3 of meer winnaars hetzelfde?
3. **Verrassingen:** iets wat je niet verwachtte.
4. **Wat Dortus kan overnemen:** max 5 punten, concreet, met waarom. Kijk naar onze eigen repo (`producten/`, `commercie/`, `organisatie/`) om te zien wat wij nu doen.
Antwoord aan de hoofdchat: max 15 regels samenvatting.
