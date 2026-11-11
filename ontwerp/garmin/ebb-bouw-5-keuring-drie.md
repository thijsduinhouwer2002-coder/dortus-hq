# Ebb bouw 5: keuring door drie frisse beoordelaars (11 nov, 09:30 NL)

Gekeurd: code `claude/garmin-2026-11-10b` 81ae64c5 (na het opruimen), plaatjesrun 42983660035 (35 scènes, geen crash). Beelden fenix 8 en FR255 los bekeken en nagemeten, steekproef Venu 3S, vivoactive 5, FR165, fenix 7, epix.

| Onderdeel | Bouw 2 | Bouw 3 | Bouw 4 | Bouw 5 |
|---|---|---|---|---|
| Code | 3 | 7 | 7 | 7 |
| Veiligheid en regels | 4 | 6 | 6 | 6 * |
| Bouw visueel | 4 | 6 | 5 | 6 |
| Product | 5 | 6 | 7 | 6 |
| Dieren in de app | 7 (blad) | 6 | 6 | 6 |

\* De keurder gaf 7. De hoofdchat zet het op 6: op de FR255 is de veiligheidstekst in kleine Barlow fout te lezen ("Nol if pregnant", "hearl", "Nol a medical device"). Zelf vergroot nagekeken in k15.

Laagste 6, drempel 8. Productkeurder: app zelf rond 7, nog 10 tot 14 uur tot een 8.

Af: zwart blok weg, alle dierschermen via één tekenfunctie zonder crash, Barlow overal, code opgeruimd (elk bestand hoogstens 300 regels, pixelbewijs 35 van 35 gelijk), sea log v9 (sterkste scherm van de app), silhouet als schaduw, Save uit de pauze toont het eindscherm, winkelzinnen kloppen met de code.

## Besluiten hoofdchat
1. **Leesbaarheid gaat voor de eigen letter.** Tekst kleiner dan wat leesbaar blijft gebruikt de systeemletter, of Barlow in een maat waarin de t heel blijft. Veiligheidstekst moet op elk horloge foutloos te lezen zijn. Harde eis.
2. **Dier tijdens inhouden wordt echt 90 x 70 (454) en 50 x 40 (260).** De cijfers worden daarvoor iets kleiner en zakken ongeveer 25 px. Waarom: het eigen dier is de haak van de app (besluit 22:53 en Thijs over de kwal); nu is het 66 x 42.
3. **Winkelbeelden nu, niet meer "later".** De oude beelden beloven meters en dieren voor langer inhouden: misleidend. Dat ze er nog staan komt door de hoofdchat, die ze achteraan zette.

## Voor Gijs (in deze volgorde)
1. **Leesbare tekst** (besluit 1): veiligheid 13 t/m 15, how it works 11, scène 6, 18, 20 op FR255 en alle MIP-horloges. Kleine tekst op 454 minstens 22 px hoog (nu 15 tot 17 px); veiligheid en how it works een maat groter. Controleer met vergrote uitsnede dat elke t een dwarsstreep heeft.
2. **Winkelbeelden** uit plaatjesrun van deze bouw: poster die in één beeld zegt wat Ebb is (ademrondes, de zee, dieren door trouw), plus inhouden met dier (s2), new friend (s17), sea log (s4), Calm (s7) en sea complete na punt 3. Oude vijf (0-poster-v2, 1-dive, 2-meet, 4-dive-profile, 5-tide) weg. Lijst in winkeltekst.md bijwerken, blok Nagekeken opnieuw tegen de huidige code.
3. **Sea complete** leeg op 416 en 454 (fenix 8, Venu 3S, epix): 120 opbouwbeurten, plaatje verschijnt pas aan het eind. Walvis eerst tonen, elke beurt plakken wat er staat, of bouwen bij het opslaan. Via de gedeelde tekenfunctie (REGELS.md punt 4). Plaatje loslaten bij verlaten van het scherm. Testen met 20 s per scène op AMOLED. Op FR255 het kluwen rustig ordenen (Mila geeft de opstelling) en de fontein onder de kamlijn.
4. **Dier tijdens inhouden** volgens besluit 2 (scène 0 t/m 3, 24).
5. **Uiterlijk:** zeester scène 17 ongeveer 15 px lager; zee met kamlijn ook op 12 t/m 15, 19, 20, 22; scène 18 rustiger (minder vol, grotere tijden of alleen de beste 3 plus "6 rounds"); silhouet volgend dier ongeveer 60 px; keuzestip sea log blad 4 los van de inktvis en raster in het midden; menu-dier 80 px; "new friend" op 260 groter dan de kop.
6. **Pauzemenu in Ebb-stijl** (nu het witte systeemmenu) met scène; scène bonusblad; "24 of 24 + bonus".
7. **Horloges:** Venu 4 strings (welke knop?), Venu X1 erbij (verticaal centreren).
8. **Batterij en geheugen:** niet elke 100 ms hertekenen als er niets verandert (EbbView.mc:183, RustigView). Grootste plaatjesopbouw meten op FR165 en Venu 3S (ook graphics pool).
9. **Pixelvergelijking als workflowstap** (voor en na per scène), zodat iedereen het bewijs kan zien.
10. **Klein:** `bron/__pycache__` uit git en in .gitignore; `EbbDierPlaatje.amoled` dubbel; `tekst()` dubbel in SeaLog en SeaComplete; kopregel DierMaat.mc; palet sea log op AMOLED.

## Voor Mila
1. Sea complete: een rustige opstelling van 24 dieren plus walvis op 260 en 454 (geen kluwen), fontein onder de kamlijn. Geef Gijs posities.
2. Pauzemenu in Ebb-stijl (Resume, Save, Discard) op 454 en 260.
3. Kijk mee naar de poster voor de winkel: één beeld dat zegt wat Ebb is. Lever een ontwerp, Gijs vult het met echte schermen.
