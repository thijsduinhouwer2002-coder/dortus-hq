# Thijs, accounts en naar buiten

Lees dit als iets Thijs, zijn accounts, de browser of iets openbaars raakt.

## Wanneer Thijs vragen (aangescherpt 16 nov 2026 21:12)
Thijs: "alleen over 1, de rest vertrouw ik jou mee en heb geen tijd om continu te doen". Hij beslist alleen nog over:
- **Geld uitgeven.** Elke euro of dollar: wat, hoeveel, waarom.

Daarnaast blijven de stappen die alleen hij **kan** doen (geen keuze, maar zijn handen): inloggen met zijn wachtwoord, een account aanmaken, betalen, voorwaarden accepteren, een sleutel (token) of secret aanmaken, eigen gegevens invullen, plaatsen onder zijn naam op plekken die voor ons geblokkeerd zijn (Reddit). Zet die klaar zodat het hem zo min mogelijk tijd kost.

Al het andere beslist de ploeg zelf: Daan keurt (Iris bij Hats), de hoofdchat zet de eerste lancering live (updates van een product dat al live staat: zie `regels/uitbrengen.md`) en meldt het in het eindantwoord van haar ronde. Dat geldt ook voor de site, filmpjes, winkelteksten, uploads van gekeurde versies, nieuwe kanalen en wat lastig terug te draaien is; daar beslist de hoofdchat met extra zorg en schrijft het waarom in `organisatie/besluiten.md`. Vaste afspraken van Thijs blijven gelden (Hats-spelerstekst schrijft hij zelf, geen AI-zin in posts, Ebb geen medische claims, geen AI-beeld of -geluid op Steam, privacyregels van de openbare repo).

**Inloggen via Chrome (Thijs, 17 nov 16:50):** de hoofdchat mag in de Chrome van Thijs (HP of werklaptop) overal inloggen met zijn Google-account, vakjes aanvinken, voorwaarden accepteren en doorklikken, zonder het eerst te vragen. Grenzen die blijven: geld uitgeven blijft een ja van Thijs; ID-controle, bankgegevens en andere persoonsgegevens vult Thijs zelf in; een openbaar bericht onder zijn naam gaat pas na zijn ja op de tekst; niets verwijderen wat niet van ons is. Geplande agents hebben geen browser: zij zetten zulke stappen klaar voor de hoofdchat in `berichten/hoofdchat.md`, niet voor Thijs.

Agents melden zo'n vraag of stap in `berichten/hoofdchat.md`; alleen de hoofdchat zet hem op `organisatie/lijst-thijs.md` (max 5, regel Thijs 17 nov). Schrijf erbij: wat, waarom, een link, en precies wat hij moet doen. Zet alles klaar wat klaargezet kan worden. Ga daarna door met ander werk.

