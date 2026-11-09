# Productkans Google Workspace: foto's in bulk naar Google Slides

Vera, 9 nov 2026, run 04:31 (Amsterdam). Nagekeken door een controleur: getallen en citaten kloppen, één telling (25 werd 23) en drie aanvullingen verwerkt. Labels: GEZIEN (zelf gemeten), DERDEN (bron met link), GOK.

**Cijfer 3 (eerst 4, na de controle omlaag). Advies: nee voor nu, wel het duidelijkste gat dat ik in de Workspace Marketplace vond.** Er wordt aantoonbaar betaald en de top 3 is zwak, maar de bedragen zijn klein (±$4 per maand bij de nummer één), nieuwkomers stromen al binnen en de onderscheidende punten die wij zouden kiezen zijn al bezet, en Dortus heeft op Google Workspace nog geen account, uploadroute of betaalroute.

## Hoe gezocht
1. Basis: de meting van 7 nov (`data/gwm-detail-2026-11-07.jsonl`, 5.865 add-ons met gebruikers, ster, prijsvorm en datum). GEZIEN
2. Nieuw vandaag: van alle **1.227 add-ons met 100K+ gebruikers** de vermelding opnieuw gelezen en de ±10 zichtbare reviews per add-on bewaard (`data/gwm-kapot-script.py`, uitkomst `data/gwm-reviews-100k-2026-11-09.jsonl`). Geteld: reviews uit 2026 die zeggen dat de add-on niet (meer) werkt, en reviews die over betalen gaan (paid, subscription, refund, premium, $). GEZIEN
   - 507 van de 1.227 hebben een review uit 2026 op de pagina.
   - 23 hebben 3 of meer "werkt niet meer"-reviews uit 2026.
   - 23 hebben 3 of meer reviews over betalen én een ster van 3,6 of lager (ontevreden betalers). De betaaltelling neemt alle zichtbare reviews mee, niet alleen die uit 2026.
3. Per thema (24 thema's op naam) de top 7 met ster, reviews, datum en prijsvorm bekeken, en van 12 kandidaten de reviewteksten gelezen. GEZIEN

## Het gat: foto's in bulk naar Slides
**Wat de gebruiker wil:** een map of album vol foto's in één keer in Google Slides zetten, één per dia of in een raster, met bijschrift. Voor wie: leraren (klassendia's, uitstapjes), fotografen, makelaars, bouwinspecteurs, families (staat zo letterlijk in de vermelding van de nummer één).

**De top 3 (GEZIEN, 7 en 9 nov):**
| Add-on | Gebruikers | Ster (reviews) | Bijgewerkt | Prijsvorm | Hoe sterk |
|---|---|---|---|---|---|
| Photos to Slides (Clay Smith, solo) | 1M+ | 2,4 (104) | 22 okt 2026 | gratis met betaalde functies (abonnement per maand) | **zwak**: 9 reviews uit 2026, waarvan 5 over betalen; "I paid ... it just doesn't work", gratis grens verlaagd van 10 foto's per uur naar 10 per 6 uur, album importeren werkt niet meer |
| Multiple Images, YouTube to Google Slides | 662K+ | 4,6 (192) | 14 feb 2025 | gratis | middel: tevreden, maar sinds 2025 niet bijgewerkt, geen betaald deel, van een "viewer-fabriek" achtig domein |
| Google Photos to Slides (Noodle Street Labs) | 228K+ | 3,2 (36) | 20 jun 2025 | gratis met betaalde functies ($7 voor 3 dagen) | **zwak**: "bait-and-switch", "paid for the upgrade, image quality was severely compressed", geen echte bulk |

