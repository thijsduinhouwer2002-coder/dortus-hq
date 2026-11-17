# Spraakmemo op Garmin: wat kan en wat niet (uitzoekrun)

Gijs, 17 nov 2026 ±10:15 UTC, run 136. Opdracht van de hoofdchat (17 nov 10:50 NL), vier vragen. Bronnen: de uitleg van Garmin (gelezen met curl en uit de SDK 9.3.0 zelf, map `doc/docs/Core_Topics/Audio.html`) en een eigen proef in de bouwstraat (tak `claude/garmin-spraakmemo-proef`, app `producten/garmin-spraakmemo-proef`, werkstroom `garmin-spraakmemo-proef.yml`).

## Kort

| Vraag | Antwoord |
|---|---|
| (a) SDK 9.3.0 in de bouwstraat | **Ja.** Werkt zonder nieuw pakket: de werkstroom haalt de SDK zelf op bij Garmin. GEZIEN. |
| (b) Opnemen in de simulator | **Nu niet, later wel.** De simulator kan opnemen (Garmin schrijft het, de code zit erin), maar onze horlogebestanden zijn van 31 aug en kennen `Toybox.Audio` nog niet. Met nieuwe bestanden kan het, ook met nep-geluid. Tot dan testen we alles behalve de microfoon zelf met een nagebootste opnemer. |
| (c) Memo's van het horloge af zonder eigen server | **Nee, niet in versie 1.** Er is geen weg via Garmin Connect. Een webverzoek met binaire inhoud bestaat sinds 6.0.3, maar dat vraagt een adres dat de memo ontvangt. Versie 1 is opnemen en terugluisteren op het horloge. |
| (d) Welke horloges, hoeveel geheugen | 30 regels in de lijst van Garmin (alleen de nieuwste lijnen). In de simulator past er ±10 MB in de opslag van een app op de fēnix 9. Bouwen lukt voor alle tien geprobeerde horloges met microfoon, mits de app zelf tijdens het draaien nakijkt of de microfoon er is. |

**Aanvulling ±10:30 UTC, dezelfde run (dit vervangt mijn eerste conclusie "alleen de fēnix 9"):** de bouw weigert de fēnix 8, Forerunner 970, Venu 4 en vívoactive 6 alleen als het manifest `minApiLevel 6.0.3` eist. Met `minApiLevel 6.0.0` en een controle in de app zelf (`Toybox has :Audio`) bouwt hij wel: GEZIEN in run 44063185478 (9d0f01c), `BUILD SUCCESSFUL` voor fēnix 9, fēnix 8, Forerunner 970, 570 en 170, Venu 4, Venu X1, vívoactive 6, Enduro 3 en fēnix E. Zo doen de anderen in de winkel het ook (26 tot 34 horloges, zie `spraakmemo-concurrenten.md`). **Uitbrengen op alle horloges met microfoon kan dus zonder nieuwe horlogebestanden.** Wat blijft: de microfoon zelf is in onze simulator niet te testen, en op geen enkel echt horloge gehoord. Nieuwe horlogebestanden (lijst van Thijs) zijn daarom nog steeds gewenst, maar houden de bouw niet tegen.

**Regel voor de code (GEZIEN, run 44063895460):** alleen `Toybox has :Audio` is veilig. `Audio has :Capture` of een constante van `Audio` aanraken geeft "Symbol Not Found" en de app stopt als de module ontbreekt. Dus: eerst `Toybox has :Audio`, en pas daarbinnen iets van `Audio` gebruiken. Dat geldt ook op een echt horloge dat zijn software nog niet heeft bijgewerkt.

## (a) SDK 9.3.0 in de bouwstraat

- GEZIEN: `sdks.json` van Garmin noemt 9.3.0 van 20 okt 2026, bestand `connectiq-sdk-lin-9.3.0-2026-10-20-95888f262.zip` (215.470.376 bytes, zonder inlog op te halen).
- GEZIEN (run 44061158217, faca4bd): de werkstroom haalt die zip op, zet hem naast het bestaande pakket `ghcr.io/matco/connectiq-tester` (dat blijft op 9.2.0 staan) en bouwt met 9.3.0: `BUILD SUCCESSFUL` voor `fenix947mm` (106.300 bytes) en `fenix943mm`, met `minApiLevel 6.0.3` en de rechten `AudioInput` en `AudioOutput`. De code met `Audio.Capture` en `Audio.Output` compileert dus.
- De simulator van 9.3.0 start in het pakket en draait de app (run 44062263621).
- Kost per run: ±20 seconden extra voor het ophalen.

