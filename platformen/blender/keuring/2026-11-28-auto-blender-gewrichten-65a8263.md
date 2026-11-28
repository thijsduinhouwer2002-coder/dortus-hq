# Keuring Click Joints Pro 1.2.9 plakkaart (verse zip), 28-11-2026, automatische keurder
Wat ik keurde: commit 65a82631b (cf10ef1..65a8263), bestanden `producten/blender-gewrichten/KAART.md` en `producten/blender-gewrichten/winkel/plak-1.2.9.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De opdracht is een plakkaart bijwerken, zodat de zip niet verloopt vóór de plak van ma 30 nov 20:00. De nieuwe run 46120199131 verloopt di 1 dec 08:34 NL, dus ruim na de plak. Dat lost het probleem op. | Feit (uit de tekst) | Hoog | Het GitHub-veld `expires_at` van de run. |
| 2 | De kaart noemt run, sha256 (`ebafe214...`) en vervaldatum, en de volledige sha256 in de plakkaart heeft 64 tekens. KAART en plakkaart zijn onderling gelijk. | Feit | Hoog | Niets nodig. |
| 3 | De regel "Bestand ... (179.325 bytes, GEZIEN)" is niet bijgewerkt, terwijl de zip van een andere run komt met een andere sha256. De grootte kan toevallig gelijk zijn, maar dat staat nergens. | Vermoeden | Midden | `ls -l` of `sha256sum` op de nieuwe zip. |
| 4 | "Groen in 4.2.23, 5.2.3 en 5.3.0" en "code gelijk aan main (compare: 0 bestanden)" kan ik niet nalopen. Ik zie alleen de tekst. | Vermoeden | Midden | De API-uitslag van run 46120199131 en de GitHub compare tussen fea86da en 32c1d5f. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen code of test aangepast, alleen twee documenten. De 400-regels-grens en architectuur.md raken niet aan deze wijziging. | Feit | Hoog | Tests niet aangepast, bestandsgrootte, architectuur.md |
| 2 | De cijfers dragen het label GEZIEN, met bron en datum. | Feit | Hoog | Cijfers met GEZIEN, DERDEN of GOK |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. Een sha256 is geen geheim. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De tijd "GEZIEN via `actions.py` op 28 nov ±09:35 NL" ligt na het moment van deze keuring (08:51 NL). Het artefact is volgens `expires_at` ±08:34 NL gemaakt, dus de run was dan nog net klaar. Waarschijnlijk is de kloktijd verkeerd genoteerd. | Vermoeden | Midden | GEZIEN moet kloppen met het moment van kijken |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing: dit is een intern plakkaartje, geen beeld, spel of winkeltekst die een klant ziet.
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen. | Niets nodig. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing: er is geen klantbeeld, geen winkeltekst en geen blinde test nodig. Er zijn dus geen cijfers en geen blokkade door een cijfer onder 8.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Zet de tijd "±09:35 NL" in de plakkaart goed (nu later dan de keuring van 08:51) of laat de bron zien.
2. Controleer de regel "179.325 bytes" tegen de nieuwe zip en werk hem bij als het getal afwijkt.
3. Laat bij het plakken `controle-1.2.9.sh` draaien en zet runnummer en sha256 in `commercie/geplaatst.md`, zoals de kaart al beschrijft.

---
Automatische keurder, model `claude-sonnet-5-5`, 21155 tokens in, 3093 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
