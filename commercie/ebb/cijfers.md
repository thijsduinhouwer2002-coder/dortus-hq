# Ebb (Garmin): cijfers

Bijgehouden door Chris. Alles met curl gemeten op de openbare winkel-API van Garmin (`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<winkel-id>`) en de zoek-API (`.../apps/keywords?keywords=<woord>&sortType=mostRelevant`, eerste 30). Winkel-id Ebb: `5280653d-1681-452d-8c03-7cbdc7284641`.

Let op bij het lezen: `downloadCount` is de teller van Garmin; hoe vaak die bijgewerkt wordt en of een retour (48 uur) eraf gaat, is NIET GEZIEN. Verkopen en geld zie je alleen in het verkopersaccount van Thijs; dat lees ik niet.

## Meetmomenten

| Moment (UTC) | Dag | Status | Downloads | Beoordelingen | Gemiddelde | Prijs | Ebb Calm openbaar |
|---|---|---|---|---|---|---|---|
| 13 nov 22:01 (Gijs, run 96) | 0 | APPROVED | 0 | 0 | 0 | $4.99 | nee (niet ingediend) |
| 14 nov 08:45 (Chris, run 35) | 1 | APPROVED | 0 | 0 | 0 | $4.99 | nee (ingediend 14 nov ±07:30, in keuring) |
| 14 nov 11:50 (Chris, run 36, tussencheck) | 1 | APPROVED | 0 | 0 | 0 | $4.99 | nee (makerlijst Dortus: 1 app) |
| 14 nov 17:50 (Chris, run 38) | 1 | APPROVED | 0 | 0 | 0 | $4.99 | nee (zoeken op "ebb calm": alleen Ebb, plek 1) |
| 14 nov 20:47 (Chris, run 39, tussencheck) | 1 | APPROVED | 0 | 0 | 0 | $4.99 | nee (makerlijst Dortus: 1 app) |

Goedkeuring: 13 nov ±21:09 UTC (veld `firstApprovalDate`; het ruwe getal geeft 15:09 UTC, maar dat kan niet, want om 15:22, 17:46 en 20:45 UTC gaf de winkel nog 404; gelezen als Amerikaanse Central-tijd 21:09 UTC, tijdzone GOK, zie `platformen/garmin/status.md`). Dag 1 is dus ±11,5 uur na de goedkeuring gemeten, nog zonder forumbericht of persoonlijke berichtjes.

## Vindbaarheid in de winkelzoeker (plek in de eerste 30, mostRelevant)

| Zoekwoord | 13 nov 22:15 (Gijs) | 14 nov 08:45 (Chris) | 14 nov 11:55 (Chris, run 36) | 14 nov 17:50 (Chris, run 38) |
|---|---|---|---|---|
| ebb | 1 | 1 | niet gemeten | 1 (87 treffers) |
| breath hold | 4 | 4 | 4 | 4 |
| breathing exercises | niet gemeten | 4 | 4 | 4 |
| breathing | niet in de eerste 30 | 30 (controleur even later: 29, plekken schuiven) | 29 | 30 |
| breathwork | niet in de eerste 30 | niet in de eerste 30 | 30 bij de eerste vraag, een minuut later niet in de eerste 30 (wisselt op de rand) | niet in de eerste 30 |
| box breathing | niet gemeten | niet in de eerste 30 | niet gemeten | niet gemeten |
| calm | niet gemeten | niet in de eerste 30 | niet gemeten | niet gemeten |
| apnea | niet gemeten | niet in de eerste 30 | niet gemeten | niet gemeten |
| 4-7-8 | niet gemeten | zoeker geeft 0 treffers | niet gemeten | niet gemeten |

"Breathing" en "breathing exercises" staan in de titel, "breathwork" alleen in de tekst en de tags. Na een week kijken of de plek op "breathwork" verandert; zo niet, dan is dat een punt voor een volgende versie van de titel (advies, niet nu: de titel is net gekeurd).

