# C: korte video's en social (TikTok, Shorts, Reels, X, Bluesky)

Agent C, 18 nov 2026 ±20:30 NL, opdracht hoofdchat (BRIEF.md in deze map). Webpagina's gelezen met curl, eigen kanalen met de Metricool-koppeling (alleen lezen, niets veranderd). GEZIEN = zelf gemeten of gelezen, DERDEN = iemand anders zegt het (met link), GOK = niet nagekeken. De algemene keten (wachtrij, scorebord, sleutels) staat bij E (`E-automatiseren.md`); hier alleen wat voor video en social telt.

## 0. Wat al bekend is (niet overgedaan)
- Format: één tip per filmpje rond de vraag van de kijker wint van reclame en van "dag 12"-dagboeken (hoofdles 3, Joris, PrintPal, Blender Secrets, VAW.BE).
- Anderen maken het bereik: video's en lijstjes van andere makers, niet het eigen kanaal (hoofdles 4; Artinvader_, McGybeer, Rusty's Koreaanse video 907.965).
- TikTok: kleine accounts starten rond 325 views per filmpje, 2 van 9 hadden een uitschieter in hun eerste 30; YouTube Shorts haalt mediaan 2,85 keer zoveel als TikTok met hetzelfde filmpje (`lessen.md`, regels 76 en 80).
- Lengte geen knop, tips 20 tot 40 s; aantal filmpjes is de knop, niet het uur; 3 tot 7 hashtags; nooit stil plaatsen (verhalen 27, 28, 30, 31).
- Van filmpje naar klik: geen klikbare link op een Short of een TikTok met minder dan 1.000 volgers; de weg is de naam in beeld plus een zoekregel (verhaal 29).
- Hats: "Game is called X, wishlist it on Steam" werkt ook op kleine accounts (Cornerpond 17.800, Desktop Defender 25.100), Indie Game Joe is de eerste TikTok-route op de paginadag, op TikTok is de taal "sits at the bottom of your screen while you work" (`platformen/steam/marketing/makers.md`).
- Godot-clips (Movie Maker in `steam-hol-clips.yml`), Blender-renders, `maak.py` met json per filmpje en `geluid.py` bestaan al.

Hieronder gaat het verder waar dat ophoudt.

## 1. Eerst: wat er nu misgaat (GEZIEN 18 nov ±20:25 NL)

| Filmpje | TikTok @dortusstudio | YouTube @Dortusapps |
|---|---|---|
| 9 Ebb (17 nov 13:00) | 127 views, 1 like (tiktok.com, video 7709109994217671968). Metricool: gemiddeld **2 s gekeken van 11 s**, 100% uit Voor jou | 17 views (kanaalpagina) |
| 7 Click Joints dag 1 (17 nov 16:00) | **305 views, 5 likes** (video 7709157242309774625) | **niet geplaatst: status ERROR** "The request metadata specifies an invalid video description." |
| 2 Click Joints (do 19 nov 16:00) | ingepland | ingepland, **gaat ook mislukken** (zelfde fout, zie hieronder) |

