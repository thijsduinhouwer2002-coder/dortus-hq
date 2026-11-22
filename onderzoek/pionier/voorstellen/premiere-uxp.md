# Voorstel: Premiere UXP-plugins (Adobe Creative Cloud Marketplace)

Noor (pionier), 8 nov 2026. Nagekeken door een controleur (agent): akkoord, met correcties die hieronder verwerkt zijn. Eigen meting van de hele Premiere-lijst in Adobe Exchange (1.477 listings, waarvan 223 UXP) met datum, downloads en prijs per plugin. Data: `data/premiere-uxp-2026-11-08.json`, meten: `node data/premiere-uxp-meet.js <uitvoer.json>`, analyse: `python3 data/premiere-uxp-analyse.py <bestand.json>`.

## Waarom dit platform
Zelfde soort kans als Reddit Devvit: een groot platform dat al zijn makers naar een nieuwe, jonge pluginlaag dwingt, met harde datums. UXP is sinds december 2025 algemeen beschikbaar in Premiere 25.6 (GEZIEN, https://blog.developer.adobe.com/en/publish/2025/12/uxp-arrives-in-premiere-a-new-era-for-plugin-development). In september 2026 legde Adobe het einde van de oude laag CEP vast (GEZIEN, https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications):
- Premiere: vanaf december 2027 geen nieuwe CEP-plugins meer in de Marketplace, vanaf december 2028 staat CEP standaard uit.
- December 2029: CEP zit niet meer in nieuwe versies van alle grote apps.
- After Effects krijgt een openbare UXP-beta "by November 2026". Dat is een tweede golf, met een nog grotere markt voor panels (aescripts).

## De vijf vragen

### 1. Groeit het platform hard en zichtbaar? Zwak.
- Premiere zelf groeit niet hard. Adobe groeit in omzet ±13% per jaar (DERDEN, https://ymcinema.com/2026/06/16/adobe-stock-free-fall-creative-software-empire/), maar het aandeel daalde in 2026 ±37 tot 40% en er is veel berichtgeving over editors die naar DaVinci Resolve gaan (DERDEN, https://erkansaka.net/2026/06/01/davinci-resolve-adobe-video-editing-dominance/). Adobe noemt geen gebruikersaantal meer. GOK: Premiere is groot (tientallen miljoenen) en ongeveer vlak.
- Wat wel hard groeit is de nieuwe laag. Nieuwe UXP-plugins voor Premiere per maand (GEZIEN): dec 2025 6, jan 5, feb 9, mrt 6, apr 11, mei 13, jun 18, jul 29, aug 31, sep 45, okt 37. Ter vergelijking: nieuwe CEP-plugins (ZXP) voor Premiere 5 tot 15 per maand in 2026 (GEZIEN). De nieuwe laag haalde de oude in april in (11 tegen 7).
- Alle 223 UXP-plugins samen: 22.636 unieke downloads (GEZIEN). De oude laag heeft nog ±1.254 listings met miljoenen downloads (Motion Bro 517.288). Die moeten allemaal over.
- Eerlijk: dit is groei door een gedwongen overstap, niet doordat het publiek groeit. Rond 2028 tot 2029 stopt die groei (CEP standaard uit in dec 2028, maar gebruikers kunnen het dan nog aanzetten; weg in dec 2029). Volgens mijn rol weegt dit zwaar, en het is het zwakke punt.

### 2. Is de winkel jong of gaat hij net open? Ja.
- UXP-plugins voor Premiere sinds eind november 2025 in de Marketplace (eerste op 27 nov), nu 223 (GEZIEN). 69% kwam vanaf 1 juli 2026 (154 van 223), 77% vanaf 1 juni (GEZIEN).
- Categorieën (GEZIEN): Tools & Automation 197, Publish & Handoff 46, Collaboration 44, Design Assets 31, Usability & Testing 26 (een plugin kan in meer categorieën staan).

### 3. Kan er betaald worden? Ja, nu al, met de beste voorwaarden die ik zag.
- Adobe rekent af via FastSpring, is verkoper (merchant of record) voor de EU met btw, eenmalig of abonnement, **10% afdracht** (GEZIEN, https://developer.adobe.com/premiere-pro/uxp/plugins/distribution/adobe-marketplace). Ook zelf verkopen buiten de winkel mag (niet-exclusief).
- 67 van de 223 UXP-plugins zijn betaald (GEZIEN). Prijzen meestal $5 tot $20, uitschieters $40 tot $65.
- Verkoop: voor een betaalde listing tel ik unieke downloads als kopers (GOK, Adobe zegt niet precies wat de teller is). Dan: mediaan 2 kopers per betaalde UXP-plugin (GEZIEN, de teller). Eén grote uitschieter: Mask To Motion ($19,99, sinds 5 aug 2026) 1.228 downloads, dat zou ±$22.000 netto zijn in drie maanden (GOK op GEZIEN). Daarna Cut to Beat ($4,99) 121, SuperSync ($9,95) 103, de rest onder 70.
- Ter vergelijking: betaalde CEP-plugins van mei 2025 tot sep 2026 (112 stuks) mediaan 0 downloads (GEZIEN). Een nieuwe betaalde plugin verkoopt dus meestal weinig, ook in de oude laag.

### 4. Is er al vraag te zien? Ja.
Terugkerende verzoeken op de forums (onderzoeker, GEZIEN op de pagina's):
- Batch export van losse clips of meerdere sequences (https://community.adobe.com/feature-requests-730/feature-request-streamlined-batch-export-for-individual-edited-clips-1329125).
- Markers exporteren naar CSV of tekst, 5.088 keer bekeken (https://community.adobe.com/questions-729/export-multiple-clip-markers-1376454).
- Clips, bins en sequences in bulk hernoemen (https://community.adobe.com/feature-requests-730/batch-rename-for-clips-in-project-panel-1330019).
- Gereedschap voor de assistent-editor: organiseren en controleren voor aflevering (https://community.adobe.com/feature-requests-730/tools-for-assistant-editors-1328309).
- Ondertitels lezen en bewerken (https://forums.creativeclouddeveloper.com/t/12405), maar dat kan de API nog niet.
De makers reageren al: in de winkel staan sinds juli 2026 kleine betaalde tools voor precies deze verzoeken (zie vraag 5). Dat bevestigt de vraag, en laat zien dat het snel voller wordt.

Wat een UXP-panel nog niet kan (onderzoeker, GEZIEN op forums.creativeclouddeveloper.com): geen knippen (razor) via de API (t/11375), captions niet lezen of bewerken (t/12405), geen drag-and-drop uit het panel (t/11373), grote bewerkingen op de tijdlijn kunnen bevriezen (t/11882). Wel: projectitems, bins, metadata, clips invoegen, in- en uitpunten, markers, effectparameters, export. Adobe-medewerker: doel is volledige gelijkheid met CEP eind 2026 (t/11408).

### 5. Is de eerste plek in een categorie nog te pakken? Ja, in workflow voor de assistent-editor.
Categorie: **aflevering en projectorde** (batch export met naamgeving, markers exporteren, hernoemen, controle voor aflevering). De huidige UXP-spelers (GEZIEN, downloads):
- Batch Exporter for Premiere Pro ($5) 30, Batch Export for Premiere Pro ($2) 25, Batch Export PRO ($39) 2
- MarkerBuddy Pro ($49,99) 15, Transcript Batch Export ($4,99) 7
- Batch Rename and Metadata ($29,90) 6, Renamer PRO ($39) 4, Bin-Laden ($0,99) 10
- Sequence checker ($22,99) 0, Timeline Preflight ($14,99) 0, Turnover Guard ($39) 0, Relink Bridge ($49) 0
Geen enkele betaalde tool heeft 100 kopers. Maar de gratis tools zijn groter (controleur, GEZIEN): File Location Checker 113, MarkerBuddy (gratis) 100, CutCue.io CSV Marker Importer 83, Magic Marker 78, Marker Exporter for Premiere Pro 65, Sequence Batch Renamer 31, Sequence Check 23, plus een rij kleintjes onder 10. Samen ±30 UXP-listings in deze hoek, allemaal klein. Gebruikers kiezen nu vooral gratis. Markers exporteren is als los ding al gratis te krijgen; het betaalde deel moet dus in batch export, controle en het geheel zitten. Eén goed ontworpen, mooi panel dat deze klussen samen doet ("alles voor de oplevering") kan nummer één worden. In de oude laag bestaan die tools wel (editingtools.io, aescripts MassRename, Premiere Studio met 20.640 downloads), maar hun klanten moeten uiterlijk vóór december 2029 iets nieuws vinden (in december 2028 krijgen ze al de duidelijke waarschuwing: CEP staat dan standaard uit).
Al bezet in UXP: easing (OpenCurve 2, 1.990 gratis), safe zones (FrameGuard Social 952), AI-onderwerpen van grote diensten (Topaz, sync., Fluen), maskers volgen (Mask To Motion).

## Risico en waaraan je het ziet
- Premiere verliest gebruikers aan Resolve en CapCut. Teken: Adobe meldt dalende Creative Cloud-omzet, of de nieuwe UXP-instroom zakt onder 20 per maand.
- De winkel loopt vol vóór wij er zijn: 45 nieuwe in september, veel kleine betaalde tools in onze categorie. Teken: een workflow-panel haalt 300+ kopers voor wij lanceren.
- Adobe bouwt het zelf in (batch export staat op de verzoekenlijst). Teken: release notes van Premiere 27 met batch export of marker-export.
- Mediaan 2 kopers per betaalde plugin. Zonder opvallend product verkopen we niets. Ons voordeel moet uiterlijk en gemak zijn (de lat van Thijs).
- Testen in de echte app: Premiere draait niet op de Linux-computers van GitHub Actions en vraagt een Adobe-login. Dat maakt e2e-testen moeilijk (GOK, moet een manager uitzoeken).

## Eerste productidee
"Oplevering" (werktitel): één UXP-panel voor de laatste stap van een montage. Batch export van sequences en losse clips met naamregels, markers en ondertitel-tijden naar CSV en tekst, hernoemen van clips en bins in bulk, en een controle voor aflevering (lege stukken, flitsframes, offline media). Gratis basis (markers en hernoemen, want dat is al gratis te krijgen), Pro $19 eenmalig (batch export met naamregels en de controle voor aflevering). Later dezelfde basis naar After Effects UXP.

## Cijfer en advies
**Cijfer 5, nog niet klaar.**
Winkel jong, betalen werkt met 10% afdracht, downloads zichtbaar, harde datums die vraag maken en een versnipperde categorie zonder leider: vier vragen kloppen. Maar de kern van de pioniersdroom, meegroeien met een groeiend platform, klopt niet: Premiere zelf groeit niet, alleen de nieuwe laag, en die groei stopt rond 2028 tot 2029. Daarbij kiezen gebruikers in onze categorie nu vooral gratis tools. En een gewone nieuwe betaalde plugin verkoopt mediaan 2 keer.

Herhaalmeting rond 8 dec 2026 met hetzelfde script. Dan een 6 (ja, kleine inzet) als: de betaalde workflow-tools hierboven samen met 50%+ stijgen, of er een betaald workflow-panel boven 100 kopers komt dat laat zien dat de categorie verkoopt, en de UXP-instroom boven 30 per maand blijft. Ook dan meten: de After Effects UXP-beta (aantal plugins, eerste betaalde), want als die opengaat is de markt twee keer zo groot. Een 3 als de instroom zakt of Adobe batch export zelf inbouwt.

Voor Vera: Mask To Motion (±1.228 kopers van $19,99 in drie maanden, GOK) is mogelijk bewijs dat een kleine maker hier nu verdient. Haar meetlat past hier misschien beter dan de mijne.
