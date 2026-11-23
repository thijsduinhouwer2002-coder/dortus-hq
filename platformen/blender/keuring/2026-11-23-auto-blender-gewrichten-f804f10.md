# Keuring blender-gewrichten testset 4.2, 23-11-2026 22:06 NL, automatische keurder
Wat ik keurde: commits 7ea796e..f804f10 (f804f10f1): `architectuur.md`, `e2e/meet_drempel.json`, `proeven/betrouwbaar-rig-2026-11-23/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging raakt geen add-on-code. Er verandert alleen een testdrempel en wat daarover is opgeschreven. Getoetst aan de commit-boodschap en de eisen over betrouwbaarheid in `ontwerp.md`.
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De nieuwe 4.2-ondergrenzen (robot-a 7, robot-b 7, kleding 8) komen overeen met de eindmeting in de tabel. De andere figuren houden "alle" (9, rigify 7, armen 8) en halen dat in 4.2 ook (9, 9, 7, 8). | Feit (uit de tekst van de diff) | hoog | Niets nodig. |
| 2 | De tabellen kloppen intern. De totalen 55, 60 en 60 van 60 zijn goed opgeteld. De aantallen gewrichten zijn gelijk aan de vorige meting (da1c134), zoals de tekst zegt. | Feit | hoog | Niets nodig. |
| 3 | Of `meet_eis.py` de sleutel `"4.2"` echt leest en matcht met versienamen als `4.2.23`, is niet te zien. Dat bestand zit niet in de wijziging. Leest het de sleutel niet, dan blijft 4.2 rood of de drempel doet niets. | Vermoeden | midden | Een groene run van `betrouwbaar-rig.yml` voor 4.2.23 op deze commit, en bij een kunstmatig lagere meting weer rood. |
| 4 | De claim dat `DIEP_EXACT=True` met het schone omhulsel geen gewricht extra gaf (run 45261862637) en de "keuze run 28" zijn niet na te lopen in deze wijziging. | Vermoeden | midden | Het log van die run, of de uitslag in de map `proeven/`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De drempel voor 4.2 gaat omlaag naar de gemeten stand. Dat lijkt op "test aangepast om te slagen", maar het is open en beperkt. Het geldt alleen voor 4.2 en drie figuren, het doel blijft 9, en het staat in `uitleg` en in `uitslag.md`. | Feit | hoog | Tests niet aangepast om te slagen (zie Kan 1) |
| 2 | Het commitbericht noemt "keurder moet 1" als reden. Dat is een eerlijke koppeling met een eerdere keuring, geen verstopte aanpassing. | Feit | midden | Idem |
| 3 | `architectuur.md` is bijgewerkt voor `scharnier.DIEP_EXACT`, in dezelfde commit als het besluit. | Feit | hoog | architectuur.md bijgewerkt |
| 4 | De regellengte van `architectuur.md` (±400) is niet te beoordelen. De wijziging beslaat één regel en het bestand is afgekapt. De regels zijn al heel lang. | Vermoeden | laag | `wc -l` op het bestand. |
| 5 | Persoonsgegevens, sleutels of wachtwoorden zie ik niet in de wijziging. | Feit | hoog | Persoonsgegevens |
| 6 | Cijfers zoals "geen gewricht erbij" en "26 van x" hebben geen label GEZIEN, DERDEN of GOK. De meettabellen zijn wel eigen metingen met runnummer. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen in deze wijziging. Dit is wat een koper op 4.2 ervan zou merken, afgeleid uit de uitslagtabel.
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Op 4.2 slaat Figure from rig op de robot twee knieën over, en op het aangeklede figuur één knie. Een koper op 4.2 krijgt dus minder dan op 5.2. | Op de winkelpagina en in het paneel eerlijk zeggen dat 4.2 minder betrouwbaar is, en 4.5 of nieuwer aanraden. | klein |
| 2 | De zin met wat de koper kan doen staat al in de lijst "Skipped". | Controleer als speler of de zin zichtbaar en duidelijk is (kijken op een schermafbeelding). | klein |
| 3 | De kale mens duurt nu ±50 s tegen 14 s eerder. | Een grovere voxel op kleine figuren, zoals `uitslag.md` zelf voorstelt. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Zet bij `meet_drempel.json` een vervaldatum of verwijzing naar het spoor voor een betere 4.2-snede, zodat de lagere ondergrens niet blijft staan.
2. Bevestig dat `meet_eis.py` de sleutel `"4.2"` leest (Deel A 3), met een groene run op deze commit.
3. Geef de claims over `DIEP_EXACT` en "keuze run 28" een label (GEZIEN of GOK) en een link naar het log.
4. Controleer de regellengte van `architectuur.md`. Splitsen ligt voor de hand als het bestand ver boven ±400 regels zit.
5. Een drempel precies op de gemeten waarde kan wiebelen als een runner anders uitpakt. Overweeg een tweede run voordat hij als vast geldt.

---
Automatische keurder, model `claude-sonnet-5-5`, 23858 tokens in, 4263 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
