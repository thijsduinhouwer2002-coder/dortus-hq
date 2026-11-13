# Roku Channel Store (Vera, 13 nov run 17:41)

Wat het is: de winkel van Roku, het grootste tv-systeem in de VS (±90 miljoen huishoudens, DERDEN). Makers kunnen een kanaal laten betalen bij installatie, of verkopen in het kanaal en via abonnementen met Roku Pay. Kanalen worden gebouwd in BrightScript en SceneGraph; testen gaat op een echt Roku-apparaat (geen officiële emulator, GOK uit eerdere kennis). Waarom bekeken: nog nooit gemeten, en tv-winkels hebben weinig van onze concurrenten.

## Eigen meting (13 nov 2026, winkel VS, robots.txt staat alles toe)
Een onderzoeker las de open winkel-API rustig uit (hooguit 2 verzoeken per seconde). Ik heb de kernuitkomst zelf nagerekend op de ruwe data.
- GEZIEN: per kanaal geeft `/api/v6/channels/detailsunion/<id>` maker, prijs, aantal beoordelingen (`ratingCount`), sterren, eerste publicatiedatum en verdienvorm. Installs of omzet geeft de winkel niet; het aantal beoordelingen is de enige maat.
- GEZIEN: 11.548 kanalen gevonden in 20 van de 26 categorieën (zes grote media-categorieën niet doorgebladerd; GOK totaal 15.000 tot 25.000). 357 kanalen vragen geld bij installatie (±3%), meestal $0,99 tot $4,99; 70 werken met een maandbedrag.
- GEZIEN, alle 357 betaalde kanalen: mediaan 2 beoordelingen. Wat telt is de leeftijd:
  - betaald, gepubliceerd in 2025 of 2026: 144 kanalen, mediaan 0, hoogste 3 beoordelingen, geen enkele met 10 of meer (zelf nagerekend);
  - betaald, 2023 en 2024: 35 kanalen, mediaan 1, twee met 10+ (beste Search with Google, 615);
  - betaald, 2017 of ouder: mediaan ±135, 51 van de 58 met 10+.
- GEZIEN, gratis kanalen (169 in de steekproef): gepubliceerd in de laatste 12 maanden 96 stuks, op één na allemaal onder 10 beoordelingen; ouder dan 3 jaar mediaan 1.748.
- GEZIEN: de kleine makers met veel beoordelingen zijn allemaal oud: Payout Bingo ($0,99, 4.895, 2016), Aquarium Screensaver van TheEndless ($3,99, 3.636, 2012), HangMan ($0,99, 1.023, 2013), Candy Bear ($2,99, 728, 2011).
- GEZIEN: Storm Jam LLC heeft 81 betaalde kanalen (vooral schermbeveiligers) met mediaan 0 beoordelingen. Veel kanalen stapelen werkt niet.
- GEZIEN: er komt wel veel bij (127 betaalde kanalen alleen al in 2026), dus de deur staat open, maar nieuwkomers krijgen geen kopers die iets achterlaten.

## Oordeel tegen "Wat een 8 is"
- Bereik: zwak. Nieuwe kanalen, betaald en gratis, blijven op 0 tot 3 beoordelingen. De winkel toont vooral wat Roku zelf kiest en wat al jaren bestaat.
- Geld: kan (betalen bij installatie, Roku Pay), maar dat kleine nieuwe makers er nu aan verdienen is niet te zien. De verdieners zijn makers van 2011 tot 2017.
- Bouwen: matig. BrightScript is te leren en draait op Linux, maar testen vraagt een echt apparaat via Thijs of een gekocht kastje.
- Thijs: ontwikkelaarsaccount, Roku Pay met belasting- en bankgegevens.

Cijfer 2, nee. Herhaalmeting niet nodig; alleen opnieuw kijken als Roku de winkel omgooit (bijvoorbeeld een nieuwe sectie voor nieuwe kanalen). LG webOS en Samsung Tizen heb ik niet gemeten; die hebben dezelfde soort winkel met nog minder openbare tellers (GOK), dus lage prioriteit.

Data: data/roku-details-2026-11-13.jsonl (526 kanalen, zonder e-mailadressen van makers), scripts data/roku-haal-script.py en data/roku-analyse-script.py. Controleur: geen aparte; de onderzoeker mat en ik rekende de kernuitkomst (144 betaalde kanalen van 2025 en 2026, hoogste 3 beoordelingen) zelf na.
