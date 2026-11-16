# Marktkaart betaalde Garmin-wijzerplaten (Vera, 16 nov 2026)

Opdracht: hoofdchat 16 nov 12:10 (`berichten/vera.md`), voor Gijs en Mila. Alles is GEZIEN (eigen meting uit de open winkel-API van Garmin, 16 nov 11:35 tot 11:55 UTC) tenzij er GOK of DERDEN staat. Ruwe data: `data/garmin-wijzerplaten-betaald-2026-11-16.csv` (5.701 betaalde wijzerplaten, alleen productgegevens). Scripts: `data/garmin-wijzerplaten-haal-script.py`, `-details-script.py`, `-analyse-script.py`. Nagekeken door een controleur (agent): alle zes kerngetallen opnieuw uitgerekend en gelijk, drie rijen live nagekeken en gelijk.

## Kort
1. **Prijs: $2,99 voor Gloop en voor Ebb.** Bij kleine makers verkoopt $1,99 niet vaker dan $2,99 of $3,99 (100+ bij 42% tegen 37%), maar een wijzerplaat van $2,99 tot $3,99 levert per stuk meer op. $4,99 werkt alleen voor makers met een naam (VAW.BE, Garmin), boven $5 zakt het hard (17%).
2. **Een figuurtje alleen verkoopt slechter.** Betaalde wijzerplaten met een dier of figuur halen half zo vaak 100+ als zonder (6,5% tegen 13,0%; bij kleine makers 21,8% tegen 39,6%). Een grap alleen: 22 betaalde, geen enkele haalt 100+. Wie met een figuur wel verkoopt (VAW.BE Goals Pro, Seasons Premium, Atelier_Dev Purrtime) zet het figuur bovenop een volle sportwijzerplaat.
3. **De drie dingen die Gloop en Ebb moeten hebben:** (a) zelf velden kiezen en kleuren kiezen, met de gegevens die sporters zoeken (Body Battery, weer, stress, hartslag); (b) slaapstand (AOD) en aanraken; (c) een winkelpagina met een filmpje, 5 schermbeelden, een lange uitleg en meer dan één taal. Zie de tabel onder "Wat de verkopers anders doen".
4. **Makers met een reeks winnen, fabrieken niet.** Makers met 4 tot 20 wijzerplaten per jaar: 39,8% haalt 100+. Fabrieken met 200+ per jaar: 1,3%. De sterke reeksmakers hebben bij bijna elke betaalde een gratis broertje en bouwen op een eerdere hit verder (Goals 9 naar Goals Pro, Cockpit I, II, III).
5. **Eerlijk over de scheefheid:** de mediaan van alle betaalde wijzerplaten is 1 download. Eén maker (TitanicTurtle, 6 betaalde) haalt 45% van alle geschatte omzet, de top 10 samen 74%. Een gewone wijzerplaat van een kleine maker brengt in zijn eerste maanden mediaan ±$25 op, een kwart haalt ±$190 of meer.

## Hoe gemeten
- Lijst `sortType=MOST_RECENT&appType=watchface` (30 per pagina, 3 tegelijk met een pauze): 13.481 wijzerplaten. Die lijst bleek gaten te hebben (juli tot oktober 2026 grotendeels weg, de volgorde is niet op datum). Daarom de betaalde wijzerplaten uit de dataset van 6 nov (`data/garmin-nieuw-sinds-jun2025-2026-11-06.json`) die ontbraken één voor één opgehaald via `/apps/<id>`: 2.708 erbij, 13 bestaan niet meer.
- Samen: **5.701 betaalde wijzerplaten met eerste goedkeuring 16 nov 2025 tot 16 nov 2026**, met prijs, downloadklasse, reviews, beschrijving en makernaam van vandaag. Wat na 6 nov uitkwam én niet in de lijst stond, mist; dat zijn alleen hele jonge wijzerplaten.
- **De downloadteller is een klasse** (0, 1, 10, 100, 1.000 ...). Ik reken met de ondergrens, dus omzet is een ondergrens. Een download is niet altijd een verkoop (sommige waren eerst gratis); de omzet is daarom een GOK op basis van GEZIEN-tellers: klasse × prijs × 0,85 (Garmin houdt 15%, DERDEN: developer.garmin.com, App Sales).
- "Minstens 3 maanden oud" = eerste goedkeuring vóór 16 aug 2026 (2.752 stuks). Succescijfers hieronder gaan daarover, tenzij anders vermeld.
- "Figuur" en "grap" en de functies zijn gezocht op woorden in naam en beschrijving (Engels). Steekproef van 20 "figuur": 17 terecht. Dat geeft een richting, geen precieze maat. Alle 5.701 hebben geen proefstand (`hasTrialMode` 0).
- Gratis wijzerplaten tellen alleen mee voor de grootte van de maker; de gratis van juli tot oktober zijn onvolledig.

## Cijfers

