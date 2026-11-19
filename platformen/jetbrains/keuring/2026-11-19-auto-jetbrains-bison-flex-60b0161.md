# Keuring jetbrains-bison-flex e2e vaste dialoogmaat, 19-11-2026, automatische keurder
Wat ik keurde: commit 60b01616 (reeks 6fb8de8..60b0161), 4 bestanden: architectuur.md, Gedeeld.kt, Hernoemen.kt en IdeTest.kt
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is `ontwerp.md` van Bison & Flex. Deze wijziging raakt alleen de e2e-test en de documentatie, geen plugincode of winkeltekst.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De belofte (gratis en Pro-functies, tekst in `plugin.xml`) verandert niet, want de diff bevat geen productcode. | Feit | Hoog | Niets nodig: de lijst gewijzigde bestanden bevat alleen e2e en `architectuur.md`. |
| 2 | Nieuwe `vastVenster()` zet de dialoog op `kleurenpagina` (2000x1400) en `hernoem-conflict` (1600x1174) op een vaste maat. Dat past bij het doel van R4: minder beeldruis tussen runs. | Feit dat de code dit doet, vermoeden dat het de ruis weghaalt | Midden | Een groene e2e-run met `beeldverschil` onder de grens van 0,3 procent op beide plaatjes, in twee runs achter elkaar. |
| 3 | De commit zegt "verschuiving over het hele maatverschil", maar `beeldvergelijk.py` staat niet in de gewijzigde bestanden. De doc noemt verschuiving als bestaand gedrag. | Vermoeden | Midden | De inhoud van `organisatie/controle/beeldvergelijk.py` en de vorige commit. Staat de verschuiving er al, dan klopt alleen het commitbericht niet. |
| 4 | Dit raakt geen zichtbaar werk voor gebruikers, dus een nieuw oordeel van Daan is niet nodig. Het Akkoord van Daan blijft staan. | Feit | Hoog | Niets nodig. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen controle of de test faalt; alleen de schermmaat wordt vastgezet. Er is niets afgezwakt. | Feit | Hoog | Tests niet aangepast om te slagen: ok |
| 2 | `architectuur.md` is bijgewerkt met de vaste maten, de reden en het runnummer. | Feit | Hoog | architectuur.md bijgewerkt: ok |
| 3 | Het runnummer 44441843802 heeft de markering GEZIEN. Bij de tekst over het verschuiven staat geen bron. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK: grotendeels ok |
| 4 | `vastVenster()` zegt "nooit de IDE zelf", maar de code controleert dat niet. Is bij de aanroep in `IdeTest.kt` het actieve venster toevallig de IDE, dan zou de IDE worden verkleind. Dat zou het IDE-scherm van 2880x1800 en de maskers breken. | Vermoeden | Midden | Robuustheid van de test: kan |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | Hoog | Geen persoonsgegevens: ok |
| 6 | Bestandslengtes van `IdeTest.kt` en `Gedeeld.kt` staan niet in de tekst. De wijziging is klein (maximaal 11 regels erbij). | Vermoeden | Laag | Regelaantal van beide bestanden: onder ±400 regels? |
| 7 | Geen AI-beeld, geen spelerstekst en geen Steam-onderdelen in deze wijziging. | Feit | Hoog | Overige regels: niet van toepassing |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Laat `vastVenster()` niets doen als `actiefVenster()` de IDE zelf is. Dan kan de test de IDE niet per ongeluk verkleinen (Deel B 4).
- Controleer of `beeldvergelijk.py` de verschuiving inderdaad al doet, of pas het commitbericht aan (Deel A 3).
- Bevestig met twee groene e2e-runs dat de ruis onder 0,3 procent komt (Deel A 2). Dat kan ik uit tekst niet zien.
- Controleer de bestandslengtes van `IdeTest.kt` en `Gedeeld.kt` (Deel B 6).

---
Automatische keurder, model `claude-sonnet-5-5`, 22508 tokens in, 3059 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
