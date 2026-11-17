# Keuring groep E: ontwikkelaarsgolven en migraties (17 nov 2026)

Keurder: alle pagina's zelf opnieuw gelezen met curl, met andere ingangen dan de onderzoeker (officiele supportpagina, Marketplace-API met vier zoektermen, de volledige Shopify-tekst).

## De gecontroleerde beweringen

### 1. Shopify doet sinds de Fall '26 Edition zelf het agent-stuk (WebMCP, "agent-ready by default")
**KLOPT.**
Bron: https://www.shopify.com/news/fall-26-edition-developer (28 okt 2026, zelf gelezen).
Letterlijk: "A set of tools on every Liquid and Hydrogen storefront and checkout that expose structured data and let browser agents search products, update the cart, and complete checkout once the buyer approves" en "Every Shopify store is agent-ready by default." Ook "no key required" voor Shop.dev klopt letterlijk.
Kleine aanvulling: dezelfde pagina noemt ook een nieuwe thema-architectuur (Liquid met blocks, typed contracts, Tailwind ingebouwd, markdownbestanden voor agents). Die heeft de onderzoeker niet genoemd; zie "Gemist?" hieronder.

### 2. De nieuwe Shopify App Store-regels van 10 nov 2026
**KLOPT, alle vier.**
Bron: https://shopify.dev/changelog/shopify-app-store-submission-requirements-build-grow-then-expand (10 nov 2026, zelf gelezen).
Letterlijk: 10 installs op "full-priced Shopify stores" per bestaande app voor je een volgende app mag aanmelden; "escalating cooldown periods" na afwijzing; "Identity verification is now a required step for developers who submit new apps"; "Apps with zero installs after six months are automatically removed". Gaat in "starting today". De GOK van de onderzoeker dat ID-controle met paspoort gaat is niet na te gaan in deze tekst: blijft ONBEKEND.

### 3. Microsoft levert zelf een gratis upgradetool voor .NET (en .NET 8 en 9 zijn uit support)
**KLOPT.**
Bron tool: https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/faq (bijgewerkt 25 sep 2026). Letterlijk: "Copilot Free (Starting with Visual Studio 2026 version 18.1)" in de lijst van toegestane abonnementen, en "The agent works with all Copilot subscription tiers, including the free tier." Werkt in Visual Studio, VS Code, Copilot CLI en GitHub.com.
Bron einddatum: https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core (zelf gelezen). .NET 8 en .NET 9: einde support 10 nov 2026. .NET 11 (STS) en .NET 10 (LTS) lopen tot 14 nov 2028. De GOK van de onderzoeker over de datum kan dus naar GEZIEN.
Kanttekening: "gratis" betekent Copilot Free met zijn beperkte maandtegoed; een groot project zal meer vragen. Maar het gat dat een kleine maker zou kunnen vullen is er niet.

### 4. De Linear-integratiedirectory weigert kleine makers
**KLOPT (met een klein kiertje).**
Bron: https://linear.app/developers/integration-directory (zelf gelezen 17 nov 2026). Letterlijk: "We'll accept integrations that we think are useful to the community and are built by formal companies. We generally do not accept scripts, low-effort/vibe coded or apps built by hobbyists, but feel free to reach out to integrations@linear.app". Het woord is "generally", dus niet hard dicht, maar voor een eenpersoonsploeg met AI-gebouwde apps is het in de praktijk een nee. Aanmelden gaat via een formulier, er is geen kassa.

### 5. Er zijn al 15+ gratis tokentools in de VS Code Marketplace
**KLOPT, en het is erger dan de onderzoeker schrijft.**
Bron: Marketplace-API (extensionquery), zelf gedraaid op 17 nov 2026 met vier zoektermen ("claude usage", "claude usage limit", "codex usage", "token usage").
De onderzoeker noemde als grootste Claude Usage Bar met ±13.600. Die zoekterm miste de echte koplopers:
- Claude Code Usage (growthjack): ±80.700 installs, sinds juli 2025
- Claude Terminal: ±31.800
- Claude Status: ±18.900
- Claude Code Usage Tracker: ±16.200
- Claude Usage Bar: ±13.600
- Claude Code Usage, History: ±12.000
- Codex Rate Limit Monitor ±8.700, Codex Usage ±8.600, Claude Context Bar ±7.400
Daarna nog ruim 40 tools tussen 500 en 6.000 installs, ook voor Copilot-tokens. Er komen er nog steeds bij (o.a. juli en oktober 2026). Wij zouden niet nummer 16 zijn maar ergens rond nummer 50. Alles gratis, geen kassa in de Marketplace.

