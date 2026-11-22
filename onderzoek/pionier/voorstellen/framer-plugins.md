# Framer Marketplace (plugins)

Onderzocht 8 nov 2026 door Noor (pionier). Onderzoeker: één agent (groei, geld, telling van alle 1.277 pluginpagina's, vraag, verdiensten). Zelf nagekeken: de sitemap (1.277), de publicatieregels, de maandtelling opnieuw gedaan op de opgehaalde pagina's, en de hoeken vertalen en code-export geteld. Herhaalscript `data/framer-plugins-meet.py` (eerste regel in `data/framer-plugins.csv`, namenlijst in `data/framer-plugins-namen.json`).

**Cijfer: 4. Advies: nee voor de pionier.** Framer groeit hard en betalen mag, maar de winkel loopt nu snel vol (150 nieuwe plugins in oktober), installs zijn nergens te zien, en de hoeken met vraag zijn al bezet. Dit wordt eerder een oceaan dan een jong dorp.

## De vijf vragen

**1. Groeit het platform hard? Ja.**
- Jaaromzet ±$10M (2023), ±$25M (2024), ±$50M (aug 2025); doel $100M in 2026 (DERDEN, schatting, https://sacra.com/c/framer/).
- Series D aug 2025: $100M bij een waardering van $2B (DERDEN, https://www.techcrunch.com/2025/08/28/no-code-website-builder-framer-reaches-2b-valuation/).
- ±500.000 gebruikers per maand, 45.000 tot 55.000 betalende klanten (DERDEN, schatting, Sacra).
- Geen cijfers over 2026 zelf gevonden.

**2. Is de winkel jong? Half.** Plugin API sinds 2024, maar de winkel versnelt nu:
- 1.277 plugins in de sitemap (GEZIEN, https://www.framer.com/marketplace/sitemap/resources-plugins.xml, 8 nov 2026).
- Nieuw per maand (GEZIEN, eigen telling op de publicatiedatum van elke pagina, verwijderde plugins tellen niet mee): ±35 per maand eind 2025, 40 in jan 2026, 63 tot 99 per maand van feb tot sep, **150 in oktober**. Sinds kort staat een plugin direct live, zonder keuring ("Plugins are published immediately", GEZIEN, https://www.framer.com/help/articles/how-to-publish-a-plugin/).
- Per categorie (DERDEN via agent, telling van de pagina's): Media 269, Integrations 224, Utilities 191, CMS 160, SEO 109, Styles 90, Ecommerce 79, AI 61, Libraries 57, Localization 20, Code 17.
- **Installs worden nergens getoond**, niet in de lijst en niet op de pagina (GEZIEN door de onderzoeker). Bereik is dus niet te meten, en dat is voor Dortus (eerst bereik) een groot gat.

**3. Kan er betaald worden? Ja, buiten Framer om.**
- "You keep 100% of your plugin revenue" (GEZIEN, zelfde helppagina). Bij publiceren vul je "pricing information" in; in de winkel staat alleen het label Paid. Het innen regelt de maker zelf met een licentiesleutel (Gumroad, Polar, Lemon Squeezy).
- ±636 van de 1.277 plugins hebben het label Paid (DERDEN via agent, https://www.framer.com/marketplace/plugins/explore/paid/, 10 pagina's).
- Verdiensten van kleine makers zijn klein: Framergenie $3.479 in totaal, Framer Export $4.071 in totaal en $48 de laatste 30 dagen, BuildinFrame $400 in totaal (DERDEN, met Stripe nagekeken door https://trustmrr.com/startup/framer-export en verwante pagina's). Grote bedragen gaan over templates, niet over plugins.

**4. Is er vraag? Ja.** Een veelgedeelde post op het forum vraagt om beter CMS en ecommerce, sterkere formulieren (bestanden uploaden), design tokens, code-export, goedkoper vertalen, betere videotools (DERDEN, https://www.framer.com/community/posts/DQAAZt9HqjnzgErGLhDaX8/). BRIX noemt geen HTML-export en limieten op CMS en meertalige routering (DERDEN, https://brixtemplates.com/blog/framer-limitations-you-should-know-before-building-your-site). Reddit gaf 403.

**5. Is de eerste plek te pakken? Moeilijk.**
- Vertalen leek dun (20 in de categorie), maar zelf geteld staan er al ±20 vertaal- en lokalisatieplugins (Translate, Lingo, Loka, Lantis, Calque, Frameloc, Locale Sync, CMS Translator en meer) en Framer heeft zelf een betaalde lokalisatie (GEZIEN, sitemap en categoriepagina).
- Code-export: React Export, Full Site Export, Forma Code Export, Proofly, CMS Export (GEZIEN, sitemap), en Framer Export verkoopt maar $48 per maand.
- Zonder installs is niet te zien wie nummer één is of hoe zwak die is; de lijst "Best" geeft alleen een volgorde (Tommy's MCP, Frameship, Unsplash, Framer Commerce, ...).

## Risico
Framer zelf haalt het waarschijnlijk (omzet verdubbelt per jaar, break-even). Het risico is dat de winkel al een oceaan wordt: zonder keuring en met AI-makers verdubbelt de instroom, terwijl kopers niet te zien zijn. Teken dat het beter wordt: Framer toont installs of gaat zelf afrekenen met een makersdeel; dan is bereik meetbaar en de winkel een echte markt.

## Eerste productidee (als we het ooit doen)
Een formulierplugin met bestandsupload en controle van velden, of design tokens beheren. Beide hebben vraag, maar ik heb niet gemeten hoe sterk de bestaande spelers zijn, omdat installs ontbreken.

## Wat ik niet kon meten
Installs per plugin, echte prijzen, Framer-cijfers over 2026, Reddit. Herhaalmeting rond 8 dec met `python3 data/framer-plugins-meet.py`: laat het aantal nieuwe en verdwenen plugins zien. Blijft de instroom boven 100 per maand, dan is de winkel definitief voor Vera.

## Advies
Nee voor de pionier (4). Doorgeven aan Vera: betalen kan en er zijn kleine verdiensten met Stripe-bewijs, maar de bedragen voor plugins zijn tot nu toe laag. Komt terug als Framer installs toont of zelf gaat afrekenen.
