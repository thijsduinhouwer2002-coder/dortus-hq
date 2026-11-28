# Keuring blender-gewrichten, plakkaart gratis 0.1.3, 28-11-2026, automatische keurder
Wat ik keurde: commit 4a4e2be49 (c5dd84e..4a4e2be): KAART.md, `plak-gratis-0.1.3.md`, `controle-gratis-0.1.3.sh`. De twee zips kreeg ik niet te zien.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De plakkaart doet wat het doel vraagt: oude 0.1.1 en 0.1.2 vervangen door 0.1.3 met de tenenfix, de meldknop en de reviewregel. Elke winkel krijgt de juiste zip, alleen extensions.blender.org krijgt de zip zonder Pro-knoppen. | Feit (uit de tekst) | hoog | n.v.t. |
| 2 | De sha256 van de direct-zip in de plakkaart (`7a943b69...680df`) is letterlijk gelijk aan die in het controlescript. | Feit | hoog | n.v.t. |
| 3 | De zips zelf en hun sha256 en groottes kon ik niet nakijken. Ze staan als GEZIEN, maar zijn niet meegestuurd. | Vermoeden dat ze kloppen | midden | `sha256sum` op beide zips in `uitgave/`; controlescript na het plakken |
| 4 | De zips komen uit f893c68 op een tak die nog niet op main staat. De releasenotes zeggen "uit CHANGELOG.md (0.1.3)", maar de getoonde CHANGELOG heeft nog geen 0.1.3-kop. | Vermoeden | midden | Controleren dat de tekst in `CHANGELOG.md` op `claude/blender-306` gelijk is aan het notitieblok in de plakkaart |
| 5 | Het akkoord van Daan (#326) en van de keurder op f893c68 staat in de plakkaart, maar ik zie dat niet in `ontwerp.md`. De keuring van deze plakkaart zelf is nog gevraagd, niet gegeven. | Feit (staat in KAART) | hoog | Daans ja op de plakkaart vóór ma 30 nov |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen testbestand aangepast. Geen code in de add-on gewijzigd, dus `architectuur.md` hoeft niet bij. Alle nieuwe bestanden zijn ruim onder 400 regels. | Feit | hoog | tests, 400 regels, architectuur.md |
| 2 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Alleen openbare winkel-URL's en repo-namen. | Feit | hoog | geen persoonsgegevens |
| 3 | Cijfers zijn gelabeld (GEZIEN met tijd en bron, "Effect op verkoop: GOK"). Dat is netjes. | Feit | hoog | GEZIEN/DERDEN/GOK |
| 4 | De extensions-zip is gescheiden van de direct-zip. Het manifest vraagt dezelfde toestemming als 0.1.1. Dat past bij de Blender-regels 6.1 en 6.3 uit het ontwerp. | Feit (uit de tekst) | midden | ontwerp.md, regels extensions.blender.org |
| 5 | De plakkaart doet iets dat de winkel moet verwerken: Thijs moet inloggen. De hoofdchat plakt, de keurder niet, en er staat een stopregel als een formulier iets anders vraagt. | Feit | hoog | geen eigen acties zonder toestemming |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De releasenotes hebben twee Fixed-regels over bijna hetzelfde: losse teenstukjes en de zool als los stuk. Dat leest als herhaling. | Eén regel van maken, bijvoorbeeld "A knee joint no longer leaves loose pieces of the toes or the sole of the foot." | klein |
| 2 | De volgorde in de notes (Fixed voor Added) wijkt af van `CHANGELOG.md` (Added voor Fixed). | Dezelfde volgorde aanhouden | klein |
| 3 | Gebruikers van 0.1.1 krijgen in één keer twee updates samen. De zin "voor het eerst naar de gebruikers" over de meldknop klopt niet voor Printables-gebruikers, want daar staat al direct-0.1.2. | Zin in de plakkaart corrigeren (de notes zelf zijn goed) | klein |

## Deel C: is het goed genoeg?
Er is geen beeld, video of nieuwe winkeltekst om naast een concurrent te leggen, alleen een versienummer, releasenotes en zips. Ik geef daarom geen cijfers. Ik kan uit tekst niet zien of de add-on of de winkelpagina's goed ogen. De blinde test is niet van toepassing, want er is geen hoofdbeeld of omslag. Het gedrag van de add-on is gekeurd op f893c68, dus niet in deze wijziging.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Plakkaart zegt "0.1.2 is nergens geplakt" en "nooit geplakt", maar dezelfde kaart noemt dat Printables direct-0.1.2 heeft (en `CHANGELOG.md` heeft 0.1.2 met datum). Herschrijf naar "in geen winkel behalve Printables".
2. Superhive Lite: de kaart zegt dat Lite "the same code as the free Click Joints 0.1.3 on extensions.blender.org" blijft, maar krijgt nu de direct-zip (met `direct.py`, drie sloten en "Upgrade to Pro") in plaats van de extensions-zip. Dat is een kleine onjuistheid op een winkelpagina (vermoeden: zo zou Daan of Thijs het zien). Pas de zin aan of laat de extensions-zip staan bij Lite.
3. Controlescript, Gumroad-regel: bij een lege of mislukte download meldt hij toch "GOED bereikbaar". De commentaarregel ("noemt geen oude versie") past ook niet bij de echte test ("print tested"). Voeg een `[ -s ]`-check toe en maak de uitleg gelijk.
4. Controlescript, extensions-regel: `grep "0\.1\.3"` kan ook andere getallen op de pagina raken (zoals "10.1.3"). Gebruik een strakker patroon, bijvoorbeeld `version.*0\.1\.3`. Het blijft WACHT of GOED, dus geen schade.
5. Controlescript controleert Printables en de zips van Gumroad en Superhive niet. Dat staat er eerlijk bij ("met het oog"). Zet het ook als eigen regel op de afvinklijst van de hoofdchat.
6. Notes-tekst: vergelijk de 711 tekens nog even met een echte teller. Ik schat het hoger (±730), nog steeds onder 1024.

---
Automatische keurder, model `claude-sonnet-5-5`, 23924 tokens in, 7931 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
