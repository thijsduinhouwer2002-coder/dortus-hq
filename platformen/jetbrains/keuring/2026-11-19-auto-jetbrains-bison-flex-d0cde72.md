# Keuring jetbrains-bison-flex architectuur.md (beeldvergelijking R4), 19-11-2026, automatische keurder
Wat ik keurde: commit d0cde729 (e188628..d0cde72), alleen `producten/jetbrains-bison-flex/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Dit is een documentatiewijziging, geen verandering aan de plugin. De belofte op de winkelpagina en de eisen uit `ontwerp.md` zijn dus niet geraakt.

| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt geen plugincode, winkeltekst of eis uit het ontwerp. De belofte (Bison/Yacc en Flex/Lex, grammatica en scanner verbonden, gratis en Pro) blijft zoals Daan haar keurde. | Feit | hoog | Het diff bevat één regel in één Markdown-bestand. |
| 2 | De commitboodschap zegt "GEMELD.md blijft staan, oudere code overschrijft geen nieuwere referentie". Dat is een gedragswijziging in `beelden.sh` of de workflow. Die bestanden zitten niet in deze wijziging. | Vermoeden | midden | De wijziging zit in een andere commit of in een ander deel van de repo. Zie `organisatie/controle/beelden.sh` en de workflow. |
| 3 | De tekst zegt dat het beeldbericht aan Chris voor dit product nog uit staat, met reden: 2 plaatjes blijven groot door timing, met twee run-nummers erbij. | Vermoeden | midden | Of de uitzetting echt in `beelden.sh` of de workflow staat, en of de run-logs 44427732156 en 44427918561 de twee genoemde plaatjes tonen. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen tests aangepast. Er is niets anders dan dit ene Markdown-bestand gewijzigd. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt in dezelfde commit als de gedragsbeschrijving. De reden en de run-nummers staan erbij, met GEZIEN. | Feit | hoog | architectuur.md bijgewerkt, cijfers met GEZIEN/DERDEN/GOK |
| 3 | De nieuwe alinea is deels dubbel en tegenstrijdig. Eerst staat dat het beeldbericht uit staat. Daarna staat er nog een restzin over "op main één kort bericht per run in `berichten/chris.md`" alsof het aan staat. Daarin staat ook "daarboven een verschilbeeld als artefact" twee keer. | Feit | hoog | Documentatie moet kloppen (architectuur.md) |
| 4 | Het getal "ruis onder 0,12 procent" heeft geen eigen bron. Het valt wel onder de GEZIEN-run-nummers in dezelfde zin. | Vermoeden | laag | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 6 | Of `architectuur.md` onder ±400 regels blijft, is uit de tekst niet te zien. Het bestand heeft zeer lange regels en de wijziging maakt één regel nog langer. | Vermoeden | laag | Bestanden onder ±400 regels (`wc -l`) |
| 7 | Geen spelerstekst van Hats en geen AI-beeld of -geluid. Niet van toepassing. | Feit | hoog | Hats-concept, geen AI-beeld op Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- Geen.

**Kan**
- Haal de restzin in de alinea weg of herschrijf hem, zodat er één lezing overblijft: het beeldbericht aan Chris staat nog uit, het verslag en het artefact zijn er wel. Nu staat er ook "op main één kort bericht per run" alsof het aan staat.
- Zet in de commit of in de tekst waar de codewijziging uit de boodschap staat ("GEMELD.md blijft staan, oudere code overschrijft geen nieuwere referentie"). Anders kan een lezer niet nagaan dat de beschrijving klopt met de code.
- Zet een label (GEZIEN) bij "ruis onder 0,12 procent", of verwijs naar het verslag `BEELDVERSCHIL.md`.
- Splits de lange alinea over week-test en beeldvergelijking in korte punten. Dat houdt het bestand leesbaar en onder de regelgrens.

---
Automatische keurder, model `claude-sonnet-5-5`, 20222 tokens in, 2797 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
