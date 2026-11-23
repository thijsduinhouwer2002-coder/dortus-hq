# Keuring Omhulsel H (controle op het lid, meer vlakken, extra meting), 23-11-2026, automatische keurder
Wat ik keurde: commit fc5b58f6d, bestanden `click_joints/betaald/omhulsel.py` en `e2e/meet_diag.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De opdracht (ja van 16 nov) gaat over gratis 0.1.1 en Pro 1.0.2. Deze wijziging komt daarna en raakt alleen de betaalde map `betaald/`. De gratis zip lijkt dus gelijk te blijven. | Vermoeden | Midden | Een groene run van `e2e/toets_zips.py` op deze commit. |
| 2 | `BUITEN_MAX` gaat van 0,002 naar 0,02. Daardoor mag nu tot 2% van de controlepunten van het lid buiten omhulsel H vallen. Het comment legt uit waarom: in een holte vouwt de verschoven huid om. Het comment noemt metingen van 0,2 tot 1,9% waarbij de snede goed bleef. | Feit (diff en comment), de redenering is een vermoeden | Midden | Een run op alle testfiguren (ook de holtefiguren) met `h_buiten` en `h_buiten_om` in het log, waarin de delen na de snede nog gesloten en zonder overlap zijn. In de diff staat geen run ná deze wijziging. |
| 3 | `MAX_VLAKKEN` gaat van 160000 naar 250000. Dat maakt de booleans trager. De eis uit het ontwerp is onder 5 s per gewricht. Of die nog gehaald wordt, staat niet in de wijziging. | Vermoeden | Midden | De tijdregels van een nieuwe run, met Exact op 4.2 en Manifold op 4.5+. |
| 4 | De controle gebeurt nu alleen op het lid. Het omhulsel rond het vlak wordt alleen gemeten voor het verslag (`h_buiten_om`). Dat past bij de titel en bij de bedoeling. | Feit | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen testbestand is aangepast. De drempel staat in de add-on zelf en niet in een test. De drempel is wel tien keer ruimer geworden, en dat is met een meting uit een eerdere run onderbouwd. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | `architectuur.md` is niet bijgewerkt. Of daar `MAX_VLAKKEN` of `BUITEN_MAX` staan, kon ik niet zien, want de tekst is afgekapt. | Vermoeden | Laag | architectuur.md bijgewerkt |
| 3 | Het comment noemt cijfers (0,2 tot 1,9 procent) en run 45255097554, maar zonder GEZIEN erbij. | Feit | Hoog | Cijfers met GEZIEN, DERDEN of GOK |
| 4 | De meetcode zet `EXACT_ZELF` per proef om en zet hem daarna terug. Dat gebeurt buiten de `try`, dus een fout in `oud(...)` laat hem niet hangen. Hij draait alleen onder `CJ_PROEVEN`. | Feit | Midden | Meten mag de knop nooit breken |
| 5 | Of de bestanden onder ±400 regels blijven, valt uit deze diff niet af te lezen. Geen persoonsgegevens of sleutels gezien. | Vermoeden | Laag | Bestanden onder ±400 regels, geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niets te zien of te spelen in deze wijziging, dus geen oordeel over plezier. Een gebruiker merkt hooguit dat het plaatsen op een lid met veel holtes langzamer of vaker raak is. | Houd de tijd per gewricht in het oog zodra `MAX_VLAKKEN` omhoog gaat. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Draai een run na deze commit en leg `h_buiten`, `h_buiten_om` en de snedetijden vast, voordat de ruimere drempel in een Pro-uitgave komt. Dat is een vermoeden dat een run moet bevestigen, geen blokkade.
- Controleer of `architectuur.md` de nieuwe waarden noemt en werk hem zo nodig bij.
- Zet een GEZIEN-label bij de cijfers in het comment.
- Dit akkoord geldt voor de tekst van deze wijziging, niet voor uitgebrachte versies. Het ja op 1.0.2 uit het ontwerp blijft apart staan.

---
Automatische keurder, model `claude-sonnet-5-5`, 20285 tokens in, 3131 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
