# Voorstel: dortus.com ombouwen naar apps en spellen voor gewone gebruikers

Onderzoek en voorstel, 12 en 13 november 2026. Alleen gelezen, niets gebouwd of gepubliceerd. Alle pagina's gelezen met `curl` op 12 nov 2026 (leesdatum hieronder steeds "12 nov") tenzij anders vermeld. GEZIEN = zelf gelezen; AFGELEID = volgt uit wat ik zag; GOK = inschatting zonder bewijs.

## Samenvatting (tien regels)

1. De voorpagina van dortus.com gaat nu helemaal over Mermaid en LaTeX voor Confluence; 60 van de 74 adressen in de sitemap zijn Atlassian-pagina's. Ebb en het spel komen nergens voor, ook niet in het privacybeleid.
2. **Dringend, los van de ombouw:** Garmin eist een eigen privacybeleid ("You cannot rely on Garmin's privacy policies"). Zet vóór of bij het indienen `dortus.com/ebb/privacy.html` neer. Dat mag nu al: een productmap valt binnen de huidige regels.
3. Kleine geslaagde makers houden hun site kaal: per product één tegel met beeld, één zin en een knop naar de winkel. Support, privacy en een perskit zitten in de voettekst. In de hoek van de bureaubladspellen is de Steam-pagina zelf de site.
4. De nieuwe opbouw: een voorpagina met Ebb en Hats of the Fallen (de Engelse naam van Het Hol), een pagina per product met eigen privacy en support, een perskit voor het spel en één pagina "For Atlassian users".
5. Atlassian: **naar een eigen hoek.** Elk bestaand adres blijft precies werken, want de Marketplace linkt naar `support.html`, `privacy.html#math` en zo verder. GitHub Pages kan niet doorverwijzen, dus verplaatsen of weghalen breekt links.
6. Vindbaarheid: op "breathing app Garmin" winnen de winkel en het Garmin-forum; daar komen wij realistisch niet boven. Wel haalbaar zijn "Ebb Garmin" en zoektermen per horloge ("breathing app fenix 8"). Gebruik altijd "Ebb for Garmin": er bestaat al een "Ebb"-ademapp voor de Apple Watch.
7. Stappen: nu de Ebb-map (privacy en support). Na goedkeuring door Garmin de Ebb-pagina met winkelknop en de nieuwe voorpagina. Zodra de Steam-pagina "binnenkort" live staat de spelpagina met verlanglijstknop en perskit. Echte foto's en de trailer volgen later.
8. Thijs koos op 12 nov 23:30 al voor de hele ombouw (`organisatie/besluiten.md`), met de eis dat niets online gaat voordat hij het concept heeft gezien. Hij moet nog beslissen: (1) of de regel "verander niets bestaands" in `regels.md` wordt aangepast; (2) of Atlassian naar een eigen hoek gaat; (3) welke producten er verder op de voorpagina staan, en onder welke naam het spel verschijnt.

---

## 1. De huidige site in het kort (GEZIEN, 12 nov)

