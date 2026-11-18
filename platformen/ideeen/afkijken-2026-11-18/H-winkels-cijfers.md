# H: winkels met openbare cijfers. Waar haalt een klein team het makkelijkst $1.000 per maand?

Onderzocht wo 18 nov 2026, ±17:55 tot 19:00 NL, door H (subagent van de hoofdchat). Alle pagina's gelezen met curl. Niets gecommit.

**Labels.** GEZIEN = het getal staat zo in de bron die ik zelf las (link erbij). Is die bron zelf een schatting (scraper, analist), dan staat dat erbij. GOK = mijn eigen rekensom of inschatting. Waar een collega in deze repo het al nagemeten had, verwijs ik naar dat bestand (daar staan de links; zij lazen het, ik las hun bestand).

**De vraag.** Kans dat een team van 1 tot 3 mensen, zonder investeerders en zonder eigen publiek, op dit platform binnen ±12 maanden ≥ $1.000 per maand netto haalt.

---

## 1. Uitkomst in het kort

**Top 5 (kans voor een klein team op ≥ $1.000 per maand):**
1. **Shopify App Store.** Kopers zijn winkels die er geld mee verdienen, ze betalen per maand, en Shopify neemt 0% tot je eerste $1 miljoen. $1.000 per maand is ±100 winkels van $10.
2. **Chrome Web Store, met eigen betaling.** Gratis bereik via de zoekbalk, 0% afdracht. Twee kleine makers in onze eigen metingen halen $1.218 en ±$8.000 per maand (Stripe, nagekeken).
3. **Atlassian Marketplace.** Bedrijven betalen per gebruiker, $7 miljard omzet sinds 2012, en vanaf 2026 0% afdracht tot $1 miljoen voor Forge-apps. Minder makers per niche dan bij Shopify.
4. **WordPress (gratis plugin in de map, Pro op eigen site).** Een maker bij Freemius met minstens $1.000 omzet per jaar haalt gemiddeld $43.000 per jaar.
5. **Apple App Store en Google Play.** 17% van de nieuwe abonnementsapps haalt $1.000 per maand (RevenueCat). Groot, maar veel concurrentie en je moet zelf verkeer halen.

**Onderaan:** Figma (nieuwe verkopers worden niet toegelaten), itch.io, Fab en Unity Asset Store (middenmoot krimpt), Notion-templates (alleen met een groot publiek).

**Waar Dortus nu zit:** Superhive (7), JetBrains (6), Steam (9), Gumroad (8). Geen van onze huidige winkels staat in de top 5, behalve Chrome, en dat hebben we op 17 nov geparkeerd.

---

## 2. Hoe ik rangschik

Per platform vijf vragen, elk zwaar of licht:
1. **Wie betaalt?** Een bedrijf dat er geld mee verdient (winkel, team, ontwikkelaar) betaalt vaker en meer dan een consument. Zwaar.
2. **Geeft de winkel zelf bezoekers?** Zoekbalk, aanraadlijst, categorieën. Zonder dat moet je eigen publiek hebben, en dat hebben wij niet. Zwaar.
3. **Hoe scheef is de verdeling?** Hoeveel procent komt boven de $1.000 per maand. Zwaar.
4. **Afdracht.** 0% tot 30%. Licht: het verschil tussen 15% en 30% beslist zelden of je de $1.000 haalt.
5. **Instap.** Kosten, keuring, wachttijd, wat Thijs moet doen. Middel.

De kans in de tabel is een GOK op basis van die vijf, verankerd aan de getallen in de kolommen.

---

## 3. De ranglijst

