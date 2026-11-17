# Spraakmemo op Garmin: de dichtstbijzijnde apps (concurrentiecheck, deel 1)

Gijs, 17 nov 2026 ±10:25 UTC, run 136. Bron: de meting van Noor (`platformen/pionier/data/garmin-audio-2026-11-17.json`, 17 apps met het recht `AudioInput`) en de winkelgegevens per app, door mij met curl gelezen om ±10:17 UTC (`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>`). Alles hieronder GEZIEN in die gegevens, tenzij er iets anders bij staat. Downloads toont de winkel in klassen (1, 10, 100).

## De zes die het dichtst bij een spraakmemo zitten

| App | Wat het doet | Waar blijft het geluid | Prijs | Downloads, reviews | Horloges |
|---|---|---|---|---|---|
| **Chui** (0.1.2-early) | Memo inspreken, komt als tekst en nette notitie in je Chui-account | Naar hun dienst, via de telefoon. Zonder telefoon stopt een opname na 2 minuten en wacht op het horloge tot hij verstuurd kan worden | gratis (account nodig) | 1, 0 | 34 |
| **SayNote AI** (V1.4) | Inspreken wordt tekst (tot 60 s), plus AI-vragen met eigen sleutel | Naar een dienst voor herkenning; "the audio is deleted right after recognition, only the text is kept" | gratis, 20 keer per dag | 10, 2 | 126 (typen op horloges zonder microfoon) |
| **WristMemo** (1.0.0) | "Private voice memo app for personal testing", stuurt naar de eigen server van de maker | Eigen server van de maker | gratis | 1, 0 | 2 |
| **Voxwrist Ask** (2.0.7) | AI-assistent met stem, dagoverzicht, herinneringen met stem | Naar OpenAI of Gemini met een eigen sleutel | gratis | 10, 2 | 26 |
| **WristVoice AI** (2.0.39) | AI-vragen met stem, antwoord terug met stem | Naar hun dienst (OpenAI), met abonnement | gratis app, abonnement | 10, 1 | 26 |
| **WristTalk** (1.6.0) | Stem voor Home Assistant | Naar de eigen Home Assistant van de gebruiker | gratis | 1, 0 | 2 |

Verder in de meting, verder weg: AllTelegram (100 downloads, 8 reviews, spraakberichten in Telegram), Remote for Claude ($2,99), AI Buddy, AI Question, twee stemapparaten voor gitaar, twee geluidsmeters ($0 en $1,99).

## Wat valt op

1. **Niemand speelt een memo terug af op het horloge.** Alle zes sturen het geluid weg: naar een dienst, een account, een sleutel of een eigen server. Bij SayNote wordt het geluid zelfs meteen gewist.
2. **Niemand werkt zonder telefoon of account als belofte.** Chui komt het dichtst (wacht op het horloge tot de telefoon er is), maar stopt dan na 2 minuten en vraagt een account.
3. **Niemand vraagt eenmalig geld voor een memo-app.** De betaalde in deze hoek zijn een afstandsbediening ($2,99) en een geluidsmeter ($1,99). De AI-apps kosten de maker geld per gebruik en leunen op een abonnement of een eigen sleutel.
4. **Aantal horloges:** 26 of 34 bij de apps die alleen op horloges met microfoon staan. Dat is dus haalbaar, ook voor ons (zie `spraakmemo.md`).
5. **Les uit de tekst van Chui:** "Recording stops if the watch cannot reserve more storage" en "Garmin stops microphone recording when you leave the app". Twee grenzen die wij ook hebben en die wij ook eerlijk moeten tonen.

## Wat hebben wij dat zij niet hebben

**Je memo blijft van jou en je hoort hem terug op je pols: geen account, geen telefoon, geen abonnement, geen dienst die meeluistert.** Eén knop, praten, klaar, met tijd, duur en plek erbij. Dat doet op dit moment geen enkele van de zeventien.

De keerzijde, eerlijk: wij maken er geen tekst van en de memo komt niet op je telefoon. Wie dat wil, kiest Chui of SayNote. Onze koper is de hardloper, wandelaar of vakman die onderweg iets wil vasthouden en het later op de pols terug wil horen.

## Nog niet gedaan (volgende run)

