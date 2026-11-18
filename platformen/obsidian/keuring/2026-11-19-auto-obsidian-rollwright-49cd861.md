# Keuring obsidian-rollwright week-test en vast zaad in e2e, 19-11-2026, automatische keurder
Wat ik keurde: commit 49cd8613 (64cb28b..49cd861), alleen `producten/obsidian-rollwright/e2e/wdio.conf.mjs`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is het akkoord in `ontwerp.md` voor 0.3.5. Dat akkoord geldt zolang alleen `manifest.json`, `versions.json` en de CHANGELOG veranderen en e2e main groen is. Er is geen apart ontwerp voor deze roestronde, dus ik toets de wijziging aan zijn eigen commitbericht.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het product (`src/`, `styles.css`, manifest) is niet aangeraakt. De voorwaarde van het akkoord voor 0.3.5 blijft dus staan. | Feit | Hoog | Niets nodig. |
| 2 | `OBSIDIAN_APP` en `OBSIDIAN_INSTALLER` kiezen een andere Obsidian-versie. Zonder die variabelen blijft het bij "latest" en "earliest", dus de gewone e2e verandert niet. | Feit | Hoog | Een groene e2e-run op main na deze commit. |
| 3 | Het bericht noemt "beeldvergelijking in drie e2e's", maar in de diff staat geen enkele spec of vergelijking. Het zaad is er wel, de vergelijking niet. | Feit dat het niet in de diff staat, vermoeden dat het elders hoort | Midden | Een diff met de drie specs, of een andere commit in de reeks waar ze wel in staan. |
| 4 | Het commentaar zegt dat specs die `Math.random` vastzetten (crit, classic) de reeks bewaren en herstellen. Die specs staan niet in de diff. | Vermoeden | Midden | De crit- en classic-spec lezen, of een run waarin de crit- en classic-tests nog groen zijn. |
| 5 | Het zaad werkt alleen als de rekenkern `Math.random` aanroept (`src/engine/random.ts`, de standaard toevalsbron). Dat heb ik niet gezien. | Vermoeden | Midden | Zien dat `random.ts` `Math.random` gebruikt, of dezelfde worpen in twee runs naast elkaar. |
| 6 | De titel noemt Blender alpha en IDE EAP. Dat hoort bij andere producten en past niet bij Rollwright. De workflow voor de week-test staat ook niet in de diff. | Feit | Hoog | De workflow en de andere producten in dezelfde commit bekijken. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Alleen de configuratie is uitgebreid. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand is klein, ruim onder 400 regels. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Er is geen bestand bij gekomen of weggehaald, dus dat hoeft ook niet. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | In de diff staan geen persoonsgegevens, sleutels of wachtwoorden. De zaadwaarde 20261119 is gewoon een datum. | Feit | Hoog | Geen persoonsgegevens |
| 5 | Er is geen speltekst of beeld voor Steam bij gekomen, en geen AI-beeld of -geluid. | Feit | Hoog | Spelerstekst en Steam-regels |

## Moet (blokkeert akkoord) / Kan (mag later)

**Moet:** geen.

**Kan:**
1. Een mislukte zaadzetting wordt alleen gelogd (`ZAAD NIET GEZET`) en de test gaat gewoon door. Een latere beeldvergelijking kan dan zonder duidelijke reden afwijken. Laat de run falen of markeer het in het log, zodra de beeldvergelijking erin zit.
2. Laat de drie specs met beeldvergelijking meesturen, of leg uit in welke commit ze staan (zie A3). Het bericht belooft meer dan de diff laat zien.
3. Controleer in de volgende e2e-run op main dat crit en classic nog groen zijn met het vaste zaad (A4, A5). Dit is een vermoeden, geen bewijs.
4. Haal Blender alpha en IDE EAP uit de titel van deze commit of splits de commit per product (A6).

---
Automatische keurder, model `claude-sonnet-5-5`, 18990 tokens in, 2914 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
