# Onderzoek betaalweg Rollwright

Datum: 6 november 2026. Onderzoeker: Claude (agent). Labels: GEZIEN = zelf op de pagina gezien (link erbij), DERDEN = bron van een ander (link erbij), GOK = eigen inschatting.

## 1. Regels van Obsidian

- Developer policies: betaling, account en netwerkgebruik zijn toegestaan, mits "clearly indicated in your README". Letterlijk onder "Disclosures": "Payment is required for full access", "An account is required for full access", "Network use. Clearly explain which remote services are used and why they're needed." Niet toegestaan: verborgen (obfuscated) code, ads die via internet laden, telemetrie aan de kant van de gebruiker, zichzelf installeren of updaten. GEZIEN: https://docs.obsidian.md/Developer+policies (bron: publish-01.obsidian.md/access/.../Community directory/Developer policies.md)
- Submission requirements: `fundingUrl` alleen voor donaties (Buy Me A Coffee, GitHub Sponsors), niet voor een winkel. Node/Electron API's alleen op desktop; gebruik `SubtleCrypto` in plaats van Node `crypto`. GEZIEN: https://docs.obsidian.md/Submission+requirements+for+plugins
- Labels in de nieuwe Community directory (FAQ): Free, Optional payment ("if you lock certain features behind payment"), Paid (alleen tegen betaling). GEZIEN: docs.obsidian.md, pagina Community directory/Frequently asked questions. Rollwright (gratis kern, betaalde skins) = **Optional payment**.
- Blog "Future of plugins": "Obsidian Community is not a store, and does not offer any built-in payment solutions. Developers can continue to use external payment mechanisms such as license keys, API keys, and login gates." GEZIEN: https://obsidian.md/blog/future-of-plugins/
- Online sleutel controleren: mag. Er is geen verbod; het valt onder "Network use" en moet in de README staan (welke dienst, waarom). GEZIEN (policies hierboven). Obsidian `requestUrl` werkt "without any CORS restrictions". GEZIEN: https://docs.obsidian.md/Reference/TypeScript+API/requestUrl

Wat in de README moet (voorstel, gebaseerd op de policies):
1. "Skins zijn betaald (eenmalig). De dobbelstenen en tabellen zijn gratis." (betaling)
2. "Geen account nodig." (als dat zo is)
3. "Netwerk: alleen bij het invoeren van een sleutel stuurt de plugin de sleutel naar <dienst> (api.lemonsqueezy.com of api.polar.sh) om hem te controleren. Verder geen netwerkverkeer." Plus link naar privacybeleid van die dienst. (Geen telemetrie.)
4. LICENSE-bestand blijft verplicht; code niet verbergen.

## 2. Betaaldiensten