| # | Platform | Afdracht | Hoe groot | Verdeling en typische winnaar | Instap | Kans ≥ $1k/mnd (GOK) |
|---|---|---|---|---|---|---|
| 1 | **Shopify App Store** | 0% op de eerste $1 mln levenslang, daarna 15%, plus 2,9% verwerking; $19 eenmalig (GEZIEN [1]) | Shopify betaalde ontwikkelaars ruim $1,3 mld "last year"; 21.000+ apps (GEZIEN [2]); 22.546 live apps juni 2026 (GEZIEN, telling [3]) | Top 1% (225 apps) pakt ±72% van de omzet; ±36% van de apps verdient iets; 51% heeft 0 reviews; meest gevraagde instapprijs $9,99 (GEZIEN, schatting van RevenueHunt [3]) | Middel. Partner-account gratis, $19, app-keuring, veel hulpvragen van winkels | **hoog**: ±1 op 4 serieuze pogingen (GOK) |
| 2 | **Chrome Web Store** (betalen via eigen Stripe of ExtensionPay) | 0% van de winkel; betaalde extensies via de winkel bestaan sinds 2021 niet meer (GEZIEN [4]); alleen Stripe-kosten | 111.933 extensies geteld (GEZIEN, DebugBear 2024 [5]) | 85% heeft minder dan 1.000 installaties, 0,2% meer dan een miljoen (GEZIEN [5]). Een nieuwe extensie van een kleine maker: mediaan 15 gebruikers na 7 tot 15 weken, 2% haalt 1.000+ (GEZIEN, eigen meting [6]). Wie wel doorbreekt en iets zakelijks verkoopt: 2 tot 7% betaalt (GEZIEN, [7]) | Laag. $5 eenmalig (GOK, bekend bedrag), keuring van dagen | **hoog**: ±1 op 5 (GOK); het gat moet zakelijk zijn |
| 3 | **Atlassian Marketplace** (Jira, Confluence) | Forge-apps: 0% tot $1 mln levenslang vanaf 2026, daarna 16 tot 17%; oude Connect-apps 20 tot 25% (GEZIEN [8]) | $7 mld omzet sinds 2012, de laatste $1 mld in 9 maanden; 6.000+ cloud-apps; 40%+ van de klanten heeft een app (GEZIEN [9]) | Gemiddeld ±$220.000 per cloud-app per jaar, maar heel scheef (GOK: $1,33 mld per jaar gedeeld door 6.000; geen openbare verdeling gevonden) | Middel tot hoog. Forge leren, veiligheidseisen, zakelijke kopers verwachten hulp | **hoog tot middel**: ±1 op 5 (GOK) |
| 4 | **WordPress** (gratis in de map, Pro via Freemius of eigen site) | Map gratis; Freemius rekent een deel, bij één maker 7% na zijn eerste $5.000 (GEZIEN [10]) | 75.485 plugins in de map (GEZIEN, WordPress-API [11]); 3.000+ makers bij Freemius (GEZIEN [12]) | Makers bij Freemius met minstens $1.000 per jaar halen gemiddeld $43.000 per jaar, de top meer dan $700.000 (GEZIEN [12]). Op CodeCanyon verkocht 92,5% van de plugins nooit meer dan 1.000 licenties (GEZIEN, oud, 2017 [13]) | Laag. Keuring van de map duurt (GOK), daarna eerst gratis installs opbouwen | **middel tot hoog**: ±1 op 6 (GOK) |
| 5 | **Apple App Store en Google Play** | 15% onder $1 mln per jaar (Apple Small Business Program, GEZIEN [14]); Google: 99% van de betalende makers 15% of minder (GEZIEN [15]) | Apple: $1,3 bln omzet via apps in 2024 (GEZIEN, kop van Shopifreaks over Apple, niet zelf nagelezen [16]) | Van nieuwe abonnementsapps haalde 17% in 2025 $1.000 per maand en 4,6% $10.000 (2024: 19% en 5,3%) (GEZIEN, RevenueCat 2026 via 9to5Mac [17]). Let op: alleen apps die RevenueCat gebruiken, dus al betaalde apps | Middel. $99 per jaar Apple, $25 Google (GOK, bekende bedragen); keuring | **middel**: ±1 op 6 betaalde pogingen (GOK, RevenueCat is te rooskleurig voor alle apps) |
| 6 | **JetBrains Marketplace** | 15%, nooit meer dan 25% (GEZIEN [18]) | 897 betaalde en freemium plugins (GEZIEN, eigen scan 8 nov [19]) | Geen omzetcijfers openbaar. BashSupport Pro: 624.199 downloads, $39 per jaar, maker verdient ervan (GEZIEN [20]). Betaald haalt 4 tot 10% van de downloads van de gratis voorganger (GEZIEN [20]) | Laag. Gratis, keuring 1 tot 2 werkdagen (GOK) | **middel**: klein publiek, maar weinig concurrentie (GOK) |
| 7 | **Superhive** (Blender) | Maker 70% op het gratis plan, 80 of 90% met abonnement van $49 of $199, plus $0,49 per verkoop en 4 tot 5,5% kosten (GEZIEN [21]) | 7.012 makers, 74.043 producten, $53,5 mln uitbetaald sinds 2014 (GEZIEN [22]) | ±$7.600 per maker in 12 jaar (GOK, rekensom). De baas zegt: "many are working harder than ever for less income", minder omzet per klant (GEZIEN, geciteerd [23]) | Laag. Gratis, keuring 3 tot 5 dagen | **middel tot laag** (GOK) |
| 8 | **Gumroad** (kassa, plus Discover) | 10% + $0,50 bij eigen link, 30% via Discover (GEZIEN [24]) | 43.884 verkopers met zichtbare verkoop gevolgd, $206 mln geschat (GEZIEN, schatting van InsightRaider [25]) | Mediaan verkoper ±$72 per maand (GEZIEN, schatting [25]). Discover pas na $100 omzet en ±3 weken keuring (GEZIEN [26]) | Heel laag | **laag zonder eigen publiek**, hoog met (GOK) |
| 9 | **Steam** | 30%, lager boven $10 mln (GOK, bekend); $100 per spel, terug na $1.000 omzet (GEZIEN [27]) | 15.274 spellen in 2025 tot okt; $17,7 mld omzet op Steam in 2025, waarvan indie ±$4,4 mld (GEZIEN [28][29]) | 65,9% van de spellen uit 2025 haalde minder dan $1.000 in totaal, ±40% niet eens $100; de top 5% gemiddeld $300.000+ (GEZIEN, schatting Gamalytic [28]) | Middel. ID- en bankkeuring (bij ons tot 45 werkdagen), pagina en demo, maanden werk | **laag** per spel, maar grote uitschieters (GOK) |
| 10 | **Etsy** (digitale producten) | $0,20 per vermelding, 6,5% transactie, betaalkosten, Offsite Ads 12 tot 15% (GEZIEN [30][31]) | 5,6 mln actieve verkopers, $10,46 mld omzet in 2025, 89% eenmansbedrijf (GEZIEN, jaarverslag [32]) | Gemiddeld ±$1.870 per verkoper per jaar, alle soorten waren (GOK, rekensom) | Heel laag, maar eenmalige instapkosten sinds 2024 (GEZIEN [32]) | **laag** (GOK) |
| 11 | **Roblox** | Uitbetaling via DevEx, koers in 2025 met 8,5% verhoogd (GEZIEN [33]) | Makers verdienden $1 mld+ in 12 maanden tot mrt 2025; 24.500+ in het DevEx-programma (GEZIEN [34]) | Mediaan DevEx-maker $1.575 per jaar; top 1.000 gemiddeld $820.000 (GEZIEN [34]) | Laag in geld, hoog in werk (spelontwerp voor kinderen, live bijhouden) | **laag** (GOK: misschien 1 op 10 van de DevEx-makers haalt $12.000 per jaar) |
| 12 | **Notion-templates** | Notion Marketplace 8% + $0,40 per verkoop (GEZIEN [35]) | Geen platformcijfer gevonden | Winnaars hebben een groot publiek: Thomas Frank $1 mln in 2022 met een team van 8 en een YouTube-kanaal (GEZIEN [36]) | Heel laag, dus overvol | **laag zonder publiek** (GOK) |
| 13 | **Unity Asset Store en Fab** (spelonderdelen) | Unity: maker 70% (GEZIEN [37]); Fab: maker 88% (GEZIEN [38]) | Fab: makers verdienden $24 mln+ in 2025 (GEZIEN, verkoperblog die Epic citeert [39]) | Fab: middenmoot krimpt, wat $20.000 tot $60.000 per jaar deed, doet nu $15.000 tot $45.000; nieuwe verkopers starten trager (GEZIEN, verkoperblog [39]) | Laag | **laag** (GOK) |
| 14 | **Figma Community** | 15% als je mag verkopen (GEZIEN [40]) | Geen cijfer | Figma: "We are not approving new creators to sell paid files on Community at this time"; in mei 2026 bleef de prijsknop voor een nieuwe Nederlandse maker op slot (GEZIEN [40][41]) | **Dicht** voor nieuwe verkopers; alleen eigen betaling in je plugin | **heel laag** via Figma zelf (GOK) |
| 15 | **itch.io** | Zelf kiezen, standaard 10% (GEZIEN [42]) | Geen recent cijfer | Veel gratis spellen en jams; geen platformcijfer over omzet per maker (GOK) | Heel laag | **heel laag** (GOK) |

