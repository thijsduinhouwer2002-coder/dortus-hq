# Keuring blender-gewrichten, herkeuring betrouwbaar-rig (cf40965..dc39666), 24-11-2026, automatische keurder
Wat ik keurde: commit dc3966683, alleen het bestand `producten/blender-gewrichten/keuring/2026-11-24-betrouwbaar-rig-A.md` (tekst, geen code)
Akkoord: nee

## Deel A: doet het wat beloofd is?
De wijziging is een keuring, geen add-on. Ik toets of die keuring klopt en zichzelf waarmaakt. De add-on op tak `claude/betrouwbaar-rig` en de logs van run 45282711505 zie ik niet.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | M1c telt kloppend op: 173+220+220 = 613 tak en 48+111+112 = 271 nul, samen 884 geslaagde kogelsneden, zoals de keuring zegt. | Feit (rekensom uit de tekst) | Hoog | Alleen de bron zelf: de JSON in `betrouwbaar-uitslag/45282711505/`. |
| 2 | M1d somt voor 4.2 op: robot-a 6, robot-b 6, robot-fijn 7, kleding 8, mens 9, rigify 7, armen 8. Dat is samen 51 van 60. M2a rekent "44 van 51" voor als 6+6+8+9+7+8. Die som laat een 7 weg en komt op 44, terwijl M1d 51 geeft. De twee bladzijden gebruiken "51" dus voor iets anders, en de tekst legt dat niet uit. | Feit (tegenstrijdigheid in de tekst), oorzaak is een vermoeden | Midden | Een uitleg waarom 44 van 51 een andere meting is dan 51 van 60, of een rechtgezette telling bij de bron. |
| 3 | Het releasenote-voorstel ("44 instead of 28 of 51") komt uit die onduidelijke telling. Dit gaat in een openbare tekst. | Feit | Midden | Hetzelfde als bij 2. |
| 4 | De keuring zegt "Akkoord: ja", maar met een open voorwaarde. Run 45287215003 moet groen zijn in 4.2.23. De nieuwe toets `CJ_HERKANS=3` is alleen in 5.2.3 en 5.3.0 gezien. Dat staat eerlijk in de tekst. | Feit | Hoog | Een groene run 45287215003 in 4.2.23. |
| 5 | M3 zegt dat er geen bestaande `check(...)`-regels of `meet_drempel.json` veranderd zijn. Dat is niet na te gaan in de gestuurde diff, alleen de keuring is meegestuurd. | Vermoeden | Midden | `git diff 5aa27a8 25efd95` op de tak. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen code of test aangepast. Alleen een keuringsbestand is aangevuld. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand bevat geen persoonsgegevens of sleutels. Het noemt alleen run-nummers, commits en figuurnamen. | Feit | Hoog | Geen persoonsgegevens |
| 3 | Cijfers staan met GEZIEN of als telling bij de bron. Alleen "voxelsneden 125, 37, 35" is niet nageteld, en dat staat er ook bij. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Het formulier wijkt af van het vaste model: het heeft "Deel A" en een eigen tabel met "Punt" in plaats van de vaste kolommen, en er is geen Deel B of C. Dat is te verdedigen voor een herkeuring van twee punten. | Feit | Midden | Vast formulier |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing: er is niets te zien of te spelen in deze wijziging.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | In het releasenote-voorstel staat "In 4.2, Figure from rig can take a few minutes". Dat is eerlijk, maar een koper op 4.2 ziet liever vooraf in het paneel dat het even duurt. | Een korte regel of voortgangsmelding in het paneel bij 4.2. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Maak de telling "28 naar 44 van 51" in M2a consistent met de 51 van 60 in M1d. De som 6+6+8+9+7+8 = 44 laat een van de zeven getallen weg. Leg uit wat 44 van 51 meet, of zet het goed voordat het in het releasenote-voorstel blijft staan.

**Kan**
1. Zet de voorwaarde (run 45287215003 groen in 4.2.23) duidelijk in de kop, bijvoorbeeld "Akkoord: ja, onder voorwaarde". Werk de keuring bij zodra de run klaar is.
2. Verbeter de twee kleine dingen die de keuring zelf noemt: "rigify tak 1 van 5" tegenover 3 van de 5, en "4.2 zie het bericht".
3. Tel de voxelsneden (125, 37, 35) na of haal ze weg.
4. Stuur bij een volgende keuring de diff van de tak mee, zodat bewering M3 te toetsen is.

---
Automatische keurder, model `claude-sonnet-5-5`, 19277 tokens in, 3876 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