### Alle betaalde wijzerplaten
| Groep | Aantal | Mediaan downloads | 10+ | 100+ | 1.000+ | 10.000+ | Mediaanprijs |
|---|---|---|---|---|---|---|---|
| Betaald, laatste jaar | 5.701 | 1 | 34% | 9,9% | 1,8% | 0,18% | $2,25 |
| Betaald, minstens 3 mnd oud | 2.752 | 1 | 44% | 12,5% | 2,9% | 0,36% | $2,25 |
| Gratis, minstens 3 mnd oud (ter vergelijking) | 6.386 | 10 | 85% | 22,6% | 2,6% | 0,08% | |

Nieuwe betaalde per maand: dec 258, jan 294, feb 326, mrt 281, apr 356, mei 365, jun 402, jul 258, aug 364, sep 769, okt 808, nov (1 tot 16) 1.171. **Het aanbod is sinds september twee tot drie keer zo groot.** Van de lichting aug tot okt haalt bij kleine makers nu 9,9% 100+, tegen 37 tot 46% bij oudere lichtingen; dat komt deels door de leeftijd (ze zijn 1 tot 3 maanden oud), deels door de drukte. Niet uit elkaar te halen met één meting.

### Prijs
| Prijs | Alle (3 mnd+): n, 100+ | Kleine makers (≤20 per jaar): n, 100+, 1.000+ | Kleine makers: omzet per wijzerplaat mediaan, 75e percentiel (GOK) |
|---|---|---|---|
| $1,99 | 1.314, 11,6% | 226, 42,0%, 13,7% | $17, $169 |
| $2,00 tot $2,49 | 999, 7,1% | 79, 36,7%, 11,4% | $21, $212 |
| $2,50 tot $2,99 | 214, 27,6% | 95, 36,8%, 6,3% | $25, $254 |
| $3,00 tot $3,99 | 106, 35,8% | 65, 36,9%, 4,6% | $34, $297 |
| $4,00 tot $4,99 | 75, 24,0% | 40, 32,5%, 17,5% | $42, $424 |
| $5 en meer | 43, 9,3% | 24, 16,7%, 4,2% | |

Lees de linkerkolom niet als "duurder verkoopt beter": de fabrieken zitten bijna allemaal op $1,99 tot $2,49 en halen bijna niets. Bij kleine makers is de kans op 100+ tussen $1,99 en $4,99 bijna gelijk; de opbrengst per wijzerplaat stijgt met de prijs.

### Makergrootte (wijzerplaten van die maker in het jaar)
| Maker met | Aantal betaalde (3 mnd+) | 10+ | 100+ | 1.000+ |
|---|---|---|---|---|
| 1 tot 3 | 103 | 74% | 29,1% | 6,8% |
| 4 tot 20 | 427 | 75% | 39,8% | 11,7% |
| 21 tot 50 | 281 | 68% | 27,0% | 6,4% |
| 51 tot 200 | 381 | 41% | 12,1% | 0,8% |
| 201 en meer | 1.560 | 30% | 1,3% | 0,2% |

### Figuur of grap
| Groep (3 mnd+) | Aantal | 100+ | 1.000+ | Mediaanprijs |
|---|---|---|---|---|
| Figuur of dier | 246 | 6,5% | 0,4% | $1,99 |
| Geen figuur | 2.506 | 13,0% | 3,2% | $2,49 |
| Figuur, kleine maker | 55 | 21,8% | 1,8% | $1,99 |
| Geen figuur, kleine maker | 475 | 39,6% | 11,8% | $2,49 |
| Grap in naam of begin van de tekst (alle leeftijden) | 22 | 0% | 0% | $1,99 |

Het enige betaalde figuur van het jaar op 1.000+ volgens de woordzoektocht is Cool Otter (MONYMAHONY, $1,99, 5 reviews; een review zegt dat hij eerst gratis was). VAW.BE's Goals Pro (10.000+) en Seasons Premium (1.000+) hebben seizoensplaatjes en figuurtjes maar verkopen als volle sportwijzerplaat. De figuren van fabrieken (GreenPoint, IAMBEN) blijven op 0 tot 10.

### Wat de verkopers anders doen (kleine makers, minstens 3 mnd oud)
Woorden in de beschrijving. Let op: makers die meer opschrijven, maken vaak ook betere wijzerplaten; dit is samenhang, geen bewijs van oorzaak.
| Kenmerk | Met: 100+ | Zonder: 100+ |
|---|---|---|
| Filmpje op de winkelpagina | 64,8% (n=54) | 34,7% (n=476) |
| Aanraken (tik op een veld opent iets) | 49,6% | 33,9% |
| Weer | 46,3% | 23,1% |
| Body Battery | 45,9% | 27,7% |
| Slaapstand (AOD, always on) | 45,9% | 29,9% |
| Zelf velden kiezen | 42,7% | 20,3% |
| 5 of meer schermbeelden | 42,1% | 28,7% |
| Meer dan één taal | 41,1% | 36,9% |
| Stapdoel of voortgang | 35,7% | 39,2% |
| Animatie | 38,0% | 37,7% |
| 13 of meer functies genoemd | 55,1% | 24 tot 31% |