- Wat er **aankomt**: het forum van Garmin (Showcase), r/Garmin en r/GarminWatches, GitHub op `Audio.Capture`. Niet gezocht in deze run.
- Of Garmin zelf een memo-app op deze horloges heeft staan (de ingebouwde spraaknotities). Op de fēnix 8 bestaat "Voice Notes" (GOK uit mijn geheugen, niet nagelezen): als dat op alle horloges met microfoon zit, is de basistaak al bezet en moeten wij iets hebben dat die niet heeft (de plek, een lijst per dag, sneller starten). **Dit is het belangrijkste open punt voor de keuze en gaat voor het ontwerp.**

# Deel 2: de ingebouwde spraaknotitie van Garmin zelf (17 nov 2026 ±15:05 UTC, run 137)

Opdracht van de hoofdchat (17 nov ±15:10 NL): per horloge met microfoon nakijken of Garmin zelf al een spraaknotitie heeft, met bron. Alles met curl gelezen op 17 nov tussen ±14:57 en ±15:02 UTC. Handleidingen: `https://www8.garmin.com/manuals-apac/webhelp/<horloge>/EN-SG/` (lijst van alle onderwerpen in `suitehelp_topic_list.html`) en de Amerikaanse onder `https://www8.garmin.com/manuals/webhelp/GUID-.../EN-US/`.

## Uitkomst in één zin

**Op elk horloge met microfoon waar een app van ons de microfoon mag gebruiken, zit al een gratis spraaknotitie van Garmin. Horloges met microfoon zonder ingebouwde notitie: 0 gevonden** (MARQ Gen 3 niet kunnen nalezen).

## Wat de ingebouwde notitie doet (GEZIEN, handleiding fēnix 9, onderwerp "Recording a Voice Note")

"You can record and listen to voice notes using your watch's built-in speaker and microphone." Daarna: Voice Notes kiezen, opnemen, stoppen. Keuzes: "Select Location to save your GPS location with the voice note", volume, afspelen, "rename or delete the voice note", "view the voice note location on the map" (die laatste alleen in de handleiding van de fēnix 9 gezien) en "view your voice note library". Dat is precies onze versie 1: opnemen, terugluisteren, lijst, plek.

Garmin op het eigen forum (DERDEN, medewerker "Garmin - CF", Forerunner 970): "Voice notes are saved on the watch and are not synced to a Garmin Connect account." De vraag daar was of je de notities zonder kabel op telefoon of computer krijgt. Met kabel kan het dus kennelijk wel (GOK, niet nagelezen); onze app kon dat niet eens.

## Per horloge uit de lijst van Garmin voor `Toybox.Audio`

