# Keuring blender-gewrichten, 19-11-2026, automatische keurder
Wat ik keurde: commit 281d0a3b (3424f23..281d0a3), alleen `producten/blender-gewrichten/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt één alinea toe aan `architectuur.md`. De add-on, het ontwerp en de beloofde functies blijven gelijk. Het ja van Daan voor 0.1.1 en 1.0.2 (tak `claude/blender-een-lid` 4b7e722) wordt dus niet geraakt. | Feit | hoog | De lijst met gewijzigde bestanden bevat alleen dit ene bestand. |
| 2 | Het commitbericht noemt ook maskers voor kluisnaam en melding in Rollwright, een verslag naast de schermen en een oorzaak voor Chris. In deze diff staat daar niets van. Of dat werk elders zit of in het bericht te veel wordt beweerd, kan ik niet zien. | Vermoeden | midden | De volledige bestandslijst van 281d0a3b, met `organisatie/controle/beelden.sh`, `beeldvergelijk.py` en Rollwright. |
| 3 | De alinea beschrijft een weektest op maandag 04:37 NL en een beeldvergelijking met een grens van 0,02 procent van de pixels. Of `week-test.yml` en de stap "Beeldvergelijking" dat echt doen, kan ik niet nagaan, want die bestanden zitten niet in de diff. | Vermoeden | midden | `.github/workflows/week-test.yml`, `beelden.sh` en een groene weekrun met artefact `beeldverschil-blender-gewrichten-<versie>`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt voor deze wijziging, met een nieuwe alinea over week-test en beeldvergelijking. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | Het bestand is door de afkapping niet volledig te zien. Het is waarschijnlijk lang, maar het aantal regels weet ik niet. Er komen 2 regels bij. | Vermoeden | laag | Bestanden onder ±400 regels |
| 4 | In de diff staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit | hoog | Geen persoonsgegevens |
| 5 | "Blender tekent zonder ruis" en "nu 5.4.0-alpha" staan er zonder GEZIEN of GOK. Het zijn technische stellingen, geen marktcijfers. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | Er is geen spelerstekst van Hats en geen AI-beeld of -geluid. | Feit | hoog | Hats en Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij "Blender tekent zonder ruis" en bij de grens van 0,02 procent een label. Dat kan GEZIEN zijn met het runnummer waarop de grens is gemeten.
- Controleer of het commitbericht klopt met de inhoud. De Rollwright-maskers en het verslag staan niet in deze diff. Als ze in een andere commit zitten, moet die apart gekeurd worden.
- De kop van `architectuur.md` zegt nog "v0.1, gratis kern", terwijl de gratis versie nu 0.1.1 is. Werk dat bij als je er toch aan zit.

---
Automatische keurder, model `claude-sonnet-5-5`, 17757 tokens in, 2284 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
