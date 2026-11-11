# Ebb bouw 4: keuring door drie frisse beoordelaars (11 nov, 07:10 NL)

Gekeurd: code `claude/garmin-2026-11-10b` 15ed6f30, plaatjesrun 42967655209 (31 scènes op 12 horloges, "Geen crash" groen). Beelden fenix 8 en FR255 los bekeken en nagemeten, steekproef Venu 3S, vivoactive 5, FR165, fenix 7.

| Onderdeel | Bouw 2 | Bouw 3 | Bouw 4 |
|---|---|---|---|
| Code | 3 | 7 | 7 |
| Veiligheid en regels | 4 | 6 | 6 |
| Bouw visueel | 4 | 6 | 5 |
| Product | 5 | 6 | 7 |
| Dieren in de app | 7 (blad) | 6 | 6 |

Laagste 5, drempel 8. **Nog niet naar de winkel.** Productkeurder schat 18 tot 25 uur werk tot een 8.

Af sinds bouw 3: Calm en My pattern via de check, zware scènes getest, weekdoel met vlag, opslagversie, sea complete, 28 horloges, ruimte rond tekst, Calm-cijfer in het midden, testbeelden voor ademen uit, Calm onder 1 min, sea log blad 2 en 3.

Visueel ging omlaag door een nieuwe fout: de crashfix met de krab (a404eab) tekent het dier als plaatje met een **zwart blok** erachter. Hoofdchat heeft dit zelf in scène 0 en 24 vergroot bekeken: klopt.

## Voor Gijs (in deze volgorde)
1. **Zwart blok achter het dier** (scène 0 t/m 3 en 24, alle AMOLED): het plaatje is niet doorzichtig, 88 x 56 px, vinnen recht afgesneden, op Venu 3S en vivoactive 5 over "· round 1". Doorzichtig maken (bijvoorbeeld palet met doorzichtige kleur, of het plaatje op de achtergrondkleur van die zeestand tekenen) en nameten.
2. **Watchdog op de andere dierschermen:** menu (Start.mc:86), eindscherm new friend en sea complete (EbbApp.mc:992, 1003), silhouet volgende dier (EbbApp.mc:996, 6 keer tekenen), Calm-einde (RustigView.mc:214, 220). Overal EbbDierPlaatje, ook voor het silhouet. Scènes erbij: menu met krab, 6c met krab als silhouet, 6b met zeekomkommer, Calm-einde met krab.
3. **Winkelbeelden opnieuw** uit de echte bouw plus een poster die in één beeld zegt wat Ebb is. Oude vijf weg, lijst in winkeltekst.md aanpassen. Na punt 1, 4 en 5.
4. **Barlow Condensed voor alle tekst** (koppen, tijden, knoppen, sea log, instellingen). Staat nu twee keuringen open; dit maakt het verschil tussen standaard en eigen. Geheugen meten op FR255 en Venu 2 (de CI-stap vond het patroon niet).
5. **Dieren los van tekst:** zeester scène 17 ongeveer 20 px lager (minstens 10 px onder de tijden, ook FR255 en Venu 3S), "new friend" groter dan de kop. Krab scène 24 op 260 los van cijfers en hartslagregel. Walvis scène 25 los van de tijden.
6. **Sea log:** keuzestip onder het juiste dier (blad 2 en 3), rij met één dier in het midden, "24 of 24" uitleggen of tot 25 tellen.
7. **Rest uiterlijk:** pil instellingen 12 px hoger of letter kleiner; kop boven het cijfer 12 px (scène 9, 30); veiligheidsschermen dezelfde zee met kamlijn; silhouet volgend dier beter zichtbaar.
8. **Winkeltekst (drie talen):** "the sea at the bottom rises and falls" in plaats van "the screen fills"; trillen "from 3:00 on, every 30 seconds"; "shows" in plaats van "says 'time to breathe'"; Duits "Halte den Atem nur an"; Nagekeken bijwerken.
9. **Pauze en Save** toont het eindscherm (nu meteen System.exit, EbbApp.mc:1281), zodat je een verdiend dier ook ziet.
10. **Horloges:** Venu X1 erbij (besluit 05:30 blijft). Venu 4 heeft geen strings-map: controleren of er een START-knop is. Overweeg FR255S/M, FR265S, fenix 7S.
11. **Testverhaal kloppend** (stippen passen bij weken en "counts as a session"), scène pauzemenu en My pattern-check. Menu bij eerste start met een belofte, bijvoorbeeld "first friend after 1 session". "Ebb makes no sound" als tekst, niet als knop.
12. **Klein:** `koorde` ongebruikt (InstellingenView.mc:125), onbereikbare return (Start.mc:191), opmerking duikprofiel (EbbApp.mc:890), eindscherm niet elke 100 ms opnieuw tekenen.

## Voor Mila
1. Sea log op 260: dieren zijn ongeveer 15 px en nauwelijks te herkennen. Ontwerp een blad met grotere dieren (bijvoorbeeld 2 rijen per blad, meer bladen) en geef Gijs de maten.
2. Silhouetten van orka, haai en zwaardvis zijn op 260 rafelig.
3. "Sea complete" verdient een eigen viering (geen gewoon eindscherm met kleine walvis en sessiestippen). Maak een ontwerp op 454 en 260.
4. Silhouet van het volgende dier: donkerblauw op donkerblauw is bijna onzichtbaar. Kies een kleur die werkt op AMOLED en MIP.