---

## 4. Per platform: wat de cijfers zeggen

### 1. Shopify App Store
- **Geld:** Shopify betaalde "more than $1.3 billion" aan ontwikkelaars, en er zijn "more than 21,000 apps" (GEZIEN [2]). Gemiddeld ±$60.000 per app per jaar (GOK). Maar: top 1% neemt ±72%, dus de andere 99% deelt ±$360 mln, ±$16.000 per app per jaar, en omdat maar ±36% iets verdient ±$45.000 per verdienende app (GOK, rekensom op de schatting van [3]).
- **Afdracht:** "You keep 100% of your first $1,000,000 USD in lifetime gross app revenue, and 85% of earnings above that" (GEZIEN [1]).
- **Waarom bovenaan:** de koper verdient geld met de app, betaalt per maand via Shopify (geen eigen kassa nodig), en 57% van de betaalde apps heeft een gratis plan (GEZIEN [3]), dus proberen is normaal. $1.000 per maand is ±100 winkels op $9,99 (GOK).
- **Waarom niet makkelijk:** de winkel groeide 10 keer sinds 2020 en kreeg 6.000+ apps in 12 maanden (GEZIEN [3]); "The scarce thing is distribution and trust: answering support, earning reviews one merchant at a time" (GEZIEN [3]).

