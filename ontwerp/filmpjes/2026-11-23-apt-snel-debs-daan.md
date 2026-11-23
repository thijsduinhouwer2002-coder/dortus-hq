# Keuring apt-snel.sh met bewaarde .deb-bestanden (Olaf, 825ffda), 23 nov 2026 ±23:25 NL, Daan
Wat ik keurde: `commercie/filmpjes/apt-snel.sh`, `.github/workflows/apt-snel-proef.yml`, uitslag run 45268193244 (volgens Olaf)
Akkoord: ja (veilig), met M1 voordat de regisseur-workflows het overnemen

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigt of weerlegt |
|---|---|---|---|---|
| A1 | **Een verouderde of kapotte bewaarde map geeft geen kapotte installatie.** Toets hier op Ubuntu 24.04 met dezelfde opties (`Dir::Cache::Archives`, `Sandbox::User=root`, `Keep-Downloaded-Packages`): een beschadigde cowsay .deb met de juiste naam haalt apt gewoon opnieuw van de spiegel (hash klopt niet), een bestand met een oude versie in de naam laat apt links liggen (GEZIEN) | feit | hoog | eigen toets |
| A2 | Is de pakketlijst van de runner ouder dan de map, dan wil apt een oudere versie die misschien niet meer op de spiegel staat; dan faalt poging 1 en doet de terugval update plus opnieuw. Werkt, alleen trager | vermoeden | midden | een run na een image-wissel |
| A3 | **Cachesleutel:** bij een exacte treffer bewaart actions/cache niets nieuws. De sleutel hangt alleen aan de hash van het script. Komt er een nieuw runner-image (ongeveer wekelijks) met nieuwere versies, of zet je een pakket bij in de lijst, dan haalt elke run die van de spiegel en komt het nooit in de bewaarde map. De winst zakt dan stil weg tot iemand het script wijzigt | feit (zo werkt actions/cache) | hoog | `apt-snel: van de spiegel gehaald: N` in de log groeit na een image-wissel |
| A4 | trap met chown en lock weg: nodig zodat de cache-stap de map kan lezen; goed | feit | hoog | |

## Deel B: regels
Geen geld (actions/cache is gratis), geen persoonsgegevens, cijfers GEZIEN. Proef draait bij elke push op die twee bestanden: prima.

## Moet / Kan
- **M1:** sleutel ook op de pakketlijst en het runner-image, bijvoorbeeld een stap `echo "img=$ImageOS-$ImageVersion" >> "$GITHUB_OUTPUT"` en dan `key: apt-debs-filmpjes-v1-${{ steps.<id>.outputs.img }}-${{ hashFiles(script) }}-${{ hashFiles(bestand met pakketlijst) }}` (of de lijst in de sleutel via een stap-uitvoer). restore-keys blijft zoals het is, dan begint een nieuwe sleutel met de oude map en hoeft alleen het verschil van de spiegel.
- K1: map groeit met oude versies (Keep-Downloaded-Packages); na een paar wissels kun je in de vul-stap `apt-get autoclean` met dezelfde Archives-optie draaien, maar pas als de map boven ±500 MB komt.
