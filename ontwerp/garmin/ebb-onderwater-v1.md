# Ebb: onderwaterachtergrond voor startscherm, pauze en sea log (Mila, run 53, 12 nov 04:40 UTC)

Opdracht hoofdchat (berichten/mila.md, 05:15 NL). Script `bron/onderwater_v1.py`, beelden `onderwater1/` (overzicht 260 2x en 454 1x, dag en nacht, losse schermen). Meting `bron/meet_onderwater_v1.py`: **elke tekstregel 4,5 of hoger (laagste 5,43)**, 260 en 454, dag en nacht. GEZIEN met Read: beide overzichten.

## Het thuiswater (geldt voor alle drie)
Zelfde water en oppervlak als hold (`werelden_v21.water_onder`, raster tot y 146 op MIP), **zonder lichtbundel** (achter menu en tekst haalde geel daar maar 4,27), met:
- Twee verre ruggen: (30, y+4) 70 × 22 en (230, y) 64 × 26, kleur zoals de verre ruggen van hold (MIP `mip_verder`, AMOLED gemiddelde van `ver` en `zee_top`).
- Zandrand FFFFAA vanaf y + 10 (golf 2 hoog, 2 golven) met een witte lijn van 1,2; twee kiezels AAAA55 met witte rand op (96, y+22) en (168, y+20). Bij nacht zand AAAA55 als basis.
- Kelp links (x 32) en rechts (x 230): drie sprieten van 46, 34 en 28 hoog, 4 dik, 00AA55, met een bolletje 55FFAA bovenop, licht slingerend.
- y = 214 (start), 226 (pauze), 222 (sea log).
- Overdag de stofjes van hold; bij pauze in plaats daarvan vier belletjes stil op één rij op y 150: **het water staat stil**, "the sea waits".
- Nacht: de nachtregel (`ebb-nachtregel-v1.json` v1.1).

## Startscherm (eerste keer, of nog geen wereld)
Menu zoals in de werelden ("Ebb" geel 25 op 16, pillen op 52 en 86, gekozen pil met witte rand 3,2, de andere 00AAFF 2; menuregel geel 16 op 120). Het eigen dier maat 30 onderin midden op (130, 196), met twee belletjes erboven. Haak: je zee is er al, je vriend wacht.

## Pauze (blad v10 op het thuiswater)
"paused" 00FFFF 26 op 16, "round 2 · 1:12" wit 17 op 46. Resume, Save, Discard (24) op y 98, 134, 170; gekozen regel in een pil 00FFFF (110 × 32, rond) met tekst 000055; **het eigen dier (maat 18) wijst aan**, midden op x 58 naast de pil, schuift mee. "the sea waits" 00FFFF 15 op 204.

## Sea log
"sea log" geel 24 op 16, "8 of 24" wit 16 op 42. Twee rijen van drie belletjes: midden (76 + kolom × 54, 92 + rij × 58), straal 23, rand 00AAFF 1,6 (gekozen: wit 2,6), vlak 000055 (AMOLED 001E3C), glimpje wit. Gevonden: het dier maat 23; nog niet gevonden: de schaduw (`horloge_sim.silhouet`). Naam van de gekozen vriend wit 18 op 182 (nog niet gevonden: "?"). Paginastipjes op y 210, x 112 + k × 12.

## Voor Gijs
Bouwen na de krabpunten, het eenheidsblad en strand v2. Geen plaatjes nodig behalve de dieren; kelp en ruggen zijn een paar veelhoeken.

## v1.1 na de frisse keuringen (run 53)
- Startscherm: de grap: je vriend blaast twee belletjes en de bovenste is een roze hartje (FF55AA met witte rand, op (166, 150)): hij wacht op je.
- Nacht: zand basis 5555AA (koel, dan de nachtregel), geel gedimd naar AAAA55 ("Ebb", menuregel, "sea log"), "paused" en "the sea waits" 55AAFF, de gekozen pauzeregel een pil 0055AA met rand 55AAFF en witte tekst.
- Meting: laagste 5,43, 0 te laag.
