# Ebb bouw 3: keuring door drie frisse beoordelaars (11 nov, 05:30 NL)

Gekeurd: code `claude/garmin-2026-11-10b` 09a38e86, plaatjesrun 42956563037 (22 scènes op 8 horloges, 8 minuten, geen crash). Beelden fenix 8 en FR255 los bekeken en nagemeten.

| Onderdeel | Bouw 2 | Bouw 3 |
|---|---|---|
| Code | 3 | 7 |
| Veiligheid en regels | 4 | 6 |
| Bouw visueel | 4 | 6 |
| Product | 5 | 6 |
| Dieren in de app | 7 (blad) | 6 |

Laagste 6, drempel 8. **Nog niet naar de winkel.** Wel een grote stap: crash weg, echte crash-stap in CI (werd rood in run 42953647184), weekreeks, sessieminimum, Calm-check, settings-pil, herstel, opruimen, FIT en sensor af.

## Besluiten hoofdchat
1. **My pattern blijft**, maar loopt via "Sit or lie down" en komt in de winkeltekst. Waarom: het zit al in de app en het is een echte functie; alleen de veiligheidscheck ontbrak.
2. **Een einde aan het verzamelen:** na de walvis een scherm "sea complete", en na week 7 een reeksteller die blijft groeien ("12 weeks in a row") zonder nieuwe dieren. Waarom: anders beloont de app na 4 maanden niets meer.
3. **Meer horloges** (zie punt 2 hieronder). Waarom: bereik bepaalt de verkoop meer dan wat ook.

## Voor Gijs (in deze volgorde)
1. **Winkelbeelden opnieuw** uit de echte bouw: inhouden met dier, eindscherm "new friend", sea log, Calm 4-7-8, 8 weeks. Oude `0-poster-v2` (183 m, whale op 3:00), `1-dive`, `2-meet`, `4-dive-profile` (new best), `5-tide` weg; lijst in winkeltekst.md aanpassen. Pas na punt 4 tot 8 de definitieve set maken.
2. **Meer horloges:** fenix 8 43/51 mm, fenix 7 Pro/X, epix Pro 42/51, FR 165/570/955/970, vivoactive 6, Venu 3S, Venu X1 (wat de SDK kent). Fenix 7 ook in de plaatjesmatrix.
3. **Veiligheid:** "Start my pattern" via StartCheckView (InstellingenView.mc:147-151). Calm-check toont "Calm 4-7-8" als kop, niet "3 rounds · 30 breaths" (EbbApp.mc:358). Scène voor de Calm-check erbij.
4. **Zwaarste schermen echt testen:** scène sea log blad 3 met alle 25 dieren (`BITS=(1<<25)-1`, `keuze=18`), inhoudscherm met de krab (`GEKOZEN=4`). DierenDataTest bewijst geen watchdog; dat doen alleen deze scènes.
5. **Letter:** Barlow Condensed voor alle tekst op alle schermen (nu alleen de grote cijfers; koppen zijn Roboto). Geheugen meten op FR255 en Venu 2.
6. **Ruimte rond tekst:** titel en tijden minstens 10 px op 454 en 6 px op 260 (scène 16, 18, 21). Titel minstens 18 px binnen de rand (scène 18 valt erbuiten). "4 min · 12 breaths" kleiner. Kop boven het cijfer minstens 12 / 6 px (scène 8, 9). Calm: cijfer zelf centreren, "s" los erachter (scène 7). Settings: pil 10 px hoger, één lettermaat, regels gelijk verdeeld.
7. **Eén zee onderaan** voor alle schermen, met dezelfde kamlijn; op AMOLED echt verloop, ook op de eindschermen (nu drie harde stroken).
8. **Dier tijdens inhouden** 90 x 70 op 454, 50 x 40 op 260, 8 px boven de hartslagregel. Testreeks steeds hetzelfde eigen dier. Scène 17: "new friend" groter dan alles, zeester 15 px lager. Menu-dier 80 px.
9. **Sea log op 260:** 3 px tussen rijen, keuzestip 3 px onder het dier, naam 10 px onder het raster, hint "START: swims with you".
10. **Weekdoel wisselen:** vlag "week gehaald", tellen bij `weekSes >= doel && !gehaald` (Profiel.mc:150), met toets. Oude opslag: `trReeks` en `trBeste` (dagen) één keer wissen met een opslagversie.
11. **Kleine fouten:** Calm onder 60 s toont seconden (RustigView.mc:196-202). 8 weeks kijkt naar sessies, niet naar inhouden (EbbApp.mc:998), en telt van maandag tot zondag. Geen lege sessie in Today bij 0 inhouden (EbbApp.mc:483). "1 more session" wordt "1 more session: new friend", stippen apart.
12. **Einde** volgens besluit 2.
13. **Winkeltekst:** "up to two a day" erbij, My pattern en trillen aan/uit erin, "before every session sit or lie down" moet waar zijn, blok "Nagekeken" opschonen. Drie talen.
14. **Ontbrekende testbeelden:** ademen uit, pauzemenu, today met 3 sessies, sea log blad 2 en 3, lege staat bij eerste start, weekdoel gehaald, alle 24 gevonden, Calm onder 1 minuut. Testgegevens één kloppend verhaal (6d "counts as a session" moet een stip erbij geven).
15. **Dode code:** `getijden`, `zwem`, `CYCLUS_MS`, `IN_BEELD_MS`, Box en 5.5 in `Ebb.patronen()`, opmerkingen over duikprofiel.

## Voor Mila
Dieren in de app op 6, vooral op 260 (MIP):
1. Ogen: één donkere pupil van 2 x 2 px, geen witte plusjes.
2. Kogelvis: silhouet leest als harige ring, maak de vorm duidelijk.
3. Controleer alle 25 op 260 px op de echte FR255-beelden (`garmin-adem/plaatjes/fr255-scene4.png` op tak schermen) en geef Gijs de verbeterde data.
