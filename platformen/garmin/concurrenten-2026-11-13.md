# Concurrenten van Ebb in de Connect IQ-winkel (13 nov 2026)

Voor: lancering Ebb ($4,99, eenmalig). Alleen de concurrenten en hoe wij ons neerzetten; het algemene deel (hoe mensen apps vinden) doet een andere onderzoeker.
Gelezen op 12 nov 2026 tussen 23:25 en 00:30 UTC, alleen lezen, met curl op de open winkel-API.

## Samenvatting (voor wie weinig tijd heeft)

1. De echte concurrent is één maker: MobileDriveway, met **WHM breathing** (gratis, 50.000+ downloads, 1.730 beoordelingen, 4,8) en **WHM breathing+** ($4,99, 1.000+ downloads, 607 beoordelingen, 4,9). Samen ruim 2.300 beoordelingen; de rest van de ademhoek haalt per app hooguit 150.
2. De plus-versie krijgt nog steeds ±26 beoordelingen per maand (2026); de gratis versie verwijst er zelf naar. Zijn model: alles werkt gratis, de plus-versie is "steun de maker" met wat extra instellingen.
3. Zijn kracht: telt voor je, tempo instelbaar tijdens de sessie, zeer goede opslag in Garmin Connect (inhoudtijd per ronde, eigen grafieken), werkt op 100+ horlogetypes, een maker die luistert. Zijn zwakte: zakelijk en kaal uiterlijk, geen eigen patroon (4-7-8, box), geen trilling bij in én uit, te veel knoppen, vraagt om beoordelingen, niet voor elk horloge.
4. Ebb wint op: trilling per fase met ogen dicht, 4-7-8 en eigen patroon in dezelfde app, een reden om terug te komen (zeedieren voor trouw), bevestiging en veiligheid rond inhouden, nooit om beoordelingen vragen, mooi rond beeld.
5. Ebb verliest op: prijs naast een gratis app die het meeste al doet, maar 28 ronde horloges (geen Instinct, geen vivoactive 3/4, geen oudere fenix), geen tempo wijzigen tijdens de sessie, geen bewezen trouwe groep, geen beoordelingen op dag 1.
6. Neerzetten, één zin: "Ebb is geen teller voor één methode maar een rustig ademmoment met ogen dicht, waar je zee groeit omdat je terugkomt, niet omdat je langer inhoudt."
7. Prijs en proberen: Garmin Pay kent **geen proefversie**, alleen 48 uur terugbetalen (forum Garmin, GEZIEN). Advies: houd $4,99 voor de lancering, maar zet in de eerste weken een tijdelijke lagere prijs als dat in het ontwikkelaarsportaal kan (de concurrent deed dat ook), en bouw voor 1.1 een gratis broertje "Ebb Calm" (alleen 4-7-8, met één dier) dat naar de volle app wijst. Geen ontgrendelcode via een derde partij: dat breekt onze belofte "no unlock code".

Labels: **GEZIEN** = zelf gelezen in de winkel-API of op de genoemde pagina. **AFGELEID** = volgt uit wat ik zag, niet direct zo getoond. **GOK** = eigen inschatting.

## Bronnen (alle GEZIEN, gelezen 12 nov 2026)

- Details per app: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>`
- Beoordelingen: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>/reviews?startPageIndex=<offset>&pageSize=30` (startPageIndex is een beginpositie: 0, 30, 60)
- Zoeken: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords?keywords=<woord>&startPageIndex=0&pageSize=30&sortType=mostRelevant&appType=watch-app`
- Schermafbeeldingen: `https://apps.garmin.com/api/appsLibraryExternalServices/api/screenshots/<screenshotFileId>` (pad gevonden in de script van de winkel, `apps.garmin.com/_next/static/chunks/...`; nieuw, stond nog niet in ons onderzoek)
- Winkelpagina voor mensen: `https://apps.garmin.com/apps/<id>`
- Proefversie bij betaalde apps: https://forums.garmin.com/developer/connect-iq/f/connect-iq-web-store/436796/adding-a-7-day-trial-to-a-garmin-pay-paid-app-what-s-the-official-path en https://forums.garmin.com/developer/connect-iq/f/discussion/439822/paid-ciq-apps
- Eerder onderzoek van ons: `platformen/garmin/onderzoek-ronde-5-2026-11-09.md`, `onderzoek-winkeltekst-2026-11-10.md`, `ontwerp/garmin/ebb-keuring-product-2026-11-12.md`; Ebb zelf: `producten/garmin-adem/winkeltekst.md` v19 en `producten/garmin-adem/manifest.xml` op tak `claude/garmin-2026-11-10b`.

