# Voorstel: Whop App Store (pionier)

Noor, pionier. Run 8 nov 2026, ±05:45 tot ±06:35 UTC. Onderzoeker (agent) voor groei, geld, vraag en wie er bouwt. Zelf nagekeken: de openbare app-lijst van Whop (alle 191 apps, eigen telling via de API) en de installs per app op elke apppagina (alle 191, eigen meting), de docs over betalen in de app, en de financieringsronde van oktober. Herhaalscript: `data/whop-apps-meet.py`, eerste meting in `data/whop-apps-2026-11-08.json`. Geen aparte controleur: het advies is geen ja, en de kerncijfers heb ik zelf gemeten.

**Cijfer: 5 van 10. Advies: nog niet klaar. Herhaalmeting rond 22 nov en 8 dec.** Whop is het hardst groeiende platform dat ik tot nu toe zag, met een winkel die jong en nog bijna leeg is (191 apps), betalen in de app werkt al, en installs per app zijn openbaar te meten. Dat is precies het soort plek dat Thijs zoekt. Maar de winkel is van Whop zelf: de eigen apps van Whop halen 97% van alle installs, en alle 161 apps van buitenstaanders samen halen ±3.000 installs per week. Of een buitenstaander daar nummer één kan worden in een categorie, zien we pas als die weektelling stijgt. Daarom nu nog geen ja.

Wat is Whop: een platform waar makers (vooral cursussen, trading-groepen, sportvoorspellingen, communities en software) abonnementen en digitale producten verkopen. Elke verkoper heeft een "whop", een eigen plek met apps erin. Een app van Whop of van een buitenstaander draait in die whop, op het web en in de mobiele app van Whop.

## 1. Groeit het platform hard en zichtbaar? Ja, heel hard.

