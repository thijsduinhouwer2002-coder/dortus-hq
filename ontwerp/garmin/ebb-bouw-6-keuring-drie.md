# Ebb bouw 6: keuring door drie frisse beoordelaars (11 nov, 10:45 NL)

Gekeurd: code `claude/garmin-2026-11-10b` 38f98eab, plaatjesrun 42991019029 (36 scènes, geen crash), winkelbeelden v3 (poster en vijf kaarten).

| Onderdeel | B2 | B3 | B4 | B5 | B6 |
|---|---|---|---|---|---|
| Code | 3 | 7 | 7 | 7 | 7 |
| Veiligheid en regels | 4 | 6 | 6 | 6 | 7 |
| Bouw visueel | 4 | 6 | 5 | 6 | 7 |
| Product | 5 | 6 | 7 | 6 | 7 |
| Dieren in de app | 7 | 6 | 6 | 6 | 7 |
| Winkelbeelden | | | | | 7 |

Laagste 7, drempel 8. Productkeurder: nog 7 tot 9 uur.

Af: veiligheidstekst op MIP foutloos (systeemletter, letter voor letter gelezen op FR255, fenix 7, 7X Pro), kleine tekst 22 px op 454, nieuwe eerlijke winkelbeelden (aantallen kloppen met TrouwDieren.mc), pauzemenu in Ebb-stijl (sterkste scherm), sea complete als klassenfoto op 260, Discard bewaart niets, Save toont eindscherm, .pyc weg.

## Besluit hoofdchat
**E2e-eis 11 (cijfers tijdens inhouden 30 procent van het scherm) wordt 25 procent.** Waarom: besluit 09:30 punt 2 maakte de cijfers kleiner zodat het eigen dier 90 x 70 kan worden; het dier gaat voor. De e2e-run 42991019138 is daardoor rood en moet met de nieuwe eis weer groen.

## Voor Gijs (in deze volgorde)
1. **E2e groen** met eis 11 op 25 procent (besluit hierboven), en noem het besluit in de workflow.
2. **Na sea complete weer het gewone eindscherm** met rondetijden (EindScherm.mc 25-28). Feestscherm alleen de eerste keer. De winkeltekst belooft tijden na elke sessie.
3. **Sea complete af op AMOLED:** fenix 8 toont 17 van 24, epix 15, Venu 3S 6 met een witte halve krab. Bouw het plaatje bij het opslaan of toon het pas als het af is; alleen afgemaakte dieren plakken (SeaComplete.mc:108); ook op 390 px meer lagen per beurt. Plaatjesrun 20 s per scène op AMOLED. Geheugen meten met het plaatje erbij (graphics pool) op FR165 en Venu 3S.
4. **Pauzemenu:** Calm ook via PauzeView (RustigView.mc:117-123); onTap die de aangetikte regel kiest (Venu, vivoactive); Discard terug naar het menu in plaats van de app sluiten.
5. **Uiterlijk:** keuzestip sea log naast het dier of een ring om het gekozen dier (blad 2 en 4), raster in het midden; zeester (s17) en zeekomkommer (k33) onder de kamlijn; kamlijn op 5, 6, 11, 13, 14, 15, 19, 20; scène 28 "first friend after 1 session" los van de kamlijn; scène 18 rustiger; lange namen op twee regels in plaats van kleiner (k33); dier tijdens inhouden 10 procent groter.
6. **Winkelbeelden v4:** kaarten inzoomen (scherm minstens 60 procent breed, geen band, minder zwart); geen rood in koppen, wel schuim of geel; Calm-kaart vervangen door het pauzemenu of een sea log met meer gevonden dieren; sea log-kaart met een kloppende stand. Titel: "Ebb: Breathing, Breath Hold Rounds & 4-7-8". "no extra account" in plaats van "no account". Bonusdier zichtbaar in de sea log ("24 of 24 + bonus").
7. **Horloges:** Venu 4 knoptekst nagaan en strings, plaatje van de Venu 4; Venu X1 in het manifest.
8. **Batterij:** niet elke 100 ms hertekenen op stilstaande schermen (EbbView.mc:184, RustigView.mc:58); bij inhouden eens per seconde.
9. **Pixelvergelijking als workflowstap.** Dubbele tekst() en px() naar Teken.mc. REGELS.md kaart aanvullen (Pauze.mc, SeaComplete.mc). Nagekeken bijwerken.

## Voor Mila
1. Winkelkaarten v4: ontwerp de ingezoomde kaart (scherm groot, kop in schuim of geel) en kies samen met Gijs welke vijf schermen het sterkst verkopen.
2. Keuzemarkering in de sea log: ring of glans om het gekozen dier op 454 en 260.
