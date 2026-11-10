# Ebb blad v2.3: alle schermen (Mila, 10 nov run 17 tot 19)

**Nieuwste blad: `ontwerp/garmin/ebb-blad-v2.3.png`** (per scherm links 454 px AMOLED, rechts 260 px MIP, ware grootte; icoon ook op 70 en 40 px). Losse beelden en meting in `ontwerp/garmin/blad23/` (`meting-v23.txt`), bron `ontwerp/garmin/bron/ebb_blad_v23.py`. Vervangt v2.2 (`ebb-blad-v2.png`, `blad2/`, die blijven staan ter vergelijking). Gaat eerst naar Thijs via de hoofdchat; Gijs bouwt pas na zijn ja.

## Vierde frisse keuring (v2.2, 6 van 10, elf moet-punten). Wat ik deed in v2.3 (GEZIEN met Read, gemeten)
**Grootste besluit: twee gezichten van één app.** De keurder had gelijk: op 454 zag het eruit als een opgeblazen MIP-scherm. Een AMOLED-horloge kan echte kleuren en zachte randen; het kleine MIP-horloge kan dat niet. Dus:
- **454 (AMOLED):** de zee is één doorlopend verloop door dezelfde vier tinten (helderder gekozen), zachte golflijnen tussen de lagen, een gloed onder het schuim, heel zachte lichtstralen onder water, de zon met een warme gloed, zachte letters en randen. De grafieken (today, 8 weeks) zijn ook een verloop van licht naar diep. 800 tot 15.000 kleuren per beeld.
- **260 (MIP):** strak en eerlijk: harde vlakken, alleen MIP-kleuren (0 pixels erbuiten op alle 13 schermen), **geen dithering meer** langs de golfranden.

Per moet-punt:
1. 454 met verloop en zachte randen, 260 strak zonder dithering (zie boven).
2. **Voortgangsboog:** donker spoor rondom, de boog in oranje 0xFF5500 (een eigen kleur, nergens anders gebruikt sinds de schildpad groen is), witte stip met zwarte rand aan het eind, met een zwarte rand los van de golf. Bij de walvis (alles gevonden) een volle oranje ring.
3. **3b:** "whale found" en "4 of 4" op het moment van vinden, in twee regels (op één regel raakte het de ring). Daarna toont het duikscherm een nieuw doel: "best 3:12" (je record plus 9 s); dat scherm teken ik niet apart, het is scherm 3 met een andere ondertekst.
4. **8 weeks:** de lijn eindigt rechts in de gouden stip van vandaag; onder de grafiek "best 2:08 today". Today eindigt met dezelfde 2:08 in goud als derde ronde. Eén verhaal.
5. **Eén betekenis per groot getal:** op 2 is het getal je ademteller: titel "in" (wisselt met "out"), onder "breath 23 of 30" en "round 2". Op 4 en 5 zijn het seconden: "15 s" en "7 s", de s klein en grijs, samen gecentreerd.
6. **3d:** "turtle found" groot, "held 2:03 · 3 of 4" eronder.
7. **260:** kleinste letter nu 20 px = 14 px kapitaalhoogte (gemeten). Pijltjes bij 30 nu 10 px hoog (waren 7).
8. **Sea log:** de verborgen walvis is precies dezelfde walvis als silhouet, met cyaan rand en een "?" op zijn lijf, en "next 3:00". **Schildpad groen** (schild 0x00AA55, huid 0xAAFF55, donkere schildrand, geen stippen, klein staartje): nu nooit meer te verwarren met de vis. **Kwal** opnieuw in de ronde stijl: ronde kap met golvende onderrand, vier zachte armen die taps toelopen met een rond eind, glans linksboven.
9. **Menu:** Box eruit (eerst een eigen scherm verdienen). Nu "Calm · 4-7-8", "Rounds 3 x 30" (gekozen), "Sea log". Sea log in het menu: zo kom je bij je dieren zonder eerst te duiken.
10. **Veiligheid:** voluit "Never hold your / breath in water / or while driving.", het hele blok lager (teken op 27% D, OK op 76,5% D).
11. **START-boog: nergens.** Hij stond er maar op drie schermen en suggereerde dat START elders niets doet. De gekozen pil en de OK-knop zeggen al wat START doet.