- Omzet van Whop: $23M (begin 2024), $56M (eind 2024), $142M per jaar in oktober 2025, +255% op jaarbasis (DERDEN, https://sacra.com/research/whop-at-142m-revenue). In 2026 meldt Whop zelf meer dan $400M per jaar en ±25.000 verkopers die samen ±$550M per maand omzetten (DERDEN, https://europeanbusinessmagazine.com/?p=145417; datum in dat artikel onduidelijk).
- Financiering: $17M (2023), $50M bij $800M waarde (juni 2024), $200M van Tether bij $1,6B (feb 2026), en **$205M bij $5,1B onder leiding van Sequoia met Shopify Ventures (22 okt 2026)** (GEZIEN, kop en datum op https://techfundingnews.com/whop-raises-205m-at-5-1b-valuation-as-sequoia-reverses-its-earlier-pass/; eerdere rondes DERDEN, https://en.wikipedia.org/wiki/Whop.com).
- Mobiele app van Whop: 3,1 miljoen installs op Android, +26.000 per week (DERDEN, schatting van https://appgoblin.info/apps/com.whop.whopapp); iOS 60.083 beoordelingen, gemiddeld 4,82 (GEZIEN door de onderzoeker via de iTunes-API).
- Eigen meting: de standaard-app Forums kreeg **84.070 installs in de laatste 7 dagen**, op 325.935 in totaal (GEZIEN, `data/whop-apps-2026-11-08.json`). Een kwart van alle Forums-installs ooit kwam deze week. Dat wijst op heel veel nieuwe whops, al kan een wijziging bij Whop (Forums standaard aan in nieuwe whops) dit ook verklaren (GOK).
- Motor: veel geld van grote partijen (Sequoia, Shopify Ventures, Tether), en Whop zet hard in op bouwen met AI (CLI, plugin voor Claude Code, hosting op whop.site) (GEZIEN, https://docs.whop.com/llms.txt).

## 2. Is de winkel jong? Ja.

- De App Store opende in juni 2025 (DERDEN, Sacra); de blog meldde op 12 sep 2025 "The Whop App Store is live", met wedstrijden en geldprijzen voor bouwers (GEZIEN door de onderzoeker, https://whop.com/blog/whop-app-store/).
- Nu **191 apps** (GEZIEN, eigen telling, `GET https://api.whop.com/api/v1/apps`, werkt zonder sleutel). Daarvan 30 van Whop zelf en 161 van buitenstaanders (eigen indeling op bedrijfsnaam, `data/whop-apps-2026-11-08.json`). Dat is ±11 apps per maand sinds de opening: weinig voor een platform van deze omvang.
- Categorieën in de winkel: Community, Business, Games, Sports, Social Media, Trading, AI, Education, E-commerce, Health, Travel (DERDEN, https://docs.whop.com/whop-apps/whop-app-store.md).
- Niet gemeten: wanneer elke app erbij kwam (de API geeft geen datum). Met het herhaalscript zien we vanaf nu hoeveel apps er per maand bijkomen.

## 3. Kan er betaald worden? Ja, nu al.

- In de app: `inAppPurchase` uit de iframe-SDK opent de betaalmodule van Whop voor eenmalige aankopen of abonnementen (GEZIEN, https://docs.whop.com/developer/guides/iframe.md). Kosten 2,7% + $0,30 per betaling, plus 1,5% bij buitenlandse kaarten (GEZIEN door de onderzoeker, https://docs.whop.com/payments-and-billing/fees/fees.md).
- Een app kan dus de verkoper laten betalen (abonnement voor een dashboard-app) of de leden (iets kopen in de app). Een vaste afdracht aan Whop op app-omzet vond de onderzoeker niet in de docs. De blog noemt voorbeeldmodellen: een installatieprijs, 10 tot 30% van de omzet die de app oplevert, of $1 per lid per maand (GEZIEN door de onderzoeker, blog). Dat zijn voorbeelden, geen regeling.
- Pluspunt: de klanten in deze winkel verdienen zelf geld op Whop. Zo'n koper betaalt eerder voor een app die omzet oplevert dan een hobbygebruiker (GOK).

## 4. Is er al vraag te zien? Zwak bewezen.

- Installs zijn openbaar per app (`totalInstalls` en `totalInstallsLast7Days` in de broncode van whop.com/apps/<id>/). Eigen meting: mediaan 16 installs per app; 43 van de 191 apps boven 100 (GEZIEN).
- **De eigen apps van Whop halen ±99.100 van de ±102.100 installs van de laatste week. Alle 161 apps van buitenstaanders samen: 2.987 installs per week, 11.293 in totaal** (GEZIEN, eigen meting). Maar 4 buitenstaanders zitten boven 500 installs: Digital Products AI 1.892 (560 in 7 dagen), YouTube AI Video Clipper 1.547 (414), Dashboard Agent 707 (127), Website Embed 530 (137; bedrijfsnaam "Steven", mogelijk van Whop zelf). Content Rewards (8.194) telde ik als Whop, maar dat is niet zeker.
- Wat er wel loopt bij buitenstaanders: AI die producten of clips maakt, e-mail en winback, upsell en checkout, boeken en agenda (booking 2 apps samen 506, calendar 3 samen 360) (GEZIEN, eigen telling op naam).
- Forums, Reddit en Discord kon de onderzoeker niet lezen (Reddit 403, Trustpilot botcheck). Klachten volgens een review: geld dat vastgehouden wordt, onduidelijke uitbetalingen, wisselende kwaliteit in trading en "snel rijk" (DERDEN, https://fritz.ai/whop-app-review/).

## 5. Is de eerste plek in een categorie nog te pakken? Ja, maar Whop pakt de kern zelf.

Eigen telling op naam (ruw):
- Analytics: 1 app (Subscription Analytics, 77 installs). Affiliate: 1 (80). Referral: 0. Leaderboard: 2 (samen 18). Quiz: 4 (samen 34). Sport en wedden: 7 apps, samen ±70 installs, terwijl sportvoorspellingen een van de grootste groepen verkopers op Whop zijn (DERDEN, Sacra). Trading-tools: 5, samen 493.
- Dus in bijna elke categorie buiten de basis is er geen sterke nummer één. Het risico: Whop bouwt de basis zelf en wint dan meteen (Forums, Chat, Courses, Content, Files, Livestreaming, Events, Telegram, Discord: allemaal Whop). Whop heeft ook al eigen analytics en een eigen affiliate-programma in het dashboard (GOK op basis van de docs, niet nagekeken per functie). Een categorie die Whop zelf waarschijnlijk niet bouwt: **tools voor sportvoorspellers** (pick-tracker met ROI per pick, ranglijst van leden, controleerbaar track record). Grote groep verkopers, nu ±70 installs verspreid over 7 zwakke apps.

## Risico: haalt het platform het, en haalt een app van buiten het?

- Platform: weinig twijfel dat Whop blijft groeien op korte termijn (geld, omzet, Sequoia). Risico's: reputatie (veel "snel rijk", trading en wedden), regels rond gokken en financieel advies, en Whop dat meer zelf bouwt.
- Voor ons: het teken dat het stokt is als de weekinstalls van buitenstaanders vlak blijven (nu 2.987) terwijl Forums blijft stijgen. Dan is de winkel een etalage voor Whop zelf.
- Reputatie voor Dortus: een tool voor sportvoorspellers zit dicht tegen gokken aan. Een pick-tracker zonder wedtips of affiliate-links naar bookmakers houdt dat schoon (GOK).

## Eerste productidee

**Pick Tracker voor sportgroepen**: de verkoper zet zijn picks in de app, de uitslag wordt automatisch of met één klik bijgewerkt, leden zien een eerlijk track record (winst, ROI, reeks) dat de verkoper niet kan wissen, plus een ranglijst als leden zelf meespelen. Betalen: abonnement voor de verkoper via Whop ($19 tot $49 per maand, GOK). Waarom wij: de huidige apps in sport halen samen ±70 installs, dus er is geen nummer één; en een controleerbaar track record helpt eerlijke verkopers precies tegen de klacht over oplichters.

## Advies

Nog niet klaar, cijfer 5. Over twee weken (rond 22 nov) opnieuw meten met `python3 data/whop-apps-meet.py` en vergelijken met de meting van 8 nov:
- **Ja (cijfer 6 of 7)** als de weekinstalls van buitenstaanders duidelijk stijgen (boven ±4.500 per week) of als er nieuwe buitenstaanders boven 1.000 installs komen, en de sportcategorie nog leeg is.
- **Nee** als buitenstaanders vlak blijven of Whop een eigen app in de sportcategorie uitbrengt.
Voor de hoofdmanager: dit is het enige platform tot nu toe waar groei, een jonge winkel, betalen en openbare installs alle vier tegelijk kloppen. Het enige zwakke punt is vraag 4, en die is met het script binnen weken te meten.
