# Voorstel: Zoho Marketplace (extensies voor Zoho CRM, Books, Desk en andere Zoho-apps)

Vera, verkenner, 7 nov 2026 run 19:33. Advies: **nee. Cijfer 2.**

## Wat is het
Zoho is een groot pakket bedrijfssoftware (CRM, Books, Desk, Recruit, Mail en meer). Zoho zegt 45 miljoen+ gebruikers (DERDEN: [zoho.com/marketplace/monetize-your-coding-skills.html](https://www.zoho.com/marketplace/monetize-your-coding-skills.html)). In de Marketplace staan ±2.900 extensies (DERDEN: Zoho zelf in de maandlijst van juni 2026; in 2023 noemde Zoho nog 2.000+). Een extensie wordt in 2 tot 3 weken nagekeken door Zoho (DERDEN: [FAQ](https://www.zoho.com/marketplace/faq.html)).

## Zo gemeten (GEZIEN)
- Er is geen sitemap met apps en de lijst in de winkel laadt via een script. Daar ben ik niet in gaan zoeken.
- Wel publiceert Zoho elke maand een openbare lijst "What's new on Zoho Marketplace in <maand>" op help.zoho.com, met links naar alle nieuwe extensies. Ik las jan 2025 t/m okt 2026. Okt, nov en dec 2025 miste ik eerst (okt staat onder een ander adres, nov en dec mislukten bij het ophalen); de controleur haalde ze op (64 extra apps, 61 leesbaar, lijst in `data/zoho-nieuw-okt-dec-2025-controleur.txt`). Aug 2025 laadt alleen via een script en is niet geteld. Overzicht: [new-on-marketplace](https://help.zoho.com/portal/en/kb/zoho-marketplace/new-on-marketplace).
- Uit die lijsten: 354 nieuwe extensies. Elke app-pagina gelezen met curl: 340 leesbaar. Per app: installemmer, publicatiedatum, maker, en of de app betaald of gratis is (de pagina zet `Pricing = 'Paid'` of `'Free'`).
- Data: `data/zoho-nieuw-2025-2026.json` en `data/zoho-nieuw-maand.json`. Scripts: `data/zoho-maandlijsten-script.sh` en `data/zoho-nieuw-haal-script.py`. Eerdere steekproef van 104 uitgelichte apps: `data/zoho-uitgelicht-2026-11-07.json`.
- 66 van de 340 zijn van Zoho zelf. Die tel ik niet mee bij kleine makers. Blijven 274 extensies van 190 makers (naam opgeschoond door de controleur). Met de 37 extra van de controleur: 311.
- Niet geteld: 13 apps voor Bigin (aparte winkel op marketplace.bigin.com) en 1 link zonder productpad. Verandert niets.

## Bereik
De pagina toont een installemmer pas vanaf **100+**. De html heeft een veld `"installCount":"100+ Installs"` dat bij pagina's zonder teller helemaal ontbreekt. In alle ±530 bekeken pagina's (uitgelicht, nieuw en die van de controleur) is de kleinste emmer 100+, en ook online is geen "50+ Installs" te vinden; een pagina zonder teller heeft dus vrijwel zeker minder dan 100 installs (GOK, sterk: nergens een kleinere emmer gezien, Zoho noemt de drempel niet).

Nieuwe extensies van andere makers dan Zoho, aandeel met 100+ installs (GEZIEN):

| Lichting | Betaald | 100+ | Gratis | 100+ |
|---|---|---|---|---|
| jan t/m jun 2025 (16 tot 22 mnd oud) | 49 | 1 (2%) | 49 | 6 (12%) |
| jul t/m dec 2025 (met okt t/m dec van de controleur) | ±42 | 1 (2%) | ±30 | 2 (7%) |
| jan t/m apr 2026 (6 tot 10 mnd) | 20 | 0 | 31 | 3 (10%) |
| mei t/m aug 2026 (2 tot 6 mnd) | 30 | 1 (3%) | 38 | 0 |
| sep t/m okt 2026 | 10 | 0 | 12 | 0 |

- **Mediaan: onder de 100**, voor elke lichting. Van alle ±141 betaalde nieuwe extensies van andere makers halen er **3** de 100 (Einvoice Malaysia 200+, Future Tickets 100+, ClickSend SMS 100+).
- Beste nieuwe app van een andere maker: WebAmigo Lead Enrichment (jan 2025, gratis) 2.400+. Daarna 400+ (Callyzer, TimelinesAI WhatsApp).
- Zoho zelf (pagina uit 2023): 30.000 installs per maand voor de hele winkel met 2.000+ extensies, dus ±15 per extensie per maand (DERDEN: [1-million-installs](https://www.zoho.com/marketplace/1-million-installs.html)). In 2022 telde een buitenstaander dat 97% van alle installs naar apps van Zoho zelf ging (DERDEN: [Pro SaaS, jul 2022](https://prosaas.substack.com/p/zoho-marketplace-review)). Bij de uitgelichte apps zijn de grootste ook van Zoho (128K+, 85K+, 51K+, GEZIEN).

## Geld
- Betaald verkopen kan. Twee wegen (DERDEN: [vendor-agreement](https://www.zoho.com/marketplace/vendor-agreement.html), artikel 2.3): de maker rekent zelf af, of via het bestel- en licentiesysteem van Zoho, maar dan moet je **apart een overeenkomst sluiten met Zoho over "listing fees"**. Het percentage staat nergens openbaar.
- 62 van de 92 betaalde nieuwe extensies uit 2025 t/m mei 2026 tonen een knop "Start free trial" (GEZIEN).
- Geen enkele kleine maker met een bedrag gevonden. Het enige openbare getal: Bercha Consulting, één oprichter, bouwt CRM-apps voor Zoho, HubSpot, Pipedrive en Creatio samen: $15 MRR, 6 abonnementen, $174 in totaal (DERDEN: [TrustMRR](https://trustmrr.com/startup/bercha-consulting), stand 19 nov 2025, daarna niet meer bijgewerkt).
- Bij 3 betaalde nieuwe apps met 100+ installs in 22 maanden is er geen route naar $300 per maand te zien (GOK).

## Drukte (GEZIEN)
±20 nieuwe extensies per maand (7 tot 31), ongeveer gelijk in 2025 en 2026. Rustig, dat is het enige echte pluspunt. Veel makers zijn Zoho-partners en bureaus (OCTFIS, Yaali, Nexivo), en bekende bedrijven die hun eigen koppeling neerzetten (IndiaMART, Sinch, ElevenLabs via TECHMA).

## Vindbaarheid
- De winkel zit in de Zoho-apps zelf, per product. Zoeken sorteert sinds 2021 op beoordeling (DERDEN: [whats-new](https://www.zoho.com/marketplace/whats-new.html)), dus nieuwe apps zonder reviews staan onderaan.
- Zoho zet nieuwe apps in een maandlijst en de nieuwste 4 op de newsroom-pagina. Dat levert gemeten weinig op.

## Past het bij ons
- Bouwen kan met Deluge (Zoho's eigen scripttaal) of de API, en vraagt een Zoho-ontwikkelaarsaccount. Een eenvoudige CRM-extensie in 1 tot 2 weken kan (GOK).
- Maar de kopers zijn bedrijven die vaak via een Zoho-partner werken. Bureaus bouwen maatwerk en zetten het daarna in de winkel. Daar concurreren we niet mee.

## Voor en tegen
- Voor: veel gebruikers, betalen kan, rustige winkel, eerlijke openbare lijsten.
- Tegen: bereik voor nieuwe apps bijna nul (mediaan onder 100, betaald 3 van ±141 boven 100), Zoho's eigen apps nemen bijna alles, afdracht niet openbaar en via een aparte overeenkomst, geen kleine maker met een bedrag.

## Eerste idee (als het ooit ja wordt)
Een kleine, betaalde CRM-hulp die ontbreekt, bijvoorbeeld een nette exportknop of een veldcontrole, met een gratis versie voor reviews. Pas zinvol als Zoho nieuwe apps beter laat zien.

## Nagekeken
Controleur akkoord met nee en cijfer 2, 6 correcties verwerkt: makertelling 217 werd 190, okt t/m dec 2025 bijgeteld (27 betaalde, geen enkele boven 100), Bigin genoemd, bron van de teller (`installCount`), Bercha preciezer, jaartallen bij Zoho-getallen. Afdracht ook door de controleur niet gevonden: de partner console heeft een tabblad Revenue maar geen percentage.

## Advies
**Nee, cijfer 2.** Reden: bereik en geld zijn allebei gemeten slecht, en de winkel werkt vooral voor Zoho zelf en voor partnerbureaus.
Wat dit zou veranderen: een openbare afdracht zonder listing fee, en twee kleine makers met $300+ per maand uit de winkel. Herhaalmeting kan met de maandlijsten (`data/zoho-maandlijsten-script.sh`).
