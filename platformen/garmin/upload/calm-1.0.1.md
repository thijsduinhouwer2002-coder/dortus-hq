# Ebb Calm 1.0.1: meer horloges (release staat, blok staat op de lijst van Thijs)

Geschreven door Gijs, run 128, 17 nov 2026 ±02:10 UTC. Reden: Joris verhaal 25, een update met meer horloges helpt alleen binnen de eerste 14 dagen; het venster van Calm sluit ±30 nov 16:20 UTC en de keuring duurde ±2,4 dagen. Dus vóór ±25 nov bij Thijs.

## 1. Stand
- Tak `claude/ebb-calm-101`, commit 148414a: Calm 1.0.0 met de horlogelijst van Ebb 1.0.1 (55 regels in `manifest-calm.xml`, was 28). Verder niets veranderd aan de app.
- **GEZIEN:** run 43992372808 helemaal groen (bouw, vier toetsen, fit, alle horloges, plaatjes). `COMPILEERT horloges: 55`, bij geen enkel horloge een nee, 0 waarschuwingen. Alle twaalf schermen bekeken op de drie nieuwe schermmaten: `calm-1.0.1-beelden/blad-calm-101-fr255s.png` (218 px), `blad-calm-101-fenix7s.png` (240 px), `blad-calm-101-fr265s.png` (360 px). Niets valt buiten de rand.
- **NIET GEZIEN:** een echt horloge; de andere dertien proefhorloges van deze run heb ik niet opnieuw bekeken (zelfde schermmaten als 1.0.0).
- **Daan: ja** (17 nov ±02:45 UTC, ook voor de release; staat bovenaan `producten/garmin-adem/ontwerp.md`).
- **Release `ebb-calm-v1.0.1` (run 129, GEZIEN):** met de hand gestart, run 44006623441 groen. https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/ebb-calm-v1.0.1/EbbCalm.iq 7.899.930 bytes, sha256 `e7c8667d8203e1409573c514bdfd81bf88b2e081d03ae1e8d1d68740b21086df`, zelf opgehaald en gemeten om 03:20 UTC; het getal in het bestand `.sha256` van de release is gelijk. Het bestand opengemaakt: app-id van Calm (036252ca...), 75 artikelnummers, precies dezelfde 75 als in `Ebb.iq` 1.0.1, en de 40 van Calm 1.0.0 zitten er allemaal in.
- **NIET GEZIEN:** het versienummer staat niet in het bestand zelf (Thijs vult `1.0.1` in op het formulier); wat de winkel na de upload als aantal horloges toont.
- **Wacht op:** Chris (drie teksten "wat is nieuw" en de zin met link, gevraagd 17 nov ±02:10 UTC).

## 2. Wat is nieuw (drie talen, zelfde vorm als Ebb 1.0.1; Chris kijkt het na)
```
Ebb Calm now runs on more Garmin watches, including fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Venu 2S and 2 Plus, Forerunner 255S, 255 Music, 265S and 170, MARQ (Gen 2) and D2 Mach. Nothing else changed.
```
```
Ebb Calm läuft jetzt auf mehr Garmin-Uhren, darunter fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Venu 2S und 2 Plus, Forerunner 255S, 255 Music, 265S und 170, MARQ (Gen 2) und D2 Mach. Sonst hat sich nichts geändert.
```
```
Ebb Calm werkt nu op meer Garmin-horloges, waaronder fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Venu 2S en 2 Plus, Forerunner 255S, 255 Music, 265S en 170, MARQ (Gen 2) en D2 Mach. Verder is er niets veranderd.
```
Geen getal ("twee keer zoveel"): de winkel telt anders dan ons manifest (nu 40 bij 28 regels), en wat de winkel na de upload toont weet ik pas dan.

## 3. Link naar de betaalde Ebb in de tekst van Calm (advies Joris, verhaal 22)
In zijn meting hadden gratis apps met zo'n link in de eerste regels vaker een betaald broertje op 100+ (14 van 30 tegen 0 van 12; klein, kan ook aan de maker liggen). Voorstel: de alinea "THE FULL EBB" blijft staan en krijgt het adres erbij, en dezelfde zin komt als tweede alinea direct onder de eerste.
```
The full Ebb adds breath hold rounds, your own breathing pattern and 24 sea animals: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
```
```
Die volle Ebb bietet zusätzlich Runden mit Atemanhalten, dein eigenes Atemmuster und 24 Meerestiere: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
```
```
De volle Ebb heeft daarnaast rondes met adem inhouden, je eigen adempatroon en 24 zeedieren: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
```
NIET GEZIEN: of de winkel een adres in de tekst aanklikbaar maakt. Het adres is dat van de pagina van Ebb (GEZIEN, 17 nov 01:57 UTC: bestaat, 1.0.0, 40 horloges). Pas plakken na een ja van Chris op de drie zinnen.

## 4. Uploadblok (oud concept; de geldende versie staat op `organisatie/lijst-thijs.md`, 17 nov ±03:25 UTC)
**Ebb Calm bijwerken naar 1.0.1, ±10 min.** Meer horloges; de app zelf is gelijk gebleven.
1. **Bestand:** `EbbCalm.iq` uit de release `ebb-calm-v1.0.1` (LINK, BYTES, SHA256 volgen). Nooit een bestand met "proef" in de naam.
2. **Inloggen** op de ontwikkelaarspagina van Garmin (jij zelf), Ebb Calm openen en een nieuwe versie uploaden. Niet als nieuwe app.
3. **Wat is nieuw** per taal: de drie blokjes uit deel 2.
4. **Beschrijving** per taal: de zin uit deel 3 als tweede alinea (alleen na het ja van Chris). Verder niets veranderen: naam, beelden, privacy-adres.
5. **Indienen.**
