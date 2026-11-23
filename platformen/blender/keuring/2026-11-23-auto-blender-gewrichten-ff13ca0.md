# Keuring blender-gewrichten, notitie betrouwbaar-rig deel A, 23-11-2026, automatische keurder
Wat ik keurde: commit ff13ca0bb, het nieuwe bestand `producten/blender-gewrichten/keuring/2026-11-23-betrouwbaar-rig-deel-A.md`. Geen add-on code.
Akkoord: ja

Kort: dit "ja" gaat alleen over de keuringsnotitie als document. Het product blijft geblokkeerd door het "nee" en de punten M1 tot en met M3 in die notitie. Ik kan de run-cijfers, JSON en logs niet nalezen, dus die zijn voor mij vermoedens.

## Deel A: doet het wat beloofd is?
(De wijziging is een keuringsnotitie. Ik toets haar aan de opdracht in `ontwerp.md` en aan zichzelf.)

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één nieuw tekstbestand. De goedgekeurde add-on (Click Joints 0.1.1 en Pro 1.0.2) verandert niet. | Feit | hoog | `git diff --stat 663585d..ff13ca0`. |
| 2 | De getoonde `ontwerp.md` noemt "Figure from rig" en de belofte "60 per versie" niet (de tekst is afgekapt). Ik kan de notitie dus niet tegen de opdracht toetsen. | Vermoeden | midden | De volledige opdracht of het bericht van Betrouwbaarheid. |
| 3 | De cijfers in de notitie kan ik niet narekenen. Het gaat om de run-ids, 35/59/59, 55 van 60, 240112 tegen 273112 punten en de tijden. | Vermoeden | laag | JSON op de tak `betrouwbaar-uitslag` en `e2e/meet_tabel.py`. |
| 4 | De notitie is in zichzelf consistent. Het "nee" volgt uit M1 tot M3, en 4.2 hoort bij wat het ontwerp belooft (Blender 4.2 tot 5.2). | Feit (uit de tekst) | hoog | Niet nodig. |
| 5 | In A5 is de som "2+2+7+8+9+8 = 36 van 53" niet te herleiden uit de genoemde figuren. Alleen robot-a, robot-b en robot-fijn staan er met naam. | Vermoeden | midden | Een lijst per figuur. |
| 6 | Het bericht staat op ±22:55, terwijl de aanvraag van 22:45 NL is en de stand 21:42 UTC. Het is onduidelijk of dat NL- of UTC-tijd is. | Vermoeden | laag | Tijdstempel in `berichten/hoofdchat.md`. |
| 7 | M3 zegt dat drie runs nog liepen. Dat kan al achterhaald zijn. | Vermoeden | midden | De uitslag van runs 45267268513 en 45267268414. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast en er is geen code gewijzigd. | Feit | hoog | Tests niet aangepast om te slagen. |
| 2 | Het bestand is 50 regels. | Feit | hoog | Bestanden onder ±400 regels. |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. | Feit | hoog | Geen persoonsgegevens. |
| 4 | `architectuur.md` hoefde niet bij, want het product veranderde niet. | Feit | hoog | architectuur.md bijgewerkt. |
| 5 | De cijfers zijn gelabeld met Feit, vermoeden of GOK, niet met GEZIEN, DERDEN of GOK. Dat is bruikbaar maar niet de vaste woorden. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK. |
| 6 | Deel B ontbreekt, bedoeld voor een tweede keurder. "Akkoord" staat op regel 5 in plaats van regel 3. | Feit | hoog | Vast formulier. |
| 7 | De notitie meldt zelf dat `betaald/rig.py` 815 regels is, boven de ±400. Dat zit niet in deze wijziging maar in de tak. | Feit (volgens de notitie) | midden | Bestanden onder ±400 regels. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen, dus dit gaat alleen over de verbeterideeën in de notitie.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De ideeën C1 tot C4 in de notitie zijn nuttig en vanuit de koper bedacht. Ze zijn nog niet verwerkt. | Ze meenemen bij de volgende bouwronde, vooral de ene regel boven de lijst voor 4.2. | klein |
| 2 | De cellen in A5 en A6 zijn erg lang en moeilijk snel te lezen. | Korte kop per bevinding, details in een bijlage. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen, voor deze wijziging.

Het product zelf blijft op "nee" staan tot M1 tot en met M3 uit de notitie zijn opgelost:
- De 4.2-meting opnieuw doen.
- De vastlopende 4.2-jobs uitzoeken.
- 4.2 groen laten zien op de eindcode.

**Kan:**
- Schrijf in A5 de som per figuur uit.
- Controleer het tijdstip van het bericht (NL of UTC).
- Herkeur M3 zodra de lopende runs klaar zijn.
- Laat een tweede keurder deel B doen, ook over de grootte van `betaald/rig.py` (815 regels).
- Zet de formulierkop weer volgens het vaste formulier, met "Akkoord" op regel 3.

---
Automatische keurder, model `claude-sonnet-5-5`, 22019 tokens in, 7235 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
