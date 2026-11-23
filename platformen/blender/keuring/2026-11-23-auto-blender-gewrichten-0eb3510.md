# Keuring blender-gewrichten testset-meting, 23-11-2026, automatische keurder
Wat ik keurde: commits eaa1252..0eb3510 (0eb351066), bestanden `e2e/meet_rig.py` en `e2e/meet_tabel.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De add-on zelf is niet veranderd. Dit is meetgereedschap, dus ik toets tegen de belofte in het commitbericht.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `meet_rig.py` schrijft per run een vingerafdruk (`vinger`) weg: de gesorteerde regels met bereik en het aantal punten per deel. | Feit | hoog | Een resultaatbestand van een nieuwe run met het veld `vinger`. |
| 2 | `meet_tabel.py` leest nu meerdere herhalingen (`<figuur>-<n>.json`) per cel. Het toont de gewrichten per herhaling, de slechte sneden opgeteld, de mediaan van de tijd en "1 vorm" of "N vormen". De bestandsnaam-regex en het `-t1`-filter lijken voor alle vier de naamvormen te kloppen. | Vermoeden (alleen uit de tekst gelezen) | midden | Het script draaien op een map met o.a. `robot-a-1.json`, `robot-a-2-t1.json` en een oud `robot-a.json`. |
| 3 | Het commitbericht belooft "elke meting 5 keer", de nulstand met Pro 1.2.2 en een proef met één thread. Daarvan staat niets in deze diff: de workflow ontbreekt en `CJ_THREADS` wordt alleen uitgelezen, nergens gezet. | Vermoeden | midden | De workflow in `.github/workflows` of de tak `betrouwbaar-uitslag` met 5 bestanden per cel. Het commitbericht beschrijft dan een eerdere of latere wijziging. |
| 4 | Als de thread-beperking via een Blender-vlag loopt en niet via de omgevingsvariabele `CJ_THREADS`, blijft het veld `threads` leeg. De `-t1`-suffix in de bestandsnaam doet het onderscheid dan alleen. | Vermoeden | laag | Een resultaatbestand van de één-thread-proef met `threads` gevuld. |
| 5 | "Dezelfde vingerafdruk betekent precies hetzelfde figuur" is te sterk. Gelijke regels en gelijke puntentallen sluiten een andere vorm met dezelfde aantallen niet uit. Het is een goede aanwijzing, geen bewijs. | Feit (over de aanpak) | hoog | Daarbij ook een hash van de puntposities per deel vergelijken, zoals de undo-toets al doet. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Alleen meetgereedschap is veranderd. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | `meet_tabel.py` is na de wijziging ongeveer 50 regels. De lengte van `meet_rig.py` zie ik niet, maar de diff begint rond regel 144. | Vermoeden | midden | Bestanden onder ±400 regels |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens |
| 4 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier waarschijnlijk niet, want het zijn meetscripts buiten de add-on. | Vermoeden | midden | architectuur.md bijgewerkt |
| 5 | Het commitbericht noemt geen cijfers, dus er valt niets te labelen met GEZIEN, DERDEN of GOK. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Er is niets te zien of te spelen: het zijn meetscripts voor intern gebruik.

| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De tabelcel is nu lang: "5,5,5,4,5 / 0 / 12 s / 2 vormen". Dat leest lastig. | Een korte markering zodra de herhalingen verschillen, bijvoorbeeld een uitroepteken, en het kopje "Gewrichten per herhaling" erbij. | klein |
| 2 | Bij oude mappen zonder vingerafdruk staat er "? vormen". Dat kun je verkeerd lezen als een uitkomst. | "geen vingerafdruk" tonen. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of het commitbericht (5 herhalingen, nulstand Pro 1.2.2, één thread) klopt met de workflow. Die zat niet in deze diff.
- Zet `--t1` in de gebruiksregel bovenin `meet_tabel.py`. Nu staat hij alleen in de omschrijving en in de code.
- Voeg een hash van de puntposities toe aan de vingerafdruk, zodat "zelfde figuur" sterker bewezen is.
- Maak de cel in de tabel korter, en toon "geen vingerafdruk" in plaats van "?".

---
Automatische keurder, model `claude-sonnet-5-5`, 19308 tokens in, 4439 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