| Horloge | Microfoon | Ingebouwde spraaknotitie | Bron |
|---|---|---|---|
| fēnix 9 (alle maten, Pro, Pro Solar) | ja | **ja**, met plek en kaart | GEZIEN: `manuals-apac/webhelp/fenix9/EN-SG/GUID-617B3550-7CDD-44DE-8502-3F60B1423D1C-1876.html`; ook Amerikaanse handleiding `GUID-708A8F4D-9A78-49CF-9528-DE109BBCC472` |
| fēnix 8 (43, 47, 51 mm, Solar, Pro) | ja | **ja**, met plek | GEZIEN: `manuals-apac/webhelp/fenix8series/EN-SG/GUID-6913D7F6-598C-4F20-A54F-CAF9B0C8B896-5443.html`. Sept 2026 nog verbeterd (DERDEN, Notebookcheck 9 sep 2026: opnemen via oordopjes hersteld) |
| Venu 4 (41 en 45 mm) | ja | **ja**, met plek | GEZIEN: `manuals-apac/webhelp/venu4/EN-SG/GUID-3E5A7CDA-B9E8-4299-A868-DA4CAEAB6EFC-8552.html` |
| Venu X1 | ja | **ja**, met plek | GEZIEN: `manuals-apac/webhelp/venux1/EN-SG/GUID-A5C1BDDB-367C-48BB-9ECB-C010006BDC3F-9108.html` |
| Forerunner 570 (42 en 47 mm) | ja | **ja** | GEZIEN: Amerikaanse handleiding "Forerunner 570 Series, Recording a Voice Note", `manuals/webhelp/GUID-25E3235D-44D2-4384-A591-DD1D71BEBCB1/EN-US/GUID-34D838BC-FC83-4173-A364-5D7BAEA3792C.html`. Kwam met een update ("Supports the voice notes app", DERDEN, Notebookcheck). De handleiding voor Azië noemt het nog niet (alle 241 pagina's doorzocht, 0 keer "voice note") |
| Forerunner 970 | ja | **ja** | DERDEN: medewerker van Garmin op het forum van de Forerunner 970 (zie boven) en dezelfde update. Handleiding voor Azië noemt het niet (255 pagina's, 0 keer) |
| Approach S72 (43 en 47 mm) | ja | **ja** | GEZIEN: `manuals/webhelp/GUID-91BDFC0A-876D-451A-AF8E-8DD63A4D6B85/EN-US/Approach_S72_OM_EN-US.pdf`, hoofdstuk "Recording a Voice Note" |
| D2 Mach 2 (en Mach 2 Pro) | ja | **ja** | GEZIEN: "D2 Mach 2 Series, Recording a Voice Note", `manuals/webhelp/GUID-EA112C95-8563-4EED-AADF-2AADFBB95646/EN-US/GUID-34D838BC-FC83-4173-A364-5D7BAEA3792C.html`. Of de Pro in dezelfde handleiding valt: GOK |
| MARQ (Gen 3) | ja (DERDEN, gadgetsandwearables.com) | **niet kunnen nalezen**, GOK ja: alle andere horloges met microfoon van 2025 en 2026 hebben het | geen handleiding gevonden |
| Enduro 3 | **nee** | n.v.t. | DERDEN: DC Rainmaker, "Enduro 3 doesn't have speaker/microphone features" |
| Enduro 4 | **nee** | n.v.t. | GEZIEN: handleiding `manuals/webhelp/GUID-25EFCCBC-D0EB-4E1B-AE9F-B4B900891C20/EN-US/Enduro_4_OM_EN-US.pdf`, 0 keer "microphone", 0 keer "voice note" of "voice command" |
| fēnix E | **nee** | n.v.t. | GEZIEN: handleiding voor Azië, 235 pagina's, 0 keer "microphone" |
| Forerunner 70 | **nee** | n.v.t. | GEZIEN: 192 pagina's, 0 keer "microphone" of "speaker" |
| Forerunner 170 en 170 Music | **nee** | n.v.t. | GEZIEN: 212 pagina's, 0 keer "microphone" of "speaker" (één handleiding; dat de Music daaronder valt is een GOK) |
| vívoactive 6 | **nee** | n.v.t. | GEZIEN: 222 pagina's, 0 keer "microphone" of "speaker" |

Ook met ingebouwde notitie maar buiten onze lijst (GEZIEN, zelfde onderwerp in de handleiding): tactix 8, quatix 8, D2 Air X15.

## Telling

- 15 lijnen in de lijst van Garmin (de 30 regels samengenomen per lijn).
- **8 met microfoon en ingebouwde notitie** (fēnix 9, fēnix 8, Venu 4, Venu X1, Forerunner 570 en 970, Approach S72, D2 Mach 2).
- 1 met microfoon, notitie niet kunnen nalezen (MARQ Gen 3, een horloge van duizenden euro's).
- **6 zonder microfoon** (Enduro 3 en 4, fēnix E, Forerunner 70 en 170, vívoactive 6). Daar kan onze app niets opnemen. Waarom Garmin ze toch in de lijst van `Toybox.Audio` zet weet ik niet (GOK: afspelen via een koptelefoon).
- **Met microfoon en zonder ingebouwde notitie: 0.** De vraag hoe populair die horloges zijn vervalt daarmee. Voor het beeld: juist de horloges die het meest verkocht worden met microfoon (Venu 4, Forerunner 570 en 970, fēnix 8) hebben de notitie (GOK over de verkoop, Garmin geeft geen cijfers per model).
- Oudere horloges met microfoon (Venu 3, Venu 2 Plus) staan niet in de lijst van `Toybox.Audio`: daar mag een app de microfoon niet gebruiken, dus ook daar ligt geen markt.

## Mijn fout in deel 1

In deel 1 schreef ik "niemand speelt een memo terug af op het horloge" en maakte dat onze zin. Dat klopte voor de 17 apps in de winkel, maar ik had het horloge zelf niet bekeken. Het stond er als open punt bij, maar de zin was al doorgegeven. Les: bij een concurrentiecheck eerst kijken wat het apparaat zelf al gratis doet, dan pas de winkel.

## Wat kan de ingebouwde notitie niet

1. **De memo komt niet draadloos van het horloge af** (Garmin zegt het zelf). Daar vraagt een gebruiker om op het forum. Dit is het enige echte gat.
2. Er wordt geen tekst van gemaakt.

Beide vragen een ontvanger buiten het horloge. Dat is wat Chui en SayNote AI al gratis doen (deel 1), met 1 en 10 downloads. Advies en kosten staan in `berichten/hoofdchat.md` (17 nov ±15:05 UTC).
