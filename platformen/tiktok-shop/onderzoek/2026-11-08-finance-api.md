# Onderzoek: TikTok Shop Finance-API voor boekhoudkoppeling (8 nov 2026)

Bron TikTok-docs: de docv2-pagina's halen hun tekst uit een open JSON-API, zonder inloggen te lezen met curl:
`https://partner.tiktokshop.com/api/v1/document/detail?document_id=<pad>&workspace_id=3&aid=359713&locale=en-US` (inhoudsopgave: `/api/v1/document/tree?workspace_id=3&aid=359713&locale=en-US`). GEZIEN

## 1. Finance-API in de Partner API
- **Bestaat, met deze endpoints** (GEZIEN, https://partner.tiktokshop.com/docv2/page/finance-api-overview):
  Get Statements `GET /finance/202309/statements` (dagelijkse afrekening, één per dag per winkel), Get Transactions by Statement (`/finance/202501/statements/{statement_id}/statement_transactions`, per bestelling), Get Transactions by Order (`202501`, SKU-niveau), Get Unsettled Transactions (`202507`), Get Payments (nu versie `202605`, de "accounting" gids noemt nog 202309), Get Seller Financial Transactions (`202309`), Get Withdrawals (`202309`).
  Urls: .../docv2/page/get-statements-202309, get-transactions-by-statement-202501, get-transactions-by-order-202501, get-unsettled-transactions-202507, get-payments-202605, get-seller-financial-transactions-202309.
- **Velden per bestelling** (GEZIEN, get-transactions-by-order-202501): o.a. `platform_commission_amount` ("commission charged by TikTok Shop"), transactiekosten, verzendkosten, terugbetalingen, aanpassingen, `fee_tax_amount` met `fee_tax_breakdown`. `vat_amount` en `import_vat_amount` gelden "only for cross-border shop orders"; `referral_fee_amount` alleen US. Er zijn ook velden "Applicable only for EU and UK" (bijv. FBT-verzendkosten). GEZIEN
- **Btw op de verkoop zelf voor een lokale NL-verkoper**: geen apart btw-veld per verkoop voor lokale EU-winkels gevonden. GOK: de koppeling moet de btw op omzet zelf uitrekenen uit het tarief van het product.
- **Regio**: geen EU-uitsluiting gezien. Get Statements heeft velden "applicable for all regions except UK and US"; Get Payments is "currently unavailable to SEA markets". GEZIEN. Data pas vanaf 2023-07-01. GEZIEN
- **Nederland** staat NIET in de tabel met regio's/talen (wel DE, FR, IE, IT, ES, GB) (GEZIEN, https://partner.tiktokshop.com/docv2/page/regions-and-languages). Dat gaat over taalcodes, niet over toegang. Seller University noemt "Niederlande lokal" wel als markt (zie 2). GOK: NL-winkels vallen onder de EU-omgeving en werken met dezelfde API.
- **Scope**: "Finance Information" (id 430596). In de pagina Access scope staat die als **Public** (geen aparte aanvraag) (GEZIEN, https://partner.tiktokshop.com/docv2/page/access-scope). De gids voor boekhoudapps zegt wel: Partner Center is leidend of een scope "requires approval, or is restricted for a specific app category or market" (GEZIEN, https://partner.tiktokshop.com/docv2/page/accounting-and-finance). De verkoper moet de app toestemming geven.
- **App-categorie**: er bestaat een categorie Finance > **Accounting** ("accounting, tax, and reconciliation systems that sync transaction, payment, and settlement data into finance workflows"), met Finance Information in de scope-lijst (GEZIEN, https://partner.tiktokshop.com/docv2/page/hulvi36o). De gids https://partner.tiktokshop.com/docv2/page/accounting-and-finance beschrijft precies deze use case met verplichte use cases (FIN-GET-PAYMENT, FIN-GET-STATEMENT, FIN-TXGET-STATEMENT, FIN-TXGET-ORDER, plus winkel koppelen/ontkoppelen). GEZIEN
- Ook: endpoint "Upload Invoice" (202502) en webhook "(36) Invoice status change" bestaan; niet geopend, onbekend of dat EU-koperfacturen zijn. GEZIEN (alleen titel)

## 2. Wat Seller Center zelf gratis geeft (EU)
- **TikTok maakt zelf facturen voor zijn kosten**: "Steuerrechnungen für Plattformprovisionen": onder Finanzen > Rechnungen PDF-facturen downloaden plus een Excel met details per bestelling en de kosten per bestelling; alleen "Plattformservicegebühr" en "Logistikgebühr" staan erop; batch-export van de laatste 3 maanden. Geldt voor o.a. "Niederlande lokal", DE, FR, BE. GEZIEN, https://seller-de.tiktok.com/university/essay?knowledge_id=3536081577510676&role=1&course_type=1 (bijgewerkt 13-07-2026)
- **Btw verlegd**: in dat artikel staat niets over verlegging. Niet gevonden. GOK: TikTok factureert vanuit een EU-entiteit (Ierland) met btw verlegd naar NL-ondernemers, niet bevestigd.
- **Affiliate-provisie**: TikTok maakt maandelijks btw-facturen namens creators (alleen DE, FR, ES, IE), anders "Provisionsbelege". GEZIEN, https://seller-de.tiktok.com/university/essay?knowledge_id=1813624566040337&role=1&course_type=1
- **Uitbetalingen exporteren**: artikel "Zahlungen von TikTok Shop" (ook Niederlande lokal): uitbetalingen over een periode exporteren "als Excel-Datei für weitere Analysen und den Abgleich". GEZIEN (zoekresultaat en kop, seller-de University, zoekterm "Abrechnung exportieren")
- Koperfacturen: de verkoper stuurt ze zelf (uploaden als PDF/afbeelding via chat). GEZIEN (zoekfragment "Rechnungsstellung an Käufer")
- **Eigen boekhoudkoppeling van TikTok**: niet gevonden. Er is een menu "Integrationslösungen" en een "USt-Berechnungsservice" met Fonoa, niet geopend. Niet gezien welke koppelingen daar staan.

## 3. Bonus: API's van boekhoudpakketten
- **Moneybird**: open REST-API met o.a. Sales invoices, External sales invoices, Financial mutations, Ledger accounts. OAuth2 of persoonlijke API-token; een externe app moet zich registreren bij Moneybird (client id/secret). GEZIEN, https://developer.moneybird.com/api/sales_invoices/ en https://developer.moneybird.com/authentication/
- **Exact Online**: REST-API met `salesentry/SalesEntries` (GET, POST, PUT, DELETE), `generaljournalentry/GeneralJournalEntries` (POST) en `salesinvoice/SalesInvoices`. GEZIEN, https://start.exactonline.nl/docs/HlpRestAPIResources.aspx. App registreren in het Exact App Center (OAuth) en voor openbare vermelding partnerschap: DERDEN/GOK, niet zelf gelezen.
- **e-Boekhouden**: heeft een API-pagina (https://www.e-boekhouden.nl/koppelingen/api) en een API-referentie op https://api.e-boekhouden.nl/swagger/index.html. GEZIEN (bestaat). Welke endpoints (mutaties boeken) en of aanmelding nodig is: niet gelezen.

## Conclusie in het kort
Technisch kan het: Finance-API is er, scope staat als Public, er is een aparte app-categorie Accounting voor precies dit. Open punten: btw op omzet voor lokale EU-winkels zit niet als veld in de API, NL ontbreekt in de regiotabel, en of de scope in Partner Center voor EU echt zonder goedkeuring komt is pas te zien na aanmaken van een app.

## Nagekeken (Tess, 8 nov 23:30 UTC)
Zelf met curl tegen de JSON-API van de docs gecontroleerd: de gids `accounting-and-finance` noemt FIN-GET-PAYMENT, FIN-GET-STATEMENT, FIN-GET-WITHDRAWALS, FIN-TXGET-STATEMENT en FIN-TXGET-ORDER en spreekt over goedkeuring per categorie of markt; `access-scope` zet "Finance Information" (afrekening per bestelling) op Public. Klopt.
