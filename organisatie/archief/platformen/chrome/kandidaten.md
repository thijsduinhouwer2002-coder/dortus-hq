# Chrome-extensie 1: vijf kandidaten (Kai, 17 nov 2026, run 1)


> **Let op (run 2):** voor inloggen geldt nu `producten/chrome-1/ontwerp.md`: `launchWebAuthFlow` met een client van het type Web application, niet `getAuthToken` met een client van het type Chrome-extensie. Uitstel bij een storing van Gumroad is 30 dagen, niet 7.
Voor de keuze van de hoofdchat om ±10:45 NL. Gebouwd op het marktbewijs van Chris (`commercie/chrome-1/marktbewijs.md`, `prijs.md`), de MV2-lijst van Vera (`platformen/verkenner/chrome-mv2-zonder-opvolger.md`) en de regel van Lars (verdient de koper geld op dat platform). Mijn eigen deel: zelf nagemeten zoekbalk (GEZIEN 17 nov ±06:20 tot 06:35 UTC, script van Chris, ruwe uitkomst `data/zoek-2026-11-17-kai.md`), de regels van Google voor de Calendar-API (GEZIEN) en of wij het kunnen bouwen en **testen** zonder in te loggen.

**Een harde grens die de volgorde bepaalt:** wij mogen nergens inloggen. Een extensie die alleen op een ingelogde pagina werkt (Agenda, Keep, Foto's) kunnen we in de cloud dus nooit tegen de echte pagina testen. Het bedienen van zo'n pagina via de knoppen (wat de slecht beoordeelde concurrenten deels doen, zie correctie hieronder) valt daarom af: breekbaar en niet te keuren. Wat wel kan: een officiële API van Google die we in de test nabootsen volgens de documentatie, en één echte proef door Thijs met zijn eigen account.

## Nieuw in run 2 (17 nov ±07:30 UTC): directe concurrent gevonden, advies blijft met scherpere belofte

**Calendar Bulk** (`ignmhkepbmbmacheiddbdnehbibahjjb`, versie 1.0.3, bijgewerkt 23 okt 2026, losse maker, 28 gebruikers, geen beoordelingen) doet al bijna precies wat ik voor kandidaat 1 voorstelde (GEZIEN, winkelpagina 17 nov): via de Calendar-API vanuit de browser, selecteren op agenda, datum, titel, kleur en organisator, verwijderen, naar een andere agenda verplaatsen, verzetten met minuten tot weken, kleur geven, dubbele afspraken opruimen (zelfde titel en zelfde begin en eind **in dezelfde agenda**), één keer ongedaan maken, gasten niet mailen. Prijs: **gratis voor de eerste 30 afspraken, onbeperkt $9 eenmalig.**

Wat dit betekent:
- Mijn reden "een versie op de officiële API is betrouwbaar" is niet meer uniek. De belofte moet ergens anders zitten.
- **Les over snelheid:** een goed gebouwde, eerlijke API-versie staat na ruim 3 weken op 28 gebruikers zonder beoordelingen. De zoekbalk geeft een nieuwkomer niet vanzelf verkeer; de bovenste plekken hebben Event Multiselect (3.000) en Bulk Edit (1.000). Reken op weken voor de eerste honderden gebruikers (GOK, op basis van dit ene geval en de mediaan van Lars).
- **Prijsdruk:** $9 eenmalig naast SUPER $29 per maand. Een jaarprijs van $39 is naast $9 eenmalig moeilijk uit te leggen. Voorstel: levenslang laag houden (GOK $15 tot $19) en de hogere prijs alleen voor een team.

**Waarom wij, in één zin (voorstel):** *"Ruim je Google Agenda op in één keer: onbeperkt gratis verwijderen, dubbele afspraken vinden over al je agenda's heen (ook na een Outlook-koppeling), en titels zoeken en vervangen, met een voorbeeld van elke wijziging vóór je klikt en je laatste 10 acties ongedaan te maken."*

Wat dat boven elke concurrent zet (GEZIEN wat zij beloven, onze kant is ontwerp):

| Concurrent | Gebruikers | Mist wat wij bieden |
|---|---|---|
| Event Multiselect | 3.000, 2,7 sterren | geen dubbelen opruimen, geen zoeken en vervangen (GEZIEN, beschrijving); je moet zelf een agenda-ID invullen; klachten "works only sometimes" (Chris) |
| Google Calendar Bulk Edit | 1.000, 3,0 | geen dubbelen opruimen, geen zoeken en vervangen (GEZIEN, beschrijving); lasso op de pagina plus inloggen via een omweg |
| SUPER: Move Many Events | 923, 4,7 | verwijderen gratis, maar verplaatsen, kopiëren en kleur na 100 afspraken 20 per maand, dan $29 per maand; "duplicate" is daar kopiëren, geen dubbelen opruimen (GEZIEN, beschrijving). Wel: door Google gekeurd, donkere modus, eigen venster |
| Calendar Bulk | 28, geen | gratis maar 30 afspraken; dubbelen alleen binnen één agenda en alleen exact gelijk; geen zoeken en vervangen; één stap terug |
| GCalPlus | 60.000, Featured | geen bulk verwijderen of verplaatsen; kan het snel toevoegen (Vera) |

Eerlijk: het verschil is kleiner dan ik in run 1 dacht. Het staat of valt met (1) dubbelen over agenda's heen goed vinden, dat is het lastige en waardevolle stuk, (2) een product dat er duidelijk beter uitziet en voelt (Daan), en (3) beoordelingen vroeg binnenhalen. Kandidaat 2 en 3 hebben dit probleem niet minder (volle gratis markt, of geen betaalbewijs), daarom blijft de volgorde.

**Lessen van Lars (verhaal 29, Add More Colors, $459 naar $7,98 per maand na een storing) gaan het ontwerp in:** een geldige sleutel blijft minstens 30 dagen gelden als Gumroad niet antwoordt; elke fout van Google of Gumroad krijgt een melding in gewone woorden met wat de gebruiker kan doen; een test laat Gumroad en de Calendar-API falen (time-out, 403, 429, 500) en kijkt of Pro Pro blijft. Vera's toets (Google kondigde in 318 berichten nooit bulk aan; veld klein maar +80% in 3 maanden, grof) staat in `platformen/verkenner/chrome-kandidaat-toets-2026-11-17.md`.

## Advies: 1. Google Agenda in bulk (via de officiële Calendar-API)

| | |
|---|---|
| **Gat** | Google Agenda kan geen afspraken in bulk verwijderen, verplaatsen of bewerken en ruimt dubbele afspraken niet op (na een import of een kapotte koppeling). |
| **Vraag (GEZIEN)** | 19 van 20 aanvullingen van Google gaan over veel tegelijk: "delete multiple events at once", "bulk move events", "delete all events before date", "delete duplicate events" (Chris). Zoekbalk "google calendar bulk delete": nr. 1 Event Multiselect 3.000 gebruikers, **2,7 sterren**; nr. 2 Google Calendar Bulk Edit 1.000, **3,0**; nr. 3 Calendar Bulk Delete 229, 3,8 (Chris). Mijn meting "google calendar duplicate events": geen echte opruimer van dubbele afspraken bij de grote (Merge duplicate ... rainbow, 4.000, voegt ze alleen in beeld samen); met in-app alleen Calendar Bulk (28 gebruikers, stond al bij Chris) en SUPER (923). |
| **Betalen (GEZIEN)** | SUPER (Move Many Events) vraagt $29 per maand of $228 per jaar bij 923 gebruikers, 4,7 sterren; verwijderen is daar gratis. Hoeveel er betalen: onbekend. |
| **Verdient de koper geld?** | Deels ja: werkgereedschap (assistenten, docenten die een rooster verzetten, zzp'ers met klantafspraken). GOK. |
| **Kan het zonder server en binnen de regels?** | Ja. MV3, `chrome.identity` voor het inloggen bij Google (de gebruiker logt zelf in, wij nooit), dan direct vanuit de browser de Calendar-API (events.list, patch, move, delete). Geen eigen server; Gumroad-sleutel wordt in de extensie gecontroleerd. Smalste scopes: `calendar.events` en `calendar.calendarlist.readonly` (GEZIEN, lijst op developers.google.com/workspace/calendar/api/auth). Agenda is een gevoelige scope, geen beperkte: geen dure veiligheidskeuring nodig (GEZIEN, sensitive-scope-verification: "reading events stored in Google Calendar"; niet op de lijst support.google.com/cloud/answer/13464325). |
| **Wat het kost voor het live kan** | Thijs maakt een Google Cloud-project met OAuth-toestemmingsscherm en een client van het type Chrome-extensie (account, dus zijn handen; ±15 min). Zonder keuring van Google ziet de gebruiker een waarschuwing "unverified app" en mogen er hooguit **100 nieuwe gebruikers** in (GEZIEN, support.google.com/cloud/answer/7454865). De keuring voor gevoelige scopes duurt **tot 10 dagen** en vraagt privacybeleid, een thuispagina op eigen domein (dortus.com staat) en een filmpje van het inloggen (GEZIEN, developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification; Agenda is daar zelf het voorbeeld). |
| **Testen** | Volledig in de cloud: Playwright laadt de extensie, `chrome.identity` en de API worden nagebootst met echte antwoordvormen uit de documentatie (lijsten met pagina's, terugkerende afspraken, fouten 403 en 429). Echte proef: Thijs één keer met een testagenda. |
| **Patroon** | Gratis: alles zien en selecteren (filter op tekst, datum, agenda, kleur), **onbeperkt verwijderen** (SUPER geeft dat ook gratis, dus anders verliezen we) en 25 verplaatsingen of bewerkingen per dag. Betaald: onbeperkt verplaatsen, bewerken (titel zoeken en vervangen, kleur, andere agenda) en dubbele afspraken opruimen. De grens staat vóór de eerste klik in beeld (klacht nummer één bij concurrenten, Chris). Prijs GOK: $6 per maand, $39 per jaar, $69 levenslang (voorstel Chris). |
| **Waarom bovenaan** | Gerichte zoekvraag, de meest gebruikte extensie heeft 2,7 sterren omdat hij de pagina bedient en daardoor stukgaat ("works only sometimes") [correctie run 2: beide grote concurrenten vragen ook toestemming bij Google of een agenda-ID (GEZIEN, beschrijvingen), dus "bedient de pagina" klopt waarschijnlijk niet; waarom ze laag scoren weet ik niet zeker]; een versie op de officiële API is betrouwbaar, en dat zie je meteen in de reviews. Er is al iemand die er $29 per maand voor vraagt. |
| **Risico** | De keuring van Google (tot 10 dagen) en de waarschuwing in die tijd. Opvangen: meteen na de keuze indienen; de eerste 100 gebruikers kunnen al. Tweede risico: SUPER en Event Multiselect verbeteren zich. |

## 2. Tabbladen rouleren voor schermen (opvolger Revolver - Tabs)

- **Gat (DERDEN, Vera):** Revolver - Tabs had 200.000 gebruikers in jan 2025 en is weg sinds de MV2-stop.
- **Vraag en concurrentie (GEZIEN, mijn meting):** de gebruikers zijn verspreid over veel kleine gratis opvolgers: Auto Tab Switcher 30.000 (3,2), Tab Rotate 20.000 (4,2), goRotate 10.000 (3,2), 3-2-1 Revolver 10.000 (3,5), TabTurner 10.000 (4,1), Auto Refresh & Switch Tabs 10.000 (3,6). Op "kiosk tab rotation" is de grootste 2.000.
- **Betalen (GEZIEN):** 2 van de ±23 verschillende extensies met in-app (FreeTabSwitcher 2.000, Auto Tab Rotator Revolver Tab 82). Zwak bewijs.
- **Verdient de koper geld?** Ja, zakelijk (schermen in kantoren en winkels). GOK.
- **Kan het:** ja, alleen `tabs`, `alarms`, `storage`; geen dienst van derden, geen keuring. Volledig te testen op openbare pagina's. Het snelst live.
- **Patroon:** gratis rouleren; betaald schema's per tijdstip, eigen tijd per tab, herstel na een storing, instellingen naar meer schermen.
- **Waarom niet bovenaan:** geen leeg gat maar een volle markt van gratis en middelmatige tools; een nieuwkomer zonder reviews valt daar niet op.

## 3. Google Keep naar Markdown of Obsidian

- **Vraag (GEZIEN, Chris):** 10 aanvullingen ("export all notes", "to obsidian", "to markdown"); zoekbalk bijna leeg (Keep to Markdown Export 175 gebruikers). Mijn meting "google keep export obsidian": niets voor Keep, wel 7 van 10 betaalde exporteurs voor andere diensten (ChatGPT, Claude, Gemini naar Obsidian, tot 5.000 gebruikers; Twitter Bookmarks Export 10.000).
- **Betalen:** niet gezien bij Keep zelf. Takeout geeft Keep gratis als HTML en JSON.
- **Kan het:** Keep heeft geen API voor gewone accounts (GOK). Wel goed te doen en volledig te testen: de Takeout-zip in de extensie openen en omzetten naar Markdown met labels, lijstjes, kleuren als tags, plaatjes en datums.
- **Verdient de koper geld?** Nee.
- **Waarom derde:** makkelijk te vinden, maar zwak betaalbewijs en Takeout is gratis.

## 4. Video's niet vanzelf laten starten (opvolger AutoplayStopper en Disable HTML5 Autoplay)

- **Gat (DERDEN, Vera):** samen 200.000+ gebruikers weg; Reddit: "We desperately need a new video Autoplay stopper" (r/chrome, mei 2025).
- **Concurrentie (GEZIEN, mijn meting):** alles middelmatig: AutoplayStopper (MV3) 10.000, **3,4**; Disable HTML5 Autoplay (M3) 4.000, **1,8**; Disable Autoplay for YouTube 20.000, 3,6. Duidelijk ontevreden gebruikers.
- **Betalen:** 1 van 10 met in-app. Mensen betalen zelden voor zo'n hulpje (GOK).
- **Kan het:** ja, content script bij document_start in alle frames; video in iframes van andere sites is het lastige deel. Goed te testen op eigen testpagina's.
- **Verdient de koper geld?** Nee.
- **Waarom vierde:** goed voor bereik (gratis), zwak voor de eerste euro's.

## 5. Google Foto's in bulk verwijderen of downloaden

- **Vraag en betalen (GEZIEN, Chris):** bewezen: Delete All Google Photos 10.000 (≈ $7 eenmalig), Bulk Edit Google Photos $6,99 per maand tot $199 per jaar, Google Photos Downloader 20.000, $10 per maand.
- **Kan het:** de Photos Library API mag sinds 31 maart 2025 alleen nog bij foto's die de app zelf maakte (GEZIEN, developers.google.com/photos/support/updates: "only list, search, and retrieve albums and media items that were created by your app"), dus het moet via de pagina zelf: breekbaar en voor ons niet te testen zonder inloggen.
- **Waarom vijfde:** vol met twee spelers van 10.000+, en technisch het zwakst voor ons.

## Afgevallen na meting
- **YouTube-beschrijvingen in bulk:** YouTube Studio kan zelf titel en beschrijving van veel video's tegelijk bewerken (GEZIEN, support.google.com/youtube/answer/6249768). Geen gat.
- **LinkedIn in bulk:** LinkedIn verbiedt automatiseren waarschijnlijk in zijn voorwaarden (GOK, niet nagekeken) en de markt is klein (Unpend 646, Chris).
- **Gmail naar PDF, YouTube-reacties:** vol of gratis (Chris).
