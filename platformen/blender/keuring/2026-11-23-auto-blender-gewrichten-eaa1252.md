# Keuring blender-gewrichten, uitslag betrouwbaar-rig (eindmeting), 23-11-2026, automatische keurder
Wat ik keurde: commit eaa12520e (6dc00b2..eaa1252), alleen `producten/blender-gewrichten/proeven/betrouwbaar-rig-2026-11-23/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging is alleen een meetverslag, geen code. De add-on en de gratis zip veranderen niet. Ik toets of het verslag klopt met zichzelf en met de opdracht (betrouwbaar gewrichten plaatsen in Pro).

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De kolomsommen kloppen met de tabel: 5.2.3 en 5.3.0 geven 60 van 60, 4.2.23 geeft 55 van 60. | Feit | Hoog | Alleen narekenen in de tabel. |
| 2 | De kolom 4.2.23 komt uit een eerdere commit (7ea796e), want de 4.2-jobs voor robot en rigify werden afgebroken. Het verslag zegt dit open. | Feit | Hoog | Een nieuwe run van 4.2 op 6dc00b2 voor robot en rigify. |
| 3 | De stelling dat de 4.2-weg (Exact) in beide commits gelijk is, kan ik niet uit deze diff halen. Alleen kleding, mens en armen gaven hetzelfde aantal. | Vermoeden | Midden | `git diff 7ea796e 6dc00b2` op de add-on met alleen de 5.x-paden veranderd, of een groene 4.2-run. |
| 4 | De claim "nul slechte sneden in 5.x" (was 16 per versie) staat in de tabel (tweede getal 0 in beide kolommen). De 19 voxelvormen en de gelijke uitkomst op AMD en Intel kan ik niet zien. | Deels feit, deels vermoeden | Midden | De logs van run 45267268513 en de eerdere runs. |
| 5 | De eerlijke open punten staan erin: 4.2 haalt 55 van 60, de rechterknie van de Meshy knight zit op de grens (5,3 tot 5,6% tegen vangnet 6%), 4.2 is traag. | Feit | Hoog | De rest is niet te zien zonder de runs. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests of code aangepast, alleen een markdownbestand. | Feit | Hoog | Tests niet aangepast om te slagen: ok |
| 2 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want er is geen code gewijzigd. | Feit | Hoog | architectuur.md bijgewerkt: niet van toepassing |
| 3 | De nieuwe tijden en aantallen hebben een runnummer, maar geen label GEZIEN, DERDEN of GOK. Alleen de eerdere bijstelling heeft "GEZIEN". | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK: klein gebrek |
| 4 | De commitboodschap noemt berichten aan de hoofdchat en Bram. Die staan niet in de meegestuurde bestanden. | Feit | Hoog | Alleen te melden, geen regel geraakt |
| 5 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens: ok |
| 6 | De Meshy knight wordt gebruikt in de gewone e2e met een licentie die "niet zelf nagelezen" is. Hij zit niet in de testset en niets ervan gaat naar Steam of een winkelplaatje. | Feit | Midden | Eigen materiaal of CC0 voor testfiguren (ontwerp): risico, zie Kan |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen in deze wijziging. Wat volgt is uit de tekst afgeleid.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | In Blender 4.2 kost een figuur 2 tot 5 minuten en haalt Pro 55 van 60 gewrichten. Een koper op 4.2 voelt dat als traag en soms als mislukt. | Een voortgangsmelding en bij een overgeslagen gewricht de zin die al in `redenen.py` zit (vooral het advies om 4.5 of nieuwer te gebruiken). Vermoeden: dat die zin zichtbaar genoeg is, dat moet iemand in het paneel zien. | Klein |
| 2 | Robot-fijn in 5.2.3 duurde 244 s tegen 171 s in de vorige meting. Het verslag zegt er niets over. | Kijken of dat ruis van de runner is of een echte vertraging. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij de nieuwe cijfers GEZIEN of GOK (regel cijfers).
- Bevestig de 4.2-kolom met een nieuwe run op 6dc00b2 voor robot en rigify, of laat zien met `git diff` dat de 4.2-weg gelijk is gebleven (A3).
- Controleer de licentie van de Meshy knight, of haal hem uit de gewone e2e.
- Zeg in het verslag waarom robot-fijn in 5.2.3 trager werd (C2).
- De regel "Keuring: nog niet gedaan" is verouderd nu deze keuring er is. Werk hem bij.

---
Automatische keurder, model `claude-sonnet-5-5`, 20537 tokens in, 3828 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
