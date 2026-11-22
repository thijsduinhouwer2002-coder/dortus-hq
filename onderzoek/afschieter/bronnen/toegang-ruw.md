# Toegang per platform: officiële sleutels en tokens (ruwe bronnotities)

Opgehaald op 10 november 2026 uit officiële documentatie met curl. Alles wat ik niet in een officiële bron terugvond staat als "niet bevestigd". Minuten zijn schattingen van mij, niet uit de bron.

Uitgangspunt: agents werken via GitHub Actions. Sleutels staan als repository secret of environment secret in GitHub. Wachtwoorden worden nergens opgeslagen.

---

## 1. JetBrains Marketplace

**Sleutel: Permanent Token (in de Gradle docs "Personal Access Token" genoemd)**
- Wat hij kan: een nieuwe versie van een bestaande plugin uploaden via `POST https://plugins.jetbrains.com/api/updates/upload` met `Authorization: Bearer <token>`, of via de Gradle taak `publishPlugin` (token in `ORG_GRADLE_PROJECT_intellijPlatformPublishingToken`). Ook voor .NET plugins via `nuget push`. Opties bij upload: kanaal (bijv. nightly), `isHidden`, `containsAds`. Max 400 MB. Bron: https://plugins.jetbrains.com/docs/marketplace/plugin-upload.html en https://plugins.jetbrains.com/docs/intellij/publishing-plugin.html
- Wat hij NIET kan: de eerste publicatie. "The first plugin publication must always be uploaded manually." Bron: https://plugins.jetbrains.com/docs/intellij/publishing-plugin.html
- Beperken: in de documentatie staan geen scopes, geen verloopdatum en geen beperking per plugin. Niet bevestigd dat dit kan. Je ziet de token maar één keer.
- Aanmaken: inloggen op JetBrains Marketplace, profiel, tab **My Tokens**, naam invullen, **Generate Token**, meteen kopiëren. Ongeveer 3 minuten. Bron: https://plugins.jetbrains.com/docs/intellij/publishing-plugin.html
- Vereisten: JetBrains Account. Bij de eerste upload moet je de JetBrains Marketplace Developer Agreement accepteren en een Vendor profiel maken. Bron: https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html . 2FA als vereiste: niet bevestigd.
- Extra geheim: plugins horen ondertekend te zijn (`signPlugin` draait vóór `publishPlugin`). Daarvoor is een certificaat met private key nodig, ook als secret op te slaan. Dat is een sleutel, geen accountwachtwoord. Bron: https://plugins.jetbrains.com/docs/intellij/publishing-plugin.html

**Blijft handwerk**
- Eerste upload, Vendor profiel, Developer Agreement accepteren, eigen EULA meegeven. Bron: https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html
- Elke nieuwe plugin én elke update wordt handmatig gekeurd door JetBrains, reactie meestal binnen 3 tot 4 werkdagen. Bron: https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html
- Betaalde plugins (prijzen, licenties): niet uitgezocht, niet bevestigd.

---

## 2. extensions.blender.org

**Sleutel: Authentication token (Blender Extensions Platform)**
- Wat hij kan: een nieuwe versie uploaden van een bestaande extensie: `POST https://extensions.blender.org/api/v1/extensions/<extension_id>/versions/upload/` met header `Authorization:bearer <token>`, velden `version_file` (de .zip) en `release_notes` (markdown). Bron: https://developer.blender.org/docs/features/extensions/ci_cd/
- Wat hij NIET kan: in de docs alleen het uploaden van versies. Een nieuwe extensie aanmaken via de API staat er niet in, dus niet bevestigd. De handleiding beschrijft de eerste publicatie als upload via de website met Blender ID. Bron: https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html
- Beperken: scopes of verloopdatum staan niet in de documentatie. Niet bevestigd.
- Aanmaken: "Authentication tokens can be generated from the user profile page on the extensions platform." Ongeveer 3 minuten. Bron: https://developer.blender.org/docs/features/extensions/ci_cd/
- Vereisten: Blender ID account. Verder niets gevonden.

**Blijft handwerk**
- Eerste upload via de website; de extensie wordt vastgehouden voor review en pas gepubliceerd als het moderatieteam akkoord geeft. Bron: https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html en https://developer.blender.org/docs/features/extensions/moderation/
- Of latere versies ook opnieuw gekeurd worden: niet bevestigd.

