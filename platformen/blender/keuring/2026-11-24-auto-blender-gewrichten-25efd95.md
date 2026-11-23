# Keuring blender-gewrichten (verlies en eerlijke cijfers), 24-11-2026, automatische keurder
Wat ik keurde: commit 25efd957b (e2e/meet_tabel.py en proeven/betrouwbaar-rig-2026-11-23/uitslag.md)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | "4.2 gaat van 28 naar 44 van 51" klopt met de tabellen. Nulstand 4.2: 4+4+6+3+5+6 = 28 (armen volgt uit het totaal). Tak 4.2: 51 met robot-fijn (7) is 44 zonder. | Feit (uit de tekst gerekend) | Hoog | Het armen-cijfer van de nulstand staat in een deel van de tabel dat ik niet zie. |
| 2 | De regel "nergens slechter dan de nulstand" klopt niet. In 5.2.3 robot-b en 5.3.0 robot-a is de tak 0,3% tegen 0,0% in de nulstand. Het is klein en ver onder 6%, maar de zin is te sterk. | Feit | Hoog | Tabel "Verlies bij kogelsneden", twee cellen. |
| 3 | De toevoeging `--verlies` in `meet_tabel.py` leest `verloren_diag` uit de pogingen en telt per cel het maximum en het aantal boven 6%. Dat past bij de tabel. De logica is te volgen. Of de json-bestanden dat veld echt hebben, kan ik niet zien. | Vermoeden | Midden | Het script draaien op een run-map. De uitvoer moet de tabel in de uitslag opleveren. |
| 4 | Het bericht noemt "berichten en releasenote", maar die staan niet in de meegestuurde bestanden. De changelog die ik zie heeft geen regel over dit vangnet of over 4.2. | Feit | Hoog | De bestanden of het bericht zelf. Ik kan hier niets over zeggen. |
| 5 | De add-on-wijziging (`rig.py` met `VERLOREN_MAX` 0,06) en de toets `CJ_HERKANS=3` zitten in 1945f46 en niet in deze diff. De uitslag noemt de 4.2-toets "zie het bericht", dus daar is geen bewijs te lezen. | Vermoeden | Laag | De log van run 45282711505 voor 4.2. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test is aangepast om te slagen. Er verandert alleen een meetscript en documentatie. Bestanden blijven ruim onder 400 regels. | Feit | Hoog | Tests en bestandsgrootte |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 3 | Een deel van de nieuwe cijfers heeft geen label. De verlies-tabel en "28 naar 44" missen GEZIEN, terwijl andere regels het wel hebben. De tellingen 194 van 567 en 85 naar 93 hebben het ook niet. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | De cijfers lijken niet goed bij elkaar te passen. "93 keer werd een mislukte vereniging een voxelvorm" staat naast "125 in 4.2, 37 en 35" voxelvormen bij kogelsneden. Dat gaat over verschillende tellingen, maar de uitleg ontbreekt. | Vermoeden | Midden | De ruwe json uitgesplitst per versie en per nulstand of tak |
| 5 | In 4.2 had in run 45279729768 mens-3 één slechte linkerschoudersnede. Een paar regels verder staat "0 slechte sneden" voor de tak. Dat kan kloppen voor de twee genoemde runs, maar de zin noemt ze niet. | Feit | Midden | Eerlijke cijfers: noem bij elke bewering de runs |
| 6 | De tekst "use a newer Blender such as 5.2" houdt zich aan de regel dat 4.5 niet gemeten is. De uitslag zegt dat ook zo. | Feit | Hoog | Alleen beweren wat gemeten is |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze wijziging. Ik kan geen oordeel geven over plezier of beeld. | n.v.t. | n.v.t. |
| 2 | Op 4.2 zijn lichte figuren 2 tot 3,6 keer trager geworden (rigify 64 naar 230 s). Een koper merkt dat. | Zet de wachttijd of een voortgangsregel in het paneel, of raad 5.x aan in de releasenote. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Pas "nergens slechter dan de nulstand" aan naar wat de tabel laat zien: grootste verlies op de tak 0,9%, in de nulstand 5,0%, nergens boven 6%.
- Zet GEZIEN of GOK bij de nieuwe cijfers en noem bij "0 slechte sneden" de runs 45273407326 en 45275271607.
- Leg het verschil uit tussen 93 mislukte verenigingen en 125, 37 en 35 voxelvormen bij kogelsneden.
- Laat zien dat de 4.2-toets voor `CJ_HERKANS=3` groen is, met het log, in plaats van "zie het bericht".
- Controleer dat het bericht en de releasenote bij deze commit zitten. Ik zag ze niet.

---
Automatische keurder, model `claude-sonnet-5-5`, 23109 tokens in, 6256 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