**Waarom het nu een gat is:** Google heeft op 31 maart 2025 de Photos Library API ingeperkt: apps zien alleen nog wat ze zelf hebben geüpload, en voor de bibliotheek van de gebruiker moet de nieuwe Picker API (DERDEN: [Google Developers Blog](https://developers.googleblog.com/en/google-photos-picker-api-launch-and-library-api-updates/), [Updates to the Google Photos APIs](https://developers.google.com/photos/support/updates)). Dat verklaart de klacht van september 2026 bij de nummer één: "it will only let me import photos I select, not ... an entire album" (GEZIEN). Een nieuwkomer die vanaf het begin op de Picker API en op Drive-mappen bouwt, heeft dat probleem niet. Het hele album in één klik blijft voor iedereen onmogelijk (GOK op basis van de API-regels); alles kiezen in de Picker kan wel.

**Het gat in één zin:** de mensen die al betalen om foto's in bulk naar Slides te krijgen, krijgen een add-on die vaak niet werkt, de beeldkwaliteit verpest of de licentie niet herkent, en er is geen betrouwbare, mooie betaalde versie.

## Bewijs van betalen (GEZIEN tenzij anders)
- Reviews bij de nummer één, 2026: "i paid for it ... it just doesn't work" (20 aug), "I paid for the program and it never let me upload more than 1 picture" (12 okt), "Good app when you pay for the subscription - handled the 300+ photos" (28 jul, gaat over import in Sheets, zwakker bewijs), "well worth one month's subscription" (14 apr), "when I paid for this (one month)" (27 sep).
- Bij nummer drie: "$7 for unlimited use for 3 days" (jun 2025), "Paid for the upgrade" (aug 2026).
- Wie betaalt: een persoon voor zichzelf, vaak één maand voor één klus (GEZIEN in de teksten). Dus kleine, losse betalingen, geen vaste abonnees (GOK).
- Bedragen: bij de nummer één noemt een review van 27 sep "$4" voor één maand (controleur, GEZIEN), dus ±$4 per maand. Omzet per maand: niet openbaar. Geen van deze makers staat op TrustMRR (de scan van 8 nov vond voor heel Workspace maar 0 tot 2 makers met $300+). Niet te meten zonder inkijk bij de maker.

## Nieuwkomers in dit gat (GEZIEN)
| Add-on | Sinds (eerste review) | Gebruikers op 7 nov |
|---|---|---|
| Photo To Slide Pro (Trawivo) | nov 2025 | 2K+, 5,0 (12) |
| Image Converter for Google Slides | nov 2025 | 189 |
| Bjorn's Photoslides | bijgewerkt okt 2025 | 151 |
| Slides from Photos (DZS Labs) | bijgewerkt 11 okt 2026 | 64 |
| Photo Slides: Bulk Photos (Daily Picks) | bijgewerkt 4 nov 2026 | 50 |

Verder kleine betaalde spelers: Photo to presentation (appwouldwork, 8K+, 2,3, proef), Import Images into Slides en Download Images for Slides (LeadCamp, 5K+ en 7K+, betaalde functies). In de zoekresultaten van de Marketplace staat geen sterke concurrent (controleur).

Een goede nieuwkomer haalt hier dus ±2.000 gebruikers in een jaar; de meeste blijven onder de 200. Daily Picks is een seriemaker (14 add-ons, allemaal okt en nov 2026), net als Single Task Tools (15) en Onibaku (6). Zij vullen gaten in Workspace binnen weken.

## Wat de scan nog meer liet zien (voor later)
- **Kapot sinds juni 2026, gebruikers zonder alternatief:** Sorted Paragraphs (4M, 9 van 10 reviews uit 2026: "stopped working", "only option is Help") en Table of contents van LumApps (4M, 3.113 reviews, idem). Waarschijnlijk een wijziging bij Google rond juni 2026 die oude Docs-add-ons alleen nog het menu Help laat tonen (GOK, oorzaak niet bevestigd). Maar: gratis functies, geen bewijs van betalen, en in okt en nov 2026 kwamen er al minstens 5 nieuwe sorteer- en 5 nieuwe inhoudsopgave-add-ons bij (Onibaku, Single Task Tools, Daily Picks, utilbits, Pocket Tools). Geen kans voor ons.
- **Ontevreden betalers elders:** Page Sizer (122K, 2,2, betaald: "error occurred while verifying the subscription"), Export Calendar Events to Spreadsheet (145K, 2,9: "I paid $20 ... did not recognize that I had paid"), Calendar Events Creator (2M, 2,5: "I paid $239 ... out of Quota"), Copy folder in Google Drive (661K, 3,3), Advanced Find & Replace (216K, 2,2). Steeds dezelfde klacht: **de licentiecheck werkt niet**. Een maker die betalen betrouwbaar regelt, onderscheidt zich hier al. Kalender naar en uit Sheets is wel druk (135 add-ons, 75 met betaalvorm).
- **Music Snippet** (9M, 3,3, $19 per jaar, van Tutteo, het bedrijf achter Flat): muziekleraren klagen dat het gratis was en nu betaald is en soms niet werkt; geen concurrent in de winkel. Interessant, maar het is een bedrijf met een eigen notatie-editor erachter; harde regel: eerst sterker meten.

## Eerste productidee (GOK)
"Photo Deck": kies een Drive-map of foto's via de Google Photos Picker, kies een opmaak (één per dia, 2, 4 of 6 per dia, filmstrip), bijschrift uit bestandsnaam of datum, sorteren op opnamedatum, scheidingsdia's per dag, volle resolutie. Gratis tot 25 foto's per keer; eenmalig $9 voor een maand onbeperkt of $24 per jaar (past bij hoe mensen hier betalen: per klus). Betalen via Stripe of Polar met een licentiecheck die gewoon werkt. Bouwtijd 1 tot 2 weken in Apps Script (GOK).

## Waarom geen ja
0. **Ons idee is al bezet (controleur).** De nummer één zet sinds de update van 22 okt 2026 precies deze functies als betaald op de vermelding: tot 2.000 foto's per keer, raster, filmstrip, collage, sorteren op tijd of naam, bijschriften, titel- en scheidingsdia's, gedeelde Drives. En Daily Picks (4 nov) belooft al "sharp, up to 3840 px, not re-compressed", eenmalige aankoop, geen watermerk. Wij zouden alleen in betrouwbaarheid verschillen, en dat is geen belofte die je op een winkelpagina in één zin waarmaakt.
1. **Geld klein en onzichtbaar.** Betaald wordt er zeker, maar per klus en zonder bedragen. Rekensom (GOK): 2.000 gebruikers per jaar, 3% betaalt ±$4 tot $9 is ±$540 per jaar, ±€40 per maand. Ver onder wat Dortus nodig heeft.
2. **Seriemakers zitten al in het gat**, en de beste nieuwkomer (Trawivo) staat er al een jaar met 5 sterren.
3. **Geen eigen platform.** Workspace vraagt een Google Cloud-project, een Marketplace-vermelding en een OAuth-keuring van Google, op naam van Thijs. Dat is werk voor Thijs en duurt weken (GOK, niet gemeten).
4. Workspace als platform staat op cijfer 5 (7 nov): bereik goed, geld voor nieuwe makers klein. Deze run verandert dat niet.

## Wat het cijfer zou verhogen
- Een maker in deze hoek met een openbaar bedrag boven $500 per maand.
- Als Dortus toch op Workspace komt (bijvoorbeeld voor een ander product), dan is dit een snelle tweede add-on: dezelfde Cloud-, keurings- en betaalroute.

## Herhaalmeting
Niet nodig als aparte taak. Bij een volgende Workspace-herhaalmeting `python3 -I data/gwm-kapot-script.py data/gwm-detail-2026-11-07.jsonl uit.jsonl` opnieuw draaien en de 23 kapotte en 23 ontevreden betaalde add-ons vergelijken.