### 2. Chrome Web Store
- **Geld:** de winkel betaalt niets uit; je verkoopt zelf. Google stopte op 21 feb 2021 met betalingen via de winkel (GEZIEN [4]).
- **Bereik:** de zoekbalk werkt voor kleine makers: Save Bulk Gmail Attachments staat met 2.000 gebruikers op nummer 1 boven extensies met 50.000 (GEZIEN [7]).
- **Verdeling:** een gewone nieuwe extensie blijft hangen op ±15 gebruikers (GEZIEN [6]). Wie wel groeit en een zakelijke koper heeft, verdient: 142 abonnees op ±2.000 gebruikers (±7%) geeft $1.218 in okt 2026 (GEZIEN [7]).
- **Oud maar nuttig:** lijst van ExtensionPay met GMass $130.000 per maand (2019), Closet Tools $42.000, GoFullPage $10.000 (2021, 4 mln gebruikers, $1 per maand), Night Eye $3.100, Weather $2.500 (GEZIEN [43]; cijfers van 2019 tot 2021).

### 3. Atlassian Marketplace
- **Geld:** "surpassed $7B in lifetime sales ... The most recent $1 billion was transacted in just nine months" (GEZIEN [9]).
- **Afdracht:** 0% tot $1 mln levenslang op Forge (sinds 1 jan 2026; Atlassian schoof de verhoging voor oude apps later op naar 1 apr 2026), daarna 16 en vanaf jul of okt 2026 17% (GEZIEN [8]).
- **Waarom hoog:** zakelijke kopers, prijs per gebruiker (een team van 50 betaalt 50 keer), en "6,000 Cloud apps" tegen "more than 40% of Atlassian customers had at least one Marketplace app" (GEZIEN [9]). Veel minder apps dan Shopify (22.546), en veel meer geld per app (GOK).
- **Waarom niet bovenaan:** geen openbare verdeling gevonden; Forge en de veiligheidseisen kosten weken; zakelijke kopers willen hulp en vertrouwen.

### 4. WordPress
- **Geld:** "A software maker on Freemius now earns an average of $43,000 annually", alleen makers met minstens $1.000 per jaar meegeteld (GEZIEN [12]). Dat is een gemiddelde van wie al verkoopt, dus scheef naar boven (GOK).
- **Hoe het werkt:** gratis plugin in de map voor installs, Pro op eigen site. SSL Zen: Pro pas bij 5.000 actieve installs, $29 per jaar, ±$5.000 per maand (EIGEN OPGAVE in Freemius-blog, mei 2020 [10]).
- **Let op:** goedkope prijzen en veel hulpvragen; de map groeit snel (75.485 plugins, GEZIEN [11]).

### 5. Apple App Store en Google Play
- **Verdeling:** "19% of all new apps crossed the $1,000/month recurring revenue threshold in 2024, that figure slipped to 17% in 2025" (GEZIEN [17]). Een jaar eerder: "about 20-25% of apps achieve monthly revenue of $1,000 within two years" en gemiddeld 60 dagen tot $1.000 (GEZIEN [44]).
- **Wat werkt:** Foto en video het vaakst boven $1.000 (21,4%); betaalmuur zet bijna 6 keer beter om dan freemium (GEZIEN [17]).
- **Kanttekening:** RevenueCat telt alleen apps met hun abonnementssoftware; de echte kans voor elke app is lager (GOK).

### 6. JetBrains Marketplace
- 15% afdracht (GEZIEN [18]). 897 betaalde en freemium plugins (GEZIEN [19]). Geen omzetcijfers openbaar. Kopers zijn ontwikkelaars met een werkgever die betaalt. Klein publiek per niche. Wij zitten er al (Bison & Flex).

### 7. Superhive
- $53.533.002 uitbetaald aan 7.012 makers sinds juni 2014 (GEZIEN [22]). Rekensom: ±$7.600 per maker over 12 jaar (GOK), dus de meeste makers verdienen weinig.
- De baas van Superhive (maart 2026): "Blender Creators are being squeezed between declining sales and an ever-increasing number of customers who expect ongoing updates" (GEZIEN, geciteerd in [23]).

### 8. Gumroad
- Mediaan verkoper ±$72 per maand (GEZIEN, schatting van InsightRaider die zijn eigen data verkoopt [25]).
- Gumroad is vooral een kassa: verkoop komt van je eigen publiek. Discover pas na $100 omzet en ±3 weken keuring, en dan 30% (GEZIEN [26]).

