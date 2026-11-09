# Gumroad Discover (marktplaats van Gumroad)

Vera, 9 nov 2026 run 15:31 (Amsterdam). Advies: **nee. Cijfer 3.**

## Wat het is
Gumroad is een kassa voor digitale producten (pdf, sjablonen, presets, plugins, cursussen). Discover (gumroad.com/discover) is de eigen marktplaats: zoeken, categorieën, "hot and new" en aanbevelingen. Waarom ik keek: Thijs kan er als persoon binnen een week verkopen en wij kunnen alles bouwen wat een bestand is. Punt 3 en 4 van "Wat een 8 is" zijn dus sterk. De vraag was of nieuwe kleine makers er bereik en geld krijgen.

## Eigen meting (GEZIEN)
- **Open bronnen.** robots.txt verbiedt alleen /purchases/. Er zijn sitemaps per maand met alle nieuwe productpagina's, en de zoek-API van Discover (`gumroad.com/products/search`) is open en geeft JSON met ratings en prijs.
- **Drukte.** De sitemap van mei 2026 heeft 18.292 producten, juni 20.856. Discover telt 740.811 producten in totaal. Grootste labels: vrchat (20.091), notion template (11.344), blender (7.903), procreate (6.072).
- **Steekproef nieuwe producten.** 400 willekeurige producten uit de sitemaps van mei en juni 2026, elke pagina gelezen (curl, 6 tegelijk, doorverwijzingen gevolgd). 346 leesbaar (de rest weg of verborgen), waarvan 306 betaald, mediaanprijs $9 (in USD).
  - Met minstens 1 rating: **3 van de 306 betaalde (1%)**, 9 van de 346 in totaal. Met 5 of meer: 1 betaald. Met 20 of meer: geen.
  - Verkoopteller (alleen zichtbaar als de maker hem aanzet): 24 betaalde producten tonen hem, daarvan 0 met een verkoop. Het enige grote getal (1.873) is een gratis DaVinci-pakket.
  - Wat er staat: veel AI-promptpakketten, ebooks over geld verdienen, planners, kleurplaten, LUTs. Dezelfde rommelstroom als bij Teachers Pay Teachers.
- **Hoe zwaar weegt een rating?** Bij 8 producten met een zichtbare teller (controleur): betaald 732 verkopen en 39 ratings (±1 op 19), gratis ±1 op 100. Dus "1% heeft een rating" betekent eerder: ±1% van de nieuwe betaalde producten haalt ±10 tot 20 verkopen of meer. De 24 zichtbare tellers met 0 verkopen steunen dat de rest weinig verkoopt (wel scheef: de maker zet de teller zelf aan). Let op: ratings kunnen uit staan; dan telt een product hier als 0.
- **"Hot and new" van Discover** (producten jonger dan 90 dagen die al in Discover mogen, dus met minstens 1 verkoop en een goedgekeurde verkoper; gesorteerd op omzet van de laatste 3 maanden; totaal 22.402). De API toont alleen de eerste 10.000. Gelezen per 9 producten (ik en de controleur): bovenaan 10 tot 2.623 ratings; tot ±plaats 3.500 heeft ongeveer de helft een rating; plaats 4.000 tot 9.000 nog 1 tot 3 van de 9. Ruw: ±3.000 tot 5.000 producten per kwartaal met minstens één rating, tegen ±60.000 nieuwe in de sitemaps (±5 tot 8%, GOK op steekproeven van 9). Dat zijn producten die al binnen zijn, grotendeels van makers met eigen verkopen (GOK).
- **Software in "hot and new"** (categorie software-development, 397 producten onder 90 dagen): zelfs de top 9 heeft 0 tot 6 ratings. Daar is weinig vraag.

## Bronnen (onderzoeker, nagelezen)
- Kosten: 10% + $0,50 per directe verkoop, plus kaartkosten; **30% bij een verkoop via Discover** (GEZIEN, gumroad.com/pricing en help/article/66).
- Gumroad is sinds 1 jan 2025 merchant of record, btw in de EU geregeld; uitbetaling naar een Nederlandse bank in EUR vanaf $100; als "Individual" zonder KvK; Stripe vraagt wel ID en ID-nummer (GEZIEN, help/article/13, 10 en 260).
- **Toegang tot Discover:** het account moet eerst $100 aan echte verkopen hebben en een risicocontrole halen (gemiddeld ±3 weken), en elk product moet zelf al 1 verkoop hebben (een gratis download telt ook), een categorie en aangezette ratings; Discover-producten doen automatisch mee aan het affiliateprogramma van Gumroad (GEZIEN, help/article/79-gumroad-discover). Producten die als volwassen zijn aangemerkt staan standaard niet in hot and new.
- **Rangschikking** (open broncode, GEZIEN): "featured" sorteert op wat Gumroad aan het product verdiende in de laatste 3 maanden; "hot and new" op omzet; aanbevelingen komen uit wat kopers samen kochten. Wie nog niets verkoopt, staat dus nergens.
- Ervaringen (DERDEN): een maker zette in okt 2026 130 AI-producten op Gumroad, 0 verkopen, kwam nooit in Discover (dev.to/mattbusel). Indie Hackers-post "Gumroad has zero organic discovery" (niet leesbaar, Cloudflare). Een blog noemt 10 tot 20% van de omzet uit Discover bij sommige verkopers. In 2020 leverde Discover Gumroad ±$10.000 per maand aan fees op, een klein deel van het geheel (tweet Sahil Lavingia).
- AI-beleid: AI-diensten en doorverkochte prompts of PLR-boeken zijn verboden (prohibited, herzien 16 sep 2026); zelf met AI maken mag (GEZIEN). Gumroad kromp van 32 naar 14 mensen (mrt 2026).

## Scores op "Wat een 8 is"
1. Nieuwe kleine makers verdienen: **nee**. 1% van de nieuwe betaalde producten heeft één rating.
2. Bereik voor nieuwkomers: **zwak**. Discover gaat pas open na $100 eigen omzet en ±3 weken controle, en rangschikt op omzet. Wie binnen is en een beetje verkoopt, krijgt wel enig bereik (duizenden producten met 1 tot 5 ratings in hot and new). Discover vergroot bereik dat je al hebt; het maakt geen bereik vanaf nul.
3. Bouwen en testen: ja, sterk (bestanden).
4. Thijs kan binnen een week verkopen: ja, sterk.

## Voor en nadelen
- Voor: open data, makkelijke kassa, merchant of record, geen KvK.
- Tegen: geen eigen bereik voor nieuwkomers, 30% bij verkoop via Discover, overspoeld met AI-rommel.

## Wat we er zouden bouwen
Niets als platform. Gumroad blijft wel bruikbaar als **kassa** voor een product dat zijn bereik elders haalt (zoals Olaf Polar.sh gebruikt bij Obsidian). Dat is een betaalweg, geen platform.

## Cijfer en advies
**3, nee.** Twee van de vier punten sterk, maar juist de twee die het zwaarst wegen (geld en bereik voor nieuwkomers) zijn zwak: ±1% van de nieuwe betaalde producten haalt naar schatting 10 tot 20 verkopen, en Discover gaat pas open na eigen omzet. Nagekeken door de controleur: akkoord met het advies, 8 correcties verwerkt (onder meer hot and new beter geteld, de API stopt bij 10.000, en wat een rating zegt over verkopen). Opnieuw kijken alleen als Gumroad Discover opent voor nieuwe makers zonder eigen verkopen.

Data: `data/gumroad-steekproef-mei-jun-2026.json` (400 regels), script `data/gumroad-steekproef-haal.sh` en `data/gumroad-steekproef-tel.py`.
