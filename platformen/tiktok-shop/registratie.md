# TikTok Shop: registratie als app-ontwikkelaar (klaargezet door Tess, 9 nov 2026)

Doel: als de KvK er is, kan Thijs zich in één keer van ±30 minuten registreren, zonder zoeken. Alles hieronder komt uit de partner-docs van TikTok, gelezen met curl via de open docs-API op 9 nov 2026 (GEZIEN, ruwe tekst in `onderzoek/2026-11-09-registratie.md`).

## Kort antwoord: kan het zonder KvK?
- **Volledig registreren (certificering): nee.** Elk partnerformulier vraagt een bedrijfsnaam zoals op het bedrijfsdocument, inschrijfdatum, inschrijfnummer, een foto van het bedrijfsdocument en een ID van de eigenaar. Een route voor particulieren of losse ontwikkelaars staat nergens in de docs (gezocht op sole proprietor, individual developer, freelancer, without a company: niets). Zonder certificering kan een openbare app niet gepubliceerd worden.
- **Een eenmanszaak is genoeg (GOK, maar sterk):** de docs vragen "company document" en "company registration number"; een KvK-uittreksel van een eenmanszaak heeft beide. Welke documentsoorten per land precies mogen, staat in een gids op Feishu die inloggen vraagt (niet te lezen). Kleine Nederlandse BV's staan erin (Stockhub, Stockpilot, GEZIEN door Noor); een eenmanszaak niet zelf gezien.
- **Wel vóór de KvK mogelijk (GEZIEN, docs "Developer onboarding"):** een Partner Center-account aanmaken, ISV kiezen, het formulier op "Save for later" zetten en toch al een app aanmaken ("If you create an app now, you can't publish it until certification is complete"). Daarmee krijgt hij een app key en kan hij een **Core Function**-testwinkel maken (geen echte bedrijfsgegevens nodig, Nederland lokaal ondersteund). Niet helemaal zeker: de pagina "Create a TikTok Shop App" zegt ook dat een test-app "still have to pass all the TikTok Shop requirements to enable it". Of een app zonder certificering echt API-aanroepen mag doen, zien we pas in Partner Center.
- **Maar:** de Core-testwinkel heeft **geen financiële overzichten en afrekeningen**. Die zitten alleen in de **Full Function**-testwinkel, en die vraagt "business and KYC information" die gekeurd kan worden. Voor de boekhoudkoppeling (die juist op de Finance-API draait) helpt een vroeg account dus maar half: we kunnen inloggen, tokens en bestellingen testen, niet de uitbetalingen. Bovendien verlopen testwinkels na 180 dagen (ze zijn wel opnieuw aan te zetten). **Conclusie: niet nu vragen.** Pas als Hans ja zegt op de boekhoudkoppeling en de bouw begint, is een vroeg account de ±10 minuten van Thijs waard.

## Stappen voor Thijs, als het zover is

### Vooraf klaarleggen (±10 min)
1. **E-mailadres** dat NIET aan een TikTok Shop-verkopersaccount hangt (anders ziet TikTok je als verkoper en kun je alleen "seller developer" worden, geen openbare app). Voorstel: een eigen adres op dortus.com, bijvoorbeeld thijs@dortus.com, als dat nooit voor een TikTok-winkel is gebruikt.
2. **KvK-uittreksel** als foto of scan (jpg of png, onder 10 MB). Daaruit: volledige bedrijfsnaam (precies zoals op het uittreksel, max 100 tekens), datum van inschrijving, KvK-nummer.
3. **ID van de eigenaar** (paspoort of ID-kaart), foto jpg of png, onder 10 MB, één foto per vak. Alleen Thijs vult dit in.
4. **Logo** 1080 x 1080 pixels, jpg of png. Daan maakt dit (taak op zijn lijst zodra Hans ja zegt).
5. **Bedrijfsintroductie als pdf** (max 30 MB): wat Dortus doet, team, voorbeelden. Tess en Chris schrijven hem; Daan maakt hem op.
6. **Partnernaam**: de unieke naam die verkopers in de winkel zien ("Partner name is your unique account ID"). Voorstel: Dortus.
7. **Korte introductie** (max 1000 tekens), **doelgroep van verkopers** en **diensten**, in het Nederlands, de taal van de markt en Engels. Tess zet de teksten klaar zodra Hans een product koos.
8. **Twee keuzevelden**: soort bedrijfsdocument (kies KvK-uittreksel of wat het menu daarvoor biedt) en soort ID van de eigenaar (paspoort of ID-kaart).
9. **Bedrijfsadres** in het Engels: land + regio + adres + postcode, max 150 tekens. Volgens de docs is dit het adres waar je nu werkt; de eis "gelijk aan het bedrijfsdocument" staat er alleen voor Spanje en Ierland. Neem toch het adres van het uittreksel, dat voorkomt vragen (GOK).
10. **Contactpersoon en e-mail**; telefoon (met landcode) is optioneel.
11. Optioneel: website dortus.com.

