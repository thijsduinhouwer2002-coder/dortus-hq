# Keuring Click Joints Pro #114 (Pro zet de gratis zelf uit), 26-11-2026 08:10 NL, automatische keurder
Wat ik keurde: commits bf64d24..99a3c69 (f43c3c67d, 46f8667c2, 99a3c69f8), 5 bestanden onder `producten/blender-gewrichten/`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Pro zet bij aanzetten een gratis Click Joints uit een andere repository uit met `addon_utils.disable(..., default_set=True)`, vóór de kern van Pro zich registreert. Dat past bij issue 114 en het ontwerp ("zet die dan zelf netjes uit"). | Feit (uit de diff) | hoog | n.v.t. |
| 2 | Lukt uitzetten niet, dan blijft `weiger_dubbel` de oude melding geven. Er staan dus nooit twee tegelijk aan. De volgorde in de code klopt: eerst uitzetten, dan weigeren. | Feit | hoog | n.v.t. |
| 3 | Bij een fout in de unregister van de gratis komt één regel in de console (aanrader A1 van Daan, #138). `GRATIS_UIT` wordt leeg bij afmelden, dus de regel blijft niet hangen. | Feit | hoog | n.v.t. |
| 4 | De paneelregel "Free Click Joints was turned off; Pro includes everything in it." staat bovenaan via `BOVEN.insert(0, ...)`. | Feit dat de code dit doet, vermoeden dat het zo draait | midden | Een schermafbeelding uit de e2e-run, of de groene stap "(a) paneel toont de regel als eerste". |
| 5 | `zet_gratis_uit` roept `_meld(...)` aan. `_meld`, `toetsen_paneel` en de imports in `test_betaald.py` staan niet in de diff. | Vermoeden | midden | Een groene e2e-run op 4.2, 5.2 en 5.3 (zoals bij eerdere akkoorden), of de volledige bestanden. |
| 6 | Het concept van de Docs-tab 1.2.9 staat niet in de meegestuurde bestanden. Ik kan dus niet nagaan of "Disable it first" echt weg is. | Vermoeden | laag | Het conceptbestand zelf. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is aangepast omdat het gedrag bewust veranderd is (weigeren wordt overnemen), niet om een rode test groen te krijgen. De oude controles van de weigering zijn vervangen door strengere controles van het nieuwe gedrag. Voorbeelden: gratis uit de voorkeuren, niet verwijderd, Pro werkt, paneelregel, winkellinks. | Feit | hoog | Tests niet aangepast om te slagen: ok |
| 2 | `architectuur.md` en `ontwerp.md` zijn bijgewerkt en noemen de toetsstappen (a) en (b). De docstring van `betaald/__init__.py` en de test is ook bijgewerkt. | Feit | hoog | architectuur.md bijgewerkt: ok |
| 3 | `ontwerp.md` en `architectuur.md` zijn veel groter dan 400 regels. Dat was al zo en deze wijziging verandert er weinig aan. `betaald/__init__.py` blijft ruim onder de 400 regels. | Feit | midden | ±400 regels: oud, geen moet |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Geen nieuwe cijfers zonder label, geen spelerstekst van Hats, geen AI-beeld of -geluid. | Feit | hoog | Overige regels: ok |
| 5 | Geen groen e2e-resultaat in de aangeleverde tekst. | Vermoeden | midden | De groene run op de commit 99a3c69. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Wie van gratis naar Pro overstapt hoeft niets meer te doen. Eerder moest hij zelf uitzetten, en dat is vervelend. Dat ziet er goed uit op papier. Ik kan het niet zien of spelen. | n.v.t. | n.v.t. |
| 2 | De uitleg staat de hele sessie bovenaan het paneel, zonder een knop om hem weg te halen. Na een herstart is de gratis uit en verdwijnt de regel vanzelf. Of dit storend is, is een vermoeden. | Eventueel een kruisje, zoals bij de beoordelingsregel. | klein |
| 3 | De regel zegt niet dat de instellingen in het .blend-bestand blijven. Dat staat wel in de oude weigermelding. | Een extra halve zin of een tooltip: "Your settings are kept." | klein |

## Deel C: is het goed genoeg?
Geen eerste-indrukbeeld (hoofdbeeld, omslag of thumbnail) in deze wijziging, dus geen blinde test nodig. Ik kan één regel tekst in een paneel niet zien. Daarom geef ik geen cijfers. De beoordeling van uiterlijk en gebruik is al gedaan door Daan (#138 en #148, volgens de commit). Een eigen cijfer zou schijnzekerheid zijn.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Controleer dat de groene e2e-run op 99a3c69 echt bestaat en de stappen "(a) paneel toont de regel als eerste" en "(b) betaald uit: regel van de overname weg" bevat (deel A 5 en deel B 5).
2. Bekijk de Docs-tab 1.2.9 en haal "Disable it first" weg, zodra 1.2.9 live is. Het ontwerp zegt hetzelfde (deel A 6).
3. Overweeg een kruisje bij de paneelregel en een halve zin over bewaarde instellingen (deel C 2 en 3).
4. Als Pro na het uitzetten van de gratis toch niet opstart (fout in `_register_kern`), heeft de gebruiker beide uit. Dat is zeldzaam, maar dit staat nergens in de toets.

---
Automatische keurder, model `claude-sonnet-5-5`, 28512 tokens in, 5392 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
