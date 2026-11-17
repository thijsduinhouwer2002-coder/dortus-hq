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
