# Ontwerp koersverschil-scanner (19 nov 2026)

**Wat en voor wie:** een meting voor Thijs: bestaan er tussen crypto-beurzen prijsverschillen boven alle kosten
die lang genoeg blijven staan en waar opnemen en storten open is? **Af** = de workflow draait 4 keer per dag
±5,5 uur, de data staat op de tak `ai-handel-data`, `rapport.py` maakt er per dag en totaal echte kansen,
mediane winst, beste munten en beurzen en een som voor €2.000 en €5.000 van, en de tests zijn groen.

## Drie aanpakken
1. **Alle orderboeken elke ronde ophalen.** Precies, maar duizenden verzoeken per 20 seconden: de beurzen zetten
   ons dan vast. Valt af.
2. **Websockets per beurs.** Snelst en meest precies, maar 15 verschillende protocollen en lang bouwen. Te groot
   voor een uur en voor een vraag die ook met 20 seconden resolutie te beantwoorden is.
3. **Gekozen: middenweg.** Eén verzoek per beurs per ronde voor bod en laat van alle paren (bulk-ticker), en
   alleen voor kandidaten het orderboek. Een rooster (open kansen, dan nooit gecontroleerd, dan langst geleden)
   zorgt dat alle kandidaten om de beurt aan bod komen met hooguit 100 boekcontroles per ronde.

## Keuzes
- Geen omrekenen tussen quotes (opdracht). Euro alleen voor het optellen in het rapport.
- Echte kans vereist opnamestatus **bekend en open**. Onbekend telt niet (voorzichtig), maar staat apart in het
  rapport, zodat zichtbaar is hoeveel we daardoor misschien missen.
- Overlappende kansen van dezelfde munt zijn één gebeurtenis (je kunt de goedkope voorraad maar één keer kopen).
- Opslaan op de tak met een verse clone per poging en een gewone push: geen rebase, geen force, geen botsing met
  de schaduwbot (andere map).
- Proefruns (met de hand) hebben een eigen concurrency-rij en raken de klok niet, zodat een proef de vaste meting
  niet stopt of 6 uur uitstelt.

## Bekende grenzen
Netwerk per munt niet vergeleken; overmaaktijd niet gemeten; opnamekosten bij een deel van de beurzen geschat;
de API is de wereldwijde versie, niet altijd de EU-versie met vergunning. Alles staat in README.md.
