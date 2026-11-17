# Keuring van A-microsoft.md (17 nov 2026)

Keurder: tweede Claude. Alles met curl gelezen op 17 nov 2026 tussen 17:45 en 18:00 UTC, tenzij anders vermeld.

## Bewering 1: in de Copilot Plugin Catalog kom je alleen via Partner Center met bedrijfsverificatie
Oordeel: KLOPT (met één aanvulling: het is zwaarder dan A schrijft).

- Openbaar publiceren gaat alleen via Partner Center, programma "Microsoft 365 and Copilot". GEZIEN: https://learn.microsoft.com/en-us/plugins/publish en https://learn.microsoft.com/en-us/plugins/publish-plugin-publicly (beide bijgewerkt 16 nov 2026): "Submit through Microsoft Partner Center and track the review." Delen met "Only you" of "Specific users" binnen je eigen organisatie kan zonder winkel, maar dat is geen etalage.
- Eisen voor het account. GEZIEN: https://learn.microsoft.com/en-us/partner-center/marketplace-offers/open-a-developer-account: een Microsoft Entra-werkaccount, "Authority to sign legal agreements on your company's behalf", "Your company's legal business name, address, and primary contact (this can be you). We verify this information".
- Wat Microsoft precies controleert. GEZIEN: https://learn.microsoft.com/en-us/partner-center/enroll/understand-the-verification-process. Vijf controles:
  - e-mail: een zakelijk e-mailadres, "not a personal or free email account" (dus geen Gmail/Outlook.com);
  - identiteit: een overheids-ID van een gebruiker;
  - "employment verification": domeinpapieren van je eigen domein bij een erkende registrar, met bedrijfsnaam en adres;
  - "business verification": "your business is legally registered with the appropriate authority", met een inschrijvingsbewijs;
  - soms nog een extra controle.
- Lukt dat voor een eenmanszaak in NL? GOK: ja, als Thijs zich bij de KvK inschrijft. Een KvK-uittreksel is een "registration" bij de bevoegde instantie, en "primary contact (this can be you)" laat zien dat één persoon mag. Zonder KvK: nee, want de bedrijfscontrole vraagt een inschrijving. Let op de verborgen eisen die A mist: een eigen domein met papieren op bedrijfsnaam en een e-mailadres op dat domein. Op het Tech Community-forum staan veel klachten over afgewezen verificaties (zoekresultaten, niet gelezen), dus afwijzing is een echt risico.
- Hoe lang? GEZIEN: "In most cases, the process takes three to five business days", "some checks might take longer". De WIQD-gids zegt "several business days". Daarna nog de keuring per plugin (duur ONBEKEND). Samen met KvK-inschrijving (online afspraak, meestal binnen een paar dagen, GOK) is 7 dagen krap tot onhaalbaar. A's GOK van 1 tot 3 weken is redelijk.

## Bewering 2: de catalogus heeft geen eigen kassa
Oordeel: KLOPT, met een kleine kanttekening.

