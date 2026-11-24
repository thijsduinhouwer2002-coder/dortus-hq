# Keuring Bison & Flex architectuur.md (bekende platformfouten), 24-11-2026, automatische keurder
Wat ik keurde: commit d7178439a (ddccb89..d717843), alleen `producten/jetbrains-bison-flex/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één alinea tekst in `architectuur.md`. Er is geen code, plugin.xml, winkeltekst of change-note aangepast, dus de belofte uit `ontwerp.md` en de akkoorden van Daan blijven onaangeraakt. | Feit | Hoog | Het bestandsoverzicht noemt alleen dit ene bestand. |
| 2 | De tekst zegt dat `bekendePlatformfouten` in `e2e/.../Gedeeld.kt` en `PlatformfoutTest.kt` bestaan. Die bestanden zitten niet in deze wijziging. | Vermoeden | Midden | Ze staan al in een eerdere commit. Dat blijkt als `git show` ze in de geschiedenis voor ddccb89 laat zien. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt met de nieuwe uitzondering in de IDE-test, met reden, voorwaarde en een weghaal-regel. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er wordt een fout in de IDE-test overgeslagen. Dat is geen aanpassing om te slagen, want de uitzondering is smal: alle stukjes van de regel moeten kloppen en `com.dortus` mag niet in de melding staan. Er staat een weghaal-regel bij en een nieuwe regel vraagt een run-nummer en een stack zonder regels van ons. | Feit (tekst), vermoeden (code) | Midden | Tests niet aangepast om te slagen |
| 3 | De claim is onderbouwd met twee run-nummers (45262737601 en 45305066655), als GEZIEN gemarkeerd, met IDE-versie 2025.2.6.4. Ik kan die runs zelf niet openen. | Feit (er staat GEZIEN), vermoeden (juistheid) | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3a | De zin "kan van de keurder, Chris 24 nov" zegt wie het goedkeurde. Dat kan ik niet controleren. | Vermoeden | Laag | Een bericht of keuring van Chris op 24 nov zou het bevestigen. |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | Het bestand blijft ruim onder de ±400 regels (ongeveer 82 regels). | Feit | Hoog | Bestanden onder ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niets te zien of te spelen, want de wijziging is alleen documentatie. | Niet van toepassing. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- De kop van `architectuur.md` zegt nog "Stand 8 nov 2026: versie 0.2", terwijl 2026.1.2 al is uitgebracht. Werk die regel bij zodat de stand klopt.
- Controleer dat `Gedeeld.kt` en `PlatformfoutTest.kt` al in de geschiedenis staan (Deel A, punt 2). Zo ja, dan klopt de tekst. Zo nee, dan beschrijft hij code die er niet is.
- Het overslaan van een fout in de IDE-test blijft een risico: een echte fout met dezelfde tekst zou ook worden overgeslagen. De voorwaarde "geen `com.dortus`" en de weghaal-regel dempen dat. Kijk bij elke nieuwe IDE-versie of de regel weg kan.

---
Automatische keurder, model `claude-sonnet-5-5`, 18627 tokens in, 2449 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