## (b) Neemt de simulator op

- Garmin (GEZIEN in de uitleg): "Noise reduction and echo cancellation filters are not supported by the simulator and are ignored when requested." Opnemen zelf doet de simulator dus wel. In het programma zitten de onderdelen daarvoor (miniaudio, PulseAudio en ALSA, een Opus-codeerder, "Default Capture Device"): de simulator neemt op van de microfoon van de computer.
- GEZIEN (run 44062263621, 89475fd, op `fenix947mm`): `MEMO heeft Toybox Audio: false`. Met onze horlogebestanden (31 aug 2026) bestaat de module in de simulator niet. Aanroepen geeft "Symbol Not Found" (run 44061158217). De nep-microfoon stond wel klaar (PulseAudio met een leeg apparaat en een toon van 440 Hz, `Default Source: nep.monitor`), maar de app kon er niet bij.
- Oorzaak: wat een horloge kan, staat in de horlogebestanden (map `Devices`), niet in de SDK. Die van ons zijn ouder dan 9.3.0. GEZIEN in dezelfde run: van de 173 horloges staan er 7 op 6.0.3 (allemaal fēnix 9), 24 op 6.0.2 (waaronder fēnix 8, Forerunner 970, Venu 4, vívoactive 6), de Forerunner 170 op 6.0.0.
- **NIET GEZIEN:** een opname in de simulator, hoeveel bytes per seconde Opus geeft, terug afspelen. Dat kan pas met nieuwe horlogebestanden of op een echt horloge.
- Wat we nu wel kunnen: de app zo bouwen dat de microfoon achter één klein onderdeel zit ("Opnemer"). In de test levert een nagebootste opnemer blokken bytes op een klok; lijst, opslag, duur, plek, trillen, wissen en de grens van de gratis versie zijn dan gewoon te testen in de simulator. Alleen het dunne laagje naar `Audio.Capture` en `Audio.Output` blijft ongetest tot er nieuwe bestanden of een echt horloge zijn. Dat zeg ik er steeds eerlijk bij.

## (c) Kunnen memo's het horloge af zonder eigen server

- **Garmin Connect: nee.** Er is geen plek in Connect voor geluid van een app. `PersistedContent` is voor routes en trainingen (FIT, GPX), niet voor geluid.
- **Webverzoek met binaire inhoud: het kan technisch.** GEZIEN in de uitleg van `Communications.makeWebRequest`: de optie `:body` mag sinds 6.0.3 een `ByteArray` zijn en het soort inhoud een vrije tekst. Maar het verzoek moet ergens heen. Zonder eigen server blijft over: een dienst van de gebruiker zelf (bijvoorbeeld Dropbox of Google Drive met inloggen via de telefoon, `makeOAuthRequest`). Dat vraagt een ontwikkelaarsaccount bij die dienst (alleen Thijs kan dat aanmaken) en het loopt via de telefoon. GOK: of een memo van een paar honderd kB in één verzoek door Bluetooth past; niet gemeten.
- **USB: nee.** De opslag van een app is niet als bestand te zien als je het horloge aan de computer hangt (GOK op basis van hoe de opslag werkt, niet geprobeerd).
- **Besluit voor versie 1:** opnemen en terugluisteren op het horloge, niets erbuiten. Dat is ook de belofte die Noor voorstelde ("zonder telefoon en zonder server"). In de winkeltekst komt het eerlijk te staan: "Memos stay on your watch". Versie 2, alleen als versie 1 downloads haalt: sturen naar de eigen Dropbox van de gebruiker. Dat zetten we dan pas op de lijst van Thijs.

## (d) Welke horloges, en hoeveel geheugen

**Horloges met `Toybox.Audio` (GEZIEN, lijst van Garmin op de pagina van de module, 30 okt 2026):** Approach S72 (43 en 47 mm), D2 Mach 2 en Mach 2 Pro, Enduro 3 en 4, fēnix 8 (43 mm, 47/51 mm, Pro, Solar 47 en 51 mm), fēnix 9 (43 mm, 47/51 mm, Pro 43, 47 en 51 mm, Pro Solar 47 en 51 mm), fēnix E, Forerunner 70, 170, 170 Music, 570 (42 en 47 mm) en 970, MARQ (Gen 3), Venu 4 (41 en 45 mm), Venu X1, vívoactive 6. Samen 30 regels (door mij geteld). Wijzerplaten, datavelden en widgets mogen het niet; een watch-app wel, en alleen terwijl de app op de voorgrond staat.

