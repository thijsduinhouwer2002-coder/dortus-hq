# Keuring jetbrains-bison-flex pluginversie uit versie.txt, 19-11-2026, automatische keurder
Wat ik keurde: commit 0e8dd720 (7528aea..0e8dd72), alleen de tekst van de wijziging
Akkoord: ja

## Deel A: doet het wat beloofd is?
De commit belooft de interne API weg te halen, zodat Plugin Verifier weer groen wordt. De meldlink moet daarbij nog dezelfde pluginversie krijgen. De opdracht (`ontwerp.md`) noemt de meldknop zelf niet.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `PluginManagerCore.getPlugin` en `PluginId` zijn uit `Melden.kt` verdwenen en vervangen door het lezen van `/bisonflex/versie.txt`. | Feit | Hoog | Niet nodig, het staat in de diff. |
| 2 | Of de Plugin Verifier hierdoor groen wordt, is uit de tekst niet te zien. Er kan ergens anders nog een interne API gebruikt worden. | Vermoeden | Midden | Een nieuwe verifier-run tegen IDEA 2026.2 zonder "internal API usage". |
| 3 | `processResources` vult `${versie}` in met `project.version`. Dat klopt alleen als de versie in `build.gradle.kts` boven dit blok is gezet. Anders komt er "unspecified" in. | Vermoeden | Midden | De nieuwe test in `MeldenTest` (regex `\d{4}\.\d+\.\d+`) in een groene run. |
| 4 | De terugval naar "unknown" voor een niet ingevulde `$`-tekst is verstandig. Een melding zonder versie blijft zo mogelijk. | Feit | Hoog | Niet nodig. |
| 5 | Daans akkoord geldt niet voor de meldknop en error handler van R5. Dit commit zit in dat nog niet gekeurde stuk. | Feit | Hoog | `Akkoord: ja` van Daan voor een commit na eb02ba1. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is strenger gemaakt (een assert op de versie erbij), niet versoepeld. | Feit | Hoog | Tests niet aangepast om te slagen: in orde. |
| 2 | `architectuur.md` is bijgewerkt voor de nieuwe bron van de versie, met reden en run-nummer. | Feit | Hoog | architectuur.md bijgewerkt: in orde. |
| 3 | De bewering dat Plugin Verifier de oude aanroep afkeurde in een bepaalde run heeft geen label (GEZIEN of DERDEN). | Feit | Midden | Cijfers en beweringen met label: klein gebrek. |
| 4 | `architectuur.md` noemt nog versie 2026.1.1 voor `plugin.xml` en "versie 0.2" in de kop, terwijl er al 2026.1.2 is. | Feit | Midden | architectuur.md bijgewerkt: verouderd, niet door deze commit. |
| 5 | In `architectuur.md` staat een GitHub-accountnaam die waarschijnlijk een echte naam bevat (niet overgeschreven). De regel bestond al. | Vermoeden | Laag | Geen persoonsgegevens: even nakijken of dit openbaar mag. |
| 6 | De gewijzigde bestanden zijn klein, ruim onder de 400 regels. | Feit | Hoog | Bestandsgrootte: in orde. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Plugin Verifier opnieuw draaien en de groene run bij de commit zetten (A2).
- Controleren dat `version` in `build.gradle.kts` boven het nieuwe `processResources`-blok staat, of laten bevestigen door de groene test (A3).
- Voor uitbrengen laat Daan de meldknop en error handler van R5 keuren. Zijn akkoord dekt die nu niet (A5).
- Bij de run-claim in `architectuur.md` een label zetten, bijvoorbeeld GEZIEN met datum (B3).
- De verouderde versieregels in `architectuur.md` bijwerken (B4).
- De accountnaam in `architectuur.md` nakijken (B5).

---
Automatische keurder, model `claude-sonnet-5-5`, 22090 tokens in, 3391 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
