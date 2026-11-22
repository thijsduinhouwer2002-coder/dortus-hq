# Voorstel: Reallusion Marketplace (iClone, Character Creator, Cartoon Animator)

Vera, 8 nov 2026, run 17:33 (Amsterdam). Controleur akkoord met de cijfers, 4 correcties verwerkt.

## Kort
**Advies: nee voor nu. Cijfer 3.**
Een levende winkel (±450 nieuwe items per maand, 73.078 items) waar nieuwe items van kleine makers wel in de bestsellerlijst komen, en de maker 70% krijgt. Maar verkopen zijn nergens te zien, echt geld krijg je pas na erkenning als Certified Content Developer, de winkel draait op 3D-content (personages, kleding, animaties, decors) en niet op software, en de pluginmarkt is piepklein: 61 plugins in totaal, 10 nieuwe in 2026 van 6 makers. Groot worden kan hier niet met wat Dortus het beste kan.

## Hoe gemeten
- Open zoek-API van de winkel gevonden in app.js: `api.reallusion.com/Marketplace20/v1/Content/OpenSearch` (POST, veld Condition met OrderBy en Range). robots.txt van marketplace.reallusion.com staat alles toe behalve /temp. Rustig gelezen, 1,5 s tussen verzoeken.
- De 3.500 nieuwste items (11 feb t/m 8 nov 2026), de top 300 bestsellers van de laatste 3 maanden, en alle 61 plugins.
- Datum: de tijdstempel in de naam van de thumbnail. De controleur legde die naast CreateDate van 4 items: minder dan een dag verschil, ±1% ruis. Goed genoeg voor maandtellingen.
- Niet gemeten: verkoopaantallen. De pagina heeft een veld PurchasedTimes, maar de API geeft het voor elk item leeg (ook voor de bestsellers); de winkel toont het alleen intern. Niet geprobeerd te omzeilen.
- Scripts en data: `data/reallusion-lijst-script.py`, `data/reallusion-nieuwste-2026-11-08.json`, `data/reallusion-top300-3mnd-2026-11-08.json`, `data/reallusion-plugins-2026-11-08.json`.

## Cijfers
**Drukte**
- GEZIEN: nieuwe items per maand: mrt 558, apr 344, mei 457, jun 221, jul 198, aug 252, sep 388, okt 494. Gemiddeld ±360 tot 450.
- GEZIEN: cohort mei t/m aug 2026: 1.128 items, 1.098 betaald, van 83 makers. Sterk geconcentreerd: LeBaronMarket 135, Jahangir Mangrio 96, Biofilmes 80, BrittanyFactory 80, Sisi 3D Forge 76, BBAlley 68.
- GEZIEN: verkoopprijs mediaan $7,25 (40% staat in de aanbieding; mediaan normale prijs $9,50).

**Bereik**
- GEZIEN: ratings zijn heel schaars en zeggen weinig. Betaalde cohortitems: mediaan 0, 234 van 1.098 met 1+, 2 met 5+, max 5. Hele cohort (met gratis): 264 met 1+, 16 met 5+, max 14.
- GEZIEN: zelfs de nieuwe items die in de top 300 bestsellers staan hebben 0 tot 5 ratings. Ratings zijn dus geen maat voor verkoop hier.
- GEZIEN: 55 van de 1.098 betaalde cohortitems (5%) staan in de top 300 van de laatste 3 maanden, van 16 makers. Van de 270 betaalde items van derden in die top 300 zijn er 150 uit 2026. Nieuw werk kan dus bovenkomen.
- Let op (controleur): de top 300 is een rangorde zonder aantallen, telt waarschijnlijk stuks (items van $0,50 staan op plaats 9 tot 11), en het venster bevoordeelt verse items. "In de top 300" betekent "verkoopt relatief vaak", niet "verdient geld".

**Geld**
- GEZIEN (developer.reallusion.com/faq.html): maker krijgt 70% in de Marketplace, 50% in de Content Store. Verkoop via iContent (in de app) gaat voor 30% van de prijs; een maker meldt $25 → $7,50 → $5,25 voor hem (discussions.reallusion.com/t/icontent-severely-undervalues-creator-work/14502).
- GEZIEN: 100 DA Points = $1 (reallusion.com/da-points). Een gewone maker krijgt alleen DA Points; echt geld pas als Certified Content Developer, na meer dan 10.000 verdiende punten ($100) en goedkeuring. Uitbetaling maandelijks naar de bank met W-8-formulier (forum.reallusion.com/PrintTopic554254.aspx).
- Niet gevonden: bedragen van kleine makers, of "Reallusion betaalde $X uit". Makers klagen over iContent zonder cijfers.
- GOK: met ±$7 per item, 70% en de bestsellers van 16 makers is een top-maker hier misschien enkele honderden tot enkele duizenden dollars per maand waard, maar dat is niet te bewijzen.

**Plugins (wat bij ons past)**
- GEZIEN: 61 Python-plugins voor iClone in totaal, 46 van derden, 31 betaald, mediaanprijs $10, 22 makers. Uit 2026 maar 10, waarvan 5 van één maker (RM3D). Ratings 0 tot 6.
- GEZIEN (wiki.reallusion.com): derden mogen plugins verkopen en zelf de prijs zetten, met proefversie.
- DERDEN: gebruikersaantal van iClone en CC nergens openbaar. CC5 uit sinds aug 2025, abonnementen sinds jan 2026 (iClone $199 per jaar, CC $99 per jaar), gratis iClone Personal.

**AI-regels**
- GEZIEN (FAQ): AI-content mag, maar moet op de productpagina gemeld worden; hoofdbeelden moeten echte renders zijn. Geen regel over AI-code.

## Voor en tegen
Voor:
- Levende winkel, nieuwe makers komen in de bestsellers, 70% voor de maker.
- Pluginmarkt bijna leeg: weinig concurrentie voor een goede iClone-tool.
- AI mag openlijk.

Tegen:
- Verkoop onzichtbaar; geld van kleine makers niet aangetoond.
- Echt geld pas na certificering; iContent drukt prijzen.
- Het geld zit in 3D-content (personages, kleding), niet in software. Pluginmarkt is te klein om groot te worden (61 stuks in 7 jaar).
- Gebruikersgroep onbekend en waarschijnlijk klein naast Blender en Unreal.

## Wat we zouden bouwen (als het ooit ja wordt)
Een iClone/CC-plugin die Blender en iClone verbindt (bijvoorbeeld een betere GLB- of Blender-import met materialen), te verkopen voor $10 tot $15. Past bij het werk van Bram aan Blender. Maar gezien de markt van 61 plugins verwacht ik hooguit tientallen verkopen.

## Wat het oordeel kan veranderen
- Reallusion maakt aankoopaantallen openbaar (het veld PurchasedTimes bestaat al).
- Een kleine pluginmaker deelt bedragen boven $300 per maand.
- Herhaalmeting: script over 4 weken opnieuw; kijk of de pluginlijst groeit.
