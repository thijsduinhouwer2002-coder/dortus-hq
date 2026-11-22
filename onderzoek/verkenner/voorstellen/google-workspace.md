# Voorstel: Google Workspace Marketplace (add-ons voor Sheets, Docs, Gmail, Forms, Slides)

**Advies: nee voor nu. Cijfer: 5 van 10.** Het bereik is goed (vergelijkbaar met JetBrains), maar geld van nieuwe kleine makers is niet aangetoond: alle makers die sinds 2025 begonnen en hun omzet delen zitten onder $150 per maand. Echt geld zit bij makers die in 2021 of eerder begonnen. Geschreven op 7 nov 2026, run 12:31.

## Wat ik zelf mat
- Met `data/gwm-zoek-script.py` ±400 zoekwoorden in de Marketplace gezocht (100 kaarten per zoekwoord): **5.865 verschillende add-ons**. Dat is ongeveer de hele winkel (derden tellen ±5.400). GEZIEN
- Met `data/gwm-haal-script.py` van alle 5.865 de vermelding gelezen: gebruikers, aantal reviews, "Listing updated", prijsvorm en de reviewdatums op de pagina. Uitkomst in `data/gwm-detail-2026-11-07.jsonl`, tellen met `data/gwm-tel-script.py`. GEZIEN
- **Meetgrens:** Google toont geen eerste publicatiedatum, alleen "Listing updated". De Wayback Machine was hier niet bereikbaar. Daarom een benadering van "nieuw": bijgewerkt in de periode, en geen reviews of een eerste review vanaf de maand ervoor. Daar zitten ook oude apps in die nooit een review kregen (drukt de mediaan) en apps van grote bedrijven (trekt hem op). Ook vallen actieve nieuwe add-ons die na de periode nog bijwerkten weg (drukt de mediaan): SheetLane zelf is op 21 okt 2026 bijgewerkt en zit er dus niet in. 657 add-ons hebben geen "Listing updated" en vallen buiten alle groepen. Leeftijd dus GOK, de aantallen zelf GEZIEN.
- De controleur bekeek 10 add-ons uit de groep mei tot aug: 5 lijken nieuw, 4 twijfel, 1 waarschijnlijk oud (een maker die 10 oude add-ons tegelijk bijwerkte). Minstens 23 van de 305 hebben 10K+ gebruikers en zijn vaak duidelijk oud (BetterCloud, Quizlet). Ruwe schatting: ongeveer de helft van de groep is echt nieuw.
- "Gebruikers" is het getal van Google ("Number of users"), waarschijnlijk alle installs ooit, niet actieve gebruikers (GOK).

## Cijfers

**Bereik**
- Hele winkel (n=5.778 met getal): mediaan 4.000 gebruikers, 80% heeft 100+. GEZIEN (scheef door oude apps).
- Waarschijnlijk nieuwe add-ons, bijgewerkt mei tot aug 2026 (laatste update 2 tot 6 maanden geleden, leeftijd onbekend, GOK): n=305, waarvan 273 zonder reviews, **mediaan 48, 39% haalt 100+**, 20% 1.000+. GEZIEN, leeftijd GOK.
- Waarschijnlijk nieuw, bijgewerkt maart tot juni 2026 (laatste update 4 tot 8 maanden geleden, leeftijd GOK): n=231, waarvan 202 zonder reviews, **mediaan 97, 50% haalt 100+**. GEZIEN, leeftijd GOK.
- Strengere groep, alleen apps waarvan alle reviews zichtbaar zijn en de eerste review in mei tot aug 2026 viel: n=52, mediaan 90, 48% 100+. GEZIEN, wel scheef naar apps met reviews.
- Met een betaalvorm (proef of betaalde functies) liggen de nieuwe lager: mediaan 35, 32% 100+ (n=154). Gratis: mediaan 80, 46% (n=151). GEZIEN
- Ter vergelijking (GEZIEN eerder, zie `onderzocht.md`): JetBrains mediaan 111 en 54%, Obsidian 213 tot 364.
- Nichevoorbeeld: SheetLane (Pennylane naar Sheets, start dec 2025) heeft 188 gebruikers en 20 reviews (GEZIEN), start dec 2025 (DERDEN, TrustMRR).

