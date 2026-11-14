# Voorstel: WHMCS Marketplace (modules voor hostingbedrijven)

Vera, 14 nov 2026, run 17:31 (Amsterdam). Advies: **nee, cijfer 2.** Niet apart nagekeken (nee, en de cijfers staan in de data).

## Wat het is
WHMCS is de factuur- en klantsoftware die veel hostingbedrijven gebruiken. Op marketplace.whmcs.com staan modules van derden: betaalmodules, koppelingen met registrars, thema's, hulpmiddelen.

## Cijfers
- **De marketplace is een etalage, geen kassa.** Plaatsen is gratis; bij een betaalde vermelding geeft de maker "a direct link to the checkout process" op zijn eigen site (GEZIEN, marketplace.whmcs.com/help/developer, 14 nov). WHMCS rekent niet af en betaalt niets uit. Wij zouden dus zelf moeten verkopen, met licenties, btw en een eigen kassa.
- **Eigen steekproef** (GEZIEN, 14 nov): alle 181 vermeldingen uit de lijst "New" (9 pagina's, ids 7909 tot 9294). 119 betaald, 62 gratis. Van de 119 betaalde: mediaan 0 reviews, 12 (10%) met 1 of meer, 2 met 5 of meer. Reviews zijn hier zeldzaam (een bekende module van de grootste maker heeft er 9), dus het is een zwakke maat; verkopen zelf zijn niet zichtbaar.
- **Wie er nieuw plaatst**: vooral hostingbedrijven die hun eigen dienst aanbieden (TIVRO 10, HosTwega 9, Provonic 7, OneSystems 6). De nummer één onder de echte modulemakers is ModulesGarden, een bureau met honderden modules: sterk en goed bijgewerkt.
- **Kopers**: hostingbedrijven, dus zakelijke inkoop met support- en licentie-eisen.

## Voor
- Technisch haalbaar: PHP-modules, te testen in Docker.
- Prijzen per module zijn hoog genoeg ($30 tot $200+).

## Tegen
- Geen kassa en geen uitbetaling via WHMCS: geld via de marketplace is niet aan te tonen en niet te meten.
- Sterke nummer één (ModulesGarden) en veel hostingbedrijven die alleen reclame voor zichzelf maken.
- Nieuwe betaalde modules krijgen bijna geen reacties.
- Kleine markt met zakelijke kopers; past slecht bij "Thijs kan binnen een week verkopen".

## Advies
Nee, cijfer 2. Niet opnieuw bekijken tenzij WHMCS zelf gaat afrekenen en uitbetalen.

## Bronnen
- https://marketplace.whmcs.com/help/developer
- https://marketplace.whmcs.com/category/new
- Script en data: `data/whmcs/haal.py`, `data/whmcs/producten-new-2026-11-14.json`
