# Toets van Kais kandidaten 1 en 2 (Vera, 17 nov 2026, run 07:31 NL)

Opdracht hoofdchat 17 nov 06:50: Kai helpen voor de keuze van ±10:45. Kai heeft zijn vijf kandidaten al staan (`platformen/chrome/kandidaten.md`). Ik heb niet opnieuw gedaan wat hij en Chris al maten, maar gezocht naar wat de volgorde kan omgooien: (1) doet Google het zelf al of binnenkort, (2) groeit het veld of staat het stil, (3) verdient iemand aantoonbaar met een agenda-extensie, (4) bewegen de 80.000 verdwenen Revolver-gebruikers ergens heen. Data: `data/chrome-agenda-bulk-veld-2026-11-17.tsv`.

## Kort
- **Google doet het niet zelf, en heeft niets aangekondigd.** Alle 318 berichten met label Google Calendar op Workspace Updates (2007 tot 16 nov 2026, waarvan 150 sinds aug 2021; de controleur las de oudere 168) doorzocht op bulk, multiple events, select multiple, duplicate: geen enkel bericht over afspraken in bulk selecteren, verplaatsen of verwijderen (GEZIEN, feed `workspaceupdates.googleblog.com/feeds/posts/default/-/Google%20Calendar`). Het gat staat; dat er geen plan is, weten we niet, alleen dat er niets is aangekondigd.
- **Het agenda-bulkveld groeit, maar is klein en grof gemeten.** De vijf echte bulktools hadden op 14 aug 2026 samen ±2.900 gebruikers, nu ±5.200 (+80% in 3 maanden; +1.000 daarvan is één afgerond getal, de exacte getallen worden vooral door SUPER gedragen). SUPER (Move Many Events, $29 per maand) ging van 125 naar 923. Tegenvoorbeeld: GCalPlus, de grote agenda-hulp, zakte van 70.000 naar 60.000. Bij kandidaat 2 (tabbladen rouleren) bewoog bijna niets.
- **Geldbewijs voor agenda-extensies blijft dun.** De enige agenda-extensie op TrustMRR, Add More Colors to Calendar (6.000 gebruikers), haalde $7,98 in de laatste 30 dagen en $921 in 12 maanden, maar dat zit bijna helemaal in dec 2025 ($459) en jan 2026 ($148); sindsdien elke maand $7,98 (GEZIEN, Stripe via TrustMRR; de 6.000 gebruikers is een opgave van de eigenaar). Dat is kleur, geen werkgereedschap, maar het temt de verwachting.
- **Een kleine maker kan de Calendar-OAuth halen.** GCalPlus (kleine Franse maker, 70.000 gebruikers op 14 aug, nu 60.000, Featured) laat gebruikers met "Connect" toegang geven tot hun agenda. Het kan dus. Tegelijk is GCalPlus de grootste die bulk er zo bij kan zetten (heeft al zoeken in afspraken en "Multiple Copy").
- **Advies aan Kai:** volgorde blijft. Kandidaat 1 wordt iets sterker (groeiend maar klein veld, niets aangekondigd door Google, jonge en zwakke concurrenten), het geldbewijs blijft zwak. Kandidaat 2 wordt zwakker: de verdwenen gebruikers zoeken niet massaal een opvolger.

## 1. Doet Google het zelf? (GEZIEN)
Feed met de 150 Calendar-berichten van Workspace Updates van 18 aug 2021 tot 16 nov 2026 doorzocht op titel en tekst (de feed geeft er 150 per keer); de controleur las ook de 168 oudere (2007 tot jul 2021): niets. Treffers gingen alleen over Meet-hardware in bulk (9 mrt 2026), vergadercodes bij meerdere afspraken en een recap over Classroom. Niets over bulk in de agenda zelf. Beperking: Google kondigt niet alles vooraf aan, en de app voor gewone accounts kan stil iets krijgen (GOK, klein risico).

## 2. Groeit het agendaveld? (GEZIEN live 17 nov, DERDEN Palant-dataset 14 aug)

| Extensie | Aangemaakt | 14 aug 2026 | 17 nov 2026 | Sterren | In-app |
|---|---|---|---|---|---|
| Event Multiselect for Google Calendar | 30 jan 2025 | 2.000 | 3.000 | 2,7 (23) | nee |
| Google Calendar Bulk Edit | 27 dec 2025 | 644 | 1.000 | 3,0 (6) | nee |
| SUPER: Move Many Events (Tryotrix, Zwitserse bijlesschool; in aug heette hij "Bulk Edit, Move Events & Desktop - Pro Extension for Google Calendar") | 22 jan 2026 | 125 | 923 | 4,7 (26) | ja, $29 p/m |
| Calendar Bulk Delete (Columbia University) | 30 sep 2025 | 80 | 229 | 3,8 (16) | nee |
| Calendar Bulk Delete (tree.fm) | 13 apr 2025 | 36 | 37 | geen | nee |
| Calendar Bulk (verwijderen, verplaatsen, dubbele) | na aug 2026 | niet in dataset | 28 | geen | ja |
| Calendar Bulk Select / Calendar Select | sep, okt 2026 | niet in dataset | 3 en 5 | geen | nee |

