# Keuring blender-gewrichten (Figure from rig, extra kogelplek), 23-11-2026, automatische keurder
Wat ik keurde: commits e292277..a3f5e85 (5bac7f758, 6dcadc823, 08d1637ab, 8e07654fc): `betaald/rig.py`, `architectuur.md` en `proeven/studio2-figuren-2026-11-23/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Het akkoord in `ontwerp.md` (16 nov) gaat over gratis 0.1.1 en Pro 1.0.2. Deze wijziging raakt alleen Pro-code (`betaald/rig.py`) en bewijs, en zegt nergens dat er iets live gaat.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De code voegt als laatste kogelkandidaat dezelfde plek 0,3 mm verder het lid in toe, met een grens `< 0,5 * lengte`. Dit komt overeen met de beschrijving in architectuur.md. | Feit (diff) | hoog | n.v.t. |
| 2 | Het beweerde resultaat is robot CI 8 naar 9 gewrichten, gelijk aan lokaal 9. Dat staat alleen in de uitslag, met verwijzing naar runs 45206324187 en 45208410893. Ik zie de logs niet. | Vermoeden | midden | De logs in `organisatie/actions-logs/` of een groene CI-run op de robot met 9 gewrichten. |
| 3 | In de diff zie ik niet waar `t_vrij` en `u` zijn gedefinieerd. Het gebruik past bij de naburige code, maar ik kan niet nagaan of de variabele altijd bestaat. | Vermoeden | midden | Een run van `kogel_schuif` op een figuur waar `t_vrij` normaal is, of de volledige functie. |
| 4 | De oorzaak is niet weggenomen. Op de AMD-processor blijft de eerste heupplek kapot (1110 overlappende driehoeken), alleen de tweede plek is gaaf. Een figuur waarvan ook de tweede plek per processor kapot uitvalt, blijft dus mogelijk hetzelfde probleem houden. | Vermoeden | midden | Dezelfde proef op meer figuren op de AMD-runner. |
| 5 | Architectuur.md zegt dat de volgende plek alleen bij "too close", "no watertight parts" en (scharnier) "too thin"/"tight" wordt geprobeerd. De uitslag zegt dat de knop de "blocked" snede terugdraait en daarna een extra plek nodig had. Hoe "blocked" bij een kogel de volgende kandidaat bereikt, is uit de diff niet te zien. | Vermoeden | laag | De aanroeper van `kogel_schuif` in `rig.py`. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast. Er is ook geen toets voor de nieuwe 0,3 mm plek, want de fout hangt van de processor af. | Feit | hoog | Tests niet aangepast om te slagen: in orde. Een eigen toets ontbreekt (kan). |
| 2 | Architectuur.md is bijgewerkt voor zowel de volgende plek als `kogel_schuif`. | Feit | hoog | architectuur.md bijgewerkt: in orde |
| 3 | `rig.py` heeft meer dan 320 regels (de wijziging staat rond regel 313). Of het onder ±400 blijft, zie ik niet. | Vermoeden | laag | Bestanden onder ±400 regels: de regelstand van `rig.py` |
| 4 | De uitslag labelt cijfers met GEZIEN en GOK en noemt de bronnen. Alleen de tabelrijen van Stan, Mike, George en Cyberpunk hebben geen eigen label, al staat de bron (release `studio-2`) erboven. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK: grotendeels in orde |
| 5 | De uitslag spreekt zichzelf tegen: "CI-meting loopt" staat bovenaan en de uitslag staat verderop. | Feit | hoog | Nauwkeurigheid van bewijs (kan) |
| 6 | Ik zie geen persoonsgegevens, sleutels of wachtwoorden in de drie bestanden. Er is geen AI-beeld of -geluid voor Steam en geen spelerstekst van Hats. | Feit | hoog | Geen persoonsgegevens: in orde |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan niets zien of spelen. De wijziging is alleen logica en documentatie.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een koper met een AMD-pc kan een ander aantal gewrichten krijgen dan een koper met een Intel-pc, zonder dat de reden zichtbaar is. De fix verkleint dat verschil. | Een korte melding in het paneel als een plek is overgeslagen vanwege een kapotte snede. | klein |
| 2 | Mike, Stan en George krijgen 0 tot 4 gewrichten. Een koper ziet dat als "werkt slecht", ook al is het eerlijk. | Eén samenvattende regel met de reden en een tip, bijvoorbeeld "zet het figuur aan elkaar" bij los gedeelde stukken. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Voeg een toets toe die de extra 0,3 mm plek raakt, bijvoorbeeld door op een gewone machine de eerste plek te weigeren, zoals `CJ_HERKANS=1` dat al voor "no watertight parts" doet.
- Onderzoek de snede die per processor verschilt. Test het ook op scharnieren: de fix geldt alleen voor de kogel (`kogel_schuif`).
- Haal "CI-meting loopt" uit de uitslag en label de overige rijen van de tabel.
- Controleer in `rig.py` dat `t_vrij` en `u` altijd bestaan en dat het bestand onder ±400 regels blijft.
- Klaar om samen te voegen in deze scope. Een nieuwe Pro-uitgave (Superhive) hoort een eigen keuring te krijgen, want het akkoord in `ontwerp.md` geldt voor 1.0.2.

---
Automatische keurder, model `claude-sonnet-5-5`, 23272 tokens in, 4187 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