### Hoe de zoeker rangschikt (14 nov 11:55 UTC, run 36)
Gemeten op dezelfde zoek-API, eerste 30 van "breathing" (993 treffers) en "breathwork" (995 treffers), met titel, downloads en hoe vaak het woord in de Engelse tekst staat. GEZIEN; de ruwe lijst is niet bewaard, opnieuw te halen met de curl uit de kop van dit bestand (met `startPageIndex=0`, anders geeft de API een fout).
- **"breathing":** alle 30 hebben het woord in de titel. Bovenaan staan korte titels waarin het woord een groot deel is: 1 "Box Breathing" (10+ downloads), 2 "Breathing Exercises" (1.000+), 3 "Tactical Breathing" (100+), 5 "Breathing Assistant" (10+). De grootste, WHM breathing (50.000+), staat pas op 8; "Breathe: Breathing Exercises" (1.000+, de concurrent die het meest op ons lijkt, AFGELEID) op 16. Ebb (titel van 6 woorden, 0 downloads) staat op 29, net voor "Breath – Guided Breathing, HRV & Breath Holds" (30), ook een lange titel met weinig downloads.
- **"breathwork":** plek 1 tot 8 hebben het woord in de titel, ook apps met 0 tot 10 downloads ("Breathwork" 10+, "BREATHWORK" 10+, "GroundApp: Breathwork with Bodie" 0). Vanaf plek 9 staat het woord alleen in de tekst (1 tot 4 keer). Ebb heeft het 2 keer in de Engelse tekst en hangt op de rand van plek 30.
- **Wat ik eruit afleid (AFGELEID, niet bewezen):** de zoeker kijkt eerst naar de titel, en een korte titel waarin het zoekwoord een groot deel is, wint van veel downloads. De tekst telt pas als geen titel past. Downloads en beoordelingen tellen vermoedelijk wel mee, maar minder dan de titel (GOK).
- **Wat het betekent voor Ebb:** op "breath hold" (4) en "breathing exercises" (4) staan we goed, want daar zijn weinig titels met precies die woorden (AFGELEID). Op de brede woorden "breathing" en "breathwork" komen we met deze lange titel niet hoog, ook niet met wat downloads erbij (GOK). Hoeveel mensen op elk woord zoeken, laat de winkel niet zien. Zie advies 37 in `commercie/adviezen.md`.

## Ebb in de lijsten van de winkel: "Hot & Fresh" loopt ±17 nov af (14 nov 20:45 UTC, run 39)

GEZIEN met curl op dezelfde winkel-API, met `commercie/ebb/meet-lijsten.py`. De namen staan in de pagina en broncode van apps.garmin.com: `store_category_hotFresh` "Hot & Fresh Apps", `store_category_newAndUpdated` "New and Updated Apps", `store_category_trending` "Trending Apps", en in de code `HOT_FRESH:"hotFresh"`. Dat "New and Updated" op de site de API-sortering `mostRecent` gebruikt, is AFGELEID, niet bewezen. Hoe groot elk blok op de site of in de Connect IQ-app is (hoeveel apps je ziet zonder door te klikken), is NIET GEZIEN.

- **"Hot & Fresh Apps", alleen watch-apps:** 120 plekken. Plek 1 tot 9 zijn bekende apps met veel downloads (Crossy Road 3D, Atmos Weather, ...). Daarna 111 nieuwe apps (`markedAsNew: true`), nieuwste goedkeuring eerst: 38 van 13 nov, 43 van 12 nov, 30 van 11 nov. **Ebb staat op plek 36.** In dezelfde lijst ook twee nieuwe ademapps: "GroundApp: Breathwork with Bodie" (plek 19, gratis, 0 downloads, ook 13 nov) en twee keer "Nim Breathe" (plek 68 en 69, gratis, 1+; lijken twee aparte apps met dezelfde naam), en de vrijduikapp "Capnia" (plek 16).
- **Dezelfde lijst voor alle soorten samen (met wijzerplaten):** Ebb staat niet in de 120. Wie in de winkel niet op "apps" filtert, ziet Ebb hier dus niet.
- **Hoe lang nog:** Garmin keurt in groepen op werkdagen. Nieuw goedgekeurde watch-apps per dag (afgeleid uit de lijst "New and Updated", `firstApprovalDate`): 9 nov 134, 10 nov 49, 11 nov 62, 12 nov 48, 13 nov 38; op za 7 nov 2 en zo 8 nov 0. Na ±85 nieuwe watch-apps valt Ebb uit de 120 (plek 36 van een lijst die bij 120 stopt; controleur: pagina 5 en verder geven niets). **Verwachting (GOK op GEZIEN): Ebb staat het weekend nog in Hot & Fresh en valt eruit bij de goedkeuringen van ma 16 of di 17 nov, uiterlijk wo 18 nov.** Na het vorige weekend kwamen er op ma 9 nov in één keer 134 bij; gebeurt dat weer, dan is het maandag al.
- **"New and Updated Apps" (`mostRecent`):** gesorteerd op `changedDate`; in de API oplopend vanaf ±7 nov, Ebb op plek 744 van 1.350. Hoe de site die lijst toont, is NIET GEZIEN. Een nieuwe versie zet `changedDate` opnieuw (GOK, niet getest).
- **"Trending Apps":** Ebb staat niet in de eerste 118.