**Geld**
- Geen betaling in de winkel en geen afdracht aan Google; makers bouwen zelf een licentiecheck met Stripe of Paddle. DERDEN: [overzicht Google](https://developers.google.com/workspace/marketplace/overview), [Mailmeteor, nov 2022](https://mailmeteor.com/blog/monetize-google-workspace-addon)
- In de winkel heeft 2.438 van 5.863 add-ons een betaalvorm (proef, betaalde functies of betaald); alleen 221 heten gewoon "Paid". GEZIEN
- Makers die sinds 2025 begonnen, omzet via Stripe gecontroleerd op TrustMRR (gelezen 7 nov 2026), DERDEN:
  - [SheetLane](https://trustmrr.com/startup/sheetlane), start dec 2025: $73 per maand, 6 abonnees.
  - [LeadToSheet](https://trustmrr.com/startup/leadtosheet), start sep 2025: $67 per maand.
  - [getstyled.art](https://trustmrr.com/startup/getstyled-art), start apr 2025: $10 per maand.
  - [SheetSandbox](https://trustmrr.com/startup/sheetsandbox), start dec 2025: $23 totaal.
  - [XLSheetAI](https://trustmrr.com/startup/xlsheetai), start onbekend: $134 per maand.
- Oudere makers wel met echt geld, DERDEN: [Sync2Sheets](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets) (1 persoon, start mei 2021) $9.000 per maand in mei 2024; [BudgetSheet](https://dev.to/vlucas/how-i-built-a-google-sheets-extension-making-16k-mrr-1amn) $1.600 per maand in 2022.
- Waarschuwing: [SheetAI](https://trustmrr.com/startup/sheetai-app) (start nov 2022, $52.305 omzet ooit) heeft ±198.000 gebruikers maar nu $388 per maand. Veel installs is hier geen omzet. AI-hulpjes in Sheets lijken verzadigd, ook nu Gemini in Sheets zit (GOK).
- Rekensom: een nieuwe betaalde add-on met 1.000 gebruikers en 1 tot 3% betalers van $5 tot $10 is $50 tot $300 per maand. GOK, past bij de TrustMRR-cijfers.

**Drukte**
- ±5.400 tot 5.900 add-ons. Per maand bijgewerkt in 2026: 120 tot 240 (okt 704, waarschijnlijk een golf updates). Echt nieuwe per maand: niet te zien. Schatting ±40 per maand: de groep van 305 over 4 maanden is ±75 per maand, waarvan ongeveer de helft echt nieuw (steekproef). GEZIEN / GOK

**Vindbaarheid**
- Zoeken in de Marketplace en het menu Extensions > Add-ons > Get add-ons in Sheets, Docs en Slides (al gefilterd op de app). Featured-plekken zijn niet te kopen. DERDEN: [support Google](https://support.google.com/marketplace/answer/6067029)
- Sync2Sheets kreeg zijn eerste installs via Reddit-video's, Facebookgroepen en later SEO op "Notion Google Sheets". DERDEN: Starter Story hierboven.

**Past het bij ons**
- Apps Script of een Workspace add-on met scopes voor alleen het open bestand (`spreadsheets.currentonly`, `drive.file`) is in 1 tot 2 weken te bouwen en vraagt geen dure beveiligingskeuring. DERDEN: [scopes](https://developers.google.com/workspace/add-ons/concepts/editor-scopes)
- Gevoelige of beperkte scopes (Gmail lezen, hele Drive) vragen verificatie en soms een CASA-keuring van $540 tot $40.000 per jaar en weken wachten. DERDEN: [Nango](https://nango.dev/docs/api-integrations/google-shared/google-security-review), [forum juni 2025](https://community.latenode.com/t/is-casa-tier-2-assessment-necessary-for-all-gmail-api-apps-options-for-indie-developers/22861)
- Thijs moet een Google Cloud-project en een Marketplace-vermelding aanmaken, en Stripe of Paddle. Review van de vermelding: "several days". DERDEN: [Google](https://developers.google.com/workspace/marketplace/about-app-review)

## Voor
- Goed bereik voor een winkel met betaling buiten de winkel: de helft van de waarschijnlijk nieuwe add-ons (laatste update 4 tot 8 maanden geleden, leeftijd GOK) heeft 100+ gebruikers.
- Geen afdracht, enorme gebruikersgroep (bedrijven en scholen).
- Een koppeling tussen een bekende tool en Sheets (zoals Sync2Sheets, SheetLane) heeft een duidelijke zoekterm en een kopende klant.

## Tegen
- Geen enkele nieuwe kleine maker sinds 2025 boven $150 per maand gevonden, laat staan boven de $300 die we elders als grens nemen (zie Blender). Aantoonbaar geld voor kleine makers is precies de eis van Thijs.
- Betalen is helemaal zelf bouwen (licentie, Stripe, server), en gebruikers zijn het niet gewend in deze winkel.
- Betaalde nieuwe add-ons halen minder bereik dan gratis.
- Gemini in Workspace neemt de makkelijke AI-hulpjes over (GOK).

## Eerste idee (als het later ja wordt)
Een koppeling van een tool die veel kleine bedrijven gebruiken (boekhouding of webshop) naar Sheets, met alleen `spreadsheets.currentonly`, freemium met Stripe. Voorbeeld: SheetLane doet dit voor Pennylane in Frankrijk; voor Nederlandse pakketten (Moneybird, e-Boekhouden) is te zoeken of het er al is.

## Wat er nog gemeten kan worden
- Een betere leeftijd: Wayback Machine (hier niet bereikbaar) of over 4 weken `gwm-zoek-script.py` opnieuw draaien en zien welke add-ons nieuw zijn. Dat geeft een echte lijst nieuwe add-ons met datum, en dan na 3 maanden hun gebruikers.
- Twee makers vinden die sinds 2024 begonnen en boven $300 per maand zitten. Lukt dat, dan wordt het een 6.

## Nakijken
Controleur akkoord (7 nov run 12:31), 10 correcties verwerkt: vertekening door latere updates, 657 zonder datum, groep vooral zonder reviews en steekproef half nieuw, leeftijd is tijd sinds update, label bij vergelijking, bron startdatum SheetLane, SheetAI oud, schatting nieuw per maand onderbouwd, label in Voor, één geldgrens ($300). Telscript: verkeerd betaalfilter weggehaald.
