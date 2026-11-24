# Keuring blender-gewrichten, uitslag omslagfiguren (kan-punten 97ccf45), 24-11-2026, automatische keurder
Wat ik keurde: commit 4bc5e88 (alleen `producten/blender-gewrichten/proeven/omslag-figuren-main-2026-11-24/uitslag.md`)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen een proefuitslag, geen add-on-code. De beloofde functies in het ontwerp veranderen dus niet. | Feit | Hoog | De lijst met gewijzigde bestanden bevat alleen dit .md-bestand. |
| 2 | De releasenote wordt eerlijker: er staat nu letterlijk dat de belofte alleen voor 5.2 en 5.3 geldt en dat kleding in 4.2 op 8 van 9 uitkomt. Dat past bij de tabel eronder (4.2 kleding 8, 5.x 9). | Feit | Hoog | Vergelijken van de tekst met de tabel in dezelfde wijziging. |
| 3 | De claim dat de add-on tussen 14e6e42 en 3974792 gelijk is, kan ik niet nagaan. Ik zie alleen de tekst. | Vermoeden | Midden | `git diff 14e6e42 3974792 -- producten/blender-gewrichten/click_joints` is leeg. |
| 4 | De conclusie dat het verschil "in de eerste twee pogingen" zit en niet in de dikte van het been, volgt niet helemaal uit de lijst. Poging 1 en 2 falen in de beweegproef (overlap in rust), niet in Exact. Alleen poging 3 is een Exact-fout. | Vermoeden | Midden | Een proef van de rechterknie in 4.2 met de spiegelplek (-20,9; 10,3; 59,1), met het log van de beweegproef erbij. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests of drempels aangepast. De uitslag noemt de ondergrens 8 in `meet_drempel.json` als gelijk aan de meting en past hem niet aan. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Het bestand is kort (ongeveer 50 regels) en er is geen code veranderd, dus `architectuur.md` hoeft niet mee. | Feit | Hoog | Bestanden onder ±400 regels, architectuur bijgewerkt |
| 3 | Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De cijfers dragen GEZIEN-labels in de llopende tekst. De samenvattingstabel heeft zelf geen label en verwijst naar de tak `betrouwbaar-uitslag`. Dat is acceptabel, maar de bron staat niet bij elke rij. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | De bewering over `rig.py` ("nu wint de melding van de laatste poging, behalve bij `vangnet`") komt uit de code, maar die zie ik niet in deze wijziging. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | De overdracht aan Betrouwbaarheid "via de hoofdchat" staat in de tekst. Het berichtenbestand zelf zit niet in deze wijziging, dus ik kan niet zien dat het bericht er echt is. | Vermoeden | Laag | Een regel in `berichten/hoofdchat.md` over de rechterknie in 4.2 |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De koper krijgt bij de rechterknie in 4.2 het advies "try a spot further from the end". Dat advies klopt niet met de echte oorzaak (overlap op de goede plek) en stuurt de koper de verkeerde kant op. De uitslag beschrijft dit zelf goed. | De reden van de eerste kandidaat op het bot tonen in plaats van die van de laatste noodplek. Dit is aan Betrouwbaarheid doorgegeven. | Klein tot midden |
| 2 | Ik kan zonder spelen of beeld niet beoordelen hoe de lijst met ontbrekende gewrichten er voor de koper uitziet. | Iris of Daan laten kijken naar de lijst in het paneel. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- De conclusie over de oorzaak (punt A4) voorzichtiger formuleren, bijvoorbeeld "waarschijnlijk", of eerst een proef met de spiegelplek in 4.2 doen.
- Een bronregel onder de samenvattingstabel zetten, bijvoorbeeld "GEZIEN, tak `betrouwbaar-uitslag`, map `main-45295977807/`".
- Nagaan of het bericht aan Betrouwbaarheid echt in de hoofdchat staat.
- De misleidende foutmelding in 4.2 oplossen vóór de koper hem ziet, of opnemen in de bekende beperkingen.

---
Automatische keurder, model `claude-sonnet-5-5`, 18702 tokens in, 3064 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
