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

# Herkeuring (12 nov 17:35 NL, bouwtak fc7bcf59)

Keurder: fris, opus, alleen lezen. **Veiligheid en winkel 7, code 7** (was 6 en 6).

De vijf MOET-punten van vanmiddag: alle vijf opgelost, vier met een toets. Inhouden stopt op 5:00 (EbbView.mc r.73 tot 83, DelegateTest.mc r.160 tot 175); Calm en pauze na 30 min (RustigView.mc r.51 tot 57, Pauze.mc r.30 tot 61; Calm alleen getoetst op teLang, niet tot en met opslaan); nooit de donkere zee (TrouwDieren.mc r.169, SessieScherm.mc r.61, WereldTest.mc r.151 en 169); terugval tekent een effen vlak (KrabV2.mc r.233 tot 243, geen toets op beurtduur); 28 horloges bouwen (job alle-horloges groen).

## Nieuwe MOET
1. Winkelbeelden kloppen nog niet (winkel/1-breathe.png is het oude zwarte scherm; veld Screenshots verouderd).
2. Niet inleveren voor de plaatjesrun op alle 13 horloges groen is.
3. Terugval zonder echte toets: laat de workflow bij sessie-terugval op de fr255 rood worden als "traagste beurt" (KrabV2.mc r.283) boven een vaste grens komt.

## KAN
1. Een vanzelf gestopte inhouding telt als 5:00 mee in Today, 8 weeks en de lap; blaast het gemiddelde op en 5:00 kan een doel lijken.
2. Melding over het pauzemenu zet de 30 minuten terug op nul; en wie niets doet begint na het herstel vanzelf aan de volgende ronde, tot drie keer 5:00.
3. Winkeltekst noemt de stop van Calm na 30 minuten niet.
4. Open van vanmiddag: kop KrabV2.mc r.7 tot 11, Scenes.mc zonder (:plaatje), Storage.setValue zonder try/catch, vandaag() op de dag dat de zomertijd eindigt.

## Niet na te gaan
Snelheid, geheugen en batterij op echte horloges (ook het steeds opnieuw aanmaken van een schermgroot plaatje bij elke wissel); contrast van de basiswereld per familie; of de .iq van de release precies deze commit is.
