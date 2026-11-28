# Rafelrand om de helden: zit in het spel, niet in de opname (Sanne, 28 nov 2026, Daan #358 Moet 1, issue #314)

**Vraag van Daan:** op itch-scherm 2 en 3 hebben de helden een rafelige donkere rand met een lichte geblokte buitenrand. Opname of spel?

**Antwoord: het spel.** Het bronbeeld op ware maat (1920 x 240, uit de film van 46ca6e9) heeft de geblokte lichte rand al, vóór ons opschalen (`scherm3-bron-held-6x.png`, 6x NEAREST uit `../bron6-1376s.png`). Het is de lichte buitenrand van `systemen/held_licht.gd` (Olaf #256): 2 spelpx warm licht buiten de donkere rand, NEAREST. Op hoogte 240 is dat een brede geblokte band.

**Proef (GEZIEN, Godot 4.3 Linux onder Xvfb, main 2e1f5be, `--write-movie --fixed-fps 5`, `hoogte=240 vers=1 zaad=7 balk=0 duur=120 uitleg_klik=6 koper=1 koper_wacht=8`, 0 SCRIPT ERROR):**
`held-240-5x-nu-px1-licht0.png`, twee helden op 5x, van links naar rechts:
1. zoals nu: geblokte lichte band om lijf en hoed (dit zag Daan);
2. `PX := 1.0` (tijdelijk, niet op main): de lichte rand valt bijna helemaal achter de donkere rand, je ziet hem niet meer;
3. `licht=0` (lichte rand uit): alleen de donkere rand van #242. Rustig, de held staat nog los van de muur.
Met `licht_proef=mip` (mipmaps) bleef de band even geblokt, dus het filter is het niet; de breedte is het.

**Besluit Sanne (eigenaar):** de lichte buitenrand gaat standaard uit. Hij gaf het "opgeplakte" en goedkope gevoel dat de blinde tests noemen, en sinds de gedempte grond (#333) en de donkere rand van #242 staat een held ook zonder hem los. Bouwen doet Olaf (#333). Ziet Iris daarna een held wegvallen tegen de blauwgrijze steen, dan een smallere variant, niet terug naar 2 spelpx.

Itch-scherm 2 en 3 zijn opnieuw gemaakt uit een film met `licht=0`, dus zoals het spel straks is (zie `../LEESMIJ.md`). Plaatsen pas als de rand ook op main uit staat.
