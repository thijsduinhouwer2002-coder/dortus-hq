# Keuring Steam-paginaconcept Hats, 21 nov 2026, Iris
Wat ik keurde: `platformen/steam/pagina-concept-2026-11-21.md` (commit 23454d4, Sanne), naast de spelcode op main (bevroren build) en de Steam-gegevens van de drie voorbeelden (zelf opgehaald met curl, 21 nov ±14:40 UTC).
Akkoord: **nee**, om één zin (moet 1). De rest klopt; na die ene wijziging is het ja zonder nieuwe ronde over de rest.

## Deel A: doet het wat beloofd is?
Opdracht hoofdchat 21 nov 12:35: past het bij het spel zoals het nu speelt, is de spelerstekst CONCEPT, kloppen de vergelijkingen met de voorbeelden.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | **Lange tekst, kopje 3: "A hero who got away with your gold returns" klopt niet met de build.** Een held die vlucht neemt geen goud mee: goud komt alleen bij een val (`kern/afloop.gd` regel 93 tot 95), wie vlucht laat zelfs een munt vallen (`systemen/voortgang.gd` regel 45), en `hol.gd` regel 44 zegt "nooit iets kwijt". v3a zei daarom "Nothing was stolen". Voorstel: "A hero who got away returns with ..." (zonder "with your gold"). | feit | hoog | een plek in de code waar `hol.goud` daalt bij een vlucht; die vond ik niet (`goud -` alleen in upgrades) |
| 2 | Rest van de korte en lange tekst klopt met de build: held naar de schat, hap, hoed op Gloop; kroon, chef's hat, bucket en pan staan in `HOED_NAMEN` (`boek.gd` regel 50); Tibbe is een heldennaam en staat op `4-val.png`; nemesis na drie keer vluchten, "about every minute" (held elke 40 tot 60 s), 12 uur weg op lagere snelheid, stil (geen geluid in het spel), "redraws when something moves", geen winkel in het spel: allemaal al eerlijk-gecheckt in `teksten.md` regel 61 tot 85 en niet veranderd in de bevroren build. | feit | hoog | |
| 3 | Tellingen van Sanne zelf nagerekend, GEZIEN: korte tekst 36 woorden en 186 tekens; lange tekst 217 woorden zonder opmaak (zij: ±215). Reviews 13.991 / 7.156 / 2.605, uitgavedata, korte teksten (Tiny Pasture 46 woorden, zij ±45), schermen 6 / 8 / 7, trailers 45,9 / 67,3 / 100,4 s (HLS opgeteld), Cornerpond 0 berichten voor de uitgave, Rusty's 7 voor de uitgave: alles klopt. | feit | hoog | |
| 4 | Scherm 1 van alle drie bekeken (Read): heel bureaublad met witte pijl, bij Tiny Pasture met de zin "Animals live at the bottom of your screen". Tiny Pasture scherm 5 is de code-editor met "Will not affect your work and study". Klopt met haar beschrijving. | feit | hoog | |
| 5 | Tiny Pasture: ik tel 7 aankondigingen vóór 17 feb 2025, zij 8. Verschil zit waarschijnlijk in het bericht op de uitgavedag zelf. Rusty's: eerste aankondiging 30 jan 2024; "pagina ±begin dec 2023" haal ik niet uit het nieuws, dus label GOK of bron erbij. | feit (telling), vermoeden (oorzaak) | midden | de datums van de 8 berichten naast elkaar |
| 6 | "zoals ... 10 van de 13 winnaars van Sem" bij de korte tekst: in `marketing/winkeltekst.md` regel 22 gaat 10 van 13 over "noemt idle", niet over soort plus plek plus "while you work". Kleine overtrekking. | feit | hoog | |
| 7 | Lange tekst heeft 5 kopjes (4 plus het lijstje), het recept zegt 4. Sanne zegt het zelf ("plus één kort lijstje"); prima. "Your dungeon" in kopje 4 tegenover "0 van 13 noemen dungeon": dat geldt voor de korte tekst; in de lange is het niet fout. Thijs kiest al. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alle spelerstekst staat als CONCEPT, met "tot Thijs ja zegt" bovenaan en per blok. | feit | hoog | spelerstekst Hats alleen CONCEPT |
| 2 | Cijfers hebben GEZIEN of GOK; "veel wishlists op paginadag" eerlijk als GOK. Twee kleine punten: A5 (pagina dec 2023 zonder label) en A6. | feit | hoog | GEZIEN/DERDEN/GOK |
| 3 | Bevroren build niet aangeraakt; plek 5 is alleen filmen. Pijl en woorden op scherm 1 komen met de hand op een echte opname, geen AI-beeld. | feit | hoog | geen AI-beeld op Steam |
| 4 | Geen persoonsgegevens; bestand ±100 regels. | feit | hoog | |

## Deel C: zou een koper het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Bureaublad met pijl op plek 1 is de sterkste verandering: in de drie voorbeelden zie je in één tel "dit leeft onderaan mijn scherm". | Pijl groot en wit zoals Rusty's; tekst onder de 5 woorden; strook moet ook in de miniatuur van 600 px breed (zoeklijst) nog te zien zijn. Ik keur hem als hij er is. | klein |
| 2 | Plek 5 "naast echt werk" is goed, maar alleen als er een held of hap in beeld is; een lege strook naast een spreadsheet leest als "er gebeurt niets" (zelfde stilte als mijn keuring 24). | Opname kiezen op een moment met held plus kroniekregel. | klein |
| 3 | De nieuwe korte tekst is duidelijker dan v3a voor wie langs scrolt: soort en plek eerst. Mijn stem: de nieuwe. | | |

## Moet (blokkeert akkoord)
1. A1: "got away with your gold" eruit (het spel verliest nooit goud).

## Kan (mag later)
- A5: Tiny Pasture 7 of 8 rechtzetten; "pagina begin dec 2023" GOK of bron.
- A6: "10 van de 13" aan "noemt idle" koppelen.
- C1, C2 bij het maken van scherm 1 en 5.

## Nakeuring 21 nov ±17:40 UTC, Iris
Sanne 2b1a321 nagelezen: moet 1 opgelost ("A hero who got away returns with a bandage, a nickname and a grudge", geen goud meer). A5 (GOK bij begin dec 2023, 7 vóór 17 feb 2025) en A6 (10 van 13 gekoppeld aan "idle") verwerkt. Rest ongewijzigd. **Akkoord: ja.** Spelerstekst blijft CONCEPT tot Thijs. C1 en C2 keur ik als scherm 1 en 5 er zijn.
