# Voorstel: Odoo Apps Store (betaalde modules voor Odoo)

Vera, 8 nov 2026 run 03:33 UTC. Controleur akkoord (30 van 30 live gelijk, plus 80 kaartjes), correcties verwerkt.

## Advies: nee, cijfer 3

Er is echt geld in deze winkel en elke kaart toont openbaar hoeveel keer een module verkocht is, ook vorige maand. Maar een gewone nieuwe betaalde module verkoopt bijna nooit: van de echt nieuwe modules uit juni t/m augustus 2026 heeft 94% nul aankopen en de beste haalt er 3. Het geld zit bij een kleine groep oude spelers en een paar vroege makers met een sterk thema.

## Wat het is
- apps.odoo.com: winkel voor modules (Python) voor de bedrijfssoftware Odoo. Odoo rekent af en betaalt de maker uit.
- Maker krijgt 70%, Odoo 30%. Minimumprijs 9 EUR, eenmalige koop per Odoo-versie. Uitbetaling maandelijks per SWIFT zodra er 400 EUR openstaat, met een factuur van de maker (dus een eenmanszaak of BV nodig, GOK). Geen keuring vooraf, geen regel over AI-code. Prijs moet de laagste zijn die je ergens vraagt, 2 maanden terugbetaalrecht. DERDEN: https://apps.odoo.com/apps/vendor-guidelines, https://apps.odoo.com/apps/sales-conditions, https://apps.odoo.com/apps/faq
- Modules van derden draaien niet op Odoo Online (de SaaS-versie), alleen op Odoo.sh en eigen servers. Dat maakt de markt kleiner. DERDEN (sales-conditions)
- Volgorde in de lijst: een score van 5 punten (icoon, omslag, licentie, rating boven 3, HTML-beschrijving), daarna bestsellers. Nieuwe modules komen dus achteraan bij de vele andere met dezelfde score. DERDEN (vendor-guidelines)

## Cijfers

### Drukte
- Betaalde modules met een 19.0-versie: 2.493 lijstpagina's van 20, ±49.800 stuks. Met een 20.0-versie al ±29.000, alle betaalde samen ±71.600 (3.582 pagina's). GEZIEN
- Het interne module-ID loopt tussen juni en oktober 2026 met ±850 tot 1.100 per dag op (alle versies, ook gratis en overgezette). GOK, afgeleid uit OCA-merges

### Geld, alle betaalde modules met een 19.0-versie
Steekproef: elke 10e lijstpagina, 250 pagina's, 4.998 kaartjes (GEZIEN, data/odoo/lijst19.json). Aankopen zijn het totaal over de hele levensduur en alle versies samen.
- Mediaan 0 aankopen. 69% heeft er 0, 10,9% 10+, 1,5% 100+. GEZIEN
- Maar 3,2% had vorige maand minstens één verkoop, 0,3% vijf of meer. GEZIEN
- Mediaanprijs $54,74 (bij 1,1% van de kaartjes las het script geen prijs). GEZIEN
- Omzet vorige maand in de steekproef (prijs keer verkopen vorige maand): de 10 grootste makers hebben 87%. Emipro (Shopify- en WooCommerce-koppelingen) alleen al ±$40.000. GEZIEN, ruwe schatting want prijs is de lijstprijs
- 911 makers in de steekproef. Grote bureaus met honderden modules (Probuse, Pokutsoft, Cerevantix, Softhealer, BrowseInfo). GEZIEN