- GEZIEN: de openbare inventaris van de catalogus (https://res.cdn.office.net/taos-platsvcs-controlplane/public-metadata/public-catalog.json, stand 29 okt 2026, 653 items) heeft geen enkel veld voor prijs, aankoop, abonnement of licentie. Per plugin staan er alleen naam, uitgever, beschrijving, skills, connectors en een winkellink.
- GEZIEN: https://learn.microsoft.com/en-us/plugins/publish-plugin-publicly zegt alleen "State whether the plugin requires additional purchases". Er is geen stap om een prijs in te stellen.
- Kanttekening: voor Teams-apps in hetzelfde Partner Center-programma kun je een "transactable SaaS offer" koppelen, waarbij Microsoft de betaling regelt (https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/prepare/include-saas-offer, bijgewerkt 27 nov 2024). Dan moet je zelf een landingspagina en de SaaS Fulfillment API bouwen. Of dat ook voor Copilot-plugins kan: ONBEKEND, de plugin-docs noemen het niet. In de praktijk dus: geen kassa in de winkel, alleen je eigen abonnement buiten de winkel.

## Bewering 3: een IT-beheerder moet elke plugin eerst toestaan
Oordeel: DEELS.

- GEZIEN: https://learn.microsoft.com/en-us/plugins/publish: "Each customer's administrator still installs the plugin, allows its publisher category, and sets availability."
- Maar "elke plugin" is te streng. GEZIEN: https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers (bijgewerkt 16 nov 2026): de beheerder kiest onder Agents > Settings > Agent and plugin access welke groepen uitgevers gebruikers mogen "discover and install": Microsoft, de eigen organisatie, of "certified external publishers". Zet de beheerder die laatste groep aan, dan installeren gebruikers zelf, zonder goedkeuring per plugin. Staat hij uit, dan ziet de gebruiker de plugin wel, met "This plugin is blocked by your organization's policy", en kan hij op "Request access" klikken. Dan beslist de beheerder.
- Wat er standaard aanstaat: ONBEKEND. Ik heb de standaardinstelling nergens gevonden. De gebruiker blijft dus afhankelijk van de keuze van zijn IT-afdeling. Dat is een poort, maar niet per plugin.

## Book of News Microsoft Ignite 2026
- Adres gevonden: https://news.microsoft.com/events/ignite/2026/book-of-news/ (A probeerde een verkeerd adres, news.microsoft.com/ignite-2026-book-of-news/, dat geeft nog steeds 404).
- Stand om 17:53 UTC (curl): de pagina zegt letterlijk "The Book of News will be available at the conclusion of Chairman and CEO Satya Nadella's keynote on Nov. 17." De keynote begon om 18:00 UTC; de inhoud stond er dus nog niet. Inhoud: ONBEKEND.
- Live-blog: https://news.microsoft.com/events/ignite/2026/live-news/ had om 17:52 UTC nog geen aankondigingen.
- Officiële feeds (blogs.microsoft.com, news.microsoft.com/source, blogs.windows.com), stand 17 nov rond 17:50 UTC: geen bericht over een nieuwe winkel, kassa, Agent Store of betalen per gebruik voor kleine makers. Wel: Copilot harness (28 okt 2026), Agent 365 en beheer.
- "Windows Agent Store" met 85% voor de maker: NIET GEVONDEN bij een primaire bron. Het staat op byteiota.com (auteur "ByteBot", 1 juni 2026), fourweekmba.com en rework.com, maar geen van die stukken linkt naar Microsoft. Het officiële Build 2026-bericht van Windows (https://blogs.windows.com/windowsdeveloper/?p=57809) bevat de woorden "Agent Store", "Agent Gallery" en "revenue share" niet. De docs-pagina learn.microsoft.com/en-us/windows/ai/agent-framework/ geeft 404. Dit lijkt verzonnen door AI-sites; ik behandel het als niet bestaand tot Microsoft zelf het noemt.
- Advies: na ongeveer 19:30 UTC (einde keynote) opnieuw curl op het adres hierboven en zoeken op "store", "marketplace", "monetiz", "pay-per-use", "Agent Store".

## Eindoordeel over het werk van A
Netjes en eerlijk werk. De drie hoofdbeweringen houden stand. Correcties: (1) de verificatie vraagt ook een eigen domein en zakelijk e-mailadres, niet alleen KvK; (2) de IT-poort zit per groep uitgevers, niet per plugin, al blijft de gebruiker afhankelijk van IT; (3) het Book of News staat op een ander adres dan A probeerde.

Cijfer Copilot Plugin Catalog blijft 5 (wet 1 en wet 3 vallen af, wet 4 twijfel door Microsofts eigen skillpakketten). De rest van A's lijst krijgt van mij hetzelfde of lager.

## Mijn top
Niets haalt een 7. Beste kans blijft de Copilot Plugin Catalog (5), alleen als Thijs een eenmanszaak met KvK, eigen domein en zakelijk e-mailadres regelt en we gratis bereik willen testen. Het Book of News kan dit nog veranderen; dat moet na de keynote opnieuw bekeken worden.
