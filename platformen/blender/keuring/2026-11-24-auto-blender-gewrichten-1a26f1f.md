# Keuring blender-gewrichten (KAART.md), 24-11-2026, automatische keurder
Wat ik keurde: commit 1a26f1f1c (bereik 9e2c417..1a26f1f), bestand `producten/blender-gewrichten/KAART.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging is één nieuw tekstbestand, een weekkaart. De opdracht (`ontwerp.md`) vraagt hier niets over, dus ik toets op consistentie met `ontwerp.md`, en niet op functie.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De kaart is kort en bevat doel, team, lat, voordeel, winkelstand en actie. Dat past bij een kaart per product. | Feit | Hoog | n.v.t. |
| 2 | "Ons voordeel: de enige die vanuit je rig automatisch scharnieren en kogels met eindstop maakt" is een absolute claim. `ontwerp.md` noemt Cut Flex met 15 gewrichtsvormen en Cleave met kogelgewrichten, en geeft geen bron voor "de enige". | Vermoeden | Midden | Een nagekeken vergelijking met Cleave, Cut Flex en CatPin (in `organisatie/lat/click-joints-pro.md`). |
| 3 | "Klaar om te plakken: 1.2.7". In `ontwerp.md` staat een akkoord van Daan voor Pro 1.2.6, maar ik zie er geen voor 1.2.7 of 1.2.8. | Vermoeden | Midden | Een keuring of akkoord voor 1.2.7 voordat het live gaat (zie "Daan: kniefout" en volgende keuringen). |
| 4 | De winkelstand (versie 1.2.3, prijzen) staat niet in de meegestuurde tekst en is niet te controleren. | Vermoeden | Laag | De live winkelpagina's bekeken met curl. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests of code aangepast. Het bestand is 12 regels. | Feit | Hoog | Tests niet aangepast, bestanden onder ±400 regels |
| 2 | Er zijn geen persoonsgegevens, sleutels of wachtwoorden. De Gumroad-link is een openbare winkel-URL. | Feit | Hoog | Geen persoonsgegevens |
| 3 | Cijfers staan zonder GEZIEN, DERDEN of GOK: prijzen $19/$24/$59 en $12/$45/$3, "1 verkocht ($19, 22 nov)" en de blindtestscores "Gemini 2,0, ChatGPT 2,0". | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | `architectuur.md` is niet bijgewerkt. Dat hoeft ook niet, want er is geen code veranderd. | Feit | Hoog | architectuur.md bijgewerkt |
| 5 | De kaart verwijst naar `organisatie/lat/click-joints-pro.md` en `organisatie/blindtest/uitslag/`. Of die bestanden bestaan, kan ik uit de wijziging niet halen. | Vermoeden | Laag | Controle dat de paden bestaan |
| 6 | De kaart noemt in de zin "Blinde test" dat het hoofdbeeld op plek 2 staat. Dat is eerlijk en past bij de regel dat een beeld zonder GESLAAGD niet akkoord is. | Feit | Hoog | Blinde test voor hoofdbeelden |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Dit is een intern document, er valt niets te zien of te spelen.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een lezer van de kaart ziet niet welke taak of welk issue nu als eerste komt. | Eén regel "Eerst: ..." bovenaan. | Klein |

## Deel C: is het goed genoeg?
Geen klantbeeld, video, winkeltekst, spel of site in deze wijziging. De blinde test is hier niet van toepassing en ik geef geen cijfers. Voor de beelden die de kaart noemt, geldt dat zonder uitslag GESLAAGD het akkoord nee blijft.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet GEZIEN, DERDEN of GOK achter de prijzen, de verkoopstand en de blindtestscores (deel B 3).
- Verzacht of onderbouw "de enige die ..." (deel A 2). Gebruik het pas in een winkeltekst na controle tegen Cleave, Cut Flex en CatPin.
- Laat 1.2.7 en 1.2.8 pas live gaan na een eigen keuring (deel A 3).
- Controleer of de twee verwezen paden bestaan (deel B 5).
- Voeg bovenaan één regel toe met wat nu als eerste moet (deel C).

---
Automatische keurder, model `claude-sonnet-5-5`, 18361 tokens in, 3055 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
