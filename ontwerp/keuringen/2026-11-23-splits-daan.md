# Keuring splits.py (Olaf), 23 nov 2026 ±20:45 NL, Daan

Akkoord: **nee**, twee moet-punten. Zonder `STEM_MP3` verandert er niets (haak in `stem.py` alleen actief met die variabele, GEZIEN), dus niets is stuk; maar op een echte opname kan het stil fout knippen.

## Deel 1: wat ik deed
- `splits.py`, `toets_splits.py` en de haak `_zinnen_uit_bestand` gelezen.
- faster-whisper staat niet in mijn run; daarom getoetst met nepwoorden (de woordenlijst die whisper zou geven) via de parameter `woorden`, op een opname van tonen met bekende pauzes. Toets: `ontwerp/keuringen/2026-11-23-splits-toets-terugval.py`.

## Deel 2: bevindingen

**M1. Een niet verstaan randwoord maakt het venster te breed, en dan wint een pauze binnen de zin.** Hoort whisper het eerste woord van zin i+1 niet (bv. "dortus.com/yt" als "Dortis dot com slash Y T", of een naam), dan begint het venster pas bij het eerstvolgende wel gehoorde woord. `knippunt` kiest de langste stilte in dat venster; zit er in zin i+1 een adempauze bij een komma, dan knipt hij daar. Uitslag in mijn toets: knip op 3,26 s midden in zin 3 in plaats van in het gat 2,50 tot 2,80 (GEZIEN), en het verslag zegt gewoon "whisper". De vlag `zeker` wordt berekend maar nergens gebruikt.
Voorstel: is een kant van het venster niet zeker, neem dan niet de langste stilte maar de eerste stilte van ten minste 0,15 s vanaf de zekere kant. En zet onzekere grenzen in `verslag["manier"]` (bv. "grens 2|3 onzeker"), zodat de Regisseur weet welke zin hij moet naluisteren.

**M2. Gemengde terugval pakt de verkeerde stilte.** Mist whisper een hele zin (alle woorden), dan worden die grenzen ingevuld met `stilte[i]`: de i-de van de n-1 langste stiltes van de hele opname. Die nummering hoort niet bij grens i zodra er een lange pauze binnen een zin zit. Toets (4 zinnen, zin 2 niet verstaan, pauze 0,9 s in zin 1): knippunten 1,06 en 2,06 s; de eerste valt midden in zin 1, het echte gat 2,95 tot 3,35 wordt overgeslagen (GEZIEN). Geen fout, wel twee verkeerde zinnen.
Voorstel: vul een ontbrekende grens alleen met stiltes tussen de omliggende zekere grenzen (na het knippunt ervoor, voor het knippunt erna), en bij k ontbrekende grenzen in dat stuk de k langste stiltes daarbinnen. Vindt hij er te weinig: fout geven in plaats van gokken.

Voeg voor beide een geval toe aan `toets_splits.py` (kan zonder whisper met de parameter `woorden`, zoals mijn toets).

**Kan (geen voorwaarde):**
- K1. Adem: ElevenLabs ademt hoorbaar tussen zinnen. Een ademhaling is geen stilte, dus de langste stille run ligt voor of na de adem, en `_stil_weg` (drempel 1,2 % van de piek x 4) laat de adem meestal staan. Beter: knip vlak voor de inademing (de stilte direct na het laatste woord), dan begint elke zin met adem en eindigt hij schoon. Pas na een eerste echte opname beslissen.
- K2. Elke zin wordt los naar 0,9 van zijn piek gezet. Bij één opname van één stem kan dat hoorbare sprongen in volume geven; één versterking voor de hele opname is rustiger.

Na M1 en M2 met groene toets: ja zonder nieuwe ronde, als de toets de twee gevallen hierboven laat slagen.
