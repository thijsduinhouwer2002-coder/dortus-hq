# Keuring blender-gewrichten (akkoord Pro 1.2.8 in ontwerp.md), 25-11-2026, automatische keurder
Wat ik keurde: commits 278f40c..08eaf88 (08eaf8887), bestand producten/blender-gewrichten/ontwerp.md
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt alleen één regel met "Akkoord: ja" voor Pro 1.2.8 toe bovenaan ontwerp.md, in dezelfde vorm als de oudere regels. Er is geen code of beeld aangepast. | Feit | Hoog | De diff zelf. |
| 2 | De regel verwijst naar `platformen/blender/keuring/2026-11-25-pro-1.2.8-uitbrengen-daan.md`. Dat bestand zit niet in deze wijziging, dus ik kan niet nagaan of het bestaat en of het ja daar onderbouwd is. | Vermoeden | Midden | Het bestand openen en kijken of het "Akkoord: ja" en de punten uit #37 noemt. |
| 3 | Run 45526260663, de sha256 (c3daa159...e4af) en "main 278f40c" staan als GEZIEN. Ik zie alleen de tekst, dus ik kan niet bevestigen dat de zip bij die run en die hash hoort. | Vermoeden | Midden | De zip ophalen uit de run en `sha256sum` vergelijken met de volledige hash. |
| 4 | "Moet 1 en 2 uit #37 zijn gedaan" is een bewering zonder bewijs in deze wijziging. | Vermoeden | Laag | De moet-punten van #37 naast de commits op main 278f40c leggen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast en geen code gewijzigd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | architectuur.md hoefde niet bij te werken, want er is geen code veranderd. Of dat voor 1.2.8 zelf bij 278f40c is gebeurd, zie ik hier niet. | Vermoeden | Midden | architectuur.md bijgewerkt |
| 3 | Persoonsgegevens, sleutels of wachtwoorden staan niet in de toegevoegde regel. | Feit | Hoog | Geen persoonsgegevens |
| 4 | Het cijfer (sha256) heeft het label GEZIEN. De herkomst staat erbij, maar ik kan hem niet controleren. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | ontwerp.md is vermoedelijk veel langer dan 400 regels. Het is een lopend logboek, dus dat was al zo. | Vermoeden | Laag | Bestanden onder ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | In deze wijziging is niets te zien of te spelen, dus hier valt niets over de speler of koper te zeggen. | Niet van toepassing. De knie met kniekap en de enkels van 1.2.8 vragen een eigen keuring op beeld. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing op deze wijziging: er zit geen beeld, winkeltekst of build in, dus ook geen blinde test. Ik geef geen cijfers, want die zouden verzonnen zijn. Het product Pro 1.2.8 zelf valt buiten wat ik zie.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- Geen.

**Kan**
- Neem het keuringsbestand voor 1.2.8 en de moet-punten van #37 in dezelfde commit op, of verwijs naar de commit waarin ze staan. Dan kan een volgende keurder het ja nalopen.
- Leg de sha256 volledig vast, niet afgekort, zodat de zip te controleren is.
- Controleer voor het live zetten op Superhive dat een agent de release keurde. Dat blijft nodig, ook na het ja van Daan.
- De kop van ontwerp.md zegt nog "Nog niet beoordeeld door Daan" en "v1.2". Dat is verouderd en kan worden bijgewerkt.

---
Automatische keurder, model `claude-sonnet-5-5`, 18330 tokens in, 2784 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
