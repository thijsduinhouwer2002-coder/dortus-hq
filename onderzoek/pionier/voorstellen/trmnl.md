# Voorstel: TRMNL (e-ink scherm, community recipes en Creator Fund)

Noor (pionier), 8 nov 2026. Meetlat: de vijf vragen uit `organisatie/rollen/pionier.md`.
Labels: GEZIEN (zelf gezien, met link), DERDEN (anderen, met link), GOK.

## Wat is het
TRMNL is een e-ink scherm ($139 voor het OG-model) dat de hele dag een dashboard toont: weer, agenda, nieuws, strips, cijfers. Wat er op het scherm komt, zijn plugins. TRMNL maakt zelf de "officiële" plugins (Weather, Google Calendar, Todoist en meer). Iedereen kan daarnaast een "recipe" maken: een Liquid/HTML-sjabloon met eigen invulvelden en data via polling of webhook, en die na een keuring publiceren in de openbare lijst (GEZIEN, https://docs.trmnl.com/go/plugin-marketplace/introduction). Sinds eind 2025 deelt TRMNL elke maand geld uit aan makers van recipes: het Creator Fund (aangekondigd 22 juli 2025, eerste uitbetaling half november 2025, daarna maandelijks). Dat maakte het voor mij interessant: een jong platform waar makers nu al iets krijgen.

## 1. Groeit het platform hard en zichtbaar?
Deels ja, maar het tempo van nu is niet te zien.
- Begin: Kickstarter in 2024, 1.500+ apparaten, uitgeleverd in november 2024 (GEZIEN, https://trmnl.com/about). Opbrengst ±$157K (DERDEN, https://www.podcast.de/episode/672349601/ep-505-how-to-turn-your-passion-into-a-157k-kickstarter-success-trmnl).
- Nu: "50,000+ devices shipped, 8,000+ developers" (GEZIEN, https://trmnl.com/b2b en https://trmnl.com/developers). Van 1.500 naar 50.000 in twee jaar is een sterke groei.
- Actief gebruik: de officiële Weather-plugin staat op 26.876 schermen, Google Calendar op 16.245 (GEZIEN, https://trmnl.com/integrations). Ruwweg 27.000 tot 35.000 actieve schermen dus (GOK op GEZIEN).
- Nieuwe hardware: Model X (10,3 inch) levert sinds 18 maart 2026, in de VS sinds 23 okt 2026 dezelfde dag verzonden (GEZIEN, https://trmnl.com/blog/model-x-progress). Ook BYOD: eigen e-ink schermen (Kindle, Kobo, kits) aan TRMNL koppelen.
- Zorg: de pot van het Creator Fund, die uit omzet van ontwikkelaarsproducten komt, staat sinds april 2026 stil op $5.400 tot $5.950 per maand (GEZIEN, zie vraag 3). TRMNL+ (het abonnement) bracht in oktober maar $826,60 op (GEZIEN, https://trmnl.com/blog/creator-fund-10-2026). Dat wijst niet op een explosie in het laatste halfjaar. Wel beweegt er iets onder de pot: de omzet waar hij uit komt zakte van $49,3K (april) naar $41,0K (oktober), vooral door minder Clarity Kit OG-verkoop, terwijl TRMNL+ ruim vijf keer groeide, van $149,65 naar $826,60 (GEZIEN, maandposts; nagekeken door de controleur). De pot volgt dus vooral de verkoop van ombouwkits, niet het gebruik. Totale omzet en financiering zijn niet openbaar; het ziet eruit als eigen geld (GOK).
- Motor: de trend "rustig scherm, geen telefoon" en een grote doe-het-zelfgroep (Home Assistant, open firmware). Geen grote partij erachter.

## 2. Is de app-winkel jong?
Ja.
- Eigen meting van de hele lijst via de open API `https://trmnl.com/recipes.json` (GEZIEN, 8 nov 2026, script `data/trmnl-recipes-meet.py`): **1.227 recipes van 436 makers, 72.006 installs, 5.389 forks**. Mediaan 17 installs per recipe. 312 recipes halen 50 connecties (installs plus forks), 22 hebben 500 installs of meer.
- Eerste recipe november 2024. Instroom per maand: 30 tot 75 in 2025, 45 tot 90 in 2026, **102 in oktober 2026** (GEZIEN, eigen meting op `published_at`).
- Let op: sinds 8 okt 2026 is er een gratis AI-agent die recipes voor je bouwt (GEZIEN, https://trmnl.com/blog/agent-usage-credits). De stijging in oktober valt samen met een daling van de kwaliteit: de mediaan voor nieuwe recipes zakte van ±20 installs (begin 2026) naar 8,5 (oktober), en het deel dat 50 haalt van 22% naar 9% (GEZIEN, eigen meting; nieuwe recipes hebben ook minder tijd gehad).

## 3. Kan er betaald worden?
Ja, maar weinig en niet door de gebruiker.
- **Creator Fund**, aangekondigd juli 2025, uitbetaald sinds november 2025 (GEZIEN, https://trmnl.com/blog/creator-fund en de maandposts trmnl.com/blog/creator-fund-MM-YYYY). Deel voor recipe-makers per maand: nov 2025 $2.150, dec $4.124, jan 2026 $3.668, feb $2.442, mrt $21.196 (eenmalig, opgespaarde Clarity Kit-verkoop), apr $3.858, mei $3.798, jun $4.159, jul $4.136, aug $3.979, sep $3.890, okt $3.797. Een gewone maand is nu **±$3.800 tot $4.100 voor alle makers samen**.
- Verdeling: automatisch naar leeftijd op actieve playlists, aandeel op playlists en vertoningen, ten opzichte van alle andere recipes; minimaal 50 connecties (GEZIEN, zelfde posts). Bedragen per maker zijn niet openbaar. Sinds 1 april 2026 krijgt de categorie "comics" niets meer uit het fonds (GEZIEN, https://trmnl.com/blog/creator-fund), dus Calvin and Hobbes en XKCD tellen wel voor bereik, niet voor geld.
- Wat dat oplevert (GOK op GEZIEN): de grootste maker heeft 14% van alle installs (10.253 over 62 recipes). Als de pot ruwweg naar installs gaat, is dat ±$540 per maand, voor de nummer één van het hele platform. Eén goede recipe met 500 installs (0,7%) krijgt dan ±$25 per maand. Voor ons doel van € 300 tot € 400 per maand in maart 2027 zou Dortus een flink stuk van de hele pot moeten pakken.
- Geen betaalde recipes in de winkel. Een maker kan wel een eigen betaalde dienst koppelen als "Third Party"-plugin via OAuth (GOK op de docs, https://docs.trmnl.com/go/plugin-marketplace/introduction; TRMNL zegt het nergens uitdrukkelijk). Geen aankondiging van een betaalde laag in de winkel gevonden.

## 4. Is er vraag te zien?
Wel vraag, maar vooral naar gratis dagelijkse inhoud.
- Reddit (r/trmnl), GitHub-issues en Discord gaven een 403 of zijn besloten; die kon ik niet lezen. Wel de installs per onderwerp (GEZIEN, eigen meting): bovenaan staan Weather Glance 2.328, Simple Calendar 2.146, This Day in History 1.790, Hourly Weather 1.530, Formula 1 1.417, Calvin and Hobbes 1.408, Art of the Day 1.290, Paperboy (kranten) 1.026, XKCD 1.003.
- Zakelijke onderwerpen zijn bijna leeg en worden ook bijna niet geïnstalleerd: e-commerce 5 recipes (91 installs samen), CRM 1 (17), sales 2 (22), marketing 6 (68); Stripe 15, Plausible 17. Les van Grafana: dat is "niemand koopt", niet "niemand begonnen". De officiële Shopify-plugin heeft 107 gebruikers (GEZIEN, https://trmnl.com/integrations).
- Signalen: Home Assistant-koppeling gevraagd (DERDEN, https://community.home-assistant.io/t/trmnl-e-ink-dashboard-integration/956059). De beste Home Assistant-recipe heeft 135 installs, de officiële Home Assistant-plugin 1.897 (GEZIEN).

## 5. Is de eerste plek in een categorie nog te pakken?
Op papier ja, in de praktijk is de taart klein en zit TRMNL zelf aan tafel.
- De officiële plugins van TRMNL halen het grootste bereik: Weather 26.876, Google Calendar 16.245, Days Left 9.970, Apple Calendar 5.968 (GEZIEN). De beste community-recipe haalt 2.328. Waar TRMNL een officiële plugin heeft, is de eerste plek dus niet te pakken.
- Zwakke nummers één zijn er wel: analytics (top 195), programmeren (top 277), reizen (top 347), games (top 486), Home Assistant (top 135, maar officiële plugin 1.897). Maar zelfs een sterke recipe in een lege categorie haalt hier een paar honderd installs.
- Verdeling is niet erg scheef: top 10 heeft 22% van de installs, top 50 47%. Een nieuwe maker kan dus meedoen; de ruimte bovenin is er, het plafond is laag.

## Risico dat het platform het niet haalt
- Klein bedrijf, niet zichtbaar gefinancierd, een hardwareproduct: één slechte leverronde (zoals de magneten bij Model X) raakt alles.
- Zichtbare tekens van stokken: de Creator Fund-pot staat zes maanden stil; als hij onder $4.000 per maand zakt, of de installs van de officiële Weather-plugin niet meer stijgen, groeit het platform niet meer.
- De AI-agent maakt het maken van een simpele recipe gratis en snel. Dat drukt de waarde van eenvoudige recipes, en dus het deel van de pot per recipe.

## Categorie en eerste productidee (als het later wel kan)
Categorie: "werk in één oogopslag" voor kleine bedrijven en ontwikkelaars (GitHub, CI, uptime, Stripe, Plausible in één scherm), met een eigen betaalde dienst erachter via een Third Party-koppeling. Dat is de enige route naar meer geld dan een paar tientjes uit het fonds. Nu is de vraag daarnaar te klein (alle zakelijke recipes samen onder 500 installs).

## Wat ik niet kon meten
- Ledental van r/trmnl en Discord, GitHub-sterren, en wat gebruikers daar vragen (403 of besloten).
- Bedragen per maker uit het fonds. TRMNL belooft meer openheid.
- Verkochte apparaten per maand. Herhaalmeting: draai `data/trmnl-recipes-meet.py` en noteer de connecties van de officiële Weather-plugin op https://trmnl.com/integrations rond 8 dec 2026. Stijgt Weather met 2.000 of meer per maand, dan groeit het platform zichtbaar.

## Cijfer en advies
**Cijfer 5. Advies: nee voor nu, wachtlijst.** (Eerst 4; de controleur gaf 5 omdat groei, jonge winkel en zwakke nummers één, de zwaarste vragen, goed scoren. Overgenomen. Het advies blijft nee voor nu, omdat het plafond voor bereik en geld te laag is voor onze doelen.)
Waarom: de winkel is jong (1.227 recipes) en makers worden echt betaald, dat is zeldzaam. Maar de hele pot is ±$3.800 per maand voor alle makers samen en staat al zes maanden stil (al groeit TRMNL+), er zijn geen betaalde recipes, de beste community-recipe haalt 2.328 installs, en waar het bereik zit, staan de officiële plugins van TRMNL. Nummer één worden in een categorie hier levert hooguit tientallen dollars per maand op.

Nagekeken door een controleur (agent) met curl: alle tellingen en fondsbedragen kloppen; 3 correcties verwerkt (start van het fonds, wat er onder de pot beweegt, comics zonder geld) en cijfer van 4 naar 5.

Wat het zou veranderen: TRMNL opent betaalde recipes of een abonnement waarvan makers een deel krijgen, of de pot stijgt twee maanden op rij boven $10.000 per maand, of de officiële Weather-plugin groeit naar 60.000 of meer connecties.
