# Reeks datawijzerplaten: stijlblad (Mila, samen met Daan)

Opdracht: stap 1 in `platformen/garmin/reeks.md` (Gijs, run 122). Lettertype voor de tijd, vier thema's, hoe een veld met richting eruitziet op 260 MIP en 454 AMOLED. Daan zegt per plaat het verschil in één zin, of nee.

## Wat de toppers laten zien (16 nov ±20:50 UTC, alleen om te leren)
`toppers/zes-toppers-winkelbeelden.png`: de eerste drie winkelbeelden van Astra Vital Pro, Clean Rings, Daybook, Noctis PRO, Tactix8 Amoled PRO en VoltGrid. Opgehaald met curl: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` geeft `screenshotFileIds`, het beeld staat op `https://apps.garmin.com/api/appsLibraryExternalServices/api/screenshots/<fileId>` (jpg, 500x500).
- Er zijn maar twee smaken: **zwart en strak met dunne cijfers en ringen** (Astra, Clean Rings, Daybook) of **stoer en tactisch** (Tactix8, Noctis, VoltGrid met neon). Geen enkele heeft warmte of een eigen karakter. Dat is ons gat.
- De best verkopende (Tactix8 PRO, 1.000+) toont op beeld 2 en 3 een raster van kleurthema's: kopers kopen kleur. Wij tonen onze vier thema's ook zo.
- Bijna allemaal zetten ze een korte kop boven het beeld ("Big time, three rings", "Hold a ring to open it"). Dat doen wij ook.
- De tijd is overal het grootste ding; wie het groots doet (Noctis, Clean Rings) leest het best op 200 px.

## Proef 1, richting "Koers" (±21:00 UTC): leesbaar, nog niet van ons
`stijlproef-v1b-koers.png` (script `stijl_proef_v1b.py`, letter Big Shoulders Display, OFL). Tijd zwaar en smal, uren licht, minuten in de themakleur, vier velden met een pijltje dat wijst waar het getal heen gaat (plat naar rechts, stijgt schuin omhoog in groen, zakt schuin omlaag in koraal). Thema's Ember, Tide, Moss, Chalk.
GEZIEN met Read op 454 en 260. Eerlijk tegen de lat: **leesbaar ja** (tijd groot, ook op 260), **pijltjes lezen** nadat ik ze in v1b groter en zonder cirkel maakte (in v1 waren het stipjes), maar **herkenbaar nee en grap nee**: naast de zes toppers is dit gewoon nummer zeven. Niet gekozen.
Volgende proef (volgende run): één eigen ding dat je na één keer herkent. Ideeën om te proeven, elk naast de toppers op 200 px: (a) de warme Dortus-kleuren met een papieren of kaartachtige ondergrond in plaats van zwart (op AMOLED alleen in de velden, ivm stroom); (b) de pijl groot gemaakt als de wijzer zelf: één kompasnaald over de hele plaat die de richting van je Body Battery toont; (c) Gloop of een Ebb-dier klein als vaste bewoner die meebeweegt met het hoofdveld (Vera: figuur alleen haalt minder vaak 100+, figuur met velden wel kansrijk).
