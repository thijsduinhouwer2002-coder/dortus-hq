# Keuring van G (omzet makers) en H (winkels met cijfers)

Onafhankelijke keurder, wo 18 nov 2026 ±19:10 NL. Ik deed het onderzoek niet zelf. Alle bronnen opnieuw gelezen met curl (snapshots van vandaag). Niets gecommit.

**Kort oordeel:** de getallen zelf kloppen bijna allemaal; de fouten zitten in wat er met de getallen gedaan wordt. Vier van de twaalf zijn verouderd, half gelezen of te gunstig uitgelegd (FriendFilter, Save Bulk Gmail, RevenueCat 17%, Figma). Beide ranglijsten zijn te rooskleurig over de kans, en H bepleit twee kanalen (Shopify, Atlassian) waar Thijs al eerder nee op zei of die Dortus al zelf mat met slechte uitkomst.

---

## 1. Steekproef: 12 getallen die de conclusies dragen

| # | Getal (wie) | Bron die ik las | Oordeel | Wat wijkt af |
|---|---|---|---|---|
| 1 | Shopify neemt 0% tot $1 mln (H) | [shopify.dev revenue-share](https://shopify.dev/apps/store/revenue-share) | **KLOPT** | Letterlijk: "You keep 100% of your first $1,000,000 USD in lifetime gross app revenue, and 85% of earnings above that". Plus 2,9% verwerking. Alleen omzet vanaf 1 jan 2025 telt, en alleen voor bedrijven onder $100 mln omzet. |
| 2 | Shopify betaalde $1,3 mld uit, 21.000+ apps; Kaching $0,9 naar $4,3 mln, Locksmith 162.000 installs (H) | [shopify.com/news](https://www.shopify.com/news/billion-dollar-ecosystem), 28 apr 2026 | **KLOPT** | "paid out more than $1.3 billion to the developers who build across its ecosystem": het hele ecosysteem, niet alleen de App Store. Kaching heeft nu 40 mensen, Lightward 12; dat zijn geen kleine teams meer. |
| 3 | Shopify top 1% pakt ±72% (H) | [RevenueHunt](https://revenuehunt.com/state-of-the-shopify-app-economy/), juni 2026 | **KLOPT** (als schatting) | "72% of revenue earned by the top 1% ... Estimated". Omzet is gemodelleerd uit prijzen en reviews, niet gemeten. Zelfde bron: maar ±36% van de apps verdient iets, 51% heeft 0 reviews. RevenueHunt verkoopt zelf een Shopify-app. |
| 4 | 17% van nieuwe abonnementsapps haalt $1.000 per maand, 4,6% haalt $10.000; betaalmuur ±6x freemium (G en H) | [9to5Mac](https://9to5mac.com/2026/03/04/new-report-looks-into-the-sustainability-of-the-subscription-app-market-for-2026/) en het rapport zelf, [revenuecat.com/state-of-subscription-apps](https://www.revenuecat.com/state-of-subscription-apps/) | **KLOPT DEELS** | Getal klopt (17,3%). Maar de definitie is: "share of newly-launched apps that hit revenue milestones in their first 2 years". Dus: ooit één maand $1.000 aangetikt, binnen 2 jaar, en alleen apps die RevenueCat gebruiken (al ingericht om te verdienen). G en H schrijven "haalde in 2025 $1.000 per maand", wat klinkt als een vast inkomen. Blijvend $1.000 is minder vaak. |
| 5 | Stencil AI: 30d $58.015, sinds jan $486.788, ±$48.700 per maand (G) | [trustmrr stencil-ai.md](https://trustmrr.com/startup/stencil-ai.md) | **KLOPT** | Precies zo. Sterker dan G schrijft: profiel zegt "Team size: 1 person", "Bootstrapped", 17 volgers op X. Niet te koop. Omzet vlak sinds juli (±$62.000 per maand). |
| 6 | Boothie: 30d $54.680, totaal $207.972, alleen TikTok (G) | [trustmrr boothie.md](https://trustmrr.com/startup/boothie.md) | **KLOPT** | Getallen en kanaal kloppen. Niet vermeld door G: "Listed for sale", vraagprijs $900.000 (±1,4x jaaromzet, laag: de markt verwacht dat dit zakt), winstmarge 55% (AI-kosten). |
| 7 | House Goals: 30d $9.868, sinds jun $60.099 (G, voorbeeld nr. 1 bij "hoe") | [trustmrr house-goals.md](https://trustmrr.com/startup/house-goals.md) | **KLOPT DEELS** | Getallen kloppen, het beeld niet. Per maand: aug $20.685, sep $19.200, okt $12.725; 30 dagen -37%. Team "2 tot 5 mensen", te koop voor $600.000. Een dalende app die in de verkoop staat is geen sterk voorbeeld van "zo doe je het". |
| 8 | FriendFilter: 30d $6.904 (G: "stand 18 nov"); ±$8.000 tot $12.000, 337 abonnees (H) | [trustmrr friendfilter-groupfilter.md](https://trustmrr.com/startup/friendfilter-groupfilter.md) | **KLOPT DEELS** | De Stripe-koppeling is verlopen op 18 sep 2026; sindsdien staat alles op $0. Het 30d-getal is dus van september, niet van november. 12m/12 $8.598 klopt. Trend dalend: $12.000 per maand in dec tot apr, $8.000 in jul en aug. De $11.300 MRR in de omschrijving is een verkooptekst van de maker. |
| 9 | Save Bulk Gmail Attachments haalt $1.218 per maand, 142 abonnees (H) | [trustmrr save-bulk-gmail-attachments.md](https://trustmrr.com/startup/save-bulk-gmail-attachments.md) | **KLOPT DEELS** | $1.218 was de beste maand (okt). MRR nu $711, 30d $976, 143 abonnementen, totaal $6.698 na 18 maanden (±$540 per maand gemiddeld over 12 maanden). Haalt de strenge $1.000-toets van G niet. H gebruikt de piek als "haalt". |
| 10 | Freemius: maker verdient gemiddeld $43.000 per jaar (H) | [freemius.com year-in-review-2024](https://freemius.com/blog/year-in-review-2024/) | **KLOPT** | "A software maker on Freemius now earns an average of $43,000 annually", alleen makers die dat jaar meer dan $1.000 verkochten. Het is een gemiddelde, getrokken door makers boven $700.000. Geen mediaan. Freemius doet sinds kort ook SaaS, dus niet alleen WordPress. |
| 11 | Atlassian: 0% op Forge tot $1 mln; $7 mld omzet, laatste $1 mld in 9 maanden (H) | [atlassian updates 2026](https://www.atlassian.com/blog/developer/updates-to-marketplace-revenue-share-2026), [$7 billion](https://www.atlassian.com/blog/teamwork/atlassian-marketplace-7-billion) (26 okt 2026) | **KLOPT** | Letterlijk zo. Voorwaarde: alleen "eligible" Forge-apps (alleen Forge-modules, Forge-login, Forge-UI). $7 mld is verkoop aan klanten sinds 2012, inclusief oude Server en Data Center; H's rekensom "$220.000 per cloud-app per jaar" deelt die door alleen de cloud-apps en is dus te hoog. |
| 12 | Figma laat geen nieuwe verkopers toe (H) | [Figma Help](https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources), [Figma Forum](https://forum.figma.com/ask-the-community-7/can-plugins-still-use-figma-native-payments-monetization-54336) | **KLOPT DEELS** | De zin staat er, maar gaat over bestanden: "We are not approving new creators to sell paid **files**". Figma-medewerker op het forum (27 mei 2026): "If you want to sell plugins/widgets, you do not need approval", Stripe in een toegestaan land is genoeg (Nederland staat op de lijst). De Nederlandse maker met de dichte prijsknop schreef op 12 jul (niet mei) en werd naar moderatie verwezen: één geval, geen beleid. "Figma is dicht" klopt dus niet voor plugins. De eindconclusie (Figma zwak) blijft wel staan op G's cijfers: Figma-plugins op TrustMRR doen $0 tot $62 per maand. |

**Extra nagekeken, KLOPT:** [trustmrr.com/stats](https://trustmrr.com/stats): 67,8% onder $1k, 17,0% tussen $1k en $10k, mediaan totale omzet RevenueCat $391, Superwall $2.610, Stripe $265 (54,1%), r = 0,25 bij n = 6.388. En [Respira](https://trustmrr.com/startup/respira-for-wordpress-1.md): 30d $12.094, MRR $7.532, 1 persoon, betaalt via **Polar**, eerste omzet april 2026.

**Telling:** 7 KLOPT, 5 KLOPT DEELS, 0 KLOPT NIET, 0 NIET TE CONTROLEREN. Geen verzonnen getallen gevonden. Wel: verouderde stand (8), piek als normaal (7, 9), definitie te ruim (4), half gelezen (12).

---

## 2. Tegenspraak tussen G en H

| Punt | G zegt | H zegt | Wie heeft gelijk |
|---|---|---|---|
| **Nummer 1** | Mobiele abonnementsapp | Shopify App Store (mobiel pas 5e) | **G heeft het beter gemeten getal, H heeft de betere redenering over wie betaalt; geen van beiden past bij Dortus (zie 4).** G's 17% is een echt gemeten getal over 115.000 apps. H's "±1 op 4 serieuze pogingen" bij Shopify is een GOK zonder meting, en botst met Dortus' eigen meting: Vera vond op 7 nov dat een gewone nieuwe Shopify-app in 2 tot 6 maanden zelden 100 installs haalt (±2 tot 6 van de 100, `organisatie/besluiten.md` 7 nov). RevenueHunt zegt zelf dat maar 36% iets verdient. Op bewijs wint G. Het hangt af van één ding: **heeft het product een verspreidingsmotor?** De mobiele winnaars hebben TikTok of advertenties (TrackAI: Meta-advertenties); zonder die motor is de mobiele mediaan een paar honderd dollar totaal. Shopify geeft de koper wel aan, maar alleen aan apps met reviews. |
| **Atlassian** | Niet genoemd | Nummer 3 | **G, bij gebrek aan bewijs.** H vond geen enkele kleine maker met omzet, noemt het zelf "een gat in ons onderzoek", en schrijft "niemand van ons keek ernaar". Dat klopt niet: Dortus had Atlassian-apps, Thijs stopte ermee op 6 nov ("te weinig installs, markt verzadigd") en `doelen.md` zegt "Atlassian doen we niet meer". Een nummer 3 zonder één voorbeeld en tegen een besluit van de eigenaar in hoort niet in een top 5. |
| **Mac-app direct** | Nummer 4 | Niet beoordeeld | **Open.** H keek alleen naar winkels. G's Mac-voorbeelden zijn grotendeels zelf gemeld (MacMD, Xnapper) of een lanceermaand (Woday). Geen basiscijfer. |
| **Chrome** | Nummer 3 | Nummer 2 | **Eens over de plek, allebei te rooskleurig over de kans.** H's "±1 op 5" botst met zijn eigen bronnen: mediaan 15 gebruikers na 7 tot 15 weken, 2% haalt 1.000 gebruikers. Beide leunen op FriendFilter (verouderd, dalend) en H op de beste maand van Save Bulk Gmail. |
| **WordPress** | Samen met Shopify op 5 | Nummer 4 | **Eens.** G is eerlijker: drie van de vier geverifieerde WordPress-producten zitten op $430 tot $1.220 per maand. H steunt op het Freemius-gemiddelde van $43.000, dat de mediaan ver overschat. |
| **Figma** | Zwak, op omzetcijfers | Dicht voor verkopers | **G.** Zie steekproef 12: plugins kunnen wel betaald, ze verdienen alleen weinig. |
| **Steam** | Mediaan $1.100 tot $3.500 voor altijd | 65,9% onder $1.000 totaal | Geen echte tegenspraak; twee schattingen die op hetzelfde wijzen. |

---

## 3. Vertekening: zijn de conclusies te rooskleurig?

**Ja, op vijf punten.**
1. **TrustMRR is ook een verkoopmarkt.** Boothie (vraagprijs $900.000) en House Goals ($600.000) staan te koop; FriendFilter's omschrijving is een verkooptekst. Wie verkoopt, laat zijn beste stand zien. De omzet zelf is wel echt (uit de betaaldienst).
2. **TrustMRR is van Marc Lou.** G gebruikt drie van zijn producten (DataFast, CodeFast, ShipFast) als voorbeeld voor "eigen SaaS". DataFast draait onder TrustMRR zelf en Marc heeft 425.000 volgers. Dat is geen voorbeeld dat Dortus kan nadoen.
3. **Pieken als normaal.** House Goals daalt hard, Save Bulk Gmail wordt genoemd met zijn beste maand, FriendFilter met een stand van twee maanden oud. Alle drie in de richting van "beter dan het is".
4. **Gemiddelden in plaats van medianen.** Freemius $43.000 en Atlassian $220.000 per app zijn gemiddelden over een scheve verdeling. RevenueCat's 17% telt één goede maand, niet een blijvend inkomen.
5. **De "kans"-kolom van H is een GOK die hoger uitvalt dan zijn eigen bronnen.** Shopify 1 op 4 terwijl 64% van de apps niets verdient; Chrome 1 op 5 terwijl 2% van de nieuwe extensies 1.000 gebruikers haalt.

**Eerlijke middenwaarde per top-kanaal** (wat een gewone poging oplevert, niet de winnaar; allemaal mijn GOK op de getallen hierboven):

| Kanaal | Mediaan (gewone poging) | Kans op blijvend ≥ $1.000 per maand binnen 12 maanden | Waar het op rust |
|---|---|---|---|
| Mobiele abonnementsapp | een paar honderd dollar totaal | ±1 op 10 (17% tikt het ooit aan binnen 2 jaar, blijvend minder) | RevenueCat 17,3% in 2 jaar; TrustMRR-mediaan RevenueCat $391 totaal |
| Shopify-app | $0 | ±1 op 15 tot 1 op 30 zonder nieuwe golf | RevenueHunt 36% verdient iets; Vera: 2 tot 6 van 100 nieuwe apps halen 100 installs in 2 tot 6 maanden |
| Chrome-extensie (zakelijk gat, eigen betaling) | $0 | ±1 op 20 tot 1 op 50; een "goede" zaak doet $500 tot $1.000 na een jaar | mediaan 15 gebruikers; Save Bulk Gmail $711 MRR na 18 maanden |
| WordPress (gratis plus Pro) | onder verkopers een paar honderd dollar per maand | ±1 op 10 | G's geverifieerde plugins $430 tot $1.220; CodeCanyon 92,5% nooit 1.000 licenties |
| Atlassian Forge | onbekend | onbekend; Dortus' eigen poging leverde te weinig installs | geen enkel openbaar voorbeeld |

---

## 4. Past het bij Dortus?

**Meetlat:** Thijs zo min mogelijk werk (accounts, ID, betalen, support), geen tijd voor geld, en volgens `koers-kingmaker.md` vroeg op een platform of golf en daar nummer één worden. Thijs zei op 7 nov letterlijk dat hij "niet nog een visje in een oceaan" wil zijn, met Shopify en Atlassian als voorbeeld.

| Kanaal | Wat Thijs moet doen | Past bij "vroeg en groot"? | Oordeel |
|---|---|---|---|
| **Chrome-extensie** | Eenmalig $5 en een Google-account; betalen via **Polar, dat er al staat** (merchant of record, btw geregeld, betaalt uit naar NL). Geen server nodig. Support per mail, kan een agent. Handelaarsverklaring EU (GOK: adres kan zichtbaar worden). | Ja, als het product vroeg is op iets nieuws in Chrome of in een grote dienst (nieuwe AI-functie, nieuwe app zonder bulkknop). | **Past, nummer 1.** Minste werk voor Thijs van alle kanalen. Wel: eerlijke kans per poging is klein, dus alleen met een scherp zakelijk gat en de 4-weken-stopregel die al in het besluit van 17 nov staat. |
| **WordPress-plugin op de AI-golf** (gratis in de map, Pro via Polar of Freemius) | Een wordpress.org-account (geen ID-keuring, GOK) en eventueel een Freemius-account. Betalen kan via Polar. Support op het forum van de plugin: kost tijd, maar een agent kan antwoorden schrijven. | Deels: WordPress is oud, maar AI-koppelingen voor WordPress zijn een nieuwe golf in een grote bestaande winkel (de hoek van Lars). Bewijs: Respira, 1 persoon, Polar, van $0 in maart naar $12.000 in september 2026 (GEZIEN). | **Past, nummer 2.** Kost Thijs bijna niets, betaalcultuur bestaat (Pro per jaar is normaal), en de golf is jong. Keuring van de map kan weken duren (GOK, nameten). |
| Shopify-app | Partner-account, belastingformulier en uitbetaling (eenmalig), app-keuring. Daarna: winkeliers verwachten snelle hulp en een eigen server met klantdata (AVG-verzoeken). | Nee, tenzij een nieuwe Shopify-regel of API zonder sterke app (de regel van Vera blijft goed). | **Valt af als hoofdkanaal.** Te druk, eigen meting zwak, en Thijs wees het al af. Alleen op een golf. |
| Mobiele app | Apple Developer $99 per jaar met ID; als EU-handelaar worden adres, telefoon en mail openbaar op elke app-pagina (botst met de privacyregel; postbus en zakelijk nummer nodig). Google Play: persoonlijk account eist 12 testers 14 dagen achter elkaar (Thijs moet die mensen vinden), of een organisatie-account met KvK en D-U-N-S. De winnaars draaien op dagelijkse TikTok of betaalde advertenties, en de koers zegt juist dat filmpjes zonder volgers verspilling zijn. AI-fotoapps kosten per gebruik (Boothie 55% marge). | Nee: de grootste oceaan die er is. Uitzondering: een nieuw apparaat of oppervlak (Android XR, HomeView, Googlebook) waar hetzelfde account toegang toe geeft. | **Valt af nu.** Het meeste werk voor Thijs (ID, openbaar adres, testers, advertentiegeld) en geen verspreidingsmotor. Wel bewaren voor een pionierskans op een nieuw apparaat. |
| Atlassian Forge | Account bestaat waarschijnlijk nog. | Nee, volwassen markt. | **Valt af:** besluit Thijs 6 nov, `doelen.md`. |
| Mac-app direct | Apple Developer $99 voor notariseren (Thijs). Betalen via Polar. | Nee, geen nieuwe winkel. | Middenmoot; niet nu. |

**De twee die het best passen: Chrome-extensie en een WordPress-plugin op de AI-golf**, allebei met Polar als kassa. Ze vragen Thijs hooguit een account van een paar minuten, er is geen ID-keuring met openbaar adres, geen testers, geen advertentiegeld, en de support is mail of forum die een agent kan doen. Voorwaarde voor allebei: kies een zakelijke koper (wie eraan verdient, betaalt; dat patroon van H staat stevig) en wees vroeg op iets dat net nieuw is.

---

## 5. Eindoordeel: wat staat stevig, wat niet

**Staat stevig**
- Afdrachten en regels: Shopify 0% tot $1 mln, Atlassian 0% op Forge tot $1 mln, platformen zakken met hun afdracht. Afdracht beslist het niet meer.
- Alle winkels zijn scheef; de mediaan is overal laag ($0 bij Shopify en Chrome, een paar honderd dollar bij apps).
- Zakelijke kopers betalen vaker en meer dan consumenten (H, patroon 1).
- AI-fotoapps van één maker kunnen in maanden $10.000 tot $60.000 per maand halen (Stencil AI en Boothie geverifieerd, Stencil zonder publiek).
- Smalle doelgroep, één belofte, en één verspreidingsmotor (G, patronen 1 en 4).
- Figma, Notion, itch.io, Etsy en Superhive zijn zwak voor een team zonder publiek.

**Staat niet stevig**
- H's kanskolom (Shopify 1 op 4, Chrome 1 op 5, Atlassian 1 op 5): GOK's die hoger zijn dan de eigen bronnen en dan Dortus' eigen metingen.
- Atlassian op plek 3: geen enkel voorbeeld, en tegen een besluit van Thijs.
- "Figma is dicht": geldt voor bestanden, niet voor plugins.
- FriendFilter, House Goals en Save Bulk Gmail als bewijs: verouderd, dalend of een piekmaand.
- G's advies "zet het volgende product in een mobiele app": het getal klopt, maar de route vraagt van Thijs het meest (ID, openbaar adres, testers) en een TikTok- of advertentiemotor die Dortus niet heeft.
- RevenueCat's 17% als "haalt $1.000 per maand": het is "tikt het ooit aan binnen 2 jaar".

**Advies aan de hoofdchat:** neem uit G en H de patronen over (zakelijke koper, smalle belofte, één motor, Polar als kassa), niet de ranglijsten. Voor een volgend product: Chrome of een WordPress-plugin op een nieuwe golf, met de bestaande stopregel van 4 weken.
