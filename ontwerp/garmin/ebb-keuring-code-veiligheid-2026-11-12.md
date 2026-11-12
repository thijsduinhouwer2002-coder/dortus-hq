# Ebb, vroege keuring code en veiligheid (12 nov 13:15 NL, proef65 532fb02)

Keurder: fris, opus, alleen lezen. **Veiligheid en winkel 6, code 6.** Lat is 8.

## MOET voor inleveren
1. **Inhouden heeft geen maximum.** Sessie.mc r.200 tot 222: de inhoudfase eindigt alleen met een knop. Doet iemand niets of valt hij weg, dan loopt het eindeloos door (na 3:00 trilt het elke 30 s). Oplossing: bij een vaste grens vanzelf stopInhouden en door naar herstel; ook in de winkeltekst.
2. **Calm en pauze lopen eindeloos**, opname blijft open (RustigView.mc r.28 tot 70, Pauze.mc). Na een vaste tijd zonder knop vanzelf opslaan of stoppen.
3. **Eerste sessie zonder dier tekent het oude scherm**, waar de zee elke 30 s donkerder wordt tot 2:30 (SessieScherm.mc r.60, 61, 113; Profiel.mc r.42; TrouwDieren.mc r.151 tot 161). De winkeltekst belooft dat het beeld gelijk blijft. zeeStand op 0 of ook zonder dier de basiswereld (WereldSessie.mc r.42).
4. **Winkelbeelden kloppen niet met de app** (werelden staan aan, beelden tonen ze niet; winkeltekst v14 nog niet gekeurd).
5. **Wereldcode draait nu in de echte sessie maar is alleen in de simulator gemeten.** Bij elke wissel maakt WereldSessie.mc r.70 tot 75 een nieuwe KrabV2View met een plaatje zo groot als het scherm. Lukt dat niet, dan tekent KrabV2.mc r.217 tot 221 vijf lagen in één beurt: watchdog op MIP. Terugval: hoogstens één laag per beurt, of de wereld overslaan. Plaatjesrun draait op 13 van de 28 horloges.

## KAN later
1. Scenes.mc, ThuisSchermen.scene en proefscènes missen het (:plaatje)-label en zitten in het winkelbestand (niet bereikbaar, maar ThuisSchermen r.39 tot 51 schrijft dieren naar opslag). Label geven, spaart geheugen.
2. EbbView.vandaag() rekent met de tijdzone van nu; op de dag dat de zomertijd eindigt kan een sessie bij de vorige dag komen.
3. Storage.setValue zonder try/catch voor volle opslag.
4. Kopteksten KrabV2.mc r.7 tot 11 en REGELS.md zeggen "alleen plaatjesbouw", maar het draait nu in de app.
5. Today en 8 weeks: geen nadruk op de langste tijd, zo houden.

## Goed bevonden
Stopregel altijd in beeld; Terug en knoppen stoppen het inhouden; veiligheidsbladen (water, autorijden, duizeligheid) elke 30 dagen; geen record of langste tijd; eindscherm alleen tijden per ronde; nergens freediving of apnea; geen medische claims; terugbetaling, support en privacy in drie talen; horlogelijst gelijk aan manifest (28); rechten alleen Fit, FitContributor, Sensor; releasebouw sluit demo en plaatjes uit; ontbrekende hartslag en kapotte opslag vallen veilig terug.

## Niet na te gaan door de keurder
Snelheid en geheugen op echte horloges; of FR255, FR955 en fenix 7 API 5.0.0 halen; of de bovenste knop op Venu 4 en vivoactive 6 onSelect geeft; of het bestand voor alle 28 horloges compileert; waar het versienummer vandaan komt (manifest zonder versie, versie.txt zegt 1.0.0).