### Bereik nieuwe modules (de hoofdvraag)
Methode: 900 willekeurige kaartjes uit de steekproef, modulepagina gelezen voor ID en versies (data/odoo/pag19.json). Echt nieuw = 19.0-ID tussen 326.000 en 372.000 (begin juni t/m eind augustus 2026 volgens de ijking) en de oudste versie ook 320.000 of hoger (dus geen oude module die alleen is overgezet).
- Lichting juni t/m aug 2026 (2 tot 5 maanden oud): **n=207 van 96 makers, 94% heeft 0 aankopen, 6% heeft 1 tot 3, maximum 3, 0% 5+.** 4 hadden vorige maand een verkoop. Mediaanprijs $70,86. GEZIEN (data/odoo/kand2.json)
- Zonder de twee grootste leveranciers (Pokutsoft 34, Cerevantix 16) blijft het 93% met 0. Maar 13 van de 96 makers hebben ooit iets verkocht. GEZIEN (controleur)
- Oudere lichting, 19.0-ID 260.000 tot 326.000 (ongeveer sep 2025 t/m mei 2026, 6 tot 14 maanden oud; ijking voor juni is GOK): n=167 van 110 makers, 73% heeft 0, 27% 1+, 3% 10+. Beste: trilab_ksef (Poolse e-factuur, $603, 145 aankopen). GEZIEN (data/odoo/kandoud2.json)

### Geldvoorbeelden van kleinere makers
- mcp_server_odoo (KSRO Labs): $312,82, 65 aankopen totaal, 7 vorige maand (±$2.200 omzet in een maand, maker ±$1.500). 19.0-ID 289.017, dus voorjaar 2026 (GOK). GEZIEN
- rag_odoo_mcp_server (RAG Solutions): $201,10, 121 totaal, 13 vorige maand (±$2.600). 19.0-ID 300.148. GEZIEN
- Trilab (Pools, e-facturen KSeF en JPK): drie modules samen 24 verkopen vorige maand. GEZIEN
- Het patroon: geld komt bij een thema dat nieuw en dringend is (AI-koppeling via MCP, een wettelijke e-factuurplicht), en bij wie er vroeg bij is. Geen bron gevonden waarin een kleine maker zelf bedragen noemt. DERDEN (zoekwerk onderzoeker, niets gevonden)

## Voordelen
- Openbare verkooptellers, ook per maand: zeldzaam eerlijk meetbaar.
- Hoge prijzen ($50 tot $600), 70% voor de maker, geen keuring, geen AI-regel.
- Python-modules zijn voor ons goed te bouwen en te testen (Odoo draait in Docker op GitHub Actions).

## Nadelen
- Bereik van een gewone nieuwe module is bijna nul (94% verkoopt niets in 2 tot 5 maanden).
- Heel druk: ±50.000 betaalde modules per versie, grote Indiase bureaus zetten er tientallen per maand bij.
- Werkt niet op Odoo Online, en elke Odoo-versie is een apart product dat je elk jaar opnieuw moet overzetten.
- Uitbetaling pas vanaf 400 EUR en per factuur; terugbetaalrecht 2 maanden; support en bugfixes verplicht.

## Als we het toch zouden doen
Alleen met een thema-golf: bijvoorbeeld een AI-koppeling (MCP-server, AI-assistent in Odoo) of een nieuwe wettelijke plicht met een datum. Maar de MCP-plek is al bezet door minstens twee modules die verkopen, en bij de e-factuurgolf in Shopify zagen we dat oude spelers winnen. GOK

## Tegenargument
De tellers laten alleen verkopen via de winkel zien. Bureaus verkopen ook maatwerk eromheen, en een module kan als visitekaartje werken. Voor Dortus telt dat niet: wij willen verkoop in de winkel zelf.

## Wat er nog gemeten kan worden
- Herhaalmeting over 3 maanden met data/odoo-lijst-script.py, odoo-pagina-script.py en odoo-oudste-script.py: groeit de lichting juni t/m aug nog? (Controleur: laat het oudste-script voortaan het laagste ID over alle versies nemen.)
- Een lichting rond een thema (alle modules met "mcp" of "ai" in de naam) om te zien of thema's echt sneller verkopen.

## Bronnen
- Eigen meting 8 nov 2026, data in `data/odoo/` (lijst19.json, pag19.json, kand2.json, kandoud2.json).
- IJking ID naar datum: OCA-merges via GitHub (onder andere OCA/sale-workflow, purchase-workflow, account-financial-reporting, edi-framework, stock-logistics-warehouse): ±326.000 begin juni, ±338.000 eind juni, ±371.000 eind aug, ±420.000 begin okt, ±445.000 eind okt 2026.
- robots.txt van apps.odoo.com nageleefd: geen ?order=, ?page= of ?search=.
