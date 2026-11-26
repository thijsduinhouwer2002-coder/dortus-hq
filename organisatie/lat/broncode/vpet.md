# Broncode: VPet-Simulator (Steam, gratis, desktop-huisdier)

Uitgeplozen door de Afkijker op do 26 nov 2026 (±13:30 NL), voor issue #20. Code gelezen uit `git clone --depth 1` van https://github.com/LorisYounger/VPet (laatste commit 51da0bd, 26 nov 2026; niets uitgevoerd). Winkelpagina, appdetails en de best beoordeelde negatieve reviews met curl gelezen.

## Waarom dit project
- **Steam: "Overwhelmingly Positive", 95% van 3.761 Engelse reviews, laatste 30 dagen 98% van 470** (GEZIEN, https://store.steampowered.com/app/1920960/, 26 nov). Uit sinds 13 aug 2023, gratis, 75 prestaties, Workshop en Steam Cloud, 3 gratis DLC (GEZIEN, `store.steampowered.com/api/appdetails?appids=1920960`).
- Het is een figuur dat op je bureaublad leeft terwijl je werkt: zelfde plek en zelfde klant als Hats of the Fallen (Steam-labels Desktop Companion, Idler).
- Licentie: Apache-2.0 (GEZIEN, `LICENSE`). Code overnemen mag met hun naam en licentietekst erbij; het idee nabouwen in GDScript is het schoonst.
- Het spel is in C# met WPF, alleen voor Windows. We lenen dus regels en getallen, geen code.

## Wat ze slim doen (bestand en regels)
1. **Vragen met een dobbelsteen die steeds kleiner wordt.** Heeft het figuur honger, dan gooit het elke tik `Rnd.Next(teller--) == 0` (`VPet-Simulator.Windows/MainWindow.cs` r. 622 tot 624 en 649 tot 651). Na de start is de teller 20 (r. 561 tot 562), daarna 200: de kans is dan eerst 1 op 200, dan 1 op 199, enzovoort: nooit twee keer kort na elkaar, en toch gegarandeerd binnen de cyclus (standaard 200 tikken, `Function/Setting.cs` r. 35). Na het vragen gaat de teller terug naar 200. De zin hangt af van hoe erg het is (licht, midden, sterk) en hoe goed je elkaar kent (`LowText`, 47 regels in `mod/0000_core/text/LowText.lps`).
2. **Niets doen wordt niet gestraft: het figuur koopt zelf.** Met "AutoBuy" aan koopt het zelf eten en drinken als het onder 70% zakt, voor 1,2 keer de prijs, en alleen gezond eten (`MainWindow.cs` r. 563 tot 600). Wegkijken kost dus een beetje munt, nooit het figuur.
3. **Hoe langer het stil is, hoe groter de kans dat het iets doet.** Elke 15 s (`Display/MainLogic.cs` r. 35) kiest het uit `Rnd.Next(max(20, 200 - CountNomal))` (r. 550): bewegen, rondhangen, slapen of iets eigens. `CountNomal` telt de stille tikken en gaat op 0 zodra je klikt (`Display/Main.xaml.cs` r. 356). Is het aan het werk, dan is de kans meer dan twee keer zo klein (r. 552). Zo is het rustig als jij bezig bent en levendig als je even kijkt.
4. **Jij kiest of de muis erdoor gaat, en je ziet het.** In het menu bij het icoon in het systeemvak zet je "doorklikken" aan of uit (`MainWindow.xaml.cs` r. 855 tot 882, `WS_EX_TRANSPARENT`). Staat het aan, dan wordt het figuur doorzichtig (standaard 60%, `Function/Setting.cs` r. 517), zodat je ziet dat klikken nu naar het venster eronder gaat. "Altijd bovenop" is ook een eigen keuze (`SetTopMost`, r. 585), en bij het openen van de instellingen gaat het figuur even naar achteren (`Function/MWController.cs` r. 195).
5. **Wie aan de rand van het scherm sleept, verstopt het half.** Sleep je het figuur over de rand, dan gaat het in een "zijkant-verstopt" houding en piept het om de hoek (`Display/MainLogic.cs` r. 596 tot 637), in plaats van weg te raken.

## Wat gebruikers klagen (negatieve reviews, best beoordeeld, GEZIEN 26 nov, https://steamcommunity.com/app/1920960/negativereviews/?browsefilter=toprated)
- **"Malware", veruit de grootste klacht (7 van de 10 bovenste negatieven):** "after uninstalling it, it keeps trying to force itself to reinstall. every time I boot up my pc i get a pop up to install it" (28 aug 2023); "This game is 100% Malware. It keeps trying to reinstall itself" (8 sep 2023); "DO NOT DOWNLOAD. It tries to reinstall itself if you uninstall it" (24 aug 2024). Oorzaak staat in de code: "starten met Windows" zet een snelkoppeling in de map Opstarten (`WinDesign/winGameSetting.xaml.cs` r. 1484 tot 1512), die via Steam start. Steam ruimt die bij verwijderen niet op, dus daarna vraagt Steam bij elke start om het spel te installeren. De makers wisten het: de uitleg erover staat uitgezet in `MainWindow.cs` r. 2716 tot 2724 ("游戏卸了也不知道", het spel weet niet dat het verwijderd is). Wie het al aan had, krijgt de snelkoppeling na een update nog een keer opnieuw gemaakt (r. 2344 tot 2349).
- **Mods van anderen die alles laten vastlopen:** "downloaded some steam community mods, and lead to a big Frozen screen" (5 jun).
- **Slechte Engelse vertaling en ongemakkelijke zinnen:** "english translation makes it unfun, and i also wish that she wouldn't call me master" (27 mei 2025).
- **Foutmeldingen vol code:** "nothing works and when it doesn't it spits code at me. I'm not a coder" (29 aug 2023).
- Issues op GitHub kon ik niet lezen: buiten onze repo's geeft de API 403.

## Welk product wordt er beter van
**Hats of the Fallen** (`producten/steam-hol/godot/`).
1. **Nooit "start met Windows" zonder opruimen.** Het grootste gevaar voor de reviews van een bureaubladspel is niet saai, maar "malware". Thijs zei over Hats al "voelt als een virus" (issue #19). Regel: geen snelkoppeling in Opstarten en niets in het register zolang er geen nette weg is om het weg te halen; komt het er ooit, dan uit standaard, met een zin in de instellingen hoe je het weghaalt.
2. **"Doorklikken" en "Altijd bovenop" als vinkjes in het menu van het systeemvak** (`kern/systeemvak.gd` heeft nu Pause, Sound, Height, Quit). Met doorklikken aan wordt de strook doorzichtig, zodat je ziet dat de muis erdoor gaat. Dat geeft de koper de baas over zijn scherm: het tegendeel van een virus.
3. **Vraag-dobbelsteen voor het tempo** (past bij tempo-regel 2 in `organisatie/lat/hats-tempo.md`): als een held of Gloop iets wil, kans per tik 1 op N, N telt af, daarna terug naar N. Nooit twee vragen kort na elkaar, nooit langer dan N tikken niets.
4. **Levendig als je kijkt, rustig als je werkt:** de kans dat er iets gebeurt groeit met de stille tijd en gaat op nul bij een klik; tijdens typen kleiner.

Geen nieuw issue (bijsturing hoofdmanager 25 nov 15:45): de lessen staan in `organisatie/lat/hats.md` onder Lessen uit broncode. Punt 1 is een verbod, geen bouwwerk; punt 2 is klein en past bij het menu van #24.
