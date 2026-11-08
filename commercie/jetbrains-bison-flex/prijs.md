# Bison & Flex (JetBrains): prijsvoorstel

Door Chris, 7 nov 2026. Prijs is een besluit van Jet na dit voorstel (rol commercieel manager). Het besluit komt in `organisatie/besluiten.md`.

**Besluit (Jet, 8 nov 2026):** voorstel overgenomen, zie `organisatie/besluiten.md`. Op dortus.com/bison-flex/ staat het als geplande prijs tot JetBrains het bedrag goedkeurt (Chris, 8 nov).

## Voorstel
| | Per jaar | Per maand |
|---|---|---|
| Persoonlijk (Personal) | **$19** | **$1,90** |
| Zakelijk (Commercial) | **$49** | **$4,90** |

- **Proef:** 30 dagen (de standaard; ook 7, 10 of 14 kan, DERDEN [release-plugin](https://plugins.jetbrains.com/docs/marketplace/release-plugin.html)).
- **Soort licentie:** abonnement met **fallback license** (wie een jaar betaalt en stopt, houdt de versie van dat moment). DERDEN: [license types](https://plugins.jetbrains.com/docs/marketplace/license-types-and-schemes.html).
- **Gratis licentie voor open-bronmakers en onderwijs:** ja, via de programma's van JetBrains (mag, hoeft niet: DERDEN [community programs](https://plugins.jetbrains.com/docs/marketplace/community-programs.html)).
- **Geen korting voor het 2e en 3e jaar** bij de start.

## Onderbouwing
Prijzen van vergelijkbare betaalde plugins op de Marketplace, per jaar in USD (GEZIEN 7 nov via `https://plugins.jetbrains.com/api/marketplace/plugin/<id>/prices?countryCode=US`, downloads via de zoek-API):

| Plugin | Persoonlijk | Zakelijk | Downloads |
|---|---|---|---|
| Procfile | 10 | 25 | 1.516 |
| Jenkinsfile | 15 | 50 | 162.620 |
| Caddyfile Pro | 16 | 32 | 775 |
| Nginx Configuration Pro | 20 | 50 | 268.881 |
| ANTLR4 Helper (grammatica's) | 20 | 40 | 269 |
| Jenkinsfile Pro | 24 | 65 | 30.605 |
| Flexible For Arduino (freemium) | 29 | 69 | 13.408 |
| BashSupport Pro (2e en 3e jaar goedkoper, nu tijdelijk $27) | 39 | 99 | 621.031 |
| CMake Plus | 40 | 100 | 58.922 |
| Verilog Language Support | 69 | 169 | 5.016 |

Wat dat zegt:
- Plugins voor **één bestandssoort** vragen persoonlijk $10 tot $25 en zakelijk $25 tot $65. Plugins voor een **hele taal** persoonlijk $29 tot $69 en zakelijk $69 tot $169. Ons Pro is smal: springen, alle plekken en hernoemen binnen één bestand zijn gratis, Pro is alleen het werk tussen scanner en grammatica (tokens) plus straks de meldingen ongedefinieerd en ongebruikt. Dus de lage groep past.
- Zakelijk is meestal 2 tot 2,5 keer persoonlijk, bij goedkope plugins tot 3,3 keer. $49 tegen $19 is 2,6 keer. Veel CLion-gebruikers werken bij een bedrijf dat de IDE betaalt (GOK), en daar is $49 per jaar een kleine post.
- De maandprijs is bijna overal een tiende van de jaarprijs (GEZIEN). Een maand proberen na de proef verlaagt de drempel (GOK).
- $19 eindigt op 9, zoals JetBrains aanraadt (DERDEN [pricing guidelines](https://plugins.jetbrains.com/docs/marketplace/pricing-guidelines.html)), en blijft onder $20, de prijs van Nginx Pro en ANTLR4 Helper.
- Een harde minimumprijs vond ik niet in de documentatie; de laagste die ik zag is $10 (Procfile).

**Waarom open bron en onderwijs gratis:** veel mensen met Bison en Flex zijn studenten in een compilervak of makers van open-bronprojecten (GOK). Die betalen zelden $19, maar ze schrijven reviews en nemen de plugin mee naar hun werk. Het kost ons dus weinig omzet en levert bereik op.

## Wat het oplevert (GOK)
Netto na 15% afdracht (DERDEN [revenue sharing](https://plugins.jetbrains.com/docs/marketplace/revenue-sharing-and-fees.html)): $16,15 per persoonlijk jaar, $41,65 per zakelijk jaar. Bij ±200 downloads per maand (GOK, bouwbesluit) en 2 tot 5% betalers, half persoonlijk half zakelijk: 4 tot 10 nieuwe licenties per maand. Bij jaarlicenties komt er per maand ±$115 tot $290 netto binnen; omgerekend naar een maandwaarde groeit de vaste omzet elke maand met ±$10 tot $25, opgeteld zolang mensen verlengen. Zoals in het bouwbesluit staat: dit product haalt de doelen niet alleen; het bewijst de weg.

## Risico's
- **Alle grammatica-plugins zijn gratis**, behalve ANTLR4 Helper ($20/$40), en die heeft maar 269 downloads (GEZIEN). ANTLR v4 (788.253) geeft navigatie en hernoemen gratis. De vraag naar betaald kan heel klein zijn (GOK). Daarom: het gratis deel moet goed genoeg zijn voor bereik en reviews, en Pro moet tijd besparen bij grotere grammatica's.
- **Pro heeft alleen waarde voor wie een `.l` en een `.y` samen in één project heeft** (plus de meldingen van eis 7, zodra die er zijn). Wie alleen een grammatica schrijft, heeft Pro niet nodig. Dat maakt de groep die kan betalen kleiner dan de groep die installeert (GOK). Zie advies 6.
- De licentiestempel wordt nog niet op echtheid gecontroleerd (`producten/jetbrains-bison-flex/architectuur.md`, punt "Open"; staat in Moet in 1.0, punt 6). Zonder die controle is Pro makkelijk te omzeilen.

## Wanneer opnieuw kijken
Op dag 30 na de lancering: aantal proeven, aantal betaalde licenties, verhouding persoonlijk en zakelijk. Minder dan 1 betaalde licentie op 30 proeven: Pro-grens of prijs herzien. Let op: een aanbieding met korting kan niet binnen 30 dagen na een prijsverhoging (DERDEN [special offers](https://plugins.jetbrains.com/docs/marketplace/special-offers.html)), dus liever niet laag beginnen en dan verhogen.