| Dienst | Kosten per verkoop | MoR (btw) | Sleutels + controle | Geheime sleutel nodig? | CORS / requestUrl | Uitbetaling NL | Bijzonder |
|---|---|---|---|---|---|---|---|
| Lemon Squeezy | 5% + $0,50 (GEZIEN, lemonsqueezy.com/pricing) | Ja (GEZIEN, pricing) | Ja, `POST https://api.lemonsqueezy.com/v1/licenses/validate` (en /activate, /deactivate), 60 verzoeken per minuut (GEZIEN, docs.lemonsqueezy.com/help/licensing/license-api) | Nee, alleen `license_key` (GEZIEN, live getest: antwoord zonder API-sleutel) | `access-control-allow-origin: *` (GEZIEN, live test); requestUrl werkt sowieso | GOK: ja (bank via Stripe of PayPal) | Overgenomen door Stripe. Hun eigen blog "2026 Update" zegt dat Stripe Managed Payments "the future" is en dat ze LS-gebruikers willen laten overstappen (GEZIEN, https://www.lemonsqueezy.com/blog/2026-update). Risico: later verhuizen. Of nieuwe aanmeldingen dicht zijn: niet vastgesteld (pricing-pagina toont nog "Get started"). |
| Polar.sh | Starter: 5% + $0,50, plus 1,5% voor niet-VS kaarten; Pro $20/mnd: 3,8% + $0,40 (GEZIEN, https://polar.sh/docs/merchant-of-record/fees.md) | Ja (GEZIEN, zelfde pagina) | Ja, sleutels als "benefit"; `POST https://api.polar.sh/v1/customer-portal/license-keys/validate` met `key` + `organization_id` (GEZIEN, https://polar.sh/docs/features/benefits/license-keys.md) | Nee, de organisatie-ID is openbaar (GEZIEN, docs + live test) | `access-control-allow-origin: *` (GEZIEN, live test) | Ja, Nederland staat op de lijst, via Stripe Connect Express (GEZIEN, https://polar.sh/docs/merchant-of-record/supported-countries.md) | Klant kan sleutel zelf roteren; activatielimiet per apparaat mogelijk. Geen bekende problemen gevonden. |
| Gumroad | 10% + $0,50 (direct), 30% via Discover (GEZIEN, https://gumroad.com/pricing) | Ja, sinds 1 januari 2025 (GEZIEN, pricing-pagina) | Ja, `POST https://api.gumroad.com/v2/licenses/verify` met `product_id` + `license_key` (GEZIEN, live getest) | Nee (GEZIEN, live test zonder token) | `access-control-allow-origin: *` (GEZIEN) | GOK: ja | Duurste van de vier. |
| Paddle | 5% + $0,50 (GEZIEN, https://www.paddle.com/pricing) | Ja (GEZIEN) | Nee in Paddle Billing: "Build your own workflows using transaction webhooks" (GEZIEN, developer.paddle.com/llms.txt) | n.v.t. | n.v.t. | GOK: ja | Zonder eigen server ongeschikt. Keurt kleine verkopers streng (GOK). |
| Payhip | Gratis plan 5% plus kosten Stripe/PayPal (~2,9% + $0,30) (DERDEN, https://fungies.io/payhip-review-2026) | Nee, geen volledige MoR; regelt alleen EU- en UK-btw (DERDEN, zelfde) | Ja, `GET https://payhip.com/api/v2/license/verify`, met per product een "product secret key" (GEZIEN, https://help.payhip.com/article/317-software-license-keys-new) | Ja, een productsleutel (minder erg dan account-API-sleutel, maar staat dan in de plugin) | niet vastgesteld | GOK: ja | Kan **zelfgemaakte sleutels uploaden** (tot 10.000 per keer, max 100 tekens): handige route voor offline handtekening-sleutels zonder server (GEZIEN, zelfde pagina). |

Stripe Managed Payments (opvolger LS): of het ingebouwde licentiesleutels heeft, niet vastgesteld.

## 3. Bestaande betaalde Obsidian-plugins

- **Copilot for Obsidian** (Brevilabs): Plus/Believer/Supporter-licentie, eigen account en eigen backend, online. README heeft een aparte "Paid Plan Disclosure" (account, betaling, netwerk, privacy). GEZIEN: https://github.com/logancyang/obsidian-copilot (README). Welke betaaldienst: niet vastgesteld.
- **Smart Connections**: "Pro plugins" voor "project supporters", via eigen site smartconnections.app; bron is "source available" met eigen licentie. GEZIEN: https://github.com/brianpetro/obsidian-smart-connections (README). Betaaldienst: niet vastgesteld.
- **Bases Power Pack**: $29 eenmalig via Buy Me a Coffee, sleutel "emailed to you automatically, within seconds", "unlocks instantly, offline", "governed by a signed license key". Dit is precies het offline-handtekening-model. GEZIEN: https://github.com/israerusan/bases-power-pack (README) en https://www.obsidianstats.com/plugins/bases-power-pack
- **Excalidraw** en **Omnisearch**: geen betaalde functies, alleen donaties (Ko-fi, GitHub Sponsors). GEZIEN: READMEs zsviczian/obsidian-excalidraw-plugin en scambier/obsidian-omnisearch.
- Forumdraad over licentiesleutels/WebCrypto voor betaalde plugins (2025): https://forum.obsidian.md/t/96401 (GEZIEN, vraag van een ontwikkelaar; geen officieel antwoord gelezen).

## 4. Offline sleutel met digitale handtekening

- Idee: Thijs heeft een geheime sleutel; de plugin bevat alleen de publieke sleutel en controleert de handtekening met `crypto.subtle.verify`. Geen netwerk nodig, dus ook geen netwerk-melding in de README. Beperking: een gelekte sleutel werkt overal; intrekken kan alleen met een lijst in een update (GOK). Code is open, dus wie wil kan de controle eruit halen; dat geldt voor elke methode (GOK).
- Automatisch zonder eigen server, route A: **Payhip lijst uploaden**. Thijs (of een agent) maakt vooraf bijvoorbeeld 1.000 ondertekende sleutels en uploadt ze; Payhip geeft er per verkoop één af. Geen server, geen webhook. GEZIEN (upload-functie, link hierboven). Nadeel: Payhip is geen volledige MoR.
- Route B: **webhook naar Cloudflare Workers** (gratis: 100.000 verzoeken per dag, 10 ms CPU per verzoek; GEZIEN, https://developers.cloudflare.com/workers/platform/pricing/). De worker ondertekent bij een "order_created"-webhook en moet de sleutel dan nog bij de klant krijgen (mail via een extra dienst, of de klant haalt hem op met zijn ordernummer). Werkt, maar is wel een eigen stukje server om te onderhouden (GOK).
- Route C: **met de hand** (Thijs ondertekent per bestelling): werkt, maar Thijs wil zo min mogelijk doen. Afgeraden.
- Route D (eenvoudigst): dienst-sleutel online controleren en daarna het resultaat lokaal bewaren, zodat de plugin daarna offline werkt (GOK, gangbaar patroon).

WebCrypto ondersteuning (bron: MDN browser-compat-data 8.1.8, 2 nov 2026, GEZIEN via https://unpkg.com/@mdn/browser-compat-data/data.json, pad api.SubtleCrypto.verify):
- **ECDSA P-256**: verify sinds Chrome 37, Safari/iOS 7, Android WebView 37. Werkt dus op desktop (Electron), iOS en Android. GEZIEN.
- **Ed25519**: Chrome 137, Android WebView 137, Safari en iOS 17. GEZIEN. Op desktop hangt het af van de Electron-versie van de installer: Obsidian laat het app-versienummer apart van het "installer version" (Electron) zien en oude installers blijven in gebruik (DERDEN, https://forum.obsidian.md/t/110663). Gebruikers met een oude installer of iOS 16 hebben dan geen Ed25519. Oplossing: ECDSA P-256 kiezen, of Ed25519 laten controleren met een kleine JS-bibliotheek zoals @noble/ed25519 (GOK).

## Advies (5 regels)

1. Dienst: **Polar.sh** (MoR, regelt btw, NL-uitbetaling bevestigd, licentiesleutels ingebouwd, controle zonder geheime sleutel). Lemon Squeezy is gelijkwaardig maar Stripe laat het uitfaseren richting Managed Payments; Gumroad is te duur (10%).
2. Controle: **allebei**. Eén keer online controleren bij invoer via `requestUrl` naar `api.polar.sh/.../license-keys/validate` (controleer ook dat de sleutel bij onze organisatie en benefit hoort), daarna resultaat lokaal opslaan zodat skins offline blijven werken.
3. Offline handtekening (ECDSA P-256, niet Ed25519) pas later toevoegen als er vraag is naar volledig offline gebruik; dan via Cloudflare Worker of Payhip-lijst. Niet nu: kost een extra account en onderhoud.
4. Listing: label "Optional payment"; README met een kopje "Betaling en netwerk": skins betaald, geen account nodig, netwerk alleen voor sleutelcontrole bij Polar, link naar Polar-privacybeleid. Verwijder de huidige controlesom-sleutel.
5. Stappen Thijs: Polar-account aanmaken (GitHub-login), organisatie aanmaken, Stripe Connect Express koppelen met NL-bankrekening en ID-controle, product "Rollwright Skins" eenmalig met prijs (bijv. $6 of "betaal wat je wilt" met minimum), License Keys-benefit toevoegen, en de organisatie-ID en benefit-ID doorgeven aan de ploeg. Geen API-sleutel nodig voor de plugin.

## Controle (6 nov 2026, controleur, met curl en een live test)
Akkoord met punten. Aanvullingen die het advies bijstellen:
- Polar-kosten gaan over het bedrag inclusief btw, plus $15 per dispuut. Bij $6 is dat ±$0,95 per verkoop, ±15% (GOK, eigen rekensom). De vaste 50 cent weegt zwaar.
- Een 200-antwoord van validate heeft altijd `status` `granted`. Ingetrokken, uitgeschakeld, verlopen of een benefit die niet past komen als 404 (`ResourceNotFound`, GEZIEN live voor een onbekende sleutel). Een fout `organization_id` geeft 422. CORS `*`. `benefit_id` kan in het verzoek mee.
- Het antwoord bevat naam en e-mail van de koper (`customer`): niet bewaren.
- In de benefit geen activatielimiet en geen vervaldatum aanzetten: met een limiet geeft validate zonder `activation_id` een 404 en werkt geen enkele sleutel.
- Gumroad is bij $6 maar ±25 cent per verkoop duurder (GOK). Het echte argument voor Polar boven Lemon Squeezy is de onzekere toekomst van Lemon Squeezy (blog "2026 Update"), niet de prijs.