Let op bij de cijfers: "downloads" is de klasse die de winkel toont (10.000+ enzovoort), niet een exact getal. "Laatste update" is `changedDate` uit de API (datum van de laatste wijziging aan de vermelding); bij WHM breathing+ klopt die met de laatste regel in "What's new". "Horloges" is het aantal apparaattypes in `compatibleDeviceTypeIds`.

## 1. De top van de ademapps (watch-apps)

Gekozen uit 527 apps uit 18 zoekopdrachten (breathing, breathwork, breath, box breathing, wim hof, meditation, breathe, apnea, WHM ...), gesorteerd op downloadklasse en aantal beoordelingen. Puur meditatietimers zonder ademgeleiding en apneu-tabellen voor duikers staan onderaan als "buiten de kern". Alles GEZIEN, tenzij anders vermeld.

| # | App (maker) | Prijs | Downloads | Beoord. | Gem. | Laatste update | Horloges | Betaalde ontgrendeling? |
|---|---|---|---|---|---|---|---|---|
| 1 | WHM breathing (MobileDriveway) | gratis | 50.000+ | 1.730 | 4,8 | 15 apr 2025 (v3.65) | 117 | nee; vraagt om de plus-versie of PayPal-gift |
| 2 | WHM breathing+ (MobileDriveway) | $4,99 | 1.000+ | 607 | 4,9 | 20 okt 2026 (v1.58) | 103 | is zelf de betaalde versie |
| 3 | Meditation and Breathwork (FlorianGeigl) | gratis | 10.000+ | 150 | 4,3 | 23 okt 2026 (v11.2.2) | 172 | nee; "buy me a coffee" |
| 4 | JMG-APP Relax HR Coherence (Surfy66) | gratis | 10.000+ | 138 | 4,1 | 5 nov 2026 (v3.22) | 228 | nee (zusje JMG Apnea wel, via code) |
| 5 | Breathing Timer: HRV · BOLT · Wim Hof · 4-7-8 (BreathingTimer) | gratis | 1.000+ | 92 | 4,6 | 27 okt 2026 (v1.12.2) | 180 | nee |
| 6 | Breath trainer (Brucemax) | gratis | 10.000+ | 32 | 3,3 | 28 aug 2026 | 152 | nee; hoort bij een betaalde telefoonapp |
| 7 | Coherence (Walhalla) | gratis | 10.000+ | 30 | 4,3 | 24 okt 2023, wordt niet meer bijgewerkt | 68 | nee |
| 8 | Breathe (Hemanth1984) | gratis | 10.000+ | 24 | 3,5 | 19 mei 2017 | 43 | nee |
| 9 | Breath Training Tool (Bitochi) | gratis | 1.000+ | 21 | 4,9 | 5 okt 2026 | 222 | nee; lokt naar BTS PRO |
| 10 | Breathe: Breathing Exercises (FikirLtd) | $2,99 | 1.000+ | 18 | 4,4 | 6 okt 2026 | 103 | is betaald |
| 11 | Breath Training System PRO (Bitochi) | $6,25 | 100+ | 34 | 4,7 | 18 okt 2026 (v42) | 71 | is betaald |
| 12 | Box Breathing (Dialforge.dev) | gratis in de winkel | 10+ | 0 | - | 3 okt 2026 (v1.0.0) | 77 | ja: 30 dagen gratis, dan code van 4,99 EUR via eigen site |

