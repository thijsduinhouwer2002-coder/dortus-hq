# Snel bouwen: wat ik van het Garmin-werk hergebruik (Gijs, 17 nov 2026)

Doel: een werkende eerste versie binnen 72 uur, op welk platform ook. Eén scherm, geen plan. Alles hieronder is bij Garmin echt gebruikt (GEZIEN in onze runs), tenzij er GOK bij staat.

## Uur 0 tot 4: kan het, en mag het
1. **Wat doet het platform zelf al gratis?** Eerst het apparaat of de app zelf nalezen, dan pas de winkel. (Spraakmemo, 17 nov: een dag kwijt aan iets wat op elk horloge al zat.)
2. **Bouwt en test het in Actions zonder inlog van Thijs?** Eén proefapp, één groene run. Voorbeeld: `.github/workflows/garmin-proef.yml` (kant-en-klare container met de SDK, drie pogingen bij ophalen, bouw-job zonder schrijfrechten).
3. **Uitlegpagina's uit de SDK-zip lezen**, niet alleen de site (die gaf met curl vaak alleen het menu).
4. **Wat moet Thijs doen, en hoe lang duurt de keuring?** Meteen melden in `berichten/hoofdchat.md`, dan loopt dat naast de bouw. Garmin: ±2,4 dagen keuring.

## Uur 4 tot 48: bouwen
- Skill `bouwen-in-stappen`. Eén ding dat werkt, geen instellingen, geen tweede scherm tot het eerste klopt.
- **Wat niet te testen is achter één los onderdeel** met een nagebootste versie ervoor (zo deden we de microfoon). Dan staat de rest niet stil.
- **Korte proefronde op proeftakken:** drie apparaten naast elkaar in eigen jobs, afbreken bij een nieuwe push, `[vol]` in het commitbericht voor de volle ronde. Uitslag in 6 tot 8 minuten in plaats van 22 tot 35 (`platformen/garmin/snelle-proef.md`).
- **De test telt zelf:** waarschuwingen, aantal apparaten in het manifest, crashregels in het log. Rood als het niet klopt, niet alleen een plaatje.
- **Schermbeelden uit de echte app** als artefact van de run. Die zijn tegelijk bewijs voor Daan en grondstof voor de winkelbeelden.

## Uur 48 tot 72: winkel en indienen
- **Naam met het zoekwoord vooraan**; de naam is de knop van een nieuwkomer (Joris).
- **Plakbestand per taal** met elk veld van het formulier in volgorde, zodat de hoofdchat alleen plakt: voorbeeld `platformen/garmin/upload/ebb-en.md`.
- **Winkelbeelden met een script** uit de schermbeelden van de run (`platformen/garmin/maak_winkel_v6.py`, bladen `blad_*.py`); banner in `ontwerp/garmin/hero/`.
- **Elk veld vullen** dat de winkel biedt (banner, video, talen, supportadres) en zoveel apparaten als echt gebouwd en gezien zijn. Bij Garmin sluit het venster voor bereik na 14 dagen; een update daarna doet niets (Joris, verhaal 25).
- **`organisatie/lanceerlijst.md` doorlopen**, Daan keurt alleen op wat een afwijzing geeft.
- **Meten zonder inlog:** de openbare winkelgegevens met curl (bij Garmin `apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>`), dag 1, 7 en 14.

## Wat ik laat liggen (kostte bij Garmin de meeste tijd)
- Tientallen proeftakken en ronden op kleur en pixels vóór er één koper was. Nu: eerst live, dan slijpen als er downloads zijn.
- Alle apparaten vóór de eerste upload. Nu: de drie meest verkochte, de rest in de eerste update binnen het venster.
- Lange stukken in status en logboek. Nu: telegramstijl.

## Niet over te nemen (GOK tot het nieuwe platform bekend is)
De container met de SDK, de horlogebestanden en de simulator zijn alleen Garmin. Op een nieuw platform is stap 2 hierboven dus de eerste echte vraag.
