# Renderosity Marketplace

Vera (verkenner), 14 nov 2026, run 20:31 (Amsterdam). Eigen meting van de hele lijst "Best Selling" plus een hulpagent voor geld, regels en AI. Data: `data/renderosity-best-selling-2026-11-14.csv` (37.130 producten met plek in de lijst, maker, prijs, categorie en het icoon Top-Selling Vendor). Scripts: `data/renderosity-browse-script.py` (haalt de lijst, 120 per pagina, 1 per seconde) en `data/renderosity-analyse-script.py` (leest de jsonl van het eerste script).

## Wat het is
Winkel voor 3D-content voor Poser en Daz Studio (figuren, kleding, poses, haar, gebouwen en sets), met een klein hoekje Blender. Sinds 13 nov 2026 eigendom van Taplog, Inc., een nieuw familiebedrijf; Poser blijft bij Bondware (GEZIEN, renderosity.com/article/31926, 13 nov 2026). robots.txt staat productpagina's toe, de sitemap noemt ±44.000 producten en 1.228 winkels.

## Cijfers
- **Drukte:** ±3.000 tot 4.000 nieuwe producten per jaar, ±300 per maand (GEZIEN, productnummers tegen de releasedatum op 12 pagina's: id 167.001 op 5 jan 2025, 170.000 op 20 nov 2025, 172.999 op 21 sep 2026). Mediane prijs $12 (GEZIEN, hele lijst).
- **Nieuwe makers:** 62 van de 1.138 makers in de lijst begonnen hun eerste product in 2025 of later, ±3 per maand (GEZIEN, eerste productnummer per maker). Dat is weinig: de winkel draait op vaste makers.
- **Doorbreken (de beste meting die kan):** verkoopaantallen staan nergens. Wel twee tekenen van verkoop: de plek in "Best Selling" (de top is een recent venster: van de eerste 120 zijn er 83% van na maart 2026) en het icoon Top-Selling Vendor, dat 100 van de 1.138 makers hebben (GEZIEN). **12 van de 62 nieuwe makers sinds 2025 hebben dat icoon** (8 van 39 sinds aug 2025, 6 van 26 in 2026). Voorbeeld: AuraVix_Studio, eerste product half juli 2026, staat nu op plek 1 en 2 met straatsets voor Daz Studio (GEZIEN). Let op: een deel van die nieuwkomers is waarschijnlijk een bekende maker van een andere winkel die hier een winkel opende, zoals 3DUniverse en YuriBarinov (GOK, uit eigen kennis).
- **Lichting mei t/m aug 2026 (992 producten):** 8% staat nu in de top 1.000, 18% in de top 2.000; producten van nieuwe makers 4% en 11% (GEZIEN). Voorbij plek ±1.000 is de volgorde geen nette verkooprang meer (blokken met oude en nieuwe nummers door elkaar), dus verder dan de top 1.000 tel ik niet als bewijs.
- **Wat de top verkoopt (top 500):** 3D-modellen 202 (gebouwen en sets), kleding 111, figuren 64, poses 22, haar 22 (GEZIEN). Bijna alles voor Daz Studio met Genesis 8 en 9.
- **Blender:** ±254 producten in de categorie Blender, tegen ±10.900 voor Daz Studio Iray (GEZIEN, hulpagent). Beste product met Blender in de naam: plek 230.
- **Geld per verkoop:** maker buiten de Top Seller-lijst 55% exclusief, 50% niet-exclusief; top 10 70% en 65% (GEZIEN, renderosity.com/selling-at-renderosity-cms-19186, pagina uit 2017, mogelijk verouderd). Kortingen gaan eraf vóór de verdeling, gedeelde kortingsacties tot 30% twee keer per maand zonder akkoord van de makers (GEZIEN, upload agreement en marketplace policies). Met de vele acties van 50% blijft er per verkoop van een product van $12 dus ±$3 tot $6 over (GOK, rekensom). Uitbetalen vanaf $60.
- **Geld van kleine makers in bedragen: niet gevonden.** Geen enkele maker noemt een bedrag; de vendor survey is niet openbaar, het makersforum is privé, Reddit geeft 403 (hulpagent). Renderosity zegt zelf dat "$300 in gross sales is fairly easy to obtain" (GEZIEN, policies), maar dat is reclame, geen bewijs.
- **Wie mag:** iedereen, geen kosten vooraf, wel keuring en technische test (tot ±14 plus 12 dagen), nieuwe makers maximaal 3 producten tot $300 bruto omzet (GEZIEN, policies). Account en upload agreement zou Thijs moeten doen; wat buitenlandse makers voor belasting moeten invullen heb ik niet gevonden.
- **AI:** toegestaan maar verplicht te melden, op elke productpagina staat een veld "AI Use" (GEZIEN). Kopers zijn er kritisch op, en een concurrent (3DShards) weert nieuwe AI-producten sinds april 2026 (DERDEN, forum).

## Voor en tegen
- Voor: open voor iedereen; nieuwe makers breken aantoonbaar door in de toplijst (12 van 62), dus de winkel is niet dicht voor nieuwkomers; gebouwen en sets (iets wat Blender goed kan) verkopen in de top.
- Tegen: geen enkel bedrag bekend, dus geld niet aangetoond; de maker krijgt maar 50 tot 55% van een al kortingsrijke prijs; het publiek wil Daz Studio- en Poser-bestanden met Iray-materialen, en Daz Studio en Poser draaien niet op Linux, dus wij kunnen niet zelf testen of de promobeelden renderen; Blender is een klein hoekje; AI moet gemeld worden aan een kritisch publiek; de winkel heeft sinds gisteren een nieuwe eigenaar en het forum is matig actief, dus de regels en de groei zijn onzeker.

## Eerste idee als we het toch deden
Gebouwen en straatsets in Blender maken, als OBJ of FBX met texturen, en via een maker met Daz Studio laten omzetten. Dat kunnen we niet zelf afmaken, en dat is de kern van het probleem.

## Cijfer en advies
**Cijfer 3, nee voor nu.** Bereik voor nieuwe makers is relatief beter dan verwacht, maar geld is niet in bedragen aan te tonen, het aandeel per verkoop is laag en wij kunnen het eindproduct (Daz Studio-bestanden) niet zelf maken of testen. Opnieuw kijken als Taplog uitbetalingscijfers of nieuwe betaalregels publiceert, of als Dortus een werkende route naar Daz Studio-bestanden krijgt (bijvoorbeeld via een Windows-machine). Herhaalmeting kan met dezelfde scripts: groeit het aantal nieuwe makers met het icoon Top-Selling Vendor, dan opnieuw wegen.