---

## 3. Obsidian community plugins

**Belangrijke wijziging:** de officiële docs beschrijven niet meer een PR naar `obsidianmd/obsidian-releases`. Inzenden gaat nu via de Obsidian Community directory op https://community.obsidian.md : inloggen met een Obsidian account, je GitHub account koppelen, plugin toevoegen. Daarna volgt een automatische review met feedback in de directory. Bron: https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Plugins/Releasing/Submit%20your%20plugin.md (gepubliceerd als https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin). De README van obsidian-releases verwijst ook naar die pagina. Bron: https://github.com/obsidianmd/obsidian-releases

**Sleutel: geen Obsidian sleutel nodig voor updates. Alleen GitHub.**
- Wat kan automatisch: na publicatie haalt Obsidian nieuwe versies zelf uit GitHub releases (tag = `version` uit `manifest.json`, bestanden `main.js`, `manifest.json`, `styles.css`). "You only need to submit the initial version of your plugin." De officiële voorbeeldworkflow gebruikt `GITHUB_TOKEN` met `permissions: contents: write, id-token: write, attestations: write` en maakt een release met build attestation. Bron: https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Plugins/Releasing/Release%20your%20plugin%20with%20GitHub%20Actions.md
- Let op: de voorbeeldworkflow maakt een **draft** release die je met de hand publiceert. Je kunt `--draft` weglaten, dan publiceert de workflow direct (dat is gewone `gh release create`, geen Obsidian regel).
- Instelling: in de repo onder Settings, Actions, General, Workflow permissions: **Read and write permissions**, of per workflow `permissions:` zetten. Bron: zelfde pagina.

**Blijft handwerk**
- Obsidian account aanmaken, GitHub koppelen, plugin toevoegen in community.obsidian.md, automatische reviewfouten oplossen. Bron: Submit your plugin (link hierboven).
- Aankondigen op forum en Discord (Discord `#updates` vereist de developer rol). Bron: zelfde pagina.

---

## 4. Steam / Steamworks

**4a. Build account voor steamcmd (uploaden van builds)**
- Wat het is: een gewoon Steam account dat in je Steamworks account de rechten "Edit App Metadata" en "Publish App Changes To Steam" krijgt. Valve raadt aan een apart build account te maken met alleen die rechten. Bron: https://partner.steamgames.com/doc/sdk/uploading (sectie Steam Build Account)
- Wat het kan: builds uploaden met steamcmd en een app build script; met `SetLive` een build automatisch live zetten op een **beta branch**. Bron: zelfde pagina.
- Wat het NIET kan: de `default` branch kan niet automatisch live, dat moet in het App Admin panel. Bron: zelfde pagina. Om een build live te zetten voor een uitgebrachte app moet het account een telefoonnummer of de Steam Mobile App hebben; na een beveiligingswijziging (e-mail, telefoon) 3 dagen wachten. Bron: zelfde pagina.
- **Steam Guard probleem en wachtwoorden:** steamcmd werkt met gebruikersnaam en wachtwoord, er is geen API token voor uploads. De officiële CI aanpak: één keer `steamcmd +login <naam>` met wachtwoord en Steam Guard code op de machine, daarna alleen nog `+login <naam>` zonder wachtwoord, en het bestand `config/config.vdf` bewaren tussen runs omdat daar het login token in staat. Bron: https://partner.steamgames.com/doc/sdk/uploading (sectie Using SteamPipe In A CI/CD Environment). Bij "Login Failure" door Steam Guard: code uit e-mail halen en `set_steam_guard_code <code>`. Bron: zelfde pagina (Troubleshooting).
- Gevolg voor onze regel: het wachtwoord hoeft niet opgeslagen te worden, wel `config.vdf` als secret. Hoe lang dat login token geldig blijft: niet bevestigd. Als het verloopt moet Thijs opnieuw één keer handmatig inloggen. Het bekende GitHub Action `game-ci/steam-deploy` werkt zo met een configVdf secret, maar dat is geen officiële Valve bron.
- Aanmaken: nieuw Steam account via https://store.steampowered.com/join , daarna voegt een Steamworks admin het toe en geeft de twee rechten (Users & Permissions). Ongeveer 15 minuten plus de eenmalige eerste login. Bron: https://partner.steamgames.com/doc/sdk/uploading

