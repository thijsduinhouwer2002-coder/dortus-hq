# projecten.json: uitleg van de velden

`organisatie/projecten.json` is de ene bron voor de stand per project. Het dashboard (`dashboard/bouw.py`, elk half uur naar de tak `dashboard`) leest het; de hoofdchat-ronde werkt het elk uur bij. Een push die dit bestand raakt, bouwt het dashboard meteen opnieuw.

**Regels:** geen persoonsgegevens van Thijs (schrijf "staat bij Thijs"); elk getal krijgt een label GEZIEN, DERDEN of GOK; verzin niets, schrijf "nog geen schatting" als een keuring geen bedrag of kans geeft. Bij elke wijziging aan een project ook `laatste_update` bijwerken.

**Schrijf voor Thijs, niet voor agents.** De statuszin, volgende stap en het risico leest Thijs in één oogopslag: gewone woorden, zoals een eigenaar het zegt ("Speelt op de computer, wacht op een tweede keuring"). Geen commit-hashes, geen run-nummers, geen vaktaal als "moet-punten", "Pending", "e2e" of "R4". Op het overzicht staat alleen het begin van de statuszin (één regel): zet het belangrijkste vooraan.

**Controle:** `dashboard/bouw.py` controleert dit bestand eerst (`dashboard/controle.py`). Klopt er iets niet (geen geldige JSON, een tekst waar een getal hoort, een datum als "27 nov"), dan bouwt het dashboard toch en zet bovenaan de pagina een rode melding met wat er mis is; het foute veld wordt weggelaten. Bij een bestand dat helemaal geen geldige JSON is, toont het dashboard de laatste goede stand uit de geschiedenis, met de melding erboven. Dezelfde controle draait vanzelf vóór elke push (`.githooks/pre-push`) als `projecten.json` meegaat: klopt hij niet, dan stopt de push. Zelf nakijken: `python3 dashboard/controle.py`.

## Bovenaan
- `bijgewerkt`: `datum` ("JJJJ-MM-DD UU:MM", NL-tijd) en `door` van de laatste ronde die het bestand naliep.

## Per project
| Veld | Wat | Voorbeeld |
|---|---|---|
| `id` | korte naam, kleine letters en streepjes; wordt de link `#id` | `reddit-hat-tower` |
| `naam`, `kort` | volle naam, en een korte voor tabs op de telefoon | |
| `wat` | één zin: wat is het | |
| `soort` | `product`, `geldroute` of `meetproject` | |
| `voor` | `Dortus` of `Thijs-zelf` (meetprojecten van Thijs, los van Dortus: geen bedragen, geen gegevens van Thijs) | |
| `platform` | waar het staat of komt | |
| `status` | `woord` (één woord), `kleur` en `zin` (één zin). `kleur` is `op-koers`, `let-op`, `risico` of `stil` (geparkeerd); het dashboard toont kleur, vorm en woord samen | |
| `eigenaar` | wie het eindoordeel heeft (agent of `hoofdchat`) | |
| `agents` | wie er nu aan werkt; namen zoals in `dashboard/ploeg.json` | |
| `kans` | kans op meer dan €0 binnen 12 weken. Of `laag` en `hoog` in procent, of `tekst` ("middel", "nog geen schatting"). Altijd `label`, `reden` en `bron` (pad of link naar de keuring) | `{"laag": 10, "hoog": 20, "label": "GOK", ...}` |
| `prognose` | euro's binnen 12 weken (tot do 11 feb 2027). `verwacht` is een getal of `[van, tot]`, en is al kans maal opbrengst (zo rekenen de keurders). `laag` en `hoog` zijn de slechtste en beste uitkomst, als de keuring die geeft. `samen: true` als het bedrag voor meer projecten samen geldt. Geen bedrag: `tekst`. Altijd `label`, `reden`, `bron` | |
| `volgende_stap` | één zin | |
| `deadline` | `datum` (JJJJ-MM-DD), optioneel `tijd` (NL), en `wat`; of `null` | |
| `thijs` | **een lijst** met wat alleen Thijs kan voor dit project, elk punt met `doen` en optioneel `voor` (JJJJ-MM-DD); `[]` als hij niets hoeft. Een project kan dus meer punten hebben. "Jij moet doen" op het dashboard is `lijst-thijs.md` plus deze punten, zonder dubbelingen (zelfde woorden of zelfde datum telt als hetzelfde punt). De lijst van Thijs blijft van de hoofdchat: zet een punt dat echt moet ook daar | `[{"doen": "Speeltest spelen", "voor": "2026-11-21"}]` |
| `risico` | één zin: wat kan het laten mislukken | |
| `laatste_update` | `datum` en `door` | |
| `links` | lijst van `naam` en `url`; een pad in de repo wordt vanzelf een GitHub-link | |
| `cijfers` | sleutels uit het scorebord: `product|platform|maat`, precies zoals in `organisatie/scorebord-data.csv`. Het dashboard haalt waarde, bron en reeks zelf op | `Rollwright|Obsidian|downloads` |
| `mappen` | mappen in de repo; het dashboard toont de laatste commits die ze raakten | |
| `keuringen` | keuringsbestanden; het dashboard toont het nieuwste oordeel ("Akkoord:"-regel) met de kop erboven. Nieuwste = de regel die het laatst in git kwam, dus een herkeuring mag boven- of onderaan staan | |

## Hoe het dashboard sorteert en wat het toont
Op de overzichtstab staan projecten van Dortus eerst, gesorteerd op verwachte opbrengst (het midden van `verwacht`, dat al kans maal opbrengst is). Daarna projecten zonder schatting, dan projecten met €0, en als laatste de meetprojecten van Thijs zelf. De kop van het overzicht telt `verwacht` van alle Dortus-projecten op. Bovenaan staat ook "Stand projecten" uit `bijgewerkt`; die wordt oranje als hij ouder is dan 3 uur, dus werk `bijgewerkt` elke ronde bij, ook als er niets veranderde. GEZIEN, DERDEN of GOK staat alleen bij getallen; een woord als "middel" of "laag" krijgt geen label op het scherm, maar wel in dit bestand.

## Wat de ronde elk uur bijwerkt
1. `status` (woord, kleur, zin), `volgende_stap`, `deadline` en `thijs` van elk project dat veranderde (lees bord, berichten, logboeken).
2. `kans` en `prognose` alleen als er een nieuwe keuring of meting is; zet de bron erbij.
3. Nieuwe sleutels in `cijfers` als het scorebord een nieuwe maat krijgt.
4. `agents` als er iemand aan of uit gaat.
5. `laatste_update` per gewijzigd project en `bijgewerkt` bovenaan.
6. Een nieuw project: kopieer een bestaand blok, nieuwe `id`.