**Techniek.** Statische HTML op GitHub Pages (`server: GitHub.com` in de kop van het antwoord van https://dortus.com; `CNAME` met `dortus.com` in de repo https://github.com/thijsduinhouwer2002-coder/dortus, alleen-lezen gekloond in /tmp). Eén `styles.css`, een eigen `home.css`, een klein `site.js` van 19 regels (alleen de rand van de kop bij scrollen), eigen lettertypes in `assets/fonts/`. Geen analytics-script gevonden (gezocht op plausible, gtag, googletagmanager, goatcounter, umami, cloudflareinsights: 0 treffers). Er zijn `sitemap.xml` (74 adressen), `robots.txt`, `llms.txt`, een eigen `404.html` en JSON-LD (Organization met e-mail support@dortus.com, WebSite). Taal Engels; vijf Duitse gidsen in `de/`.

**Voorpagina** (https://dortus.com, titel "Dortus: Mermaid and LaTeX editors for Confluence Cloud, running on Atlassian"), van boven naar beneden:
- Kop: Dortus, Apps, Guides, Support, knop "Get Mermaid Editor".
- Held: "Editors for Confluence Cloud. Write it as text, see it on the page." met twee knoppen naar de Marketplace, en twee live voorbeelden (Mermaid-code wordt een diagram, LaTeX wordt een formule).
- "The editors": twee kaarten (Mermaid Editor gratis; Math gratis tot 10 gebruikers), elk met vier punten en "Get it on the Marketplace".
- "Nothing leaves your Atlassian site" (Forge, geen eigen servers).
- "Who is behind Dortus": "Dortus is one developer, Thijs. He writes the code, tests every release and answers every support email himself."
- "Guides": ruim 50 gidsen over Mermaid, LaTeX, Markdown, e-mail in Jira en JSM, Q&A, opslag.
- Voettekst: Apps, Guides, Company (Support, Security, Privacy policy, Terms of service, Email check, Shopify-check (NL)), support@dortus.com, de regel "Dortus is not affiliated with Atlassian".

**Toon.** Kort, feitelijk, eerlijk ("No invented roadmap", "No sales follow up"), persoonlijk (één maker die zelf antwoordt). Die toon past ook bij Ebb. De inhoud past er niet bij: alles gaat over Confluence.

**Andere pagina's (GEZIEN):**
- `atlassian.html` heet "All Dortus apps", maar toont alleen Atlassian-apps: de twee editors, daaronder "Other apps" (MailView voor Jira en Confluence, AskSpace, Live Countdown, Mermaid Live Preview for Jira, Email check). Deze pagina is al een kant-en-klare "Atlassian-hoek".
- `support.html`: "One inbox. Answered by the person who wrote the code.", support@dortus.com, eerste antwoord binnen één werkdag, per app een lijst wat je meestuurt, veelgestelde vragen. Alleen Atlassian.
- `privacy.html` (bijgewerkt 2 nov 2026): hoofdstukken per Atlassian-app met ankers (`#mermaid`, `#math`, `#countdown`, `#mermaid-jira`, `#mailview`, `#askspace`, `#plantuml`, `#markdown`), plus hoofdstuk 14 over Arrears voor Shopify. **Ebb, Rollwright, Bison & Flex, Click Joints en het spel staan er niet in.**
- `terms.html`: algemene voorwaarden voor de Atlassian-apps, plus hoofdstuk 14 over Arrears.
- `security.html`, `partners.html` (MailView voor Solution Partners), `email-check.html`, `webshop/` ("Winkelklaar", Nederlandse Shopify-check), `klopt/` (Nederlands, TikTok Shop en Moneybird).
- Productmappen van de ploeg: `rollwright/` (Obsidian), `bison-flex/` (JetBrains), `click-joints/` (Blender). Ze volgen de huisstijl: eigen kop met Features, Privacy, Support, een installatieknop, support op thijs@dortus.com. Geen `ebb/` en niets over het spel: https://dortus.com/ebb/ geeft 404.

**Links vanuit de Atlassian Marketplace (GEZIEN via de openbare API, https://marketplace.atlassian.com/rest/2/addons/<key>, 12 nov):**
| App | Privacylink | Supportlink | Documentatie |
|---|---|---|---|
| Math for Confluence | dortus.com/privacy.html#math | dortus.com/support.html | dortus.com/math.html#docs |
| Mermaid Live Preview for Jira (2 gebruikers) | dortus.com/privacy.html#mermaid-jira | dortus.com/support.html | dortus.com/mermaid-jira.html#docs |
| Live Countdown for Confluence (14 gebruikers) | dortus.com/privacy.html#countdown | dortus.com/support.html | dortus.com/countdown.html#docs |
| Mermaid Editor for Confluence | niet te lezen (de API gaf een pagina "Human Verification") | idem | de voorpagina linkt naar dortus.com/mermaid.html |

Bij het zoeken op "dortus" gaf de API vier apps terug. MailView en AskSpace kwamen niet terug; GOK: niet meer openbaar te vinden. Hun pagina's op de site blijven toch nodig voor wie ze nog gebruikt.

**Tegenstrijdigheid om op te lossen:** de site noemt overal support@dortus.com, terwijl `organisatie/regels.md` voor nieuw werk thijs@dortus.com voorschrijft (sinds 7 nov).

---

## 2. Voorbeelden: hoe kleine makers het doen

Alle sites gelezen met curl op 12 nov 2026.

| # | Maker en link | Voorpagina | Meerdere producten | Naar de winkel | Support, privacy, pers | Uitstraling |
|---|---|---|---|---|---|---|
| 1 | **Panic**, https://panic.com | Titel "We code apps, publish games, and make Playdate." Bovenaan een draaiende rij uitgelichte titels, dan twee blokken met elk een eigen zin: "Panic codes Mac apps for developers." en "Panic publishes amazing video games." | Per product een tegel met beeld, naam, één zin en een regel met de platforms ("Available now for Steam, Switch, Itch.io, and Mac App Store") plus "Buy Now". Apps en spellen staan apart. | Eén knop per product, die naar een eigen productpagina gaat. | Privacy in de voettekst (`/privacy/`). | Groot beeld per product, weinig tekst. Elke tegel heeft de kleur van het product. |
| 2 | **inkle**, https://www.inklestudios.com | Bovenaan meteen "The inkle newsletter: Very infrequent! Sign up", daarna een tegel per spel met een citaat of één zin. | Lange rij tegels, nieuwste eerst, ook oude werken. | Via de spelpagina. | Een aparte perskit (`/press`) met per spel een eigen perspagina (`/press/80days`, `/press/heavensvault` en zo verder), logo's in zwart en wit, korte geschiedenis, oprichters, prijzen. Contact per e-mail. Discord. | Rustig, het beeld van elk spel draagt de pagina. |
| 3 | **Lucas Pope**, https://dukope.com | "Games by Lucas Pope". Per spel een blok met een paar zinnen verhaal, "Full version available from ...", "Game Homepage" en "Development Log". | Eén lange pagina, nieuwste spel bovenaan. | Elk spel heeft een eigen domein (obradinn.com) met de winkelknoppen. | Op obradinn.com: knoppen per winkel (Steam, Nintendo), "Support" (naar een Zendesk), "media @ this domain", "Request a Review Code", lijst van talen. | Elke pagina in de stijl van het spel. De makerspagina is bijna kaal. |
| 4 | **Bippinbits** (2 man, Dome Keeper), https://bippinbits.com | "Hi there! We are Bippinbits, an independent game developer from germany." en één zin over hun doel ("without sacrificing gameplay for profit"). | "Our Games": vier tegels met een beeld. Daaronder jamgames op itch.io. | Via de tegels (beeld, zonder tekstknop). | Contact (één e-mailadres), Imprint, Privacy Policy, Discord. Geen perskit op de site. | Heel kaal: drie alinea's en tegels. De pagina is 3,6 KB. |
| 5 | **Balatro** (één maker, uitgever Playstack), https://www.playbalatro.com | Een pagina voor één spel. | Niet van toepassing. | Een rij winkelknoppen: Steam (met `?utm_source=website`), Nintendo, Apple, Google Play. | `/support/`, `/press-kit/`, Discord. | Het spel zelf is de huisstijl. |
| 6 | **Mister Morris Games** (Rusty's Retirement, een van de grootste bureaubladspellen, $6,99), https://mistermorris.games | Een "plank" met spellen die je opent (heeft JavaScript nodig). Zonder JavaScript staat er alleen "You can find all my games on Steam". | Plank met doosjes. | Link naar de uitgeverspagina op Steam. | Alleen "About". Op Steam staan als support deze site en een e-mailadres (Steam appdetails, https://store.steampowered.com/api/appdetails?appids=2666510). | Speels, maar zonder inhoud voor zoekmachines. |
| 7 | **Conradical Games** (Desktop Defender, 1.789 reviews volgens `platformen/steam/idee.md`), https://conradicalgames.com | "Welcome to Conradical Games!", één zin, "Our Games", "Our Partners", contact per e-mail. | Tegels met beeld. | Via de tegels. | Alleen e-mail en sociale media. Op Steam is het veld website leeg. | Kaal. |
| 8 | **moczan** (Ropuka's Idle Island), https://moczan.com | "video games and stuff", gevolgd door een gewone lijst van alle spellen met jaar, jam en techniek. | Lijst. | Niet. | Niets. Steam: alleen een supportadres. | Een pagina van 2,4 KB met simple.css. |
| 9 | **dynamicWatch** (dwMap, Garmin), https://dynamic.watch | Titel met de zoekwoorden ("dwMap routeCourse for Garmin GPS watch and Edge"). Kop "Don't get lost on your ride, run or hike!", dan vier Connect IQ-apps met elk één alinea. | Per app een alinea met "Learn more", een link naar de Connect IQ-winkel en een link "full list" van ondersteunde horloges. | Directe links naar `apps.garmin.com/en-US/apps/<id>` en naar hun ontwikkelaarspagina in de winkel. | Help via Zendesk, waar ook de lijsten van horloges staan. Privacy op `/help/privacy`. Zeven talen. | Functioneel, gericht op sporters. |
| 10 | **FMP** (Fatigue Monitor, Garmin), https://fmp.it.com/en/ | "Products": per product een kaart met een zin, status ("Available" of "In Development") en platform ("Garmin Connect IQ", "iOS / Android"). | Kaarten met status en platform. | Via de productpagina. | Voettekst: About, Terms of Service, Privacy Policy, Commercial Disclosure. Engels en Japans. Gebouwd met Hugo. | Rustig, sjabloonachtig. |
| 11 | **SIGN** (vier Garmin-apps, één maker), https://forums.garmin.com/developer/connect-iq/f/showcase/444450/ | Geen eigen site. Eén bericht in de Showcase van het Garmin-forum met per app een zin en een winkellink. | Lijst. | Directe winkellinks. | Niets. | Niet van toepassing. |

Ook gezien, voor de hoek van de bureaubladspellen (Steam appdetails, 12 nov): Desktop Defender, Ropuka's Idle Island, Bongo Cat, Dungeon Architect: Idle, Grave Ambition en The Throne Below hebben **geen** website ingevuld op Steam, alleen een supportadres. Tiny Pasture verwijst naar een Linktree.

**Wat de beste gemeen hebben (AFGELEID uit de tabel):**
1. **Per product één tegel:** beeld, naam, één zin over wat het is, op welk platform, één knop. Geen lange uitleg op de voorpagina (Panic, inkle, Bippinbits, FMP).
2. **Het platform staat erbij** ("For Playdate, Steam ...", "Garmin Connect IQ"), zodat een bezoeker meteen ziet of het voor hem is.
3. **Een productpagina met de winkelknop zo hoog mogelijk**, en voor een horloge-app een lijst van horloges (dwMap).
4. **Support, privacy en pers in de voettekst**, één e-mailadres, geen ticketportaal nodig voor een kleine maker (Bippinbits, inkle, FMP).
5. **Perskit per spel** (inkle, Balatro), niet per app.
6. **Weinig techniek:** statische pagina's, snel, geen inlog (Bippinbits 3,6 KB, moczan 2,4 KB, FMP Hugo). Dat past bij wat dortus.com al is.
7. **Het product bepaalt de uitstraling, de maker blijft op de achtergrond.** De makerspagina is neutraal, de productpagina heeft de kleuren van het product (Panic, Lucas Pope).
8. In de hoek van de bureaubladspellen doet **de Steam-pagina het werk**. Een eigen site is daar een extra en geen voorwaarde. Voor ons is die vooral nuttig voor de perskit, de verlanglijstknop met UTM-meting en de link vanuit de Ebb-hoek.

---

## 3. Wat eisen Garmin en Valve (GEZIEN, 12 nov)

**Garmin, App Review Guidelines** (https://developer.garmin.com/connect-iq/articles/app-review-guidelines/Overview.html, "Last Updated: Oct 13th, 2021"):
- Privacy: "Publish and make available your own privacy policy or other notice concerning your processing of personal data and how users may contact you to exercise any of their privacy rights. You cannot rely on Garmin's privacy policies." Ebb verzamelt niets, maar een korte eigen verklaring is dus nodig. Die staat nu nergens op dortus.com.
- Support: "You should clearly explain to users your support policy and availability. It is your responsibility to follow through on whatever support commitments you make."
- Betalen: "Inform users of your refund policy or lack thereof."
- Eerlijk, **ook buiten de winkel**: "This also applies to any other advertising you for your app, whether or not on a Garmin digital property". Je moet ook je contactgegevens actueel houden en mag geen samenwerking met Garmin suggereren. Elke zin op de Ebb-pagina valt dus onder dezelfde keuring als de winkeltekst.
- Verboden: apps "designed to be used during dangerous activities such as scuba diving, free diving". En medisch: wie claimt te helpen bij "diagnosis, cure, mitigation, treatment or prevention of disease" moet een toelating kunnen laten zien. Daarom ook op de site geen duikwoorden en geen gezondheidsbeloftes.

**Garmin, Connect IQ Brand Guidelines** (https://developer.garmin.com/brand-guidelines/connect-iq/): "The badge can be used to promote apps that are compatible and available on the Connect IQ store app and website." Er is een donkere en een lichte badge in https://developer.garmin.com/downloads/connect-iq/brand-assets_2024.zip, met de regel "Please do not alter any Connect IQ brand images." Verder is een "Hero Image" van 1440 x 720 px mogelijk in de winkel; die kunnen we ook op de site gebruiken.

**Valve, Steamworks:**
- Coming Soon (https://partner.steamgames.com/doc/store/coming_soon): "For new products, you must have a Coming Soon page up for at least two weeks before releasing." Nodig: "a set of branding images, written description, and ideally a gameplay trailer."
- Widget en meting (https://partner.steamgames.com/doc/marketing/utm_analytics): een link als `https://store.steampowered.com/app/<appid>?utm_source=...&utm_medium=web` wordt in Steamworks geteld, ook verlanglijstjes en aankopen. Hetzelfde werkt in de widget: `<iframe src="https://store.steampowered.com/widget/<appid>/?utm_source=mywebsite...">`.
- Merk (https://partner.steamgames.com/doc/marketing/branding): het Steam-logo mag niet suggereren dat Valve ons steunt, mag niet "primary or prominent" zijn en moet los staan. Bij gebruik moet de regel "Steam and the Steam logo are trademarks and/or registered trademarks of Valve Corporation in the U.S. and/or other countries." erbij.
- Fest (https://partner.steamgames.com/doc/marketing/upcoming_events/themed_sales/desktop_companion_2027): "January 14, 2027 @ 10:00am PST to January 18, 2027 @ 10:00am PST", met vakken voor "unreleased titles in Coming Soon mode, games with demos". Wanneer we zelf mogen melden dat we meedoen (8 januari met de asset kit), staat in `ontwerp/steam/winkelpagina/fest.md` (Sanne, GEZIEN 9 nov). Dat heb ik niet opnieuw nagelezen.
- Een eis van Valve voor een eigen privacybeleid of website heb ik **niet** gevonden (niet uitgebreid gezocht). GOK: niet verplicht zolang het spel niets verzamelt, maar wel netjes, en goedkoop om te maken.

**Atlassian** (https://developer.atlassian.com/platform/marketplace/app-approval-guidelines/ en .../prepare-branding-support-privacy-and-security/): vraagt "Create a privacy policy", "Publish a privacy policy with data handling details" en "Support infrastructure set up with defined channels and SLAs". AFGELEID: als de privacy- en supportlinks van een openbare app kapotgaan, schiet die app tekort tegenover de Marketplace.

---

## 4. Voorstel: de nieuwe opbouw

### Uitgangspunten
- Eén merk, Dortus, als neutrale maker. Elk product heeft een eigen map en een eigen gezicht, zoals bij Panic. Dat sluit aan op de bestaande regel "dortus.com/<productnaam>/".
- Alles Engels (de markt is wereldwijd; Garmin vertaalt de winkel, de site hoeft dat nog niet).
- Statisch, zonder cookies en zonder analytics. Dan klopt "we collect nothing" ook voor de site. Meten gebeurt met UTM-links naar Steam en met de cijfers van Garmin en Steam zelf.
- Elke zin op een productpagina komt letterlijk uit de goedgekeurde winkeltekst of is in de code nagelopen (stijlregel versie 28). Wat niet in de app zit, staat er niet.

### Pagina's
| Adres | Wat | Wanneer |
|---|---|---|
| `/` (index.html) | Nieuwe voorpagina | Na goedkeuring van Ebb en na het ja van Thijs op het concept (zie punt 7 en 8) |
| `/ebb/` | Productpagina Ebb | Nu al als "binnenkort", af na goedkeuring van Ebb |
| `/ebb/privacy.html` | Privacy voor Ebb | **Nu**, vóór of bij het indienen |
| `/ebb/support.html` (of een blok op `/ebb/`) | Support, terugbetalen, veelgestelde vragen | Nu |
| `/hats-of-the-fallen/` | Spelpagina met verlanglijstknop | Zodra de Steam-pagina "binnenkort" openbaar is |
| `/hats-of-the-fallen/press/` | Perskit | Tegelijk met de spelpagina, af vóór 8 jan |
| `/hats-of-the-fallen/privacy.html` | Privacy voor het spel | Tegelijk |
| `/atlassian.html` (bestaat al) | De hoek "For Atlassian users": de huidige inhoud van de voorpagina erbij | Tegelijk met de nieuwe voorpagina |
| Alle andere bestaande adressen | Blijven precies zoals ze zijn | Altijd |

### Voorpagina, van boven naar beneden (eerste concept, Engels)

**`<title>`**: `Dortus: Ebb, breathing exercises for Garmin watches, and small games for your desktop`
**meta description**: `Dortus makes small, honest apps and games: Ebb, breathing exercises for your Garmin watch, and Hats of the Fallen, a tiny dungeon on your taskbar. One price, no ads, no tracking.`

1. **Kop**: Dortus (woordmerk), rechts: Ebb, Hats of the Fallen, Support. Geen "Guides" meer in de hoofdmenu.
2. **Held** (kort, geen grote belofte):
   > **Small apps and games that keep you company.**
   > Made by one developer. One price, no ads, no tracking, and every email answered by the person who wrote the code.
3. **Tegel Ebb** (het grootste blok, beeld: `ontwerp/garmin/winkel-echt/0-poster-v5.png` of later een echte foto):
   > **Ebb** · Garmin watches
   > Breathing exercises on your wrist. Breath hold rounds and calm 4-7-8 breathing, followed by vibration with your eyes closed, while a small sea fills with animals as you keep coming back.
   > $4.99, one payment · 28 Garmin watches
   > [Get Ebb on the Connect IQ Store] (officiële badge)   [More about Ebb]
   (Vóór de goedkeuring: "Coming soon to the Connect IQ Store" zonder winkelknop.)
4. **Tegel Hats of the Fallen** (beeld: capsule of een GIF van de strook boven de taakbalk):
   > **Hats of the Fallen** · Steam, Windows
   > A tiny dungeon lives on top of your taskbar. Heroes climb in, fall into your traps and get eaten by Gloop, who wears their hats.
   > Coming to Steam. Wishlist it to hear when it is out.
   > [Wishlist on Steam]   [More about the game]
   (Deze zinnen komen uit de korte beschrijving in `ontwerp/steam/winkelpagina/teksten.md`, versie 2. Ze gaan pas online als die beschrijving gekeurd is en de Steam-pagina bestaat. Tot dan geen tegel, of alleen "In the works: a small game for your desktop, early 2027".)
5. **Andere dingen die we maakten** (klein, één regel per stuk, alleen als Thijs dat wil): Rollwright for Obsidian, Bison & Flex for JetBrains IDEs, Click Joints for Blender, elk met een link naar de eigen map.
6. **Hoe we werken** (drie korte punten, alleen wat voor elk genoemd product waar is):
   > **One price.** You pay once in the store. No subscription.
   > **Nothing collected.** Ebb keeps your sessions on your watch. This site has no cookies and no tracking.
   > **Answered by the developer.** Write to thijs@dortus.com. You get a reply from the person who made it.
   (Let op: "Nothing collected" voor het spel pas als Olaf bevestigt dat het spel niets verstuurt. Rollwright verkoopt via Polar, dus "one price" en "nothing collected" gelden daar anders. Daarom staan de punten hier alleen over Ebb en de site.)
7. **Voettekst**: Support · Privacy · Press (spel) · **For Atlassian users** (naar `/atlassian.html`, met de zin "Mermaid Editor, Math for Confluence, MailView and our other Atlassian apps keep working. Docs, support and privacy are here.") · thijs@dortus.com · de merkregels van Garmin en Valve, en de bestaande regel over Atlassian, alleen op de pagina waar dat merk staat.

### Ebb-pagina `/ebb/`, van boven naar beneden (eerste concept, Engels)

**`<title>`**: `Ebb for Garmin: breathing exercises, breath hold rounds and 4-7-8 on your watch`
**meta description**: `Ebb is a breathing app for Garmin watches. Breath hold rounds and calm 4-7-8 breathing, followed by vibration, while a small sea fills with animals. $4.99, one payment, no subscription. Fenix, Forerunner, Venu, vívoactive and epix.`
**h1**: `Ebb: breathing exercises for your Garmin watch`

1. **Held** (beeld rechts: poster v5; later een foto van het horloge om een pols):
   > # Ebb: breathing exercises for your Garmin watch
   > Breathwork rounds and calm 4-7-8 breathing on your Garmin. Follow every phase by vibration with your eyes closed, while a small sea fills with animals as you keep coming back.
   > [Get Ebb on the Connect IQ Store, $4.99] (badge)
   > One payment. No subscription, no extra account, no phone app. Works on 28 Garmin watches. [See the list]
2. **Hoe het werkt** (drie kaarten uit `ontwerp/garmin/winkel-echt/`: `1-breathe.png`, `2-hold.png`, `3-new-friend.png`):
   > **Breathe with the water.** Your round watch face becomes a porthole on a small sea. The water rises as you breathe in and falls as you breathe out.
   > **Hold, under water.** When you hold your breath you go under water with a sea animal. The picture stays the same however long you hold. Hold only while it feels easy.
   > **Make sea friends.** New animals join at the end of a session, earned by showing up, never by holding longer.
3. **Breath hold rounds**:
   > Rounds of deep breaths at a steady pace, then breathe out and hold for as long as feels right. Press a button to end the hold, then take one big breath in and hold it briefly to recover. From 3:00 the watch shows "breathe" at the top. A hold stops by itself after five minutes.
4. **Calm 4-7-8 and My pattern**:
   > Breathe in for 4, hold for 7, out for 8, with the sea rising and falling. Or set your own seconds in, hold, out and hold in the settings.
5. **Collect sea animals by showing up** (kaarten `4-sea-log.png`, `5-sea-complete.png`):
   > 24 sea animals, earned with sessions and weeks in a row. Your streak counts weeks in which you reach your weekly goal (3 sessions, or set 2 to 7), so rest days never break it. The Sea log shows exactly how to get the next one.
6. **Breathe with your eyes closed**:
   > Every phase has its own vibration. The last three breaths before the hold feel different. While you breathe and hold, the touchscreen does nothing, so a sleeve cannot stop a hold. Ebb makes no sound.
7. **Saved in Garmin Connect**:
   > Each session is saved as a breathing activity with your heart rate. In Rounds, every round is a lap with its hold time. For interest only; Ebb gives no score.
8. **Safety** (opvallend blok, letterlijk uit de winkeltekst):
   > For practice on land only. Sit or lie down. Never practise breath holds in or near water, in the bath, or while driving. Feel dizzy or tingly? Stop and breathe normally. Not if pregnant, under 18, or with epilepsy, heart or blood pressure problems. Ebb is not a medical device.
9. **Supported watches** (uit `manifest.xml` op tak `claude/garmin-2026-11-10b`, 28 stuks; de namen heb ik afgeleid van de apparaatcodes, AFGELEID, nalopen tegen de winkel):
   > fēnix 7, fēnix 7 Pro, fēnix 7X, fēnix 7X Pro · fēnix 8 43 mm, fēnix 8 47 mm, fēnix 8 Pro 47 mm, fēnix 8 Solar 47 mm, fēnix 8 Solar 51 mm · epix Pro (Gen 2) 42, 47 and 51 mm · Forerunner 165, 165 Music, 255, 265, 570 (42 and 47 mm), 955, 965, 970 · Venu 2, Venu 3, Venu 3S, Venu 4 (41 and 45 mm) · vívoactive 5, vívoactive 6.
   > The Connect IQ Store shows whether Ebb works on your exact model.
   (Deze lijst helpt bij het zoeken: mensen zoeken op hun horloge. De lijst moet altijd gelijk zijn aan het manifest; Garmin eist dat ook in de winkel.)
10. **Questions** (FAQ; elk antwoord staat in de winkeltekst of is na te lopen in de code):
    - *Do I need my phone?* No. Ebb runs on the watch; settings are on the watch. You need the Connect IQ app once to install it.
    - *Is it a subscription?* No. One payment in the Garmin store.
    - *Can I get a refund?* Refunds follow Garmin's Connect IQ Store policy: a 48-hour return window after you buy.
    - *Does Ebb collect data?* No. Your sessions, animals and settings stay on your watch. Only an activity you choose to save goes to Garmin Connect, under Garmin's privacy policy.
    - *What language is the app in?* English.
    - *Can I use it in water or while swimming?* No. Ebb is for practice on land only, sitting or lying down.
    - *Can I turn the vibration off?* Yes. One buzz stays on: every 30 seconds after 3:00 of holding, for your safety.
11. **Support**:
    > Mail thijs@dortus.com with your watch model. We aim to reply within 5 working days.
12. **Privacy** (kort, met link naar `/ebb/privacy.html`).
13. Voettekst als op de voorpagina, plus: "Garmin, Connect IQ, fēnix, Forerunner, Venu, vívoactive and epix are trademarks of Garmin Ltd. or its subsidiaries. Dortus is not affiliated with Garmin." (GOK over de precieze merkregel: de officiële formulering heb ik niet gevonden; nalopen in de brand-assets-zip.)

**Wat er niet op mag (eis):** de woorden freediving, apnea, diving en duikbeelden; Wim Hof; claims over stress, slaap, angst, bloeddruk, longinhoud of "better breathing"; "new best", records of iets wat langer inhouden beloont; sterren of reviews die niet echt zijn. Elke nieuwe zin gaat door dezelfde keuring als de winkeltekst.

**`/ebb/privacy.html`** (eerste concept, kort):
> **Ebb privacy policy.** Ebb is made by Dortus (contact: thijs@dortus.com). Ebb does not collect, send or sell any personal data. The app has no internet or phone permission. Your sessions, sea animals and settings are stored only on your watch. When you save a session, it goes to Garmin Connect as an activity, under Garmin's privacy policy; Dortus never sees it. If you email us, we use your email only to answer you and delete it when the question is closed [termijn: Thijs]. Questions or requests about your data: thijs@dortus.com. Last updated: [datum].
(De zin "no internet or phone permission" is nagelopen tegen het manifest volgens `winkeltekst.md`, Nagekeken versie 12. Opnieuw nalopen op de kandidaat-build.)

### Spelpagina `/hats-of-the-fallen/` vóór de lancering (opbouw, nog geen teksten)
1. Held: logo (`ontwerp/steam/winkelpagina/logo-1280.png`), de korte beschrijving, de **Steam-widget** met UTM (`?utm_source=dortus&utm_medium=web&utm_campaign=site`) en een gewone knop "Wishlist on Steam".
2. Trailer of een korte film (als die er is) en daarnaast drie of vier GIFs van de echte strook op ware hoogte. Laat eerlijk zien hoe dun de strook is (zie het punt van Daan in `platformen/steam/status.md`).
3. Drie blokken uit de lange beschrijving ("Gloop wears the hats", "Heroes hold grudges", "Glance, smile, get back to work"), alleen zinnen zonder [v1].
4. "Demo" zodra er een is. "Desktop Companion Fest, January 14 to 18" pas als we zijn uitgenodigd of aangemeld.
5. Systeemeisen (Windows), prijs pas als die vaststaat.
6. Optioneel: nieuwsbrief (besluit Thijs; zie punt 7). Zonder nieuwsbrief is de verlanglijst op Steam het enige "houd me op de hoogte". Dat is ook prima, want Steam mailt bij het uitbrengen (GOK over hoe goed dat werkt).
7. Links naar perskit, support en privacy.

**Perskit `/hats-of-the-fallen/press/`** (zoals inkle en Balatro): feitenlijstje (maker, platform, datum, prijs, talen), korte en lange beschrijving, 5 tot 8 schermen in volle maat, logo en capsules als download, trailer, "Request a key" via e-mail, één alinea over de maker. Geen persoonsgegevens behalve naam en e-mailadres.

### Uitstraling (wat nodig is, geen ontwerp)
- Een neutrale Dortus-laag (voorpagina, voettekst, support, privacy) en per product het eigen gezicht: bij Ebb de zee en de patrijspoort, bij het spel de pixelkunst. De huidige groene Atlassian-uitstraling (theme-color `#004c3f`, Forge-taal) hoort bij de Atlassian-hoek en hoeft niet terug op de voorpagina.
- Nodig van Daan of Mila: een woordmerk of teken voor Dortus dat bij consumentenproducten past (het huidige `dortus-mark.svg` kan misschien blijven), een kleur en een lettertype voor de neutrale laag, een tegelvorm voor producten en een `og:image` per pagina (1200 x 630).
- Echte beelden wegen het zwaarst: een foto van Ebb op een echte pols en een GIF van het spel op een echte taakbalk. Winkelkaarten zijn een goede start.
- Dark en light, snel op een telefoon (de meeste Garmin-bezoekers komen vanuit de Connect IQ-app of het forum op hun telefoon: GOK).

---

## 5. Wat er met Atlassian gebeurt

| Keuze | Wat | Risico |
|---|---|---|
| **1. Weg** | Atlassian-pagina's verwijderen | **Hoog.** De Marketplace linkt naar `privacy.html#math`, `#countdown`, `#mermaid-jira` en `support.html` (GEZIEN). Die links breken voor apps met echte gebruikers (Countdown 14, Mermaid for Jira 2, GEZIEN in de API), en Atlassian vraagt een gepubliceerd privacybeleid en support (GEZIEN). Bovendien vallen ruim 50 gidsen weg, en daarmee al het zoekverkeer dat de site nu heeft (hoeveel weten we niet: geen analytics). Het gaat ook in tegen `organisatie/doelen.md` ("De bestaande Atlassian-pagina's op de site blijven staan"). |
| **2. Eigen hoek (advies)** | Elk bestaand adres blijft byte voor byte gelijk. Alleen de voorpagina wordt nieuw. Wat er nu op de voorpagina staat, gaat naar `atlassian.html`, dat al "All Dortus apps" heet en alle Atlassian-apps toont (titel aanpassen naar "Dortus apps for Atlassian"). De voorpagina linkt in de voettekst naar "For Atlassian users". `privacy.html` en `support.html` blijven de Atlassian-pagina's, met bovenaan één regel: "Looking for Ebb or Hats of the Fallen? Each has its own privacy and support page." | **Laag.** Een Garmin-bezoeker die op een oude gidspagina belandt, ziet een Confluence-site; die pagina's hebben hun eigen kop met "Apps, Guides". Dat is te verhelpen met een kleine strook "Dortus now makes Ebb for Garmin" bovenaan, als Thijs dat wil (dat is wel een wijziging van bestaande bestanden). Voor zoekmachines blijft de site grotendeels over Confluence gaan, waardoor de Ebb-pagina iets minder gewicht krijgt (GOK, klein effect). |
| **3. Aparte pagina of eigen domein** (bijvoorbeeld atlassian.dortus.com) | Alle Atlassian-pagina's verhuizen | **Middel tot hoog.** GitHub Pages kan geen echte doorverwijzing (301) geven (AFGELEID: statische hosting, geen serverregels). Elke oude URL heeft dan een eigen doorverwijspagina met meta-refresh nodig, ankers als `#math` gaan daarbij makkelijk verloren, en het zoekverkeer van de gidsen begint opnieuw. Veel werk aan een deel waar de ploeg niets nieuws voor bouwt. |

**Advies: keuze 2.** Het kost het minst, breekt niets en past bij "de bestaande Atlassian-pagina's blijven staan". Concreet:
1. Niets hernoemen, niets verwijderen: geen enkel bestand uit de sitemap van vandaag.
2. `index.html` wordt de nieuwe voorpagina; de oude inhoud komt in `atlassian.html`.
3. `sitemap.xml`: nieuwe pagina's erbij, oude blijven staan. `llms.txt` en de JSON-LD op de voorpagina gaan over Dortus als geheel.
4. `404.html`: links naar Ebb en het spel erbij.
5. Supportadres: de Atlassian-pagina's houden support@dortus.com (dat staat in de listings en blijft dus werken, mits dat adres blijft aankomen). Nieuwe pagina's gebruiken thijs@dortus.com.

---

## 6. Vindbaarheid

**Wat ik zag (GEZIEN, 12 nov, WebSearch; dat is niet hetzelfde als Google):**
- Bij "breathing app Garmin watch" staan bovenaan showcase-berichten op het Garmin-forum (Breathing Timer, Breath Training System), blogs van Garmin zelf over de eigen ademfunctie, en handleidingen van Garmin.
- Bij "Ebb breathing app" staat bovenaan een iOS-app "Ebb - Evaluate. Breathe. Begin." voor de Apple Watch (https://apps.apple.com/us/app/-/id1183024708). **De naam Ebb is dus niet uniek in ademapps.**
- Pagina's in de Connect IQ-winkel hebben titel en beschrijving in de HTML (`og:title`, `og:description`, gezien bij https://apps.garmin.com/apps/ff485586-320b-4c73-87ee-4d2094541278). AFGELEID: Google kan ze lezen, dus onze eigen winkelpagina gaat waarschijnlijk boven dortus.com uit bij "Ebb Garmin".

**Wat realistisch is (GOK):**
- "breathing app Garmin" en "breathwork Garmin": daar winnen Garmin zelf, het forum en grote blogs. Wij staan er de eerste maanden hooguit op pagina 2 of 3. Geen tijd in steken.
- "Ebb Garmin", "Ebb breathing Garmin", "Ebb Connect IQ": haalbaar binnen een paar weken na het indexeren, samen met de winkelpagina. Zoekers op deze termen kennen de naam al (van het forum, Reddit of de winkel), dus de site werkt vooral als bevestiging en als plek voor support en privacy.
- Lange zoektermen per horloge of oefening: "breathing app fenix 8", "breath hold app Forerunner 965", "4-7-8 breathing Garmin", "box breathing Garmin". Weinig concurrentie (GOK) en precies de lezers die al een horloge hebben. Daarom de lijst van horloges als tekst op de pagina, en later misschien één eerlijke gids ("4-7-8 breathing on a Garmin watch: the built-in Breathwork activity and apps"), zoals de Atlassian-gidsen nu werken.

**Opbouw die helpt:**
1. Adres `dortus.com/ebb/`, een `<title>` en `h1` met "Ebb", "Garmin" en "breathing" (zie hierboven), `canonical`, `og:image`.
2. Overal "Ebb for Garmin", nooit alleen "Ebb".
3. JSON-LD `SoftwareApplication` met `name` "Ebb", `operatingSystem` "Garmin Connect IQ", `offers` 4.99 USD, `url` van de winkel. Geen `aggregateRating` tot er echte beoordelingen zijn (GOK dat dit helpt; het is wel de standaard).
4. Tekst als echte HTML (geen tekst in plaatjes), de lijst van horloges als tekst, de FAQ als tekst.
5. Links naar ons: de showcase-post op het Garmin-forum (die scoort zelf hoog, GEZIEN) en de verspreidingsplekken van Chris. De winkelpagina zelf heeft geen veld voor een website (GOK: niet gezien in het uploadformulier, `platformen/garmin/upload-en-keuringsregels-2026-11-11.md`).
6. Sitemap bijwerken, en Google Search Console als Thijs dat wil (inloggen kan alleen hij). Het bestand `99b51feeb51a9a81cb709b26637cf03d.txt` in de site-repo lijkt een verificatiesleutel (GOK; IndexNow of iets vergelijkbaars).

Voor het spel is de site bijna onbelangrijk voor vindbaarheid. Zoekers op Steam komen via tags en de fest-vakken binnen. De site is er voor de perskit en voor meting met UTM.

---

## 7. Volgorde in stappen

**Stap 0, nu (binnen de huidige regels, er verandert niets bestaands):**
- `ebb/privacy.html` en `ebb/support.html` (of `ebb/index.html` met die blokken) in de huisstijl van `rollwright/`. Reden: Garmin eist een eigen privacybeleid (GEZIEN) en dortus.com/privacy.html noemt Ebb niet (GEZIEN). Vraagt het uploadformulier om een privacy-URL, dan is die er. Wie: de website-maker van de ploeg (Gijs of Daan), niet dit onderzoek.
- `ebb/index.html` als korte pagina "Coming soon to the Connect IQ Store", zonder winkelknop.

**Stap 1, zodra Garmin Ebb goedkeurt (winkellink bekend):**
- De Ebb-pagina helemaal af, met badge en winkellink, en de blokken van punt 4.
- **Na het ja van Thijs op het concept (besluit 12 nov 23:30: niets online zonder dat hij het zag) en met de regel aangepast:** nieuwe `index.html`, oude inhoud naar `atlassian.html`, bijwerken van `sitemap.xml`, `llms.txt`, JSON-LD en `404.html`, en één regel bovenaan `privacy.html` en `support.html`. Alles in één commit, zodat terugdraaien makkelijk is.
- Forum-showcase en de plekken van Chris linken naar `dortus.com/ebb/`.

**Stap 2, zodra de Steam-pagina "binnenkort" openbaar is (gepland rond 1 tot 20 december, `fest.md`):**
- `hats-of-the-fallen/` met widget, UTM en verlanglijstknop; de perskit; privacy.
- Tegel op de voorpagina.

**Stap 3, rond 8 januari 2027:** de regel over het fest en de demo-link erbij, en de perskit compleet (trailer, key-aanvragen).

**Stap 4, als er betere beelden zijn:** echte foto van Ebb om een pols, een korte film, GIFs van het spel. Wissel de helden op beide pagina's. Een eventuele gids over 4-7-8 op Garmin pas als Ebb loopt en er tijd over is (geld gaat voor bereik).

---

## 8. Wat Thijs zelf moet beslissen of aanleveren

1. **De regel aanpassen voor de ombouw.** Thijs koos op 12 nov 23:30 voor de hele ombouw (keuze B in `organisatie/besluiten.md`), maar `organisatie/regels.md` zegt nog: "Verander of verwijder niets wat er al staat", ook `index.html` en `sitemap.xml`. De ombouw kan niet zonder die bestanden te wijzigen. Voorstel: toestemming voor `index.html`, `atlassian.html`, `sitemap.xml`, `llms.txt`, `404.html` en één regel bovenaan `privacy.html` en `support.html`. Al het andere blijft onaangeroerd.
2. **Atlassian: keuze 1, 2 of 3** (punt 5). Advies 2 (eigen hoek, niets breekt). Let op: dit is iets anders dan Thijs' keuze "B" van 12 nov 23:30 (de hele site ombouwen); die keuze ligt al vast.
3. **Wat staat er verder op de voorpagina?** Alleen Ebb en het spel, of ook Rollwright, Bison & Flex en Click Joints? En de Nederlandse producten (Klopt, Winkelklaar): die zou ik niet op de Engelse voorpagina zetten.
4. **Naam van het spel op de site.** Op Steam heet het **Hats of the Fallen** (`ontwerp/steam/winkelpagina/teksten.md`); "Het Hol" is de werknaam. Voorstel: overal Hats of the Fallen, adres `/hats-of-the-fallen/`.
5. **Supportadres.** Nieuw werk gebruikt thijs@dortus.com. Blijft support@dortus.com aankomen voor de Atlassian-gebruikers? Dat adres staat in de listings en op alle oude pagina's.
6. **Nieuwsbrief: ja of nee**, en zo ja via welke dienst. Een statische site heeft daar een externe dienst voor nodig, en dat moet dan in het privacybeleid. Advies: nee tot na de lancering van het spel; de Steam-verlanglijst doet hetzelfde.
7. **Meten: ja of nee.** Nu meet de site niets, wat goed past bij "no tracking". Advies: geen analytics, wel UTM-links naar Steam en eventueel Google Search Console (alleen Thijs kan inloggen).
8. **Aanleveren:** een foto van een Garmin-horloge om een pols met Ebb erop (als Thijs een van de 28 horloges heeft), een termijn voor het bewaren van supportmails voor het privacybeleid, en een akkoord op de over-tekst ("Made by one developer"; de naam Thijs staat al op de huidige site).
9. **Over-pagina**: hoeveel persoonlijk? Alleen voornaam en "one developer", zoals nu. Geen woonplaats of andere gegevens.

---

## Wat ik niet kon nagaan
- De listing van Mermaid Editor in de Marketplace-API (een pagina "Human Verification"), en daarmee welke links die app naar dortus.com heeft.
- Hoeveel bezoekers de Atlassian-gidsen nu krijgen (er is geen analytics; Search Console kan alleen Thijs zien).
- Of het uploadformulier van Garmin om een privacy- of website-URL vraagt (stap 2 van het formulier is nog niet gezien).
- Of Valve een eigen privacybeleid eist (niet gevonden, niet diep gezocht).
- De officiële merkregel van Garmin voor de voettekst (staat waarschijnlijk in de brand-assets-zip, die ik niet heb uitgepakt).
- Echte posities in Google: WebSearch is een andere zoekmachine dan Google.
- Of de namen van de horloges in punt 4 precies zo in de winkel staan (afgeleid van de apparaatcodes in het manifest).