Kan-punten: (2) walvissen 1,2% D naar links op menu, 3b, sea log en icoon (zwaartepunt bleef optisch rechts); (4) icoon met vier grotere bouten en water tot boven in de poort, leest nu op 70 en 40 px (GEZIEN); (5) AMOLED: boven het water blijft het zwart, alleen het water licht op. (1) hoofdletterregel: titels klein (today, sea log, settings), items met hoofdletter (Rounds, Sea log, Buzz on): stond al zo. (3) "round 1, 2, 3" bij today: niet gedaan, de drie tijden zeggen het al en op 260 is er geen ruimte voor een vierde regel zonder te kleine letters.

**Gemeten (`blad23/meting-v23.txt`):** kader van alles wat getekend is binnen 1,5 px van het midden op alle 26 beelden (sea log 1,5 px door de walvis die bewust naar links staat). Optisch midden op 260 binnen 2 px, behalve today (+5,7 px) en 8 weeks (+4,2 px): het record staat nu rechts, omdat het vandaag is. Dat is de data, geen scheefstand.

**Beeldtaal, wat er verandert ten opzichte van de 10 regels hieronder:** regel 4 wordt "één schaal van vier blauwtinten: op AMOLED als zacht verloop, op MIP als harde vlakken zonder dithering"; regel 5 krijgt "oranje = voortgang"; regel 6: kleinste letter 20 px op 260 (14 px kapitaalhoogte), op AMOLED zachte letters; regel 8: dieren elk in hun eigen tint (walvis, vis en kwal warm, schildpad groen), verder dezelfde stijl.

**Voor Gijs (pas na het ja van Thijs), GOK om na te kijken:** verloop op AMOLED het makkelijkst als vaste PNG per scherm-achtergrond (de zee per diepte vooraf getekend, 3 tot 4 standen), of met `Graphics.createColor` en `setAntiAlias(true)` (API 3.2+); lichtstralen als bitmap met alfa. Geheugen nakijken op de venu2 en vivoactive5. Op MIP-horloges (260, fenix 7, Forerunner 255) de harde versie.

---

## Eerder: Ebb blad v2.2: alle schermen, ronde 2 (Mila, 10 nov run 17 en 18)

Blad: **`ontwerp/garmin/ebb-blad-v2.png`** (per scherm links 454 px, rechts 260 px, ware grootte). Losse beelden en meting in `ontwerp/garmin/blad2/` (`meting-v2.txt`), bron `ontwerp/garmin/bron/ebb_blad_v2.py`. Vervangt blad v1. Gaat eerst naar Thijs via de hoofdchat; Gijs bouwt pas na zijn ja.

Opdracht: de frisse keuring van blad v1 (`ebb-blad-v1-frisse-keuring.md`, 5 van 10, tien moet-punten), door de hoofdchat overgenomen. ## Beeldtaal van Ebb in 10 regels (bijgewerkt; regel 3, 4, 5, 7 en 8 zijn anders dan in v1)
1. **Gevoel: één duik, van kust tot diep en terug.** Menu is de kust, ademen is golven, inhouden is zakken, boven komen is zon, het resultaat is je duikprofiel en een nieuw dier.
2. **Rust boven alles.** Eén groot ding per scherm, hooguit twee kleine regels. Wat beweegt, beweegt traag.
3. **Vorm: een dunne ring** (3 px op 454, 2 px op 260) langs de rand van elk scherm. De patrijspoort met bouten is alleen nog het icoon: het venster waardoor je de app binnenkijkt. *(was: ring met acht bouten op elk scherm; te zwaar en nep)*
4. **Water: één schaal van vier blauwtinten** W0 0x00AAFF, W1 0x0055AA, W2 0x0000AA, W3 0x000055, hoe dieper hoe donkerder. Op MIP (260) twee rijen dithering tussen de banden, op AMOLED (454) vlakke banden (dithering flikkert daar als het beweegt). Schuim alleen op de bovenste golf.
5. **Kleur: koud met drie warme stemmen, elk met één betekenis.** Koraal = wat leeft (dieren) en gevaar. Goud 0xFFAA00 = je record. Geel = de zon. *(was: koraal ook voor record)*
6. **Letter: Barlow Condensed Medium**, harde randen zoals het horloge tekent, kleinste maat 17 px op 260 (12 px kapitaalhoogte).
7. **Getallen staan altijd vrij.** Het water stijgt en zakt alleen onder het getal; tekst staat nooit op een golfrand en wordt nooit gesneden. *(was: het getal zakt in het water; las slecht, de 3 werd een 5)*
8. **Dieren: één stijl.** Gevulde vlakken zonder lijnen, eigen tint binnen koraal, buik een tint lichter, vin een tint donkerder, hetzelfde oog, allemaal naar links, geplaatst op hun zwaartepunt. Een houding per scherm (dalen, stijgen, dobberen). Een dier is een beloning en krijgt zijn eigen scherm.
9. **Grafieken zijn zee, geen statistiek**, maar wel eerlijk: diepte evenredig met tijd, labels erbij, kader binnen 15 tot 85% van D.
10. **Overgangen voelen als water.** Het peil stijgt of zakt tussen schermen; bij een record één korte trilling en goud, geen vuurwerk.

