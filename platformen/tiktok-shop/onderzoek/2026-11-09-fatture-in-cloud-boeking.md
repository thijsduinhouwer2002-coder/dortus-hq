# Fatture in Cloud: kan een TikTok-uitbetaling er echt in?

Onderzoeker, 9 nov 2026. Pagina's gelezen met curl, OpenAPI-bestanden zelf gedownload. Labels: GEZIEN (zelf gelezen, met URL), DERDEN (andere bron, met link), GOK.

## Antwoord

**Ja, maar.** Met documenten en kasboek kan de app per uitbetaling alles vastleggen wat een Italiaanse verkoper fiscaal nodig heeft: de verkopen als corrispettivi (`receipts`), de TikTok-kosten als ontvangen document (`received_documents`), de verplichte btw-integratie op die kosten als autofattura TD17 (`issued_documents` type `self_supplier_invoice`), en de geldstroom via een eigen betaalrekening "TikTok Shop" in de prima nota (`cashbook`). Wat niet kan: een grootboekrekening kiezen, een memoriaalpost of een afrondingsregel maken. Dat is geen echte rem, want Fatture in Cloud is voor deze klanten een factuur- en registratiepakket; de echte boekhouding doet de commercialista in zijn eigen pakket. Wel een kans: geen enkele bestaande marktplaatskoppeling die ik vond boekt de marktplaatskosten of de uitbetaling, ze zetten alleen bestellingen om in facturen of corrispettivi.

**Voorstel per uitbetaling (settlement):**
1. `POST /receipts`: één corrispettivo per dag (of per uitbetaling) per btw-tarief, brutoprijzen, `payment_account` = "TikTok Shop". Terugbetalingen als negatieve regel of aparte receipt (nog testen). Bestellingen waarvoor de klant een factuur vraagt: `issued_documents` type `invoice` in plaats daarvan.
2. `POST /received_documents` type `expense`: TikTok-commissie, verzendkosten en andere kosten, leverancier TikTok (Ierse entiteit, GOK), btw 0 met natura N2.1/reverse charge, `category` "Commissioni marketplace", betaling `paid` vanaf rekening "TikTok Shop".
3. `POST /issued_documents` type `self_supplier_invoice` met TipoDocumento **TD17** (dienst uit EU), 22% btw, en via SDI versturen. Dit is de integratie die de wet vraagt.
4. `POST /cashbook`: uitbetaling als "uit" van rekening "TikTok Shop" en "in" op de bankrekening van de klant, met het settlement-ID in de omschrijving. Het saldo van "TikTok Shop" moet dan op nul uitkomen; een verschil zie je meteen.

## Bewijs

### 1. Wat de API heeft (OpenAPI van Fatture in Cloud)

Bron: https://raw.githubusercontent.com/fattureincloud/openapi-fattureincloud/master/openapi.yaml en de modelbestanden onder `/models/schemas/` en `/models/enums/` in dezelfde repo. Alles hieronder GEZIEN daar.

