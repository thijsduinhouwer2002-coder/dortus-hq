# Keuring blender-gewrichten testkaartplaatjes 20 en 20h, 19-11-2026, automatische keurder
Wat ik keurde: commit bb82f1869 (49f8c53..bb82f18), bestand producten/blender-gewrichten/e2e/scherm_testkaart.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging raakt alleen het schermscript voor de winkelplaatjes. De add-on zelf verandert niet. De toets is de commitbelofte "camera past zichzelf in beeld, niets afgesneden".

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De nieuwe functie `pas_in_beeld` zet alle acht hoeken van elk object om naar cameracoördinaten. Ze schuift de camera 5% terug tot alles binnen 5% marge staat en boven de bijschriftstrook (y ≥ 0,12). De logica is goed te volgen. | Feit (uit de code) | Hoog | n.v.t. |
| 2 | Of plaatje 20 en 20h nu echt niets meer afsnijden, kan ik niet zien. Ik zie geen beeld en geen run. | Vermoeden | Midden | De logregel "camera afstand ... x ..y.." uit de volgende run (x en y binnen 0,05..0,95) en het plaatje zelf bekeken met de Read-tool. |
| 3 | Bij elke herhaling roept `camera()` zichzelf opnieuw aan, tot 40 keer. Als die functie elke keer een nieuw cameraobject en bijschrift maakt, blijven oude over in de scene. Een oud bijschrift kan dan in beeld staan. | Vermoeden | Laag | Aantal camera- en tekstobjecten na `pas_in_beeld` tellen, of de code van `camera` en `bijschrift` lezen. |
| 4 | Haalt de lus na 40 stappen het beeld niet, dan komt er geen waarschuwing en `ok` blijft waar. Het log toont dan de afstand van de laatste ronde, niet die van de camera die blijft staan. | Feit (uit de code) | Hoog | n.v.t. Het is klein, want 40 keer 5% is ruim genoeg. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Alleen het schermscript is gewijzigd en de controle op beeld blijft gelijk. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Het bestand blijft waarschijnlijk ruim onder 400 regels (de wijziging voegt ±20 regels toe aan een script van ±200). De totale lengte zie ik niet. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` en `CHANGELOG.md` zijn niet gewijzigd. Dat hoeft hier ook niet, want het is een intern schermscript zonder verandering voor de gebruiker. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | De commitregel noemt "log, bericht Daan", maar die bestanden staan niet in de lijst met gewijzigde bestanden. Misschien zijn ze er gewoon niet bij gestuurd. | Vermoeden | Laag | Alleen ter controle |
| 5 | Ik zie geen persoonsgegevens, sleutels of AI-beeld of -geluid in de wijziging. | Feit | Hoog | Geen persoonsgegevens, geen AI-beeld op Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beeld, dus dit zijn vermoedens.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Terugschuiven in stappen van 5% kan plaatje 20 verder weg zetten dan Daan wilde ("iets dichterbij", herkeuring 20). Het staafje is dan kleiner in beeld. | Na de run de afstand in het log bekijken. Is er veel lucht, dan kan de startafstand kleiner of de marge strakker. | Klein |
| 2 | De 5% marge geldt rondom, maar onderin geldt 12%. Het object kan dan scheef in het kader staan. | Het beeld in het midden van de vrije ruimte zetten, of de camera iets omhoog richten. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Na de volgende run de plaatjes 20 en 20h bekijken met de Read-tool en de logregel "camera afstand" nalezen (Deel A 2).
- Nagaan of `camera()` bij elke herhaling nieuwe objecten laat liggen, en die zo nodig opruimen (Deel A 3).
- Een waarschuwing in het log zetten als de lus na 40 stappen nog niet past (Deel A 4).
- De compositie nakijken op te veel lucht of scheef in het kader (Deel C 1 en 2).

---
Automatische keurder, model `claude-sonnet-5-5`, 18395 tokens in, 3019 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