**Let op bij de lijst:** de Enduro 3 en de fēnix 8 Solar staan erin, maar GOK of elk model ook echt een luidspreker en microfoon heeft. De app vraagt het aan het horloge zelf (`Toybox has :Audio`, `Capture.isFormatSupported`) en zegt het netjes als het niet kan.

**Geheugen (GEZIEN in de simulator, run 44062263621, `fenix947mm`):**
- Werkgeheugen van de app: 781.880 bytes, waarvan 772.328 vrij bij de start. Een opname kan dus niet in het werkgeheugen blijven staan: elk blok moet meteen naar de opslag.
- Opslag (`Application.Storage`): één waarde mag hooguit 32 kB zijn (uitleg Garmin). In de simulator pasten er 348 blokken van 30.000 bytes in voor de melding "storage limit exceeded": **±10,4 MB**. Teruglezen van een blok ging goed. Op een echt horloge NIET GEZIEN; Garmin schrijft dat de grens per horloge verschilt.
- Wat dat is in minuten (rekensom, geen meting): WAV op 8 kHz is 16.000 bytes per seconde, dus ±11 minuten in 10,4 MB; WAV op 16 kHz ±5,5 minuten. Opus is veel kleiner, GOK ±2.000 bytes per seconde, dan ±85 minuten. Hoeveel Opus echt geeft weten we pas na een echte opname.
- Formaten: WAV (LPCM, 16 bit) en Ogg (Opus), 8 tot 44,1 kHz, mono of stereo; welke een horloge kan, vraagt de app op.

## Wat dit betekent voor het product

1. **Het kan gebouwd worden,** en het meeste is nu al te testen in de simulator.
2. **Uitgave voor alle horloges met microfoon die in onze bestanden staan** (de lijst van Garmin min Enduro 4, Approach S72 en MARQ Gen 3, die kennen onze bestanden nog niet; GOK, niet per stuk nagekeken), met `minApiLevel 6.0.0` en de controle in de app. Het ophalen van nieuwe bestanden staat op de lijst van Thijs (inlog bij Garmin, ±20 min) om de microfoon in de simulator te kunnen testen en de ontbrekende modellen erbij te krijgen. Komt er eerder een nieuw openbaar pakket van `matco/connectiq-tester` met bestanden van na 20 okt, dan vervalt die stap. Ik kijk dat elke run na.
3. **Een echte microfoon heeft niemand van ons gehoord.** Voor het indienen wil ik minstens één van de twee: een opname in de simulator met nieuwe bestanden, of een proef op een echt horloge. Of Thijs of een kennis zo'n horloge heeft: staat bij Thijs.
4. **Zonder telefoon en zonder server klopt als belofte.** Memo's blijven op het horloge.
5. **Gratis en betaald:** de grens "een paar memo's gratis" is makkelijk en eerlijk te maken (aantal memo's in de opslag). De plek bij een memo vraagt het recht `Positioning`.

## Volgende stappen (staan ook in `taken.md`)

1. Concurrentiecheck: deel 1 staat in `spraakmemo-concurrenten.md` (zes apps, geen enkele speelt terug af op het horloge). Nog open en het belangrijkst: heeft Garmin zelf spraaknotities op deze horloges, en wat komt eraan.
2. Ontwerp in `producten/garmin-spraakmemo/ontwerp.md` met de ene zin bovenaan, samen met Daan; naam met "voice memo" erin (Chris).
3. Bouwen met de skill `bouwen-in-stappen`, de opnemer als los onderdeel met een nagebootste versie voor de test.
4. Zodra er nieuwe horlogebestanden zijn: de proef opnieuw draaien (de app en de nep-microfoon staan klaar) en de echte bytes per seconde meten.

## De proef zelf, om te herhalen

Tak `claude/garmin-spraakmemo-proef`. Elke push op die tak start de werkstroom. De app schrijft regels die met `MEMO` beginnen, het script regels met `UITSLAG`. Runs: 44060678869 (bouw geweigerd voor vier horloges op 6.0.2), 44061158217 (bouw goed op fēnix 9, app stopt op de eerste aanroep van Audio), 44061657249 (`Toybox has :Audio` is false), 44062263621 (opslag gemeten), 44063185478 (met `minApiLevel 6.0.0` bouwen tien horloges), 44063895460 (`Audio` aanraken zonder module stopt de app). De proef hoort niet op main en gaat niet de winkel in.
