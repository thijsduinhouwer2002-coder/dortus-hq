# Voorstel: betaalde wijzerplaten voor Wear OS op Google Play

Vera, 8 nov 2026 run 02:33 (UTC). Nagekeken door een controleur: niet akkoord met mijn eerste mediaan, correcties hieronder verwerkt. Gekozen na Facer: wie wijzerplaten wil verkopen zonder uitnodiging, doet dat op Google Play.

## Wat het is
Wijzerplaten voor horloges met Wear OS (Pixel Watch, Galaxy Watch en andere) staan als losse apps in Google Play. Sinds 27 jan 2025 moeten nieuwe wijzerplaten in Watch Face Format (een XML-formaat, gemaakt met Samsung Watch Face Studio, de Figma-plugin Watch Face Designer of met de hand). Google rekent af. Afdracht: 15% over de eerste $1 miljoen per jaar (in EER, VK en VS sinds 30 juni 2026 10% plus 5% voor de betaling). Een ontwikkelaarsaccount kost eenmalig $25 (account van Thijs nodig).

## Cijfers

### Bereik
- GEZIEN: zelf verzameld via de categorie WATCH_FACE, 50 zoekopdrachten en daarna alle apps op de makerpagina's van de gevonden makers: 6.315 apps, waarvan 4.084 wijzerplaten van 271 makers. Per app het exacte aantal installs (realInstalls, hetzelfde getal waarvan Play "100+" maakt). Data: `data/wearos-wijzerplaten-2026-11-08.jsonl`, script `data/wearos-haal-script.py`.
- GEZIEN, lichting mei t/m aug 2026 (3 tot 6 maanden oud), betaalde wijzerplaten van gevonden makers (n=339): mediaan 117 installs, 53% haalt 100+, 6,8% haalt 1.000+, hoogste 2.696. Lichting 2025 betaald (n=851): mediaan 385, 75% 100+.
- Controleur: deze makers zijn gevonden omdat ze zichtbaar zijn, dus het beeld is te mooi. Hij vond via "lijkt op" en "meer van deze maker", beginnend bij kleine apps, nog 113 wijzerplaten uit de lichting die ik miste, en de titelfilter miste nog 102 (vooral betaald, mediaan 72). Alles samen (n=568 betaald): mediaan ±75, 45% 100+, 5% 1.000+. Data: `data/wearos-controleur-extra-2026-11-08.jsonl`.
- GEZIEN door de controleur, **nieuwe onbekende makers** (24 makers, 49 betaalde wijzerplaten uit mei t/m aug): mediaan 9 installs, 14% 100+, 4% 1.000+. Maar 5 van de 24 makers halen per wijzerplaat een mediaan van 100 of meer. Deze steekproef leunt naar klein; de echte mediaan voor een nieuwkomer ligt tussen ±10 en ±75 (GOK).
- GEZIEN, nieuwkomers in mijn eigen set (eerste wijzerplaat in 2026): sterk wisselend. Vesterjil (14 wijzerplaten) 1.077 tot 6.342 per stuk, TMZ Visionary 146 tot 1.424, MKW 205 tot 1.284; maar Darwin Hub, Felsh, CMDN (16 tot 20 wijzerplaten elk) nog 0 uit de lichting en GoodTimes rond 100.

### Geld
- GEZIEN: betalen zit in Google Play. Van de lichting is 86% betaald, meestal $0,99 tot $2,99 (vaakst $1,99 en $1,49).
- GOK op GEZIEN: installs maal prijs voor de 339 betaalde wijzerplaten is $171.000 bruto, mediaan per maker ±$640 bruto voor de wijzerplaten uit 4 maanden. Dit is een bovengrens: installs zijn geen verkopen. Promotiecodes, tijdelijk gratis acties, delen in de gezinsbibliotheek en terugbetalingen tellen mee, en daar gaat nog 15% af.
- GEZIEN (onderzoeker): tijdelijk gratis weggeven is heel gewoon. Op mydealz.de alleen al ±30 gratisacties voor Wear OS-wijzerplaten in 2026; op de Play-pagina van amoledwatchfaces stonden op 8 nov twee wijzerplaten op 100% korting.
- NIET GEVONDEN: geen enkele kleine maker met een openbaar omzetbedrag. Samsung-forumdraadjes over winst geven 404 sinds de overstap, Reddit en XDA niet leesbaar vanaf hier.
- GOK: een nieuwkomer die het goed doet verdient een paar honderd dollar per maand met tientallen wijzerplaten; de gewone nieuwkomer tientjes.

### Drukte
- GEZIEN: in mijn set ±80 tot 110 nieuwe wijzerplaten per maand in 2025 en voorjaar 2026, maar 158 in september en 201 in oktober 2026. Dat is alleen het deel dat ik vond; het echte aantal is veel hoger. Het aanbod groeit snel.
- DERDEN: Google meldt 180%+ groei van Watch Face Format-wijzerplaten in een jaar (googleblog, mei 2025). Met de Figma-plugin Watch Face Designer (bijgewerkt 5 mrt 2026) wordt maken nog makkelijker.

### Vindbaarheid
- DERDEN: zoeken in Play (filter "Watch faces"), de categoriepagina, makerpagina's en "lijkt op". Zoeken geeft vooral bekende makers terug (controleur: 50 zoekopdrachten met zeldzame woorden gaven maar 4 apps uit de lichting).
- DERDEN: dealsites en gratisacties zijn aantoonbaar een kanaal. Grote abonnementsapps (Facer, WatchMaker, Pujie) krijgen via Watch Face Push (Wear OS 6) extra kracht en zijn concurrenten.
- DERDEN: Galaxy Store valt af als tweede winkel; Samsung noemt die voor deze wijzerplaten alleen voor China.

### Past het bij ons
- Ja, technisch: een wijzerplaat in Watch Face Format is een klein XML-pakket met plaatjes, in dagen te bouwen en te herhalen. Uiterlijk is alles, wat past bij de nieuwe lat van Dortus. Nadeel: testen vraagt een emulator of horloge, en het Play-account moet van Thijs komen.

## Voor- en nadelen
- Voor: open winkel zonder uitnodiging, betalen ingebouwd, kopers betalen echt voor een wijzerplaat, sommige nieuwkomers halen duizenden installs per wijzerplaat, snel te maken.
- Tegen: de gewone nieuwkomer haalt ±10 installs per wijzerplaat, lage prijzen ($1 tot $2), aanbod groeit hard, zoekresultaten bevoordelen bekende makers, verkopen niet zelf te meten (installs zijn een bovengrens), AI-hulp maakt het aanbod nog groter.

## Idee
Een reeks van 20 tot 30 opvallende wijzerplaten met één herkenbare eigen stijl, gratis broertje plus betaalde versie, en gratisacties bij de start. Alleen zinvol als we een stijl hebben die echt opvalt.

## Cijfer en advies
Cijfer 4. Advies: nee voor nu. Geld bestaat aantoonbaar in de winkel, maar per wijzerplaat is het klein en de gewone nieuwkomer blijft rond 10 installs. Wat het zou veranderen: een openbaar omzetbedrag van een nieuwkomer, of een meting die laat zien wat de 1 op 5 nieuwkomers met 100+ anders doet (stijl, gratisacties, aantal). Herhaalmeting kan met de scripts in `data/`.
