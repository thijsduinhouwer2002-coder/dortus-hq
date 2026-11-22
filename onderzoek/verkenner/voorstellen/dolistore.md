# Voorstel: DoliStore (modules voor de ERP/CRM Dolibarr)

Vera, 14 nov 2026, run 17:31 (Amsterdam). Advies: **nee, cijfer 3.** Niet apart nagekeken: het oordeel hangt aan de jaarcijfers van de stichting, die hieronder letterlijk staan.

## Wat het is
Dolibarr is open-source software voor boekhouding, offertes, voorraad en klanten, vooral bij kleine bedrijven en zzp'ers in Frankrijk, Spanje, Italië, België en Noord-Afrika. De stichting achter Dolibarr runt DoliStore, waar makers modules verkopen. De stichting rekent af, betaalt de btw en houdt 20%; de maker krijgt 80% (GEZIEN, dolistore.com/terms-and-conditions.php, 14 nov). Iedereen met een account mag verkopen, zonder lid te zijn. Keuring minstens 2 weken. Een verkoop is pas na 1 maand definitief.

## Cijfers
- **Totale omzet van de winkel** (GEZIEN, jaarverslagen van de stichting op wiki.dolibarr.org, "Gains DoliStore", exclusief btw): 2022 € 475.852, 2023 € 436.827, 2024 € 452.157, 2025 € 457.924 (+1,3%). Uitbetaald aan makers 2025: € 371.219. **Vlak sinds 2022**, ±€ 38.000 per maand voor de hele winkel.
- **Aanbod** (GEZIEN, categoriepagina's 14 nov): 2.093 modules, plus 205 skins en sjablonen. Gemiddeld ±€ 220 omzet per module per jaar. Als ±300 makers verkopen (GOK), is dat ±€ 1.200 tot 1.500 per maker per jaar, net als bij Fab.
- **Gebruikers** (DERDEN, wiki.dolibarr.org/FAQ_Who_uses_Dolibarr): schatting van de stichting ±200.000 organisaties wereldwijd, ±100.000 in Frankrijk. Downloads van de hoofdserver ±4.200 per week (2025).
- **Verkopen per module: niet zichtbaar.** Productpagina's tonen prijs, auteur, versie, datum van de laatste versie en compatibiliteit, maar geen verkopen, downloads of reviews (GEZIEN, 49 pagina's van de nieuwste ids). De id's zijn bij de verhuizing naar de nieuwe winkel (2025/2026) opnieuw uitgedeeld, dus ook de leeftijd van een module is niet uit de pagina te halen. Bereik en geld van nieuwe kleine makers zijn daardoor **niet zelf te meten**. Dat kan alleen met verkoopcijfers van een maker zelf (het verkopersdashboard).
- **Prijzen**: betaalde modules in de steekproef € 75 tot € 450, mediaan € 279 (GEZIEN, n=7 met leesbare prijs).
- **Opvallend**: van de 49 nieuwste pagina's zijn er 17 van één maker en 9 van een tweede (GEZIEN). Er zijn dus al makers die in hoog tempo modules uitbrengen, vermoedelijk met hulp van AI (GOK).

## Voor
- Echt geld: de winkel rekent af, 80% voor de maker, kopers zijn bedrijven die € 100 tot € 450 per module betalen.
- Past technisch bij ons: PHP-modules, te testen op Linux met een Dolibarr in Docker op GitHub Actions.
- Geen grote spelers aan de top, wel veel kleine Franse bureaus.

## Tegen
- **De hele markt is klein en groeit niet**: ±€ 458.000 per jaar voor 2.093 modules. Zelfs 10% van alles is ±€ 3.800 per maand, en dat haal je niet als nieuwkomer.
- Geen enkele maat voor bereik of verkopen per product: we zouden blind bouwen.
- Modules moeten onder GPL (open broncode). Kopers mogen de code doorgeven.
- Kopers verwachten steun in het Frans, en bedrijfssoftware raakt aan boekhoudregels per land.
- Concurrerende winkels (bijvoorbeeld dolimarketplace.com) en verkoop via eigen sites splitsen de markt verder.

## Wat we er zouden bouwen
Een module die een terugkerende ergernis oplost, bijvoorbeeld een modern dashboard of een bankkoppeling. Maar zonder verkoopcijfers weten we niet welke soort verkoopt.

## Advies
Nee, cijfer 3. Geld is aantoonbaar op winkelniveau, maar klein en vlak, en niet per maker te meten. Dortus kan hier geen grote speler worden. Opnieuw bekijken als de stichting verkoopcijfers per module openbaar maakt, of als de jaaromzet van de winkel duidelijk gaat groeien (jaarverslag 2026, rond maart 2027).

## Bronnen
- https://www.dolistore.com/terms-and-conditions.php (regels, 80/20, GPL)
- https://wiki.dolibarr.org/index.php/Fiscal_Report_/_Rapport_Financier_2025 (en 2024, 2023, 2022)
- https://wiki.dolibarr.org/index.php/FAQ_Who_uses_Dolibarr
- https://wiki.dolibarr.org/index.php/Statistics
- Script en ruwe data: `data/dolistore/haal.py`, `data/dolistore/producten-2026-11-14.json`
