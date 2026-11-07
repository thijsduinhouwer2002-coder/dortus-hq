# Voorstel: Firefox (extensies op addons.mozilla.org)

**Advies: nee. Cijfer: 1 van 10.** Veel te druk en bijna geen bereik: ±5.000 (juli) tot ±10.000 (okt) nieuwe extensies per maand, afgerond, nieuwe extensies van juni t/m aug 2026 hebben mediaan 1 gebruiker per dag en 2% haalt 100+. Geen betaling in de winkel. Geschreven op 7 nov 2026, run 13:31 (derde platform). Nagekeken door de controleur (akkoord, 6 correcties verwerkt).

## Wat ik zelf mat
- Met `data/firefox-haal-script.py` via de open API van addons.mozilla.org de nieuwste extensies (sort=created). De API telt 116.388 openbare extensies maar toont alleen de nieuwste 30.000 (600 pagina's van 50; pagina 601 geeft "Invalid page.", pagina 600 eindigt bij ±8 juni, nagekeken met curl). GEZIEN. Ik nam elke 5e pagina: **6.000 extensies**, gemaakt van ±8 juni tot 5 nov 2026. Uitkomst in `data/firefox-steekproef-2026-11-07.json`, tellen met `data/firefox-analyse-script.py`. GEZIEN
- Dat de 30.000 nieuwste maar tot ±8 juni teruggaan zegt al genoeg over de drukte.
- **Meetgrens:** ADU is gemiddeld aantal gebruikers per dag (updatecontrole), dichter bij echte gebruikers dan downloads. De zoek-API toont alleen openbare, goedgekeurde extensies.

## Cijfers

**Bereik**
- Gemaakt 10 juni t/m 31 aug 2026 (2 tot 5 maanden oud): n=2.600 in de steekproef, **mediaan 1 gebruiker per dag, 12% 10+, 2% 100+**, 9 boven 1.000 in de steekproef (±45 in het hele venster, GOK). De grootste is van een bedrijf (Seqrite, 8.529), geen kleine maker. GEZIEN
- Alleen juni t/m juli (3 tot 5 maanden): n=1.500, mediaan 1, 3% 100+. GEZIEN
- Alleen extensies met minstens 1 review (n=276): mediaan 9, 17% 100+. GEZIEN
- Ter vergelijking: Chrome en Edge 8 tot 9 (eerdere meting, `onderzocht.md`), Thunderbird 16, JetBrains 111.

**Geld**
- Geen betaling in de winkel. Van de nieuwe extensies jun t/m aug heeft 127 (5%) de vlag "vraagt betaling": mediaan 1 gebruiker per dag. GEZIEN
- Geen kleine maker met een bedrag gezocht: bij deze aantallen niet nodig. GOK

**Drukte**
- In de steekproef (1 op 5): juli 950, aug 1.100, sep 1.250, okt 1.950. Dus ±4.750 (juli) tot ±9.750 (okt) nieuwe extensies per maand, afgerond ±5.000 tot ±10.000, met ±250 tot 500 onzekerheid per maand (steekproef 1 op 5 pagina's). GEZIEN, vermenigvuldigd met 5. Meetgrens: alleen extensies die nu openbaar zijn; verwijderde of uitgezette vallen weg, vooral bij oudere maanden. Juli is daarom waarschijnlijk te laag geteld en de stijging naar oktober is deels schijn. Waarschijnlijk veel AI-gebouwde extensies (GOK).

**Vindbaarheid**
- Zoeken op addons.mozilla.org en "Recommended" door Mozilla. Bij deze stroom verdwijnt een nieuwe extensie meteen. GOK

**Past het bij ons**
- Een WebExtension is in 1 tot 2 weken te bouwen. GOK. Maar dat kan iedereen, en dat zie je.

## Voor
- Open API, goed te meten.

## Tegen
- ±5.000 (juli) tot ±10.000 (okt) nieuwe extensies per maand, afgerond.
- Mediaan 1 gebruiker per dag na 2 tot 5 maanden.
- Geen betaling in de winkel, betaalde nieuwe extensies ook mediaan 1.

## Eerste idee
Geen.

## Wat het van nee naar ja zou brengen
Niets in zicht. Alleen als Mozilla de stroom nieuwe extensies flink inperkt en betalen in de winkel inbouwt.