### 9. Steam
- "65.9% Of Steam Releases In 2025 Earned Less Than $1,000"; "the bottom 30% of games averaging just $37 in revenue, and the top 5% averaging over $300k" (GEZIEN, schatting Gamalytic via OpenCritic [28]).
- Grootste indie-hits van 2025: Schedule I $151 mln, R.E.P.O. $147 mln (GEZIEN, schatting Alinea [29]).
- $1.000 per maand is $12.000 per jaar; dat haalt ruwweg 15 tot 20% van de spellen (GOK, tussen de 66% onder $1.000 en de top 5%).

### 10. Etsy
- 5,6 mln actieve verkopers, $10,46 mld omzet in 2025; 89% "businesses of one" (GEZIEN [32]). Gemiddeld ±$1.870 per verkoper per jaar (GOK). Digitaal apart: geen cijfer gevonden.
- Offsite Ads: 15% onder $10.000 omzet per jaar, 12% erboven (GEZIEN [31]).

### 11. Roblox
- "more than 24,500 are part of our DevEx Program, with the median creator participating in the DevEx Program receiving $1,575 USD" (2024); top 1.000 gemiddeld $820.000, top 10 gemiddeld $33,9 mln (GEZIEN [34]).

### 12. Notion-templates
- Notion rekent 8% + 40 cent (GEZIEN [35]). Thomas Frank: Ultimate Brain $760.000 in 2022, "currently have a team of 8 people", verkoop via Lemon Squeezy en een kleiner YouTube-kanaal van 43.000 naar 110.000 abonnees (GEZIEN [36]). Zonder publiek geen verkoop (GOK).

### 13. Unity Asset Store en Fab
- Unity: "Unity will pay you seventy (70) percent of the sales price" (GEZIEN [37]). Fab: "industry-leading 88% revenue share" (GEZIEN [38]).
- Fab: "creators earned more than $24 million on Fab over the course of 2025"; middenmoot krimpt; nieuwe verkopers starten trager (GEZIEN, verkoperblog StraySpark [39]).

### 14. Figma Community
- Figma neemt 15% maar laat nieuwe verkopers niet toe (GEZIEN [40]). Een Nederlandse maker meldde in mei 2026 dat de prijs op slot bleef (GEZIEN [41]). Wie wil verdienen, verkoopt een licentie buiten Figma (GOK).

### 15. itch.io
- Standaard 10%, maker kiest 0 tot 100% (GEZIEN [42]). Veel gratis spellen; geen platformcijfer over omzet per maker gevonden.

---

## 5. Top 5: hoe makers het doen (2 of 3 per kanaal)

### 1. Shopify App Store
| Maker | Wat | Waar | Hoe | Cijfer |
|---|---|---|---|---|
| **Kaching Appz** (Erikas Mališauskas, begon met 1 ontwikkelaar, 2020) | Upsell- en bundelapps | Alleen Shopify App Store | Freelance winkelontwerper zag dezelfde vraag bij klanten steeds terugkomen; meerdere kleine apps in één soort | "from roughly $900,000 to $4.3 million in annual revenue, entirely through organic growth"; nu team van 40, 100.000+ winkels (GEZIEN [2]) |
| **Lightward** (Isaac Bowen, Locksmith) | Producten en pagina's afschermen | Shopify App Store, een van de eerste 100 apps | 15 jaar dezelfde app bijhouden, klein houden, zonder investeerders | "more than 162,000 installs and roughly 16,000 active subscribers and 8-figure revenue", team van 12 (GEZIEN [2]) |
| **Wat het gemiddelde zegt** | | | Gratis plan is normaal (57% van de betaalde apps), instap $9,99 | De winnaars lijken op bureauwerk dat een app werd (GOK) |

Les: begin bij een vraag die winkels al stellen, gratis plan plus $9,99, en antwoord elke winkel. Reviews zijn de munt (51% heeft er 0).

### 2. Chrome Web Store
| Maker | Wat | Waar | Hoe | Cijfer |
|---|---|---|---|---|
| **Save Bulk Gmail Attachments** (klein bedrijf, Tsjechië) | Bijlagen uit veel mails tegelijk opslaan | Chrome Web Store + eigen site met 271 artikelen | 7 bijlagen per dag gratis, $9 per maand of $39,99 per jaar; nummer 1 in de zoekbalk | $1.218 in okt 2026, 142 abonnees, ±2.000 gebruikers (GEZIEN Stripe via TrustMRR [7]) |
| **FriendFilter** (maker onder schuilnaam, VS) | Facebook-vriendenlijst opschonen voor wie er geld mee verdient | Chrome Web Store + eigen site | 5 verwijderingen per dag gratis, $29 tot $49 per maand, proef $9 voor 7 dagen | ±$8.000 tot $12.000 per maand, 337 abonnees op ±12.000 gebruikers, $1,8 mln sinds 2019 (GEZIEN Stripe via TrustMRR [7]) |
| **GoFullPage** | Hele pagina als schermafbeelding | Chrome Web Store | Jaren gratis tot 4 mln gebruikers, daarna premium voor $1 per maand | $10.000 per maand (2021, GEZIEN in lijst ExtensionPay [43]) |

