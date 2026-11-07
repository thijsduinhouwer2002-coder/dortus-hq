# Middelen: alle sites en programma's die Dortus gebruikt

Bijgehouden door de hele ploeg. Begin je iets nieuws te gebruiken (site, programma, dienst, account)? Zet het hier meteen bij. Stop je ermee? Zet het onder "Gestopt".

Kolom **Inloggen** zegt wie er mag inloggen:
- **Claude (lezen):** Thijs logt in in de browser van zijn Claude desktop-app, zodat Claude cijfers kan lezen als zijn computer aan staat. Let op: de geplande runs draaien in de cloud en kunnen die inlog niet gebruiken (niet getest).
- **Alleen Thijs:** hier kan geld worden uitgegeven, iets definitief gebeuren of iets onder zijn naam worden gepost. De ploeg zet het klaar op `lijst-thijs.md`.
- **Geen:** openbaar, of de ploeg heeft al toegang.

## Waar we werken

| Wat | Waarvoor | Inloggen |
|---|---|---|
| [Claude](https://claude.ai), project Dortus-HQ | De ploeg: geplande taken, de projectchat met Thijs | Alleen Thijs |
| [GitHub: dortus-hq](https://github.com/thijsduinhouwer2002-coder/dortus-hq) | Hoofdkwartier: regels, rollen, logboeken, rapporten, code | Geen (ploeg heeft toegang). Insights lezen: Claude (lezen) |
| [GitHub: dortus](https://github.com/thijsduinhouwer2002-coder/dortus) | De website dortus.com | Geen (ploeg heeft toegang) |

## De cloudomgeving van de ploeg

- **Wat het netwerk van de runs bepaalt:** de runs zijn aangemaakt vanuit de projectchat. Daarvoor geldt de instelling in claude.ai: Instellingen > Capabilities > "Use the internet while making files" > Allowed websites. Die staat sinds 6 nov 2026 16:55 op **Any website** (gecontroleerd: JetBrains Marketplace, Gradle en Shopify geven 200). Let op: dit geldt voor het hele (gedeelde) account.
- De Code-omgeving **Default** (claude.ai/code) staat ook op Network access Full, maar dat bleek niet de instelling die de runs gebruiken.
- **Network secrets:** hier komen sleutels per platform (bijvoorbeeld een upload-sleutel van JetBrains), zodat de ploeg zonder browser kan publiceren. Nooit Thijs' Google-wachtwoord of een ander wachtwoord. Een sleutel mag maar één ding kunnen en moet in te trekken zijn.

## Website en mail

| Wat | Waarvoor | Inloggen |
|---|---|---|
| [dortus.com](https://dortus.com) | Productpagina's, privacy, support (alleen eigen productmappen, zie `regels.md`) | Geen |
| Hosting van dortus.com | GOK: GitHub Pages (er staat een CNAME-bestand in de repo). Thijs: bevestig | Alleen Thijs |
| Domein dortus.com (registratie, DNS) | Waar het domein geregistreerd is: **onbekend, Thijs vult in** | Alleen Thijs |
| support@dortus.com | Supportadres op alle winkelpagina's. Mailaanbieder: **onbekend, Thijs vult in**. Werkt: bevestigd door Thijs op 7 nov 2026. Thijs heeft ook thijs@dortus.com (alleen voor Thijs zelf, niet op winkelpagina's) | Alleen Thijs |
| [Google Search Console](https://search.google.com/search-console) | Hoe vaak mensen onze pagina's via Google vinden | Claude (lezen), zodra de eerste productpagina live staat |

## Platformen

| Wat | Waarvoor | Inloggen |
|---|---|---|
| [JetBrains Marketplace](https://plugins.jetbrains.com) | Onze JetBrains-plugins: downloads, verkopen, reviews | Dashboard: Claude (lezen). Uploaden: Alleen Thijs |
| [JetBrains Account](https://account.jetbrains.com) | Verkopersprofiel, uitbetaling, voorwaarden | Alleen Thijs |
| [Obsidian pluginlijst](https://github.com/obsidianmd/obsidian-releases) | Plugins vergelijken, ons gat controleren | Geen |
| [community.obsidian.md](https://community.obsidian.md) | Obsidian-plugin indienen (met Thijs' GitHub) | Alleen Thijs |
| [forum.obsidian.md](https://forum.obsidian.md), Reddit, Discord | Lanceerberichten onder Thijs' naam | Alleen Thijs |

## Inloggen met Google

Thijs logt overal in met zijn eigen Google-account (keuze Thijs, 6 nov 2026). Een Claude met de browser kan daardoor op veel sites binnenkomen zonder wachtwoord. Daarom geldt:
- Gebruik die inlog alleen voor sites met **Claude (lezen)** in de tabellen hierboven, en alleen om te lezen.
- Open nooit Gmail, Google Drive, de instellingen van het Google-account of Google-betalingen.
- Klik nooit op betalen, kopen, voorwaarden accepteren, verwijderen of plaatsen, ook niet als het kan. Zet zo'n stap op `lijst-thijs.md`.

## Nooit voor Claude

Bank, betaalgegevens, de mailbox zelf, domein en DNS, het Google-account zelf.

## Gestopt

| Wat | Sinds | Waarom |
|---|---|---|
| Atlassian Marketplace | 6 nov 2026 | Te weinig kans op installs. Oude pagina's op dortus.com blijven staan |
