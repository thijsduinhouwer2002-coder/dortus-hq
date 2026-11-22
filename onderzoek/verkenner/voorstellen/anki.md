# Anki, add-ons via AnkiWeb

Onderzocht: 7 nov 2026, run 23:32 UTC, door Vera. Onderzoeker (geld) en controleur ingezet. Controleur akkoord, correcties verwerkt.

## Advies: nee voor nu. Cijfer 4.

Anki groeit volgens derden en wordt sinds februari 2026 overgedragen aan AnkiHub, dat aankondigde dat add-ons makkelijker te vinden worden. Maar een gewone nieuwe add-on krijgt bijna niets, er is geen betaling in AnkiWeb, en het geld van kleine makers via Patreon blijft klein (tientallen tot een paar honderd dollar per maand). Twee gratis uitschieters uit 2026 laten wel zien dat een nieuwe maker in maanden heel groot kan worden. Opnieuw bekijken als AnkiHub een nieuwe add-on-winkel aankondigt met downloads of betaling.

## Wat het is
Anki is een gratis flitskaartenprogramma (vooral geneeskundestudenten en taalleerders). Add-ons zijn Python-uitbreidingen voor de computerversie, gedeeld via ankiweb.net/shared/addons. Add-ons werken niet op iPhone en nog niet op Android (DERDEN, forums.ankiweb.net/t/idea-for-new-anki-addon-platform/68264).

## Hoe gemeten
- AnkiWeb is een SvelteKit-app. De lijst en de info per add-on komen uit open endpoints (`/svc/shared/list-addons?search=` en `/svc/shared/item-info?sharedId=ID`, protobuf, zelf uitgepakt). Robots.txt verbiedt alleen decks en downloads.
- Hele lijst: 3.835 add-ons met duimpjes omhoog en omlaag en laatste wijziging. Info (beschrijving en alle beoordelingen met datum) voor 2.299 add-ons: de 400 bovenaan de lijst plus alles gewijzigd sinds 1 nov 2025.
- AnkiWeb toont **geen downloads en geen startdatum**. Downloads zijn alleen voor beheerders. Leeftijd geschat met de datum van de eerste beoordeling. Add-ons zonder beoordeling hebben dus geen datum.
- Aanvulling: alle 1.908 onderwerpen in de forumcategorie Add-ons (Discourse, open JSON), met de eerste post van de 54 onderwerpen uit mei t/m aug 2026.
- Scripts en data: `data/anki-haal-script.py`, `data/anki-info-bijhaal-script.py`, `data/anki-analyse-script.py`, `data/anki-lijst-2026-11-07.json`, `data/anki-info-2026-11-07.jsonl`, `data/anki-forum-addons-mei-aug-2026.json`.

## Cijfers

### Bereik (beoordelingen, geen installs)
- GEZIEN, alle 3.835 add-ons: mediaan 1 duimpje omhoog, 40% (1.525) heeft geen enkele beoordeling, 16% heeft 10+, 2,1% heeft 100+.
- GEZIEN, gewijzigd sinds 1 nov 2025: 2.011 add-ons, waarvan 1.129 (56%) zonder beoordeling.
- GEZIEN, lichting met eerste beoordeling mei t/m aug 2026 (n=232, minstens 2 tot 6 maanden oud; de eerste beoordeling geeft alleen een ondergrens voor de leeftijd, er kunnen oudere add-ons tussen zitten die laat hun eerste beoordeling kregen): mediaan 1 duimpje, 2,6% heeft 10+, 0,4% heeft 50+. Top: 413, 47, 37, 10, 10, 10. Dit telt alleen add-ons die minstens één beoordeling kregen; tel je de add-ons zonder beoordeling mee, dan is de mediaan vrijwel zeker 0: 56% van de recent gewijzigde add-ons heeft geen enkele beoordeling (die zijn zelf niet te dateren).
- GEZIEN, lichting nov 2025 t/m apr 2026 (n=243, minstens 6 tot 12 maanden): mediaan 2, 9,9% 10+, 1,2% 50+.
- GEZIEN, nieuwe add-ons uit het forum (mei t/m aug 2026, met AnkiWeb-link, zonder de oude): bijna allemaal 0 tot 3 duimpjes; Audio Tools 47.
- GEZIEN, uitschieters: **Synapse** (eerste beoordeling 2 feb 2026, gratis; volgens de eigen beschrijving een solo geneeskundestudent uit Duitsland) 1.454 duimpjes, nu nummer 3 op heel AnkiWeb, 349 beoordelingen in de laatste 30 dagen. **Cristal Memoria** (9 mei 2026, gratis spel) 413. Daarna Memory Forest 88, Anki MCP Server 66, Elemental 53. Opvallend: veel spelletjes (gamification) en AI-koppelingen.
- GOK: hoeveel installs bij een beoordeling horen is niet bekend. AnkiWeb vraagt zelden om een beoordeling; 1 op 50 tot 200 installs is een gok. Dan zit de middelste nieuwe add-on onder de 100 installs en Synapse ergens tussen 70.000 en 300.000.

