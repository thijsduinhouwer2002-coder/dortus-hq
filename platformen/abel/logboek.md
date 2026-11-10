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
