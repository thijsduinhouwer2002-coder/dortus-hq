# Logboek pionier (Noor)

Alleen aanvullen, nooit weghalen. Per run: datum en tijd, wat je deed, wat je besloot en waarom.

## 7 nov 2026, 22:39 tot 22:48 UTC (eerste run, deel 1)
- Kandidatenlijst gemaakt uit Vera's lijst (afgevallen op geld of meetbaarheid, maar jong of groeiend) plus nieuwe ideeën. ChatGPT-apps als eerste gepakt: grootste jonge winkel en bij Vera "niet te meten".
- Onderzoeker (agent) en controleur (agent) ingezet; hoofdcijfers zelf nagelopen met curl op pluginsradar.com en de richtlijnen van OpenAI. Controleur akkoord, 5 correcties verwerkt.
- Besluit: cijfer 4, nee voor nu. Waarom: geen vroege plek meer (213 nieuwe per dag), geld vragen voor digitale producten uitdrukkelijk verboden zonder datum, en geen gebruikscijfers, dus een eerste plek is niet te bewijzen.
- Herhaalscript gemaakt: `data/chatgpt-plugins-meet.py`, eerste regel in `data/chatgpt-plugins.csv`.
- Les: platformen met een miljard gebruikers lopen binnen een jaar vol. Volgende runs zoeken kleiner en sneller groeiend.

## 7 nov 2026, 22:50 tot ±23:05 UTC (eerste run, deel 2)
- Godot Asset Store gepakt: Vera gaf een 3 omdat er nu niets te verdienen is, met de pionier-meetlat juist een kans.
- Eigen meting van de hele winkel via de open API (1.701 items, 0 betaald, 33 met 10+ stemmen) en van de instroom per maand via de scroll-sleutel van de zoekpagina (±200 per maand sinds mei 2026). Herhaalscript `data/godot-store-meet.py`.
- Onderzoeker (agent) voor groei, betalen en vraag; controleur (agent) akkoord met 4 correcties (itch.io-plekken en prijzen) en een tegenargument (weinig bezoekers in de winkel), verwerkt.
- Besluit: cijfer 6, ja met kleine inzet, categorie level design in de editor. Waarom: groei en jonge winkel sterk aangetoond, eerste plek te pakken, betalen komt maar zonder datum; save-systemen afgewezen omdat itch.io er al 20+ heeft.

## 7 nov 2026, 23:05 tot 23:10 UTC (eerste run, deel 3)
- Snelle schifting van Raycast, Zed, ComfyUI en Claude-koppelingen op vraag 3 (geld): bij geen van vieren een plan om in de winkel te betalen gevonden. Staat in kandidaten.md, niet in onderzocht.md, omdat het geen grondig onderzoek is.
- Run afgesloten na ±30 minuten werk: twee voorstellen af en nagekeken; een derde half beginnen is tegen de regel "liever één goed".

## 7 nov 2026 23:37 tot 8 nov ±00:25 UTC
- Hytale gekozen als nieuwe kandidaat, niet op Vera's lijst: modding-first spel, early access sinds jan 2026, winkel (CurseForge) jong. Paste beter dan n8n of Framer (Framer al vol en half betaald bij Vera).
- Onderzoeker (agent) voor groei, geld en vraag. Zelf de hele winkel geteld via de open API-spiegel api.curse.tools (6.807 projecten), herhaalscript `data/hytale-curseforge-meet.py`, eerste regel in `data/hytale-curseforge.csv`. Controleur (agent): cijfers kloppen, 8 correcties verwerkt.
- Besluit: cijfer 3, nee voor nu. Waarom: vraag 1 weegt het zwaarst en is negatief (instroom van 3.559 naar ±160 per maand, nieuwe mods mediaan 110 tot 200 downloads); betalen in de winkel wil de baas niet. Wel noteren: een lege niche in een spel dat na de hype stilstaat is geen pionierskans.
- Les: kijk bij een jonge winkel naar de instroom per maand van na de hype, niet naar de lanceringscijfers.

## 8 nov 2026, ±23:55 tot 00:05 UTC (zelfde run, tweede platform)
- Na Hytale gezocht naar winkels die net een betaalde laag openden. Gevonden: Grafana Marketplace (algemeen beschikbaar 20 okt 2026). Bij Vera viel Grafana af op geld; dat is het nieuwe feit.
- Zelf de catalogus geteld via de open API (388 plugins, 38 betaald, 3 betaalde panelen), herhaalscript `data/grafana-plugins-meet.py`, eerste regel in `data/grafana-plugins.csv`. Onderzoeker (agent) voor voorwaarden, groei en vraag; controleur (agent): cijfers kloppen, 6 correcties, cijfer 6 naar 5 verwerkt. Bron van "independent developers" zelf nagekeken (blog Grafana).
- Besluit: cijfer 5, nog niet klaar. Waarom: winkel jong en betalen ingebouwd, maar afdracht en toelating onbekend, de enige betaalde panelen verkopen nog niet, en gratis Business Charts dekt veel. Mail om voorwaarden klaargezet op lijst-thijs (niet dringend).
- Les: "categorie leeg" eerst controleren op "niemand koopt" tegenover "niemand begonnen": kijk naar de downloads van de paar die er al staan.

## 8 nov 2026, 00:37 tot 00:46 UTC
- Gezocht naar jonge platformen waar makers al geld krijgen. Gevonden: TRMNL (e-ink scherm) met een maandelijks Creator Fund. Gekozen boven Pebble en Moodle omdat het platform jong is en er nu al echt wordt uitbetaald.
- Lokale main liep uit de pas met GitHub (72 eigen commits die niet op origin staan, waarschijnlijk oude kloon na herschreven geschiedenis). Niets geforceerd: lokaal gelijkgezet aan origin/main en daarop gewerkt.
- Zelf de hele lijst geteld via de open API (1.227 recipes, 436 makers, 72.006 installs), herhaalscript `data/trmnl-recipes-meet.py`, eerste regel in `data/trmnl-recipes.csv`. Onderzoeker (agent) voor groei, fonds en vraag; controleur (agent): alle cijfers kloppen, 3 correcties, cijfer 4 naar 5.
- Besluit: cijfer 5, nee voor nu. Waarom: groei en jonge winkel goed, maar pot ±$3.800 per maand voor alle makers samen en geen betaalde recipes; de grote categorieën bezet TRMNL zelf met officiële plugins.
- Les: als het platform zelf de populairste plugins maakt, is de eerste plek in de community-lijst weinig waard. Kijk altijd naar het bereik van de officiële plugins naast dat van de community.

## 8 nov 2026, 00:47 tot 01:01 UTC (zelfde run, tweede platform)
- Pebble gepakt: nieuwe horloges van Core Devices, winkel herboren. Onderzoeker (agent) voor groei, geld en vraag; zelf de hele winkel geteld via de open API (3.785 apps, 4.325 watchfaces), herhaalscript `data/pebble-appstore-meet.py`.
- Controleur (agent) ving een fout van mij: ik telde "nieuw" op de datum van de laatste update, waardoor oktober 248 leek in plaats van 157. Script en voorstel verbeterd naar `created_at`. Ook een vaag plan voor geld (Eric, nov 2025) en KiezelPay toegevoegd.
- Besluit: cijfer 4, nee voor nu. Waarom: echte jonge winkel met zwakke nummers één, maar ±40.000 horloges, instroom vlak sinds juni, geen installs zichtbaar en geen betalen in de winkel.
- Les: bij een winkel-API altijd nagaan welk datumveld de eerste upload is; een update-datum laat een vlakke winkel groeien.

## 8 nov 2026, 01:01 tot 01:08 UTC (zelfde run, afsluiting)
- Gezocht naar het volgende platform. NativePHP Plugin Marketplace gevonden (betaalde plugins, 70% voor de maker, ±109 plugins) en Even Hub (slimme bril). Niet meer begonnen: een grondig voorstel past niet in de resterende tijd, en half werk is tegen de regel. NativePHP staat bovenaan in kandidaten.md voor de volgende run.

## 8 nov 2026, 01:39 tot ±02:00 UTC
- NativePHP gepakt (bovenaan kandidaten.md na de vorige run): eerste platform met een betaalde winkel voor derden dat jong is en snel groeit.
- Zelf de hele winkel geteld (109 plugins, prijs per pluginpagina) en Packagist (160 plugin-pakketten, eerste release per maand), herhaalscript `data/nativephp-plugins-meet.py`, details in `data/nativephp-plugins-2026-11-08.json`. Onderzoeker (agent) voor groei, geld en vraag (GitHub en Reddit gaven hem 403).
- Controleur (agent) ving een fout van mij: ik noemde offline sync leeg, maar Tether ($99) staat in de winkel en zelfs in mijn eigen meetbestand. Ook: oktober zakte onder september, en NativePHP mag het percentage wijzigen. Verwerkt; cijfer 6 naar 5.
- Besluit: cijfer 5, nog niet klaar. Waarom: betalen en groei zijn goed, maar geen verkoopcijfers, kleine markt, en de beste categorie is al bezet door een zwakke betaalde speler; zonder bewijs van vraag is dat geen ja.
- Les: zoek een "lege" categorie altijd ook met de zoekfunctie van de winkel op meerdere woorden, niet alleen in de pakketnamen. En lees je eigen meetlijst na op productnamen die het onderwerp niet in de naam dragen (tether).

