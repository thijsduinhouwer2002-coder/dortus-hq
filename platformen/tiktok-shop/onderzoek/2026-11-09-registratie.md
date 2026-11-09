# Registratie als app-ontwikkelaar: wat de docs zeggen (Tess, 9 nov 2026, 05:10 tot 05:30 UTC)

Gelezen met curl via de open docs-API: `https://partner.tiktokshop.com/api/v1/document/detail?document_id=<id>&workspace_id=3&aid=359713&locale=en-US`. Alle citaten letterlijk (GEZIEN). De gids voor documentsoorten per land staat op Feishu en vraagt inloggen (curl geeft 302 naar een loginpagina): niet gelezen.

## Partner registration application requirement
https://partner.tiktokshop.com/docv2/page/64f19899cb677b0286e75d67

- `| Full company name | Text | requires the name of the company's business license, no more than 100 characters <br> *Should be consistent with company document |`
- `| Date of registration | Date | Year/Month/Day |`
- `| Company registration number | Text | No more than 100 characters <br> *Should be consistent with company document |`
- `| Company document | Image (jpg/jpeg/png) | Selection based on company entity, refer to [guidance](https://bytedance.feishu.cn/docx/XkYVdMmwwoTCkjxBo56couGEnP5?from=from_copylink). and the picture does not exceed 10M |`
- `| Business owner ID | Image (jpg/jpeg/png) | Each module only supports uploading 1 picture, and the picture does not exceed 10M |`
- `Common qualification information will keep same for different categories . You only need to fill in one time while onboard. If you want to apply for the new category, common qualification information will be automatically reused and you don't need to fill in again. For certain corporate partners, TikTok Shop may also require information and supporting documents relating to the company's Ultimate Beneficial Owner(s) (`
- `| Partner logo | Image (jpg/jpeg/png) | Size 1080*1080, no more than 30M |`
- `| Business address | text | The company operating address represents your current working address. Please fill in in English and follow the rules: country + region + specific address + post code; no more than 150 characters |`
- `| Company introduction | PDF | Please upload a document about the basic introduction of the company, including such as the introduction of the company's business capabilities, team composition, successful cases, etc.; the document is in PDF format and should not exceed 30M |`
- `| Brief company introduction | Text | Please briefly introduce the company's background description. The introduction will be displayed on behalf of the partner in other scenarios in the future, and it needs to be filled in properly; no more than 1000 characters |`
- `| Documento nacional de identidad (DNI) <br> *only required in the Spain and Ireland market | Upload pictures and input Character | 1. Upload front and back image of DNI <br> 2. First, Middle, Last Name <br> 3. Card number <br> 4. Date of Birth |`

## Developer onboarding
https://partner.tiktokshop.com/docv2/page/6789f73f18828103147a8ca1

- `* If you don't have these ready, select **Save for later**; you can then go *Back to profile* or *Create app or service*. (If you create an app now, you can't publish it until certification is complete.)`
- `> ⚠️ Use the right email for your developer type. If you want to register as an app developer or system integrator (ISV), do not use the email associated with your TikTok Shop seller account. If you register with a Shop account email, the system will identify you as a seller and you can only register as a seller developer.`
- `* **Registration region:** must be consistent with your company's business certification.`
- `* **Target market:** cross-border partners (registration region China and/or Hong Kong, China) may select UK, MY, VN, TH, PH, or SG; local partners (entities in the local market) should choose only their local market.`
- `If you already have an ISV app and want to expand it, you can start from that app's **+ Add market (Seller type)** dialog. See **Add markets to an existing app** in [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app) for the complete flow.`
- `Once you've registered as a developer partner, initiate the compliance and legal review. It can take **three or more weeks**. Reviews are required case-by-case for some partners, but are **always required for US and UK partners**.`
- `3. **Initiate the compliance and legal review** — required for US and UK partners (and case-by-case for others). This step can take **three or more weeks**, so start planning for it early.`

## Register as a service partner
https://partner.tiktokshop.com/docv2/page/64f19887dc7f3e028d381064

- `* **Registration Region:** Please ensure the region is consistent with your company's business certification.`
- `* Local partners (entities in the local market) should choose only the local market as their target market.`

