# Keuring blender-gewrichten KAART.md, 24-11-2026, automatische keurder
Wat ik keurde: commit 8fcde9ebb (b2eccf6..8fcde9e), alleen `producten/blender-gewrichten/KAART.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De commit belooft "kaart bij". De regel "Klaar om te plakken" is bijgewerkt met 1.2.8, winkeltekst B3 en de e2e-stand. | Feit | Hoog | Het diff zelf. |
| 2 | De uitspraak "winkeltekst B3 GESLAAGD, plek 1,0 bij beide rechters" kan ik niet nalezen. `pro-winkeltekst-b3.md` en de blindtest-uitslag zitten niet in de wijziging. | Vermoeden | Laag | Het bestand `platformen/blender/pro-winkeltekst-b3.md` en de uitslag in `organisatie/blindtest/uitslag/`. |
| 3 | 1.2.8 staat op main, maar 4.2 is rood (wisselende boolean op army_man, issue #14). Het ja van Daan voor 1.2.6 steunde op groen in 4.2.23, 5.2.3 en 5.3.0. Voor 1.2.8 is nog geen groen op alle drie. | Feit (volgens de kaart) | Midden | Een groene herstart van de 4.2-job. |
| 4 | De kaart zegt dat 1.2.8 en B3 nog wachten op Daan en de uitgave-run. Er wordt dus niets uitgebracht. | Feit | Hoog | Het diff. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het diff raakt geen code, geen tests en geen persoonsgegevens. De Gumroad-link is een publieke winkellink. | Feit | Hoog | Geen persoonsgegevens, tests niet aangepast. |
| 2 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet: er is geen codewijziging in deze commit. | Feit | Hoog | architectuur.md bijgewerkt. |
| 3 | Cijfers als "plek 1,0", "Gemini 2,0, ChatGPT 2,0", "1 in totaal ($19, 22 nov)" hebben geen label GEZIEN, DERDEN of GOK. Dat was in de oude regels van de kaart ook al zo. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK. |
| 4 | Het tijdstip "24 nov 23:00" in de kaart ligt na de keuringstijd (22:40 NL). | Feit | Midden | Is dit een typefout, of de tijd waarop de agent de uitgave verwacht? |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De wijziging is een interne statuskaart en een klant ziet er niets van. Er is niets om te zien of te spelen. | Niet van toepassing. | Klein |
| 2 | De blinde test adviseert een gedetailleerd personage in plaats van de tekenpop, plus tekst op elk beeld. De cover in de winkel (tekenpop) is nog niet aangepast. | Dat advies als eerstvolgende winkelwerk plannen. | Midden |

## Deel C: is het goed genoeg?
Deze commit verandert niets wat een klant ziet. De winkeltekst B3 zelf zat niet in de wijziging, dus ik geef geen cijfers. Daarom blijft het akkoord ja voor deze kaartwijziging. Voor het live zetten van B3 of 1.2.8 is nog een aparte keuring nodig, met de tekst erbij en cijfers per vraag.
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | geen cijfer | Tekst niet meegestuurd. |
| Zou ik het zelf kopen of bekijken op basis van dit? | geen cijfer | Tekst niet meegestuurd. |
| Zou Thijs er trots op zijn? | geen cijfer | Tekst niet meegestuurd. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Leg de uitslag van de blinde test voor B3 bij de wijziging, zodat "GESLAAGD, plek 1,0" na te lezen is (vermoeden tot dan).
- Zet bij de cijfers op de kaart GEZIEN, DERDEN of GOK.
- Controleer het tijdstip "23:00" in de kaart.
- Zet 1.2.8 pas live na een groene 4.2-run (issue #14) en het ja van Daan (issue #11). Dat is de voorwaarde uit het eerdere akkoord.

---
Automatische keurder, model `claude-sonnet-5-5`, 18250 tokens in, 2858 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