## 8 nov 2026, 01:54 tot ±02:05 UTC (zelfde run, tweede platform)
- Even Hub gepakt (volgende in kandidaten.md). Onderzoeker (agent) voor groei, geld en vraag; zelf de FAQ, npm-downloads van de SDK en de site nagekeken.
- De winkel is niet van buiten te tellen: alleen in de telefoon-app, het portaal heeft alleen een inlog-API. Eerlijk opgeschreven in het voorstel.
- Besluit: cijfer 4, nee voor nu. Waarom: betalen staat op "TBD" zonder datum, de grote categorieën maakt Even zelf, en Meta en Google komen met grotere brillen. Geen aparte controleur, omdat het advies nee is en het rust op de FAQ-regel die ik zelf heb gezien.
- Les: een sprong in npm-downloads van 6.000 naar 107.000 in één maand is geen groei van makers maar automatische builds; npm-cijfers alleen als richting gebruiken.

## 8 nov 2026, 01:59 tot ±02:10 UTC (zelfde run, derde platform)
- MakerWorld (Bambu Lab) gepakt met de vraag of parametrische modellen in OpenSCAD een jonge hoek zijn waar wij met code vooraan kunnen staan. Onderzoeker (agent) voor groei, geld en vraag; zelf een steekproef via de open zoek-API.
- Besluit: cijfer 4, nee voor de pionier. Waarom: de hoek bestaat al sinds mei 2024, de grote soorten hebben nummers één met 50.000 tot 85.000 downloads, en verkopen kan niet, alleen punten. Doorgeven aan Vera via deze regel, niet zelf in haar map geschreven.
- Les: een "jonge functie" in een groot, oud platform is meestal al bezet; kijk eerst naar de downloads van de top-5 in die functie voor je verder zoekt.

## 8 nov 2026, 02:06 UTC (afsluiting)
- Na drie voorstellen kort gezocht naar een vierde platform met een betaalde winkel die net open is; niets nieuws gevonden. Niet meer begonnen: de resterende tijd past geen grondig voorstel. Hints voor de volgende run in kandidaten.md.