Over alle betaalde (3 mnd+): bij de wijzerplaten met 100+ noemt 85% zelf velden kiezen en 85% kleuren of thema's, bij die onder 10 downloads 39% en 42%. Stappen, hartslag en batterij staan bij bijna iedereen (83 tot 89%) en onderscheiden dus niet. **Een stapdoel dat iets laten groeien onderscheidt ook niet** (35,7% met, 39,2% zonder): het is geen verkoopreden op zich.

### De makers met een reeks
| Maker | Betaald dit jaar | Gratis dit jaar | Op 100+ | Geschatte omzet ondergrens (GOK) | Wat opvalt |
|---|---|---|---|---|---|
| TitanicTurtle | 6 | 1 | 6 | $413.000 | Black Hawk Elite 100.000+ (4.249 reviews), Vanguard Elite 50.000+; $2,99, strakke tactische sportwijzerplaten, alles instelbaar |
| VAW.BE | 16 | 17 | 11 | $61.000 | Bijna elke betaalde een gratis broertje; reeksen (Goals 9 naar Goals Pro $4,99 10.000+, Cockpit I en II 1.000+); figuren alleen als extra |
| Stash.Digitale | 3 | 1 | 3 | $38.000 | Modello GMT $3,99 10.000+ |
| Garmin zelf | 14 | 10 | 11 | $31.000 | $4,99, merkwijzerplaten |
| JS_ProDesign | 33 | 6 | 19 | $29.000 | $2,25 tot $2,75, RESISTANCE 10.000+ |
| timwatch | 14 | 0 | 12 | $28.000 | $1,99, 10 van 10 oudere op 100+ |
| Atelier_Dev | 36 | 27 | 34 | $8.800 | Maker van Purrtime (de levende kat); veel gratis broertjes, bijna alles 100+ |
| TDSH (fabriek) | 593 | 0 | 14 | $14.000 | Massa: 2% op 100+ |

Van de 397 makers met een betaalde wijzerplaat halen er 136 een geschatte $100 of meer in het jaar, 58 een $1.000 of meer. Van de 340 kleine makers (≤20) is de mediaan ±$25 per jaar; 93 halen $100+, 35 halen $1.000+.

## Advies voor Gloop en Ebb

**Prijs: $2,99.** Reden: bij kleine makers is de kans op 100+ op $2,99 even groot als op $1,99, en de opbrengst hoger; Gijs kwam vanaf de concurrenten op hetzelfde uit. $3,99 kan voor Ebb als die veel velden heeft; $4,99 pas als we een naam hebben.

**De drie dingen die moeten:**
1. **Een volle, instelbare sportwijzerplaat onder het figuur.** Minstens: tijd groot, datum, stappen, hartslag, batterij, en twee of drie velden die je zelf kiest uit Body Battery, weer, stress, calorieën, trappen en meldingen. Plus een paar kleurthema's. Zonder dit verkoopt een figuur bij kleine makers half zo vaak. Het figuur (de hoedentoren, de zee) is de reden om naar ons te kijken; de velden zijn de reden om te kopen.
2. **Slaapstand (AOD) en aanraken.** Een rustige AOD op AMOLED en tikken op een veld om de Garmin-weergave te openen. Beide horen bij de verkopers en ontbreken bij de massa.
3. **Een winkelpagina als die van de verkopers:** een kort filmpje (de toren die de rand uitschuift, het dier dat wisselt), 5 schermbeelden, een lange, nette uitleg met alle velden, en meer dan één taal. Het filmpje is het sterkste losse kenmerk dat ik vond (64,8% op 100+ bij kleine makers).

**Ook:** een gratis broertje met minder erin (geen proef die na 2 dagen om geld vraagt, zie Gijs), en reken op een reeks: een hit komt bij de reeksmakers meestal pas na een paar wijzerplaten. Verwachting eerlijk: mediaan ±$25 per wijzerplaat in de eerste maanden, met kans op $200+ als het goed valt (GOK uit de tabel van kleine makers).

**Wat dit omgooit:** als Gloop met velden, AOD en filmpje na 30 dagen onder 10 downloads blijft, dan ligt het niet aan de kenmerken maar aan de drukte sinds september, en is een tweede wijzerplaat niet zinvol zonder ander kanaal (r/Garmin, de kijkers van het spel).

## Grenzen
- Woordzoektocht in Engelse teksten; figuren zonder dierwoord in de tekst missen, en een tekst kan een functie noemen die er niet goed in zit.
- Downloads zijn klassen en geen verkopen; omzet is een ondergrens met onzekerheid.
- Schermbeelden van de wijzerplaten niet bekeken.