**Is 0 downloads normaal? Ja, voor een betaalde nieuwkomer (GEZIEN, zelfde lijst, 14 nov 20:45 UTC).** Van de 111 nieuwe watch-apps zijn er 24 betaald in de winkel ($1,99 tot $4,99, geen enkele met proef). Na 1 tot 3 dagen staan er 13 op "1" (1 tot 9 downloads) en 11 op 0; **geen enkele haalde 10+**. Bij de 87 gratis nieuwkomers staan er 28 op 10+ en 1 op 100+. Eén maker bracht op 13 nov drie apps van $4,99 tegelijk uit (Racketday, Catchday, Huntday), alle drie 0. Ebb wijkt dus niet af. AFGELEID: de winkel brengt een betaalde app in de eerste dagen bijna niets; kopers moeten van buiten komen (forumdraad, persoonlijke berichtjes uit `proberen.md`) of later uit de zoeker.

**Wat dit betekent:**
1. De gratis zichtbaarheid van Hot & Fresh is er nog tot ±17 nov. Dit weekend is dus het beste moment voor de persoonlijke berichtjes uit `proberen.md` en de handtekening: wie Ebb dan opzoekt, ziet hem ook nog in de lijst van nieuwe apps.
2. **Ebb Calm krijgt waarschijnlijk zijn eigen plek in Hot & Fresh** als hij goedgekeurd wordt (AFGELEID: hij is een nieuwe app en, volgens Gijs, als watch-app gebouwd). Als gratis app haalt Calm in die dagen waarschijnlijk wel 10+ (zoals 28 van de 87 gratis nieuwkomers, GOK voor Calm), en de tekst van Calm verwijst naar Ebb. Dat is de tweede kans op aandacht, zonder werk van Thijs.
3. Na ±17 nov komt bereik in de winkel alleen nog uit de zoeker (zie hierboven: "breath hold" en "breathing exercises" plek 4) en mogelijk uit "New and Updated" bij een nieuwe versie (GOK). Zie advies 38.

## Winkelpagina nagekeken (14 nov 08:45 UTC, GEZIEN)
- Titel en: "Ebb: Breathing Exercises, Breath Hold & Calm"; ook een Duitse en een Nederlandse titel staan erop.
- Prijs $4.99, eenmalig, geen proefperiode (`hasTrialMode: false`).
- Vijf beelden (Gijs: poster, breathe, hold, new friend, sea log). Sea complete staat er niet; de lanceerstukken verwijzen er niet naar.
- 40 artikelnummers van horloges in de API. Het manifest noemt 28 modellen; het verschil zijn vermoedelijk regionale varianten van hetzelfde model (GOK). In de teksten blijft "28".
- Supportadres thijs@dortus.com, rechten Fit, FitContributor, Sensor.
- dortus.com/ebb/ geeft 200 en linkt naar deze winkelpagina. De hoofdpagina dortus.com noemt Ebb nog niet (geen pagina van mij).

## Volgende metingen
- Dag 7: 20 nov. Dag 30: 13 dec. Tussendoor bij elke run één regel als er iets verandert.
- Wat ik verwacht (GOK): zonder forumbericht en persoonlijke berichtjes bijna niets, want Ebb staat op de grote zoekwoorden niet of laag in de eerste 30. Het plan (`commercie/ebb/proberen.md`) mikt op 10 mensen die het een week proberen; het weekverslag met kopers is van Gijs (plan dag 7 in `platformen/garmin/gebruikers-krijgen-2026-11-13.md`).

## Forumdraad in de Connect IQ Showcase

Geplaatst door de hoofdchat op 14 nov ±07:35 UTC, eerst "Content Under Review". Link en tekst in `berichten-geplaatst.md`.

| Moment (UTC) | Zichtbaar zonder inlog | Antwoorden | Bekeken | Volgers | Plek op de eerste pagina van de Showcase |
|---|---|---|---|---|---|
| 14 nov 11:50 (Chris, run 36) | nee (niet in de lijst, niet te vinden) | | | | |
| 14 nov 17:47 (Chris, run 38) | ja, pagina 200 met de volledige tekst | 0 | 1 | 5 | 3 (na de vaste README-draad op 1 en één andere draad) |
| 14 nov 20:46 (Chris, run 39) | ja | 0 | 4 | 5 | niet gemeten |

GEZIEN met curl. "Bekeken" is de teller van het forum zelf; of die bezoekers zonder inlog telt, is NIET GEZIEN. De 5 volgers zijn waarschijnlijk vaste abonnees van nieuwe draden of de maker zelf (GOK).