- Paden: `/c/{company_id}/issued_documents`, `/received_documents`, `/receipts`, `/cashbook` (GET en POST "Create Cashbook Entry"), `/info/vat_types`, `/settings/vat_types` (aanmaken), `/info/payment_accounts`, `/settings/payment_accounts` (aanmaken), `/info/received_document_categories`, `/info/revenue_centers`, `/info/cost_centers`. Geen pad voor grootboek, rekeningschema, journaalpost of memoriaal.
- **ReceivedDocumentType** enum: `expense`, `passive_credit_note`, `passive_delivery_note`, `self_invoice`. (models/enums/ReceivedDocumentType.yaml)
- **ReceivedDocument** velden: `entity`, `date`, `category` (vrije tekst), `description`, `amount_net`, `amount_vat`, `rc_center`, `invoice_number`, `currency`, `tax_deductibility`, `vat_deductibility`, `items_list`, `payments_list`, `attachment_token` (pdf van TikTok meesturen), `auto_calculate` ("total items amount and total payments amount can differ if this field is set to false"). Een veld "reverse charge" bestaat niet; dat gaat via de btw-soort (VatType met `ei_type` = natura) en het aparte autofattura-document. (models/schemas/ReceivedDocument.yaml, VatType.yaml)
- **Betaling van een ontvangen document**: `payments_list` met `amount`, `due_date`, `paid_date`, `status`, `payment_account`. (ReceivedDocumentPaymentsListItem.yaml)
- **IssuedDocumentType** enum bevat `self_own_invoice` en `self_supplier_invoice`. (models/enums/IssuedDocumentType.yaml)
- **TD17 en TD19 via de API**: in `GetIssuedDocumentPreCreateInfoResponse` staat `documents_type_info` met o.a. "TD16 - integrazione fattura reverse charge interno", "TD17 - integrazione/autofattura per acquisto servizi", "TD18 - integrazione per acquisto di beni intracomunitari", "TD19 - integrazione/autofattura per acquisto di beni ex art.17", elk met `self_supplier_invoice: true`. De keuze zit in `ei_raw` → `FatturaElettronicaBody.DatiGenerali.DatiGeneraliDocumento.TipoDocumento` (select met deze opties). GEZIEN in openapi.yaml rond regel 8150 en 8720.
- `ei_raw` is bedoeld voor velden die het gewone model niet heeft: "these advanced fields can instead be managed using the ei_raw params", alles als string. GEZIEN https://developers.fattureincloud.it/docs/guides/e-invoice-xml-customisation/
- Fatture in Cloud zelf: "gestisci facilmente tutti i tipi di autofattura, dal reverse charge interno ed esterno (TD16 e TD17) ...". GEZIEN https://www.fattureincloud.it/software-fatturazione/autofattura/
- **Receipt** (corrispettivi): `date`, `number`, `numeration`, `amount_net`, `amount_vat`, `amount_gross`, `use_gross_prices`, `type` (`till_receipt` of `sales_receipt`), `rc_center`, `payment_account`, `items_list` met per regel `amount_net`, `amount_gross`, `category`, `vat`. Er is ook `/receipts/monthly_totals`. (Receipt.yaml, ReceiptItemsListItem.yaml, ReceiptType.yaml)
- **CashbookEntry**: `date`, `description`, `kind` (`cashbook`, `issued_document`, `received_document`, `tax`, `receipt`, `ts_pay`), `type` (`in` of `out`), `entity_name`, `document` (id, type), `amount_in` + `payment_account_in`, `amount_out` + `payment_account_out`. Voorbeeld in de spec koppelt een kasboekregel aan een factuur (`kind: issued_document`, `document.id`). Dus ja: een kasboekregel naar een gekozen payment_account maken kan. (CashbookEntry.yaml, CashbookEntryKind.yaml, openapi.yaml rond regel 3410)
- **PaymentAccount**: type `standard` of `bank`; aanmaken via `POST /settings/payment_accounts`. Een rekening "TikTok Shop" als tussenrekening maken kan dus. GEZIEN (PaymentAccountType.yaml, openapi.yaml regel 4334)

### 2. Hoe bestaande koppelingen het doen

Ik vond geen koppeling die marktplaatskosten of uitbetalingen in Fatture in Cloud zet. Ze doen allemaal alleen de verkoopkant:
- **MarketRock** (Amazon, eBay, Shopify naar Fatture in Cloud): kiest per kanaal "Company, Section, and Balance Account", en "billing or issuing a receipt"; optie "Enable Receipt Registration ... whether the receipts will be of the 'receipt' or 'invoice' type". Niets over fees. GEZIEN https://marketrock.it/en/fatture-in-cloud-shopify en https://kb.marketrock.it/en/knowledge/marketrock-and-fattureincloud-integration-everything-you-need-to-know . "Balance Account" is vermoedelijk het `payment_account` (GOK).
- **Base.com (BaseLinker)**: "issue and handle invoices and, for some of the accounting integrations, also receipts ... forward them to Fatture in Cloud". Geen fees. GEZIEN https://base.com/en-GB/integrations/fattureincloud/
- **GetSync per Fatture in Cloud** (Shopify): orders naar Fatture in Cloud, review noemt "anche per corrispettivi e gestione OSS". Geen fees. GEZIEN https://apps.shopify.com/myappify-fattureincloud
- **Fatture in Cloud zelf**: koppelingen "In pochi clic emetti ricevute, fatture, fatture elettroniche e corrispettivi"; marktplaatsen via tussenpartijen. GEZIEN https://www.fattureincloud.it/software-gestione-ecommerce/
- De App Store-lijst op fattureincloud.it/integrazioni laadt met script; niet volledig doorzocht. Er kan een koppeling zijn die wel fees doet (GOK dat die er niet is).

