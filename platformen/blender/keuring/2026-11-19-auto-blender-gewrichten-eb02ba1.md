# Keuring blender-gewrichten meldknop (R5), 19-11-2026, automatische keurder
Wat ik keurde: commits 281d0a3..eb02ba1 (eb02ba15), product `blender-gewrichten`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Ik las alleen tekst. Ik heb niets gedraaid en geen scherm gezien.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `meld.py` maakt een operator en een subpaneel zonder kop met `bl_parent_id` op het hoofdpaneel. `meld` staat na `paneel` in `MODULES`, dus de volgorde van registreren klopt. | Feit | Hoog | Een schermafbeelding van het tabblad in 4.2 en 5.x, gratis en betaald. |
| 2 | De knop staat echt onderaan, ook onder knoppen die de betaalde build ophangt. De tekst zegt "GEZIEN op een scherm", maar er is geen beeld meegestuurd. | Vermoeden | Midden | Een schermafbeelding van de betaalde build met de knop als laatste. |
| 3 | De link bevat naam en versie uit het manifest, de Blender-versie, het systeem en een body. De toets leest het manifest uit de zip en vergelijkt dat met de geïnstalleerde add-on, dus ook de plek van het manifest wordt getoetst. | Feit (code en toets) | Hoog | Een groene run van `toetsen_melden.py` voor beide zips. |
| 4 | De gratis code noemt de betaalde versie, Pro of een prijs nergens. De naam komt uit het manifest. | Feit | Hoog | Een groene `toets_zips.py`. |
| 5 | De link gebruikt geen `template=`. Het ontwerp zegt dat de veld-ids het formulier vullen zodra het er staat, maar dat gebeurt waarschijnlijk alleen mét `template=`. Dan komt alleen de body door, en het kan zijn dat GitHub eerst de keuzepagina toont. | Vermoeden | Midden | De link openen in de loketrepo nadat het formulier erin staat. |
| 6 | Het is niet zichtbaar of de loketrepo `click-joints` al bestaat en meldingen toestaat. De tekst zegt zelf dat het formulier er nog niet staat. Bestaat de repo niet, dan geeft de knop een 404. | Vermoeden | Midden | De URL `.../click-joints/issues/new` openen. |
| 7 | In de diff staat geen run van de e2e, terwijl "e2e groen" een eis in het ontwerp is. `test_achtergrond.py` gebruikt `zip_pad`, en dat is in de diff niet te zien. | Vermoeden | Laag | Een groene run voor gratis en betaald. |
| 8 | De formulieren `bug.yml`, `idea.yml` en `config.yml` volgen het GitHub-formaat. Alleen "what" en "version"/"blender" zijn verplicht. De validatie zelf (GEZIEN 19 nov) heb ik niet gezien. | Feit (lezen) | Midden | Een uitslag van een schema-validator. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toetsen zijn niet versoepeld. Er is een nieuw bestand `toetsen_melden.py` bij gekomen. In `toets_zips.py` zijn alleen de hashes van `__init__.py` en `meld.py` bijgewerkt, met uitleg in een commentaarregel. Ik heb de hashes niet nagerekend. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Nieuwe code is klein: `meld.py` heeft 80 regels en de toets 63. `ontwerp.md` en `architectuur.md` zijn al ver boven 400 regels en groeien nog (6 regels, plus 2 lange regels in `architectuur.md`). | Feit | Hoog | Bestanden onder ±400 regels (voor code gehaald, voor documenten overschreden) |
| 3 | `architectuur.md` is bijgewerkt met `meld.py`, de formulieren en `toetsen_melden.py`. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | In de wijziging staan geen sleutels of persoonsgegevens, alleen een openbare GitHub-accountnaam in de repo-URL. De link stuurt het systeem zonder gebruikersnaam of paden mee. | Feit | Hoog | Geen persoonsgegevens |
| 5 | "GEZIEN op een scherm" en "geldig tegen het schema (GEZIEN 19 nov)" staan in de tekst, maar zonder bewijs erbij. Het onzekere gedrag van `template=` is wel als GOK gemarkeerd. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | `architectuur.md` zegt dat meldingen "vanzelf in `berichten/hoofdchat.md`" komen via `loket-meldingen.yml`. Die workflow zit niet in deze wijziging. Als daar tekst van buiten letterlijk in een agentbestand komt, kan dat persoonsgegevens meebrengen of agenten sturen. | Vermoeden | Laag | Geen persoonsgegevens, veilig omgaan met tekst van buiten |
| 7 | `bug.yml` vraagt om een foutmelding te plakken, zonder te zeggen dat paden met een gebruikersnaam eruit moeten. | Feit | Midden | Geen persoonsgegevens |
| 8 | De Daan-akkoordregel bovenin `ontwerp.md` geldt voor 0.1.1 op tak 4b7e722. De nieuwe knop is zichtbaar uiterlijk en heeft nog geen akkoord van Daan. | Feit | Hoog | Bij uiterlijk keurt Daan |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan, voor het uitbrengen:**
1. Laat Daan de knop in de gratis én de betaalde build beoordelen (rij A2, B8).
2. Bevestig met een groene run dat de e2e en `toets_zips.py` slagen voor beide zips (A3, A4, A7).
3. Controleer dat de loketrepo bestaat en dat het formulier erin staat. Voeg dan `template=bug.yml` toe en open de link nog eens, want zonder dat vullen de veld-ids waarschijnlijk niets (A5, A6).
4. Zet in `bug.yml` een zin dat paden met een gebruikersnaam uit een geplakte foutmelding moeten (B7).
5. Laat `loket-meldingen.yml` alleen titel en link naar de hoofdchat zetten, niet de hele melding (B6).

**Kan, later:** `ontwerp.md` en `architectuur.md` splitsen, want ze zijn ruim boven de 400 regels (B2).

---
Automatische keurder, model `claude-sonnet-5-5`, 30431 tokens in, 9601 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