Let op: TikTok kan later extra gegevens vragen over de uiteindelijke eigenaar (UBO); dat meldt Partner Center dan zelf. Ook kan er per categorie en land extra bewijs nodig zijn ("Category Qualification"); de tabel in de docs noemt Nederland en ontwikkelaars niet, dus dat zien we pas in het formulier (GOK).

### In Partner Center (±20 min, alleen Thijs: account, voorwaarden, ID)
1. Ga naar https://partner.tiktokshop.com/account/sign-up (de wereldwijde site, niet partner.us). Geen Amerikaanse VPN gebruiken, anders stuurt de site je naar de VS-versie.
2. Account maken met het e-mailadres van stap 1, wachtwoord, telefoon mag. Voorwaarden lezen en zelf accepteren.
3. Kies in de gids **For app developers (ISV)**, dan **Start Business**.
4. **Registration region:** Netherlands. **Target market:** Netherlands (een lokaal bedrijf kiest eerst alleen het eigen land). **Business category:** de categorie voor app-ontwikkelaars die het menu toont. Finance > Accounting is een app-categorie; of die hier al gekozen wordt, is niet zeker (GOK).
5. Vul de bedrijfsgegevens, contactgegevens en uploads in uit de lijst hierboven, en klik **Submit**.
6. Status zien onder **My Account > My category & market**. Registratiekeuring duurt meestal ±5 werkdagen. Afgekeurd: **Modify** en opnieuw indienen.
7. Daarna andere landen erbij via de app: **+ Add market (Seller type)** (DE, FR, IT, ES, BE, AT, PL, IE). Welke landen kunnen hangt af van registratieland en categorie; Noor zag kleine Nederlandse BV's in alle negen EU-landen. Elk land is een eigen kwalificatie: **Submit** op "Partner info" bewaart alleen een concept en dient niets in; contactgegevens worden per nieuwe categorie opnieuw gevraagd.
8. Zet in de projectchat "TikTok Partner Center staat", dan neemt Tess het over (app aanmaken, testwinkel, keuringen).

### Wat de ploeg daarna zelf doet (geen Thijs nodig, behalve waar vermeld)
- App aanmaken (eerst "custom" om te testen, later "public"), redirect- en webhook-adres op dortus.com.
- Testwinkel: Core Function eerst. Let op: een testwinkel aan het account koppelen kan niet ongedaan worden; Tess doet dit één keer en bewust. Full Function (voor de uitbetalingen) vraagt bedrijfs- en KYC-gegevens, minstens twee nieuwe TikTok-accounts voor testen en een toestel en netwerk in het juiste land: weer een stap voor Thijs, eerder ±30 min dan 10 (GOK).
- App sleutel en geheim: de App Secret komt nooit in de repo. Thijs zet hem in de Network secrets (zie `organisatie/middelen.md`), Tess vraagt dat op zijn lijst als het zover is.
- Keuringen voor een openbare app, in deze volgorde: registratie (±5 werkdagen), listing per taal en markt (7 tot 10 werkdagen per markt), ontwerp of ARD als Partner Center erom vraagt (3 tot 5), test van de app (7 tot 10), privacy en beveiliging (DSPR, ±2 weken, eerder starten mag en moet). Daarnaast per geval een compliance- en juridische keuring van 3 weken of meer, aan te vragen bij partner@tiktokshop.com meteen na de registratie ("initiate this review as soon as you've registered"). De listingkeuring geldt per markt of taal, dus voor negen landen meerdere rondes. De tijden zijn schattingen van TikTok, geen beloftes, en na opnieuw indienen begint de klok meestal opnieuw. Reken 4 tot 8 weken tot live (GOK), langer als de juridische keuring nodig is. Voor de DSPR is onder meer een werkende link naar een privacybeleid nodig dat bij het bedrijf en de dienst hoort: dat komt op dortus.com/<product>/.

## Kosten
Geen registratiekosten gevonden in de docs (GEZIEN). De KvK-inschrijving zelf kost geld, maar die staat los van TikTok en is het plan van Thijs.