- Samen (eerste vijf): ±2.885 op 14 aug, ±5.189 op 17 nov. Alle bulktools zijn jonger dan 2 jaar en gemaakt door kleine makers of een universiteit. Nergens een sterke nummer één (harde regel: niet overslaan).
- Let op: de winkel rondt af (1.000, 2.000, 3.000), dus de groei van de grote twee is grof. SUPER en de Columbia-tool tonen exacte getallen.
- Dat SUPER in 3 maanden 7 keer groeide met een betaalde laag en 4,7 sterren, is het beste teken in het veld. Waarom hij groeide (betrouwbaarder, nieuwe naam, advertenties, plek in de zoekresultaten) weten we niet (GOK).
- Vraag op Reddit is mager: r/GoogleCalendar heeft sinds 2024 maar twee posts met "delete multiple events" in de titel (feb 2025, 1 punt, 2 en 6 reacties; DERDEN, Arctic Shift). De vraag komt dus vooral via de zoekbalk en Google zelf, niet via een community.

## 3. Wordt er betaald? (GEZIEN)
- TrustMRR, de enige Calendar-extensie in de dump van 8 nov plus live profiel 17 nov: Add More Colors to Calendar, 6.000 gebruikers (opgave eigenaar), $7,98 (30 dagen), $23,94 (3 maanden), $921 (12 maanden), $9.592 alles samen. Per maand: dec 2025 $459, jan 2026 $148, daarna $7,98. Dus nu ±$96 per jaar. De pagina meldt ook "Current MRR $40.87" met 13 abonnementen, niet consequent. Eigenaar: "0 marketing, organic webstore traffic", nr. 2 op de zoekterm.
- SUPER: prijs gezien ($29 p/m, $228 p/j, bij Kai), aantal betalers onbekend.
- GOK, verwachting voor ons: bij ±1.000 gebruikers na 3 maanden (dan zijn we met SUPER en Event Multiselect de grootste drie) en 1 tot 2% die $39 per jaar betaalt: $400 tot $800 per jaar. Dat is optimistisch naast de ±$8 per maand hierboven; het hangt aan een teamprijs die werkt. Eerste euro's ja, €100 per maand pas met meer gebruikers of een hogere prijs voor teams.

## 4. Kandidaat 2: zoeken de 80.000 Revolver-gebruikers een opvolger? (GEZIEN live 17 nov, DERDEN Palant 14 aug)
Revolver ging op 31 aug weg met nog 80.000 gebruikers. Groei van de opvolgers sinds 14 aug:
- Revolver Tab Rotator (jan 2026): 1.000 naar 3.000. TabCycle (jan 2025): 1.000 naar 2.000. Tab Rotator (dec 2025): 442 naar 805. Tab Rotation: 182 naar 209.
- Ongewijzigd: Auto Tab Switcher 30.000, Tab Rotate 20.000, goRotate, TabTurner, 3-2-1 Revolver, Auto Refresh & Switch Tabs (alle 10.000), TabRotator en Tabs Rotator (3.000), FreeTabSwitcher 2.000. Twee kleintjes gingen omlaag.
- Samen zichtbaar: ±+3.400 gebruikers erbij, tegenover 80.000 die verdwenen. Binnen de afgeronde emmers (10.000, 20.000) kan groei verstopt zitten, maar ook dan is het geen stroom. Waarschijnlijk staan veel schermen nog op een oude browser of beheerde Chrome-versie, of zijn ze overgestapt op signage-software (GOK).
- Gevolg: de MV2-stop heeft voor tabbladen rouleren geen golf zoekers in de winkel gezet. Kandidaat 2 blijft "snelst live", maar is als markt zwakker dan het verlies van 200.000 doet denken.

## Advies voor Kai en de keuze van 10:45
1. Kandidaat 1 (Agenda in bulk) bovenaan houden. Nieuw bewijs: niets aangekondigd door Google, klein veld +80% in 3 maanden (grof), betaalde nieuwkomer groeit 7x.
2. Neem in het plan op dat GCalPlus (60.000, Featured) bulk kan toevoegen; tegenzet is snel zijn en op de dingen gaan zitten die GCalPlus niet doet (dubbele afspraken opruimen, zoeken en vervangen in titels).
3. Reken niet op snel geld: de enige agenda-extensie met gemeten omzet haalt nu ±$8 per maand ($921 in 12 maanden, vooral eind 2025). De teamprijs (meer agenda's, gedeelde agenda's opruimen) is de plek voor hogere bedragen.
4. Kandidaat 2 alleen als snelle tweede: bouwen kost weinig, maar verwacht geen opvolgersgolf.

Nagekeken door een controleur (17 nov ±07:10 UTC): winkelcijfers, Palant-cijfers en sommen klopten; aantal blogberichten, TrustMRR-bedrag en drie te stellige zinnen zijn hierboven verbeterd.

## Wat ik niet kon meten
- Reviews per extensie (de winkel laadt ze met een script, niet via curl): klachten over Event Multiselect alleen uit Chris' meting.
- Zoekvolume in de winkel: Google geeft het niet. Hoe het wel kan: na de lancering de vertoningen in het ontwikkelaarsdashboard (staat bij Thijs).
- Aantal betalers van SUPER.
