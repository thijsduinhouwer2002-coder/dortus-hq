# Werelden v5: eenheidsblad, de vier punten van de hoofdchat (Mila, run 52, 12 nov 04:35 UTC)

Punten uit berichten/mila.md (hoofdchat 12 nov 05:15 NL). Beelden: `werelden5/eenheid-families-in-dag-<260|454>-1x.png` (rijen: strand, vliegers, huisjes, koud, licht) en per dier `werelden5/<dier>-<in|uit|calm>-dag-<454|260>.png`. GEZIEN met Read, allebei.

## Wat er veranderde
1. **Pijlstaartrog:** lager (in op 28 boven de golf, Calm op 26); kleinste gat tot de "12" nu 7,3/260. Grap opnieuw: een echte ufo met glazen koepel, drie gele lampen en een gele lichtbundel. Frisse kijker: "ufo/schoteltje met lichtstraal en gele bollen". Zwak: de rog zelf verdwijnt onder de ufo (kijker: "geen dier gezien").
2. **Reuzeninktvis:** held nu 75 px breed op 260 bij ademen (68 bij hold en menu). Nieuwe grap, slecht verstoppen: achter een piepklein eilandje met één palmboom; onder water achter een klein steentje. Frisse kijker: "inktvis met een eilandje en palmboom ervoor, vrij zeker".
3. **Zeepaardje:** de paal stopt onder zijn staartkrul en kruist "round 2 · 18 left" niet meer.
4. **Eigen lucht per familie** (`bron/werelden_v5_lucht.py`, geen nieuw tekenwerk per dier), alleen overdag op de ademschermen:

| familie | MIP boven | MIP band | AMOLED drie stappen (knik) | luchtdetail |
|---|---|---|---|---|
| krab, schildpad, clownvis | 0055AA | 00AAFF | 001E5F, 004BA5, 00A5FA (0,55) | zon, wolk |
| strand | 0055FF | 55AAFF | 002878, 0050D2, 5AB4FF (0,66) | zon en een zeilbootje op de horizon (x 60) |
| vliegers | 0055AA | 55AAFF | 00235A, 0055AA, 6EB9FF (0,55) | zon en twee witte windkrullen links laag |
| huisjes | 5500AA | FF5555 | 28005A, 6414A0, FF6E5A (0,55) | avond: grote oranje zon half in zee (x 46) |
| koud | 0055AA | AAFFFF | 002864, 0055A0, BEF5FF (0,74) | bleke kleine zon en zes sneeuwvlokjes aan de randen |
| licht | 0000AA | FFAAFF | 0A0050, 2814AA, FFAAE6 (0,55) | zon met acht gele stralen |

MIP: band begint 28/260 boven de horizon, zoals nu. AMOLED: verloop van stap 1 naar 2 tot knik × horizon, dan naar 3.
Contrast (`bron/meet_v5_lucht.py`, slechtste luchtpixel rond elke tekstregel tegen wit, alle 22 dieren, in, uit, Calm, 454 en 260): **laagste 4,88, 0 te laag.** De eerste versie had 34 te lage regels (windkrul door "breathe out", te lichte koude en strandlucht op AMOLED); opgelost door de krullen te verplaatsen en de knik lager te leggen.

## Grap-toets ronde 2 (frisse kijker, alleen 260)
Zonnebril maanvis: "grote zwarte zonnebril, bril zeker" (dier: twijfel). Kwal: "roze kwal onder een regenwolk met gele paraplu, zeker". Inktvis: eilandje en palmboom, vrij zeker. Rog: ufo gezien, dier niet. Alle vier tellen nu als grap.

## Open (volgende run)
- Strand (Today en 8 weeks) afmaken en de onderwaterachtergrond voor startscherm, pauze en sea log.
- Rog: iets van de rog laten zien onder de koepel (vinpunten breder dan de schotel).
- Nachtregel (`ebb-nachtregel-v1.json`) geldt ook voor deze luchten: ze gaan bij nacht naar de bestaande nachtlucht en dan door de regel.