Les: de koper moet er werk mee doen; de daglimiet zit op de handeling, niet op de functie.

### 3. Atlassian Marketplace
Geen kleine maker met openbare omzet gevonden in deze ronde (GOK: Atlassian-makers zijn bedrijven die weinig delen; G kan TrustMRR nakijken). Wat de cijfers wel zeggen: 3.700 openbare Forge-apps naast 6.000+ cloud-apps (GEZIEN [9]), en de hele Forge-omzet tot $1 mln is van de maker. **Dit is een gat in ons onderzoek; voor een besluit eerst 6 tot 10 kleine Forge-apps met installs en prijs meten (de Marketplace toont installaties per app).**

### 4. WordPress
| Maker | Wat | Waar | Hoe | Cijfer |
|---|---|---|---|---|
| **SSL Zen** (Sagar Patil, geen programmeur, huurde 2 mensen in) | SSL instellen | Gratis in de map, Pro via Freemius | Pro pas na 5.000 actieve installs; $29 per jaar, $199 onbeperkt; investering $2.200 | ±$5.000 per maand na ±6 maanden (EIGEN OPGAVE, Freemius-blog 2020 [10]) |
| **WP Mobile Menu** (Rui Guerreiro, solo) | Mobiel menu | Gratis in de map, Premium via Freemius | Eerst gratis zonder plan; Premium bij ±10.000 installs; uitleg wat gratis moet blijven uit de redenen van verwijderen | 40.000 actieve installs, fulltime (EIGEN OPGAVE, Freemius-blog 2018 [45]) |

Les: eerst duizenden gratis installs, dan pas Pro; prijs per jaar.

### 5. Apple App Store en Google Play
| Maker | Wat | Waar | Hoe | Cijfer |
|---|---|---|---|---|
| **Nomad Sculpt** (Stéphane Ginier, solo) | Boetseren op iPad en Android | App Store, Play, later computer | Jaren gratis webversie eerst, dan één prijs $19,99 zonder abonnement, zes jaar gratis updates | Zie `platformen/succes/verhalen.md` verhaal 21 (GEZIEN door Lars) |
| **Wat RevenueCat laat zien** | | | Betaalmuur zet ±6 keer beter om dan freemium; foto en video het vaakst boven $1.000 | 17% van nieuwe abonnementsapps haalt $1.000 per maand (GEZIEN [17]) |

---

## 6. Patronen (3 of meer platformen)

1. **Wie aan het product verdient, betaalt.** Shopify-winkels, Atlassian-teams, Facebook-verkopers bij FriendFilter, boekhouders bij Save Bulk Gmail, ontwikkelaars bij JetBrains. Bij consumentenwinkels (Etsy, Gumroad, Roblox, Steam) is de mediaan laag: $72 per maand, $1.575 per jaar, minder dan $1.000 in totaal.
2. **Elke winkel is scheef, de vraag is hoe scheef.** Shopify top 1% ±72%; Chrome 85% onder 1.000 installs; Steam 66% onder $1.000; Superhive ±$7.600 per maker in 12 jaar. Winkels met minder makers per koper (Atlassian, JetBrains) zijn minder scheef (GOK, geen verdeling openbaar).
3. **De platformen zakken met hun afdracht voor kleine makers.** Shopify 0% tot $1 mln, Atlassian 0% tot $1 mln op Forge, Apple en Google 15%. De afdracht is niet meer het verschil; bezoekers en betaalbereidheid wel.
4. **Eerst gratis bereik, dan betalen.** WordPress (Pro na 5.000 tot 10.000 installs), Chrome (GoFullPage na 4 mln), Shopify (57% met gratis plan).
5. **Platformen zonder eigen bezoekers belonen een publiek.** Gumroad, Notion, Etsy en Steam zonder volgers: laag. Met een kanaal (Thomas Frank, Blender Secrets 13.408 verkopen op Gumroad, `platformen/succes/verhalen-groei.md` verhaal 4) hoog.

## 7. Verrassingen

