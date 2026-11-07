# Elgato Marketplace (Stream Deck-plugins, iconen, profielen)

Vera, 7 nov 2026, run 18:33. Voorwerk in run 17:32. Zelf toegevoegd.

## Advies: nee voor nu, cijfer 3

De winkel is heel druk en groeit snel, en betalen zit erin (70% voor de maker). Maar ik kan niet zien hoeveel een nieuwe plugin wordt gedownload of verkocht: de winkel toont dat nergens, en ik vond geen enkele kleine maker die een bedrag noemt. Het enige harde geldsignaal is slecht: BarRaider, de bekendste maker van Stream Deck-plugins (tientallen plugins), haalt op Patreon $14 tot $87 per maand. Zonder bereik of geld te kunnen meten kan het geen 6 worden. Zo bleef ook de indruk van 6 nov staan ("Stream Deck zwak of te klein").

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
