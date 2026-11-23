# Keuring betrouwbaarheid Figure from rig (63f4c6e..7ea796e), 23-11-2026, automatische keurder
Wat ik keurde: commit 7ea796ef4 (scharnier.py, e2e/meet_diag.py, e2e/meet_drempel.json, proeven/betrouwbaar-rig-2026-11-23/uitslag.md)
Akkoord: nee

## Deel A: doet het wat beloofd is?
Getoetst aan de opdracht in de uitslag: elk haalbaar gewricht op een vaste testset, in Blender 4.2, 5.2 en 5.3, met oorzaak, nulmeting en eindmeting. Het oude ontwerp.md gaat over Click Joints 0.1.1 en 1.0.2 en is hier niet leidend.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Code: `DIEP_EXACT` staat weer op False, dus de oude keuze in 4.2 blijft. De commentaren zijn aangepast en de proef (run 45261862637, geen gewricht erbij) staat in de uitslag. | Feit (diff) | Hoog | Staat in de diff. |
| 2 | De uitslag meldt 60 van 60 in 5.2 en 5.3 en 55 van 60 in 4.2, nul slechte sneden in 5.x. De vijf missers in 4.2 staan eerlijk beschreven, met de oorzaak (Exact in 4.2). | Vermoeden | Midden | De JSON op tak `betrouwbaar-uitslag` en een run op de eindstand. Ik kan die niet zien. |
| 3 | De eindmeting is gedaan op da1c134 en wordt "zelfde code als de eindstand" genoemd. Deze commit zet `DIEP_EXACT` terug op False. Als da1c134 True had, is de 4.2-tabel met een andere stand gemeten. | Vermoeden | Laag | `git show da1c134:…/scharnier.py`, of een nieuwe run op 7ea796e. |
| 4 | De oorzaak (H snijdt zichzelf, boolean niet bepaald, 4.2 heeft een eigen Exact-fout) wordt met meetregels onderbouwd. Punt 3 van de oorzaak wordt als GOK gemarkeerd. | Vermoeden | Midden | De meetregels `h_zelf_overlap` en `h_soort` in de JSON. |
| 5 | De diagnose-instrumentatie (`verloren_stuk`, `CJ_OMHULSEL_UIT`) is alleen meetcode. Ze rekent met `SNEDEN`, `_HUIDIG` en `omhulsel.AAN`, die buiten deze diff liggen. | Vermoeden | Midden | Een run van meet_diag met en zonder `CJ_OMHULSEL_UIT`. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `meet_drempel.json` zegt "Geldt voor 4.2, 5.2 en 5.3". De eigen eindmeting geeft in 4.2 maar 7 (robot-a, robot-b) en 8 (kleding) tegen een drempel van 9. Of de test draait dus rood in 4.2, of de drempel geldt daar niet en de uitleg is onjuist. | Feit (tekst tegen tekst), werking van de test is vermoeden | Midden | Tests niet aanpassen om te slagen, en een drempel moet doen wat hij beweert |
| 2 | De drempel voor rigify gaat van 9 naar 7. De reden staat erbij: bovenarm van 29 mm, in elke versie, voor en na, en de nulmeting van main gaf in 5.x ook al 7. Dat is geen aanpassing om te slagen. Het is een correctie van een onhaalbaar getal. | Vermoeden | Midden | Tests niet aangepast om te slagen |
| 3 | De uitslag labelt cijfers netjes (GEZIEN, GOK). De bron is een tak die ik niet kan lezen. De uitslag noemt de MakeHuman-licentie (CC0) en de eigen robot. | Vermoeden | Midden | Cijfers met GEZIEN, DERDEN, GOK |
| 4 | Meshy knight zit in de gewone e2e, met in de uitslag zelf "licentie niet nagelezen". Dit zit niet in de testset en is niet nieuw in deze wijziging. | Feit (uitslag) | Hoog | Alleen eigen of vrije beelden en modellen |
| 5 | Bestandslengte en architectuur.md: de diff raakt geen architectuurtekst. De uitslag noemt omhulsel.py, herstel.py en redenen.py. Ik kan niet zien of die al in architectuur.md staan. De regelaantallen zijn ook niet te zien. | Vermoeden | Laag | architectuur.md bijgewerkt, bestanden onder ±400 regels |
| 6 | Geen persoonsgegevens, sleutels of wachtwoorden gezien in de wijziging. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | In 4.2 duurt "Figure from rig" nu langer op lichte figuren (mens 340 s naar 214 s, rigify 164 s naar 282 s, kale mens in 5.x 14 s naar 57 s). Een koper wacht minuten zonder te weten hoe lang. | Voortgangsregel per gewricht, en een grovere voxel op kleine figuren. | Midden |
| 2 | In 4.2 blijven op robot en aangekleed figuur de knieën soms zonder gewricht. De nieuwe zin met wat de koper kan doen is goed. | Dezelfde zin al in het paneel tonen en direct "Blender 4.5 of nieuwer" noemen. | Klein |
| 3 | Dit is mogelijk niet kijkbaar in een run. Of de gewrichten er na de snede goed uitzien en bewegen, moeten Daan en Iris zien. | Een nieuwe schermserie van de zeven figuren op tak `schermen`. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Maak de drempel in `meet_drempel.json` kloppend voor 4.2. Zet per versie een eigen ondergrens (4.2 dus lager voor robot-a, robot-b en kleding), of haal "en 4.2" uit de uitleg. Zo weten we welke versie de test bewaakt en kan een terugval in 4.2 niet ongemerkt blijven.

**Kan**
1. Controleer of de eindmeting op da1c134 met `DIEP_EXACT` False is gedaan, anders meet opnieuw op 7ea796e.
2. Lees de licentie van de Meshy knight na, of haal hem uit de gewone e2e.
3. Zet omhulsel.py, herstel.py en redenen.py in architectuur.md als dat nog niet is gebeurd.
4. Voortgangsregel of grovere voxel voor lichte figuren (deel C, punt 1).
5. Deze keuring ging op tekst alleen. Beeld en speelplezier moeten Daan en Iris nog bekijken.

---
Automatische keurder, model `claude-sonnet-5-5`, 23306 tokens in, 5663 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
