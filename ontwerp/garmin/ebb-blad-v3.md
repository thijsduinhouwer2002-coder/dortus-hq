# Ebb blad v3: alle schermen (Mila, 10 nov run 19 en 20)

**Blad: `ontwerp/garmin/ebb-blad-v3.png`.** Per scherm staat links de 454 px-versie (AMOLED) en rechts de 260 px-versie (MIP), allebei op ware grootte. Het icoon staat erbij op 560, 70 en 40 px. De losse beelden en de meting staan in `ontwerp/garmin/blad3/` (`meting-v3.txt`), de bron in `ontwerp/garmin/bron/ebb_blad_v3.py`. Dit blad vervangt v2.2 (`ebb-blad-v2.png`). In run 19 heette het nog v2.3. Het gaat eerst naar Thijs via de hoofdchat; Gijs bouwt pas na zijn ja.

Opdracht: `ebb-blad-v2-frisse-keuring.md` (v2.2 kreeg een 6 van 10, met elf moet-punten), door de hoofdchat doorgegeven in de nachtronde van 22:17.

## Het grote besluit: twee gezichten van één app
- **454 (AMOLED, onder andere fenix 8, epix Pro, Venu, FR265/965):** een echte zee. Eén doorlopend verloop door de vier blauwtinten, zachte golflijnen tussen de lagen, een gloed onder het schuim, heel zachte lichtstralen onder water, een warme gloed om de zon, en zachte letters en randen. Per beeld 1.300 tot 15.600 kleuren.
- **260 (MIP, onder andere fenix 7, FR255):** strak en eerlijk. Harde vlakken, alleen MIP-kleuren (gemeten: 0 pixels erbuiten op alle 13 schermen) en geen dithering meer.
De vorm, de indeling en de dieren zijn op beide maten hetzelfde. Alleen de afwerking hoort bij het scherm.

## Per moet-punt
1. **454 niet in het MIP-palet, MIP strak:** gedaan zoals hierboven beschreven. Hoe Gijs elk effect bouwt staat in het lijstje "Bouwbaar" hieronder.
2. **Voortgangsboog:** rondom een donker spoor, daarop een oranje boog (0xFF5500, verder nergens gebruikt) en aan het eind een witte stip met een zwarte rand. De ring loopt tot 3:00, met een wit streepje bij elk dier (1:00, 1:30, 2:00 en 3:00 bovenaan), dus hij begint niet bij elk dier opnieuw. Een zwarte rand houdt hem los van de golfkam. Op 3b staat de ring helemaal vol.
3. **3b:** op het moment van vinden staat er "whale found" in wit met "4 of 4" eronder. Het staat op twee regels, want op één regel raakte de tekst de ring (GEZIEN). Daarna toont het duikscherm een nieuw doel: "best 3:12". Dat is scherm 3 met een andere ondertekst, daarom staat het niet apart op het blad.
4. **8 weeks gelijk aan today:** today eindigt met ronde 3 op 2:08 in goud met "new best". De lijn van 8 weeks eindigt rechts in de gouden stip van vandaag, met "best 2:08 today" en als schaal "up from 1:05".
5. **Eén betekenis per groot getal:** op 2 is het je ademteller. De titel "in" wisselt met "out", eronder staan "breath 23 of 30" en "round 2". Op 4 en 5 zijn het seconden: "15 s" en "7 s", met de s klein en grijs, en getal plus s samen gecentreerd.
6. **3d:** "turtle found" groot, met "held 2:03 · 3 of 4" eronder.
7. **260:** de kleinste letter is nu 20 px, dat is 14 px kapitaalhoogte (gemeten met de letter zelf). De pijltjes bij 30 zijn 10 px hoog (waren 7).
8. **Dieren in één stijl:** de schildpad is groen (schild 0x00AA55, huid 0xAAFF55, donkere schildrand, geen stippen). De kwal is rond: een ronde kap met een golvende onderrand, vier zachte armen die taps toelopen en rond eindigen, en een glans. De verborgen walvis is dezelfde walvis als silhouet, met een cyaan rand en een "?" op zijn lijf.
9. **Menu:** Box is eruit. Er staan nu "Calm · 4-7-8", "Rounds 3 x 30" (gekozen) en "Sea log", zodat je je dieren ook bereikt zonder te duiken.
10. **Veiligheid:** voluit "Never hold your / breath in water / or while driving." met "Sit. Stop if dizzy." in geel eronder. Het blok staat lager en OK staat op 76,5% D.
11. **START-boog:** staat nergens meer. Hij stond er op drie schermen en wekte de indruk dat START elders niets doet. De gekozen pil en de OK-knop laten al zien wat START doet.