## Eens met de cijfers?
Ja. Ik vind geen enkele bewering waarop de onderzoeker te positief was; bij de tokentools was hij zelfs te mild. Per tip:
- .NET 11: 2 klopt (Microsoft doet het zelf, gratis; jaarlijkse release, geen nieuw platform).
- Linear: 1 klopt (etalage dicht voor hobbymakers, Linear bouwt zelf een agent).
- Render/Cloudflare sandboxes: 1, niet zelf nagekeken maar de redenering (geen winkel, geen kassa) is sterk genoeg.
- Shopify: 2 klopt. Wet 4 is hard nee voor alles rond "winkel klaar voor agents". De nieuwe regels maken het voor een nieuwkomer zwaarder, en met één app tegelijk tot die 10 betalende installs heeft past het niet bij onze werkwijze van snel veel proberen.
- Opal, Claude Data, AG-UI, HubSpot, Vertex: 1 tot 2 is terecht; geen winkel met kassa of het platform doet het zelf.
- Tokentools: 2 is terecht, eerder 1,5.

## Gemist? Gezocht naar een kans binnen deze golven die wel alle wetten haalt
Kandidaat die de onderzoeker niet noemde: **Shopify's nieuwe thema-architectuur (Fall '26) in de Shopify Theme Store.**
- Bestaat: JA. Shopify-pagina hierboven (28 okt 2026); ook beschreven door themamaker The4: https://the4.co/blogs/shopify-themes/shopify-editions-fall-2026-theme-developers . Nieuw: Liquid met blocks en typed contracts, Tailwind ingebouwd, markdownbestanden die Sidekick vertellen hoe het thema in elkaar zit, en de nieuwe editor Canvas (early access) draait erop. Ook nieuw: een app-add-on aan een themavermelding koppelen.
- Waarom het leek te passen: elke winkelier heeft een thema nodig (wet 2 ja), de Theme Store heeft een eigen kassa met 15% afdracht (https://shopify.dev/docs/storefronts/themes/store.md , GEZIEN) en een sterke betaalcultuur (wet 3 ja), en de Theme Store toont thema's zelf aan kopers (vraag 5 ja). Een nieuwe architectuur betekent dat bijna niemand nog een thema op de nieuwe basis heeft.
- Waarom het toch sneuvelt:
  - Wet 1: nee. Een thema voor de Theme Store moet aan een lange eisenlijst voldoen en wordt anders afgewezen (GEZIEN in de docs). De keuring duurt weken tot maanden; in juli 2026 vroegen makers op het Shopify-forum al na ruim een week zonder antwoord om een tijdsindicatie (https://community.shopify.dev/t/theme-store-review-expected-feedback-timeline/35809). Binnen 7 dagen staan is uitgesloten (GOK op de exacte duur, maar ruim boven 7 dagen).
  - Wet 4: twijfel. Shopify levert zelf gratis thema's en bouwt Canvas op de nieuwe architectuur; vrijwel zeker komen de gratis Shopify-thema's als eerste op de nieuwe basis (GOK).
  - Een volwaardig premiumthema is een flink bouwwerk met hoge ontwerpeisen; de grote themahuizen (zoals The4: "It's the biggest change for us in years") zitten er al bovenop.
- Cijfer: 3. De enige plek in groep E met etalage, kassa en een echt nieuwe golf, maar te traag te keuren en de vaste themahuizen zijn er eerder.

Verder gekeken en afgeschoten: een Rider/JetBrains-plugin voor C# 15 union types (JetBrains Marketplace heeft wel een kassa, maar Rider en Visual Studio bouwen taalondersteuning zelf in: wet 4 nee); hulpmiddelen voor de verplichte Shopify-migraties (script tags weg, verlopende tokens voor januari 2027): dat is werk voor app-makers, geen winkelier koopt dat (wet 2 nee, geen etalage).

## Mijn top
**Niets haalt een 7.** Ik sluit me aan bij het advies van de onderzoeker: groep E levert geen kandidaat op. De beste gemiste invalshoek (thema op de nieuwe Shopify-architectuur) komt niet verder dan een 3 omdat de Theme Store-keuring wet 1 breekt.
