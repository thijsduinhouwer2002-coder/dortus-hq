# Ebb: frisse keuring van de zichtbaarheid van de dieren, ronde 1 van run 73 (12 nov 2026, 21:12 UTC)

Keurder: een frisse hulp-agent die de app niet kende. Bladen: `ebb-contrast-run73a-fr255.png` en `ebb-contrast-run73a-fenix8.png` (links oud uit run 72, rechts nieuw), plus de vijftien losse beelden per horloge op ware grootte. Venu 3s niet bekeken. Code: proeftak `claude/garmin-2026-11-12-proef73` d81f6262 (plaatjesrun 43305714283): nachtregel v1.4 voor de held (koele kleuren houden hun kleur) en de zwaardvis met de lichte luchtband.

**Cijfer: 7,5 (was 6). Net geen 8.** Geen dier valt meer weg. FR255: 14 goed (3 krap), 1 zwak. Fenix 8: 12 goed (3 krap), 3 zwak.

| scherm | FR255 | fenix 8 |
|---|---|---|
| dolfijn in dag | GOED, krap (witte buik raakt de golflijn) | GOED, krap (witte rand valt weg in de horizon) |
| dolfijn hold dag | GOED | GOED |
| dolfijn in nacht | GOED | GOED |
| dolfijn hold nacht | GOED | GOED |
| zwaardvis in dag | GOED, krap | ZWAK, licht zeil tegen bleke horizon |
| zwaardvis in nacht | GOED | GOED (zwaard ligt op de waterlijn) |
| zwaardvis hold nacht | GOED | GOED |
| narwal hold dag | GOED | GOED |
| narwal in nacht | GOED | GOED, krap (tand dun bij de waterlijn) |
| narwal hold nacht | GOED, beste nachtbeeld | GOED |
| orka in nacht | ZWAK, leest als grijze haai, rugvin flauw | ZWAK, donkergrijs op donkerblauw |
| orka hold nacht | GOED, krap | ZWAK |
| octopus hold nacht | GOED | GOED |
| reuzeninktvis in nacht | GOED | GOED |
| reuzeninktvis hold nacht | GOED | GOED, krap |

**MOET volgens de keurder:** (1) orka bij nacht op beide horloges: lichte rand rond het lijf en vooral de rugvin, meer wit. (2) Zwaardvis bij inademen overdag op de fenix 8: de lichte band maakt zeil en staart flets.

**KAN:** donker randje onder de witte buik van dolfijn en zwaardvis bij inademen overdag; zwaard en narwaltand bij nacht iets boven de waterlijn; het deel onder water bij inademen in de nacht iets lichter; armen van de reuzeninktvis lichter.

**Slechter dan oud:** niets ernstigs. Op de fenix 8 vielen de witte rand van de dolfijn en het zeil van de zwaardvis bij inademen overdag in het oude beeld beter op. Alle nachtbeelden zijn beter of gelijk.

**Wat ik ermee deed (Gijs):** beide MOET-punten gebouwd op 1411b3b7: de orka krijgt bij nacht een lichtere rand (AAAAFF in plaats van 5555AA), de zwaardvis houdt de lichte band alleen op MIP. Zie de status van run 73 voor de tweede ronde.

## Ronde 2 (21:24 UTC), een tweede frisse keurder, code 1411b3b7 (plaatjesrun 43307595385)

Bladen: `ebb-contrast-run73b-fr255.png` en `ebb-contrast-run73b-fenix8.png`. Deze keurder kende ronde 1 niet en keek ook naar vier beelden van de venu 3s.

**Cijfer: weer 7,5.** Dertien van de vijftien schermen zijn op beide horloges in één blik goed, niets valt weg. Alleen de orka houdt het onder de 8.

- Orka inademen nacht: FR255 ZWAK (het grijze lijf heeft de toon van de waterlijn, alleen de oogvlek is wit, "een grijze vin op een streep"), fenix 8 zwak tot net goed. Orka inhouden nacht: goed maar krap op beide.
- Zwaardvis inademen dag: goed maar krap op beide (fenix 8 weer gelijk aan oud; op de FR255 leunt het lichte zeil op de zwarte rand).
- Alle andere schermen GOED. Venu 3s: geen eigen problemen.

**MOET:** (1) de orka een donkerder lijf met de lichte rand, zodat lijf en waterlijn uit elkaar liggen; (2) de orka herkenbaar als orka: echt wit, en bij inademen een stuk witte buik boven water.

**KAN:** orka groter (op de FR255 ongeveer 60 beeldpunten breed), zwaardvis overdag een tint donkerder, het deel onder water van de reuzeninktvis bij inademen opruimen, losse streepjes van de omtrek bij de waterlijn op de fenix 8 (stond ook in oud).

**Slechter dan oud:** de orka is zijn zwart kwijt (zichtbaar maar grijs); op de FR255 heeft het zeil van de zwaardvis overdag minder verschil met de lichte band.

**Wat ik ermee deed (Gijs):** op 6845a6a7 volgt het donkergrijs van de orka weer de gewone nachtregel (bijna zwart), met de lichte rand AAAAFF en wit dat nu echt wit blijft. De witte buik boven water bij inademen is een wijziging aan de tekening van het dier en is NIET gedaan.

## Ronde 3 (21:35 UTC), een derde frisse keurder, code 6845a6a7 (plaatjesrun 43309527062)

Bladen: `ebb-contrast-run73c-fr255.png` en `ebb-contrast-run73c-fenix8.png`. Venu 3s niet bekeken.

**Cijfer: 7. Slechter dan ronde 2.** De zwarte orka met alleen een lichte rand is "een schetsje, geen dier": bij inademen in de nacht ZWAK op beide horloges, bij inhouden goed maar krap op de FR255 en ZWAK op de fenix 8. Deze keurder vond ook de dolfijn bij inademen overdag op de FR255 ZWAK (lichtblauwe rug tegen de lichte band, alleen de omlijning houdt hem bij elkaar); keurder 1 en 2 noemden hetzelfde beeld GOED. De andere dertien schermen: GOED.

**MOET:** de orka bij nacht een eigen vlak dat afsteekt (donker leigrijs of blauwgrijs, of een rand van 2 tot 3 px en grotere witte delen); de dolfijn overdag op de FR255 een tint donkerdere rug of een minder lichte band.

**Wat ik ermee deed (Gijs):** ronde 3 teruggedraaid. De proeftak staat op 5680d2a7 en is in de app gelijk aan ronde 2 (1411b3b7): grijze orka met lichte rand. Dat is de beste stand tot nu toe: 7,5, geen 8.
