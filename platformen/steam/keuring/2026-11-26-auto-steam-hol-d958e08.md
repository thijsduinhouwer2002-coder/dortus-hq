# Keuring steam-hol, 26-11-2026, automatische keurder
Wat ik keurde: commits bbc43cc..d958e08 (alleen de tekst en diff; geen beeld gezien, niets gedraaid)
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `hol/luik.gd` en `hol.gd` tekenen op elke dichte put een luik, met een eigen beeld per stap (0 tot 3, stap 4 tot 6 houden beeld 3 met gouden stenen erop). Dat past bij #209. | Feit (code), vermoeden (of het op 1x leest) | midden | De bewijsbeelden in `bewijs-luik/` (niet meegestuurd) en Daans nakeuring. |
| 2 | `ritme.gd`, `held_val.gd`, `afloop.gd` en `kaartje.gd` brengen koopgeluk, droogte, +4 goud na minuut 4 en stap 4 tot 6. De demo-film (`demo=1`) houdt zijn oude waarden. De code laat dit zien. | Feit (code) | hoog | De cijfers (langste gat 172 s, mediaan 134 s en 142 s) staan in bestanden die ik niet zag. |
| 3 | `veilig_bestand.gd` schrijft via `.tmp`, bewaart de vorige save en zet een kapotte save opzij. Alle paden die ik las lijken kloppend, ook een crash tussen twee hernoemingen. | Vermoeden (alleen code gelezen) | midden | `toets_opslag.gd` en de duurtest op Windows (niet zichtbaar). |
| 4 | Droogte en koopgeluk laten helden vaker vallen en minder vaak ontsnappen. Dat past bij "nooit straffen". Het kan wel het aantal terugkomers met wrok verlagen, wat het hoofdidee van de kerker is. | Vermoeden | laag | Een telling van terugkomers per 20 minuten voor en na de wijziging. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `hol_vast.gd` is er ±200 regels bij gekomen (grond, achterwand, wand_dingen). De hunk begint al op regel 560, dus het bestand was al groter dan 400 en is nu minstens ±760. `hol.gd` is minstens ±630. | Feit | hoog | Bestanden onder ±400 regels |
| 2 | `architectuur.md` heeft nieuwe rijen voor licht, leven, hol-lagen, veilig bestand en stap-tekens. Er staan geen rijen voor `hol/luik.gd` en de lagen grond en achterwand in `hol_vast.gd`. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | `toets_systemen.gd`, `toets_opslag.gd` en `toets_licht.gd` zijn gewijzigd maar niet meegestuurd. Ik kan niet nagaan of de toetsen niet aangepast zijn om te slagen. De commits melden "0 FOUT". | Vermoeden | laag | Tests niet aangepast om te slagen |
| 4 | Nieuwe spelertekst: "All bought." (zichtbaar) en "Heroes drop 2 more gold." (niet meegestuurd). Ik zie geen CONCEPT-markering. | Vermoeden | laag | Spelerstekst Hats alleen als CONCEPT |
| 5 | Alle commits, ook de Iris-keuringen, staan als "(Claude)". Ik kan niet zien of de keurder los van de bouwer werkte. | Vermoeden | laag | Keurder is niet de bouwer |
| 6 | In KAART.md staan cijfers met GEZIEN of GOK. Persoonsgegevens, sleutels of wachtwoorden zag ik niet. | Feit | midden | Cijfers met label, geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Worm, mot, stofjes en vleermuis komen elke 5 tot 15 s, steeds één en nooit hetzelfde twee keer achter elkaar. Na een kwartier kan dat voorspelbaar worden (vermoeden). | Een zeldzaam ding erbij, bijvoorbeeld een druppel of een held die schrikt. | klein |
| 2 | Koopgeluk en droogte laten de eerste held na een koop of na lange tijd zonder vangst altijd vallen. Een oplettende speler merkt dat het gestuurd is (vermoeden). | Laat de kans oplopen in plaats van een zekere val. | klein |
| 3 | Stap 4 tot 6 zijn alleen een gouden steen en +2 goud. Het hol ziet er dus niet anders uit dan bij stap 3. | Eén klein eigen detail per stap, zoals bij het luik. | midden |
| 4 | Gang en grond hebben nu plekken steen, wortels en kiezels. Het ritme is bewust gebroken (#133). Of dat op 1x echt rijk leest, kan ik niet zien. | De blinde test herhalen met een lezer die het niet kent. | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | geen cijfer | Ik zie geen beelden en kan niet naast Rusty's Retirement of Spirit City leggen. Iris gaf "mooi 8" (commit a216caf8c), de eerdere builds kregen 7. |
| Zou ik het zelf kopen of bekijken op basis van dit? | geen cijfer | Zelfde reden. |
| Zou Thijs er trots op zijn? | geen cijfer | Daan keurde de Deep Pit eerder met 7,5 (nee). De nakeuringen (#213, #214) lopen nog. In `ontwerp.md` staat "Akkoord: nog niet". |

Zonder een zichtbaar cijfer van 8 of hoger van Daan blijft het akkoord nee.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. `hol_vast.gd` (en `hol.gd`) zijn ruim boven de ±400 regels. Haal grond en achterwand eruit naar een eigen bestand, zoals eerder met `hol_lagen.gd` gebeurde.
2. Het uiterlijk heeft nog geen akkoord van Daan (#213 en #214 open, `ontwerp.md` zegt nog niet). Er is ook geen cijfer van 8 of hoger dat ik kan nagaan. Zet het pas live na Daans ja.

**Kan**
- Voeg in `architectuur.md` rijen toe voor `hol/luik.gd` en de lagen in `hol_vast.gd`.
- Controleer dat de gewijzigde `.import`-bestanden (uid verwijderd bij `deco.png`, `holbord.png` en `holkaart.png`, uid veranderd bij `tekens.png`) nergens per uid worden aangeroepen.
- Zet "All bought." en "Heroes drop 2 more gold." als CONCEPT in de spelerstekstlijst.
- Laat de Iris-keuringen door een aparte keurder ondertekenen.
- Het kleine leven tekent op 12 beelden per s, terwijl het ontwerp 10 fps noemt. Dat kost weinig, maar leg het vast.
- Meet het aantal terugkomers voor en na koopgeluk en droogte (Deel A rij 4).

---
Automatische keurder, model `claude-sonnet-5-5`, 99891 tokens in, 8549 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
