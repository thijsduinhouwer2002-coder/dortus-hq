# Logboek Abel (accountverzorger)

Alleen aanvullen, nooit weghalen.

## Run 1, 10 nov 2026 00:22 NL
- Gelezen: berichten/abel.md, regels, middelen, rol, besluiten (bovenste), plan van Mila (`ontwerp/steam/winkelpagina/plan.md` punt 2).
- `merk/maten.md` gemaakt, vroeg zoals de hoofdchat vroeg, zodat Mila vannacht de juiste maten heeft. Steam-maten uit de Steamworks-docs: logo 184 x 184 en kopachtergrond 1500 x 220 op de ontwikkelaarspagina, logo 1200 x 460 in de v2-editor. Blender: icoon 256, beeld 1920 x 1080 (uit de broncode van de site). GitHub social 1280 x 640.
- `inventaris.md`: alles openbaar bekeken. Grootste vondsten: (1) dortus.com gaat nog over Confluence, (2) GitHub heeft de standaardavatar, (3) JetBrains toont woonadres en telefoon van Thijs (EU-handelaarsregel), (4) Polar-pagina geeft 404.
- Besluit: ik maak zelf geen logo (bericht hoofdchat 00:16). Ik geef Mila wel mijn eis mee dat het Dortus-merk de maker is en geen spelfiguur, omdat hetzelfde beeld naast een parser-plugin voor programmeurs moet staan.
- Ik mag niet in berichten/mila.md schrijven (regels: alleen mijn eigen bestand). Mila kijkt volgens haar opdracht in `platformen/abel/merk/`; daar staat alles.
- `accounts/steam.md` versie 1: profiel dortusgames, groep Dortus, ontwikkelaarspagina (kop 184 en 1500 x 220, v2-editor), alle teksten om te plakken, waar klikken. Vrije namen gecontroleerd: /id/dortus, /groups/dortus en /developer/dortus zijn vrij (GEZIEN).
- Besluit: in het Steam-plan de AI-vraag van de Content Survey opgenomen, met een eerlijke voorgestelde tekst. Waarom: Valve eist het (DERDEN, doc contentsurvey) en r/ObsidianMD liet op 9 nov zien dat verzwegen AI tot een ban kan leiden. Regel op lijst-thijs als ter info.
- Open punt Steam: is dortusgames een beperkt account (minder dan $5 in de winkel)? Dan lukt de groep niet. Staat als controle in het plan.
- `merk/teksten.md`: kern, bio's kort en lang in Engels en Nederlands, toon. Besluit: in de lange bio één rustige zin dat Thijs met AI-hulp bouwt. Waarom: eerlijk, Valve vraagt het, en r/ObsidianMD liet zien dat ontdekt verzwijgen erger is dan vooraf zeggen. Thijs mag de zin schrappen, nooit het tegendeel.
- `accounts/jetbrains.md`: logo en kleine aanpassing beschrijving; ter info dat woonadres en telefoon openbaar staan (EU-handelaarsregel). `accounts/github.md`: profiel, repo-beschrijvingen en topics, pins zonder dortus-hq. `accounts/dortus-com.md`: hoofdpagina gaat over Confluence; vraag om ja op lijst-thijs (regels verbieden bestaande pagina's te wijzigen).
- Polar: polar.sh/dortus geeft 404, maar de afrekenpagina toont organisatie "Dortus", slug dortus, en een avatar die Polar automatisch van logo.dev haalt (GEZIEN in de afrekenpagina). Plan volgt in run 2.
- `accounts/blender.md` (avatar via Blender ID; nu het lege standaardplaatje, GEZIEN; listing niet aanraken tijdens de keuring), `accounts/polar.md` (eigen logo op de afrekenpagina, winkelpagina uit laten tot 3+ producten), `accounts/obsidian.md` (forumprofiel Thijs.Dortus: letter-avatar, About me met eerlijke AI-zin).
- Besluit: Polar-winkelpagina uit laten. Waarom: één product in een lege winkel wekt minder vertrouwen dan geen winkel; kopers komen via de plugin.
- `communities.md`: regels van Blender Artists, Godot-forum, forum.obsidian.md, JetBrains Platform-forum. Grote vondst: Blender Artists en Godot verbieden AI-geschreven antwoorden (DERDEN, links in het bestand), r/ObsidianMD ook.
- Besluit: geen antwoorden voor Thijs klaarschrijven op plekken die AI-tekst verbieden; elders alleen korte, geteste antwoorden die Thijs leest; eigen plekken eerst. Waarom: de rol zegt "nooit iets wat de regels van die plek breekt", en betrapt worden kost precies het vertrouwen dat we zoeken. Ter info op lijst-thijs.
- `dortus-com/index.html` eerste versie van de nieuwe hoofdpagina (drie productkaarten, wie maakt dit, link naar de oude Confluence-pagina's), met schermafbeeldingen desktop en telefoon, bekeken. Posters eerst bijgesneden aan de bovenkant; opgelost met 3:2 en contain.
- Volgende run: (1) kijken of Mila iets in `merk/` zette en de plannen daarop aanpassen; (2) Steam Online Conduct lezen; (3) eerste bijdrage op een eigen plek (issues rollwright of click-joints, forumdraad Rollwright); (4) `klaar.md` opzetten.
- `klaar.md` versie 0 opgezet (volgorde en stand per account).

## Run 2, 10 nov 2026 01:23 NL
- Gelezen: logboek, berichten, Mila's `merk/uniform.md` (deur-D op een kier) en keuring 1 van Daan. Alle beelden van Mila bekeken met Read.
- Proef gebouwd: de openbare Steam-pagina van Klei in de browser geladen en hun beelden vervangen door de onze (`merk/bron/mock*.js`). Gemeten hoe Steam toont: kop niet geschaald, gecentreerd, zijkanten eraf plus grijs verloop op de buitenste 15%; achtergrond bovenaan gecentreerd; logo op 1200 breed bovenaan.
- Vondst 1: in Mila's kop valt de deur op 1024 px weg. Besluit: v1b met haar eigen `kamer()` en de deur op x=950. Waarom: dan staat hij heel op 1024 en 1280 (GEZIEN in `merk/proef/`). Mila's v1 niet overschreven.
- Vondst 2: de achtergrond had een tweede grote D naast het woordmerk ("ortusD") en half onder de spellen. Besluit: v1b zonder tweede D, het licht valt uit de D van het logo, spullen in de kantlijn. Waarom: één D tegelijk is rustiger en het logo blijft de held. Uitleg en verzoek in `merk/voor-mila.md`.
- Steam-profiel getoetst: Steam toont maar drie regels. Besluit: profieltekst korter (spel in één regel), zodat het mailadres in beeld blijft. Groep en ontwikkelaarspagina houden de lange zin.
- Daans moet-punten 1 en 2 en kan-punt 3 verwerkt in `teksten.md` v2 en `steam.md` v2. Regel voor keuring 2 onderaan `ontwerp/keuring-abel.md`.
- GitHub getoetst op de repopagina van Rollwright (licht en donker): avatar leest op 24 px. Ter info in `github.md`: bij de commits staat "claude" als maker; past bij de eerlijke AI-zin.
- dortus.com v2 in het uniform, met nieuwe bestandsnamen zodat niets bestaands verandert; voorbeelden opnieuw bekeken. Eerst zag je een donker vierkant achter de grote D; opgelost met een versie zonder achtergrond.
- `klaar.md` versie 1.
- Volgende run: keuring 2 van Daan verwerken; kijken of Mila v1b overnam; plannen Polar, Blender, JetBrains, Obsidian met proef per platform (rond knippen op Discourse en Blender ID); Steam Online Conduct lezen; eerste bijdrage op een eigen plek.

## Run 3, 10 nov 2026 ±02:20 NL
- Gelezen: logboek, berichten (niets nieuws voor mij), Mila's v2 onderaan `merk/uniform.md` (wacht op keuring 3 van Daan), keuring 2.
- Blender: in de openbare broncode van Blender ID en extensions-website nagezocht dat er een eigen avatarveld is (png/jpg/webp, max 2 MB, wordt JPEG), dat extensions.blender.org hem via een seintje overneemt, en waar het veld staat (id.blender.org/settings/profile). Onzekerheid over Gravatar weg. Proef in de echte wachtrijpagina. Plan v2.
- Obsidian: vondst, het forumprofiel staat op verborgen (`profile_hidden: true`), dus About me zou niemand zien. Stap toegevoegd. Besluit: About me met dezelfde woorden als de draad van 8 nov ("The code is written by AI agents; I direct and test the work"). Waarom: twee versies van de AI-zin lezen als afzwakken. Proef op de echte draad, licht en donker. Plan v2.
- Polar: logoveld nagezocht in de broncode van Polar (rondje "Logo" in Settings, max 1 MB, ook svg). Op de afrekenpagina staat nu een grijze letter D (logo.dev vond niets). Eén bezoek aan de afrekenpagina, niets ingevuld; proef met onze D. Plan v2. Besluit: Polar in de volgorde naar voren. Waarom: dat is waar iemand betaalt.
- JetBrains: vondst, een verkoperspagina heeft geen logo (zelfs JetBrains zelf niet, GEZIEN in de browser). Logo-stap geschrapt, alleen een kleine tekstwijziging over, laagste voorrang. Plan v2.
- Steam: grootste vondst. Valve: een account met minder dan $5 uitgegeven in de winkel kan geen groep maken en zijn profiel niet aan niet-vrienden tonen (help.steampowered.com en Steamworks-docs, GEZIEN). dortusgames is nieuw, de $100 fee telt waarschijnlijk niet (GOK). Besluit: stap 0 in het Steam-plan (v3) en een ja/nee voor €5 op de portemonnee op lijst-thijs. Waarom: zonder dat lopen profiel, groep en ontwikkelaarspagina vast.
- Daans moet-punt 1 (grote D achter de middenkolom) genoteerd als opgelost: v1b en v2 hebben geen tweede D. In het Steam-plan staat welke versie (v1b nu, v2 na keuring 3).
- Mila geantwoord in `merk/voor-mila.md`: social per repo eerst rollwright, dan click-joints; avatar op 24 px rond leest, scharnieren worden spikkels (kan-punt, geen haast).
- Communityregels: Obsidian-gedragscode gelezen (geen AI-regel, wel "participate more than you promote"), Steam Online Conduct gelezen (geen AI-regel; geen advertenties, wedstrijden of reviews sturen). Eigen plekken: 0 issues, geen reacties in de draad; niets te beantwoorden.
- `klaar.md` versie 2.
- Volgende run: keuring 3 van Daan verwerken (v2-bestanden in alle plannen); GitHub-plan nalopen op v2 en social per repo; dortus.com-pagina controleren tegen v2; nagaan of de hoofdchat de dortus.com-vraag al stelde.

## Run 4, 10 nov 2026 03:24 NL
- Gelezen: logboek, berichten (niets nieuws), keuring 3 en Mila's v3 en avatar v2 in `uniform.md`.
- Daans moet 3 (keuring 3) uitgevoerd: achtergrond v3 met kop en logo v2 op de echte Steam-pagina gezet op 1280, 1920 en 2560 (`proef/steam-pagina-v3-*`). Vondst: Steam zet naast het plaatje de paginakleur die de maker kiest (Klei: zwart, harde rand op 2560). Met `#1d1426` naadloos, gemeten. Besluit: paginakleur als vaste stap in het Steam-plan. Waarom: anders faalt Mila's oplossing op brede schermen. Later bevestigd in de Steamworks-docs: Valve raadt precies dit aan.
- Vloerlijn op y 386 gemeld als kan; Daan: laten zo.
- Daans kan 5 (geen "small games" op og en social zolang er geen spel uit is): `og-1200x630-v2-nu.png` en `social-1280x640-v2-nu.png`, Mila's v2 met alleen een andere onderregel ("Focused tools today, small games on the way"). Besluit: zelf gedaan met `sed` op haar svg. Waarom: tekstwijziging, geen nieuw beeld, en dortus.com en GitHub kunnen eerder live dan Hats op Steam. Daan: ja.
- dortus.com: og-home, titel en beschrijving op de ware zin; deur-D op avatar v2; voorbeelden opnieuw bekeken.
- Keuring 4 van Daan kwam binnen tijdens deze run: achtergrond v3 ja (mits paginakleur Nacht), avatar v2 ja. Alle plannen nu op avatar v2, kop v2, logo v2, achtergrond v3. Steam-plan v4, GitHub-plan v3 (bio zonder spelbelofte, social preview stap).
- Steam-groep: kop "Focused tools today, small games on the way". Waarom: zelfde reden als kan 5.
- Obsidian-GOK opgelost: "Hide my public profile" staat in Preferences > Profile (Discourse-broncode).
- Eerste community-bijdrage: `bijdrages/2026-11-10-obsidian-open-with.md`, antwoord op een vraag zonder antwoord sinds 2 nov, onderbouwd met de officiële changelog, geen promotie.
- Proeven van Polar, Blender, Obsidian en GitHub opnieuw met avatar v2 (`bron/mock4v2.js`, `mock5v2.js`, `mock6v2.js`), bekeken: de scharnieren zijn geen spikkels meer.
- Mila gevraagd (kan): Steam-logo, og en social gelijktrekken met avatar v2.
- `klaar.md` versie 3.
- Steam-profielproef opnieuw met avatar v2 (mal: openbaar profiel robinwalker, alleen in mijn browser vervangen).
- Volgende run: kijken of Mila logo/og/social v2-scharnieren maakte en wisselen; eigen plekken nalopen (issues, forumdraad) en de bijdrage nog eens checken (heeft iemand intussen geantwoord?); eventueel een tweede bijdrage, alleen als hij echt goed is.

## Run 5, 10 nov 2026 04:23 NL
- Gelezen: logboek, berichten (niets nieuws), keuring 4, `uniform.md` en `voor-mila.md`. Mila maakte de v2-scharnieren voor logo, og en social niet (ze werkt aan Hats).
- Eigen plekken nagelopen (curl): issues rollwright en click-joints 0, Rollwright-draad op het forum 1 bericht en geen reacties, Royi's vraag (bijdrage 1) nog steeds zonder antwoord. Bijdrage blijft geldig.
- Besluit: scharnieren van Steam-logo, og en social zelf gelijkgetrokken met avatar v2, als `-v2b`. Waarom: Daans kan uit keuring 4, de kit moet om 06:19 klaar zijn, en het is Mila's eigen regel (zelfde twee getallen), geen nieuw beeld. Script `merk/bron/abel_scharnier_v2.py`, voor en na `merk/proef/scharnier-v2-v2b.png`, bekeken: scharnieren nu half in de D zoals in de avatar. Mila en Daan op de hoogte; plannen wisselen pas na Daans ja.
- `upload/` en `dortus-beelden.zip`: alle goedgekeurde beelden per account met namen die zeggen waar ze heen gaan, plus `LEESMIJ.md` (bron `merk/LEESMIJ-upload.md`, script `merk/bron/maak_upload.sh`). Waarom: in `merk/` staan v1, v1b, v2, v3 en v2b door elkaar; zo kan Thijs niet het verkeerde bestand pakken. Alles bekeken in één overzicht; nagemeten dat de Steam-avatar echt v2 is.
- Steamworks-docs: veilige zone van 940 px en achtergrond onder 4 MB (ons bestand 0,3 MB). Knopnaam paginakleur staat niet in de openbare docs (pagina laadt pas na inloggen); blijft "het veld bij de achtergrond".
- Geen tweede bijdrage: de open vragen op forum.obsidian.md (Get help, Developers) vragen tests of data die we niet hebben. Liever geen dan een half antwoord.
- Volgende run (05:19): Daans antwoord op v2b verwerken (upload opnieuw, plannen wisselen); klaar.md naar versie 5; bijdrage 1 nog eens checken.

## Run 6, 10 nov 2026 05:22 NL
- Gelezen: logboek, berichten (niets nieuws), keuring 5 van Daan: **ja voor de scharnieren v2b** (Steam-logo, og en social), "de v2-versies niet meer gebruiken".
- Uitgevoerd: v2b in `accounts/steam.md` (paginalogo, twee plekken), `github.md` (social preview), `dortus-com.md` en `dortus-com/assets/og-home.png`. `maak_upload.sh` maakt nu standaard v2b; `upload/` en `dortus-beelden.zip` opnieuw gemaakt en met `cmp` nagemeten dat de juiste bestanden erin zitten. Alle tien uploadbeelden samen bekeken met Read.
- Definitieve Steam-proef opnieuw gemaakt met logo v2b (`proef/steam-pagina-definitief-1920.png` en `-1280.png`), bekeken: avatar linksboven en groot logo hebben nu dezelfde scharnieren. Regel voor Daan onder keuring 5.
- Nieuw: `merk/proef/overzicht-alle-accounts.png`, alle proeven op één blad (script `merk/bron/abel_overzicht.py`), bekeken. Besluit: dit als eerste blad in `klaar.md`. Waarom: Thijs wil "mooie plaatjes overal" zien; één blad om 08:00 is sneller dan zeven losse bestanden.
- `klaar.md` versie 5.
- Bijdrage 1 nagekeken: Royi's vraag (t/120796) heeft nog steeds 0 antwoorden (curl, 05:30). Blijft geldig.
- Op zoek naar een tweede bijdrage: forum.obsidian.md Get help en Developers zonder antwoord nagelopen. Vondst die voor ons telt: t/121588 (makers zien dat ±38% van de downloadcijfers in `community-plugin-stats.json` automatische manifest.json-ophaalacties waren, en dat dat rond 1 nov bijna stopte). Bij Rollwright klopt het cijfer per versie met de manifest.json-tellers op GitHub, en main.js loopt gelijk op (0.3.3: 6 en 6; 0.3.4: 4 en 5; GEZIEN via de openbare API). Dus onze 23 downloads zijn waarschijnlijk echte installs of updates, geen robots. Besluit: geen antwoord in die draad klaarschrijven. Waarom: de vraag is aan het Obsidian-team, en onze plugin bestaat pas sinds na de daling, dus we voegen weinig toe; liever geen dan een dun antwoord. Ter info voor wie downloads meet (Patrick), via de hoofdchat.
- Steam stap 0 (telt de $100 mee voor de $5-grens?): nog eens gezocht, niets nieuws in openbare bronnen. Blijft GOK met de controle die al op lijst-thijs staat.
- Volgende run (06:19): merkkit en Steam-plan moeten dan klaarstaan (dat doen ze). Dan: alle plannen nog één keer van boven naar onder lezen als Thijs (klopt elke knop, elk bestand, geen v1/v2 meer), en de teksten in `steam.md` naast het overzichtsblad leggen.

## Run 7, 10 nov 2026 06:21 NL
- Gelezen: logboek, berichten (niets nieuws), keuring-abel (niets nieuws na keuring 5). Lokale kopie stond los van main; opnieuw aan origin/main gekoppeld.
- Alle zeven plannen van boven naar onder gelezen als Thijs met de zip open. Rechtgezet: elk plan noemt nu het bestand uit `upload/` (naam die Thijs ziet) in plaats van `merk/...-v2.png`; koppen van de plannen bijgewerkt (Steam zei nog "beelden v2"); Steam-knoppen ook in het Engels; Polar zonder oude "spikkels"-zin; Obsidian begint met het vinkje "Hide my public profile".
- Vondst: de GitHub-bio beloofde nog "A tiny dungeon game is on its way to Steam", terwijl run 4 noteerde dat dat eruit was. Besluit: bio `Focused tools for Obsidian, Blender and JetBrains. Small games on the way.` Waarom: gelijk aan og en social (Daan, kan 5) en aan mijn eigen regel in `teksten.md` (spel pas noemen als de winkelpagina "binnenkort" is). Op Steam zelf noemen profiel en groep het spel wel; dat is de plek waar het komt, en we zeggen nergens dat het uit is.
- Nagemeten met `cmp`: avatars in `upload/` zijn de goedgekeurde v2.
- Teksten naast de winkelpagina van Sanne gelegd: zelfde ondertitel "a tiny dungeon on your taskbar", geen tegenspraak.
- GitHub-proef opnieuw (`bron/mock4v3.js`): nu ook het vak About gevuld zoals na stap 2. Het oude script verving "No description" niet (de tekst zat in een element met kinderen). Licht en donker bekeken.
- Overzichtsblad aangevuld met dortus.com (rij 6, wacht op ja), bekeken.
- Bijdrage 1: Royi's vraag nog steeds zonder antwoord (curl 06:35). Blijft geldig.
- `klaar.md` versie 6.
- Volgende run (07:19): klaar.md definitief maken (stand in één zin bovenaan nalezen, tijden optellen); lijst-thijs nalopen of mijn punten daar nog kloppen met de plannen.
- Nog gezocht naar een tweede bijdrage (forum.obsidian.md, nieuwste vragen zonder antwoord). t/121749 ("Network drive access" bij elke start, SMB-kluis): alle desktop-changelogs 1.14.0 tot 1.15.1 doorzocht, niets over die melding. Besluit: geen antwoord. Waarom: zonder eigen test of bron zou het gokken zijn. t/121779 is door de vrager verwijderd.
- `klaar.md`: totale Thijs-tijd erbij (±34 min plus later 15).

## Run 8, 10 nov 2026 07:21 NL
- Gelezen: logboek, berichten (niets nieuws), keuring-abel (niets na keuring 5), lijst-thijs. Mijn twee punten daar (€5 Steam, dortus.com) kloppen met de plannen. Steam-namen id/dortus en groups/dortus nog vrij (curl). Bijdrage 1: vraag t/120796 nog zonder antwoord.
- Vondst: Hans zette om 06:45 een Superhive-verkopersaccount op lijst-thijs (Click Joints Pro). Besluit: Superhive-plan maken. Waarom: dat account komt er vanochtend, en Superhive zegt zelf dat een winkel zonder instellen een standaardbanner, leeg rondje en geen beschrijving toont; dat is precies wat mijn rol moet voorkomen.
- Nagezocht: eisen uit Superhive's hulppagina's (avatar 400x400 JPG, banner 1200x330, JPG/PNG, onder 5 MB, veldnamen) en in hun stylesheet hoe het getoond wordt (banner 350 px hoog, volle breedte, bijgesneden in het midden; avatar rond 150 px met witte rand half over de onderrand). Slug `dortus` lijkt vrij.
- Besluit: banner als uitsnede van Mila's goedgekeurde achtergrond v3, opnieuw getekend uit de svg op 2400x660, bovenrand y 270. Waarom: geen concurrerend beeld, zelfde uniform; eerste poging (y 330) sneed de lichtopening weg op 1920, dus omhoog geschoven. Proef op de echte winkel op 1920, 1280 en telefoon, bekeken.
- Beschrijving zonder antwoordtijd. Waarom: niemand leest die berichten nu elke dag; geen belofte die we niet halen.
- `upload/7-superhive/` en de zip opnieuw gemaakt (cmp nagemeten). Keuring 6 gevraagd aan Daan; Bram ter info (productpagina is van hem). Regel op lijst-thijs direct onder het punt van Hans.
- `klaar.md` versie 7, definitief.
- Volgende run (08:19, laatste): Daans antwoord op de banner verwerken (ja: niets doen; nee: banner uit plan en upload); klaar.md nalezen (Superhive staat sinds run 8 al in het overzichtsblad, rij 7).