**4b. Publisher Web API key**
- Wat hij kan: beveiligde Web API methoden, per rechtengroep: Microtransactions, Sales Data (IPartnerFinancialService), Economy (Steam Inventory), General (bijv. eigendom van DLC controleren). Bron: https://partner.steamgames.com/doc/webapi_overview/auth
- Beperken: hoort bij een groep (Publisher Group) met gekozen apps, je kiest de rechten, en per sleutel een **IP whitelist** mogelijk. Bron: zelfde pagina. Let op: GitHub hosted runners hebben geen vast IP, dus een IP whitelist werkt daar niet zonder eigen runner (mijn afleiding).
- Wat hij NIET kan: builds uploaden (dat gaat via steamcmd). Niet bedoeld voor gameclients.
- Aanmaken: als Steamworks admin naar Users & Permissions, Manage Groups, (dedicated) groep kiezen of maken, apps controleren, **Create WebAPI Key**, rechten kiezen, Save Changes. Ongeveer 5 minuten. Bron: zelfde pagina.

**4c. Financial API key (Partner Financials)**
- Wat hij kan: alle verkoopdata van het hele partneraccount lezen (`GetChangedDatesForPartner`, `GetDetailedSales`), zonder ingelogde gebruiker. Bron: https://partner.steamgames.com/doc/webapi/IPartnerFinancialsService
- Wat hij NIET kan: alleen lezen van financiële data; geen beperking per app mogelijk ("no app limitations or user limitations").
- Beperken: alleen via IP whitelist in "Manage WebAPI Key" op de groep. Bron: zelfde pagina.
- Aanmaken: op Manage Groups een speciale "Financial API Group" maken (geen gebruikers, geen apps); de sleutel staat dan op de groepspagina. Ongeveer 5 minuten. Bron: zelfde pagina.

**Vereisten en blijft handwerk (Steam)**
- Steam Direct fee van $100 per product, niet terug te krijgen, wel terugverdiend na $1.000 omzet; 21 dagen wachten tussen betalen en uitbrengen. Bron: https://partner.steamgames.com/steamdirect
- Onboarding: NDA en Steam Distribution Agreement digitaal tekenen, bank en belastinggegevens, identiteitsverificatie. Bron: https://partner.steamgames.com/doc/gettingstarted/onboarding
- Build live zetten op default branch, storepagina, prijzen, publiceren via het App Admin panel. Bron: https://partner.steamgames.com/doc/sdk/uploading . Store review: niet uitgezocht, niet bevestigd.
- KvK als harde eis: niet bevestigd (wel identiteit en belastinggegevens).

---

## 5. Polar.sh

**Sleutel: Organization Access Token (OAT)**
- Wat hij kan: namens één organisatie de API gebruiken (producten, prijzen, checkouts, orders, abonnementen, benefits, enz.), header `Authorization: Bearer polar_oat_...`. Bron: https://polar.sh/docs/api-reference/introduction en https://polar.sh/docs/integrate/oat
- Wat hij NIET kan: hoort bij precies één organisatie. Niet in de browser gebruiken. Sandbox en productie hebben aparte tokens. Bron: zelfde pagina's.
- Beperken: bij aanmaken kies je **naam, verloopdatum en scopes**. Bron: https://polar.sh/docs/integrate/oat . Beschikbare scopes (uit de broncode van Polar, https://github.com/polarsource/polar/blob/main/server/polar/auth/scope.py ) zijn onder meer: `products:read/write`, `checkout_links:read/write`, `checkouts:read/write`, `discounts:read/write`, `benefits:read/write`, `files:read/write`, `orders:read/write`, `subscriptions:read/write`, `customers:read/write`, `refunds:read/write`, `payments:read`, `metrics:read`, `webhooks:read/write`, `license_keys:read/write`, `payouts:read/write`, `transactions:read/write`, `organization_access_tokens:read/write`. Voor een publicerende agent zijn `products`, `benefits`, `files`, `checkout_links` genoeg; geef geen `payouts:write`, `refunds:write` of `organization_access_tokens:write` (mijn advies).
- Bij lekken: wordt automatisch ingetrokken door secret scanning. Bron: https://polar.sh/docs/api-reference/introduction
- Aanmaken: dashboard, Settings, Access Tokens, **Create token**, naam, verloopdatum, scopes. Ongeveer 3 minuten. Bron: https://polar.sh/docs/integrate/oat