### 3. Fiscaal: wat moet een Italiaanse verkoper vastleggen

- **Verkoop aan consumenten**: online verkoop van fysieke goederen is "commercio elettronico indiretto": vrijgesteld van telematisch versturen van corrispettivi, "fermo restando l'obbligo di annotazione nel registro dei corrispettivi nonché l'emissione della fattura se richiesta dal cliente" (interpello 198/2019). DERDEN https://www.ecnews.it/fiscale/fisco-e-patrimonio/iva/e-commerce-indiretto-esonerato-dalla-trasmissione-telematica-dei-corrispettivi/ . Dus: corrispettivi registreren (receipts) volstaat, geen kassabon en geen RT nodig. Dat dit in 2026 nog zo geldt: GOK (geen nieuwere wijziging gezien).
- **Wie btw verschuldigd is**: een in Italië gevestigde verkoper die vanuit Italiaanse voorraad aan Italiaanse klanten verkoopt valt nooit onder "fornitore presunto"; "Questo venditore fattura, applica e versa l'IVA italiana al 22 %". TikTok wordt alleen schuldenaar in de twee gevallen van art. 2-bis DPR 633/72 (invoer tot 150 euro, of verkoper buiten de EU). DERDEN https://www.eurofiscalis.com/it/chi-paga-iva-tiktok-shop/ . Verkoop naar andere EU-landen loopt via OSS (zelfde bron); dan moeten de corrispettivi per land en tarief kunnen (te testen of `receipts` buitenlandse tarieven accepteert, GOK dat het via eigen vat_types kan).
- **TikTok-commissie**: wordt gefactureerd door een TikTok-entiteit buiten Italië (Ierland), dus dienst B2B uit de EU, art. 7-ter, zonder Italiaanse btw. GOK op de entiteit (niet op een TikTok-pagina gezien). De Italiaanse koper moet dan integreren: sinds 2022 via een autofattura/integratie naar SDI met **TD17** (diensten uit het buitenland). TD19 is voor goederen en past hier niet. Code-omschrijvingen GEZIEN in de OpenAPI (zie boven); de regel zelf DERDEN-algemeen bekend, hier GOK zonder officiële bron gelezen. Voor forfettari geldt hetzelfde plus btw betalen per F24 (codice 6493). DERDEN https://flextax.it/emettere-fattura-per-commissioni-amazon/ (over Amazon, analoog).
- Als TikTok de factuur als Italiaanse e-factuur via SDI stuurt (met Italiaanse btw-registratie), komt die vanzelf bij `received_documents/pending` binnen en is geen TD17 nodig. Welke van de twee: niet gemeten.

### 4. Wat NIET kan, en of het een rem is