## Koppelingen en Chrome (Thijs 19 nov 17:31)
Het gedeelde account is voorbij (overstap 7 nov). Koppelingen zijn nu een lijst van wat mag (CLAUDE.md regel 7); een koppeling die er niet op staat is verboden, ook als hij in je run beschikbaar is.
- **Gmail (privé-mail van Thijs): iedereen mag lezen** (Thijs 19 nov 17:02). Alleen lezen: nooit versturen, beantwoorden, verwijderen of labels zetten, en niets uit een mail in de repo behalve de zakelijke kern (regel 2 blijft). Mail aan thijs@dortus.com komt daar niet binnen.
- **Metricool:** plaatsen doet alleen de Maker van Roep (`marketing/REGELS.md`). De hoofdchat mag lezen en een foute post weghalen. Andere agents gebruiken Metricool niet.
- **Claude Code Remote** (geplande taken, repo's koppelen) en **context7** (actuele documentatie, `.mcp.json`) mogen.
- **Alle andere niet**, ook AnythingMCP, Trello, Atlassian, Claude Docs, Search1API, Polar, Shopify en Kondo. Polar lees je via de sleutel `POLAR_TOKEN` in een workflow, niet via de koppeling.
- **Chrome:** alleen op de HP van Thijs en zijn werklaptop (privé Google-profiel, Thijs 19 nov 10:18), en alleen de hoofdchat. Kies nooit een andere browser.
- Open of wijzig nooit chats, projecten of geplande taken die niet bij Dortus horen. Dortus-taken zijn de agents (Olaf, Bram, Daan, Sanne, Iris, Chris en wie later weer aangaat), de hoofdchat-ronde, de taken die met "Dortus" beginnen en de herinneringen van de hoofdchat.

## Wat je mag lezen en schrijven (besluit Thijs, 7 nov 2026)
- **Lezen:** alles wat openbaar is. Elke website, openbare API of open data, ook de winkel-API's van bijvoorbeeld SketchUp (extensions.sketchup.com/warehouse/...) en de Autodesk-winkel. Rustig, en bij anderen alleen lezen.
- **Schrijven en bewerken:** alles in de repo's van thijsduinhouwer2002-coder. De afspraken hieronder over wie waar schrijft blijven gelden, zodat jullie elkaars werk niet overschrijven.
- Wat agents nooit doen: inloggen, accounts aanmaken, betalen, gegevens of wachtwoorden invullen, voorwaarden accepteren, andermans spullen verwijderen, posten onder de naam van Thijs. De hoofdchat mag inloggen met Google en voorwaarden accepteren (zie "Inloggen via Chrome" hierboven); betalen, gegevens invullen, andermans spullen verwijderen en posten onder de naam van Thijs zonder zijn ja blijven ook voor haar verboden.

## Posten op de kanalen van Dortus (18 nov 2026, 23:17)
Thijs koos: posts op de eigen kanalen van Dortus (YouTube, TikTok via Metricool, de Discord van Hats, later nieuwe Dortus-kanalen) gaan eruit na een keuring door een ander (skill `keuren`), zonder zijn ja per post. Een agent schrijft, een ander keurt; op TikTok en YouTube plaatst de Maker van Roep (`marketing/REGELS.md`), elders de hoofdchat, en het komt in `geplaatst.md` of het logboek van het kanaal. Vaste afspraken blijven: geen AI-zin in posts en **nergens een AI-melding** (Thijs, 19 nov), Hats-spelerstekst schrijft Thijs, beelden uit het echte product. Mislukt een post of komt er een klacht, dan haalt de hoofdchat hem weg en meldt het Thijs. **Filmpjes:** een filmpje gaat pas naar Metricool of YouTube als `python3 organisatie/controle/geluid_check.py <bestand>` GOED zegt; uit een release alleen de `-geluid.mp4`, nooit het stille bronfilmpje (keuring R6, 19 nov; filmpje 7 ging eerder zonder geluid). Onder de naam van Thijs (mail, zijn eigen Reddit, berichten aan persmensen en streamers) blijft zijn ja op de tekst nodig.

## Plaatsen op Reddit en andere communities (16 nov 2026)
Op Reddit plaatst Thijs zelf (de browser van de hoofdchat is daar geblokkeerd, zie onder); de hoofdchat zet titel, tekst en beeld klaar. Andere communities onder de naam van Thijs: alleen de hoofdchat, en alleen na zijn ja op de precieze tekst en het beeld. Agents schrijven en zoeken de regels van elke community uit (zelfpromotie, dag, flair), plaatsen nooit zelf. Eén product per community per keer, geen dubbele posts, reageren op vragen doet de hoofdchat met Thijs. Beelden en filmpjes komen uit het echte product; een render staat er als render bij.

## Hats: spelerstekst schrijft Thijs (16 nov 2026)
Alles wat een speler van Hats leest (in het spel, op de Steam-pagina, in de Steam-aankondigingen) is **concept** tot Thijs het in eigen woorden heeft geschreven. Agents mogen voorstellen, maar zetten geen eigen tekst als definitief in het spel of op de pagina. Nieuwe tekst gaat in `platformen/steam/teksten-thijs.md` met status CONCEPT; Thijs zet hem op DEFINITIEF. Liever een icoon of beeld dan een zin. Code en 3D uit scripts vallen hier niet onder.

## Hoofdchat: een idee van Thijs eerst bruikbaar maken (16 nov 2026)
Thijs (17:19): "jij schiet dit gelijk af, maar als ik dan een logische follow-up stel wil je het wel ... dat gebeurt structureel." Werkwijze voor de hoofdchat bij elk idee van Thijs:
1. Zoek eerst de versie van het idee die wel werkt, en stel die zelf voor met de volgende stap (wie, wanneer).
2. Wijs alleen het deel af dat niet klopt, met een reden. "Nee" is nooit het hele antwoord.
3. Toegeven na een vervolgvraag mag alleen als de vervolgvraag echt iets nieuws toevoegt; zeg dan wat er nieuw aan is. Anders blijf je bij je oordeel.
- **Aanvulling 16 nov 17:55:** Reddit is voor de browser van de hoofdchat geblokkeerd ("This site is not allowed due to safety restrictions"). Niet omzeilen via een andere browser. Op Reddit plaatst Thijs dus zelf; de hoofdchat zet titel, tekst, beeld en de controle van de regels kant-en-klaar klaar en legt daarna vast wat geplaatst is.

## Browser: de hoofdchat doet het werk (19 nov 2026, 10:20)
- De hoofdchat opent zelf de tabbladen in de Chrome van Thijs (HP of werklaptop) en doet alles zelf. Tabbladen blijven open zolang Thijs ermee bezig is; niet uit zichzelf sluiten.
- **Inloggen met Google waar Thijs al is ingelogd: gewoon zelf op "Doorgaan met Google" klikken.** Geen wachtwoord typen, wel klikken.
- Alleen wat echt niet kan (wachtwoord intypen, een code van zijn telefoon, CAPTCHA, geld) vraagt de hoofdchat kort aan Thijs, en daarna gaat ze zelf verder.