### Groei en drukte
- GEZIEN: ±50 tot 70 add-ons per maand krijgen sinds april 2026 hun eerste beoordeling. Groei is uit deze data **niet betrouwbaar te meten**: de info is alleen gehaald voor de top 400 en alles gewijzigd sinds nov 2025, dus in 2025 ontbreken per maand 23 tot 44 add-ons (controleur). De lagere cijfers voor 2025 zijn grotendeels een meetfout.
- GOK: met de add-ons zonder beoordeling erbij ruwweg 60 tot 150 nieuwe add-ons per maand. Niet hard. De forumcategorie Add-ons krijgt ±10 tot 25 nieuwe onderwerpen per maand, met meestal 100 tot 500 keer bekeken. Het forum is dus geen grote bron van bereik.
- DERDEN: AnkiDroid 10 miljoen+ downloads (Google Play), AnkiMobile 2.384 beoordelingen in de VS-winkel, r/Anki ±210.000 leden (gummysearch).

### Geld
- GEZIEN: AnkiWeb heeft geen betaalfunctie. Voorwaarden eisen een AGPL3-licentie of verenigbaar (ankiweb.net/account/terms). Geen verbod op betaalde functies of AI-gemaakte add-ons gevonden.
- GEZIEN, in de beschrijvingen van 2.299 add-ons: Patreon 146 keer, Ko-fi 103, Buy Me a Coffee 90, "subscription" 44, "premium" 22. Ongeveer 121 add-ons noemen een betaalde laag of proefperiode.
- GEZIEN, betaalde vormen: Deckline Premium €5 eenmalig via Ko-fi (47 duimpjes), Pomodium Pro, HyperTTS $5 per maand (vocab.ai, 640 duimpjes), Smart Notes (open add-on, betaalde server), AnkiHub $5 per maand.
- GEZIEN via graphtreon (schattingen van de site): Shige 116 leden, ±$418 per maand (sinds apr 2023, dalend); Glutanimate 155 leden, $256 tot $1K (sinds 2017); Language Tools 28 leden, $117. Ankimon (populairste add-on, 2.485 duimpjes) via Patreon maar 1 lid; Ko-fi niet te zien.
- GEZIEN, enige nieuwe maker met geld: **Gainz** (gestart 7 maart 2026), pakket van 7 betaalde add-ons voor geneeskundestudenten via Patreon, 30 leden, geschat $41 tot $262 per maand (graphtreon.com/creator/gainz757). Hoogste punt ±40 leden in april, daarna omlaag. Gebruikers klaagden over het abonnement.
- DERDEN: Shige zegt dat hij "tons of complaints about paywalls" krijgt (forumdraad 68264). De twee grootste nieuwkomers van 2026 zijn gratis.

### Vindbaarheid
- In Anki zelf kan je niet zoeken of bladeren: je kopieert een code van de website. Gebruikers vinden add-ons via de AnkiWeb-lijst (gesorteerd op beoordeling), Reddit, YouTube en blogs zoals "best Anki add-ons". Nieuwe add-ons staan nergens apart.
- GEZIEN: het Anki-team (nu AnkiHub) schreef in juni 2026 dat add-ons "easier to find and simpler to manage" worden (forums.ankiweb.net/t/updates-from-the-anki-team-june-2026/70120). Nog geen datum of details.

## Voor
- Groot publiek (groeiend volgens derden), vooral studenten die elke dag uren in Anki zitten.
- Een nieuwe maker kan in maanden heel groot worden (Synapse, Cristal Memoria).
- Python-add-ons: snel te bouwen, past bij ons.
- Eigenaar verandert, add-on-systeem wordt vernieuwd: daar kan later een kans liggen.
- Sterkste tegenargument (controleur): het doel is eerst bereik. Synapse en Cristal Memoria laten zien dat een gratis spel of AI-add-on van een onbekende maker in maanden duizenden gebruikers kan halen, en één goedkope gratis proef levert ook het ontbrekende cijfer op (installs per beoordeling). Een 5 is te verdedigen. Waarom toch 4: geld weegt voor de verkenner even zwaar als bereik, en de gewone nieuwe add-on haalt niets; we zouden op een uitschieter gokken zonder betaalroute. Naast Blender (7) en BOOTH (6) is dit zwakker.

## Tegen
- Geen betaling in de winkel, code moet open (AGPL). Betalen alleen via Patreon of een eigen dienst.
- Gebruikers zijn gevoelig voor betaalmuren; de grootste nieuwkomers zijn gratis.
- Gewone nieuwe add-on: mediaan 0 tot 1 beoordeling.
- Alleen op de computer.
- Bereik niet echt te meten (geen downloads).
- Anki bouwt de editor om (forum oktober 2026, aqt.editor.NewEditor), add-ons kunnen breken.

## Eerste idee, als het later ja wordt
Een gratis add-on met spel of voortgang (de hoek die nu groeit), met een betaalde extra laag via een eigen licentie of Patreon. Of een AI-koppeling (Claude of ChatGPT) met een betaalde server, zoals Smart Notes.

## Wat nog gemeten kan worden
- Verhouding beoordelingen en installs: alleen te weten via een maker die zijn downloads deelt, of als AnkiHub downloads gaat tonen.
- Herhaalmeting over 4 weken met dezelfde scripts: hoe snel stijgen de nieuwkomers?
- Volgen: nieuws van AnkiHub over een add-on-winkel met betaling.

## Controle
Controleur (agent) akkoord met het advies. Alle cijfers uit de data nagerekend, live steekproef van 14 add-ons: duimpjes precies gelijk. Gainz, Shige en Synapse (gratis) nagekeken. Correcties verwerkt: groei niet te meten (meetfout in 2025), leeftijd is een ondergrens, mediaan 0 vrijwel zeker, aantal nieuwe per maand voorzichtiger, tegenargument toegevoegd.
