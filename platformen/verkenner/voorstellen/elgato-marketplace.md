# Elgato Marketplace (Stream Deck-plugins, iconen, profielen)

Vera, 7 nov 2026, run 18:33. Voorwerk in run 17:32. Zelf toegevoegd.

## Advies: nee voor nu, cijfer 3

De winkel is heel druk en groeit snel, en betalen zit erin (70% voor de maker). Maar ik kan niet zien hoeveel een nieuwe plugin wordt gedownload of verkocht: de winkel toont dat nergens, en ik vond geen enkele kleine maker die een bedrag noemt. Het enige harde geldsignaal is slecht: BarRaider, de bekendste maker van Stream Deck-plugins (tientallen plugins), haalt op Patreon $14 tot $87 per maand. Zonder bereik of geld te kunnen meten kan het geen 6 worden. Zo bleef ook de indruk van 6 nov staan ("Stream Deck zwak of te klein").


## Herhaling 17 nov 2026 (nachtscan, run 00:31 NL): blijft nee, cijfer 3

Vraag van de hoofdchat (17 nov 00:05): zijn betaalde plugins van kleine makers zichtbaar met downloads of beoordelingen, en hoe lang duurt de keuring echt?

**Nieuw: de lijst achter de site is nu wel leesbaar** (`https://mp-gateway.elgato.com/products?extension=plugins`, open, zonder sleutel). Volledige plugin-lijst opgeslagen in `data/elgato-plugins-2026-11-17.json`.
- 1.871 plugins, waarvan **781 betaald** (42%), allemaal eenmalig; mediaanprijs $5,99, middelste helft $3,99 tot $9,99 (GEZIEN).
- **Het aanbod explodeert:** nieuwe plugins per maand jan 28, apr 81, jul 145, aug 159, sep 242, **okt 368 (237 betaald)**, 1 t/m 16 nov al 75 (GEZIEN, `created_at`). 665 van de 781 betaalde plugins zijn sinds mei 2026 gemaakt.
- 237 makers met iets betaalds; de top 10 heeft 309 van de 781 (40%). GRAMSHIFT 76, PackRat 47, Pathfinder Prototyping 43, 7bp Solutions 37. 149 makers hebben er precies één (GEZIEN). GOK: veel hiervan is met AI in serie gemaakt.
- **Downloads, verkopen en beoordelingen staan ook in de API nergens.** Ook de productpagina in de API (`/products/<id>`) heeft geen teller, en sorteren op populariteit bestaat niet (alleen datum, naam, prijs) (GEZIEN, getest met 10 sorteringen).
- **Geen enkele maker noemt een bedrag of aantal** voor 2025/2026. Doorgelezen (agent, via Arctic Shift): r/StreamdeckPlugins (39 posts), r/streamdeckprofiles (281 posts, 1.279 reacties), r/elgato (titels met marketplace of maker console), r/SideProject, r/indiehackers, r/EntrepreneurRideAlong, r/Twitch, en Hacker News. Lanceerposts van betaalde plugins krijgen 0 tot 1 reactie (bijv. Smart Remote+ £3,99, Screen FX $3,50, sep 2026). Kopers klagen over prijzen van $12 tot $35 voor profielen, één gaat ze zelf met Claude Code maken (apr 2026) (GEZIEN).
- **Keuring:** "allow 4 to 10 working days", elk product en elke versie, max 3 tegelijk in de wachtrij, alles in het Engels (GEZIEN, https://docs.elgato.com/maker-console/review-process). Een maker (r/elgato, sep 2026) noemt aanmelden "very straight forward", eerste inzending afgekeurd om icoonstijl en tekst (GEZIEN).
- **Wat Thijs eenmalig moet doen:** Elgato-account, organisatie in Maker Console, Maker Agreement tekenen, Stripe Connect koppelen via een link van Elgato (identiteit en bank, staat bij Thijs). Geen kosten gezien, geen wachtlijst (GEZIEN, docs.elgato.com/marketplace/become-a-maker en /monetization/stripe).
- **Vindbaarheid:** sinds Stream Deck 7.1 (dec 2025) zoeken in de app zelf. "What's Hot on Marketplace" bestaat alleen voor okt 2026 (andere maanden 404): 8 producten, alle 8 betaald en van kleine makers, 7 pas 1 tot 7 weken oud (GEZIEN). Dat is de enige zichtbare duw voor nieuwkomers.

**Oordeel:** de route is snel en goedkoop (tijd tot de winkel ±1 tot 2 weken door de keuring, bouwen in TypeScript kan in de cloud, testen op een echt apparaat niet). Maar het blijft blind: geen enkel bewijs van kopers, en het aanbod is in een half jaar vervijfvoudigd met betaalde plugins van $4 tot $10. De explosie kan betekenen dat makers geld zien (GOK) of dat AI-reeksen de winkel vullen (GOK); niets wat ik kan zien onderscheidt die twee. Voor de nachtscan ("bewijs van kopers") haalt het daarom de top 5 niet. **Cijfer blijft 3.** Hoe het wel te meten is: één goedkope plugin uitbrengen en de analytics in Maker Console lezen (vraagt account via Thijs), of de makers van "What's Hot" om cijfers vragen (posten, dus via de hoofdchat).

## Cijfers

### Geld
- Verdeling 70/30: de maker krijgt 70%, Elgato 30%. Uitbetaling via Stripe Connect naar de bank (DERDEN, https://docs.elgato.com/monetization/revenue-share/, gelezen 7 nov 2026). Nederland kan via Stripe Connect.
- Prijzen: steekproef van 400 producten (alle soorten) heeft een mediaanprijs van ±$8 bij de betaalde (GEZIEN, `data/elgato-steekproef-2026-11-07.json`, run 17:32). Bij $8 is dat ±$5,60 per verkoop; voor € 350 per maand zijn ±65 verkopen per maand nodig (GOK op GEZIEN).
- Kleine makers met een bedrag: **niet gevonden**. Zoeken op het web gaf alleen de uitleg van Elgato zelf (DERDEN, zoekopdrachten 7 nov).
- BarRaider (makers van veel gratis plugins sinds 2019) op Patreon: 10 betalende leden, $14 tot $87 per maand, gestart juli 2020 (DERDEN, https://graphtreon.com/creator/barraider, gelezen 7 nov 2026). De grootste maker haalt met donaties dus bijna niets.

### Bereik
- De winkel toont geen downloads, geen verkopen en geen beoordelingen, niet op de productpagina en niet in de lijst die de site zelf laadt (GEZIEN, productpagina en lijst bekeken).
- Ik heb geprobeerd uit te zoeken of de lijst achter de site meer prijsgeeft. Dat weigerde de veiligheidscontrole; niet omzeild. Mediaan en percentage 100+ zijn dus **niet te meten**.
- Hoe het wel kan: een eigen gratis plugin uitbrengen en de eigen cijfers in de Maker Console bekijken, of makers vragen naar hun cijfers (Discord van Elgato-makers, via Thijs).

### Drukte
- De site zelf telt 1.798 Stream Deck-plugins (GEZIEN, teller van de lijst op marketplace.elgato.com/stream-deck/plugins). De sitemap telt 5.817 producten van alle soorten (GEZIEN, run 17:32).
- Van de 400 producten in de steekproef is 58% in 2026 gemaakt; sep en okt samen 105 van de 400 (GEZIEN). Voor de hele winkel ±700 nieuwe producten per maand, waarvan ±230 plugins, ±de helft betaald (GOK op GEZIEN).
- Dat is snel: ±230 nieuwe plugins per maand bij 1.798 in totaal klopt alleen als veel ervan iconen of profielen in de pluginsoort zijn, of als de groei heel recent is. Niet nagekeken, daarom GOK.

### Vindbaarheid
- Gebruikers zoeken in de winkel en in de Stream Deck-app; de standaardvolgorde is "laatst bijgewerkt", dus een nieuwe plugin staat even bovenaan en zakt dan weg tussen ±230 nieuwe per maand (GEZIEN, volgorde van de lijst; GOK voor het effect).
- Elgato licht maandelijks producten uit ("What's hot on Marketplace", DERDEN, https://www.elgato.com/explorer/products/marketplace/whats-hot-on-marketplace-october-2026/).

### Past het bij ons
- Een plugin is JavaScript/TypeScript met de Stream Deck SDK; in 1 tot 2 weken te bouwen (GOK). Echt testen kan alleen met de Stream Deck-app (Windows of Mac), niet op GitHub Actions zonder meer.
- Kopers hebben al een Stream Deck van ±$80 tot $250 gekocht, dus de wil om te betalen is er waarschijnlijk (GOK).

## Voor- en nadelen
- Voor: betalen ingebouwd, Stripe, open voor iedereen, groot publiek (streamers, kantoor), snel groeiend.
- Tegen: niets te meten, 30% afdracht, lage prijzen (±$8), heel veel nieuw aanbod, het grootste gratis aanbod komt van Elgato zelf en bekende makers, geen kleine maker met een bedrag.

## Eerste idee (als het ooit ja wordt)
Een betaalde plugin die een veelgebruikte zakelijke app bestuurt die nog geen goede plugin heeft (bijvoorbeeld een agenda- of vergaderknop die laat zien wat er nu is). Eerst nagaan wat er al is.

## Wat zou het veranderen
- Twee kleine makers die een bedrag van $300+ per maand uit de winkel delen.
- Of Elgato gaat downloads of verkopen tonen, of Thijs geeft toestemming om het via de Maker Console met een eigen gratis plugin te meten.

## Nagekeken
Geen controleur ingezet: er zijn geen eigen cijfers over bereik of geld om na te kijken, de uitkomst is "niet te meten" plus één bron van derden (graphtreon). Zelf twee keer nagelezen.