Ids (voor de URL's hierboven): 1 a4f7e008-af89-4cdb-8368-f0df16e48ebb, 2 3543ef5f-a9ea-48ed-a0dd-925155e9c7b5, 3 e6f3f3d2-3ea6-4ec1-81a5-977c708eb75b, 4 c990bcfb-4156-4c5a-82ce-e18434cc2872, 5 59828c15-7638-4e14-b871-47f0ce0c66f0, 6 51f4bc9a-d399-45ab-983d-9d879e40867b, 7 70e5b7df-8105-42b8-99a4-ed3365333ad1, 8 ddc5823b-1ba5-4d09-9a0c-b54e5e716bfc, 9 7190365c-13f5-4789-ba3e-1f1feac42409, 10 93b31a7d-4500-41f8-a2de-9e91c9bcf86f, 11 12b88972-bc50-40c7-a138-e1e8d6f38068, 12 fcd58abc-9153-419e-9aa4-68cae96cc574.

Buiten de kern (GEZIEN): Meditate (dliedke, 10.000+, 138, niet meer onderhouden, opgevolgd door nr. 3), Meditate (vtrifonov, 10.000+, 137), JMG-APP Apnea Training (10.000+, 82, statistieken met code), Static Apnea Training Tables (1.000+, 50, laatste update 2023), DeepBreath - Wim Hof Breathing and Cold (1.000+, 7). Klein maar qua idee dichtbij: **Jelly – a jellyfish for stress and breathing** (OmniSky, gratis, 10+, 0 beoordelingen, 8 nov 2026): een kwal als huisdier die groeit van rustige dagen, met vijf ademoefeningen. Id a460e891-6d06-4bea-be04-652d2b522b7d. Het "dier dat groeit"-idee is dus niet helemaal van ons alleen, maar Jelly heeft nog geen bereik.

### Wat ze doen en hoe ze eruitzien (schermafbeeldingen bekeken, GEZIEN)

1. **WHM breathing** (gratis): rondes van snel ademen, inhouden na uitademen, korte inhouding na inademen; timer en hartslag; slaat op in Connect met eigen grafieken (rondes, ademhalingen, langste inhouding, fase-grafiek). Beelden: vier kale schermen op een fenix: zwart, groot wit getal (3.0 SEC tempo, teller 17, timer 1:07), regel "breathe in and out", eronder een tabelletje per ronde (#1 33 2:07 0:15) en een rood hart met hartslag. Eén scherm wit, één met een blauwe gloed. Zakelijk, als een stopwatch.
2. **WHM breathing+** ($4,99): hetzelfde plus: trilwaarschuwing 3 ademhalingen voor het einde, touchscreen uit, details per ronde in Connect, eigen tussenpozen voor de tril tijdens inhouden, trilsterkte, geluiden. Beelden: dezelfde stijl, blauwe gloed, tabel met rondes, hartslag 70 en 162. Taalfouten in de tekst ("warnig", "predifined").
3. **Meditation and Breathwork**: meditatie en adem met sessies die je zelf instelt, HRV en stress live en erna; sinds v11 "breath ball" en sessies als 4-7-8, coherence, sleep. Beelden: horloge voor een blauwe lucht met wolken en lotus; grafieken van stress en HRV, een groene aftelring "Relax to start", een instellingenmenu. Rijk aan meten.
4. **JMG-APP Relax HR Coherence**: hartcoherentie, hartslag omlaag brengen, RSA-score. Franstalig eerst. Beelden: brede reclameplaten met horloge en grafieken.
5. **Breathing Timer**: 7 programma's (Resonant 5.5, box, 4-7-8, Buteyko, Wim Hof-achtig, BOLT-test), tot 8 eigen routines, trilpatronen per fase "eyes closed", advies op basis van Body Battery. Beelden: drie verzorgde platen, donkerblauw, met kop "Train your nervous system. One breath at a time.", ring "Inhale 4 of 4", lijst met protocollen, pictogrammen "No account, Privacy first". De best verkochte vormgeving van de gratis apps.
6. **Breath trainer**: alleen een scherm met hartslag en zuurstof voor een telefoonapp. Eén schermafbeelding.
7. **Coherence**: ademen op vast tempo met hartslag, RSA-score. Bron kwijt, wordt niet meer bijgewerkt.
8. **Breathe** (2017): eenvoudig in, vast, uit. Niet meer bijgewerkt sinds 2017, maar heeft 10.000+ door de naam.
9. **Breath Training Tool**: gratis lokker voor BTS PRO: geanimeerde gids, eigen ritme; volgens "What's new" zonder volle Connect-opslag.
10. **Breathe: Breathing Exercises** ($2,99): 11 patronen (box, 4-7-8, cyclic sigh, coherent, ook "Pregnancy 3-6" zonder inhouden), cirkel die groeit, eigen tril per fase, opslag als Breathwork met hartslag, "No phone, no account, no internet. One-time purchase". Beelden: vijf portretplaten, zwarte ronde schermen met gele cirkel en tekst, onderschrift per plaat ("Follow the circle", "Saves to Garmin Connect"). Deze app lijkt qua belofte het meest op Ebb Calm.
11. **BTS PRO** ($6,25): freediving- en apneucoach: CO2/O2-tabellen, persoonlijk record, 9 trainingsplannen, readiness, "Wim Hof Power". Beelden: vijf brede donkere platen vol kleine schermen en grafieken ("Know your body", "PB prediction"). Precies de kant die wij bewust niet opgaan.
12. **Box Breathing** (Dialforge): box, 4-7-8, coherent, eigen patroon, vierkant met bewegende stip, eindscherm "HR start / HR end 72 -> 64". Beelden: vijf grijze platen, kop "BOX BREATHING", horloge met wit vierkant. 28 talen. Staat bij "breathing" op 1 (zie deel 6).

## 2. De grote concurrent in detail: MobileDriveway

### Gratis tegenover betaald (GEZIEN, beschrijvingen)
- **Gratis WHM breathing** doet alles wat de methode nodig heeft: tempo per ademhaling in tienden van seconden, tempo wijzigen tijdens de sessie, automatisch stoppen na een aantal ademhalingen en na de tweede inhouding, trillen elke 30 s bij inhouden en elke 15 s bij de tweede inhouding, witte of zwarte achtergrond, opslaan in Connect met eigen grafieken. De tekst zegt letterlijk dat de app "100% functional and free" is en vraagt om de plus-versie "to support the development", met een PayPal-link als alternatief.
- **WHM breathing+** voegt alleen instellingen toe: waarschuwing voor het einde van het ademen, touchscreen negeren, details per ronde in Connect, tussenpozen voor de tril bij inhouden, trilsterkte, geluiden. En: "I'll also be more responsive to implementing new features requests there".
- **Hoe hij verdient**: $4,99 eenmalig voor de plus-versie; de gratis versie wijst er in de beschrijving en in "What's new" naar ("introductory price on the PLUS version for the first month!"). Daarnaast giften via PayPal. Hij gebruikt dus een tijdelijke lagere prijs bij de start (GEZIEN in tekst; hoe hij dat in het portaal deed: niet gezien).
- **Horloges**: de gratis versie werkt op 117 apparaattypes, de plus op 103. Kopers klagen dat de plus niet op hun horloge werkt (vivoactive 3, Instinct 3 Tactical, FR965 bij aankoop) en een koper schrijft dat de gratis versie zijn nieuwe fenix 7 Pro niet meer ondersteunde, zodat hij de plus kocht (GEZIEN, beoordelingen 14 okt 2026, 12 okt 2026, 12 jan 2025, 11 nov 2025). AFGELEID: nieuwe horloges komen soms alleen in de plus, wat kopen duwt.
- **Is het de officiële Wim Hof-app?** Nee. De tekst zegt "similar to the one used by Wim Hof (WHM)"; de maker maakt ook weer-apps (eerder onderzoek, GEZIEN).

### Hoe groot (GEZIEN, alle beoordelingen opgehaald)
- Plus: 607 beoordelingen, 543 keer 5 sterren, 3 keer 1 ster; gemiddeld 4,86; maar 62 met tekst. Per maand in 2026: 31, 35, 16, 24, 26, 18, 17, 33, 32, 29 (jan tot okt). De maker antwoordde op 24.
- Gratis: 1.730 beoordelingen, gemiddeld 4,84, 220 met tekst. Per maand in 2026 dalend van 24 (jan) naar 9 tot 11 (aug tot okt).
- AFGELEID: de plus groeit niet uit zoekverkeer maar uit de gratis basis. GOK: met 1.000+ downloads en 607 beoordelingen zit de plus waarschijnlijk tussen 1.000 en 5.000 kopers, dus grofweg $3.000 tot $17.000 bruto in bijna twee jaar. Niet na te gaan.

### Bijwerken (GEZIEN, "What's new")
- Plus: 26 dec 2024 start, daarna 20 jan, 13 feb, 3 mrt, 14 apr, 7 sep 2025 en 20 okt 2026 ("Added new watches"). In 2026 dus alleen nieuwe horloges.
- Gratis: 2022 elke paar weken, daarna maart 2024 (nieuwe animatie) en 15 apr 2025. Sindsdien niets.
- AFGELEID: de maker is goed maar traag geworden; in ruim een jaar geen nieuwe functie.

### Wat gebruikers schrijven (282 beoordelingen met tekst van beide versies samen gelezen; parafrases, GEZIEN)

Vijf vaakst genoemde pluspunten:
1. Het tellen valt weg; je kunt je op het ademen richten en hebt de telefoon niet meer nodig (bijv. 3 okt 2025 "Zählen im Kopf fällt weg", 11 nov 2026 "zonder telefoon in de buurt").
2. Veel in te stellen, vooral het tempo, ook tijdens de sessie.
3. Alles staat in Garmin Connect: inhoudtijd per ronde, hartslag, stress.
4. Eenvoudig en betrouwbaar, elke dag gebruikt; "beter dan de officiële telefoonapp".
5. Maker luistert en voegt gevraagde functies toe; gratis.

Vijf vaakst genoemde klachten en wensen:
1. **Trilling of geluid bij elke in- en uitademing**, zodat het met ogen dicht kan (minstens 10 keer, van 2022 tot 2025; bijv. 3 jun 2025 "ogen dicht en hoofd leeg").
2. **Zuurstof (SpO2) meten tijdens of na het inhouden** (minstens 15 keer). Zie deel 4: niet volgen.
3. **Te veel knoppen**: drie keer drukken om te starten, steeds drukken tussen rondes; wens om een vast aantal rondes in te stellen zodat de sessie vanzelf eindigt (minstens 8 keer).
4. **Werkt niet (goed) op mijn horloge**: plus niet beschikbaar, "IQ"-foutteken op FR265, vastlopen; daarbij ook batterijverbruik (minstens 10 keer).
5. **Eigen patroon met losse tijden voor in, vast en uit** (box, 4-7-8, langere uitademing) ontbreekt (bijv. 13 apr 2025: kocht hem, maar kon geen in-vast-uit-patroon maken, 2 sterren; 19 apr 2025 in 3 s, uit 6 s).

Verder genoemd: niet om beoordelingen zeuren (16 aug 2026, 3 sterren: "harassed to provide feedback"), oude resultaten op het horloge terugzien (26 aug 2025, 2 sterren), bevestiging vragen voor weggooien (2 jul 2023: vier, vijf keer per ongeluk weggegooid), koude douche of ijsbad bijhouden (vaak), opslaan zonder activiteit in Strava, niet zo mooi vormgegeven (13 mrt 2025 "not the best graphically designed").

### Wat ontbreekt bij hem (AFGELEID uit tekst, beelden en beoordelingen)
Rustig ademen met een patroon (4-7-8, box), trilling per fase, een reden om terug te komen anders dan je eigen cijfers, veiligheid rond inhouden (alleen een tril elke 30 s; geen plek-waarschuwing in de app gezien), andere talen dan Engels, verzorgd beeld, een overzicht op het horloge.

### Andere concurrenten in hun beoordelingen (kort, GEZIEN)
- Meditation and Breathwork: HRV wordt vaak niet gemeten ("HRV waiting"), lastig te programmeren, scherm te fel in het donker, onduidelijk wanneer in of uit (28 sep 2025).
- Breathing Timer: vastlopers met "IQ" op Venu, eigen routines worden niet bewaard op horloges zonder menuknop, wens om licht uit te kunnen.
- Breathe (FikirLtd): wens om de duur te kiezen en meer patronen; eerdere klacht over geen trilling is opgelost.
- BTS PRO: "proeftijd al voorbij bij de eerste start" (9 okt 2026, 1 ster), verwarrend, harde geluiden.

## 3. Ebb tegenover de top 3

Top 3 voor Ebb: WHM breathing (gratis leider), WHM breathing+ (zelfde prijs) en Breathe van FikirLtd (betaalde rustige ademapp met de belofte die het dichtst bij Ebb Calm ligt). Ebb volgens winkeltekst v19 en manifest; niet op een echt horloge gezien.

| Functie | Ebb ($4,99) | WHM breathing (gratis) | WHM breathing+ ($4,99) | Breathe, FikirLtd ($2,99) |
|---|---|---|---|---|
| Rondes snel ademen met inhouden | ja | ja | ja | nee |
| Tempo wijzigen tijdens de sessie | nee (in de instellingen) | ja | ja | nee |
| 4-7-8 | ja | nee | nee | ja |
| Eigen patroon in-vast-uit-vast | ja (My pattern, in instellingen) | nee | nee | nee (vaste 11 patronen) |
| Trilling per fase, ogen dicht | ja, eigen tril per fase, laatste 3 ademhalingen anders | nee, alleen tijdens inhouden | deels: waarschuwing voor het einde, tril bij inhouden instelbaar | ja |
| Geluid | nee | ja | ja, keuze | GOK: nee |
| Vast aantal rondes, vanzelf door | ja (rondes in de instellingen) | deels (auto-einde per fase) | deels | n.v.t. |
| Opslaan in Connect | ademactiviteit, hartslag, lap per ronde met inhoudtijd | activiteit met eigen grafieken | idem plus details per ronde | Breathwork met hartslag |
| Overzicht op het horloge | ja (Today, 8 weeks) | vorige sessie op startscherm | idem | nee |
| Reden om terug te komen | 24 zeedieren voor sessies en weken op rij | nee | nee | nee |
| Veiligheid inhouden | waarschuwing vooraf, "breathe" na 3:00, tril blijft, stopt na 5:00 | tril elke 30 s | idem, instelbaar | geen inhouden in rust-patroon |
| Touchscreen uit tijdens sessie | ja, vast | nee | ja, instelling | onbekend |
| Om beoordeling vragen | nooit | in de tekst om geld | volgens een koper wel | onbekend |
| Talen in de winkel | en, de, nl (app Engels) | en | en | en |
| Horloges | 28, alleen rond | 117 types | 103 types | 103 types |
| Beoordelingen op dag 1 | 0 | 1.730 | 607 | 18 |
| Uiterlijk | rond "patrijspoort", zee, dieren | kale stopwatch | idem | gele cirkel op zwart |

Waar Ebb aantoonbaar anders of beter is (AFGELEID uit de tabel): de enige van de vier die rondes én 4-7-8 én eigen patroon in één app heeft, met tril per fase; de enige met een reden om terug te komen; duidelijkste veiligheid; vraagt nooit om beoordelingen.
Waar Ebb slechter is: prijs tegen gratis; geen tempo wijzigen tijdens de sessie; geen geluid; veel minder horloges; geen geschiedenis van beoordelingen; geen eigen grafieken in Connect (wel laps); voor wie alleen de methode wil telt de gratis app al alles.

**De ene zin (neerzetten):** "Ebb is geen teller voor één methode maar een rustig ademmoment met ogen dicht, waar je zee groeit omdat je terugkomt, niet omdat je langer inhoudt."
Engelse kern voor de winkel (voorstel, GOK dat dit werkt): "Breathe with your eyes closed. Your sea grows because you come back, not because you hold longer."
Daarmee vergelijkt de koper Ebb niet met "WHM breathing maar duurder", maar met een gewoonte-app. Doelgroep: wie wil beginnen of volhouden (en 4-7-8 voor het slapen wil), niet de gevorderde die zijn inhoudtijd volgt.

## 4. Klachten die Ebb oplost, wat in 1.1 kan, en wat we niet volgen

Lost Ebb nu al op (AFGELEID uit winkeltekst v19):
- Trilling per fase met ogen dicht (klacht 1 bij de leider).
- Eigen patroon en 4-7-8 (klacht 5).
- Vast aantal rondes in de instellingen (deel van klacht 3).
- Niet om beoordelingen vragen.
- Touchscreen doet niets tijdens ademen en inhouden.
- Overzicht op het horloge (Today, 8 weeks).
- Vraag voor weggooien: staat als MOET in de productkeuring van 12 nov punt 1; nagaan of dat in de ingeleverde bouw zit.

Met weinig bouwwerk in 1.1 (GOK op de moeite):
1. Tempo omhoog of omlaag met UP/DOWN tijdens de rondes (pluspunt 2 bij de leider; zijn kopers noemen dit "the update that was needed").
2. "My pattern" als derde keuze in het menu (stond al op de 1.1-lijst van de keuring).
3. Korte sessie (2 rondes, of Calm van 3 minuten) en de duur van Calm kiezen (wens bij FikirLtd en de leider).
4. Na de laatste ronde vanzelf door naar 1 minuut rustig ademen (wens 26 apr 2023 bij de leider), telt dan ook mee voor Calm.
5. Kiezen of een sessie wordt opgeslagen als activiteit (Strava-klacht).
6. Meer horloges: fenix 7S/Pro S, FR255S, Venu 2S, epix 2, Instinct 3 AMOLED (rond). Kopers van de leider kopen op horlogebeschikbaarheid. Elk horloge vraagt wel een opname en keuring.
7. Andere talen in de app zelf (de leider is alleen Engels).

NIET volgen (botst met onze regels: nooit langer inhouden belonen, geen medische claims, geen freediving):
- SpO2 of "hypoxie-niveau" tonen tijdens het inhouden: maakt van inhouden een meting om op te jagen, en zuurstofwaarden suggereren een medische betekenis.
- Inhoudtijd per ronde automatisch laten oplopen (30, 60, 90 s; wens 29 dec 2024), records of "personal best": beloont langer inhouden.
- CO2/O2-tabellen en freediving-plannen (BTS PRO, JMG): hoort bij apneutraining.
- Koude douche of ijsbad bijhouden direct na de rondes: combinatie van hyperventileren en koud water is precies wat onze veiligheidstekst afraadt.
- HRV- of stressscores als oordeel: geen medische claims; de 1-sterren bij Meditation and Breathwork laten ook zien dat HRV vaak niet werkt.
- De naam van de methode gebruiken in titel of reclame.

## 5. Prijs en proberen

### Wat de betaalde ademapps vragen (GEZIEN, details 12 nov; deels uit `onderzoek-winkeltekst-2026-11-10.md`)
- WHM breathing+ $4,99 eenmalig, geen proef; proberen gebeurt via de gratis broer.
- Breathe (FikirLtd) $2,99, geen proef; heeft ook een gratis "Breathe Free: Box Breathing" (100+, 5 beoordelingen).
- BTS PRO $6,25; gratis lokker Breath Training Tool.
- HRV Breathing (Oltek) $3,99, Kids Breathing $4,49, BREATHWORK $4,49, Breathwork (Kegles) $1,99, BreathGym $1,99, Breath and Plunge PRO $2,99 (10 nov, eerder onderzoek).
- Box Breathing (Dialforge) gratis in de winkel, 30 dagen proef, dan 4,99 EUR via code op eigen site.
- AFGELEID: elke betaalde ademapp met echt bereik heeft een gratis instap ernaast (eigen gratis broer of lokker). Geen enkele zonder gratis instap komt boven 100+ uit, behalve FikirLtd met 1.000+.

### Wat Garmin technisch biedt
- Betaald via Garmin Pay (zoals Ebb): **geen proefversie**, alleen 48 uur terugbetalen. De oude `AppBase.isTrial()` hoort bij een systeem uit 2017 en werkt niet met Garmin Pay (forum Garmin, antwoord van een vaste helper, geplaatst ongeveer juni 2026 volgens "5 months ago"; https://forums.garmin.com/developer/connect-iq/f/connect-iq-web-store/436796/adding-a-7-day-trial-to-a-garmin-pay-paid-app-what-s-the-official-path). GEZIEN; officieel antwoord van Garmin niet gezien.
- In de API heeft elke app `hasTrialMode` (bij alle 16 bekeken apps false) en de prijs heeft een `salePrice` naast `listPrice` en een veld `appliedPromotionGuids` (GEZIEN). AFGELEID: Garmin kent tijdelijke aanbiedingen; MobileDriveway schreef "introductory price on the PLUS version for the first month". Of en hoe dat in het portaal kan: niet gezien, Thijs kan het zien in het portaal.
- Proef via derden (KiezelPay) kan wel, met elke proeftijd, maar de app staat dan als gratis vermelding en ontgrendelt met een code buiten de winkel (forum, GEZIEN). Dat breekt onze belofte "no unlock code by e-mail" en de klachten erover zijn bekend (BTS PRO 9 okt 2026, eerder onderzoek over jaarabonnementen).

### Drie opzetten

**A. Betaald $4,99 met 48 uur terugbetalen (zoals nu).**
Voor: eenvoudig, eerlijk, past bij de tekst, elke download is geld; gelijk aan de leider-plus, dus geen "goedkope" indruk. Na: niemand kan proberen; naast een gratis app met 1.730 beoordelingen en een Ebb met 0 beoordelingen is de drempel hoog; betaalde nieuwkomers halen in 1 tot 2 maanden maar in ±9% van de gevallen 100+ (`onderzoek-thijsger-2026-11-10.md`). Techniek: niets extra.

**B. Gratis broertje plus de betaalde Ebb (model van de leider).**
Bijvoorbeeld "Ebb Calm" gratis: alleen 4-7-8 met de zee en één dier, en in de tekst en op het eindscherm (zonder druk, één regel) dat de volle Ebb rondes, eigen patroon en 24 dieren heeft. Voor: dit is aantoonbaar het model dat werkt in deze hoek (WHM, Bitochi, FikirLtd); de gratis app verzamelt beoordelingen en zoekverkeer. Na: tweede vermelding om te onderhouden en te keuren; gevaar dat de gratis versie genoeg is; wij moeten zorgen dat het gratis deel geen inhouden bevat, anders verspreiden we het risicodeel gratis. Techniek: gewoon een tweede app-id in de winkel; geen betaalsysteem nodig.

**C. Lagere startprijs ($2,99 de eerste maand, daarna $4,99).**
Voor: verlaagt de drempel juist als er nog geen beoordelingen zijn; de leider deed hetzelfde. Na: wie later $4,99 ziet, ziet geen bewijs dat het meer waard is; kleine opbrengst per koper; onzeker of Garmin dit per app toelaat. Techniek: `salePrice` bestaat in de API; in het portaal nakijken.

Afgevallen: gratis met ontgrendeling via code of KiezelPay (breekt de belofte, kost vertrouwen).

**Advies (GOK, met onderbouwing):** lever morgen in zoals het is (A), want inleveren wachten kost meer dan het oplevert. Kijk direct of het portaal een tijdelijke aanbiedingsprijs toelaat en zet die zo ja voor de eerste 30 dagen (C, $2,99). Bouw als eerste werk na de lancering B: een gratis Ebb Calm zonder inhouden. Dat is de enige opzet waarvan we in deze hoek zien dat hij tegen een gratis leider op werkt. $4,99 zonder enige gratis instap is naast een gratis leider niet verstandig voor de lange duur, wel acceptabel voor de eerste weken.

## 6. Titel en zoekwoorden

Huidige top bij `mostRelevant`, alleen watch-apps (GEZIEN, 12 nov 23:55):
- **breathing**: 1 Box Breathing (Dialforge, 10+), 2 HRV Breathing, 3 Tactical Breathing, 4 Breathing Assistant, 5 Breathing Exercises (liamb09), 6 WHM breathing+, 7 WHM breathing, 8 Breathing Exercises (SimonSteinhuber).
- **breathwork**: 1 Breathwork (Kegles), 2 BREATHWORK, 3 Breathwork (No_Try_Hard), ... 6 Meditation and Breathwork.
- **breath hold**: 1 BreathGym - Breath Hold Trainer, 2 Breath Hold Trainer, 3 StatiQ, 4 Breath – Guided Breathing, HRV & Breath Holds, 5 Breath Hold Coach (Dialforge) ... allemaal 100 downloads of minder. Geen sterke app staat hier bovenaan.
- **breath training**: 1 Breath Training (Deyve), ... 4 Breath Training Tool (Bitochi).
- **box breathing**: 1 Box Breathing (Dialforge), 2 Breathe: Box Breathing, 3 Breathe Free: Box Breathing.
- **breathing exercises**: 1 en 2 "Breathing Exercises", 3 Breathe: Breathing Exercises (FikirLtd).
- **wim hof**: 1 Дыхание Wim Hof, 2 DeepBreath - Wim Hof ..., 4 Breathing Timer. De WHM-apps staan hier niet bovenaan.
- **calm**: 1 Peacehabit — Breathing & Calm, 2 Deep Calm Breathing, 3 Meditation and Breathwork, 5 Jelly.
- **relaxation**: alleen kleine apps (Relaxation Feedback Aid, PMR, ZenFlow).
- **"4-7-8"** met streepjes geeft **0 treffers**; **"478"** geeft 6 treffers (1 Breath 478). AFGELEID: de zoeker kan niet met "4-7-8" overweg, dus "4-7-8" in de titel levert bij zoeken op dat woord niets op; het helpt alleen wie de titel leest.

Wat dit zegt:
- Wie het woord in de titel heeft, staat boven; downloads en beoordelingen tellen nauwelijks (bevestigt `onderzoek-winkeltekst-2026-11-10.md`). Dialforge staat met 10 downloads op 1 bij "breathing", "box breathing", "sea breathing" en zelfs "breathing game". GOK: de 28 vertaalde beschrijvingen of de exacte titel helpen.
- Ruimte voor Ebb (GOK op de volgorde): **"breath hold"** (alleen kleine apps, en het staat al in onze titel als "Breath Hold Rounds"), **"calm"** en **"relaxation"** (zwak bezet, en passend bij Calm 4-7-8), **"breathing exercises"** (de exacte woordgroep in de titel wint daar). "breathing" is druk; daar staan we met het woord vooraan in de titel naar verwachting tussen de apps met "Breathing" in de naam.
- Voorstel (voor een volgende titelwijziging, niet voor morgen): `Ebb: Breathing Exercises, Breath Hold & Calm` (41 tekens) in plaats van `Ebb: Breathing, Breath Hold Rounds & 4-7-8`. Dan pakken we "breathing exercises", "breath hold" en "calm", en laten we "4-7-8" (levert bij zoeken niets op) naar de tekst gaan, met daarbij ook "478" in de tags. Eerst nakijken of de zoeker ook op woorden in de beschrijving van andere talen let (Duitse en Nederlandse tekst), voor "Atemübungen" en "ademhalingsoefeningen".
- Niet doen: "Wim Hof" of "WHM" in titel of tekst (merk, en onze regel).

## Wat ik niet kon nagaan

- Hoe Ebb er op een echt horloge uitziet en of de tril per fase goed voelt; alles over Ebb komt uit de winkeltekst v19 en het manifest.
- Of de vraag voor weggooien (keuring 12 nov, punt 1) in de ingeleverde bouw zit.
- Echte verkoopaantallen van de concurrenten (de winkel toont alleen klassen); de schatting van kopers is een GOK.
- Of Garmin per app een tijdelijke aanbiedingsprijs toelaat en hoe (alleen velden in de API en de zin van de concurrent gezien; het portaal is niet bekeken, want we loggen niet in).
- Officieel Garmin-antwoord over proefversies bij Garmin Pay; alleen het forum.
- De winkelpagina voor mensen zelf (script); alles via de API gelezen. Van JMG Relax, Breath trainer, Coherence en Breathe (2017) heb ik de schermafbeeldingen niet bekeken, alleen tekst en cijfers.
- Of de zoeker in de app op het horloge of in de Connect IQ-telefoonapp dezelfde volgorde geeft als de website-API.