| Wat | Kan het? | Rem? |
|---|---|---|
| Grootboekrekening kiezen | Nee, geen endpoint. Alleen `category` (vrije tekst) en `rc_center`/kostenplaats. GEZIEN | Nee. De commercialista boekt in zijn eigen pakket op basis van export of SDI-bestanden; de categorie helpt hem (GOK). |
| Memoriaal/journaalpost | Nee. GEZIEN | Nee, alles past in documenten plus kasboek. |
| Tussenrekening | Ja, als payment_account "TikTok Shop" (type `standard`). GEZIEN | Geen rem; dit is de oplossing. |
| Overboeking tussen twee rekeningen in één regel (giroconto) | Onzeker: CashbookEntry heeft zowel `amount_in/payment_account_in` als `amount_out/payment_account_out`, maar `type` is `in` of `out`. GOK; anders twee regels. | Klein. |
| Afronding/verschilrekening | Geen aparte rekening. Wel `auto_calculate: false` op received_documents, en een kasboekregel `kind: cashbook` met omschrijving "arrotondamento". GEZIEN (velden), oplossing GOK | Klein. |
| Kortingen die TikTok betaalt (subsidie) | Geen apart veld; als extra regel of hogere bruto in de receipt. Fiscale behandeling niet uitgezocht. GOK | Moet een Italiaanse boekhouder zeggen. |
| Terugbetaling op corrispettivi | Geen negatief-voorbeeld in de spec. Te testen. GOK | Mogelijk; anders aparte receipt per dag met min. |
| SDI versturen van TD17 | Alleen op betaalde plannen (eerder onderzoek, developer-account-pagina). GEZIEN in 2026-11-09-pakket-apis.md | Klein; echte verkopers hebben een betaald plan (GOK). |

## Wat open blijft

1. Welke TikTok-entiteit de commissie- en verzendfacturen aan Italiaanse verkopers stuurt, met of zonder Italiaanse btw, en of die via SDI binnenkomen. Bepaalt of stap 3 (TD17) nodig is. Op te halen uit een echte factuur in Seller Center.
2. Niet getest met een echt (trial)account: of `receipts` negatieve bedragen, OSS-tarieven van andere landen en `payment_account` accepteert zoals verwacht; of een kasboekregel in en uit tegelijk kan.
3. Of de commercialista liever per bestelling facturen ziet of één corrispettivo per dag; en welke export (bijvoorbeeld naar TeamSystem) hij gebruikt.
4. Fiscale behandeling van door TikTok gefinancierde kortingen en van affiliatecommissies aan creators (die factureren de verkoper zelf, eventueel via Fonoa; DERDEN https://gestoria247.com/blog/iva-comisiones-tiktok-shop-2026 over Spanje).
5. De volledige App Store-lijst van Fatture in Cloud (laadt met script) is niet doorzocht op een koppeling die wel fees boekt.
6. Al het fiscale hierboven is door een onderzoeker zonder Italiaanse bevoegdheid samengesteld; laat het nakijken door een Italiaanse commercialista voor we het in de app vastleggen.

## Nagekeken (controleur, 9 nov 2026 ±20:15 UTC): akkoord, geen moet-punten
Correcties en aanvullingen; deze gaan voor op de tekst hierboven:
1. **Giroconto: twee regels, geen GOK meer.** In `models/schemas/CashbookEntry.yaml` geldt `amount_in`/`payment_account_in` alleen voor een regel "in" en out alleen voor "out" (GEZIEN door controleur). De uitbetaling wordt dus twee kasboekregels.
2. **Btw-soort bij de commissie:** niet "N2.1/reverse charge" maar "btw-soort 0%, niet onderworpen art. 7-ter, btw via de TD17 met 22%". N2.1 is de code van de buitenlandse leverancier.
3. **Nieuw testpunt:** telt een `self_supplier_invoice` in Fatture in Cloud zelf ook als kosten, naast het `received_document` van TikTok? Dan dubbele kosten of btw (GOK, testen met trial).
4. **Termijn TD17:** naar SDI uiterlijk de 15e van de maand na ontvangst van de factuur, dus per maand plannen, niet per uitbetaling (DERDEN, algemene regel; nog naast de officiële AdE-gids leggen).
5. **Kasboek mogelijk automatisch gevuld:** een receipt met `payment_account` en een betaald ontvangen document maken waarschijnlijk zelf al kasboekregels (enum `CashbookEntryKind`, verder GOK). Dan maakt de app in stap 4 alleen de uitbetaling zelf. Testen op dubbele regels.