**Blijft handwerk**
- Account review voor de eerste uitbetaling: aanvraag indienen, identiteitsverificatie (KYC) door de eigenaar van de organisatie, in Finance, Account. Bron: https://polar.sh/docs/merchant-of-record/account-reviews
- Uitbetalingsgegevens: niet in detail uitgezocht, niet bevestigd.

---

## 6. Moneybird

**Sleutel A: Personal API token**
- Wat hij kan: Bearer token voor de Moneybird API v2 (`https://moneybird.com/api/v2/<administratie_id>/...`). Bron: https://developer.moneybird.com/authentication/
- Wat hij NIET kan / risico: "It is similar to a password and gives access to your entire company account." Verloopdatum: niet genoemd, niet bevestigd. Bron: zelfde pagina.
- Beperken: met vinkjes scopes kiezen: `sales_invoices`, `documents`, `estimates`, `bank`, `time_entries`, `settings`. Voor contacten is een van `sales_invoices`, `documents`, `estimates`, `bank` of `settings` nodig. Zonder scope geldt `sales_invoices`. Bron: zelfde pagina.
- Aanmaken: inloggen, naar https://moneybird.com/user/applications/new , kiezen voor personal API token, scopes aanvinken. Ongeveer 3 minuten. Bron: zelfde pagina.

**Sleutel B: OAuth applicatie**
- Wat hij kan: Client ID en Client Secret; de eigenaar van de administratie keurt eenmalig goed, daarna access token en refresh token. Acties staan op naam van de app. Token verloopt "as of now" niet, maar Moneybird kan dat veranderen. Intrekken via `https://moneybird.com/oauth/revoke`. Bron: zelfde pagina.
- Voor één eigenaar is OAuth vooral nuttig omdat acties zichtbaar op naam van de app staan; anders is de personal token eenvoudiger (mijn afleiding).

**Vereisten:** Moneybird account. Of API toegang een betaald abonnement vereist: niet bevestigd.
**Blijft handwerk:** administratie inrichten, goedkeuring bij OAuth (één keer).

---

## 7. TikTok Shop (Partner Center / Open API)

- Beschikbaarheid: TikTok Shop opende 15 juni 2026 in Nederland; verkopers konden zich vanaf 1 juni registreren. Bron: https://newsroom.tiktok.com/tiktok-introduceert-tiktok-shop-in-nederland?lang=nl-NL
- Ontwikkelaarstypes: Seller Developer (koppelt alleen de eigen shop, Custom App), System Integrator, App Developer. Een Seller Developer moet eerst een **geactiveerde TikTok Shop** hebben en een toegewezen **Account Manager**; anders eerst via Seller Center support regelen. Bron: https://partner.tiktokshop.com/docv2/page/64f19846dc7f3e028d380988 (JS pagina; tekst gelezen via de JSON van dezelfde site)

**Sleutels: App Key en App Secret, plus per shop access_token en refresh_token**
- Wat ze kunnen: na "Create an app" krijg je App Key (id van de app) en App Secret; daarmee doe je de verkopersautorisatie en API calls (bijv. producten, orders, fulfilment, financiën). Bron: https://partner.tiktokshop.com/docv2/page/63fd743d715d622a338c4e69
- Beperken en verlopen: de access_token moet minstens elke 7 dagen ververst worden met de refresh_token, en de refresh_token zelf wordt elke 6 dagen vernieuwd. Een agent moet dus steeds het nieuwe token terugschrijven (bijv. naar een GitHub secret via API). Bron: https://partner.tiktokshop.com/docv2/page/63fd743d715d622a338c4e78 . Scopes per API pakket: niet bevestigd in wat ik las.
- Aanmaken: registreren als developer in Partner Center, wachten op review en goedkeuring, app maken, redirect URL opgeven. Tijd: niet te schatten, hangt af van goedkeuring. Bron: https://partner.tiktokshop.com/docv2/page/63fd743e715d622a338c4e9c

