# Ebb blad v2.1: alle schermen, ronde 2 (Mila, 10 nov run 17 en 18)

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

## Midden (harde regel 20:20) en optisch midden
Optisch midden = zwaartepunt van alles wat geen zwart, water of ring is (tekst, dieren, lijnen). Op 260: binnen 2 px op alle schermen behalve duiken (+4,0, de voortgangsboog groeit met opzet aan één kant) en 8 weeks (+4,0, de gegevens zelf). Op 454 hetzelfde beeld, binnen 3,3 px behalve die twee.

Kader van alles wat getekend is: op alle 26 beelden binnen 1 px van het schermmidden (eis 2 px).

## Voor Gijs (pas na het ja van Thijs)
- Dieren: `dier_delen()` geeft de veelhoeken in eenheden (lengte 2), `dier()` zet ze op hun zwaartepunt; reken dat zwaartepunt één keer uit (zie `dier_beeld()`) en zet de verschuiving vast in de code.
- Dithering: twee stroken van 2 px boven elke bandgrens met een vast patroon; op het horloge het makkelijkst als kleine bitmap van 2 x 2 die je langs de golf herhaalt, of als vaste PNG per band (GOK: geheugen klein, de banden bewegen niet tijdens de duik).
- Letter: Barlow Condensed Medium, kleinste maat 17 px op 260 en in verhouding op grotere schermen.
- Geen `setClip` meer nodig voor het getal: het staat boven het water.