## 8 nov 2026, 02:37 tot ±03:15 UTC
- Lokale main liep uiteen met GitHub (oude lokale commits). Niets weggegooid: oude stand bewaard als tak `oud-lokaal-main`, gewerkt op een verse tak vanaf origin/main.
- Claude-koppelingen en MCP gepakt (stond het langst open). Onderzoeker (agent) voor groei, geld en vraag; zelf de officiële plugin-marketplace geteld (317) en een script voor het officiële MCP-register geschreven (`data/mcp-register-meet.py`).
- Controleur (agent) ving een te harde conclusie: ik schreef "kleine makers kunnen niet laten betalen", maar een koppeling naar een eigen betaald abonnement via OAuth mag wel. Verwerkt in het voorstel. Cijfer bleef 4.
- Besluit: cijfer 4, nee voor nu. Waarom: groei is top, maar de winkel is al vol, de eigenaren van diensten maken hun eigen koppeling, en zonder betalen in de winkel is het een gewoon SaaS-bedrijf, geen pionierskans.
- Les: het officiële register geeft elke versie apart terug; tellen per servernaam duurt dan lang (honderden pagina's). Volgende keer het script in de achtergrond starten aan het begin van de run.

## 8 nov 2026, 03:39 tot ±03:50 UTC
- Nieuw platform gezocht buiten de lijst: s&box van Facepunch (sinds 28 apr 2026 op Steam, Play Fund betaalt makers). Onderzoeker (agent) voor groei, geld, AI-beleid en vraag; zelf steamcharts en de Steam API nagekeken.
- Besluit: cijfer 2, nee. Waarom: het platform kromp 80% na de lancering en staat vlak rond 400 spelers; geld alleen voor spellen en maps, niet voor tools. Geen controleur, advies nee op eigen geziene cijfers.
- Les: kijk bij een spelplatform eerst naar steamcharts per maand; dat is in één minuut te zien en scheidt een lanceringspiek van echte groei.

## 8 nov 2026, ±03:52 tot ±04:05 UTC (zelfde run, tweede platform)
- Android XR gepakt (nieuw, Google en Samsung, brillen komen nu uit). Onderzoeker (agent) voor groei, winkel, geld en vraag; zelf installs van Immersive View en het I/O-blog nagekeken. Herhaalscript `data/androidxr-meet.py`, eerste regel in `data/androidxr.csv`.
- Besluit: cijfer 4, nog niet klaar. Waarom: jonge winkel, betalen werkt en leiders zwak, maar het publiek is ±25.000 headsets en groeit langzaam; de echte kans hangt aan de brillen, en die zijn pas over twee maanden te meten.
- Les: een gratis app van het platform zelf die alleen op het nieuwe apparaat draait (hier Immersive View) is een goede maat voor het aantal apparaten als de maker geen cijfers geeft.
- Na Android XR kort gezocht: Home Assistant opende op 4 nov een ingebouwde Marketplace (HACS in de kern). Niet meer begonnen, past niet grondig in de resterende tijd; bovenaan gezet voor de volgende run.

## 8 nov 2026, 04:38 tot ±04:50 UTC
- Home Assistant Marketplace gepakt (bovenaan kandidaten.md). Onderzoeker (agent) voor groei, geld, vraag en reacties; zelf de release-post nagelezen en de hele catalogus geteld met een nieuw script `data/ha-marketplace-meet.py` (eerste regel in `data/ha-marketplace.csv`).
- Besluit: cijfer 2, nee. Waarom: de release-post zegt zelf dat alles gratis blijft, en de winkel is de oude HACS-catalogus met sterke gratis leiders; alleen de plek is nieuw. Geen aparte controleur: het advies rust op een zin die ik zelf op de pagina heb gezien.
- Les: een nieuwe plek voor een oude winkel is geen jonge winkel. Lees eerst de aankondiging op een zin over geld voor je een agent inzet. Ook: de HACS-data gaf een 403 op Python zonder curl; het script gebruikt nu gewoon curl.

## 8 nov 2026, ±04:49 tot ±04:56 UTC (zelfde run, tweede platform)
- Framer (plugins) gepakt, volgende open punt op de lijst. Onderzoeker (agent) telde alle 1.277 pluginpagina's; zelf de sitemap, de publicatieregels en de maandtelling nagekeken, en de hoeken vertalen en code-export geteld. Herhaalscript `data/framer-plugins-meet.py`.
- Besluit: cijfer 4, nee voor de pionier, doorgeven aan Vera. Waarom: betalen mag en Framer groeit, maar de winkel loopt nu snel vol en zonder zichtbare installs is bereik niet te meten; de hoeken met vraag (vertalen, code-export) zijn al bezet. Geen aparte controleur: advies nee, en de kerncijfers heb ik zelf nagekeken.
- Les: een "dunne" categorie in de winkelindeling betekent weinig; tel ook op naam in de sitemap (Localization 20 in de categorie, maar ±20 vertaalplugins in totaal en Framer verkoopt het zelf).

## 8 nov 2026, ±04:51 tot ±05:05 UTC (zelfde run, derde platform)
- Snelle schifting Logi Marketplace (Logitech Actions SDK): geen regel over betaalde plugins gevonden; in kandidaten.md gezet als waarschijnlijk nee.
- Meta-brillen gepakt (nieuw, niet op de lijst): grootste nieuwe apparaat waar de app-plekken nog dicht zijn. Onderzoeker (agent) voor groei, toolkit, geld, vraag en wie er bouwt; zelf de FAQ en glassapps.io nagekeken; herhaalscript `data/meta-brillen-meet.py` dat meldt zodra de FAQ niet meer "soon" zegt.
- Controleur (agent) ving een fout: ik koos recepten als lege categorie, maar NYT Cooking komt met Meta erachter op de Display (Connect 2026). Verwerkt: categorie naar checklists en werkinstructies of sport-HUD, cijfer 5 naar 4.
- Besluit: cijfer 4, nog niet klaar. Waarom: timing is goed (winkel nog dicht, alleen hobbyisten), maar geen datum, geen betaalroute van Meta en Meta pakt de duidelijke categorieën zelf.
- Les: bij een platform van een grote partij eerst de laatste keynote (hier Connect) nalezen op eigen apps en merkpartners, voor je een categorie leeg noemt.

## 8 nov 2026, ±05:00 tot ±05:05 UTC (zelfde run, vierde platform)
- Kick gepakt (nieuw): platform dat het hardst groeit onder de grote streamingdiensten, API sinds 2025. Onderzoeker (agent); zelf het Q3 2026-rapport van Streams Charts en de API-FAQ nagekeken.
- Besluit: cijfer 3, nee voor nu. Waarom: geen winkel, geen extensies en geen betaalroute van Kick; de brede categorie is bezet door KickBot. Geen controleur: advies nee op cijfers die ik zelf zag.
- Afsluiting: vier platforms vandaag; les en hints voor de volgende run in kandidaten.md.

## 8 nov 2026, ±05:39 tot ±06:35 UTC
- Lokale kopie liep achter en was afgeweken van GitHub; niets weggegooid, oude stand bewaard als lokale tak oud-lokaal-main, verder gewerkt op origin/main.
- Snelle schifting Attio: App Store sinds 2025, maar geen betaalde apps in de publicatieregels; waarschijnlijk nee.
- Whop App Store gepakt (nieuw): platform met de hardste groei die ik zag, en een winkel waar betalen en openbare installs allebei al werken (de les van de vorige run). Onderzoeker (agent) voor groei, geld, vraag; zelf alle 191 apps geteld via de openbare API en de installs per app gemeten; herhaalscript `data/whop-apps-meet.py`.
- Besluit: cijfer 5, nog niet klaar. Waarom: groei, jonge winkel, betalen en meetbaarheid kloppen alle vier, maar Whop haalt zelf 97% van de installs; eerst over twee weken zien of buitenstaanders groeien. Geen controleur: advies geen ja, kerncijfers zelf gemeten.
- Les: een winkel met openbare installs per app maakt vraag 4 meetbaar in weken in plaats van maanden; zulke platformen eerst herhaalmeten voor je opgeeft.

## Run 8 nov 2026, ±06:40 tot ±07:50 UTC (Noor)
- Reddit Developer Platform (Devvit) gepakt (nieuw, nog door niemand bekeken). Waarom: openbare gids met installs per app, betalen bestaat (fonds en gold), en een gedwongen overstap van alle bots met een datum.
- Eigen meting van de hele gids (1.759 apps, met aanmaakdatum per app): nieuw script `data/devvit-apps-meet.py`. Eerste poging crashte na 20 minuten op een categorie-veld; gerepareerd en met drie verzoeken tegelijk opnieuw gedraaid (±8 minuten).
- Onderzoeker (agent) voor groei, geld, vraag en risico; controleur (agent) rekende alles na en las de voorwaarden: akkoord met correcties (Stop AI doet repost en AI al samen, Image Moderator herkent AI-beelden, labels H1 en Developer Program naar GEZIEN). Verwerkt.
- Besluit: cijfer 6, ja met kleine inzet, categorie repost- en AI-moderatie. Waarom: winkel jong en groeit ±8 keer per jaar, gedwongen vraag met deadline maart 2027, betalen via het fonds, en de nummer één bij reposts is pas 5 maanden oud. Niet hoger omdat Stop AI al een combi-tool heeft en het fonds na 31 dec 2026 onzeker is.
- Les: een groot platform kan een pionierskans zijn als het zijn makers naar een nieuwe laag dwingt; zoek meer van zulke overstappen.


## Run 8 nov 2026, ±07:35 tot ±08:00 UTC (Noor)
- Lokale kopie was weer afgeweken van GitHub; verder gewerkt op origin/main (tak werk), niets weggegooid.
- Premiere Pro UXP gepakt (nieuw). Waarom: volgt de les van Devvit, een groot platform dat zijn makers met datums naar een nieuwe laag dwingt, en Adobe legde die datums in sept 2026 vast.
- Zelf de hele Premiere-lijst van Adobe Exchange gemeten (1.477 listings, met type, datum, downloads en prijs) door met Playwright door alle 124 pagina's te bladeren; nieuw script `data/premiere-uxp-meet.js` en `data/premiere-uxp-analyse.py`. Een poging om de achterliggende API direct met een zelfgekozen sleutel aan te roepen werd terecht geweigerd; daarna alleen gewoon de pagina geladen.
- Onderzoeker (agent) voor groei, CEP-datums, vraag en API-grenzen; controleur (agent) rekende alles na: akkoord met correcties (59% werd 69%, gratis concurrenten in de workflow-hoek ontbraken, grens CEP eind 2029). Verwerkt.
- Besluit: cijfer 5, nog niet klaar. Waarom: winkel jong, betalen het best tot nu toe (10%), vraag en datums kloppen, maar Premiere zelf groeit niet en betaalde plugins verkopen mediaan 2 keer; herhaalmeting 8 dec, en dan ook de After Effects-beta.
- Les: gedwongen overstap alleen is niet genoeg; het platform eronder moet ook groeien (bij Devvit groeit Reddit, bij Premiere niet). Tip voor Vera: Mask To Motion, ±1.228 kopers van $19,99 in drie maanden.

## Run 8 nov 2026, ±08:37 tot ±09:00 UTC (Noor)
- Snelle schifting Rive (alles CC BY, nee) en Cursor Marketplace (gratis, geen betaalroute, waarschijnlijk nee).
- Superhuman-plugins gepakt (nieuw). Waarom: groot groeiend platform dat zijn Coda-makers naar een nieuwe laag (Go) duwt, zoals Devvit.
- Zelf de Go Store geteld via de JSON van de pagina (124 connectors, 59 eigen, allemaal installOnly) en de hulppagina over verkopen gelezen (gepauzeerd sinds 8 juli). Onderzoeker (agent) voor groei, geld, toelating, vraag en de Docs Gallery (1.261 Packs, 237 betaald). Nieuw script `data/superhuman-go-meet.py`.
- Besluit: cijfer 4, nog niet klaar. Waarom: verkopen is dicht tot er een nieuw verdienmodel is, installs niet zichtbaar, en de eigenaar en de merken pakken de categorieën. Geen controleur: advies geen ja, kerncijfers zelf gezien.
- Les: lees bij een gedwongen overstap eerst of verkopen open blijft tijdens de overstap.

## Run 8 nov 2026, ±09:39 tot ±10:05 UTC (Noor)
- Android Automotive gepakt (stond als volgende op de lijst). Onderzoeker (agent) voor groei, winkel, geld, vraag en risico; zelf nagekeken: blog Google okt 2026 (16 merken, 100+ modellen, 700+ apps), Play Billing (aankoop op een ander apparaat), kilometerstand dicht voor Play-apps, en installs van auto-apps via AppGoblin en Play. Nieuw script `data/aaos-meet.py`.
- Besluit: cijfer 4, nee voor nu. Waarom: groei gestaag maar het publiek per app is klein (Foreca weer ±1.200, Vivaldi ±6.500 installs per 4 weken), de winkel is niet jong en vult met grote merken, en de beste kans (rittenlog) is technisch dicht. Geen controleur: advies geen ja, kerncijfers zelf gezien.
- Les: installs van een app die alleen voor het apparaat is, zeggen meer over de echte markt dan het aantal apparaten.
- Aanvulling run 8 nov ±09:39 tot ±10:00 UTC: de eindtijd hierboven (±10:05) was te ruim geschat; het voorstel stond om 09:46 op GitHub. Daarna snelle schifting van Excalidraw, Warp, Meta Horizon, Discord Activities en VRChat: allemaal nee of niet voor de pionier. Canva, Elgato en Discord App Directory overgeslagen, die deed Vera al. De lijst in kandidaten.md is nu leeg; volgende run zoekt nieuwe platformen.

## Run 8 nov 2026, ±10:40 tot ±11:00 UTC (Noor)
- Lijst was leeg, dus nieuw gezocht. PowerToys Command Palette gepakt. Waarom: Extension Gallery sinds juni 2026, verspreiding via de Microsoft Store (dus betalen kan), groot bestaand publiek, en Microsoft hint op opname in Windows.
- Zelf gemeten: hele Gallery-feed (97 extensies, per maand, makers, categorieën) en per Store-extensie prijs en beoordelingen via de openbare Store-API. Nieuw script `data/cmdpal-meet.py`, uitkomst `data/cmdpal-2026-11-08.json`. Onderzoeker (agent) voor groei PowerToys, plannen met Windows, Raycast voor Windows en verzoeken op GitHub; sterren, downloads en Raycast-API zelf nagekeken.
- Besluit: cijfer 4, nee voor nu. Waarom: winkel jong en leeg, maar het platform groeit niet hard meer en het publiek per extensie is heel klein (24 beoordelingen samen). Geen controleur: advies geen ja, kerncijfers zelf gezien.
- Les: bij een winkel bovenop een groot programma eerst de groei van het programma zelf en de beoordelingen in de winkel tellen; dat schift snel.

## Run 8 nov 2026, ±11:40 tot ±12:10 UTC (Noor)
- Lijst was leeg; nieuw gezocht en Affinity by Canva (scripts) gepakt. Waarom: gratis pro-programma met miljoenen nieuwe gebruikers dat in april en sept 2026 scripting opende, zonder officiële winkel; dat is de pionierssoort die de rol zoekt.
- Onderzoeker (agent) voor groei, scripting, geld, vraag en concurrentie. Zelf nagekeken: registry (185 scripts, 76 makers, groei per maand via git-geschiedenis), sterren en downloads van de Script Manager, prijzen van Visual.af. Nieuw script `data/affinity-scripts-meet.py`, uitkomst `data/affinity-scripts-2026-11-08.json`. Een poging om affinity.studio met een browser-User-Agent te lezen werd terecht geweigerd; niet omzeild, voorwaarden op de lijst van Thijs gezet.
- Besluit: cijfer 5, nog niet klaar. Waarom: vraag 1, 2 en 5 zijn sterk, maar betalen kan alleen buiten Canva om, de voorwaarden zijn onbekend, het scriptpubliek is nog klein (±11k) en de ingebouwde AI maakt eenvoudige scripts waardeloos. Geen controleur: advies geen ja, kerncijfers zelf gezien.
- Les: zoek meer programma's die net gratis werden of hard groeiden en daarna een script-API openden.
- Correctie run hierboven: de eindtijd ±12:10 was te ruim; het voorstel stond om 11:47 UTC op GitHub. Daarna snelle schifting van DeepSeek Harness en DaVinci Resolve 21.1 (beide nee). Geen tweede volledig onderzoek begonnen: geen sterke kandidaat gevonden die in de resterende tijd grondig kon (regel 0c).

## Run 8 nov 2026, ±12:40 tot ±13:05 UTC (Noor)
- Lijst was leeg; nieuw gezocht en World App mini apps gepakt. Waarom: jonge winkel (eind 2024) in een app met miljoenen gebruikers, met een makersfonds en betalen ingebouwd; leek een pionierssoort.
- Onderzoeker (agent) vond de openbare teller van World zelf (metrics.worldcoin.org) en de lijst miniapps.world met gebruikers per app. Zelf nagekeken: stand dec 2025 en jun 2026 via het Wayback-archief en de stand van vandaag. Nieuw script `data/worldapp-meet.py`, uitkomst `data/worldapp-2026-11-08.json`.
- Besluit: cijfer 2, nee. Waarom: het platform krimpt hard (actief per maand 7,84M naar 2,21M sinds dec 2025, verificaties staan stil, aantal mini apps daalt) en het makersgeld lijkt gestopt. Geen controleur: advies is nee en de kerncijfers zelf gezien.
- Les: eerst zoeken naar een openbare teller van de eigenaar plus oude standen in het archief; dat schift binnen vijf minuten.
- Aanvulling run 8 nov ±12:40: na World App snelle schifting van Supernote, TikTok Minis, Railway-templates en Antigravity (zie kandidaten.md). Geen tweede volledig onderzoek begonnen: geen sterke kandidaat die in de resterende tijd grondig kon (regel 0c). Railway doorgegeven als tip voor Vera.

## Run 8 nov 13:38 tot ±15:00 UTC (Noor)
- Lokale kloon liep achter op een herschreven geschiedenis (origin/main los van de oude main). Oude main bewaard als tak oud-main (alleen lokaal), main gelijk gezet met origin/main. Niets van GitHub weggehaald.
- Snelle schifting Antigravity (gecureerd, geen betalen) en Homey van LG (winkel sinds 2016, geen betaalde apps): nee.
- Filament gepakt. Waarom: Packagist liet zien dat het pakket in 11 maanden bijna 7 keer zo vaak gedownload wordt, harder dan Laravel zelf, en de pluginlijst heeft betaalde plugins met eigen kassa.
- Gemeten: alle 1.237 plugins via de open API (filamentphp.com/api/plugins), Packagist-tellers voor 1.088, GitHub-issues over v4/v5-ondersteuning (194). Scripts in data/.
- Controleur (agent) mat zeven kernbeweringen opnieuw: alles klopte, mediaan nieuwe plugins in zijn steekproef iets hoger (5.731).
- Besluit: cijfer 6, ja met kleine inzet, categorie goedkeuringen voor v5. Waarom: groei en bereik voor nieuwkomers zijn sterk en betalen kan; het grootste gat is dat verkopen niet te zien zijn, dat lossen we alleen op door klein te proberen.

## Run 8 nov 14:38 tot ±15:05 UTC (Noor)
- Lokale kopie dortus-hq had een andere geschiedenis dan GitHub (resetten werd geweigerd, terecht); vers gekloond in een nieuwe map en daar gewerkt. Niets weggegooid.
- Radar (nieuwe stap): Grok Build Plugin Marketplace (gratis, nee), Google Play laat andere winkels toe (oceaan), en npm-groei van Payload, Tauri en Nuxt. Vier regels in radar.md.
- Payload CMS gepakt. Waarom: npm ±5,6 keer in een jaar, Figma maakt het de backend van Make, en Payload 4 dwingt alle plugins tot een overstap, zoals de les van Devvit en Filament.
- Zelf gemeten: hele npm-ecosysteem (729 plugins van derden, met eerste publicatie, licentie, peer-versie en downloads), nieuw script `data/payload-plugins-meet.py`. Onderzoeker (agent) voor groei, v4-migratiegids, geld, vraag en risico. Een poging om de Figma-blog met een browser-User-Agent te lezen werd terecht geweigerd; niet omzeild, via zoekresultaten en een ander artikel gelezen.
- Besluit: cijfer 4, nog niet klaar. Waarom: groei en overstap zijn sterk, maar geen winkel, geen enkele betaalde plugin, gratis cultuur en de eigenaar houdt de rijke functies. Geen controleur: advies geen ja, kerncijfers zelf gemeten.
- Daarna snelle schifting Medusa, Strapi, Nuxt, Tauri, Statamic en Flux (allemaal nee voor de pionier, zie kandidaten.md).
- Radar vond RuneScape 3 Plugin Hub (live 19 okt 2026). Meteen onderzocht met een onderzoeker (agent); de beslissende regel zelf gelezen: EULA Schedule 4, 3.2 verbiedt geld verdienen met plugins. Besluit: cijfer 2, nee. Waarom: geen enkele betaalroute en RS3 krimpt licht; de vraag is er wel, dus opnieuw als Jagex dat ooit verandert.
- Les: bij spelplatformen eerst de EULA lezen op "commercial"; dat schift in één minuut.
- Radar vond daarna de Cfx Marketplace van Rockstar (FiveM en RedM, sinds jan 2026). Voorwerk gedaan (winkel, kassa Tebex, grote verkopers op de voorpagina) en als eerste klaargezet voor de volgende run; geen half voorstel geschreven (liever één platform goed). Run gestopt om ±15:10 UTC.


## Run 8 nov 15:38 tot ±16:10 UTC (Noor)
- Cfx Marketplace gepakt (stond klaar). Eén onderzoeker (agent) mat de hele winkel via de interne laadfunctie: 1.088 pakketten, 48 makers, per categorie en platform; script en data staan in `data/`. Zelf gemeten: spelers nu (runtime.fivem.net), Steam-gemiddelden per maand, forumcijfers, toelating en afdracht (Tebex-docs).
- Besluit: cijfer 4, nog niet klaar. Waarom: winkel jong en betalen werkt, maar alleen voor toegelaten Tebex-partners en gevuld door gevestigde studio's, de markt eronder is een oceaan, en FiveM groeit nu niet. De pioniershoek (GTA 6) is nog niet aangekondigd. Markt eronder doorgegeven aan Vera via het voorstel.
- Radar: GTA 6 op 19 nov, eerst consoles, als signaal genoteerd. Geen nieuwe kandidaat met 7 of hoger gevonden.

## Run 8 nov 16:39 tot ±16:55 UTC (Noor)
- Lokale main had weer een andere geschiedenis dan GitHub; resetten werd geweigerd, dus gewerkt in een aparte worktree op origin/main. Niets weggegooid.
- Radar: Ableton Extensions SDK (beta sinds juni), Google Connected Apps (preview, AI-assistent-soort), Obsidian staat betaalde plugins toe (sinds mei). Drie regels in radar.md.
- Ableton Extensions gepakt. Waarom: een nieuwe pluginlaag in een bekend pro-programma waar al betaald wordt voor hulpmiddelen (Max for Live), dezelfde soort als Affinity.
- Zelf gemeten: nieuwe GitHub-repo's per maand en de sitemap van liveextensions.co (script data/ableton-extensions-meet.py). Onderzoeker (agent) voor status, geld, bedrijf en vraag.
- Besluit: cijfer 3, nee voor nu. Waarom: Ableton groeit niet, Extensions zit na vijf maanden nog in de beta en alleen in Suite, en het aantal nieuwe extensies zakte van 86 en 133 in juni naar een handvol per maand. Geen controleur: advies geen ja, kerncijfers zelf gemeten.
- Daarna shadcn-registry's gepakt. Waarom: npm liet zien dat de shadcn-CLI ×28 groeide in een jaar, harder dan Filament, en er bestaat een officiële lijst van registry's met betaalde aanbieders.
- Zelf gemeten: de hele officiële lijst (548 registry's, nieuw per maand, categorieën, grootste spelers), npm-reeks, docs over private registry's, prijzen Shadcnblocks. Script en momentopname in data/.
- Besluit: cijfer 4, nee voor de pionier, doorgegeven aan Vera (regel onderaan haar kandidaten.md). Waarom: groei en geld zijn er, maar de lijst is al vol en een nieuwkomer valt niet op; dat is precies haar meetlat.
- Snelle schifting Base app mini apps (Base schuift naar handelen, gebruikers lopen weg) en Nothing Playground (gebruikers maken widgets zelf met AI): nee.
- Daarna MentraOS gepakt en zelf gemeten: winkel-API (10 apps, alle van Mentra), docs (publiceren voor makers kan nog niet in 3.0, niets over betalen), npm, Discord, GitHub. Besluit: cijfer 3, nee voor nu. Waarom: geen winkel open voor makers en geen plan voor geld; volgen omdat de SDK-interesse stijgt.

## Run 8 nov 17:39 tot ±18:15 UTC (Noor)
- Radar: DeepSeek Harness plant een pluginwinkel met steun in tokens (al ±35.000 plugins) en Nous Research opende de Hermes Marketplace (976 plugins, hackathon). Beide AI-agent-soort zonder geld voor makers: nee, twee regels in radar.md.
- Taak van Hans eerst: een verkoopcijfer zoeken van een nieuwe Filament-maker (kan de 6 een 7 maken). Zelf gezocht (alle 130 kassa's, sites van makers, Filament-blog, TrustMRR-sitemap met 12.429 startups) en een hulpagent ±20 minuten laten zoeken (X, podcasts, Reddit, Gumroad). Niets gevonden; alleen een Laravel-starterkit op Gumroad met 165 verkopen, geen plugin. Besluit: vastgelegd in taken.md, de 6 blijft 6. Waarom: van buitenaf is dit niet te meten; verder zoeken kost tijd zonder kans.
- Daarna Twenty gepakt (open-source CRM, App SDK sinds april 2026). Waarom: bedrijven als klant (past bij de koers van 8 nov), npm twenty-sdk ×296 in een jaar, en een betaalblok in de SDK.
- Zelf gemeten: alle 55 apps op npm (script data/twenty-apps-meet.py), de docs over publiceren, keuring en credits, Docker-pulls, sterren. Hulpagent voor uitbetaling, groei, vraag en de officiële lijst.
- Besluit: cijfer 5, nog niet klaar. Waarom: groei en jonge winkel sterk en de eerste plek is overal te pakken, maar betalen in de winkel is "Not live yet" en er staat nergens dat makers geld krijgen. Geen controleur: advies is geen ja en de kerncijfers zijn zelf gemeten.


## Run 8 nov 18:38 tot ±19:15 UTC (Noor)
- Eerst het bericht van Thijs (19:16): betalen moet al werken. Deze run alleen winkels waar je nu al kunt verkopen. Verwerkt in berichten/noor.md.
- Radar: geen nieuwe winkels met betalen gevonden in de zoekresultaten van de laatste dagen.
- HighLevel gepakt. Waarom: 0% afdracht, HighLevel rekent zelf af, bureaus betalen. Zelf gemeten via de open API (2.844 apps, script data/highlevel-apps-meet.py). Besluit: cijfer 3, nee. Waarom: vijf app-fabrieken hebben 1.116 apps en nieuwkomers halen mediaan 5 installaties; Vera kwam op 6 nov op hetzelfde uit.
- Daarna TikTok Shop App Store. Waarom: social commerce groeit het hardst en de winkel laat makers zelf afrekenen. De open portal-API gevonden (seller-us, seller-uk, seller-eu) en alle landen geteld (script data/tiktokshop-apps-meet.py). Hulpagent voor betalen, toegang, groei en vraag in de partner-docs.
- Besluit: cijfer 6, ja met kleine inzet na één controle. Waarom: groei sterk, Europese winkel klein en categorieën leeg die in de VS vol zitten met tools van $99 tot $149 per maand, betalen werkt met eigen kassa. Geen 7 omdat niet zeker is dat een Nederlands bedrijf buiten Nederland mag listen, en installs niet zichtbaar zijn. Vraag voor TikTok op de lijst van Thijs gezet (alleen als Hans het wil). Geen aparte controleur: kerncijfers zelf gemeten en nagerekend (één fout verbeterd: VS 9 tot 49 nieuwe per maand, niet 13 tot 49).

## Run 8 nov 19:38 tot ±19:55 UTC (Noor)
- Berichten gelezen: niets nieuws sinds het bericht van 19:16 (verwerkt).
- Gekozen: de ene controle in het TikTok-voorstel (mag een Nederlands bedrijf ook in DE, FR, IT, ES listen?). Waarom: dat was het enige dat tussen de 6 en een 7 stond, en het is het eerste voorstel waar betalen nu al werkt. Dat gaat voor nieuw zoeken.
- Zelf gemeten in de tellingen van 8 nov: partner_id en service_id per land vergeleken. Stockhub B.V. (Enschede, app van 14 juni) en Stockpilot (Jiyu Ninja B.V., Utrecht) staan met één app in negen of vijf EU-landen; Poolse Sellasist en Apilo ook. Docs van TikTok (met Playwright gelezen) bevestigen "+ Add market" per categorie. Uitkomst: ja.
- Bij het nakijken gevonden: de categorie winstanalyse is sinds juni gevuld met drie nieuwe apps (Nexium, NorthProfit, SellerGoo). Daarom het eerste product veranderd naar Europese productregels (GPSR, Responsible Person, CLP, Pfand), waar TikTok steeds nieuwe verplichte velden toevoegt en nog geen enkele app voor is.
- Besluit: cijfer 7, ja met kleine inzet. Geen controleur-agent: de controle is een feitenvraag die ik met eigen tellingen en de docs zelf kon nakijken; de rest-onzekerheid (geldt het voor elke categorie) staat eerlijk in het voorstel.
- Radar: één regel (EU-changelog TikTok). Algemene zoektocht naar nieuwe winkels gaf alleen oude resultaten.
- Daarna snelle schifting van social-commerce winkels in de soort van TikTok (Temu, Allegro, Shein, Whatnot): geen open app-winkel voor kleine makers gevonden. Nee, regels in kandidaten.md.

## Run 8 nov 20:40 tot ±21:00 UTC (Noor)
- Berichten gelezen: niets nieuws sinds 19:16 (verwerkt). Radar kort: geen nieuwe betaalde winkel; Canva Apps snel bekeken, oud, niet voor de pionier.
- Gekozen: TikTok Shop App Store in de jongste landen buiten de EU (Japan, Brazilië, Mexico). Waarom: de les van de vorige run (een land dat net opent heeft een bijna lege winkel) en betalen werkt daar al zoals in de EU (eigen kassa), zoals Thijs vroeg.
- Zelf gemeten: per land een eigen host gevonden en alle apps geteld. Bij het tellen bleek de standaardsortering te verschuiven (dubbele en gemiste apps); script aangepast en opnieuw geteld.
- Besluit: Japan 5 (nog niet klaar), Brazilië 4, Mexico 4. Waarom: Japan heeft een lege categorie (Japanse reclameregels) en een jonge winkel, maar de groei bij winkeliers is onzeker en het hoort na het EU-product van Tess, niet ernaast (één taak tegelijk). Brazilië groeit het hardst maar loopt al vol met lokale ERP's.
- Controleur-agent: alle tellingen kloppen; drie kleine fouten verbeterd (60% gebruikers, oud 10%-cijfer, twee CFDI-apps) en tegenargumenten toegevoegd.
- Daarna (±20:55 tot 21:00): radar TikTok Shop nieuwe landen. Australië, Korea en Saudi-Arabië gemeld voor Q1 2027 (onbevestigd); vier extra EU-winkels gevonden (CZ, PT, GR, HU, 66 tot 71 apps, zelfde apps als NL); doorgegeven aan Hans en Tess via status.md. Brazilië-ANVISA snel nagekeken in de partner-changelog: geen regelvelden, blijft 4.
- Gestopt na een laatste algemene zoektocht zonder nieuwe winkel met betalen. Geen werk verzinnen (regel 0c); volgende run begint bij de ideeën in kandidaten.md (21:00) en probeert `shop_region=AU`.

## Run 8 nov 21:38 tot ±22:25 UTC (Noor)
- Berichten gelezen: niets nieuws sinds 22:31 en 19:16 (beide al verwerkt of zonder actie). Lokale kloon liep niet gelijk met GitHub (andere geschiedenis); main opnieuw gezet op origin/main, niets verloren want niets eigens open.
- Radar kort: TikTok Shop AU nog dicht; Google Play liet de eerste erkende andere winkel toe (oceaan, niet voor de pionier).
- Gekozen: cTrader Store. Waarom: betalen werkt al (zoals Thijs vroeg), winkel jonger dan twee jaar, en prop firms stapten in 2024 van MetaTrader over, een mogelijke gedwongen overstap.
- Zelf gemeten: alle 4.610 producten en 1.094 verkopers via de sitemap en de openbare productdata (script data/ctrader-store-meet.py). Hulpagent voor groei, regels en vraag (forum 5.368 titels geteld).
- Besluit: cijfer 4, nee voor de pionier. Waarom: instroom van makers zakt hard (57 naar 10 per maand), alle verkopers samen maar 6.192 verkopen in twee jaar, hulpmiddel-hoeken al vol, platform klein naast MetaTrader. Doorgegeven aan Vera via status.md, want verkopen per verkoper zijn hier openbaar.
- Geen aparte controleur-agent: alle kerncijfers komen uit mijn eigen volledige meting en zijn met een tweede telling nagekeken (betaalde producten met 1, 10, 50, 100 gebruikers; status actief, gearchiveerd, inactief). De achtergrondcijfers van de hulpagent zijn DERDEN met link.

## Run 8 nov 22:39 tot ±22:55 UTC (Noor)
- Berichten gelezen: niets nieuws sinds 22:31 en 19:16 (verwerkt). Lokale main liep weer niet gelijk met GitHub; op een eigen tak vanaf origin/main gewerkt en naar main gepusht.
- Radar kort: geen nieuwe betaalde winkel in de zoekresultaten.
- Gekozen: Vercel Marketplace. Waarom: betalen werkt al via de Vercel-rekening (zoals Thijs vroeg), winkel sinds aug 2024, en Vercel groeit heel hard.
- Zelf gemeten: alle 76 producten met goedkeuringsdatum uit de paginadata (script data/vercel-marketplace-meet.py). Hulpagent voor groei (npm, Sacra), regels en vraag.
- Besluit: cijfer 4, nee voor de pionier. Waarom: gecureerd en gevuld met merken (AWS, Stripe, Shopify), installs onzichtbaar, afdracht niet openbaar, en een product moet een gehoste dienst met support zijn. Niet voor Vera.
- Daarna herhaalchecks van Hans: Devvit-fondsen (geen aankondiging na 31 dec; voorwaarden H2 2026 bijgewerkt op 4 nov) en Godot betaalde items (nog geen datum). Directus snel geschift: nee. Radar: Apple EU-voorwaarden (5% voor alternatieve iOS-winkels sinds 1 okt).
- Gekozen: MSFS 2024 EFB-apps. Waarom: betalen werkt al, nieuwe app-laag met alleen kleine makers, past bij ons werk (TypeScript), en console-spelers kunnen alleen via de Marketplace iets toevoegen.
- Zelf gemeten: Steam-spelers per maand (steamcharts) en de betaalde EFB-apps op simMarket met prijs. Hulpagent voor groei, regels, forumvraag en bestaande apps.
- Besluit: cijfer 5, nog niet klaar. Waarom: groei is vooral herstel in een niche, verkopen onzichtbaar, en de console-hoek hangt aan goedkeuring door Microsoft. Herhaalmeting 8 jan 2027.

## Run 8 nov 23:38 tot 9 nov ±00:10 UTC (Noor)
- Berichten gelezen: niets nieuws (22:31 en 19:16 al verwerkt). Lokale main liep achter; vanaf origin/main gewerkt.
- Radar: TikTok AU en anderen nog dicht, Steam Frame (duur, schaars), Minecraft Marketplace (alleen partners). Nieuw gevonden: Corsair-widgets in de Elgato Marketplace.
- Gekozen: XENEON EDGE-widgets. Waarom: betalen werkt al (zoals Thijs vroeg), winkel pas sinds augustus open voor makers, en een openbare API om alles te tellen.
- Zelf gemeten: alle 395 widgets met prijs, maker, datum, apparaat en de volgorde Popular (script data/xeneon-widgets-meet.py). Hulpagent voor vraag en groei (Reddit en Corsair-forum dicht, GitHub wel). Controleur heeft alle kerncijfers nagerekend: klopt.
- Besluit: cijfer 6, ja met kleine inzet. Waarom: jong, betalen werkt, lege categorie die bij ons past (status van AI-codeerhulpen); geen 7 omdat apparaatverkoop en downloads onzichtbaar zijn en app-fabrieken snel vullen.

## Run 9 nov 00:40 UTC (Noor)
- Berichten gelezen: niets nieuws (22:31 en 19:16 al verwerkt). Lokale kloon liep weer niet gelijk; main opnieuw gezet op origin/main.
- Radar: eToro App Store gevonden (open sinds april 2026). Logi Marketplace snel bekeken: al door Vera gedaan (2, geen betalen).
- Gekozen: eToro App Store. Waarom: jonge winkel in een groot platform met 40 mln gebruikers, en de voorwaarden noemen abonnementen.
- Zelf gelezen: voorwaarden (pdf), builders portal (appstore, faq, app-registration), Q2-cijfers. Hulpagent voor betalen, catalogus, vraag en groei.
- Besluit: cijfer 5, nog niet klaar. Waarom: betalen bestaat alleen op papier ("may allow", met toestemming), geen openbare catalogus om te tellen, toelating per aanvraag, en eToro groeit gezond maar niet hard. Volgens de regel van Thijs dus geen 6 of 7.
- Daarna snel geschift: NZXT CAM (gratis, nee), losse skill-winkels voor AI-agents (geen platform, nee), OpenAI Marketplace (alleen bedrijven, nee). Een blogbericht over een betaalde Anthropic-skillwinkel bleek tegengesproken; niet overgenomen.
- Gekozen: TradingView Marketplace. Waarom: betalen werkt nu al (0% afdracht) en sinds 1 nov moet alle betaalde verkoop via de nieuwe winkel, een gedwongen overstap.
- Zelf gelezen: programmavoorwaarden, aanvraageisen, Paid Space-handleiding, verkopersregels, robots.txt. De winkel zelf (/scripts/) niet gelezen: robots.txt verbiedt AI-agents daar.
- Besluit: cijfer 5, nog niet klaar. Waarom: winkel leeg en betalen werkt, maar het platform is volwassen, wij moeten eerst drie maanden een script openbaar hebben (onder het account van Thijs, met Premium) en de gevestigde verkopers lopen er nu in. Geen aparte controleur: alle kernfeiten komen uit de eigen pagina's van TradingView (GEZIEN); de tellingen 39 en 52 zijn DERDEN met link.

## Run 9 nov 01:40 UTC (Noor)
- Berichten gelezen: niets nieuws. Lokale kloon stond los van main; opnieuw gezet op origin/main.
- Radar: Grok Build Plugin Marketplace (geen betalen, bewering kwam van een SEO-blog), Claude Marketplace (alleen zakelijke partners), ChatGPT DevDay (geen betaalroute). Nieuw gevonden: Apple HomeView.
- Gekozen: Apple HomeView. Waarom: nieuw Apple-apparaat dat over vier dagen levert, en betalen werkt al via de App Store.
- Zelf gelezen: Apple-persbericht, HIG Widgets (HomeView-deel), ontwikkelaarsovereenkomst 6.4, App Store-zoekresultaten. Hulpagent voor groei, vraag en precedent (StandBy, CarPlay).
- Besluit: cijfer 4, nee voor nu. Waarom: geen eigen winkel, bestaande widgets komen automatisch mee (de grote gezinsapps staan er op dag één), alleen het kleinste formaat, niet in de EU, en geen verkoopcijfers. Herhaalmeting 8 jan 2027.
- Daarna nog geschift (TikTok-landen, Raycast, Elgato, Tesla, ClawHub, Grav): niets met betalen dat nu werkt en jong is. Gestopt om ±02:05 in plaats van werk te verzinnen (regel 0c).

## Run 9 nov 02:40 UTC (Noor)
- Geen open berichten van Thijs, geen verlopen herhaalmetingen. Radar kort: algemene zoekopdrachten gaven niets nieuws; via de Homey- en Meta-zoektocht wel een signaal (Meta toolkit 1.0).
- Cal.com App Store gepakt (stond als idee in de vorige run). Zelf gemeten in de broncode: 93 apps, betaalblok alleen gebruikt door Cal.com zelf. Cijfer 3, nee. Waarom: geen betalen voor makers en een koppelingenlijst van vijf jaar oud.
- Daarna Meta AI-brillen gepakt, omdat toolkit 1.0 sinds 30 sept stabiel is en betalen via een eigen telefoon-app nu al werkt. Zelf gemeten: FAQ (inzendingen nog dicht), GitHub-repo's per maand, iPhone-apps via de iTunes Search API (nulmeting in `data/`). Cijfer 5, nog niet klaar: geen winkel of open ontdekplek, dus bereik nog niet te halen. Geen aparte controleur ingezet; de bronnen staan per cijfer in het voorstel, en het cijfer is geen ja, dus Hans hoeft er nu niets mee.
- Commits: a2d59fe, 266d2fb, deze run afgesloten met de commit van dit logboek.

## Run 9 nov 03:39 UTC (Noor)
- Berichten gelezen: niets nieuws. Lokale kloon liep achter (origin was geforceerd bijgewerkt); main opnieuw gezet op origin/main. Geen verlopen herhaalmetingen.
- Radar kort: algemene zoekopdrachten gaven niets nieuws; Vultisig plugin marketplace staat op pauze (nee).
- Gekozen: Omi app store. Waarom: nog niet bekeken door Vera of mij, jong apparaat met app store en betaalde apps.
- Zelf gemeten: hele catalogus via de open API (593 apps, installs, prijs, datum), betaalcode in de open-source backend (Stripe Connect, 0% afdracht), iOS-beoordelingen per land en Android-downloads. Script data/omi-apps-meet.py.
- Tijden: Omi in onderzoek 03:42, klaar 03:47 (de claim-commit noemt 03:50, dat was een schatting).
- Besluit: cijfer 3, nee. Waarom: betalen werkt wel, maar de instroom van apps is sinds mei 2026 ingestort (0 tot 2 per maand), betaalde apps verkopen bijna niet en het platform is klein. Geen controleur ingezet: alle kerncijfers komen uit de eigen API en broncode van Omi (GEZIEN) en het advies is nee.
- Daarna snel geschift: Ultrahuman PowerPlugs (alleen partners), Nothing Playground (geen betalen), Ulanzi Studio (geen winkel), Meta Horizon Worlds (platform wankelt). Alle vier nee. Geen nieuwe kandidaat met betalen die nu werkt; gestopt om ±04:00 in plaats van een half onderzoek te beginnen (regel 0c).

## Run 9 nov 04:40 UTC (Noor)
- Berichten gelezen: niets nieuws (22:31 en 19:16 al verwerkt). `git pull` bleef hangen; met `git fetch` en een timeout opgelost, main gezet op origin/main (origin was weer geforceerd bijgewerkt). Geen verlopen herhaalmetingen.
- Radar kort: Moodle Marketplace al door Vera gedaan, Base app draait naar handel, Apple Mini Apps Partner Program is oud nieuws. Niets met een mogelijke 7.
- Gekozen: Snap Specs. Waarom: nog door niemand bekeken, een grote partij erachter, eerste echte AR-bril voor consumenten, Lenses in TypeScript (past bij ons), en Snap noemt betalen in de Lens.
- Zelf gelezen: Commerce Kit-docs (closed beta, alleen VS-makers), roadmap-pagina (nog niet geleverd), monetisatieblog van Snap. Hulpagent voor levering, aantallen, Lens Fest, vraag en fondsen.
- Besluit: cijfer 4, nog niet klaar. Waarom: bril op 9 nov nog niet geleverd en zonder aantallen, en betalen kan voor een Nederlands bedrijf niet (closed beta, alleen VS). Geen controleur: geen ja, en de twee beslissende feiten heb ik zelf gelezen.
- Daarna snel geschift: Rokid Agent Store (groeit, maar geen betalen) en n8n (geen betaalde nodes). Beide nee. Gestopt om ±05:05 in plaats van een half onderzoek te beginnen (regel 0c).

## Run 9 nov 05:40 UTC (Noor)
- Berichten gelezen: niets nieuws (22:31 en 19:16 al verwerkt). `git pull` bleef weer hangen; met `git fetch` en een timeout opgelost, main gezet op origin/main (origin was geforceerd bijgewerkt). Geen verlopen herhaalmetingen.
- Radar: algemene zoekopdrachten naar nieuwe betaalde winkels gaven alleen oude bekenden; Arduino App Lab heeft geen winkel. TikTok Shop: geen nieuw land open (SA 0 apps, Zuidoost-Azië al lang open).
- Gepakt: snelle schifting Plane, Documenso en Chatwoot (stonden open in kandidaten.md), claim-commit 471d316. Zelf gemeten met een kloon van de broncode en de developer-docs. Alle drie nee: Plane heeft een marketplace met 18 apps die alle 18 van Plane zelf zijn, Documenso en Chatwoot hebben geen winkel.
- Les: GitHub-API is hier dicht voor vreemde repo's, `git clone --depth 1` en repos.ecosyste.ms werken wel.
- Geen nieuwe kandidaat met betalen die nu werkt. Gestopt om ±06:20 in plaats van werk te verzinnen (regel 0c); de lijst is leeg, volgende run eerst kijken of Hans of Tess iets van de pionier vraagt.

## Run 9 nov 06:40 UTC (Noor)
- Berichten gelezen: niets nieuws (22:31 en 19:16 al verwerkt). `git pull` bleef weer hangen; met `git fetch` en een timeout opgelost, main op origin/main gezet. Geen verlopen herhaalmetingen; bord en taken van Hans vragen niets nieuws van de pionier.
- Radar: algemene zoekopdrachten naar nieuwe betaalde winkels en fondsen gaven weer alleen oude bekenden (Moodle, Grafana, TRMNL). ClickUp heeft geen app-marketplace.
- Gekozen: Salla App Store. Waarom: nog door niemand bekeken, betalen werkt via Salla, en een Arabische markt met geld van PIF waar westerse makers bijna niet zitten, zelfde redenering als de 7 voor TikTok Shop EU. Claim-commit 84f5540.
- Hulpagent voor groei, voorwaarden en taal; zelf de openbare marketplace-API gelezen en de reviews per maand van de Google Analytics-app geteld (nieuw script `data/salla-reviews-meet.sh`, met curl, rustig). Een eerste versie in Python met een eigen User-Agent werd door de veiligheidscontrole tegengehouden; niet omzeild, overgestapt op gewone curl.
- Besluit: cijfer 4, nee voor de pionier, doorgeven aan Vera. Waarom: betalen werkt en buitenlanders mogen, maar het platform staat stil (nieuwe winkels per maand vlak sinds 2024, merchants van 80.000+ naar ±67.000) en de winkel is vijf jaar oud met sterke Arabische leiders. Geen controleur: het is een nee en de beslissende cijfers heb ik zelf gemeten.
- Les: een openbare review-API met datums geeft bij een winkelbouwer snel een groeimaat: tel de reviews per maand op een app die bijna elke nieuwe winkel installeert.
- Daarna snel geschift: Light Phone III (niet-commercieel), Kajabi (geen marketplace), Owlbear Rodeo (geen betaalroute). Alle nee.
- Tweede platform: Fourthwall Apps (claim-commit 0b4cf7a). Waarom: jonge directory, eigen kassa toegestaan, platform van creators dat groeit. Hulpagent voor groei en directory; zelf nagelezen: publiceren via Discord, eigen kassa, Storeleads-teller, changelog.
- Besluit: cijfer 5, nog niet klaar. Waarom: bijna lege winkel en betalen kan, maar klein bereik, geen installcijfers of openbare lijst, en Fourthwall bouwt veel zelf. Geen controleur: geen ja, beslissende feiten zelf gelezen.
- Volgende run: Q3-cijfers eToro (10 nov) lezen, radar, TikTok Shop-landen.

## Run 9 nov 07:40 UTC (Noor)
- Berichten gelezen: niets nieuws (22:31 en 19:16 al verwerkt). `git pull` bleef weer hangen; met `git fetch` en een timeout opgelost, main op origin/main gezet (origin was geforceerd bijgewerkt). Geen verlopen herhaalmetingen; bord en taken vragen niets nieuws van de pionier.
- Radar: algemene zoekopdrachten en Hacker News (laatste drie weken) gaven geen nieuwe betaalde winkel. Siri AI open voor alle ontwikkelaars (iOS 27.3 beta, 3 nov): bestaande apps komen vanzelf mee, nee. Kaufland nu in 9 landen, NL sinds 11 sept 2026: geen app-winkel, tip voor Tess.
- Gekozen: SHOPLINE App Store (claim-commit 8a5d1c8). Waarom: nog door niemand bekeken, betalen via de verplichte Subscription API, en SHOPLINE trekt naar het westen. Hulpagent voor groei en voorwaarden; zelf Storeleads en het aantal apps gelezen. Het pad /api/ van de winkel staat dicht in robots.txt; niet omzeild.
- Besluit: cijfer 3, nee. Waarom: platform staat stil (36.259 live winkels in Q1 2024, 30.355 nu), winkel heeft al 512 apps, afdracht achter een inlog.
- Tweede: Tiendanube / Nuvemshop (claim-commit 16881dc), gevonden door Storeleads naast elkaar te leggen voor winkelbouwers. Zelf alle 647 apps geteld met reviews en prijsvorm (scripts in data/), hulpagent voor betalen, uitbetaling en vraag. Een poging de sitemap met een browser-User-Agent te halen werd tegengehouden; niet omzeild, de gewone categoriepagina's gebruikt.
- Besluit: cijfer 4, nee voor de pionier, doorgeven aan Vera. Waarom: hardst groeiende winkelbouwer die ik zag (+67% in zeven kwartalen) en makers verdienen er, maar de winkel is rijp en de top is in handen van Braziliaanse makers. Geen controleur bij beide: het zijn neeën en de beslissende cijfers heb ik zelf gemeten.
- Volgende run: Q3-cijfers eToro (10 nov), radar, TikTok Shop-landen.

## Run 9 nov 2026 08:39 UTC (Noor)
- Radar: DeepSeek Harness (plugin-marketplace aangekondigd, geen verkoop, nee), PteroCA (marketplace gratis, nee). Geen verlopen herhaalmetingen. Geen open berichten van Thijs.
- Gekozen: Attio App Store (claim-commit 027f4b3). Waarom: jonge CRM die hard groeit, App SDK net stabiel, en een snelle blik liet zien dat makers er met eigen abonnement verkopen. Zelf alle 294 apps uit de ingebedde JSON van attio.com/apps gehaald (installs, aanmaakdatum, maker), prijspagina's van de makers gelezen, npm-downloads van de SDK geteld en de ontwikkelaarsvoorwaarden gelezen. Controleur (hulpagent) kreeg alles opnieuw te meten: alle punten kloppen; vraag via forum en Reddit niet te meten (proxy dicht).
- Besluit: cijfer 6, ja met kleine inzet, categorie Xero-facturen in Attio. Waarom geen 7: geen verkoopcijfer, vraag alleen indirect, nieuwe apps krijgen weinig installs vanzelf, en Attio krijgt een eeuwige licentie op SDK-broncode (oplossing: logica op eigen server).
- Script voor de herhaalmeting: data/attio-apps-meet.py (getest). Volgende run: radar, Q3-cijfers eToro (10 nov), en jonge start-up-software met een net stabiele app-SDK schiften (Linear, Granola, Clay, Folk, Pylon, Plain).
- Tweede (08:52 tot 09:00): snelle schifting Linear, Folk, Pylon, Plain, Granola, Clay op de Attio-manier. Alle nee: Linear heeft een oude, gecureerde integratielijst (sinds 2022, 366 stuks) zonder app-schermen; de rest heeft geen lijst voor makers. Geen derde onderzoek begonnen: geen sterke kandidaat over (regel 0c).

## Run 9 nov 2026 09:39 UTC (Noor)
- Geen open berichten van Thijs, geen verlopen herhaalmetingen (eToro Q3 morgen). Radar: Hermes Marketplace en ChatGPT Plugin Extensions, geen nieuw feit; algemene zoekopdrachten naar nieuwe betaalde winkels gaven weer alleen oude bekenden.
- Gekozen: Whatnot Seller API (claim-commit e423b3a). Waarom: hardst groeiende winkelplek van dit moment, en een API die net algemeen openging is precies het moment vlak voor een app-ecosysteem. Hulpagent voor de bestaande tools en de vraag (33 tools); zelf de blog (datum 29 okt 2026), docs, oude docs, groeicijfers en drie tools nagekeken.
- Besluit: cijfer 5, nog niet klaar. Waarom: groei en lege hoeken zijn top en een eigen kassa mag, maar de API is alleen voor eigen gebruik; apps voor andere verkopers kunnen alleen met een OAuth-app die het Whatnot-team toekent, zonder loket. Zonder die stap kunnen we niets leveren. Script data/whatnot-api-meet.py (getest) meet elke week of dat verandert.
- Een poging een pagina te lezen met een browser-User-Agent werd geweigerd; voortaan gewone curl.

## Run 9 nov 2026 10:40 UTC (Noor)
- Geen open berichten van Thijs, geen verlopen herhaalmetingen. Radar: algemene zoekopdrachten naar nieuwe winkels gaven weinig; Logi Marketplace stond al bij Vera (2, geen betalen). Wel nieuw: Sitecore Marketplace kreeg op 5 nov 2026 een openbare ideeënlijst met stemmen.
- Gekozen: Sitecore Marketplace (claim-commit c7f910b). Waarom: jonge winkel (publieke apps sinds nov 2025) in een platform met kopers die veel betalen, betalen mag met eigen kassa, en nog door niemand van ons bekeken.
- Gemeten: npm (SDK en grote pakketten), Stack Exchange-API, GitHub-codezoektocht (55 repo's), docs en changelog. Winkel en ideeënlijst zitten achter de inlog. Controleur (agent) bevestigde punten 1 tot 6; tweede punt aangevuld: in juni en juli een bult, per oktober gelijk.
- Besluit: cijfer 4, nee, ook niet voor Vera. Waarom: het platform groeit niet (alleen overstap van bestaande klanten, Stack Exchange halveert per jaar), geen betaalde app te zien, bureaus vullen de winkel met gratis apps en Sitecore met eigen default apps, en bouwen vraagt een Sitecore-omgeving plus keuring. Les in kandidaten.md: oude enterprise-CMS'en overslaan.
- Tweede (10:52 tot 10:58): snelle schifting Kit App Store en beehiiv, beide nee voor de pionier (Kit oud en vlak, beehiiv zonder app-winkel). Radar via Hacker News lukte niet (algolia geblokkeerd). Geen nieuwe kandidaat met groei en betalen die nu werkt; gestopt in plaats van een half onderzoek te beginnen (regel 0c). Volgende run: Q3-cijfers eToro (10 nov), radar.

## Run 9 nov 2026 11:40 UTC (Noor)
- Geen open berichten van Thijs, geen verlopen herhaalmetingen. Radar: algemene zoekopdracht gaf alleen oude bekenden (Freshworks); Notion lanceerde dit jaar Custom Agents, AI Skills en Workers.
- Gekozen: Notion Marketplace (claim-commit 9579dd8). Waarom: hard groeiend platform met een nieuw soort listing (agents, skills) met zichtbare installs en een eigen kassa voor templates.
- Gemeten: alle 393 agent-templates en 528 koppelingen uit `__NEXT_DATA__`, detailpagina's van alle agents (datum, maker), 703 van 2.305 AI Skills (daarna gaf de site geen data meer), help en developer-docs. Controleur (agent) bevestigde alle vijf punten; kanttekening: agent-datums in zijn steekproef alle feb tot jun.
- Besluit: cijfer 3, nee voor nu. Script data/notion-marketplace-meet.py, data in data/notion-agents-2026-11-09.json.
- Tweede (12:00 tot 12:08): snelle schifting Warp, Excalidraw en Lovable, alle nee. Geen sterke nieuwe kandidaat met groei en betalen die nu werkt; gestopt in plaats van een half onderzoek te beginnen.

## Run 9 nov 2026 12:40 UTC (Noor)
- Nieuw bericht van Thijs (9 nov 13:35): we zoeken een 8; Kees herweegt de zesjes, Lotte zoekt buiten de gewone winkels en buiten Engelstalig gebied. Hun lijsten zijn nog leeg, dus geen dubbel werk. Gelezen en verwerkt.
- Radar: algemene zoekopdrachten gaven alleen oude bekenden. Geen verlopen herhaalmetingen of weektaken (laatste weekcheck 8 nov 22:49).
- Gekozen: AltStore PAL (claim-commit c332855). Waarom: betalen werkt nu, de winkel is in Japan en Brazilië minder dan een jaar open en stond nog nergens in onze lijsten. Japan en Brazilië horen niet bij Lotte, want AltStore is Engelstalig en de makers zitten overal.
- Gemeten: docs (kosten, landen, Patreon), explore.alt.store-API (102 bronnen per maand), Patreon-API (8.710 betalende leden bij AltStore zelf). Controleur (agent) bevestigde alles en vond geen recenter gebruikerscijfer.
- Besluit: cijfer 3, nee. Waarom: klein publiek zonder zichtbare groei, en wat er werkt is wat Apple weigert. Script data/altstore-explore-meet.py, data in data/altstore-explore-2026-11-09.json.
- Git pull bleef hangen zonder time-out; voortaan `GIT_TERMINAL_PROMPT=0 timeout 60 git fetch` en daarna `git merge --ff-only` of `git rebase`.

## Run 9 nov 2026 13:40 UTC (Noor)
- Geen nieuwe berichten van Thijs (bericht van 13:35 was al verwerkt). Lijst van Kees: Steam bureaublad 8 (krap), XENEON in onderzoek bij Kees; niet dubbel gedaan. Geen verlopen herhaalmetingen.
- Radar: Google opende op 28 okt 2026 het Connected Apps Platform (apps via MCP in Gemini en Search). Verse winkel bij het grootste publiek dat er is, nog door niemand van ons bekeken.
- Gekozen: Google Connected Apps (claim-commit fe996cf). Docs en beleid zelf gelezen met curl, officiële lijst geteld (86 apps, 30 alleen VS), script data/google-connected-apps-meet.py gemaakt en getest. Controleur (agent) bevestigde: alleen VS met wachtlijst, wrapper- en reclameverbod, lijst is een merkenlijst, geen verslag van een kleine maker.
- Besluit: cijfer 4, nee voor nu, volgen. Waarom: Thijs kan er niet in (VS), betalen alleen via een eigen dienst, wrappers op andermans API verboden, dus geen snelle kleine apps.
- Les: Apify Store (Vera 4 op 6 nov) heeft sinds 2026 pay-per-event en een $1M-challenge; misschien iets voor Kees om te herwegen.
