# Houweel, ton en wortels in de kamer groter met donkere rand (Mila, 26 nov 2026)

Aanleiding: Iris op #179 (build 3fddb22, mooi 7): "wortels, haakjes en schappen zijn 4 tot 8 px en bijna wandkleur; liever minder maar groter en met een donkere rand, zoals vat en schedel."

## Wat er veranderde (3D uit code in Blender, geen AI, geen gekocht pakket)
- `modellen/hol.py`, kamerstuk `kamer_midden_b`: het houweel was een wit streepje op een dun stokje. Nu een dikke lichte steel en een gebogen ijzeren kop met twee punten; de ton is groter (lichter hout, gouden banden). Beide met een donkere omtrek (omgekeerde schil, zoals de worm en de mot).
- `modellen/versiering.py`, `wand_wortels`: twee wortels in plaats van drie, bijna anderhalf keer zo dik, lichter room, met donkere omtrek.
- De stut (`kamer_midden_a`) is NIET veranderd: dikker met omtrek las hij bij de blinde lezer als tafel, ook in een tweede vorm met schuine poten. Hij blijft zoals hij was tot er een vorm is die als mijnraam leest.
- Bladen opnieuw gerenderd met de pijplijn (`pijplijn/render.py hol_proef deco`, volle kwaliteit): alleen `kamer_midden_b` en `wand_wortels` veranderen echt; de andere stukken wijken hooguit 6 van 255 af (ruis), maten in `sprites.json` gelijk. Geen code in het spel nodig.

## Beelden
- `voor-en-na-1x.png` (ware maat, strook 120) en `voor-en-na-2x.png`: boven build 3fddb22 van Iris, onder dezelfde schermafbeelding met de nieuwe stukken erin geplakt. Licht per plek nagedaan (winst per rij = scherm gedeeld door het oude stuk op die plek); de oude wortels weggepoetst met de kale wand een tegel verder. Dus ingeplakt, niet uit het spel zelf.
- `na-heel-1x.png` en `na-heel-2x.png`: het hele beeld na.

## Blinde lezer (GEZIEN, 26 nov, een losse Claude zonder hint, alleen de uitsnede van de kamerrij, eerst 1x dan 2x)
- Houweel met ton: 1x "pickaxe leaning on a brown crate/barrel". Voorheen las Iris het als "haakje".
- Wortels: 1x "roots" (tweede gok "bones"), 2x "roots (ceiling, branching, cream colored)".
- Stut in de proefvorm: "small TABLE or workbench, not a support beam". Daarom teruggezet.
