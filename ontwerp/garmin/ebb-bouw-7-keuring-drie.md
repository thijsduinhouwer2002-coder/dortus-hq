# Ebb bouw 7: keuring door drie frisse beoordelaars (11 nov, 21:20 NL)

Gekeurd: code `claude/garmin-2026-11-10b` 330cf565, e2e 43001614437 en plaatjesrun 43001614405 groen, geen crash. Beelden fenix 8 en FR255, sea complete ook op Venu 3S, epix, FR165, vivoactive 5, fenix 7.

| Onderdeel | B2 | B3 | B4 | B5 | B6 | B7 |
|---|---|---|---|---|---|---|
| Code | 3 | 7 | 7 | 7 | 7 | 7 |
| Veiligheid en regels | 4 | 6 | 6 | 6 | 7 | 7,5 |
| Bouw visueel | 4 | 6 | 5 | 6 | 7 | 7 |
| Product | 5 | 6 | 7 | 6 | 7 | 7,5 |
| Dieren in de app | 7 | 6 | 6 | 6 | 7 | 7 |
| Winkelbeelden | | | | | 7 | 6 (codetak v3), 7 (Mila v4) |

Drempel 8. De app zelf is volgens de productkeurder een 8; visueel is AMOLED een 8 en houdt MIP het op 7. Schatting: 3 tot 4 uur Gijs, half uur Mila.

Af: e2e groen, sea complete gevuld op alle horloges, feest één keer en daarna gewoon eindscherm, pauzemenu ook voor Calm met tikken, belletje in de sea log, kamlijn overal, bonus zichtbaar, titel met Breathing.

## Voor Gijs (in deze volgorde; vult het bericht van 21:10 aan)
1. **Venu 4 (veiligheid):** geen START-knop, dus de "top button"-teksten van de Venu 3 in `resources-venu441mm` en `resources-venu445mm`. Eén plaatje in de plaatjesrun.
2. **Winkelkaarten v4 in `winkel/`, met verse opnames:** kaart 3 uit s4 (belletje), kaart 4 uit de huidige scène 25 (nu 18 dieren onder "24 of 24": niet eerlijk), kaart 5 uit s33 ("back after a break"), kop van kaart 5 even groot als de rest. Poster in v4-stijl (groot scherm, leesbaar op 150 px, "no extra account"). Icoon met blauwe walvis of het eigen dier, niet rood. Schermlijst in winkeltekst.md bijwerken.
3. **Schermen stapelen niet meer:** na een sessie met popView terug naar het bestaande menu (Start.mc:181,186; EbbDelegate.mc:50-51; RustigView.mc:219; Pauze.mc:115-116). Na My pattern niet in settings uitkomen.
4. **MIP (260) naar een 8:** eindschermdieren 50 tot 55 px breed (zeester k17 is 21 px, walvis k36 37 px, schaduwkrab k32 28 px); instellingen k19 regels los van elkaar in de pil; krab s34/k34 10 px (454) en 6 px (260) lager, onder de kamlijn; dier bij inhouden 4 tot 6 px lager en belletjes vrij van de cijfers; belletje sea log ruim om sunfish heen.
5. **Winkeltekst (drie talen):** "After every session" kloppend voor Calm en het feestscherm; "touchscreen does nothing" kloppend met het pauzemenu; "breathwork" in de eerste alinea; Nagekeken naar de huidige versie.
6. **Today en 8 weeks bereikbaar vanuit het menu** (ook na Calm).
7. **Code:** Calm eens per seconde hertekenen in de vast-fase (RustigView.mc:58); SeaComplete opnieuw `maak(_d)` als het plaatje is vrijgegeven (59-62, 117-119); feest alleen als de sessie meetelt (EbbView.mc:112); toets voor PauzeDelegate (kies, onTap, Discard); SeaLog en Pauze via EbbTeken.px en EbbZee; pixelstap met `--negeer` voor de statusbalk; graphics pool meten op FR165 en Venu 3S.
8. **Venu X1:** proberen, anders in status.md "niet in versie 1" met reden.
9. Groene e2e en plaatjesrun op de eindcommit, nieuwe release bouwen.

## Voor Mila
1. Poster in v4-stijl ontwerpen (één stijl met de kaarten, leesbaar op 150 px).
2. Icoon: blauwe walvis of het eigen dier, passend bij de app.
3. Scène 20 (instellingen blad 2) is half leeg en "Ebb makes no sound" erg dof: geef een indeling.
