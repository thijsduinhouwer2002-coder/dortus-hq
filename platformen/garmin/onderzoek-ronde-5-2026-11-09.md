# Ronde 5a: waar wordt al veel betaald? (9 november 2026, onderzoeker voor Gijs)

Koers (zie ronde 4): geen leeg gat zoeken, maar een hoek waar kopers al $3 of meer betalen, en daar zichtbaar beter en mooier zijn.

## Kassa-apps met $3 of meer en 15+ reviews (GEZIEN, dataset)
Er zijn er maar 15. Na wegstrepen (GoPro: Garmin zelf en Bluetooth; golf driving range: telt swings met de versnellingsmeter; schaak, HYROX, racket: al af) blijven over:
| Behoefte | Beste app | Prijs | Reviews | Reviews per maand 2026 |
|---|---|---|---|---|
| Ademhaling (Wim Hof, apneu) | WHM breathing+ | $4,99 | 604 | 26,1 |
| | Breath Training System PRO | $6,25 | 34 | 3,3 |
| Gebedstijden | Muslim Prayer Time | $4,99 | 31 | 3,0 |
| Herinneringen | Reminders Pro | $4,99 | 31 | 3,0 |
| Bergtoppen | Peak Finder Compass | $3,49 | 30 | 2,9 |
| Tesla | Tesla Key Pro | $9,49 | 25 | 2,4 |
(GEZIEN, reviews-API, ontdubbeld; bij WHM 280 van 604 reviews opgehaald.)

**Ademhaling springt eruit: ±26 reviews per maand bij één app van $4,99, tien keer meer dan de rest.**

## Ademhaling nader (de enige echte kandidaat)
- Klachten (GEZIEN): WHM breathing+: "I bought it, I use it daily. But I am harassed to provide feedback". BTS PRO: "heute Morgen erzählt sie mir, dass der Testzeitraum abgelaufen ist", "I can't find a way to configure my CO2 or O2 tables. The sounds are very sharp and jolting". Breathe (FikirLtd): "if there was an option to turn on vibration".
- Garmin zelf: een eigen ademhalingsactiviteit met vaste oefeningen (DERDEN: https://www8.garmin.com/manuals/webhelp/GUID-9D99A9D4-467A-4F1A-A0EA-023184FEA3DD/EN-AU/GUID-B3BD9AA0-2235-43BC-AAD0-D38008420EAD.html), maar geen Wim Hof-rondes met inhouden en geen CO2/O2-tabellen (GOK, niet in die bronnen gezien).
- Nieuw sinds aug 2026: ±13 apps (Freediver, ApneaFlow PRO, Vagal van ThijsGer, Candle, Jelly ...), bijna allemaal gratis met 0 tot 6 reviews (GEZIEN).
- Testbaar in de simulator: ja (timer, trillen, geluid, nagebootste hartslag).
- Zichtbaar beter (idee onderzoeker, GOK): een vloeiend ademende vorm, per ronde een grafiek van je inhoudtijd, eigen tabellen, alleen trillen, nooit om een review zeuren, een eerlijke proef.
- Risico: WHM staat op 4,9 en is sterk; veel gratis nieuwkomers.

## Gijs: wat ik ermee doe
Ademhaling wordt de kandidaat voor ronde 5b. Eerst nakijken: (1) wie de maker van WHM breathing+ is en of het de officiële Wim Hof-app is (merknaam, dan mogen wij die naam niet gebruiken), (2) alle 604 reviews van WHM: wat missen kopers, (3) hoe de top 3 eruitzien (screenshotFileIds in de API), (4) of Wim Hof-ademhaling eerlijk en veilig te brengen is (waarschuwing: nooit in water of achter het stuur). Pas dan een voorstel. Gebedstijden blijft reserve (klein, maar kwaliteit en kloppende tijden zijn een eerlijk verschil). Herinneringen valt af (druk).

## Aanvulling Gijs (9 nov 22:56, dataset)
- WHM breathing+ is van MobileDriveway (geen Wim Hof-bedrijf, GOK op naam; na te kijken). Dezelfde maker heeft ook een **gratis** WHM breathing met 50.000+ downloads en 1.730 reviews sinds jun 2022 (GEZIEN). De betaalde plus-versie (sinds dec 2024) leeft dus van een grote gratis basis. Een nieuwkomer staat tegenover een gratis app van 50.000+.
- 604 reviews bij 1.000+ downloads is veel; mogelijk telt de winkel een deel van de reviews van de gratis versie mee, of reviewt bijna elke koper door het vragen om een review (klacht hierboven). Volgende run nakijken voordat de 26 per maand als vraag telt.
- Verder in de hoek: Breathing Timer (HRV, BOLT, Wim Hof, 4-7-8; gratis, 1.000+, 92 reviews sinds apr 2026), Bitochi (PRO $6,25 en gratis Tool 1.000+), WhiteBear Breath and Plunge (PRO $2,99), Deyve Breath Training ($2,99, okt 2026) (GEZIEN).

## Ronde 5b, begin (9 nov 22:56, Gijs, alle reviews uit de winkel-API)
- WHM breathing+ ($4,99): alle 604 reviews opgehaald. In 2026 per maand 16 tot 35, gemiddeld ±26; oktober 29 (GEZIEN). Slechts 23 reviewers staan ook bij de gratis versie, dus het zijn echte eigen reviews, geen overgenomen (GEZIEN). Gemiddeld 4,85; maar 61 van de 604 hebben tekst, dus veel komt door het vragen om een review in de app (GOK, past bij de klacht "harassed to provide feedback").
- De gratis WHM breathing krijgt in 2026 nog 5 tot 24 reviews per maand (GEZIEN). Mensen stappen dus over van gratis naar betaald: een gewoonte-app die je elke dag gebruikt, waarvoor $4,99 geen drempel is.
- Wat de plus-versie extra biedt (GEZIEN, beschrijving): waarschuwingstril voor het einde van het ademen, aanraakscherm uit, details per ronde in de Garmin-activiteit, trilmomenten tijdens het inhouden, trilsterkte en geluiden.
- Klachten (GEZIEN, alle met 3 sterren of minder en tekst): "impossible to see your previous results", "I didn't find a way to create a breath in, hold, breath out pattern customizing the duration of each stage", knoppen reageren pas na 3 seconden, en het zeuren om een review.
- Voorlopig oordeel: ademhaling is de eerste hoek in vijf rondes met echte, doorlopende betaalde vraag (±26 kopers met review per maand, $4,99) en met klachten die wij kunnen oplossen (je eigen voortgang zien, eigen patronen, mooi en rustig). Risico blijft: een gratis basis van 50.000+ bij de leider, en veel gratis nieuwkomers. Volgende run: uiterlijk van de top 3 bekijken, merkrecht van "Wim Hof" nagaan (wij noemen het dan anders), en `volgend-product.md` schrijven als het overeind blijft.
