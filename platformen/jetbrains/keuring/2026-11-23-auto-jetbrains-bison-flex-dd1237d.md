# Keuring jetbrains-bison-flex akkoordregel 2026.1.2, 23-11-2026, automatische keurder
Wat ik keurde: commits 489f4bd..dd1237d (commit 695917c9c), alleen `producten/jetbrains-bison-flex/ontwerp.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging is alleen tekst: een nieuwe akkoordregel van Daan voor de uitgave van 2026.1.2. De belofte (wat, voor wie, gratis en Pro) is ongewijzigd. Er is geen code of beeld meegestuurd.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De belofteregel is ongewijzigd en de nieuwe akkoordregel noemt dezelfde functies (meldknop in het Help-menu, error handler). | Feit | Hoog | Vergelijking van de diff met de belofte: de belofteregel staat er als ongewijzigde context. |
| 2 | De regel zegt dat de change-notes beide nieuwe regels bevatten, met "Nothing is sent until you submit it yourself". Dat staat ook in `CHANGELOG.md` onder 2026.1.2. | Feit | Hoog | `CHANGELOG.md` en de akkoordregel komen overeen. Of `plugin.xml` hetzelfde zegt, kan ik niet zien. |
| 3 | De regel zegt dat de uitgave op commit 2e46f5e2 staat en dat de CLion-run 45197751752 en de e2e-run 45197752060 groen zijn. Dat kan ik niet nagaan, want 2e46f5e2 zit niet in deze wijziging. | Vermoeden | Midden | De uitslag van beide runs op 2e46f5e2 in de GitHub-API. |
| 4 | De keuring van Daan staat in `platformen/jetbrains/keuring/2026-11-23-bison-flex-2026.1.2-uitgave-daan.md`. Dat bestand zat niet in deze wijziging. | Vermoeden | Midden | Het bestand zelf, met `Akkoord: ja` bovenaan. |
| 5 | De open vraag of issues aan staan op de loketrepo is eerlijk als open punt genoemd. Als issues uit staan, krijgt een gebruiker die "Report a Problem" opent een dode pagina. | Vermoeden | Midden | Eén keer de meldlink openen. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het ontwerp is niet door de bouwer zelf goedgekeurd: de regel verwijst naar Daan en een aparte keuring. | Feit | Hoog | Een keurder keurt niet zijn eigen werk. |
| 2 | De oude akkoordregel van 18 nov is bewaard als "Oud" en niet gewist. Het opgeslagen voorbehoud over de meldknop blijft zo zichtbaar. | Feit | Hoog | Geschiedenis blijft leesbaar. |
| 3 | De run-nummers zijn bij GEZIEN gezet ("GEZIEN in de API"), dus de herkomst is gemarkeerd. | Feit | Hoog | Cijfers met GEZIEN, DERDEN of GOK. |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens. |
| 5 | `CHANGELOG.md` noemt Plugin Verifier tegen IDEA 2025.3, 2026.2 en CLion 2026.2. De nieuwe akkoordregel noemt de verifier niet, alleen de CLion- en e2e-run. De 18 nov-regel noemde "5 van 5 Compatible" wel. | Vermoeden | Laag | Uitslag van de verifier op 2e46f5e2. |
| 6 | De architectuurtekst begint met "Stand 8 nov 2026: versie 0.2". Of de meldknop en error handler daar beschreven staan, is in het getoonde stuk niet te zien. Deze wijziging raakt dat bestand niet. | Vermoeden | Laag | `architectuur.md` op de meldknop en error handler nalezen. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie alleen tekst en kan niets spelen of bekijken, dus hier valt weinig te beoordelen.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De meldknop in het Help-menu is voor een gebruiker alleen prettig als de meldlink werkt. | De link één keer openen en controleren dat het meldformulier verschijnt met de versies al ingevuld. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Open de meldlink één keer en controleer dat issues aan staan op de loketrepo. Doe dit vóór het uitbrengen (Daan noemde dit zelf al).
2. Zet de verifier-uitslag voor 2e46f5e2 erbij, zoals bij de oude akkoordregel.
3. Controleer dat `architectuur.md` de meldknop en error handler beschrijft en de "Stand"-regel bijwerkt.
4. Controleer bij live zetten de run-uitslagen en Daans keuringsbestand zelf; die kon ik in deze wijziging niet zien.

---
Automatische keurder, model `claude-sonnet-5-5`, 19206 tokens in, 3231 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
