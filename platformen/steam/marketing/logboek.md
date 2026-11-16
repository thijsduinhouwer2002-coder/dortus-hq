# Logboek Sem (marketeer Hats of the Fallen)

## 16 nov 2026, run 1 (±11:20 tot 11:50 UTC)
- Map `platformen/steam/marketing/` gemaakt.
- Makerslijst versie 1: 40 YouTube-kanalen (`makers.md`), uit 18 zoektermen en 246 kanalen, met scripts `data/yt-zoek.py` en `data/yt-kanaal.py`.
- Besluit: alleen YouTube in versie 1, omdat Fenna (verhaal 4) liet zien dat daar de meeste weergaven over taakbalkspellen zitten en YouTube met curl leesbaar is. Twitch, TikTok en curatoren in de volgende runs.
- Besluit: gewone gmail-adressen niet uitschrijven in de openbare repo, alleen adressen op een eigen domein of van een bureau. Waarom: regel over persoonsgegevens; wie verstuurt, vindt het adres op het kanaal.
- Volgende run: Twitch en curatoren, dan teksten per groep, dan punt 3 (festplan met meetlat, wo 25 nov).

## 16 nov 2026, run 2 (±12:20 tot 13:05 UTC)
- **Festplan versie 1** (`festplan.md`, fest-plan punt 3, eerder dan wo 25 nov): fasen met doel (500 verlanglijstjes vóór de demo, 1.000 op de avond voor het fest, GOK), festweek dag voor dag met hoedendoelen uit Sanne's optie A, meetlat na dag 2 (za 16 jan 19:00 NL) met spelers tegelijk en verlanglijstjes, en wat we doen als het stil blijft.
- **Besluit: demo openbaar op ma 4 jan, niet pas op dag 1 van het fest** (Olaf beslist over de build, vraag in `berichten/olaf.md`). Waarom: Valve sorteert in het demovak op belangstelling en populariteit (GEZIEN in de Steamworks-docs), makers hebben dan geen sleutels nodig, en fouten zien we bij weinig spelers.
- **Besluit: doelen in hoeden, niet in spelers.** Waarom: hoeden zijn onze haak, en een opgetelde Steam-stat kunnen we eerlijk tonen zonder server; spelers tegelijk niet.
- **Nulmeting** (GEZIEN 12:38 tot 12:45 UTC): van 245 demo's van aangekondigde bureaubladspellen hebben er 170 (69%) nu 0 spelers, 10 hebben er 20 of meer, 5 hebben er 100 of meer. Van de 48 kerker- en gevechtsdemo's heeft de beste 19. De grenzen 20 en 100 uit de meetlat zijn dus niet te laag. Scripts `data/demo-spelers.py` en `data/demo-spelers-lijst.py`.
- **Makerslijst:** 19 kanalen van Fenna erbij (41 tot 59), met grootste video en kans.
- **Correctie op run 1, belangrijk voor de hoofdchat:** ik schreef dat Wanderbots ("100% human-made videogames") een kans was omdat Hats geen AI-beeld heeft. Dat is misleidend: Hats wordt door AI-agents gemaakt, ook de code die de 3D-beelden bouwt en de teksten in het spel. Regel in al mijn teksten: nergens "no AI" of "human-made". Let op: `platformen/succes/onderscheid-hats.md` (Fenna) noemt "3D, zonder AI" als onderscheid en `platformen/steam/idee.md` zegt "met AI gemaakte plaatjes melden we op Steam, of we gebruiken ze niet"; de AI-melding op de winkelpagina (Valve vraagt die voor wat spelers zien, ook tekst) moet de hoofdchat met Thijs vastleggen vóór de pagina op 1 dec wordt ingediend. Ik heb nergens een besluit daarover gevonden (grep op besluiten.md, teksten.md).
- **Teksten voor makers** (`teksten-makers.md`): per groep A, B, D, Curator Connect; groep C pas als de taal in de demo zit. Niets verstuurd.
- Afspraken: Olaf (demo 4 jan, appid, doelen), Chris (zes aankondigingen en clips voor de festweek, vóór 8 jan).
- **Auto-Battler RPG Fest** (16 tot 23 nov, begint vandaag 18:00 UTC): nulmeting vóór de start gestart op de eerste 200 van 773 aangekondigde Auto Battler-spellen (`data/autobattler-demos-voor-fest-2026-11-16.csv`). Volgende run: dezelfde demo's meten tijdens het fest (met de cache, `demo-spelers-lijst.py <ids> <uit> <cache>`). Dat geeft de eerste echte cijfers over hoeveel een thema-fest optilt.
- Volgende run: (1) Auto-Battler-meting dag 1, (2) contact van de 19 nieuwe kanalen nalopen, (3) Twitch en curatoren.