**Vereisten (bedrijfsregistratie)**
- Partnerregistratie vraagt: volledige bedrijfsnaam zoals in het bedrijfsdocument, registratiedatum, **company registration number**, bedrijfsdocument (afbeelding), ID van de eigenaar, adres, en mogelijk UBO gegevens. Bron: https://partner.tiktokshop.com/docv2/page/64f19899cb677b0286e75d67 . Voor Nederland betekent dat in de praktijk een KvK uittreksel (mijn afleiding; NL wordt op die pagina niet apart genoemd).
- Of digitale producten (software) via TikTok Shop verkocht mogen worden: niet bevestigd.

**Blijft handwerk:** shop openen en verifiëren, Account Manager regelen, partner en app review, eerste autorisatie van de shop, video's en LIVE posten (niet via deze API uitgezocht).

---

## 8. Garmin Connect IQ

- **Geen officiële upload API gevonden.** De officiële stappen: .iq bestand exporteren met de Monkey C extensie in VS Code, het IQ bestand uploaden naar de Connect IQ Store, daarna beschrijving en screenshots toevoegen, dan review door Garmin. Tot goedkeuring is de app niet zichtbaar. Bron: https://developer.garmin.com/connect-iq/submit-an-app/
- Een ontwikkelaar vroeg in 2025/2026 om een API voor batch uploads; Garmin heeft dat als verzoek CIQQA-4193 "Acknowledged", dus het bestaat nog niet. Bron: https://forums.garmin.com/developer/connect-iq/i/bug-reports/connect-iq-upload-applications-updates-to-store-with-the-batch-api
- Eerder forumtopic bevestigt dat automatiseren alleen kan door het webformulier na te bootsen, wat "isn't really meant to be automated". Bron: https://forums.garmin.com/developer/connect-iq/f/discussion/211559/how-can-i-automate-deployment-to-the-app-store-not-just-build-or-release/993878 (geen officiële documentatie, wel Garmin forum)
- Wat wel automatisch kan: bouwen van het .iq bestand in GitHub Actions met de SDK (exacte CLI stappen niet uitgezocht, niet bevestigd) en het bestand als artifact klaarzetten.
- Developer key: de SDK gebruikt een eigen ondertekeningssleutel om apps te bouwen; die kan als secret. Details niet uitgezocht, niet bevestigd.
- **Blijft handwerk:** elke upload (ook updates), beschrijving, screenshots, prijzen (Merchant Onboarding staat onder Monetization: https://developer.garmin.com/connect-iq/monetization/ , details niet uitgezocht).

---

## 9. GitHub

**9a. GITHUB_TOKEN (automatisch in Actions)**
- Wat hij kan: een installation access token van een GitHub App, alleen voor de repo van de workflow. Rechten per workflow of job te beperken met `permissions:`. Bron: https://docs.github.com/en/actions/concepts/security/github_token en https://docs.github.com/en/actions/tutorials/authenticate-with-github_token
- Verloopt als de job klaar is, maximaal 24 uur verversbaar. Bron: https://docs.github.com/en/actions/concepts/security/github_token
- Wat hij NIET kan: andere repo's; events die hij veroorzaakt (bijv. een push) starten op een paar uitzonderingen na geen nieuwe workflow. Bron: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow
- Aanmaken: niets te doen. Wel standaardrechten instellen in repo Settings, Actions, General, Workflow permissions (1 minuut).

**9b. Fine-grained personal access token**
- Wat hij kan: wat de eigenaar mag, maar beperkt tot gekozen rechten (read/write/admin per onderdeel). Bron: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- Beperken: één resource owner (gebruiker of organisatie), "Only select repositories", verloopdatum 1 tot 366 dagen (of geen, tenzij een organisatiebeleid dat blokkeert). Ongebruikte tokens worden na een jaar verwijderd. Bron: zelfde pagina.
- Wat hij NIET kan: meerdere organisaties tegelijk, Packages, Checks API, bijdragen aan publieke repo's waar je geen lid bent of waar je outside collaborator bent, Projects van een gebruiker. Altijd leesrecht op publieke repo's. Bron: zelfde pagina (Fine-grained personal access tokens limitations).
- Aanmaken: Settings, Developer settings, Personal access tokens, Fine-grained tokens, Generate new token, naam, verloopdatum, resource owner, repo's, rechten. Ongeveer 5 minuten. Bron: zelfde pagina.
- Nodig wanneer: een workflow een andere repo moet aanpassen of een workflow moet starten (bijv. voor Obsidian is het niet nodig, GITHUB_TOKEN volstaat).

**9c. Repository en environment secrets**
- Secrets op repo, environment of organisatie niveau. Environment secrets in een persoonlijke repo kan alleen de eigenaar aanmaken. Bron: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
- Advies: per platform een environment (bijv. `steam`, `jetbrains`) met eigen secrets en eventueel verplichte goedkeuring, zodat niet elke workflow alle sleutels ziet (mijn advies, mechanisme staat in dezelfde bron).

---

## 10. Hosting van dortus.com

Welke host nu gebruikt wordt heb ik niet gecontroleerd (niet bevestigd). Opties:

**10a. GitHub Pages (geen extra sleutel)**
- Uitrollen via een Actions workflow met `GITHUB_TOKEN` (`pages: write`, `id-token: write`); geen externe sleutel. Eigen domein kan.
- Grenzen: site max 1 GB, zachte bandbreedtegrens 100 GB per maand. Belangrijk: Pages is niet bedoeld voor een online bedrijf, e-commerce of commerciële SaaS. Een info/landingspagina die doorlinkt naar winkels is wellicht oké, maar dat oordeel is mijn interpretatie. Bron: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Pages vanuit een privé repo vereist een betaald plan: niet gecontroleerd in deze ronde, niet bevestigd.

**10b. Cloudflare API token (Pages)**
- Wat hij kan: met recht Account, Cloudflare Pages, Edit uitrollen via `wrangler pages deploy`. Bron: https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/
- Beperken: per policy kiezen welke account of zone, Read of Edit per recht, optioneel **verloopdatum** en **IP filter**. Keuze tussen user token en Account API token (niet aan een persoon gekoppeld). Bron: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
- Wat hij NIET kan: alleen de rechten die je aanvinkt; geef geen DNS Edit tenzij nodig.
- Aanmaken: dashboard, Manage Account (of My Profile), API Tokens, Create Token, Custom Token, Account / Cloudflare Pages / Edit, Continue to summary, Create Token. Ongeveer 5 minuten. Bron: zelfde pagina's.

**10c. Netlify personal access token**
- Aanmaken via Applications, Personal access tokens, met verloopdatum. Een wachtwoordreset maakt alle tokens ongeldig. Bron: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/
- Beperken per site: niet gevonden in de documentatie, niet bevestigd (lijkt toegang tot het hele account te geven).

**10d. Vercel access token**
- Scope kiezen: Full Account, Team, of **Project** (alleen één project), met verloopdatum. Bron: https://vercel.com/docs/accounts/access-tokens
- Let op: het gratis Hobby plan is alleen voor niet-commercieel, persoonlijk gebruik. Bron: https://vercel.com/docs/plans/hobby

Mijn voorkeur voor een bedrijf: Cloudflare Pages met een Account API token met alleen Pages Edit, of GitHub Pages als de site puur informatief blijft.

---

## Overzicht: wat blijft altijd handwerk voor Thijs

| Platform | Eenmalig handwerk | Steeds handwerk |
|---|---|---|
| JetBrains | account, Developer Agreement, Vendor profiel, eerste upload, token | review door JetBrains (wachten, vragen beantwoorden) |
| Blender | Blender ID, eerste upload via website, token | geen, behalve eventuele review (niet bevestigd) |
| Obsidian | Obsidian account, GitHub koppelen, plugin toevoegen in community directory | geen; eventueel draft release publiceren als we `--draft` houden |
| Steam | $100 per app, NDA en distributieovereenkomst, bank, belasting, ID, build account, eerste steamcmd login met Steam Guard | build live zetten op default branch, storepagina, prijzen; opnieuw inloggen als config.vdf token verloopt |
| Polar | account, KYC en account review, token | geen bekend |
| Moneybird | token of OAuth goedkeuring | geen bekend |
| TikTok Shop | shop met KvK gegevens, Account Manager, partner en app review | tokens elke paar dagen verversen (kan automatisch), content posten |
| Garmin | developer account | elke upload, update, beschrijving en screenshot (geen API) |
| GitHub | fine-grained token indien nodig, secrets en environments | token vernieuwen voor hij verloopt (max 366 dagen) |
| Hosting | token aanmaken, domein koppelen | geen |
