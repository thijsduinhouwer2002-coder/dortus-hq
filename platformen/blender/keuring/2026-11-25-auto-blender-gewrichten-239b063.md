# Keuring blender-gewrichten KAART.md (Pro 1.2.8 klaar om te plakken), 25-11-2026, automatische keurder
Wat ik keurde: commit 239b06326 (f6aa9b6..239b063), alleen `producten/blender-gewrichten/KAART.md`
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De kaart zegt "Daan ja (#11, #29, #37)". De regel die vervangen is zei: "Daan #29 ja op code, nee op uitbrengen tot M1/M2", en #37 was nog een nakeuring. Dat M1/M2 zijn opgelost of dat Daan nu ook op uitbrengen ja zegt, staat nergens in deze wijziging. | Feit (tegenstrijdig met de oude regel) | Hoog | De tekst van Daan in #29 en #37, of een regel in `ontwerp.md` met "Akkoord: ja" voor 1.2.8 en de stand van M1/M2. |
| 2 | In `ontwerp.md` staat het laatste ja voor Pro 1.2.6. Voor 1.2.8 is in het zichtbare deel geen ja te vinden. De keuringsregel vraagt dat Daan dat bovenaan `ontwerp.md` zet. | Vermoeden (het bestand is afgekapt) | Midden | Een regel "Akkoord: ja ... Pro 1.2.8" in `ontwerp.md`. |
| 3 | "Zip uit e2e 45526260663 ... sha256 nagekeken" noemt geen hash. Wie de zip plakt kan niet nagaan welk bestand bedoeld is. | Feit | Hoog | De sha256 in de kaart of in de note `pro-1.2.8.md`. |
| 4 | "Gemeld bij de hoofdchat" staat niet in deze wijziging, want er is geen wijziging in `berichten/hoofdchat.md`. | Vermoeden | Midden | Een bericht in `berichten/hoofdchat.md` van na 25 nov 00:00. |
| 5 | De kaart is gedateerd 25 nov 04:20, maar de keuring is van 04:10. | Feit | Hoog | Een juiste tijd in de kaart. Dit is klein. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen een tekstbestand. Geen tests aangepast en geen bestand boven 400 regels. | Feit | Hoog | Tests en bestandsgrootte |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 3 | "Groen in 4.2.23, 5.2.3, 5.3.0" en de piek van 4,6 GB zijn eerder als GEZIEN gemarkeerd. De nieuwe regel zet GEZIEN alleen bij de e2e-run en niet bij "Daan ja". | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | De kaart zegt dat Pro 1.2.8 samen met het robot-hoofdbeeld geplakt wordt vóór de sale. Voor dat beeld is geen uitslag GESLAAGD van de blinde test te zien. De vorige cover verloor van Cleave. | Vermoeden | Midden | Blinde test voor eerste beelden |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Dit is een interne statuskaart. Er is niets te zien of te spelen, dus ik kan hier niets over zeggen. | Niet van toepassing | n.v.t. |

## Deel C: is het goed genoeg?
Niet van toepassing: de wijziging bevat geen beeld, winkeltekst of spel. De blinde test voor het robot-hoofdbeeld hoort bij dat beeld zelf (zie B4).

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Onderbouw "Daan ja (#11, #29, #37)" met een citaat of link, en zeg wat er met M1/M2 gebeurd is. Zonder dat tegenspreekt de kaart de vorige regel en leest "klaar om te plakken" als toestemming om uit te brengen. Zet ook het ja voor 1.2.8 in `ontwerp.md` (A1, A2).

**Kan**
1. Zet de sha256 van de zip in de kaart of in de note (A3).
2. Corrigeer de tijd 04:20 (A5).
3. Maak duidelijk dat het robot-hoofdbeeld pas mee mag na een blinde test met uitslag GESLAAGD (B4).
4. Voeg een bewijs toe voor "gemeld bij de hoofdchat" (A4).

---
Automatische keurder, model `claude-sonnet-5-5`, 18827 tokens in, 3220 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