## Seller Center development shops
https://partner.tiktokshop.com/docv2/page/64f199a2dc7f3e028d383538

- `| Business / KYC information | Not required for basic setup. | Required. Business and KYC information must be valid and may be reviewed. |`
- `| Financial statements and settlements | No | Yes |`
- `| Netherlands | NL (528) | Yes | Yes |`
- `| Full Function Account | A production-like test account that requires business and KYC information. It supports Core Account capabilities plus linked Official Test TikTok Accounts and Buyer Test TikTok Accounts. Use it for buyer checkout, product discovery, finance, settlement, customer service, and full-flow testing. |`
- `| Core Function Account | A lightweight test account that does not require real business information, TikTok account setup, or credit card information. It is used mainly for product, order, and fulfillment testing inside Partner Center. It does not support real buyer checkout, finance, settlement, or customer-service scenarios. |`

## Create a test seller account
https://partner.tiktokshop.com/docv2/page/686da7797cac2a04985d83a1

- `* Binding a test Seller account to your developer account is **permanent and cannot be undone**, so set it up deliberately.`
- `6. For **"Onboarding type"**, select **individual**. An **individual** seller onboards with minimal personal details, while a **business** seller must provide company and registration documents. For getting started, choose **individual**.`

## Create a TikTok Shop App (OAuth client)
https://partner.tiktokshop.com/docv2/page/686da778633023048bd10368

- `For getting started and testing, choose **custom**: it does not require app review and can immediately access the data of your linked test Seller or Creator account. You can create a **public** app later, when you are ready to distribute it on the App Store.`
- `* **App Secret**`

## App review process
https://partner.tiktokshop.com/docv2/page/64f199e5dc7f3e028d383d2b

- `| Registration review | Required | Required before broader launch when Partner Center requests it | Developer onboarding required; marketplace app review is usually not required for own-shop use | Confirms developer qualification and launch eligibility | Usually 5 business days after complete submission |`
- `| App design / ARD review | Required when Partner Center requests ARD or design materials | Required if the app is a Connector app, reaches 25 or more seller authorizations, or Partner Center requests review | Usually not required for own-shop use | Reviewer checks whether the App Requirement Document (ARD) and design materials cover required TikTok Shop use cases | Usually 3-5 business days after complete materials `
- `| App development and app review | Required | Required for Connector apps, custom apps with 25 or more seller authorizations, or apps otherwise flagged by Partner Center | Usually not required for own-shop use | Reviewer tests the app, checks API scope usage, verifies seller-facing flows, and reviews product evidence | Usually 7-10 business days after a complete testable build is submitted |`
- `| Language listing review | Required for every public app and for each target market or listing language | Not required unless the custom app is being upgraded to public or Partner Center requests listing materials | Not required | Confirms that App and Service Store listing content is accurate and market-language compliant | Usually 7-10 business days per submitted market or language |`
- `| Compliance, legal, data security, and privacy review | Required when applicable and must be passed before listing | Required when applicable based on market, category, data access, or Partner Center request | Required when Partner Center requests it | Data Security and Privacy Review (DSPR) assessment is commonly planned at about 2 weeks; full compliance/legal review may take 3 or more weeks. US data-security revie`

## Data security and privacy review
https://partner.tiktokshop.com/docv2/page/6506b876b99d5302be77f448

- `| Q14 — Privacy policy | State whether you maintain an up-to-date privacy policy for sellers and customers. If Yes, provide a working link to the policy and make sure it applies to your company and service. This is distinct from the internal procedures in Q12. |`
- `| Data Security and Privacy Review (DSPR) | Partners or apps that access, process, store, or transmit TikTok Shop Protected Data. Required before App Store launch when Partner Center or the review team requests it. | TikTok Shop privacy, security, compliance, or review teams, depending on market and app scope. | The DSPR assessment is commonly planned at about **2 weeks** after a complete submission. Full compliance `

## Gezocht en niet gevonden
In alle 16 gelezen pagina's gezocht op: sole proprietor, individual developer, personal account, without a company/business, freelancer, KVK, Chamber of Commerce. Geen treffer. Er staat dus geen route voor particulieren in de docs (wat niet betekent dat TikTok een eenmanszaak weigert).

