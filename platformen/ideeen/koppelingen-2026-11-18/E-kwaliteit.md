# E. Kwaliteit: fouten, crashes en klachten eerder zien (zoeker E, 18 nov 2026)

Kort: ons testen is al sterk (echte Blender in 3 versies, echte IDE met Starter en Driver plus Plugin Verifier, echte Obsidian met wdio, Het Hol op een Windows-runner met een duurtest van 60 minuten). Wat ontbreekt zit **na de uitgave**: we horen niets als iets bij een gebruiker misgaat, gebruikers hebben geen makkelijke meldweg met de juiste gegevens, en we zien een nieuwe Blender- of IDE-versie pas als de klachten komen. Daar zitten de vijf voorstellen.

## Top 5

### 1. Foutmeldingen van Bison & Flex naar ons dashboard op JetBrains Marketplace (één regel in plugin.xml)
- **Wat:** als onze plugin in de IDE een fout gooit of de IDE laat hangen, krijgt de gebruiker nu alleen "plugin uitzetten". Met één regel in `plugin.xml` komt er een knop "Report to third-party plugin"; de melding (stacktrace, IDE-versie, pluginversie, OS) landt op onze pluginpagina onder twee nieuwe tabbladen, Exceptions en Freezes. Wie in de IDE "fouten automatisch sturen" aan heeft, stuurt ze zonder klik (DERDEN: [error-handler](https://plugins.jetbrains.com/docs/marketplace/error-handler.html)).
- **Probleem dat het oplost:** Bison & Flex draait in CLion, IDEA en andere IDE's die wij niet allemaal testen. Een fout in een IDE-versie die wij niet hebben, zien we nu nooit; de gebruiker zet de plugin uit of geeft een lage review.
- **Hoe het koppelt:** `<errorHandler implementation="com.intellij.diagnostic.JetBrainsMarketplaceErrorReportSubmitter"/>` in `<extensions defaultExtensionNs="com.intellij">`. Beschikbaar sinds 2023.3 (DERDEN: zelfde pagina); onze `sinceBuild` is 252 (GEZIEN `build.gradle.kts`), dus dat past.
- **Waar het draait:** in de IDE van de gebruiker; de meldingen staan op de Marketplace. De hoofdchat leest ze via Chrome op het dashboard. Of er een API voor die tabbladen is weet ik niet (GOK: nee), dus agents lezen ze niet zelf.
- **Kosten:** gratis, geen grens genoemd (DERDEN: zelfde pagina noemt geen prijs).
- **Getest:** nee, alleen de documentatie gelezen (JetBrains SDK [Error Reporting](https://plugins.jetbrains.com/docs/intellij/error-reporting.html) noemt deze klasse als "simplest supported setup"). Te toetsen in onze IDE-test: Plugin Verifier moet de klasse kennen in alle vijf IDE's van `pluginVerification`.
- **Privacy:** de gebruiker ziet eerst wat er gaat en geeft zelf toestemming in het foutvenster van de IDE; JetBrains bewaart het. Geen eigen server, geen eigen privacytekst nodig (GOK; even nalezen bij de keuring).
- **Moeite:** 1 uur (GOK), met verifyPlugin en een uitgave 2026.1.3.
- **Thijs:** niets. Tekst naar buiten: geen, het venster is van de IDE.

### 2. Crashmeldingen uit Het Hol, met toestemming van de speler (Sentry of GlitchTip, gratis plan)
- **Wat:** als Het Hol vastloopt of crasht op de pc van een speler, vraagt het spel bij de volgende start één keer: "Het Hol stopped unexpectedly last time. Send the error log to the developer? Yes / No". Bij Yes gaat het einde van `godot.log` (Godot schrijft daar ook een crash met backtrace in) naar een foutendienst. Zo zien we crashes op videokaarten en schermen die onze runner niet heeft.
- **Probleem dat het oplost:** Hats of the Fallen (Het Hol) is een strook boven de taakbalk die uren naast ander werk draait. Onze duurtest draait op één soort Windows-runner met ANGLE; Next Fest-spelers hebben duizenden soorten pc's. Een crash bij een speler zien we nu alleen als die het in een review zet.
- **Hoe het koppelt:** twee wegen.
  - **a. Nu, op Godot 4.3:** een eigen klein stuk GDScript (±60 regels, GOK): bij start een merkteken "draait", bij netjes stoppen weg; staat het er bij de volgende start nog of staat er `SCRIPT ERROR`/`CrashHandlerException` in het vorige log, dan de vraag hierboven en een `HTTPRequest` POST naar de envelope-ingang van Sentry (werkt ook voor GlitchTip, dat dezelfde ingang heeft). Geen naam, geen IP: `send_default_pii` uit en in het project "IP niet bewaren" aan.
  - **b. Later, bij een Godot-update:** de officiële Sentry-SDK voor Godot (versie 2.5.1, 12 nov 2026, GEZIEN tag in `getsentry/sentry-godot`) vangt ook echte crashes met minidump en heeft een feedbackvenster (`SentryFeedback`). Maar versie 1.x en 2.x eisen Godot 4.5 of nieuwer; Het Hol draait op 4.3 (GEZIEN workflow `steam-hol.yml`). Voor 4.3 is er alleen 0.6.1 van 21 jun 2025 (GEZIEN), oud en niet meer bijgewerkt. Daarom eerst weg a.
- **Waar het draait:** in het spel bij de speler. Lezen door agents: een workflow in Actions met een alleen-lezen Sentry-sleutel als secret, die elke dag nieuwe crashes samenvat in `berichten/olaf.md` (zoals `steam-fest-meting.yml` nu cijfers haalt). sentry.io is vanuit onze shell bereikbaar (GEZIEN 200 op sentry.io/pricing), maar agents typen geen sleutel, dus via Actions.
- **Kosten:** Sentry Developer: $0, 1 gebruiker, 5k fouten per maand (GEZIEN [sentry.io/pricing](https://sentry.io/pricing/)). GlitchTip gratis: tot 1.000 meldingen per maand, 30 dagen bewaard (GEZIEN [glitchtip.com/pricing](https://glitchtip.com/pricing)). Sentry kiezen: meer ruimte en de SDK voor later.
- **Getest:** nee (geen account). Wel gezien: pricing van beide, SDK-eisen, en dat `send_default_pii` standaard uit staat (GEZIEN `doc_classes/SentryOptions.xml`).
- **Privacy:** alleen na Yes van de speler, alleen het log van het spel (daarin staan geen namen; wel even nakijken of het pad met de Windows-gebruikersnaam erin staat en dat eruit filteren). Een regel in de privacytekst op dortus.com en in de Steam-beschrijving. Opt-in, dus geen toestemmingsvenster bij elke start.
- **Moeite:** weg a 4 tot 6 uur incl. test op de runner met een geforceerde crash (GOK).
- **Thijs:** gratis Sentry-account aanmaken met thijs@dortus.com en twee waarden als secret zetten: `SENTRY_DSN` (gaat in het spel, is openbaar van aard) en `SENTRY_READ_TOKEN` (alleen lezen), ±10 min. Tekst naar buiten: de vraag in het spel en de privacyregel zijn producttekst van Dortus; keuring door een ander (skill `keuren`) volgens harde regel 4 zoals die sinds 18 nov 23:17 geldt. Alleen als Thijs als persoon in de privacytekst staat, eerst zijn ja.

### 3. Meldknop in elk product plus vaste meldformulieren in de loketrepo's
- **Wat:** in elk product een knop "Report a bug" die GitHub opent met een ingevuld formulier: versie van ons product, versie van Blender/IDE/Obsidian en het besturingssysteem staan er al in. In de loketrepo's een formulier (issue form) met verplichte velden, zodat elke melding meteen bruikbaar is. Plus een workflow die nieuwe meldingen in de loketrepo's elk uur ophaalt en in `berichten/hoofdchat.md` en via de Discord-webhook zet, zodat de skill `triage` meteen kan beginnen.
- **Probleem dat het oplost:** de loketrepo's `bison-flex` en `click-joints` hebben nu alleen een README, geen `.github/ISSUE_TEMPLATE` (GEZIEN met git clone). Een melding zonder versie kost een rondje vragen; een gebruiker die de repo niet vindt, schrijft een review. Dit geldt voor Click Joints, Bison & Flex en Rollwright.
- **Hoe het koppelt:** GitHub-URL met query-parameters: `.../issues/new?template=bug.yml&version=2026.1.2&ide=...&os=...` vult de velden met dezelfde `id` (DERDEN: [GitHub docs, creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)). In Blender `bpy.ops.wm.url_open` met `bpy.app.version_string`; in de IDE een actie met `ApplicationInfo`; in Obsidian `window.open` met `apiVersion`. Een link openen op klik is geen telemetrie, dus mag ook in Obsidian.
- **Waar het draait:** knop bij de gebruiker; het ophalen in Actions (`GITHUB_TOKEN` leest openbare repo's; vanuit onze sessie geeft api.github.com voor deze repo's "access not enabled", GEZIEN).
- **Kosten:** gratis.
- **Getest:** ja, deels. Een voorbeeldformulier `bug.yml` (versie, IDE, OS, wat gebeurde, foutregels) is GELDIG tegen het schema van GitHub issue forms (GEZIEN, ajv met `json.schemastore.org/github-issue-forms.json`); een fout type wordt afgekeurd (GEZIEN). Een ingevulde URL is 151 tekens (GEZIEN), ver onder de grens.
- **Nadeel:** melden op GitHub vraagt een GitHub-account. Voor ontwikkelaars (IDE, Obsidian, Blender) meestal geen drempel (GOK); voor Het Hol-spelers niet: die melden via Steam-discussies of Discord, of via de feedback van voorstel 2.
- **Moeite:** 1 uur per product voor de knop, 1 uur voor formulieren, 1 uur voor de ophaalworkflow (GOK).
- **Thijs:** niets. De formuliertekst staat in de loketrepo's onder zijn GitHub-account; voor de zekerheid één ja van Thijs op de tekst, daarna volstaat keuren voor wijzigingen (GOK of dit onder "zijn eigen accounts" valt; de hoofdchat beslist). Wie mag pushen naar de loketrepo's weet ik niet (GOK: alleen de hoofdchat); anders zet de hoofdchat de bestanden.

### 4. Elke week testen tegen de volgende versie van Blender, de IDE en Obsidian
- **Wat:** een geplande workflow (maandag) die onze bestaande tests draait tegen wat er aankomt: Blender 5.4 alpha en de nieuwste patchversies (5.2.4 staat er al, wij testen 5.2.3), IntelliJ en CLion EAP in verifyPlugin en de IDE-test. Rood is een bericht aan de eigenaar, geen blokkade.
- **Probleem dat het oplost:** nu horen we van een nieuwe versie pas als gebruikers klagen. Voorbeeld uit ons eigen onderzoek: Archimesh kreeg reviews als "Please update compatibility for Blender 5" (GEZIEN door Noor, `platformen/ideeen/noor.md`). Onze product-workflows draaien alleen bij een push (GEZIEN: alleen dashboard, keurder, scorebord, wegwijzer en fest-meting hebben een `schedule`), dus zonder wijziging test niemand tegen nieuwe versies.
- **Hoe het koppelt:** GitHub Actions `schedule`. Blender: de lijst van builder.blender.org als JSON (`/download/daily/?format=json&v=1`) geeft per versie de download; GEZIEN vandaag voor Linux x64: 4.2.23, 5.2.4, 5.3.0 stable en **5.4.0 alpha**. JetBrains: `pluginVerification { ides { recommended() } }` of een EAP-versie erbij. Obsidian: e2e gebruikt al "latest"; de beta (catalyst) vraagt inloggen met een insider-account, dus alleen als Thijs dat wil.
- **Waar het draait:** Actions (builder.blender.org werkt ook vanuit onze shell, GEZIEN 200).
- **Kosten:** gratis; Actions-minuten zijn gratis voor openbare repo's (DERDEN: [GitHub Actions billing](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)). Belasting: één keer per week ±40 min Blender plus ±30 min IDE (GOK uit de `timeout-minutes` van de huidige workflows).
- **Getest:** de Blender-lijst ja (zie boven). De workflow zelf niet.
- **Moeite:** 2 tot 3 uur (GOK): matrix uit de huidige workflows hergebruiken met een invoer "versie".
- **Thijs:** niets. Geen tekst naar buiten.

### 5. Schermafbeeldingen automatisch vergelijken met de vorige run
- **Wat:** onze workflows maken bij elke run tientallen schermafbeeldingen (tak `schermen`), en Daan of de keurder kijkt ze met het oog na. Een stap met `pixelmatch` vergelijkt elk nieuw plaatje met het vorige op de tak en schrijft per plaatje "gelijk" of "veranderd: x procent" plus een verschilplaatje met de rode plekken. Zo kijkt de keurder alleen naar wat veranderde, en valt een onbedoelde verandering op.
- **Probleem dat het oplost:** onbedoelde beeldfouten in Click Joints (paneel, gradenboog), Bison & Flex (structuur, meldingen) en Rollwright (skins) die tussen twintig gelijke plaatjes niet opvallen.
- **Hoe het koppelt:** npm-pakket `pixelmatch` met `pngjs` in een workflowstap (of ImageMagick `compare`, staat al in de Blender-workflow).
- **Waar het draait:** Actions, na de schermstap.
- **Kosten:** gratis (MIT).
- **Getest:** ja, op onze echte plaatjes van de tak `schermen` (GEZIEN):
  - Click Joints `1-paneel-x.png` en `2-gewricht-x.png` (Blender 5.3.0): 0 px verschil over 6 runs op rij. Blender is dus helemaal stabiel; elke verandering is echt.
  - Bison & Flex `clion-donker-calc-y.png`: 3.415 tot 3.759 px verschil tussen runs (0,066 tot 0,073 procent), kleine ruis.
  - Rollwright `1-leesweergave.png`: 283 tot 744 px (0,035 tot 0,091 procent), allemaal in één vak (x 115 tot 586, y 201 tot 785): de worpen zijn willekeurig. Een vaste zaad voor de dobbelstenen in e2e of een grens van 0,5 procent lost dat op.
- **Moeite:** 2 tot 3 uur voor alle drie (GOK), met een klein script dat ik al werkend had (`cmp.mjs`, 12 regels).
- **Thijs:** niets.

## Afgevallen
- **Plugin Verifier en IDE-starter-tests:** hebben we al (`verifyPlugin` tegen 5 IDE's, `integrationTest` en `clionTest` met Starter en Driver).
- **Blender-tests in Actions:** hebben we al (3 versies, Xvfb, `extension validate`, achtergrond- en schermtest).
- **Obsidian-plugintests:** hebben we al (vitest met nep-Obsidian, wdio met `obsidian-launcher`, scanner-lint).
- **gdUnit4 of GUT voor Het Hol:** gdUnit4 v5 werkt met Godot 4.3 (GEZIEN README), GUT 9.7.1 bestaat (GEZIEN tag), en er is een Action (`gdUnit4-action` v1.4.3). Maar onze eigen toetsen (`toets_systemen` en drie andere, 0 FOUT-regel) doen het werk al; een framework geeft vooral nettere uitvoer. Gereedschap om het gereedschap.
- **Sentry of andere telemetrie in Rollwright:** verboden: "Do not include any client-side telemetry" (GEZIEN `obsidian-developer-docs`, Developer policies). De meldknop van voorstel 3 mag wel.
- **Automatische foutmeldingen uit Click Joints:** Blender laat add-ons alleen online gaan als de gebruiker "Allow Online Access" aan heeft (GOK, niet nagelezen); de meldknop is eenvoudiger en genoeg.
- **Officiële Sentry-SDK nu in Het Hol:** eist Godot 4.5+; wij zitten op 4.3. Pas bij een Godot-update (zie voorstel 2b).
- **Steam-foutrapporten (minidumps via Steamworks):** Het Hol gebruikt de Steam-API niet (GEZIEN: geen GodotSteam of steam_api in `producten/steam-hol/godot`), dus dit werkt niet zonder extra plugin.
- **Eigen ErrorReportSubmitter naar GitHub voor Bison & Flex:** meer werk dan de Marketplace-versie en de meldingen worden openbaar; pas als het dashboard tekortschiet.
- **Percy, Chromatic, Argos voor beeldvergelijking:** vragen een account en zijn voor websites; pixelmatch doet het hier.
- **odiff:** geïnstalleerd (`odiff-bin`), niet nodig naast pixelmatch.
- **Sentry MCP voor agents:** vraagt inloggen in de sessie; de Actions-route met een lees-sleutel is genoeg.
- **Obsidian-beta in de e2e:** vraagt een insider-account; stap voor Thijs als hij dat ooit wil, niet nu.

## Bronnen
- JetBrains Marketplace error handler: https://plugins.jetbrains.com/docs/marketplace/error-handler.html
- IntelliJ SDK Error Reporting: https://plugins.jetbrains.com/docs/intellij/error-reporting.html en https://plugins.jetbrains.com/docs/intellij/ide-infrastructure.html
- Sentry voor Godot: https://github.com/getsentry/sentry-godot (README, CHANGELOG, tags 0.6.1 en 2.5.1, `doc_classes/`) en https://docs.sentry.io/platforms/godot/
- Sentry pricing: https://sentry.io/pricing/
- GlitchTip pricing: https://glitchtip.com/pricing
- Obsidian developer policies: https://github.com/obsidianmd/obsidian-developer-docs (`en/Community directory/Developer policies.md`)
- GitHub issue forms en URL-parameters: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue en schema https://json.schemastore.org/github-issue-forms.json
- GitHub Actions billing: https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions
- Blender daily builds: https://builder.blender.org/download/daily/?format=json&v=1
- pixelmatch: https://github.com/mapbox/pixelmatch
- gdUnit4: https://github.com/godot-gdunit-labs/gdUnit4 ; GUT: https://github.com/bitwes/Gut
- Eigen repo: `.github/workflows/` (steam-hol*, blender-gewrichten-e2e, jetbrains-bison-flex-e2e en -clion, rollwright-e2e), tak `schermen`, loketrepo's `thijsduinhouwer2002-coder/bison-flex` en `click-joints`.
