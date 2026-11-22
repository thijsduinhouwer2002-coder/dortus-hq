# Voorstel: Creality Cloud (3D-printmodellen van Creality)

Vera, 14 nov 2026 run 11:31 (Amsterdam). Voorwerk met een eigen, maar scheve steekproef. Niet apart nagekeken.

**Cijfer: 3 (voorlopig). Advies: nee voor nu.**

## Wat het is
Creality Cloud (crealitycloud.com) is de modelsite en printapp van Creality, de grootste maker van goedkope 3D-printers. Zelfde soort als MakerWorld (Bambu Lab, cijfer 3), Printables (Prusa) en Thangs (3).

## Eigen meting (GEZIEN)
- robots.txt staat modelpagina's toe (Crawl-delay 1), zoeken (/search) niet. Elke modelpagina heeft in de paginagegevens downloads, weergaven, likes, of het betaald is, prijs en aantal betalingen (`numOfPayment`).
- De sitemap telt 170 delen van ±1.420 modellen (±240.000). Steekproef: 106 modellen die in de sitemap een wijzigingsdatum in mrt t/m aug 2026 hebben, alle 106 gemaakt in 2026 (mrt t/m aug), van 82 makers.
- Uitkomst: downloads mediaan 1.013, allemaal 100+, hoogste 11.242. **Let op: dit is scheef.** De sitemap bevat waarschijnlijk alleen gekozen of populaire modellen (Creality heeft er veel meer), dus dit zegt niets over een gewoon nieuw model. Een eerlijke steekproef vraagt een lijst van de nieuwste modellen, en zoeken mag niet volgens robots.txt.
- Betaald: 1 van de 106 (prijs 100 in de eigen eenheid, 60 betalingen). In de lijst "premium" van de site (20 modellen) was er geen enkele betaald.
- Geld voor makers loopt dus vrijwel alleen via beloningen van Creality (er bestaat een uitbetaalpagina, /cash-out, niet leesbaar). Bedragen niet gevonden.

## Waarom nee voor nu
Zelfde beeld als MakerWorld en Thangs: veel downloads voor gratis modellen, bijna niets te koop, en het geld is een beloningsprogramma van de printermaker waar we de bedragen niet van kennen. We kunnen zelf ook niet printen. Wat het zou veranderen: openbare bedragen van de beloningen, of een eerlijke steekproef die laat zien dat gewone nieuwe modellen veel downloads halen en dat die beloning per download serieus is.

Gegevens: `data/crealitycloud-steekproef-2026-11-14.json.gz`, script `data/crealitycloud-haal-script.py`.