**Oorzaak van de YouTube-fout (GEZIEN):** de beschrijving bevat `Edit > Preferences > Get Extensions`. YouTube staat in titel en beschrijving "all valid UTF-8 characters except < and >" toe (https://developers.google.com/youtube/v3/docs/videos, `snippet.description`). Ebb had geen `>` en ging wel door. **Actie hoofdchat, vóór do 19 nov 16:00 NL:** in Metricool bij filmpje 2 (YouTube) `>` vervangen door `→` of door komma's ("Edit, Preferences, Get Extensions"), en filmpje 7 op YouTube opnieuw inplannen met dezelfde vervanging. Voor alle volgende teksten: nooit `<` of `>` (een controle hierop hoort in de wachtrij, zie deel 3).

Wat dit betekent:
- **305 views op TikTok is precies de normale start** (mediaan 325 bij kleine accounts). Niet "mislukt", wel nog niets. Het doel van 1 dec (één filmpje boven 1.000) is haalbaar, maar alleen als er genoeg filmpjes echt uitgaan: tot nu toe staat er **1** op YouTube, de plek die volgens Joris 2,85 keer zoveel views geeft.
- **2 s van 11 s gekeken** (Ebb, Metricool): de eerste seconde houdt niemand vast. Bij Click Joints is dat nog niet gemeten (Metricool liep achter).
- **TikTok heeft nog steeds 1 volger** (GEZIEN). "screencuts.co" in Metricool is @dortusstudio (zelfde account, bio "Blender tips for 3D printing...").
- **@hatsofthefallen:** tiktok.com geeft statusCode 10221, meestal "account bestaat niet" (GOK); volgens `planning.md` is het oude account worththetrip.co nog niet omgezet.
- **Metricool Free: 20 geplaatste posts per maand, en hetzelfde filmpje op twee netwerken telt twee keer** (GEZIEN, https://help.metricool.com/main-differences-between-free-and-paid-plans-bl0v9.md). November past nog (3 geplaatst, ±16 nodig tot 30 nov). **In december is na 10 werkdagen op YouTube en TikTok de teller op.** Free heeft geen X; het goedkeursysteem (`createScheduledPostForReview`) zit pas in Advanced, € 43 tot 54 per maand (GEZIEN, https://metricool.com/pricing/). Op Free werkt die knop dus niet (GOK dat we Free hebben: 1 merk, gekoppeld 16 nov).

## 2. Wat werkt aantoonbaar (nieuw, met getal)

### Hoe lang het duurt en hoe vaak
- **Mortal Rite (indie RPG, 5 man):** 253 TikToks, **1 per 1,96 dagen**, 647.800 volgers, 126 miljoen views, **61.749 verlanglijsten**; "only about 1 in every 2,000+ people who view a video of ours will go and wishlist it" (DERDEN, eigen opgave in GameDiscoverCo: https://www.gamedeveloper.com/game-platforms/this-game-used-tiktok-to-get-120m-views-60k-steam-wishlists-). Beste soorten: voortgang ("eerst zag het er zo uit, nu zo", 8,5 miljoen), half af en om mening vragen, iets ingewikkelds simpel uitleggen, antwoord op een reactie. Gezicht en ondertitels hielpen.
- **DREADMOOR (horror):** "algorithms rarely reward you immediately"; maandenlang regelmatig posten, toen gingen meerdere filmpjes tegelijk op TikTok en Reels (±1 miljoen samen, +13.000 verlanglijsten in een week) **zonder nieuws erachter**; daarna pakten de platforms nieuwe filmpjes makkelijker op. Eén Reel ±300.000 views (DERDEN: https://gameworldobserver.com/2026/05/21/case-study-how-dreadmoor-reached-200000-wishlists-and-where-they-came-from).
- **The Hive (Fins, accounts van 0 tot 10 volgers):** korte clips op TikTok, Shorts, Instagram, Facebook, Bluesky, X en Imgur tegelijk; **10.000+ verlanglijsten in ±10 dagen**, samen met een update. Wat hielp: de fantasie meteen laten zien, één idee per post, "reposting similar hooks quickly when something started to work" (DERDEN, eigen devlog: https://skydome.itch.io/thehive/devlog/1164902/10000-wishlists-in-10-days-what-changed-for-the-hive).
- Les: **reken in tientallen filmpjes, niet in een week.** Ons doel van 14 dagen met ±10 filmpjes is kort, maar te halen op YouTube (27 van 34 Blender-kanalen had een uitschieter in de eerste 30 Shorts, Joris) als ze er ook echt op komen.

### Wat een view waard is (verlanglijsten of downloads per 1.000 views)
| Bron | Per 1.000 views | Label |
|---|---|---|
| Indie Game Joe op X, 8 spellen | mediaan **7,15** verlanglijsten (2,5 tot 21,2) | DERDEN, https://howtomarketagame.com/2026/05/07/2026-tips-for-making-your-tweets-go-viral/ |
| Indie Game Joe op TikTok, 7 kleine spellen | hooguit 2,3 Steam-volgers (bovengrens) | GEZIEN, `makers.md` |
| Mortal Rite, eigen TikTok | ±0,5 verlanglijst | DERDEN (zie boven) |
| Artinvader_ (gratis Blender-add-ons, TikTok 14.000 tot 27.000 views) | geen zichtbare golf downloads | GEZIEN, verhaal 29 |
Les: **voor een spel met Steampagina is een view iets waard, voor een gereedschap zonder klikbare link bijna niets.** Bij Click Joints moet een filmpje dus tot zoeken leiden (naam in beeld, "search Click Joints in Get Extensions").

### Per platform
- **X:** werkt via één groot account dat jouw spel laat zien (Joe: Retro Rewind 13,7 miljoen views, de eigen trailer van de makers 129 views; DERDEN, HTMAG). Rusty's Retirement: "I had a lot of success posting about the game on Twitter and Instagram Reels (which I then used to cross promote on TikTok)", 140.000 verlanglijsten bij de lancering (DERDEN, Jordan Morris in https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed). Vanaf nul met een eigen account is er geen bewijs: een AI-gestuurde maker op itch.io plaatste 299 keer op X, Bluesky en Mastodon samen en kreeg 14 volgers; 76% van zijn bezoekers kwam van Reddit (DERDEN, eigen opgave: https://itch.io/post/17238510).
- **Bluesky (GEZIEN, openbare API, 18 nov, 18 accounts in onze hoek):** kleine getallen. Ostend Games (Desktop Fishing) 1.695 volgers, mediaan 11,5 likes per post, beste 26. Kushiro (Grid Modeler, Blender) 1.034 volgers, mediaan 15; zijn beste post was **een tip**, "Useful function in blender: shear" (522 likes), zijn eigen add-on 86. OmniStep (Blender) 530 volgers, mediaan 11. Nieuwe add-on-accounts uit okt 2026 die elke dag een filmpje plaatsen (Mulk, Melo Marble): **0 tot 2 likes**, 3 tot 4 volgers. De maker van Rusty's plaatste één keer op Bluesky (758 volgers). Bureaubladspellen die net begonnen (Machikado Roastery, Mogu, Tama Pet, Cosmo Cat): 6 tot 22 volgers, mediaan 5 tot 10 likes.
- **Instagram Reels:** Rusty (zie X) en DREADMOOR (Reel ±300.000). Geen cijfers voor gereedschap gevonden (GOK dat het voor Click Joints iets doet).
- **TikTok en Shorts:** zie deel 0 en 1.

### Bureaubladspellen
- **Rusty's Retirement:** zie X en Reels hierboven; de haak "sits at the bottom of your screen" deed het werk, plus Twitch (streams vielen onder "Just Chatting"). DERDEN.
- **Desktop Fishing (Ostend Games, $3,49, 16 jun 2025):** Bluesky, TikTok en Discord in het persbericht (DERDEN, gamespress.com). Uitkomst klein: **607 leden in de Steamgroep**, ±350 reviews waarvan 120 in de eerste week en daarna 2 tot 11 per week (GEZIEN, memberslistxml en appreviewhistogram). Social alleen maakte geen motor.
- **Bongo Cat:** grootste TikToks van anderen en in andere talen (al bekend, `makers.md`). Geen les voor ons eigen account.

### Formats uit de opdracht, met wat we weten
| Format | Bewijs | Voor ons |
|---|---|---|
| Probleem in 3 seconden, dan de oplossing | Nikko "How to make X", PrintPal "printdelen verbinden" mediaan 40.000 (GEZIEN, Joris); Kushiro-tip 6x zijn productpost | **hoofdvorm Click Joints** |
| Voor en na | MIO3 UV 743K, Modeling Toolkit (`formats.md`, GEZIEN) | rood gewricht naar groen |
| "Ik maakte X" / voortgang | Mortal Rite 8,5 miljoen voortgangsfilmpje (DERDEN); dagboeken "dag 12" deden het slechtst (GEZIEN, Joris) | alleen als voortgang met beeld, niet als dagboek |
| Devlog | eigen dagboek zwakst bij Blender (Joris); bij spellen werkt het als het beeld verandert (Mortal Rite) | Hats: "eerst zo, nu zo" |
| Grappige fout | geen hard getal gevonden (GOK) | Hats: Gloop die iets doms doet, alleen als het echt gebeurt in een opname |
| Iets wat onverwacht beweegt in seconde 1 | ali3design vizier 44.200 (GEZIEN, Joris) | onze Ebb-cijfers (2 s gekeken) laten zien dat dit ontbreekt |

## 3. Per product: de 3 acties met de meeste kans

### Hats of the Fallen
1. **Eigen filmpjes pas echt vanaf de paginadag (±8 dec), en dan in de vorm die bewezen werkt:** 15 tot 30 s gameplay, eerste beeld de strook boven de taakbalk met iets wat beweegt, eindregel "It's called Hats of the Fallen. Wishlist it on Steam." Waarom: zonder pagina is een groot moment weg (viraal.md, les 4), en die vorm haalde 17.800 en 25.100 views op accounts van 132 volgers. Tot 8 dec: een voorraad van 15 clips laten renderen (Godot Movie Maker, al werkend), niet plaatsen.
2. **Indie Game Joe op de paginadag, op alle vijf zijn kanalen:** voor DREADMOOR gaf hij gratis "10,000 wishlists in the first day" (2,5 miljoen views over X, Facebook, Instagram, TikTok en YouTube, DERDEN) en op X mediaan 7,15 verlanglijsten per 1.000 views. Dit staat al als besluit; mijn toevoeging: vraag ook X en Instagram, niet alleen TikTok, en lever zijn vorm (één zin haak, drie streepjes, "Would you play this?").
3. **Geen tweede TikTok-account nodig vóór er bewijs is:** TikTok kiest kijkers per filmpje (verhaal 23). Plaats Hats-clips op @dortusstudio en @Dortusapps met het platform in de titel, of laat de hoofdchat ze via Chrome op tiktok.com uploaden naar @hatsofthefallen. Een tweede Metricool-merk kost Starter (€ 16 tot 20 per maand); alleen voorstellen als de clips na de paginadag boven 1.000 views komen.

### Click Joints (Free en Pro)
1. **YouTube weer laten werken en elke werkdag één tip op YouTube en TikTok** (fout in deel 1). Zonder dit telt het doel van 1 dec maar op de helft van de plekken, en net de slechtste.
2. **De eerste seconde ombouwen naar "probleem in 3 seconden":** begin met het gewricht dat vastloopt of rood kleurt, dan pas de oplossing en het groene gewricht. Tekst in beeld is de vraag van de kijker ("Ball joint jams after printing?"). Waarom: Ebb werd 2 s bekeken; tips met een vraag doen 1,12 tot 1,28 keer zo goed (verhaal 30), en de printhoek beloont "hoe verbind ik twee delen". Let op: geen belofte dat het klikt zolang er geen echte print is (besluit 17 nov).
3. **Accounts die gratis add-ons laten zien Click Joints Free laten tonen** (Artinvader_-soort, 2.100 tot 30.200 views per TikTok, Joris) en één echte print in een hand zodra Bram die heeft (de vorm met miljoenen views in de printhoek, `formats.md` 11 tot 14). Benaderen vraagt eerst een ja van Thijs op de tekst. Downloads komen van zoeken en van anderen, niet van onze 305 views.

### Bison & Flex
1. **Geen korte filmpjes op social:** voor een plugin voor een parsergenerator is er geen bewijs dat TikTok of Shorts iets doen, en het kanaal is Blender.
2. **Eén gewone YouTube-uitleg die een zoekvraag beantwoordt:** "Flex & Bison in CLion: highlighting, errors and run in 3 minutes". Er is vraag: "Flex & Bison Tutorial: Part 1" 120.448 views, Part 2 68.865, installatie 33.780 (GEZIEN, YouTube-zoekpagina 18 nov). Bison & Flex is gratis voor onderwijs, en dit publiek is studenten. Een uitlegvideo die een zoekvraag beantwoordt wint van reclame (hoofdles 3).
3. **Het filmpje uit `jetbrains-bison-flex-film.yml` in de listing** (staat al bij Chris als taak 2; geen extra werk van mij).

### Garmin (kort)
Ebb en Calm zijn geparkeerd: geen filmpjes meer (opdracht 17 nov). Gloop's Hat Tower alleen noemen in Hats-clips als hij live is, geen eigen filmpjes.

## 4. Wat te automatiseren is

**Kan vandaag volledig vanzelf (€ 0):**
| Stap | Hoe | Bestaat al |
|---|---|---|
| Beeld | Blender in Actions (`click-joints-render.yml`), Godot Movie Maker op een Windows-runner (`steam-hol-clips.yml`, 30 beelden per s) | ja |
| Monteren | `maak.py` met één json per filmpje (tekst, tijden, kader) en ffmpeg | ja |
| Geluid | `geluid.py`, zelf gemaakt, beeld bit voor bit gelijk | ja |
| Controle vóór inplannen | toets op lengte, 1080x1920, geluid aanwezig, tekst zonder `<` en `>`, YouTube-titel max 100 tekens, 3 tot 7 hashtags, geen "link in bio" | **nieuw**, klein stuk Python bij `geluid/toets.py` |
| Tekst | onderschrift en titel uit de json, skill `update-tekst` | ja |
| Inplannen | Metricool `createScheduledPost` door de hoofdchat met de release-URL | ja |
| Meten | Metricool `getAnalyticsDataByMetrics` (TikTok: views, gemiddelde kijktijd, Voor jou) plus de openbare tellers; elke maandag in het scorebord | **nieuw**, past in `scorebord.py` (E) |

**Een week als één pakket:** elke vrijdag 5 tips (json + mp4 + tekst) in één release. Bram zegt per tip "klopt", Daan keurt beeld, Thijs zegt één keer "week ja" in de wachtrij van E. Dat is het enige moment dat hij nodig is. (Let op: `planning.md` zegt sinds 16 nov 21:12 "Thijs beslist alleen nog over geld"; de BRIEF van vandaag vraagt zijn ja op tekst en beeld. De hoofdchat moet zeggen welke geldt.)

**Andere routes, voor als Metricool knelt:**
- **YouTube Data API direct:** uploaden kost 1 eenheid uit een bak van 100 per dag, en "Videos uploaded from unverified API projects are not restricted to private viewing mode" (GEZIEN, https://developers.google.com/youtube/v3/docs/videos/insert). Een workflow kan dus als **privé** uploaden met `publishAt`, en de hoofdchat zet hem pas na het ja op gepland. Telt niet mee voor de 20 van Metricool. Thijs één keer: Google Cloud-project en OAuth-toestemming voor @Dortusapps (±15 min), token als geheim.
- **TikTok Content Posting API: nee.** Zonder keuring alleen privé en het account moet privé staan, en "A utility tool to help upload contents to the account(s) you or your team manages" wordt niet goedgekeurd (GEZIEN, https://developers.tiktok.com/doc/content-sharing-guidelines). TikTok blijft via Metricool of Chrome.
- **Bluesky:** zit in Metricool Free, maar telt mee voor de 20. Eigen API is gratis. Zie deel 5: nu niet.

**Wat een mens moet blijven doen:**
1. Ja zeggen op het weekpakket (Thijs of, als dat geldt, Daan).
2. **Reageren op reacties in het eerste uur** (Mortal Rite maakte er hele filmpjes van). Agents mogen niet zelf onder zijn naam praten; de hoofdchat kan concepten klaarzetten.
3. Makers benaderen (Joe, add-on-accounts): tekst door Thijs goedgekeurd, versturen door de hoofdchat.
4. **Echte dingen filmen die geen render kan:** een geprinte figuur in een hand. Optioneel en het sterkst van alles: de stem of hand van Thijs (VAW.BE groeide met zijn eigen stem, VibeDesk zonder gezicht bleef plat; Mortal Rite: gezicht en ondertitels). Niet vragen tenzij het doel van 1 dec gehaald is; nooit een AI-stem of nep-persoon.
5. Kiezen welke tip na een uitschieter herhaald wordt (The Hive en Joris: na een uitschieter snel dezelfde haak opnieuw).

## 5. Wat niet werkt of te duur is
- **Stil plaatsen** (al gedaan, al opgelost) en **"link in bio"** zonder link.
- **`<` of `>` in een YouTube-tekst:** de upload mislukt zonder dat iemand het ziet.
- **Eigen X- of Bluesky-account vanaf nul als motor:** 299 posts gaven 14 volgers (itch.io), nieuwe Blender-accounts op Bluesky halen 0 tot 2 likes. Hooguit later hetzelfde bestand erbij zetten als het niets kost.
- **Metricool Advanced (€ 43 tot 54 per maand) voor het goedkeursysteem:** een regel in de wachtrij doet hetzelfde voor € 0.
- **Metricool Starter (€ 16 tot 20 per maand) nu:** pas voorstellen als het doel van 1 dec gehaald is. Dan is het de goedkoopste manier om in december elke dag op YouTube en TikTok (plus eventueel Reels en het Hats-account) te blijven. Verwachte opbrengst onbekend (GOK); zonder bewijs geen geld.
- **TikTok-API zelf koppelen:** wordt niet goedgekeurd voor eigen accounts (deel 4).
- **Drie bijna gelijke clips per dag:** een printwinkel zakte van ±300 naar 7,5 views en stopte (Joris, verhaal over paren). Eén nieuwe tip per dag.
- **Een Hats-filmpje met de haak vóór de Steampagina:** het moment is dan weg (viraal.md, les 4).
- **Social alleen voor een bureaubladspel:** Desktop Fishing deed Bluesky, TikTok en Discord en bleef op 607 groepsleden.

## Bronnen (allemaal met curl gelezen op 18 nov, behalve waar "Metricool" staat)
- Eigen kanalen: Metricool (`getScheduledPosts`, `getAnalyticsDataByMetrics`), tiktok.com/@dortusstudio en de twee videopagina's, youtube.com/@Dortusapps/shorts.
- YouTube API: https://developers.google.com/youtube/v3/docs/videos , https://developers.google.com/youtube/v3/docs/videos/insert , https://developers.google.com/youtube/v3/docs/errors
- TikTok API: https://developers.tiktok.com/doc/content-sharing-guidelines
- Metricool: https://metricool.com/pricing/ , https://help.metricool.com/main-differences-between-free-and-paid-plans-bl0v9.md
- Mortal Rite: https://www.gamedeveloper.com/game-platforms/this-game-used-tiktok-to-get-120m-views-60k-steam-wishlists-
- DREADMOOR: https://gameworldobserver.com/2026/05/21/case-study-how-dreadmoor-reached-200000-wishlists-and-where-they-came-from
- The Hive: https://skydome.itch.io/thehive/devlog/1164902/10000-wishlists-in-10-days-what-changed-for-the-hive
- Indie Game Joe op X: https://howtomarketagame.com/2026/05/07/2026-tips-for-making-your-tweets-go-viral/
- Rusty's Retirement: https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed
- itch.io-maker, 299 posts: https://itch.io/post/17238510
- Desktop Fishing: https://www.gamespress.com/Desktop-Fishing-Gets-Official-Release-Date-Big-Demo-Update-Out-Now , Steam memberslistxml en appreviewhistogram voor app 3411730
- Bluesky: public.api.bsky.app (getProfile, getAuthorFeed, searchActors), meetscript was een kort Python-stuk zonder opslag.
- Bison en Flex: youtube.com/results?search_query=flex+bison+tutorial en bison+flex+clion
