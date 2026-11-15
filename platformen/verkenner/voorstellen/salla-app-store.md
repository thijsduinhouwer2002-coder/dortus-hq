# Salla App Store (Vera)

Onderzocht door Vera op 15 nov 2026, run 16:31 (Amsterdam). Vervolg op Noor (`platformen/pionier/voorstellen/salla-app-store.md`, 9 nov, cijfer 4 voor de pionier, doorgegeven aan Vera). Mijn vraag: halen nieuwe apps van kleine makers hier installs en geld?

**Cijfer 3. Advies: nee.** Geen aparte controleur: de meting is dezelfde soort als Nuvemshop van deze run (die wel is nagekeken), en twee rijen heb ik zelf live overgedaan (beide goed). Het nee volgt ook Noor.

## Wat ik zelf mat (GEZIEN, 15 nov 2026)
Alle 865 apps uit de open API `https://api.salla.dev/marketplace/v2/apps?page=N` (Noor telde 849 op 9 nov). De API geeft geen aanmaakdatum en geen installs. Daarom per app de oudste review (laatste reviewpagina, 10 per pagina) als ruwe startdatum. Dat werkt alleen voor apps met minstens één review; 368 van de 865 apps hebben er geen, hun leeftijd is onbekend. Deze maat maakt jonge lichtingen dus juist beter dan ze zijn.
Data: `data/salla-apps-2026-11-15.json`. Scripts: `data/salla-haal-script.py` (±10 minuten) en `data/salla-analyse-script.py`.

| Lichting (maand eerste review) | Apps | Mediaan reviews | 10+ | Betaald met 10+ |
|---|---|---|---|---|
| 2024 eerste helft | 43 | 8 | 20 (47%) | 10 |
| 2025 eerste helft | 45 | 7 | 14 (31%) | 12 |
| 2025 tweede helft | 59 | 5 | 19 (32%) | 9 |
| jan t/m apr 2026 | 42 | 2 | 3 (7%) | 2 |
| **mei t/m aug 2026** | **72** | **2** | **1 (1%)** | **0** |

Een deel komt door leeftijd (zie de les bij Nuvemshop), maar ook bij 7 tot 10 maanden oud (jan t/m apr) haalt maar 7% 10+ reviews. Daar komen de 368 apps zonder enkele review nog bij.

**Wie doorbreekt:** van de 15 jonge apps met de meeste reviews zijn er 6 van Salla zelf (81 apps). Losse makers: نواف حريري (gratis, 513), Madar (1.500 SAR, 141), صعودك (69 SAR per maand, 47), Mohamed Rafat (99 SAR per maand, 21). Er zijn dus een paar jonge betaalde apps met tientallen reviews, maar het zijn er een handvol.

**Buitenlandse maker:** TopSoft UG heeft hier 30 apps, vooral 36 SAR (±€ 8) per maand. Beste 94 reviews, alle apps met 10+ reviews zijn van 2022 of 2023; die van 2024 hebben er 16 of minder (GEZIEN). Dezelfde maker als bij Nuvemshop: veel apps, alleen de oudste lopen.

**Geld:** Salla rekent af en betaalt buitenlanders uit in USD of EUR, met 15% bronbelasting sinds 1 sep 2026 en paspoortverificatie (GEZIEN door Noor, salla.dev/blog). De partnersite toont "9,999,700 أرباح الشركاء" (partnerwinst) bij "+1,000 شريك" (GEZIEN, salla.partners, 15 nov). Dat ronde getal lijkt een teller met een plafond (GOK); ook als het klopt is het verspreid over meer dan 1.000 partners en jaren, en gaat het ook om thema's en doorverwijzingen. Het percentage dat Salla houdt staat achter de inlog. Geen bedrag van een kleine maker gevonden.

## Tegen de lat van een 8
1. Nieuwe kleine makers verdienen: nee, niet zichtbaar (jonge lichting 1% met 10+ reviews).
2. Bereik voor nieuwkomers: zwak, Salla zelf en oude apps boven aan.
3. Bouwen en testen: ja, gewone web-app, maar alles in het Arabisch (naam, omschrijving, plannen verplicht).
4. Thijs kan verkopen: ja, uitbetaling in EUR mag, wel paspoortverificatie (Thijs) en 15% bronbelasting.

Platform groeit niet zichtbaar (Noor: 80.000+ winkels in 2024, nu ±67.000).

## Herhaalmeting
Alleen bij een nieuw feit (zie Noor: een groot nieuw land met een eigen app-lijst). Dan `python3 -I data/salla-haal-script.py uit.json` en de analyse.
