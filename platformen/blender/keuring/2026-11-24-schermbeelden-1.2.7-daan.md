# Keuring winkelschermbeelden Click Joints Pro 1.2.7 (Daan, 24 nov 2026 ±19:15 NL)

Wat ik keurde: release `pro-schermbeelden-1.2.7`, run 45447954139, commit cd52767 (RUN.txt). Drie PNG's 1920x1080 zelf bekeken op volle maat en verkleind naar 600 px breed, plus `winkel.log`. Dit is ook de keuring die de hoofdchat (16:40) vroeg als "schermbeelden Pro 1.2.6": ze zijn met de 1.2.7-zip gemaakt.
Criteria van de hoofdchat: echt Blender, paneel leesbaar op 600 px, klopt met wat de versie doet, geen AI-figuren, geen "not print tested".

Akkoord: **nee voor w2, ja voor w1 en w3.** Na M1 en M2 mag w2 erbij zonder nieuwe keuring van mij als Olaf het resultaat zelf bekijkt op 600 px.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| A1 | Alle drie echt Blender 5.3.0 (versie rechtsonder, log: "Blender 5.3.0, betaalde zip /tmp/pro.zip"), MakeHuman-figuur, geen render die doet alsof, geen AI-figuur, geen "not print tested". | Feit (GEZIEN) | hoog |
| A2 | w1: lijst in beeld is letterlijk de lijst uit de log (11 joints, 2 rig, 2 mirror, 7 preset; ellebogen 0 tot 140, knieën 0 tot 120, enkels 0 tot 90, ballen ±20). Klopt met de note 1.2.7. Op 600 px: figuur, labels en knoppen goed te lezen, de lijst net (woorden te herkennen). | Feit (GEZIEN) | hoog |
| A3 | w2: Export STL staat nu in beeld. Maar op 600 px is het paneel niet te lezen (interface 1,25x: tekst ±4 px hoog). Juist dit beeld moet de koper laten zien dat het in drie stappen tot een STL gaat. | Feit (GEZIEN, verkleind) | hoog |
| A4 | w2: "Mesh: mens_A_A_A_A_A_A_A_A_A" bovenaan stap 1 leest als een fout in de add-on. Het is de naam van het object in onze scène, niet iets wat Pro doet. | Feit (GEZIEN) | hoog |
| A5 | w2: Exploded view staat aan maar de delen liggen nauwelijks uit elkaar; zonder het blauwe knopje zie je het niet. | Feit (GEZIEN) | hoog |
| A6 | w3: vijf staafjes 0.10 tot 0.30 met hun nummer, bogen 0° en 115°, kop "Bends 0° to 115°", en nu "Print this first: Fit test: ball / Fit test: hinge" in het paneel. Klopt met de winkeltekst (teststrip, vijf spelingen, elk met nummer). Hoofdbericht leesbaar op 600 px. | Feit (GEZIEN) | hoog |
| A7 | w3: paneel zegt Joint "Ball" en "No joint yet" naast een scharnierstrip. Klopt technisch (de strip is een los object), maar oogt tegenstrijdig. | Feit | midden |
| A8 | In de log staan tussenmeldingen "Tight: ... Try a spot further from the end." tijdens Figure from rig; daarna lukte de knop wel (11 joints). Niet zichtbaar in de beelden. Geen gevolg voor deze keuring. | Feit (log) | hoog |

## Deel B: regels
| # | Bevinding | Regel |
|---|---|---|
| B1 | Geen AI-beeld, geen foto die doet alsof het een echte print is. | merk, eerlijk |
| B2 | Geen tekst die iets belooft wat niet in een groene e2e zit. | trots-check |

## Moet (alleen w2)
1. M1: objectnaam van het figuur in de scène wijzigen in iets gewoons, bijvoorbeeld "Human" of "Figure", zodat er geen "mens_A_A_A..." in beeld staat.
2. M2: stap 3 (Good fit, Export STL) leesbaar op 600 px breed. Voorstel, kies zelf: (a) interface 2x en stap 1 inklappen of wegschuiven zodat stap 2 en 3 passen, of (b) een tweede venster-opname op 960x540 bij 1,25x en die 2x opschalen. Kijk het resultaat zelf op 600 px na (skill `kijken`).

## Kan
- K1: w2 exploded view duidelijker: grotere afstand, of de camera zo dat één knie of elleboog groot in beeld komt.
- K2: w3 Joint op "Pin" zetten, zodat het paneel bij de scharnierstrip past. Nieuwe w3 houden (met "Print this first"), niet terug naar de kale.
- K3: de ±20°-labels in w1 en w2 dichter bij de schouders en heupen; nu zweven ze een stuk naast het figuur.
- K4: op Gumroad w1 als eerste beeld: daar is ook de lijst op klein formaat het best te lezen.
