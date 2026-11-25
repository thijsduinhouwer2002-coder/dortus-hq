# Keuring blender-gewrichten, 25-11-2026, automatische keurder
Wat ik keurde: commits a3c1ea1..c4f14e5 (c4f14e537, Click Joints Pro 1.2.9, issue 70), alleen de tekst van de diff
Akkoord: ja

## Deel A: doet het wat beloofd is?
Toetssteen: de commitbelofte "winkellinks in betaald/, kern noemt Pro nergens". Dat staat niet in `ontwerp.md`, maar wel in de regels voor de gratis build.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | In `meld.py` en `paneel.py` zijn `BEOORDEEL_PRO`, `beoordeel_links`, `_naam` en de woorden "Pro-deel", "Superhive" en "Gumroad" weg. De kern heeft nu alleen `BEOORDEEL_GRATIS` en een lijst `BEOORDEEL`. | Feit (diff) | Hoog | Een zoekopdracht op "Pro", "Superhive" en "Gumroad" in de gratis zip. De toets `toets_zips.py` doet dat, maar de uitslag staat niet bij de wijziging. |
| 2 | `betaald/__init__.py` zet bij register `meld.BEOORDEEL[:] = WINKELS` (Superhive en Gumroad). Bij unregister zet hij `BEOORDEEL_GRATIS` terug. Zo krijgt Pro dezelfde twee knoppen als voorheen. | Feit (diff) | Hoog | De Pro-e2e laat in het paneel twee knoppen zien na een Good fit. |
| 3 | De gratis build toont nog één knop naar Blender Extensions. De zin "Happy with it? Leave a rating:" is niet veranderd. | Feit (diff) | Hoog | Groene e2e in 4.2.23, 5.2.3 en 5.3.0. |
| 4 | Een draai van de e2e zit niet bij de wijziging. Of de nieuwe toetsen echt slagen, zie ik dus niet. | Vermoeden | Midden | Een groene run op c4f14e5 voor zowel de gratis als de Pro-zip. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toetsen zijn aangepast aan de nieuwe vorm van de code (`beoordeel_links(naam)` is nu `BEOORDEEL`). Het zijn dezelfde twee eisen en geen versoepeling. De gratis-toets leest nu wel de constante `BEOORDEEL_GRATIS` en niet meer het echte gedrag van de gratis build, dus hij is zwakker. | Feit | Hoog | Tests niet aanpassen om te slagen: hier geen overtreding, wel een kan. |
| 2 | De gekeurde hashes van `meld.py` en `paneel.py` zijn bijgewerkt, met een uitleg in de toets (nieuwe regel van 25 nov). De wijziging in `paneel.py` is alleen commentaar. De nieuwe hashes kan ik niet narekenen. | Feit voor de bewuste update, vermoeden voor de juistheid | Midden | Gekeurde kern. Bevestigd als `toets_zips.py` groen draait. |
| 3 | `architectuur.md` is niet meegewijzigd. De kernbeschrijving van `meld.py` en `paneel.py` kan nu kloppen of verouderd zijn: de zichtbare tekst noemt de beoordeel-regel niet. Het gedeelte over de plekken in `paneel.py` en over `betaald/__init__.py` is afgekapt. | Vermoeden | Laag | `architectuur.md` bijwerken. |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. De Gumroad-link bevat een winkelnaam, en die link is bedoeld om openbaar te zijn. | Feit | Hoog | Geen persoonsgegevens. |
| 5 | De wijziging raakt alleen kleine bestanden. Maar de toetsbestanden zijn niet geteld. | Vermoeden | Laag | Bestanden onder ±400 regels. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Dit is een omzetting zonder zichtbare verandering voor de gebruiker, en ik kan geen scherm zien.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Pro en gratis tonen dezelfde "Happy with it?"-regel, in de gratis build met één knop. Dat is rustig en past in een smalle zijbalk. Of het er netjes uitziet, kan ik uit tekst niet zien. | Iris of Daan bekijken het scherm van Pro met twee knoppen naast elkaar in de zijbalk. | Klein |

## Deel C: is het goed genoeg?
Niet van toepassing. Er is geen hoofdbeeld, omslag, thumbnail, winkeltekst of spelwijziging, dus geen blinde test nodig. Ik geef geen cijfers, want ik kan niets zien of spelen. Een keuring op beeld blijft aan Daan en Iris.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- Geen.

**Kan**
- Maak de gratis-toets sterker: laat hem de echte lijst `meld.BEOORDEEL` lezen in de gratis build. Toets ook dat unregister van Pro de lijst terugzet op `BEOORDEEL_GRATIS`.
- Werk `architectuur.md` bij: de beoordeel-regel en de lijst `BEOORDEEL`, die `betaald/__init__.py` vult.
- Uitbrengen van 1.2.9 vraagt een eigen "Akkoord: ja" van Daan. In `ontwerp.md` staat het laatste ja voor 1.2.8.
- Dit oordeel geldt pas als de e2e voor gratis en Pro groen is op c4f14e5.

---
Automatische keurder, model `claude-sonnet-5-5`, 22454 tokens in, 4929 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
