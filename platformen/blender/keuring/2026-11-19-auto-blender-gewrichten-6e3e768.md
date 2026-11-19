# Keuring blender-gewrichten gratis 0.1.2, 19-11-2026, automatische keurder
Wat ik keurde: commits 804ae3d..6e3e768 (6e3e768a, tak claude/blender-0.1.2b)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Manifest staat op versie 0.1.2 en de CHANGELOG heeft een sectie "0.1.2 (unreleased)" met drie regels (Added, Changed, Fixed). Dat past bij elkaar en binnen de limiet van 5 regels per versie. | Feit (uit de diff) | hoog | n.v.t. |
| 2 | De nieuwe tagline is 58 tekens, zonder punt, noemt "poseable" en "bend range" en verwijst niet naar de betaalde versie. Dat past bij de eisen van extensions.blender.org (3.3, 3.10). | Feit (geteld en gelezen) | hoog | n.v.t. |
| 3 | Meldingen beginnen nu met wat je moet doen: "Click Make watertight first", "Not watertight, use Make watertight", "Pick a spot where the limb is free" en "Click Place joint in the 3D viewport". Bij "Joint placed." staan passing en Auto-noot voor de tijd. De f-strings zijn syntactisch in orde. | Feit (uit de diff) | hoog | n.v.t. |
| 4 | De CHANGELOG zegt dat de statusbalk het nuttige deel niet meer afknipt. Die uitwerking in de echte Blender heb ik niet gezien, en de eerste 40 tekens worden alleen met een tekstzoeker in de zip gecontroleerd. | Vermoeden | midden | Een scherm van de statusbalk in 4.2 en 5.2 met een lange melding, bijvoorbeeld uit de schermen-test. |
| 5 | De Fixed-regel over de zool van de voet (een_lid.py) en de meldknop (meld.py) zitten niet in deze diff. Ze zitten vermoedelijk al in de basis (main), dus ik kan ze hier niet keuren. | Vermoeden | midden | De diff vanaf de vorige gekeurde stand, of een groene Blender-run met de voet-test van Chris (army_man). |
| 6 | Er wordt geen Blender-run (4.2.23, 5.2.3) genoemd voor 0.1.2, alleen "toets_zips lokaal 0 FOUT". Die toets vergelijkt bestands-hashes en tekst, geen gedrag. Het risico is klein, want alleen meldteksten veranderden. | Feit (geen run vermeld) | hoog | Een groene run van de e2e-workflow op 6e3e768, met name als een toets de oude meldtekst vergelijkt. |
| 7 | De akkoord-regel bovenaan ontwerp.md geldt voor 0.1.1 en Pro 1.0.2, niet voor 0.1.2. De teksten in het paneel en de meldingen zijn uiterlijk, dus Daan hoort er nog een ja op te zetten. | Feit | hoog | Een nieuwe "Akkoord: ja" voor 0.1.2 in ontwerp.md. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De hashes in toets_zips.py zijn bewust bijgewerkt, met een datumregel waarin de reden staat. Er zijn vier extra controles bijgekomen (versie, tagline, meldingen vooraan), dus de test is niet verslapt. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | Het label "gelijk aan de gekeurde stand 014172e" klopt niet meer, want de hashes horen nu bij nieuwe inhoud. Dit is verwarrend maar niet fout. | Feit | hoog | Duidelijke naamgeving |
| 3 | architectuur.md is niet aangepast, terwijl de meldteksten in gewricht.py, een_lid.py en gesloten.py zijn veranderd. De tekst daar noemt de meldingen grotendeels niet letterlijk. | Vermoeden | laag | architectuur.md bijgewerkt |
| 4 | betaald/scharnier.py is gewijzigd: alleen de meldtekst, maar in de betaalde build. Als de Pro-zip uit dezelfde bron komt, is hij niet meer byte voor byte gelijk aan de gekeurde Pro 1.0.2. Of toets_zips die zip vastpint, zie ik niet. | Vermoeden | midden | Gekeurde zip blijft de zip die uitgebracht wordt |
| 5 | Bestandsgrootte (±400 regels) kan ik uit de diff niet halen. gewricht.py staat in de architectuur al als groot genoemd. | Vermoeden | laag | Bestanden onder ±400 regels |
| 6 | Er is geen sleutel of wachtwoord in de diff. In blender_manifest.toml staat een zakelijk contactadres van de maker (niet nieuw, bedoeld als openbaar). | Feit | hoog | Geen persoonsgegevens |
| 7 | Er is geen AI-beeld of -geluid, geen cijferclaim en geen spelerstekst in deze wijziging. | Feit | hoog | Cijfers, Hats, Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet een "Akkoord: ja" van Daan voor 0.1.2 in ontwerp.md voordat de zip naar extensions.blender.org gaat (A7).
- Laat de e2e-run in 4.2.23 en 5.2.3 groen draaien op 6e3e768 voor het uitbrengen (A6).
- Zet een scherm van de statusbalk met een lange melding bij de keuring (A4).
- Pas het label "gekeurde stand 014172e" in toets_zips.py aan naar de nieuwe stand (B2).
- Controleer of de Pro-zip na de scharnier.py-wijziging een nieuwe versie of nieuwe hashes nodig heeft (B4).
- Controleer dat `re` bovenaan toets_zips.py geïmporteerd is. Dat zie ik niet in de diff, maar volgens de commit draait de toets zonder fouten.
- Controleer dat `click-joints-uitgave.yml` de kop "## 0.1.2 (unreleased)" goed leest (voorheen "## Unreleased"), en zet bij het uitbrengen de datum erin.

---
Automatische keurder, model `claude-sonnet-5-5`, 22420 tokens in, 6319 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
