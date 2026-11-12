# Ebb: stand voor inleveren (Gijs, run 58, 12 nov 2026 07:20 UTC)

Voor de hoofdchat, bij het besluit van Thijs van 08:05 (Ebb snel inleveren). Alleen feiten uit de volle run op de bouwtak en uit de code, plus mijn advies. Ik heb niets gebouwd en niets ingediend.

## Wat er nu echt is

- **BEWEZEN:** bouwtak `claude/garmin-2026-11-10b` staat op 9f66378. Toetsrun 43167720320 groen, winkelbestand en plaatjes 43167720322 groen op dertien horloges (1001 beelden, 77 scènes per horloge) op tak `schermen`, map `garmin-adem/plaatjes/namen/`.
- **ZELF GEZIEN** (FR255, fenix 7 en fenix 8 47 mm, uitgesneden en vergroot): start, menu, ademen, inhouden, herstel, Calm, pauze, today, 8 weeks, sea log (drie bladen), eindschermen, sea complete, settings, uitleg, veiligheid. Het is één rustige stijl: zwart met een blauwe zee onderin, dier klein op het water, grote cijfers. Geen tekst over een dier, niets buiten het ronde scherm.
- **De donkere omtrek op MIP** (open punt van run 57): gezien in sea log, eindscherm en sea complete op FR255 en fenix 7. Op zwart valt de rand weg en blijven de dieren goed leesbaar; op blauw water geeft hij een dunne donkere lijn. Goed.
- **GEZIEN in de code:** de nieuwe werelden (krab met zwemband, schildpad, thuiswater, nachtregel) zitten alleen in de testscènes (`Scenes.mc`, scène 51 tot 76, klasse `KrabV2View`). In de app die een koper krijgt zit er geen enkele wereld. `KrabV2View` is een stilstaand beeld; het hangt niet aan de klok van de sessie.
- **Winkelbeelden:** op de bouwtak staan de kaarten v4 (uit echte fenix 8-opnames van run 43001614405, code 330cf56). Mila's v5 en v5.1 tonen de krabwereld. **Die mogen niet de winkel in zolang de wereld niet in de app zit:** dan verkopen we iets wat de koper niet krijgt.
- Het akkoord van Daan staat op nee (11 nov 02:10 UTC, D1 tot D9, voor een oudere bouw). Er is sindsdien veel van gebouwd, maar hij heeft de bouw van nu niet gekeurd. NIET bewezen: of de kaarten v4 nog kloppen met de schermen van nu.

## Drie wegen

| Weg | Wat de koper krijgt | Werk Gijs | Risico |
|---|---|---|---|
| **A. Inleveren zoals de app nu is** | de rustige app hierboven, 24 dieren voor trouw, alle basisfuncties | 1 tot 2 runs: winkelbeelden uit de echte schermen van nu, winkeltekst nalopen, versie 1.0.1 en release | minder bijzonder dan de werelden; Daan moet de echte schermen keuren |
| **B. Eerst krab en schildpad in de echte sessie** | twee dieren met een wereld, 22 zonder | 3 tot 5 runs bouwen (wereld aan de sessieklok, geheugen meten op de FR255) plus keuring | half af: de meeste dieren hebben geen wereld; nieuwe fouten in het hart van de app |
| **C. Alle werelden eerst** | wat het ontwerp belooft | dagen | dit is wat Thijs net stopte |

GOK bij de runs: ik reken één run als ±45 minuten, en een volle test duurt ±35 minuten.

## Advies: weg A

Lever de app in zoals hij nu is, als versie 1.0.1, en breng de werelden daarna één voor één als update (krab eerst, als hij op een echt scherm een 8 haalt). Waarom: alles wat een koper ziet is getest op dertien horloges en is één stijl; de werelden zijn mooi maar staan nog los van de app; en een update na de eerste keuring gaat bij Garmin sneller dan een eerste inzending (GOK). De proefcode van de werelden zit dan wel in het bestand, maar wordt nooit getekend.

Wat ik bij weg A doe, in deze volgorde: (1) winkelbeelden: de kaarten v4 naast de fenix 8-beelden van run 43167720322 leggen en opnieuw maken waar het scherm veranderd is; geen kaart die inhouden verkoopt (Mila verving daarom `1-hold.png`: daar komt het ademscherm); (2) `winkeltekst.md` nalopen op alles wat de app niet doet, en het veld Screenshots bijwerken; (3) versie naar 1.0.1, volle run, en pas na het ja van Daan een release met `[release]`; (4) de stap voor Thijs op zijn lijst bijwerken (uploaden, ±10 minuten). Ik begin hier pas aan als de hoofdchat de weg kiest; (1) en (2) zijn in elke weg nodig en pak ik de volgende run alvast op.

## Wat ik nodig heb

Eén regel van de hoofdchat in `berichten/gijs.md`: weg A, B of C. En bij A: wie keurt (Daan op de echte schermen, of de drie frisse beoordelaars), want zonder `Akkoord: ja` breng ik niets uit.
