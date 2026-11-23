# Keuring blender-gewrichten testset Figure from rig, 23-11-2026, automatische keurder
Wat ik keurde: commit 196691ee2 (e2e/meet_diag.py, meet_drempel.json, meet_eis.py, meet_rig.py)
Akkoord: ja

## Deel A: doet het wat beloofd is?
Er is geen ontwerpeis voor deze wijziging, dus ik toets tegen de commitbelofte: een testset met meetregels per snede (nulmeting). De add-on zelf verandert niet, dus het akkoord van 16 nov voor 0.1.1 en 1.0.2 blijft staan.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Alle zeven figuren uit de commit hebben een bouwer en een drempel (robot-a, robot-b, robot-fijn, kleding, mens, rigify, armen). | Feit (uit de diff) | hoog | n.v.t. |
| 2 | Er is geen uitslag of log van een echte run meegestuurd. Of de scripts in Blender 4.2 en 5.x draaien, staat dus niet vast. | Vermoeden | midden | Een groene of rode CI-run met de regels `MEET ...` en `EIS ...` per figuur. |
| 3 | De rigify-tak hangt af van `CJ_HOOK` in `proef_rigify.py` en van `_MEET_T0` in de namespace `G`. Dat bestand zit niet in de diff. Ontbreekt een van beide, dan zijn de meetregels uit of staat `knop_s` ongeveer op 0. | Vermoeden | midden | `proef_rigify.py` lezen op `CJ_HOOK`, of de rigify-run bekijken: staan er sneden in de uitslag? |
| 4 | `verslag("held", ...)` gaat uit van de figuurnaam "held" voor rigify. Klopt dat niet, dan telt `figuur_gewrichten` nul en staat de eis rood om de verkeerde reden. | Vermoeden | laag | Rigify-uitslag met `gewrichten` groter dan 0. |
| 5 | In `meet_eis.py` laten slechte sneden onderweg de eis niet falen. Ze worden alleen geteld en geprint. Alleen te weinig gewrichten of open delen geven rood. Een snede zonder sleutel `goed` (bijvoorbeeld bij `meetfout`) telt als goed. | Feit | hoog | n.v.t. Het kan bewust zijn voor een nulmeting, maar dan hoort het in de docstring. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alle bestanden zijn kort (ruim onder 400 regels). | Feit | hoog | Bestanden onder ±400 regels |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens |
| 3 | De drempels staan op 9 voor de zes figuren met een rig en op 8 voor armen, zonder gemeten uitslag erbij. De uitleg zegt "ondergrens", de commit zegt "nulmeting". Een drempel die niet is gemeten hoort als GOK te staan. In de LEESMIJ van de studio viel bij robot-fijn lokaal de linkerheup weg, dus die drempel kan meteen rood geven. | Vermoeden | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | De testset is nieuw en past geen bestaande test aan om te slagen. | Feit | hoog | Tests niet aangepast om te slagen |
| 5 | Figuren komen uit eigen werk, de MakeHuman-basis (CC0, staat in de repo) en de Rigify-metarig van Blender. Er is niets gedownload en er zijn geen AI-beelden. | Feit (volgens de docstring) | midden | Geen AI-beeld of -geluid op Steam |
| 6 | `architectuur.md` is niet bijgewerkt. Het zijn alleen testbestanden zonder nieuw onderdeel van de add-on. | Feit | midden | architectuur.md bijgewerkt |

## Deel C: zou een gebruiker het leuk en fijn vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Dit is alleen testgereedschap en er is niets te zien of te spelen. Ik geef geen oordeel op plezier of beeld. | n.v.t. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet in `meet_drempel.json` of de README erbij of de 9 en 8 gemeten (GEZIEN, met runnummer) of geschat (GOK) zijn.
- Laat de eis ook rood worden bij `meetfout`, of zet in de docstring dat slechte sneden bewust niet blokkeren.
- Controleer dat `proef_rigify.py` `CJ_HOOK` en `_MEET_T0` ondersteunt, en dat de rigify-figuur "held" heet.
- Koppel de testset aan een workflow (`.github/workflows`) en bewaar de uitslag-JSON als artefact. In deze diff staat daar niets van.

---
Automatische keurder, model `claude-sonnet-5-5`, 26742 tokens in, 4143 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
