# Ebb: contrast van de 25 dieren tegen het water en de lucht van hun familie (Gijs, run 71, 12 nov 2026)

Opdracht hoofdchat 12 nov 20:15 NL punt 2. Dit is de eerste stap: een berekening uit de kleuren in de code, nog geen meting op echte schermbeelden en nog niets veranderd aan de dieren.

**Wat er gemeten is.** Per dier de lijfkleur (`EbbDierData.TINT`, eerste kleur) tegen zes achtergronden van zijn familie: het water onder water overdag op AMOLED (`KrabV2Basis.WATER`), het raster op MIP overdag (de dichtste van 005555 en 0055AA), de lucht vlak boven de horizon overdag op AMOLED en op MIP (`KrabV2Basis.LUCHT`), het water bij nacht op AMOLED (000069) en zwart bij nacht op MIP. Bij nacht is de lijfkleur eerst door de nachtregel gehaald (`EbbNacht.held`). Het getal is het kleurverschil ΔE (CIE76): 0 is dezelfde kleur, onder 20 valt het dier weg, 20 tot 35 is zwak, daarboven is het duidelijk. Helderheid alleen (de WCAG-verhouding) heb ik ook uitgerekend maar die is hier misleidend: een oranje krab tegen een blauwe lucht haalt maar 1,2 en is toch goed te zien.

**Wat er NIET in zit (eerlijk).** De stickerrand (wit overdag, 5555AA bij nacht), de lichte en donkere vlakken en de ogen van het dier, de kleur van het wateroppervlak boven water, de lucht bij nacht, en waar het dier precies staat. De rand redt overdag een deel, maar een witte rand tegen een lichte lucht helpt weinig. De uitkomst moet dus nog naast de echte beelden gelegd worden.

## Tabel, slechtste dier bovenaan

| nr | dier | familie | lijf | water dag AMOLED | water dag MIP | lucht dag AMOLED | lucht dag MIP | water nacht AMOLED | nacht MIP | laagste |
|---|---|---|---|---|---|---|---|---|---|---|
| 13 | Dolphin | vliegers | 55AAFF | 29 | 34 | 10 | 0 | 41 | 64 | **0** |
| 19 | Orca | koud | 555555 | 25 | 23 | 60 | 65 | 70 | 0 | **0** |
| 14 | Swordfish | vliegers | 5555FF | 69 | 51 | 74 | 65 | 10 | 101 | **10** |
| 20 | Narwhal | koud | 5555AA | 45 | 13 | 75 | 83 | 40 | 60 | **13** |
| 9 | Octopus | huisjes | AA55FF | 66 | 59 | 111 | 108 | 16 | 96 | **16** |
| 21 | Giant squid | koud | AA55FF | 95 | 59 | 108 | 117 | 16 | 96 | **16** |
| 17 | Shark | licht | 55AAAA | 68 | 33 | 60 | 61 | 79 | 39 | **33** |
| 23 | Whale | koud | 55AAFF | 43 | 34 | 49 | 56 | 41 | 64 | **34** |
| 12 | Seal | strand | AAAAAA | 38 | 44 | 45 | 50 | 74 | 36 | **36** |
| 16 | Manta | vliegers | AAAAAA | 49 | 44 | 42 | 50 | 74 | 36 | **36** |
| 0 | Fish | huisjes | FFAA55 | 99 | 88 | 37 | 48 | 100 | 78 | **37** |
| 18 | Sunfish | licht | AAAAFF | 40 | 38 | 89 | 92 | 40 | 65 | **38** |
| 5 | Seahorse | licht | FFAA00 | 132 | 106 | 51 | 56 | 106 | 78 | **51** |
| 3 | Turtle | krab | 00AA55 | 77 | 60 | 100 | 99 | 129 | 90 | **60** |
| 1 | Shrimp | strand | FFAAAA | 69 | 72 | 68 | 70 | 79 | 60 | **60** |
| 11 | Ray | vliegers | AAAA55 | 88 | 62 | 86 | 94 | 115 | 82 | **62** |
| 2 | Jellyfish | licht | FF55AA | 68 | 76 | 98 | 104 | 65 | 72 | **65** |
| 6 | Starfish | strand | FFAA55 | 92 | 88 | 104 | 108 | 100 | 78 | **78** |
| 15 | Sea otter | strand | AA5500 | 89 | 82 | 109 | 111 | 108 | 78 | **78** |
| 24 | Sea cucumber | huisjes | 55FFAA | 112 | 79 | 120 | 130 | 139 | 113 | **79** |
| 4 | Crab | krab | FF5500 | 123 | 117 | 139 | 140 | 96 | 85 | **85** |
| 7 | Clownfish | krab | FF5500 | 123 | 117 | 139 | 140 | 96 | 85 | **85** |
| 22 | Lobster | strand | FF5555 | 101 | 100 | 107 | 107 | 88 | 85 | **85** |
| 8 | Pufferfish | huisjes | FFFF55 | 132 | 106 | 89 | 100 | 151 | 126 | **89** |
| 10 | Eel | huisjes | AAFF55 | 135 | 102 | 113 | 125 | 157 | 127 | **102** |

## Wat eruit komt

- **Dolphin (vliegers): lijf 55AAFF is precies de kleur van de MIP-lucht van zijn familie (55AAFF), verschil 0, en op AMOLED 10.** Dat is wat de hoofdchat zag. Boven water valt hij weg tegen de lucht.
- **Orca (koud): lijf 555555 wordt door de nachtregel op MIP zwart (000000) op zwart water, verschil 0.** Hij leeft dan alleen van zijn witte vlekken en de rand.
- **Swordfish (vliegers): bij nacht op AMOLED verschil 10** met het nachtwater.
- **Narwhal (koud): overdag op MIP verschil 13** met het raster onder water.
- **Octopus (huisjes) en Giant squid (koud): bij nacht op AMOLED verschil 16.**
- Zwak, tussen 20 en 35: Shark en Whale. De andere zeventien zitten op 36 of hoger.

## Voorstel (nog niet gebouwd, eerst naast echte beelden leggen)

1. Dolphin: de familie vliegers een andere luchtband geven helpt drie dieren niet, dus liever de dolfijn zelf een donkere omtrek (zoals de nachtomtrek, maar donkerblauw 000055) of een donkerder lijf (0055AA met lichte buik). Kiezen met Mila.
2. Orca bij nacht op MIP: lijf niet door de nachtregel naar zwart, maar vast 555555 laten (uitzondering in `EbbNacht.held` voor grijs), of de omtrek 5555AA dikker.
3. Swordfish, Octopus en Giant squid bij nacht op AMOLED, Narwhal overdag op MIP: een trede lichter lijf of de lichte omtrek ook overdag.
4. Daarna de zes dieren in een proefronde in beeld brengen (dag en nacht, FR255 en fenix 8) en dezelfde tabel uit de pixels van de echte beelden maken.

De berekening is opnieuw te maken uit de kleuren in `DierenData.mc`, `KrabV2Basis.mc` en `Nacht.mc`.