- **Figma is dicht.** Nieuwe makers mogen er niet verkopen, ook in mei 2026 niet.
- **Atlassian is groter dan ik dacht en niemand van ons keek ernaar:** $1 mld in 9 maanden, 0% tot $1 mln.
- **Superhive krimpt per klant**, volgens de eigen baas. Daar zit ons enige betaalde product nu.
- **Fab betaalt 88% maar de middenmoot krimpt**: hoger aandeel, minder verkoop.
- **RevenueCat's $1.000-kans daalt** (19% naar 17%), terwijl de top harder groeit.

## 8. Wat Dortus kan overnemen (max 5)

1. **Kies het volgende product op "wie verdient eraan", niet op "welke winkel".** Ons huidige werk (Hats, Click Joints Pro, Ebb) richt zich op consumenten en hobbyisten, de laagste rijen. Waarom: de mediaan daar is $72 per maand of minder; bij zakelijke kopers haalt een kleine maker $1.000 met 100 tot 150 betalers.
2. **Shopify App Store als eerste nieuwe winkel onderzoeken, met een meting zoals bij JetBrains.** Waarom: hoogste kans in deze lijst, 0% afdracht, Shopify regelt betalen, gratis plan plus $9,99 is normaal. Eerst meten: 10 niches met apps die 50 tot 500 reviews hebben, ouderdom en prijs. Vraag aan Thijs: een Partner-account en $19.
3. **Chrome niet laten liggen.** Het besluit van 17 nov 10:50 parkeerde Chrome, maar onze eigen metingen (verhalen 28 tot 30, 24, 32) laten zien dat het werkt als de koper zakelijk is en de daglimiet op de handeling zit. Waarom: 0% afdracht, $5 instap, zoekbalk die kleine makers bovenaan zet.
4. **Atlassian Forge meten voordat we het afschrijven.** 6 tot 10 kleine Forge-apps met installs en prijs per gebruiker. Waarom: grootste geld per app, 0% tot $1 mln, weinig concurrentie per niche; maar hier hebben we geen voorbeeld van een kleine maker.
5. **Geen nieuwe producten op Figma, Notion, itch.io, Etsy of Fab.** Waarom: dicht, overvol of alleen met eigen publiek; de cijfers zeggen dat een team zonder volgers daar onder de $100 per maand blijft.

---

## Bronnen

