# Keuring Gevonden worden, tags top 3 (#161), 26-11-2026, automatische keurder
Wat ik keurde: commit 02752ea56 (KAART.md, `vindbaar/bron-tags-2026-11-26.json`, `vindbaar/bron_tags.py`)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De commit legt vast waar de tags van Click Joints Pro, Cleave, CatPin, Split 3DPrint en NB Figure Joints vandaan komen: 12 tags en de categorie per Superhive-product, plus zoekuitslagen van Gumroad. | Feit (uit het JSON-bestand) | hoog | Een nieuwe run van `bron_tags.py` zou dezelfde tags moeten geven. Ik kon dat niet draaien. |
| 2 | De commit zegt dat M1 van Daan (gratis versie zonder hinge-tag) is verwerkt. In deze wijziging staat die tekst niet: `platformen/blender/vindbaar-voorstel-2026-11-26.md` is niet meegestuurd. | Vermoeden | midden | Het voorstelbestand openen en kijken of de tags voor de gratis versie "hinge" missen. |
| 3 | KAART.md noemt nu "Daan ja (#167, met M1)" en "klaar om te plakken, vóór vr 27 nov 12:00", met een hermeting na 2 tot 3 dagen. Dat is een duidelijke vervolgstap. | Feit (tekst) | hoog | Issue #167 lezen om het ja van Daan te bevestigen. |
| 4 | De Gumroad-uitslag voor Click Joints Pro (4 producten, wij niet erbij) past bij de zin "Gumroad Discover toont ons nergens". | Feit | hoog | Niets nodig, de uitslag zelf is het bewijs. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens, sleutels of wachtwoorden. Er staan alleen publieke winkel-URL's en productnamen in. | Feit | hoog | Geen persoonsgegevens |
| 2 | Alle bestanden zijn kleiner dan 400 regels (JSON 218, script 32). | Feit | hoog | Bestanden onder ±400 regels |
| 3 | Er zijn geen tests of architectuurtekst aangepast. Voor een databron en een scriptje is dat niet nodig. | Feit | hoog | Tests niet aangepast, architectuur.md |
| 4 | De cijfers in KAART.md hebben hun herkomst erbij (DERDEN voor de Gumroad-eis, GEZIEN voor de plekken). Het JSON-bestand is zelf GEZIEN met een datum. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Het script doet zich voor als een browser (Chrome-UA) met `curl`. Dat past bij de afspraak om `curl` te gebruiken, maar het is wel scrapen van winkelpagina's. | Vermoeden | laag | Geen harde regel geschonden, wel iets om te weten |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen. De winkeltekst en tags zelf zitten niet in deze wijziging. | Bij het plakken de definitieve tags nog één keer bekijken zoals een koper ze ziet. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing: deze wijziging bevat geen beeld, video, winkeltekst, spel of site die een klant ziet, dus geen blinde test en geen cijfers. De winkeltekst wordt pas straks geplakt en vraagt dan een eigen keuring.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Controleer vóór het plakken in het voorstelbestand dat de tags van de gratis versie echt "hinge" missen (M1). Dat bestand zit niet in deze wijziging.
2. `tags_data` bij "click-joints-pro in 3d/3d-assets/blender" komt uit vier andere producten en is niet onze tags. Het commentaar in het script klopt hier niet, omdat wij niet in de uitslag staan. Haal dat veld weg of zet erbij dat het alleen telt bij `totaal == 1`.
3. Sluit het bestand in `bron_tags.py` netjes (`with open(...)`) en schrijf naar een vaste map, nu is dat de huidige map.
4. De unfiltered Gumroad-zoekuitslagen ("cleave zonder filter") bevatten ruis zoals "astral projection". Laat ze weg of markeer ze als ruis.

---
Automatische keurder, model `claude-sonnet-5-5`, 23283 tokens in, 3199 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
