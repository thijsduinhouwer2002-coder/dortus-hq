# Keuring blender-gewrichten (meetscript scharniersnede), 23-11-2026, automatische keurder
Wat ik keurde: commit 78ac6d9ee, bestand producten/blender-gewrichten/e2e/meet_diag.py (f804f10..78ac6d9)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is het ja van 16 nov voor Click Joints 0.1.1 en Pro 1.0.2. Deze wijziging raakt de add-on niet. Ze voegt alleen een meting toe aan een diagnosescript.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Alleen `e2e/meet_diag.py` is gewijzigd, geen bestand in `click_joints/`. Het akkoord van 16 nov (add-on ongewijzigd sinds 1d0c54c) blijft dus gelden. | Feit | Hoog | Een `git diff` over `click_joints/` zou dit bevestigen. De bestandslijst van de commit toont het al. |
| 2 | De nieuwe meting draait alleen als `CJ_PROEVEN` is gezet, bij Exact en als de snede niet gesloten is. Zonder die variabele verandert er niets in bestaande testruns. | Feit | Hoog | Een groene run zonder `CJ_PROEVEN` met hetzelfde log als voorheen. |
| 3 | `proeven_scharnier` roept `oud` aan (de oude snijfunctie), niet `snij_scharnier`. Een eindloze herhaling is dus niet te verwachten. | Feit | Hoog | Een run met `CJ_PROEVEN` zonder vastlopen. |
| 4 | De code gebruikt `mod`, `Matrix`, `_ruim`, `os` en `oud_scharnier`. Het diff laat niet zien of die in het bestand bestaan. | Vermoeden | Midden | Een run met `CJ_PROEVEN=1` waarin `rec["proeven"]` gevuld is en er geen NameError staat. |
| 5 | De regel `if een_lid.STAND.get("h") is not None: STAND["bronnen"] = {}` wordt niet toegelicht. Ze lijkt een staat te resetten, maar de reden staat nergens. | Vermoeden | Laag | Een korte opmerking van de bouwer, of een run waarin de beide proeven gelijke startstand hebben. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Er is alleen een meetpad bijgekomen dat niets afkeurt of goedkeurt. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | De wijziging is 30 regels. Of het bestand onder ±400 regels blijft, is niet te zien. De haakjes in het diff (regel 237+) wijzen op een bestand van enkele honderden regels. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want het gaat om een testhulp en de add-on is gelijk gebleven. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | De commit bevat geen cijfers of beweringen, dus er is niets om met GEZIEN, DERDEN of GOK te labelen. Er is ook geen spelerstekst en geen AI-beeld of -geluid. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK, Hats, Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing. De wijziging bevat geen beeld, geluid of speelbare onderdelen, en geen verandering voor de gebruiker.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Geen gebruikerszichtbare verandering. | Niets nodig. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij de regel met `STAND["bronnen"] = {}` een korte opmerking over wat hij herstelt en waarom.
- Self Intersection aan duurde eerder ±87 s (GEZIEN in het ontwerp). Zet voor deze meting een tijdslimiet of een lopende teller in het log, zodat een run niet vastloopt.
- Zet `EXACT_ZELF` terug in een `finally`, zodat een afbreking midden in de proef de module niet in de verkeerde stand laat.
- Controleer in de eerstvolgende run met `CJ_PROEVEN=1` dat `rec["proeven"]` gevuld is (zie A4).

---
Automatische keurder, model `claude-sonnet-5-5`, 17986 tokens in, 2689 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
