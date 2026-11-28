# Keuring blender-gewrichten, 28-11-2026 16:11 NL, automatische keurder
Wat ik keurde: commit 5cac9041c (e360a04..5cac904), alleen `producten/blender-gewrichten/KAART.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging is een statusnotitie bij #380 (sleeplink). Er is geen code of beeld veranderd. Ik toets de notitie aan de rest van de tekst.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De notitie meldt "Daan ja (8, #398)" en "klaar om te plakken gemeld in hoofdchat 15:12". In de meegestuurde tekst staat geen keuringsbestand van Daan voor #398 en ook niet het hoofdchatbericht. | Vermoeden | Midden | `berichten/hoofdchat.md` van 28 nov 15:12 en de keuring van Daan #398. |
| 2 | De notitie noemt tijden die na het keurmoment (16:11) liggen: "curl 16:15", "#380 dicht 28 nov 16:20" en "merge-tree 16:15". | Feit dat ze later zijn dan 16:11. Of dat een fout is, is vermoeden (tijdzone of voorgeschreven tijd). | Midden | De committijd van 5cac904 en de tijdzone van de notitie. |
| 3 | De sleeplink is getest met versie 0.1.1, en de notitie zegt dat een oudere link "niet gevonden" geeft. De CHANGELOG noemt 0.1.2 al op 26 nov. Staat 0.1.2 al op de winkel, dan werkt een link naar 0.1.1 niet meer. | Vermoeden | Midden | `curl` op de pagina van Click Joints op extensions.blender.org: welke versie is live, en werkt de link nog? |
| 4 | De notitie zegt dat README en dortus.com nog niet zijn bijgewerkt (curl, GEZIEN). Dat klopt met "klaar om te plakken": er is nog niets live dat ik kan nakijken. | Feit volgens de notitie, door mij niet nagekeken | Midden | Dezelfde `curl` op de README. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is alleen één regel in een markdown-bestand aangepast. Er zijn geen tests aangepast. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Er is geen code veranderd, dus `architectuur.md` hoefde niet bij te werken. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Bewijs is gemarkeerd met GEZIEN en de bron (curl, merge-tree). "Daan ja (8" is een cijfer van een keurder en geen meting. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | De alinea over #380 is nu erg lang (±1000 tekens op één regel) en moeilijk te scannen. De bestandsgrens van ±400 regels is niet in gevaar. | Feit | Midden | Leesbaarheid, geen harde regel |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niets in deze wijziging is te zien of te spelen. Het is een interne statusnotitie. Het eindresultaat is de sleeplink op de README en dortus.com. Dat is nog niet live en hoort bij de keuring van Daan #398.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een sleeplink die bij elke nieuwe gratis versie stuk gaat, zal bij een koper als kapot overkomen. | Op de README en op dortus.com ook de gewone winkelknop laten staan naast de sleeplink. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing. Er is niets dat een klant als eerste ziet (geen hoofdbeeld, omslag of thumbnail), dus de blinde test geldt niet. Ik geef geen cijfers, want ik heb geen beeld en geen concurrentenvoorbeeld om tegen te vergelijken. De sleeplink zelf wordt pas beoordeeld als hij live staat.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:**
- Geen.

**Kan:**
- Controleer vóór het plakken met `curl` welke gratis versie live staat (zie A3). Het plakbestand `vindbaar/sleeplink-380.md` moet de link naar die versie bevatten.
- Controleer of de tijden 16:15 en 16:20 in de notitie kloppen met de committijd (zie A2). Zijn ze vooruit geschreven, pas ze dan aan.
- Hak de alinea over #380 op in een paar korte regels, of verplaats de details naar `vindbaar/sleeplink-380.md`.
- Laat de gewone winkelknop naast de sleeplink staan voor wie de link niet kan slepen (zie C1).

---
Automatische keurder, model `claude-sonnet-5-5`, 18703 tokens in, 3594 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
