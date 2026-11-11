# Ebb bouw 8: keuring door drie frisse beoordelaars (11 nov, 23:25 NL)

Gekeurd: code `claude/garmin-2026-11-10b` 3598a845, e2e 43105047698 en plaatjesrun 43105047693 groen, geen crash op 13 horloges, 42 van 42 toetsen. Keurders op Opus.

| Onderdeel | B5 | B6 | B7 | B8 |
|---|---|---|---|---|
| Code | 7 | 7 | 7 | 7,5 |
| Veiligheid en regels | 6 | 7 | 7,5 | 7,5 |
| Bouw visueel | 6 | 7 | 7 | 7,5 |
| Product | 6 | 7 | 7,5 | 7,5 |
| Dieren in de app | 6 | 7 | 7 | **8** |
| Winkelbeelden | | 7 | 6 tot 7 | 7,5 |

Drempel 8. Dieren zijn er. De rest scheelt weinig; de keurders noemen per cijfer precies wat nog moet. Schatting: 2 uur Gijs, half uur Mila.

Af: Venu 4 "top button", schermen stapelen niet, Today en 8 weeks vanuit het menu, feest ook na Calm en alleen als de sessie meetelt, null-check sea complete, Calm eens per seconde, pixelstap draait, winkelkaarten v4 met kloppende schermen, icoon blauwe walvis, dieren op MIP 47 tot 54 px onder de kamlijn, Venu X1 "niet in versie 1".

## Besluit hoofdchat
**Posterkop wordt "Breathe. Make sea friends."** en kaart 1 "Breathe in rounds. A friend swims along." Waarom: "Hold your breath" naast een timer van 1:45 leest als beloning voor inhouden; Garmin verbiedt uitdagingen met lichamelijk risico.

## Voor Gijs (in deze volgorde)
1. **Instellingen scène 19 (nieuwe fout door de k19-fix, alle horloges):** "Rounds 3" overlapt de kop "settings" 3 px op FR255, raakt op fenix 8 (InstellingenView.mc:104-114 en 78). Regel boven de pil minstens 8 px (260) / 14 px (454) onder de kop, of het vorige item niet tonen. k20: 4 px tussen "Start my pattern" en de pil.
2. **Scène 18 (6 rondes, alle horloges):** tweede rij tijden raakt de kamlijn (0 px). Kamlijn 10 px (260) / 16 px (454) lager bij 6 rondes, of tijden op één regel kleiner.
3. **Menu scène 37:** gekozen tekstlink (Sea log, Settings, Today) duidelijk tonen (lichte rand of pil), niet alleen een streep van 1 px.
4. **Winkeltekst:** terugbetaalzin in drie talen (besluit 22:55; rechte haken weg op regel 91, 122, 141). Nagekeken: scène 37 en 38 GEZIEN, feest na Calm noemen, kaartenlijst op de eindcommit.
5. **Winkelbeelden:** nieuwe posterkop en kaart 1 (besluit hierboven, Mila levert). Kaart 2 is hetzelfde scherm als de poster: vervang door s9 (breathe in) of s8 (herstel met zon). Kleine regels leesbaar op 150 px: posterregel "One payment..." twee keer zo groot, ondertitels minstens 34 px op 800 of weg. Op twee kaarten het horloge tot ±75 procent breed.
6. **Toetsen:** scène of toets voor Discard (landt in het menu; `PauzeDelegate.kies(2)`), toets voor `EbbTrouw.feestNu` (telt niet mee, al gezien, eerste keer).
7. **Graphics pool:** grootte van het plaatje en mislukte pogingen loggen, of eerlijk in status.md "alleen in de simulator bewezen".
8. Groene e2e en plaatjesrun op de eindcommit, dan release bouwen.

## Voor Mila
1. Poster met kop "Breathe. Make sea friends." en kaart 1 "Breathe in rounds. A friend swims along."; onderregel poster groot genoeg voor 150 px.
2. Kaart 2 met een ademscherm (s9 of s8); twee kaarten met het horloge ±75 procent breed zodat de rij niet zes keer hetzelfde toont.
3. Scène 38 (today): donkerblauwe staafjes op zwart zijn mat op AMOLED; kies een helderder blauw.