Kan-punten: walvissen 1,2% D naar links (kan 2). Icoon met dunnere ring, zonder bouten en met een grotere walvis; leest op 70 en 40 px (kan 4, GEZIEN). Op AMOLED blijft alles boven het water zwart (kan 5). Titels klein, items met een hoofdletter (kan 1; stond al zo). Niet gedaan: "round 1, 2, 3" bij today (kan 3). De tijden zeggen het al, en op 260 past er geen vierde regel bij zonder dat de letters te klein worden.

## Bouwbaar: elk 454-effect in één zin (voor Gijs; GOK = nakijken in de simulator)
- **Zee-verloop:** per scherm een vaste achtergrond-PNG van de zee in een paar dieptestanden (duiken: 3 standen, 94/123/183 m), via `drawBitmap`. Het golfje bovenop teken je zelf met `fillPolygon`, zodat het blijft bewegen. GOK geheugen: één volle 454-PNG is in 16-bit ±400 kB, dus beter alleen het onderste deel als bitmap (±60% van het scherm) en maar één tegelijk laden.
- **Zachte randen en letters:** `dc.setAntiAlias(true)` (API 3.2+, AMOLED-horloges hebben dat) voor golven, dieren en ring. De letter is Barlow als eigen font in de resources, op AMOLED met antialias.
- **Gloed onder het schuim:** een smalle bitmapstrook met alfa (±454 x 30 px) die je langs de golf herhaalt, of drie lijnen in afnemende tint naast elkaar zonder alfa (goedkoper, bijna hetzelfde).
- **Lichtstralen:** zitten al in de achtergrond-PNG (ze bewegen niet), dus kosten ze geen extra geheugen.
- **Zon met gloed:** één kleine PNG (±150 x 80 px) met de gloed erin, de zon zelf met `fillCircle`.
- **Grafiekvlakken (today, 8 weeks):** een verlooprechthoek als kleine PNG (bijvoorbeeld 8 x 120 px, uitgerekt met `drawScaledBitmap`, API 3.2+, GOK), geknipt met de vorm via `setClip` per kolom, of eenvoudiger: horizontale lijnen van 1 px in oplopende tint, elk geknipt op de grafiek. Dat laatste kan overal.
- **Voortgangsring en dieren:** gewone tekenfuncties (`drawArc`, `fillPolygon`, `fillCircle`). Het streepje per dier is een `drawLine`.
- **MIP (260):** alles met tekenfuncties in de 64 MIP-kleuren, zonder bitmaps voor de zee.

## Gemeten (`blad3/meting-v3.txt`) en bekeken
- **Kader** van alles wat getekend is: binnen 1,5 px van het schermmidden op alle 26 beelden (eis 2 px). De 1,5 px komt van de walvis op de sea log, die bewust iets naar links staat.
- **Optisch midden** (zwaartepunt van tekst, dieren en lijnen) op 260: binnen 2 px op elf schermen. Uitzonderingen: today en 8 weeks (+5,7 px), want het record van vandaag staat rechts en dat is de data. De sea log zit op +2,8 px.
- **Lettermaten:** kleinste letter op 260 is 20 px (14 px kapitaalhoogte); grote cijfers 0,26 tot 0,32 D.
- **Kleuren 260:** 0 pixels buiten MIP.
- Alle 26 beelden en het blad heb ik zelf met Read bekeken, op beide maten naast elkaar.

## Beeldtaal (de 10 regels van `ebb-blad-v2.md`, met deze wijzigingen)
Regel 4: één schaal van vier blauwtinten, op AMOLED als zacht verloop met gloed, op MIP als harde vlakken zonder dithering. Regel 5: oranje = voortgang. Regel 6: kleinste letter 20 px op 260; op AMOLED zachte letters. Regel 8: elk dier zijn eigen tint (walvis, vis en kwal warm, schildpad groen), verder in dezelfde stijl.

## Open, buiten het blad (productkeuze, bij Gijs)
Meer dieren dan vier tot 3:00, en het veiligheidsscherm ook vóór de eerste ronde. Allebei staan ze als vraag in `platformen/garmin/taken.md`.