## Wat er per moet-punt veranderde (GEZIEN met Read, gemeten in `meting-v2.txt`)
1. **Golf uit het cijfer.** Op ademen, boven komen en rustig ademen staat het getal helemaal boven het water, altijd wit. Het peil zakt en stijgt alleen onder het getal (hoogste peil 60% D, onderkant van het getal 55% D).
2. **260 px: kleinste tekst 17 px = 12 px kapitaalhoogte** (gemeten met de letter zelf). De functie `tekst()` laat niets kleiner toe. Wat niet paste is eruit: "breaths" in het menu, "My pattern" in settings, "Sit or lie down" op het veiligheidsscherm (dat staat in de winkeltekst en bij de eerste start).
3. **Grijs is #AAAAAA**, contrast 9,0:1 op zwart (was 2,8:1). Wit op W1 7,3:1, schuim op W1 5,9:1.
4. **Ring 3 px op 454, 2 px op 260, zonder bouten.** Bouten alleen nog in het icoon.
5. **Eén waterschaal:** W0 0x00AAFF (oppervlak), W1 0x0055AA, W2 0x0000AA, W3 0x000055. Dezelfde op menu, ademen, duiken, boven, rustig en de grafieken. Tussen twee banden twee rijen dithering (25% en 50%), zodat het zacht overloopt met alleen MIP-kleuren.
6. **Dieren in één stijl:** gevulde vlakken zonder lijnen, lichaam in een eigen tint, buik een tint lichter, vin of poot een tint donkerder, bij alle vier hetzelfde oog (wit rondje met nachtblauwe pupil, glansje als het dier groot is). Allemaal naar links. Tinten binnen koraal: walvis 0xFF5555, vis 0xFFAA55, kwal 0xFF55AA, schildpad 0xFF5500. Geen waterstraal onder water; het spuitje zit alleen in het menu, waar de walvis aan de oppervlakte ligt.
7. **Optisch midden:** elk dier wordt geplaatst met zijn zwaartepunt (alle getekende pixels) op het midden, niet met zijn kader. Dus ook het icoon en het menu.
8. **Sea log:** drie kolommen op precies gelijke afstand (21,5% D), drie dieren even zwaar (oppervlak 434, 445 en 433 px op 260, binnen 3%). De walvis eronder groter, als het donkere silhouet dat je nog moet halen.
9. **8 weeks:** één lijn (je beste tijd per dag, met gaten waar je niet ademde) op een doorlopend getij-vlak, één koraal stip op je beste dag met het label "best 2:08" eronder. De stip ligt 55 px van de rand op 260 (eis 15).
10. **Today:** drie herkenbare duiken: een U met vlakke bodem, de diepte is je inhoudtijd, de tijd onder elke duik; het record in koraal met "new best".

Ook de kan-punten: één titelkleur (schuim) voor alle fasewoorden en titels, geel alleen voor de zon; dithering; veiligheidsscherm rustig (teken, twee regels, OK, geen golf); belletjes in verschillende maten en niet gespiegeld. Kan-punt 3 deels: de dieren hebben een houding (walvis daalt 9 graden met de kop omlaag, schildpad zweeft 6 graden omhoog, in het menu ligt de walvis plat aan de oppervlakte met zijn spuitje); de punten draaien, niet het beeld, dus de randen blijven strak.

