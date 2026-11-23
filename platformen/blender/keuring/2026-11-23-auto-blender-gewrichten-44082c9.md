# Keuring blender-gewrichten, eerlijke Tight-reden en nekreden, 23-11-2026 19:10 NL, automatische keurder
Wat ik keurde: commit 44082c9aa (868f009..44082c9), vijf bestanden onder producten/blender-gewrichten/
Akkoord: ja

## Deel A: doet het wat beloofd is?
Getoetst tegen de commitbeschrijving en ontwerp.md. Ik kon niets draaien en heb alleen de diff gelezen.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `maten_neus` gedraagt zich gelijk aan voorheen voor alle gevallen waar de oude code Tight gaf of een scharnier maakte. De nieuwe `klik_bij(l)` herhaalt de oude controles (l ≤ 0, t ≤ 0, rek tegen REK_MAX, k tegen H_MIN). Alleen de tekst verandert: TIGHT_KORT komt alleen als de volle lip wel zou klikken en de onderkant hem te kort maakt. | Feit (uit de diff) | Hoog | Een groene run van `toetsen_neus.py` en `toetsen_neus_kort.py` in Blender 4.2 en 5.2. |
| 2 | Zonder `diepte` is lip gelijk aan lip_vol, dus er komt nooit TIGHT_KORT, alleen TIGHT. Dat klopt met de bedoeling. | Feit | Hoog | n.v.t. |
| 3 | `kogel_reden` geeft nu voor NECK een leesbare zin bij "too thin here for a ball joint", "nothing was cut" of lege melding. Andere meldingen blijven ongewijzigd. De nieuwe toets in `toetsen_rig.py` dekt alle drie de takken. | Feit | Hoog | Groene run van `toetsen_rig.py`. |
| 4 | De rekenvoorbeelden in de nieuwe toets (t = 0,4, lip_vol 6,5, diepte 1,0, L = 0,2, k ≈ 0,002 tegen H_MIN 0,1) kloppen met de comments, mits ZAAG, REK_MAX en H_MIN de waarden hebben die de comments aannemen. Ik zie die constanten niet. | Vermoeden | Midden | De uitslag van de toets in de run. |
| 5 | De toetsen met de korte staaf (6 mm) en de dunne ronde onderkant (6,5 mm) verwachten nu TIGHT_KORT. Dat past alleen als de volle lip daar wel klikt. De docstring van `_schuin_tight` zegt dat dit zo is ("wel een scharnier" met alleen het midden). | Vermoeden | Midden | De regel `METING korte staaf 6 mm` en `METING dunne ronde onderkant` in het log. |
| 6 | Code die de melding vergelijkt met `neus.TIGHT` (gelijkheid) kan elders staan, bijvoorbeeld in het paneel of in `rig.py`. De diff laat dat niet zien. TIGHT_KORT begint nog wel met "Tight:". | Vermoeden | Laag | Een grep op `TIGHT` en `"Tight"` in `click_joints/` en `e2e/`. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een nieuwe toets bij gekomen (TIGHT_KORT, NECK). In `toetsen_neus_kort.py` zijn twee verwachtingen van TIGHT naar TIGHT_KORT gegaan. Dat volgt uit een bewuste gedragswijziging en geen versoepeling: de toetsen eisen nog steeds CANCELLED, geen nieuwe objecten en een precieze reden. | Feit | Hoog | Tests niet aangepast om te slagen: ok |
| 2 | `architectuur.md` is niet bijgewerkt. Het zichtbare deel noemt de Tight-teksten van de kogel en de oorzaakregel. Het afgekapte deel kan ook de scharniertekst of de NECK-melding noemen. | Vermoeden | Laag | architectuur.md bijgewerkt |
| 3 | Bestandslengte is niet te beoordelen: de diff toont alleen regels rond de wijziging. `toetsen_neus.py` loopt tot voorbij regel 177 en kan dicht bij de ±400 zitten. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. Geen cijfers zonder bron of spelerstekst (Hats) of AI-beeld of -geluid. | Feit | Hoog | Persoonsgegevens, GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan alleen de teksten lezen en heb het paneel niet gezien.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | "Neck (not placed)" zonder reden wordt een zin met een vervolgstap ("place it by hand"). Dat helpt de koper meteen. | Niets nodig. | klein |
| 2 | De nekzin noemt als oorzaak "short or sits inside the head". Een nek die echt te dun is krijgt dezelfde zin en dat kan misleiden. | "too thin, short or inside the head" of de wand in mm erbij, zoals bij de kogel. | klein |
| 3 | "Try a spot further from the end" is duidelijk. De koper weet niet hoeveel verder. | Het minimale aantal mm tot het uiteinde in de melding, bijvoorbeeld "at least N mm from the end". | midden |
| 4 | De tekst zegt bij zowel Tight als Tight_kort welke kant op te zoeken. Dat is een goede lijn en past bij de andere meldingen. | Niets nodig. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zoek op `neus.TIGHT` en `"Tight"` in paneel en `rig.py`, voor gelijkheidsvergelijkingen die TIGHT_KORT zouden missen (A6).
- Controleer of `architectuur.md` de scharnier-Tight-tekst of de NECK-melding noemt en werk dat bij (B2).
- Maak de nekzin eerlijker voor een nek die te dun is (C2).
- Overweeg het aantal mm tot het uiteinde in TIGHT_KORT (C3).
- Wacht op de groene run van `toetsen_neus.py`, `toetsen_neus_kort.py` en `toetsen_rig.py` voor je uitbrengt (A1, A4, A5). Ik heb ze niet kunnen draaien.

---
Automatische keurder, model `claude-sonnet-5-5`, 21507 tokens in, 5374 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