[1] Shopify, revenue share: https://shopify.dev/apps/store/revenue-share
[2] Shopify News, "The developers behind Shopify's $1.3 billion app ecosystem": https://www.shopify.com/news/billion-dollar-ecosystem
[3] RevenueHunt, State of the Shopify App Economy (juni 2026, omzet geschat uit prijzen en reviews): https://revenuehunt.com/state-of-the-shopify-app-economy/
[4] 9to5Google, 22 sep 2020, Chrome Web Store payments deprecation: https://9to5google.com/2020/09/22/google-chrome-paid-extensions-deprecation/
[5] DebugBear, Chrome Extension Statistics (jul 2024, bijgewerkt aug 2024): https://debugbear.com/blog/chrome-extension-statistics
[6] Eigen meting: `platformen/succes/verhalen-groei.md` verhaal 24 (725 lanceringen op r/chrome_extensions), data `platformen/succes/data/chrome-lanceringen-2026-11-16.csv`
[7] Eigen verhalen met Stripe via TrustMRR: `platformen/succes/verhalen.md` verhaal 28 (FriendFilter, https://trustmrr.com/startup/friendfilter-groupfilter.md) en 30 (Save Bulk Gmail Attachments, https://trustmrr.com/startup/save-bulk-gmail-attachments.md)
[8] Atlassian, Updates to Marketplace Revenue Share 2026: https://www.atlassian.com/blog/developer/updates-to-marketplace-revenue-share-2026 en https://www.atlassian.com/blog/developer/runs-on-atlassian-apps-can-now-take-home-100-of-marketplace-revenue
[9] Atlassian, "$7 billion and counting": https://www.atlassian.com/blog/teamwork/atlassian-marketplace-7-billion
[10] Freemius, SSL Zen (20 mei 2020): https://freemius.com/blog/success-story-ssl-zen-sagar-patil/
[11] WordPress plugin-API, gelezen 18 nov 2026: `https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[per_page]=1&request[browse]=popular` gaf `results: 75485`
[12] Freemius, Year in Review 2024: https://freemius.com/blog/year-in-review-2024/
[13] Freemius, CodeCanyon by the numbers (±2017): https://freemius.com/blog/codecanyon-wordpress-plugins-analysis/
[14] Apple, App Store Small Business Program: https://developer.apple.com/app-store/small-business-program/
[15] Google Play, service fees: https://support.google.com/googleplay/android-developer/answer/112622
[16] Shopifreaks, kop "Apple Says App Store Developers Generated $1.3 Trillion in 2024 Sales" (alleen de kop gezien in zoekresultaat): https://www.shopifreaks.com/apple-says-app-store-developers-generated-1-3-trillion-in-2024-sales-mostly-commission-free/
[17] 9to5Mac over RevenueCat State of Subscription Apps 2026 (4 mrt 2026): https://9to5mac.com/2026/03/04/new-report-looks-into-the-sustainability-of-the-subscription-app-market-for-2026/
[18] JetBrains Marketplace, revenue sharing and fees: https://plugins.jetbrains.com/docs/marketplace/revenue-sharing-and-fees.html
[19] Eigen scan: `platformen/jetbrains/data/betaalbereidheid-scan-2026-11-08.md`
[20] Eigen verhaal BashSupport Pro: `platformen/succes/verhalen.md` verhaal 5 (API https://plugins.jetbrains.com/api/plugins/13841)
[21] Superhive, How commission earnings are calculated: https://support.superhivemarket.com/article/32-how-commission-earnings-are-calculated
[22] Superhive, Market Statistics (gelezen 18 nov 2026): https://superhivemarket.com/market-stats
[23] Spencer Magnusson, "Blender Creator Economy is Breaking" (7 mrt 2026, citeert Jonathan Williamson van Superhive): https://spencer-magnusson.beehiiv.com/p/blender-creator-economy-is-breaking-whats-next
[24] Gumroad, pricing: https://gumroad.com/pricing
[25] InsightRaider op DEV, Gumroad-statistieken (scraper, schatting): https://dev.to/insightraider/almost-every-gumroad-stat-youve-read-traces-to-one-2021-blog-post-here-are-7-that-dont-3poi
[26] Eigen verhaal Gumroad: `platformen/succes/verhalen.md` verhaal 16 (Gumroad Help, Discover)
[27] Steamworks, Steam Direct fee: https://partner.steamgames.com/doc/gettingstarted/appfee
[28] OpenCritic/DualShockers, 21 okt 2025, Gamalytic-schatting: https://opencritic.com/news/22399/only-8-of-steam-games-gross-over-100-thousand-40-make-less-than-steam-listing-fees
[29] Game World Observer, 22 dec 2025, Alinea Analytics: https://gameworldobserver.com/2025/12/22/indie-projects-generated-a-quarter-of-the-total-game-revenue-on-steam-by-the-end-of-2025-analytics
[30] Etsy Help, listing fee en transactiekosten: https://help.etsy.com/hc/en-us/articles/360035902374
[31] Etsy Help, Offsite Ads: https://help.etsy.com/hc/en-us/articles/115014483627
[32] Etsy, jaarverslag 10-K 2025: https://www.sec.gov/Archives/edgar/data/1370637/000137063726000019/etsy-20251231.htm
[33] PocketGamer.biz, DevEx 8,5% hoger: https://www.pocketgamer.biz/roblox-creators-will-now-earn-85-more-from-developer-exchange
[34] Roblox, Annual Economic Impact Report (sep 2025): https://about.roblox.com/newsroom/2025/09/roblox-annual-economic-impact-report
[35] Notion Help, Selling templates on Marketplace: https://www.notion.com/help/selling-on-marketplace
[36] Thomas Frank, "$1 Million in Notion Template Sales": https://typefully.com/TomFrankly/dollar1-million-in-notion-template-sales-kuFT0iD
[37] Unity, Asset Store Provider Agreement: https://unity.com/legal/as-provider
[38] Epic, Fab documentation: https://dev.epicgames.com/documentation/fab/fab-documentation
[39] StraySpark, Fab 12-month retrospective (verkoperblog): https://www.strayspark.studio/blog/fab-marketplace-12-month-retrospective-seller-2026
[40] Figma Help, About selling Community resources: https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources
[41] Figma Forum, mei 2026: https://forum.figma.com/ask-the-community-7/can-plugins-still-use-figma-native-payments-monetization-54336
[42] itch.io, Introducing open revenue sharing: https://itch.io/updates/introducing-open-revenue-sharing
[43] ExtensionPay, 8 Chrome Extensions with Impressive Revenue (cijfers 2019 tot 2021): https://extensionpay.com/articles/browser-extensions-make-money
[44] GIGAZINE over RevenueCat 2025 (18 mrt 2025): https://gigazine.net/gsc_news/en/20250318-mobile-apps-subscriptions-revenue
[45] Freemius, WP Mobile Menu (24 okt 2018): https://freemius.com/blog/wp-mobile-menu-success-story/

**Niet gelukt:** TechRepublic, Barn2, Indie Hackers, TechSpot en het Fab-jaaroverzicht van Epic gaven een Cloudflare-muur; niet omzeild. Geen openbare omzetverdeling gevonden voor Atlassian, JetBrains, Figma, Notion en itch.io.