## Tweede frisse keuring (losse Claude zonder voorkennis, op v2): 7 van 10. Wat ik deed (v2.1)
1. **Blad liet anti-aliasing zien (297 tot 702 kleuren per beeld).** Nu harde randen: letters in 1-bit, alles in MIP-kleuren. Gemeten: 0 pixels buiten MIP op alle 26 beelden (`meting-v2.txt`). De kleinste letters (17 px) blijven 12 px hoog.
2. **Beloningsscherm ontbrak.** Nieuw scherm 3d "new friend": het nieuwe dier groot in het midden, "turtle 2:03", "3 of 4 met". Dit is het moment waarvoor je morgen terugkomt.
3. **Rood had twee betekenissen.** Record nu goud 0xFFAA00 (today, 8 weeks), koraal alleen nog voor dieren en gevaar.
4. **Duikscherm zonder doel.** Dunne voortgangsboog langs de rand (van boven met de klok mee, naar het volgende dier) en "next 2:00" onderin; bij de walvis is de boog rond en staat er "all met".
5. **Settings te hoog.** Lijst loopt nu door tot "My pattern" en staat in het midden (optisch -1,2 px op 260).
6. **Bediening.** Pijltjes omhoog en omlaag naast de waarde (knoppen, geen vegen), en de bekende START-boog rechtsboven op menu, settings en veiligheid. Die boog telt niet mee in de midden-meting: hij hoort bij de knop.
7. **Menu te zwaar onderin.** Walvis kleiner (0,11 D) en lager, meer lucht tussen "Box" en het spuitje.
8. **8 weeks.** Vlak in W1 (2,9:1 op zwart, was 1,6:1), labels "8 wk" en "now" onder de as, "44 days breathed", piek en label in goud.
Kan-punten: dithering alleen op MIP (gedaan), sea log-silhouet met cyaan rand (gedaan). Niet gedaan: schermen 2, 4 en 5 meer laten verschillen (de zon op 4 doet dat al; 5 krijgt bij de bouw een trager peil).

## Derde frisse keuring (weer een losse Claude, op v2.1): 7 van 10. Wat ik deed (v2.2)
1. **Diepte zag je niet.** De donkere banden stijgen nu met de diepte: op 94 m is de onderste band smal, op 183 m is bijna alles nachtblauw. De meters staan groter (22 px op 260, was 17).
2. **Voortgangsboog verdween in de golf.** Boog met een zwarte rand van 1 px; bij "all found" geen ring meer (leek op de knophint).
3. **"met" was dubbelzinnig.** Overal "found" ("3 of 4 found", "all found"); fasewoord op ademen is "breathe in", net als op boven komen.
4. **8 weeks.** De labels "8 wk" en "now" waren in kleine letters maar 9 px hoog: weg. Onder de grafiek staat nu wat hij toont: "best 2:08" en "longest hold per day".
5. **Dubbele spaties** weg ("turtle 2:03", "Rounds 3", "Buzz on").
Niet gedaan: water alleen onder de horizon op AMOLED (kan-punt, stroom); eerst Thijs' oordeel over het beeld.

## Midden (harde regel 20:20) en optisch midden
Optisch midden = zwaartepunt van alles wat geen zwart, water of ring is (tekst, dieren, lijnen). Op 260: binnen 2 px op alle schermen behalve duiken (+4,0, de voortgangsboog groeit met opzet aan één kant) en 8 weeks (+4,0, de gegevens zelf). Op 454 hetzelfde beeld, binnen 3,3 px behalve die twee.

Kader van alles wat getekend is: op alle 26 beelden binnen 1 px van het schermmidden (eis 2 px).

## Voor Gijs (pas na het ja van Thijs)
- Dieren: `dier_delen()` geeft de veelhoeken in eenheden (lengte 2), `dier()` zet ze op hun zwaartepunt; reken dat zwaartepunt één keer uit (zie `dier_beeld()`) en zet de verschuiving vast in de code.
- Dithering: twee stroken van 2 px boven elke bandgrens met een vast patroon; op het horloge het makkelijkst als kleine bitmap van 2 x 2 die je langs de golf herhaalt, of als vaste PNG per band (GOK: geheugen klein, de banden bewegen niet tijdens de duik).
- Letter: Barlow Condensed Medium, kleinste maat 17 px op 260 en in verhouding op grotere schermen.
- Geen `setClip` meer nodig voor het getal: het staat boven het water.
