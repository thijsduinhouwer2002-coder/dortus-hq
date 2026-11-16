# Wijzerplaat "Ebb Tide" (Mila, 16 nov 2026, concept 1)
Opdracht hoofdchat 16 nov 09:55 NL: twee betaalde wijzerplaten; dit is de tweede, met de zee en de dieren van Ebb (reclame voor Ebb). De concurrentiecheck doet Gijs eerst; dit is alleen de look, zodat hij weet waar hij naartoe bouwt. Verander gerust wat de check zegt.

**Haak 1, je stappen zijn het tij.** De wijzerplaat is de patrijspoort van Ebb. Het water stijgt met je stappen (nooit lager dan 30%, zodat er altijd iets zwemt); bij je stapdoel is het vloed. Geen balkje: je ziet de zee volstromen.
**Haak 2, wie zwemt er nu?** Elk uur zwemt er een ander dier uit Ebb door het water (24 van de 25, onderaan staat "14:00 · SWORDFISH"). De walvis komt alleen bij vloed, en blaast dan een fontein. Iets om over te vertellen ("om drie uur zag ik de octopus"), en een reden om je doel te halen. Precies de dieren uit de app, dus eerlijk en herkenbaar.

- `concept-454-ochtend-middag-vloed-aod.png`: Venu 3 (454): ochtend (2.140 stappen, kogelvis), middag (6.480, zwaardvis), vloed (10.412, walvis met fontein), AOD (zwart, tijd grijs, alleen het silhouet van het dier met blauwe rand, weinig pixels aan).
- `concept-260-middag-vloed.png`: FR255 (260) op 1x. GEZIEN met Read: tijd, stappen en het dier lezen ook op 260.
- Gemaakt met `maak_concept.py`, dieren uitgesneden uit `../dieren83/alle25-454.png` (in het echt tekent Gijs ze uit de punten in `../ebb-dieren-v83-data.json`, zoals in Ebb: geen plaatjes, weinig geheugen). Letter Barlow Condensed SemiBold zoals Ebb. Kleuren uit het MIP-palet (00FFFF, 00AAFF, 0055AA, 000055, koraal FF5555), dus het werkt ook op MIP zonder verloop.
- Indeling: datum koraal bovenaan, tijd groot, stappen cyaan eronder, hartslag (getekend hartje, de letter kent er geen) links en batterij rechts op dezelfde hoogte, dier in het water, onderregel "uur · DIER" of "HIGH TIDE · WHALE".
- GEZIEN met Read op 454 en 260. Werkt: het is meteen Ebb (zelfde patrijspoort, golf en dieren), de walvis bij vloed is de beloning. Zwak: bij vloed staat de tijd in het water, met de donkere rand leest hij nog; de fontein raakt de stappenregel net. Bij een kleine stand (ochtend) is de lucht een groot leeg nachtblauw vlak; een paar sterren of de maanstand uit `../werelden14/` kan daar.
- Nog niet: naast de toppers in de winkel gelegd (eerst Gijs' check, dan weet ik welke toppers), MIP-proef op 260 en 280 in de simulator.

## Concept 2 "Ebb Porthole" (16 nov ±11:10 UTC, Daans moets van 11:00)
`maak_concept2.py` geeft `concept2-454-ochtend-middag-vloed-aod.png` en `concept2-260-middag-vloed.png`. GEZIEN met Read op 454 en op 260 (1x).
- **Geen "tide" meer:** onderregel bij je doel is `FULL SEA · WHALE`. Naam: Ebb Porthole.
- **Koperen patrijspoort:** ring van 3,5% van de breedte in twee effen tinten (AA5500 en FFAA55 als lichtboog linksboven) met een donkere binnenlijn (550000) en zes boutjes op 30, 90, 150, 210, 270 en 330 graden. Alleen MIP-kleuren, dus op MIP hetzelfde. In de slaapstand dezelfde ring maar heel donker.
- **Golf nooit door de cijfers:** het water loopt van 70% (0 stappen) tot 43% (doel) van de hoogte; bij vloed staat de golf net onder de tijd, de stappen staan dan in het water met hun donkere rand.
- **Sterren en maan:** zes kleine gele kruisjes op vaste plekken, alleen boven het water; een maansikkel rechtsboven zolang het water laag staat. De lege lucht van concept 1 is weg, en hoe meer je loopt, hoe minder lucht: de zee stroomt de sterren in.
- Fontein van de walvis lager, raakt de stappenregel niet meer.
- Op 260 lezen tijd, ring, dier en onderregel. Werkt: het is meteen een patrijspoort en dus Ebb; tussen de strakke zwarte toppers is het de enige met een rand en een dier.
