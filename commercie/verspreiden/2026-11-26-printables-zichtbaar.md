# Printables: onze gratis strip staat niet in de zoekuitslag (Verspreider, run 27, do 26 nov 2026, C)

**Status:** keuring Daan gevraagd. Na zijn ja: klaar voor de hoofdchat (Printables-account van Dortus, ingelogd in Chrome op de HP). Niets onder de naam van Thijs, dus geen bundel voor Thijs. Niets geplaatst of veranderd.

Rooster C (eigen mensen). De Fit test strip op Printables is onze gratis ingang voor mensen die printen: hij staat in elke mail aan makers (7 verstuurd op 26 nov, `commercie/geplaatst.md`), in de bundels voor 27 tot 29 nov, in de Reddit-teksten en in de tekst voor de tien testers. Als hij niet te vinden is en er een AI-teken op staat, lekt daar het effect van al dat werk weg.

## Wat ik zag (GEZIEN, Printables-API met curl, 26 nov ±15:10 NL)
- Model 1929497 "Ball Joint Tolerance Test, 0.10 to 0.30 mm": **0 downloads, 0 likes, 0 makes**, account 0 volgers. Gepubliceerd 25 nov 21:51 UTC (na het terugzetten naar concept), dus ±17 uur.
- **Hij komt niet in de zoekuitslag**, ook niet op zijn eigen exacte naam (`searchPrints2(query:"Ball Joint Tolerance Test, 0.10 to 0.30 mm")` geeft 0 uitkomsten). Ter vergelijking: "Hinge Pin Tolerance Test" (1925065, 22 nov) komt wel, net als de verse "Heatsetinserts Tolerance Test" (1930040, vandaag 10:53 UTC). Op "tolerance test", nieuwste eerst, staan wel modellen van vandaag, die van ons niet.
- Categorie Test Models en de tags (tolerance, balljoint, poseable, blender) staan goed.

## Waarom waarschijnlijk (GOK, met wat ik wel weet)
- Het model staat op "AI-assisted" (`commercie/geplaatst.md`, 25 nov: "het Blender-script is met hulp van AI geschreven. Er staat nu een klein AI-icoon op het hoofdbeeld"). Op Printables kan elke bezoeker AI-inhoud verbergen (Settings, Display & Privacy, AI Content, Hide content) en er is een filter "exclude AI generated" bij het zoeken (DERDEN, Prusa-forum, https://forum.prusa3d.com/forum/english-forum-general-discussion-announcements-and-releases/printables-filter-out-ai-models/). Op dat draadje noemen makers AI-modellen "garbage" en "who wants to see this crap", en zeggen ze dat ze modellen met het AI-teken meteen overslaan (DERDEN, zelfde link). Of het teken ons ook uit de gewone zoekuitslag haalt, kan ik met curl niet zien: GOK, maar het is de enige afwijking die ik vind.
- Andere mogelijkheid: het nieuwe account of het terugzetten naar concept houdt het model even uit de zoekindex. Ook GOK.
- Los van de oorzaak botst het teken met onze eigen regel "Nergens AI vermelden" (CLAUDE.md regel 5): het icoon staat zichtbaar op ons hoofdbeeld, op het kanaal waar wij gevonden willen worden door printers.

## Voorstel voor de hoofdchat (±5 minuten, in Chrome op de HP)
1. **Kijk uitgelogd** (privévenster) op https://www.printables.com/search/models?q=ball%20joint%20tolerance of ons model verschijnt. Zo ja: dan is het alleen de API of de index, en stap 2 is alleen nog voor het teken.
2. **Lees de regel van Printables zelf:** https://help.prusa3d.com/article/printables-ai-tag-rules-guidelines_1306155 (de pagina laadt alleen in een browser; met curl komt er geen tekst). Vraag: geldt het AI-label voor een model waarvan de vorm uit ons eigen Blender-script komt (vijf bollen en kommetjes met vaste maten) en de beelden renders uit Blender zijn, als alleen het script met hulp is geschreven?
   - **Zegt de regel dat het label gaat over vormen of beelden die een AI-generator maakte:** zet het label op nee. Dat is dan de eerlijke keuze, want de vorm en de beelden komen niet uit een generator. Schrijf de reden in één regel in `commercie/geplaatst.md`.
   - **Zegt de regel dat ook hulp bij code telt:** laat het label staan (eerlijk boven alles). Dan rekenen we niet op zoekverkeer van Printables; de strip werkt dan alleen via directe links in mails en posts, en dat zeg ik in de volgende run aan wie ermee rekent.
   - Twijfel: laat het staan en meld het aan Thijs in het dagrapport, één regel.
3. **Saleregel onder "Make your own joints"** (mag op Printables: een gratis Blender-add-on met betaalde versie in de beschrijving is er gewoon, DERDEN, TrailPrint3D, model 1242540, zie `2026-11-23-printables.md`). Zet hem vr 27 nov aan het eind van het Pro-punt en haal hem wo 2 dec weg:
```
25% off until December 1.
```
   Geen code nodig: CYBER25 staat automatisch aan bij het afrekenen (dortus.com/click-joints zegt "applied at checkout", GEZIEN curl 26 nov).

## Bewust niet
- Geen nieuwe beelden of een tweede model: eerst weten of het eerste gezien wordt.
- Geen tekst in de beschrijving over AI of over hoe het script gemaakt is: daar gaat het label over, niet de tekst.
- Niet zelf iets aanpassen: inloggen mag ik niet, Printables is een kanaal van de hoofdchat.

## Meten
Printables-API (`print(id: 1929497){ downloadCount likesCount makesCount }`) en of het model in `searchPrints2` op "ball joint tolerance" verschijnt; Gumroad-verwijzers met `utm_source=printables`. Ik kijk elke run. Staat hij na de wijziging op 3 dec nog op 0 downloads én buiten de zoekuitslag: Printables als zoekkanaal stoppen en dat zeggen.
