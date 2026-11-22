# Voorstel: Playdate Catalog (Panic)

Vera, 8 nov 2026, run 16:33 (Amsterdam). Nagekeken door een controleur (zie onder).

## Wat is het
De Playdate is een kleine gele handheld van Panic met een slinger (crank) en een 1-bit scherm. Panic verkoopt in de Catalog betaalde spellen en apps van makers. Panic rekent af en betaalt maandelijks uit via Stripe Connect. Elke inzending wordt met de hand gekeurd.

## Cijfers

**Drukte en aanbod**
- 510 titels in de Catalog op 8 nov 2026, waarvan 9 nog "Coming Soon" (GEZIEN: alle lijstpagina's play.date/games/tags/all/?sort=newest, 17 echte pagina's van 30, en alle 510 titelpagina's gelezen).
- Nieuwe titels per jaar: 2023 120, 2024 123, 2025 147, 2026 t/m okt 119. Dat is ±12 per maand (GEZIEN, datum "First published" op elke pagina). Heel rustig vergeleken met alles wat ik eerder mat.
- Mediaanprijs $5 (normale prijs, 491 titels met prijs), maar 2 gratis titels (GEZIEN). Gemiddeld $5,94 volgens Panic (DERDEN, persbericht 26 feb 2026).

**Geld**
- Afdracht: maker houdt 75%, min Stripe-kosten (±2,9% + $0,30). Prijs tussen $1 en $100. Ook elders verkopen mag (DERDEN, https://help.play.date/developer/submit-to-catalog/).
- Hele winkel: 409.003 aankopen, 423 titels en $1.399.393 netto uitbetaald aan makers, stand 24 feb 2026 (DERDEN, https://www.gamespress.com/PANICS-PLAYDATE-GAME-STORE-CELEBRATES-3-YEARS-IN-BUSINESS-WITH-A-SALE-). In april 2025 was dat $1,04 miljoen (DERDEN, niet door de controleur nagekeken). Dus alle makers samen krijgen ±$36.000 tot $39.000 per maand (GOK op die twee cijfers en op het gemiddelde over 3 jaar). Gemiddeld ±$3.300 netto per titel over de hele looptijd.
- Kleine makers die cijfers delen (DERDEN, Bluesky, 4 van 4 nagekeken door de controleur):
  - Echo: The Oracle's Scroll ($8, nieuwe maker 2024): 3.270 verkocht t/m mrt 2025, $15.468 netto over okt 2024 t/m mrt 2025. Uitschieter (prijs Spel van het Jaar in de gemeenschap), maanden zakten van $3,1k naar $1,4k netto. https://bsky.app/profile/bumbleborn.com/post/3llqjcsk7w22g
  - RowBot Rally ($15): 1.111 in ±1 jaar. https://bsky.app/profile/rae.wtf/post/3megdk6qq7c2q
  - Hall of the Dwarf King ($6): 650+ tot dec 2025. https://bsky.app/profile/ldbrart.bsky.social/post/3malkkfqnq22i
  - SpinShot ($6): 130 in de eerste maand, na 3 jaar werk. https://bsky.app/profile/subcide.com/post/3meloglgs6c2d
  - Verder (DERDEN, niet nagekeken): XTRIS 86 in 24 uur, Spirit Trail 100 in een week, HEXA 500 in 4 maanden, weer-app Cloudburst ($5) 500+ in maart 2026, P-Racing 6.300 (uitschieter, cijfer van Panic).
- Gewoon nieuw spel: ±100 tot 150 verkocht in de eerste maand, ±300 tot 600 in 3 tot 6 maanden, dus ±$1.000 tot $3.000 netto bij $5 tot $8 (GOK op ±10 makers; wie geen cijfers deelt, verkoopt waarschijnlijk minder).

**Bereik**
- Geen teller per titel. Wat makers delen wijst erop dat een aangenomen spel bijna altijd 100+ kopers haalt (GOK). Dat is het beste bereik voor betaalde titels dat ik tot nu toe zag, maar alleen voor wat door de keuring komt.
- Het apparaat groeit niet: "over 70,000 Playdates sold", juli 2025, hetzelfde getal als feb 2024 (DERDEN, https://www.gamespress.com/it/PLAYDATE-SEASON-TWO-ENDS-WITH-A-BANG---JUVEE-PRODUCTIONS-TARIA-COMO-AN en timeextension.com feb 2024). Prijs ging in maart 2025 van $199 naar $229. Season 3 begon 8 okt 2026.
- itch.io telt bijna niet meer: makers melden 95% via de Catalog (DERDEN, Goloso Games, bumbleborn 453 tegen 12).

**Vindbaarheid**
- Nieuwe titels komen om de dinsdag in een "drop" in de Catalog-app op het apparaat. Panic kiest wat groot uitgelicht wordt. Verder de verlanglijst met saleseinden, grote sales (nu 5 tot 19 nov), Community Awards en de Playdate-showcases (DERDEN, help.play.date). Bijna geen pers.

**AI-regel (belangrijk voor ons)**
- Sinds april 2026: "Catalog will no longer accept titles that use Generative AI for art, audio, music, text, or dialog." AI-hulp bij code mag voorlopig, met een label op de pagina. Alles "subject to change at any time" (GEZIEN, https://help.play.date/catalog-developer/ai-disclosure/).
- In de praktijk: van de 66 titels sinds mei 2026 melden er 18 (±27%) AI-hulp bij code, en Panic nam ze aan (GEZIEN, controleur).
- Graphics die door code getekend worden (vormen, 1-bit) en geluid uit de synth-API zijn een grijs gebied: niet duidelijk verboden, maar als de AI feitelijk het uiterlijk of de muziek bedenkt kan een keurder dat als AI-art zien. Tekst in het spel van een LLM is wel verboden.

## Voordelen
- Geld voor kleine makers aantoonbaar, per titel beter dan bijna alle eerder gemeten winkels.
- Heel rustig (±12 nieuwe titels per maand), en elke titel krijgt aandacht in een drop.
- 75% voor de maker, Panic doet betaling en belasting.
- Een klein Lua-spel of app is in 1 tot 2 weken te bouwen; de SDK en simulator draaien op Linux (GOK, nog niet geprobeerd op GitHub Actions).

## Nadelen
- Het plafond is klein: alle makers samen ±$36.000 per maand, ±70.000 apparaten die niet meer groeien. Hier word je geen grote speler, hooguit een van de betere kleine.
- AI-regel: art, geluid en tekst moeten van mensen komen of ontwerp moet duidelijk door een mens gekozen zijn. Een mens inhuren kost geld.
- Keuring met de hand ("one of the best in your genre"), 1 tot 3 weken; afwijzing kan.
- Thijs moet een Catalog-account, Stripe Connect en belastingformulier regelen, en zou een Playdate moeten hebben om op een echt apparaat te testen (Panic vraagt dat).
- Gemeenschap is gevoelig voor AI; een label "AI-hulp bij code" kost kopers (GOK).

## Wat we zouden bouwen (eerste idee)
Een rustige app of puzzel die de slinger slim gebruikt en bijna geen tekst heeft, met strakke 1-bit vormen die een mens kiest. Bijvoorbeeld een nuttige app zoals Cloudburst (weer, 500+ verkocht): een slinger-timer of focusklok met veel zorg voor het gevoel. Eerlijke AI-verklaring: code met AI-hulp.

## Cijfer en advies
**4 van 10: nee voor nu.** Geld is aangetoond en het bereik per aangenomen titel is goed, maar het hele potje is klein, het apparaat groeit niet, en de AI-regel maakt het voor een ploeg Claudes onzeker. Thijs zoekt een plek waar Dortus groot kan worden; dat kan hier niet.

Een goedkope proef van één kleine app kan later, als er tijd over is en een mens het ontwerp kiest. Opnieuw kijken als: Panic een nieuw apparaat of grote groei meldt, of de AI-regel versoepelt.

## Controleur
Akkoord met de kern, cijfer "4 tot 5, eerlijk, misschien een halve punt te streng". Correcties verwerkt: 510 titels (niet 496, mijn ophaalscript was nog bezig), 2 gratis (niet 19: 9 Coming Soon en 8 alleen in Season 3), 18 van 66 nieuwe titels met AI bij code (niet 6 van 65, ik miste vrije teksten), uitbetaald bedrag is netto, Echo in dollars en als uitschieter. Ik hou 4: geld weegt net zo zwaar als bereik, maar het plafond van de hele winkel is te laag voor "groot worden".

## Bestanden
- `data/playdate-analyse-script.py` (leest de titelpagina's, maakt tabel en tellingen)
- `data/playdate-catalog-2026-11-08.json` (510 titels: datum, prijs, AI-tekst)
- `data/playdate-controleur-rijen-2026-11-08.txt` (telling controleur)
