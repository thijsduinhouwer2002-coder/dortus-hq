# H. Hackathons nagelopen (onderzoeker H, do 19 nov 2026, nacht)

Opdracht: controleren of de route van B (`B-nieuwe-routes.md`, route 1) echt kan, zodat Thijs morgen kan beslissen. Alle regels hieronder zelf gelezen met curl op de officiële pagina's (19 nov). Citaten staan letterlijk in het Engels. Ruwe pagina's staan niet in de repo; elke link is met curl na te lezen.

**Kort antwoord:** Reddit ja, nu meteen (Gloop's Hat Tower past, geen AI-melding, 4 tot 6 dagen werk). Codegeist kan, maar de kans is kleiner dan B dacht en het geld komt pas in april. Cloud9 alleen als Thijs een melding van Junie (een AI-hulp van JetBrains) in de tekst goed vindt; anders overslaan. De andere hackathons in de Devpost-API passen slechter (zie onderaan).

---

## 1. Reddit's Game of the Day (deadline di 8 dec 2026, 18:00 Pacific = wo 9 dec 03:00 NL)

Regels: https://redditgameofday2026.devpost.com/rules, overzicht: https://redditgameofday2026.devpost.com/

**Prijzen (GEZIEN, rules deel 8):** Best Daily Game $15.000 (1x), **Best Ported Daily Game $6.000 (1x)**, Honorable Mentions $1.000 (10x), Devvit Helpers $500 (6x, voor helpen in Discord en r/devvit), Feedback Award $200 (5x, voor een ingevuld feedbackformulier). "A project can only win one (1) prize."

| Vraag | Antwoord uit de regels (GEZIEN) |
|---|---|
| Bedrijf uit Nederland? | Ja. Open voor "Organizations ... that exist and have been organized or incorporated at the time of entry", met één "Representative". Uitgesloten zijn alleen landen met een verbod (genoemd: Brazil, Quebec, Russia, Crimea, Cuba, Iran, North Korea, Syria, OFAC-landen). Nederland staat er niet bij. Let op: Dortus is een eenmanszaak (`besluiten.md`, Steamworks-regel), geen aparte rechtspersoon; Thijs schrijft zich dus in als persoon of als "Organization" met zichzelf als vertegenwoordiger. Het geld komt in beide gevallen bij hem. |
| Bestaand of overgezet spel? | Ja. "if the Entrant's Project existed prior to the Hackathon Submission Period, must have significantly updated after the start". De categorie ported is er speciaal voor: "leverages a developer's existing IP or is ported from another platform. Note you must own the original app/IP to qualify ... Make sure to note your game is a port". Uitgesloten: spellen die eerder een Reddit-hackathon wonnen. |
| AI gebruiken? Melden? | Mag, en **hoeft niet gemeld te worden**. Niets in de rules over AI. Op de overzichtspagina: "Did you use AI? Fantastic! But it shouldn't be obvious the moment we open your app ... You can even ask your agentic assistant to help hide their involvement!" De Devvit-regels over AI gaan alleen over een taalmodel ín de app (https://developers.reddit.com/docs/devvit_rules, "Generative AI/LLM rules"), niet over hoe je bouwde. Of het inzendformulier op Devpost een AI-vraag heeft, is ONBEKEND (alleen zichtbaar na inloggen). |
| Rechten | "all Submissions remain the intellectual property of the individuals or organizations that developed them". Reddit krijgt een "non-exclusive license" voor de hackathon, en mag naam en inzending 3 jaar gebruiken voor reclame (deel 10). |
| Inleveren | Spel op Devvit Web, tekst, **filmpje optioneel** (onder 1 minuut, op YouTube of Vimeo), link naar de app (developers.reddit.com/apps/{naam}), README.md in de app, link naar een openbare test-subreddit (onder 200 leden) met een post waarin het spel draait. Code openbaar is optioneel. Alles in het Engels. |
| Jury | Vier gelijke punten: Delightful UX, Polish ("The closer to launch quality, the higher the score"), Reddity (gemeenschap), Daily Content. Niet gewild: "AI Slop", Reddit-thema's op de neus, veelgeziene ideeën ("space shooters, clone apps of popular games, simple platformers"). |
| Betaling | Uitslag ±do 17 dec. Formulieren terug binnen 10 werkdagen; "Prizes will be delivered within 60 days" na ontvangst. Dus GOK: geld tussen eind december en half februari. Kosten van overmaken en wisselen zijn voor de winnaar. |
| Belasting | Winnaar betaalt zelf belasting in eigen land; buitenlanders vullen "W-8BEN" in; de organisator mag een deel inhouden voor Amerikaanse belasting. Of er echt tot 30% wordt ingehouden of het belastingverdrag NL-VS dat voorkomt: ONBEKEND; een draad op Hackaday laat beide meningen zien (DERDEN, https://hackaday.io/page/2172). In Nederland telt het GOK als winst van de eenmanszaak. |

**Wat is Devvit en kan Hat Tower erheen? (GEZIEN, https://developers.reddit.com/docs/capabilities/devvit-web/devvit_web_overview en /docs/quickstart)**
- Devvit Web is een gewone webapp (HTML, CSS, JavaScript of TypeScript, met Phaser, three.js of React) die in een Reddit-post draait, plus een kleine Node-server met Redis (opslag) en de Reddit-API. Beperkingen: geen verzoeken van de app naar buiten, verzoek max 30 s, opslag in de browser verdwijnt bij elke update (dus scores in Redis). Node 24.18 of nieuwer.
- Hat Tower is klein: de regels zitten in `Spel.mc` (163 regels) en het tekenen in `SpelView.mc` (320 regels), Monkey C op tak `claude/garmin-gloop-2026-11-16` (GEZIEN, `git show`). Eén knop, ronde van 30 seconden, tien hoeden, beste score. Dat is in TypeScript met canvas of Phaser na te bouwen; de plaatjes van Mila (kit tot 454 px) kunnen mee. Taal: Monkey C naar TypeScript, geen motor die meekomt.
- Het moet wel een **dagspel** worden. Voorstel: elke dag dezelfde reeks helden voor iedereen (vaste dagcode), een dagranglijst in Redis, een reeks dagen op rij, een uitslagkaart om als reactie te plaatsen, en de grap die het Reddity maakt: alle spelers stapelen samen op één gemeenschappelijke toren van die dag ("de toren van r/..."). Kale Hat Tower zonder dat valt onder "simple ... clone" en scoort laag op Daily Content en Reddity (GOK).
- Devvit-regel om te weten: "Apps should not link out to other apps, or promote other versions of the app on external platforms" (devvit_rules). In het spel dus geen link naar Garmin of Steam. De reclame voor Hats waar B op hoopte, zit alleen in de Devpost-pagina en het verhaal, niet in het spel.
- Getest in deze sessie (GEZIEN): npm geeft `devvit` 0.15.4, de server van Devvit is bereikbaar door onze proxy. Inloggen kan zonder scherm: `npx devvit login --copy-paste` (GEZIEN, /docs/guides/tools/devvit_cli). Een agent mag niet inloggen, dus Thijs doet die ene stap.

**Werk (GOK, met reden):** 4 tot 6 agentdagen. Spel nabouwen in TypeScript 1 dag (500 regels logica en tekenen, plaatjes bestaan), dagcode, Redis-ranglijst, reeks en uitslagkaart 1 tot 2 dagen, gemeenschapstoren en polish voor de telefoon 1 tot 2 dagen, README, filmpje van 50 seconden en keuring 0,5 tot 1 dag. Ruim op tijd voor 8 dec als we vrijdag 20 nov beginnen.

**Concurrentie (GEZIEN):** vorige editie (Reddit Daily Games, jan tot feb 2026): 525 inzendingen (galerij 21 pagina's van 24 plus 21, https://redditdailygames2026.devpost.com/project-gallery) op 2.974 aanmeldingen, 14 geldprijzen. Winnaars waren vooral nette puzzels en woordspellen (BridgeDit, Sneakle, SerpenTiles, Quipit, Fully Packed) plus een mini-golf en een schaakspel. Nu 1.748 aanmeldingen met nog 19 dagen (Devpost-API). De categorie ported is nieuw; hoeveel ports meedoen is ONBEKEND, GOK 30 tot 80.

**Kans en geld (GOK):** ported winnen 10 tot 20% (kleine groep, eigen spel met eigen figuur, wij poetsen goed), een eervolle vermelding 5 tot 10% extra, hoofdprijs ±1%. Verwacht ±$1.100, GOK ±€950. Bonus: Feedback Award ($200, 5x) is een kwartier werk voor een agent, verwacht klein.

**Thijs moet (uiterlijk):**
1. Devpost-account en "Join Hackathon" (daarmee accepteert hij de regels), ±10 min, **uiterlijk ma 23 nov**.
2. Een Reddit-account voor Dortus (niet zijn eigen; harde regel 4) en `devvit login --copy-paste` samen met een agent of de hoofdchat (link openen, code terugplakken), ±15 min, **uiterlijk ma 23 nov**. Reddit raadt aan niet te wachten: "don't wait until the last minute to get the game running on our systems".
3. Ja op de inzendtekst (gaat onder zijn naam), ±10 min, **uiterlijk ma 7 dec**. Het filmpje gaat op @Dortusapps na keuring door een ander (mag zonder zijn ja, regel 4).
4. Bij winst: formulieren (W-8BEN en verklaring) binnen 10 werkdagen, ±20 min.

---

## 2. Codegeist 2026, Atlassian (deadline di 22 dec 2026, 12:00 Pacific = 21:00 NL)

Regels: https://codegeist2026.devpost.com/rules

**Prijzen (GEZIEN):** per categorie (software, business, specialistische sectoren) $15.000, $8.000 en $5.000 (9 prijzen), plus 4 bonusprijzen van $1.500, elk 6x (Rovo-agents, Atlassian MCP, Teamwork Graph, gepubliceerd in de Marketplace). "The same Submission can win up to one Grand Prize and one Bonus Prize."

| Vraag | Antwoord (GEZIEN) |
|---|---|
| Bedrijf uit Nederland? | Ja, zelfde tekst als Reddit; uitgesloten o.a. Brazil, Quebec, Russia, Belarus, Sudan, Myanmar en sanctielijsten. |
| Bestaand product? | Mag: "if the Project existed prior ... must have been updated or rebuilt in the Forge platform after the start ... and must have a Forge manifest file and include at least one Forge module". |
| AI? Melden? | Niets over melden in de rules. AI zit juist in de opdracht (Rovo, agents, MCP). **Geen AI-melding nodig.** |
| Rechten | "All Submissions remain the intellectual property of the individuals or organizations that developed them"; Atlassian krijgt een licentie voor de jurering en mag naam en beeld 3 jaar gebruiken. Wel: "solely owned by the Entrant". |
| Inleveren | Forge-app met installatielink voor de jury, **filmpje verplicht** (onder 5 minuten, YouTube, de app werkend), tekst, uitleg hoe aan de techniek voldaan is, uitleg voor installeren. Engels. |
| Jury | Techniek ("not just a shallow wrapper or a single hardcoded demo path"), ontwerp, impact, idee, presentatie. |
| Betaling | Jurering 5 jan tot 3 feb, uitslag ±ma 15 feb 2027, daarna 10 werkdagen formulieren en "within 60 days". Geld GOK pas eind maart tot half april 2027. Belasting zoals bij Reddit. |

**Concurrentie (GEZIEN):** Codegeist 2024: 143 inzendingen (galerij 5 pagina's van 24 plus 23, https://codegeist.devpost.com/project-gallery) op 3.704 aanmeldingen. Nu 4.211 aanmeldingen met nog 33 dagen. **Nieuw feit tegenover B:** de winnaars van 2024 waren voor een flink deel bestaande Marketplace-makers met een af product (Apwide Booking, Integrate with AWS for Jira, Capable Images for Confluence, File Approvals for Jira). We spelen dus tegen bedrijven die Jira-apps als vak hebben.

**Werk (GOK):** 5 tot 8 agentdagen per app (Forge leren, bouwen, testen in een echte Jira, filmpje). Het lastige: zien en filmen kan alleen in een ingelogde Jira, en agents mogen niet inloggen. Filmen moet dus Thijs doen, of de hoofdchat met Chrome op de HP van Thijs. Dat kost Thijs meer tijd dan B schatte.

**Kans en geld (GOK):** GOK 170 tot 250 inzendingen. Per goede app: bonusprijs 8 tot 12%, hoofdprijs 2 tot 4%. Verwacht per app ±$430, twee apps ±$860, GOK ±€750. Atlassian staat bij ons op "gestopt" (6 nov); dat verandert hier niet, het gaat om prijzengeld.

**Thijs moet:** gratis Atlassian-ontwikkelaarsaccount en ontwikkelsite plus API-sleutel als GitHub-secret (±20 min, uiterlijk ma 30 nov), Devpost "Join" (±5 min), meekijken of filmen in Jira (±1 uur, rond 18 dec), ja op de tekst (uiterlijk ma 21 dec). Voor de bonus Marketplace: een verkopersaccount; GOK dat Dortus dat al heeft van de oude Atlassian-apps (staat bij Thijs).

---

## 3. Cloud9 x JetBrains: Sky's The Limit 2026 (deadline di 12 jan 2027, 11:00 Pacific = 20:00 NL)

Regels: https://cloud9.devpost.com/rules

**Prijzen (GEZIEN):** 3 categorieën (VALORANT-scouting, League of Legends-draft, **Event Mini Game**), elk $6.000 plus reis naar GDC voor de winnaar en $2.000 voor de tweede. Bonus "Best AI-Powered Workflow Story" $1.000.

| Vraag | Antwoord (GEZIEN) |
|---|---|
| Bedrijf uit Nederland? | Ja, zelfde tekst; uitgesloten Brazil, Quebec, Russia, Crimea, Cuba, Iran, North Korea, OFAC. |
| Bestaand of overgezet? | Mag: "significantly updated after the start ... for example with new features, a major redesign". Categorie 3: "build a mini game playable at a Cloud9 booth or event". Een knoppenspel als Hat Tower past daar precies. |
| AI? Melden? | Geen meldplicht voor AI als zodanig. Maar het project moet gebouwd zijn "using at least one JetBrains tool (a JetBrains IDE ... JetBrains Air, AI Coding Agent Junie)" en de tekst moet dat aantonen; jurypunt 1 is "How thoroughly and skillfully does the project use JetBrains tools?". Wij bouwen met Claude in de cloud. Eerlijk een JetBrains-hulpmiddel gebruiken kan in de praktijk alleen met **Junie CLI** (draait zonder scherm met een sleutel, GEZIEN https://junie.jetbrains.com/docs/junie-headless.html). Junie is een AI-hulp; die noemen in de tekst is dus feitelijk een AI-melding. **Volgens de wens van Thijs is dat een reden om over te slaan**, tenzij hij zegt dat "gebouwd met Junie" mag. De AI-verhaalprijs ($1.000) vraagt een AI-verhaal en valt sowieso af. |
| Rechten | "All Submissions remain the intellectual property of the Entrant". Maar: "The repository must be public and open source by including an open source license file". De code wordt dus open source. |
| Inleveren | Openbare repo met licentie, speelbare build of link, filmpje onder 3 minuten op YouTube, tekst, korte uitleg van de aanpak. |
| Jury | Ook: "automated AI-driven analysis" mag gebruikt worden bij de jurering. |
| Betaling | Uitslag ±ma 8 feb 2027, formulieren 10 werkdagen, "within 60 days". Geld GOK maart tot half april 2027. |

**Concurrentie (GEZIEN):** editie 2025: 179 inzendingen over 4 categorieën (galerij 7 pagina's van 24 plus 11, https://cloud9-25.devpost.com/project-gallery) op 2.260 aanmeldingen. Het eventspel won "JUNIE'S ARCADE" (gebouwd met WebStorm en Junie); een stapelspel "Ascend" ("Stack. Ascend. Compete!") won de prijs voor feedback. Nu 355 aanmeldingen, net open. Minispellen GOK 30 tot 60.

**Werk (GOK):** 2 tot 3 dagen bovenop de Reddit-versie (zelfde spel, beursversie voor groot scherm met wachtrij-ranglijst en demomodus), plus Junie echt laten meewerken.

**Kans en geld (GOK):** winnen 8 tot 15%, tweede 8 tot 12%. Verwacht ±$800, GOK ±€700. Geen kosten: elke deelnemer krijgt een All Products Pack-code en een AI Ultimate-code (GEZIEN, "while supplies last").

**Thijs moet:** zeggen of een Junie-melding mag (morgen), Devpost "Join" en de codes inwisselen in zijn JetBrains-account, Junie-sleutel als GitHub-secret (±20 min, uiterlijk ma 14 dec), ja op de tekst (uiterlijk ma 11 jan).

---

## 4. Andere hackathons uit de Devpost-API (GEZIEN 19 nov, `devpost.com/api/hackathons?status[]=open&challenge_type[]=online&order_by=prize-amount`)

Ik zocht er twee die beter passen. Die zijn er niet; wel één verleidelijke die afvalt op de AI-regel.

| Hackathon | Prijzen, deadline, aanmeldingen | Waarom niet (GEZIEN in de rules) |
|---|---|---|
| **PICO Space Program** (https://pico-space-program.devpost.com/) | $50.000 in 32 prijzen, 1 feb 2027, maar 63 aanmeldingen; bouwen met Claude Code en een emulator, categorie "Best Mobile App Port"; Nederland (EU) mag | Op papier de beste kans van allemaal. Maar: "If AI tools were used, the text description must list the AI tools and models used, and Sponsor may request prompt logs". **Verplichte AI-melding, dus overslaan.** Ook: Kotlin of Unity, en een Android-emulator in de cloud is zwaar. |
| QNX Global Hackathon (https://qnx.devpost.com/) | ±$50.000, 15 dec, 1.985 aanmeldingen | QNX is gratis alleen "for non-commercial use"; Dortus is een bedrijf (GOK botst). Inloggen nodig. Ver van wat wij maken. |
| AWS MSP AI Hackathon | $64.000, 11 dec | Alleen voor leden van het AWS Partner Network. Kan niet. |
| Open Agentic Web (Cognizant) | $10.000 in 3 prijzen, 11 jan, 1.216 aanmeldingen | Te weinig prijzen, alles open source. |
| Kiroween | $100.000, 4 dec, 16.473 aanmeldingen | Te druk; vraagt de Kiro-editor (zelf een AI-editor, dus melding). |

---

## Rangorde

Bedragen in dollars uit de regels; euro's GOK bij ±€0,86 per dollar. Kans en werk zijn GOK met de reden in het blok hierboven.

| # | Hackathon | Doen? | Verwachte euro's (GOK) | Kans op geld (GOK) | Werk (GOK) | Deadline | Eerste stap |
|---|---|---|---|---|---|---|---|
| 1 | **Reddit Game of the Day**, categorie ported, met Gloop's Hat Tower als dagspel | **Ja, morgen beginnen** | ±€950 (kans op €5.200 of €13.000) | ±15 tot 25% | 4 tot 6 agentdagen, Thijs ±35 min vooraf | di 8 dec (wo 9 dec 03:00 NL) | Thijs: Devpost "Join" en Reddit-account voor Dortus plus `devvit login --copy-paste` vóór ma 23 nov; hoofdchat zet één agent op de port |
| 2 | **Codegeist 2026** | Ja, maar alleen als er een agent vrij is na Reddit, en met één app in plaats van twee | ±€375 per app | ±10 tot 15% per app | 5 tot 8 agentdagen per app, Thijs ±1,5 uur (filmen in Jira) | di 22 dec (21:00 NL) | Thijs: Atlassian-ontwikkelaarsaccount, ontwikkelsite en API-sleutel; agent kiest een idee voor een bonusprijs (minder grote makers) |
| 3 | **Cloud9 x JetBrains**, Event Mini Game met dezelfde Hat Tower | Alleen als Thijs "gebouwd met Junie" in de tekst goed vindt; anders niet | ±€700 | ±15 tot 25% | 2 tot 3 dagen na de Reddit-versie | di 12 jan (20:00 NL) | Thijs: ja of nee op de Junie-melding |
| 4 | PICO Space Program | Nee (verplichte AI-melding) | ±€0 | | | 1 feb | niets |
| 5 | QNX, AWS MSP, Cognizant, Kiroween | Nee | ±€0 | | | | niets |

**Samen (GOK):** Reddit plus één Codegeist-app ±€1.300 verwacht, met ±25 tot 35% kans op minstens één prijs. Met Cloud9 erbij ±€2.000 en ±35 tot 45%. Dat is lager dan de €2.000 tot €6.000 van B, omdat ik per hackathon de echte prijsverdeling en de concurrentie van vorige keer telde. Het eerste geld komt GOK op zijn vroegst eind december (Reddit), de rest in maart en april 2027.

**Advies in één zin:** doe Reddit nu met Hat Tower als dagspel (laag werk, eigen spel, kleine categorie, geen AI-melding), en beslis over Codegeist en Cloud9 pas als de port af is.
