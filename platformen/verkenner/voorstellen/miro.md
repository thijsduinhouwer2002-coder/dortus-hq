# Voorstel: Miro Marketplace (Vera, 8 nov 2026, run 18:33)

**Cijfer: 3. Advies: nee.** De winkel is klein (224 apps, waarvan 73 van Miro zelf), Miro's eigen apps hebben 93% van alle gebruikers, nieuwe apps van andere makers halen bijna niemand (de nieuwste 30: mediaan 19 gebruikers, geen enkele boven 1.000), Miro rekent niet af ("Verify pricing details with the developer") en ik vond geen kleine maker met een bedrag. Een paar kleine makers hebben wel veel gebruikers (Board Translator 35.000), maar dat zijn oudere apps.

## Wat ik mat en hoe
- **Eigen meting (GEZIEN):** de pagina miro.com/marketplace/ bevat de gegevens van alle 224 apps in de winkel: naam, maker, betaaltype, aantal ratings en een gebruikersteller ("Users" op de app-pagina, bijvoorbeeld "Users 35K" bij Board Translator). robots.txt staat lezen toe. De sitemap telt 144 app-pagina's (176 adressen min categorieën), waarvan 7 niet op de hoofdpagina staan; de winkel telt dus ±224 tot 231 apps. Script `data/miro-haal-script.py`, data `data/miro-apps-2026-11-08.json`.
- **Leeftijd:** de pagina toont geen datum. App-ID's van andere makers lopen waarschijnlijk op met de tijd (GOK: de oudste zijn oude koppelingen als Asana Cards Legacy, de nieuwste zoals Oplane hebben "© 2026" op hun site). Voor Miro's eigen apps zegt het ID niets, daarom tel ik alleen de 151 apps van andere makers, in drie delen op ID.
- **Niet gemeten:** wat "Users" precies telt (totaal ooit of actief), en verkopen. Geen TrustMRR-maker gevonden met een Miro-app.

## Cijfers (GEZIEN, 8 nov, 151 apps van andere makers)
| Deel (op app-ID) | Apps | Mediaan gebruikers | 100+ | 1.000+ |
|---|---:|---:|---:|---:|
| Oudste derde | 50 | 1.287 | 42 | 26 |
| Middelste derde | 50 | 615 | 37 | 21 |
| Nieuwste derde | 51 | 76 | 24 | 6 |
| Nieuwste 30 | 30 | 19 | 7 | 0 |

- Betaaltype (alle 224): Free 122, Free and paid 39, gratis bij een betaald Miro-plan 32, Paid with free trial 17, Paid 14. Betaalde apps van andere makers (64): mediaan 544 gebruikers.
- Miro en Miro Labs: 73 apps met samen 93% van alle gebruikers (Teams 3,25 miljoen, Google Meet, Google Drive, Jira).
- Andere makers met de meeste gebruikers (betaald of deels betaald): Brandfetch 63.601 en Drawify 16.945 (bedrijfjes), Board Translator (NanoGiants) 35.247, Mind Map Downloader (CSV Getter) 15.797, Pinterest for Miro 8.229, PowerPack 7.494, Super Search 6.927, Dice Roll (betaald) 4.040.
- Op elke app-pagina: "Verify pricing details with the developer". Miro rekent niet af; de maker regelt zelf betaling.

## De maatstaf
- **Bereik:** slecht voor nieuwkomers: nieuwste 30 mediaan 19 gebruikers, 7 van 30 boven 100, geen boven 1.000 (GEZIEN, als de ID-volgorde klopt).
- **Geld:** niet aangetoond. Geen bedragen gevonden, geen kassa.
- **Wie betaalt:** teams in bedrijven, zou passen bij de koers, maar er is geen bewijs dat ze voor apps betalen.
- **Drukte:** heel rustig, ±224 apps; Miro keurt apps voor de winkel.
- **Vindbaarheid:** de winkel in Miro en de pagina; Miro's eigen koppelingen en oude apps staan bovenaan.
- **Past het bij ons:** bouwen kan in 1 tot 2 weken (web-SDK).

## Voor en tegen
Voor: rustig, zakelijke gebruikers, een kleine maker kan tienduizenden gebruikers halen (Board Translator).
Tegen: nieuwe apps blijven op een handvol gebruikers, geen kassa, geen bewijs van geld, Miro bouwt zelf veel (Miro Labs, AI in het product).

## Wat het zou veranderen
Miro opent betalen in de winkel, of er duikt een kleine maker op met een openbaar bedrag. Herhaalmeting kan altijd met het script: kijk of de nieuwste 30 na 3 maanden boven de 100 gebruikers komen.

## Nagekeken
Controleur (agent, 8 nov): sommen klopten op de eerste JSON, maar het script miste 53 apps met een appKey van letters (bijna allemaal van Miro zelf). Script gerepareerd, alles opnieuw geteld op 224 apps, alleen andere makers in de tabel. Sitemapuitleg verbeterd, Brandfetch en Drawify genoemd. Oordeel controleur: 3, nee blijft; de extra apps laten zien dat Miro zelf het bereik binnenhaalt.

## Cijfer
**3, nee.**
