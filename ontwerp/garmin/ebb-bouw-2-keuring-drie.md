# Ebb bouw 2: keuring door drie frisse beoordelaars (11 nov, 04:30 NL)

Gekeurd: code op `claude/garmin-2026-11-10b` commit f46c3fbc; testbeelden fenix 8 scène 0 t/m 20 uit run 42946450008 (code van 02:30 UTC, dus zonder de Barlow-cijfers van e3ae9637 en zonder 6d). De run met de nieuwste code (42946930478) is na 40 minuten afgebroken in de stap "Scènes in de simulator".

| Onderdeel | Cijfer |
|---|---|
| Code | 3 |
| Veiligheid en regels | 4 |
| Bouw visueel | 4 |
| Product | 5 |
| Dieren v8 (blad) | 7 |

Laagste cijfer 3. Drempel 8. **Niet naar de winkel.**

Wat goed is: centreren klopt (binnen 1 tot 2 px gemeten), veiligheidsbladen zijn compleet en niet over te slaan, geen dubbel opslaan, rechten in manifest precies goed, besluit 22:53 grotendeels af (zee donkerder, geen meters, geen ring, trillen, hartslag, 8 weeks, menu).

## Eigen controle hoofdchat (vóór de keurders)
- Scène 4 (sea log): Connect IQ foutpictogram, crash.
- Scène 16 en 18: tekst over elkaar, en er staat "next: Clownfish". Besluit 22:53 punt 3 zegt: geen "next".
- Scène 19 en 20: tekst loopt buiten de blauwe pil.
- Testrun haalt de tijdslimiet niet, dus de nieuwste bouw is niet gezien.

## Besluiten hoofdchat bij deze keuring (Thijs kan ze om 08:00 terugdraaien)
1. **Reeks wordt weken op rij**, met een weekdoel van standaard 3 sessies (instelbaar 2 tot 7). Waarom: met dagen op rij breekt de reeks voor iemand die ma, wo, vr traint elke week, en dan zijn dieren 4 tot 7 nooit te halen. Garmin-gebruikers denken in trainingsweken. Tekst: "3 weeks in a row".
2. **Box gaat uit de winkeltekst** (titel, tekst, tags), Calm 5.5 en eigen patroon ook. Titel: "Ebb: Breath Hold Rounds, Breathwork & 4-7-8". Waarom: eerlijk en sneller dan Box bouwen; Box kan later als update.
3. **Een sessie telt pas mee** met minstens 1 inhoud, of bij Calm minstens 1 minuut.
4. **Calm krijgt ook de "Sit or lie down"-check**, want ook daar houd je 7 s in.
5. Veiligheidsbladen blijven elke 30 dagen terugkomen. Veiligheid gaat voor gemak.

## Voor Gijs (in deze volgorde)
1. **Crash sea log en inhoudscherm (watchdog).** Log run 42946133606: `Watchdog Tripped Error` in `delen()` (DierenData.mc:113) via `teken()` (:64) en `Dieren.mc onUpdate`; op FR255 crasht ook scène 2. Teken elk dier één keer in een BufferedBitmap en hergebruik die; rand met 4 verschuivingen in plaats van 8; sea log alleen opnieuw tekenen na een knopdruk.
2. **Echte crash-test.** DierenDataTest.mc 42-61 geeft altijd true. Test de echte `DierenView.onUpdate` en het inhoudscherm met dier 4 en 24. CI wordt rood bij "Watchdog" of "app crash" in de plaatjeslog.
3. **Testrun binnen de tijd.** De plaatjesstap haalt 40 min niet (8 horloges x 22 scènes x 15 s). Splits per horloge in een matrix, of verhoog de limiet. Alle scènes op 260, 390, 416 en 454 moeten er zijn, plus ademen uit, pauzemenu, 6d en today met 3 sessies. Venu 3 en epix ontbreken nu in plaatjes.
4. **Eindschermen 16 en 18:** geen overlap (minstens 4 px vrij boven en onder elke regel). Titel, dan tijden op één regel (4 tot 6 rondes: twee regels van 3, 6 px onder de titel). Geen "next:", wel "1 more day" of het aantal sessies tot het volgende dier. Rustdagzin alleen als je gisteren rustte. Tekst volgt besluit 1 (weken).
5. **Reeks naar weken** (besluit 1), sessieminimum (besluit 3), Calm-check (besluit 4).
6. **Instellingen 19 en 20:** pil 24 px breder dan de langste regel, maximaal 0,83 R; gekozen regel 2 px kleiner of waarde op een eigen regel; regels gelijk verdeeld.
7. **Dier tijdens inhouden:** minstens 90 x 70 px op 454 (50 x 40 op 260), midden onder de tijd, rustig heen en weer. In de testreeks steeds hetzelfde eigen dier. Belletjes alleen bij het dier. Menu: eigen dier 80 px op de kamlijn.
8. **Zee:** op AMOLED een echt verloop met kamlijn van 3 px en gloed, geen harde stroken (die alleen op MIP). Na 3:00 niet lichter dan op 2:30 (blad v5-keuring zegt: blijft gelijk). Zee onderaan op alle schermen dezelfde stijl.
9. **Letter:** Barlow Condensed ook voor koppen en regels, niet alleen het grote getal.
10. **Herstel scène 8:** zon 10 px los van "15 s" of weg. Onderste regel op alle ademschermen op dezelfde hoogte (ongeveer y 380 op 454). Driehoek veiligheid 44 px.
11. **Winkeltekst** in drie talen volgens besluit 2. Ook "every hold of the day", "average hold per session" en "saves itself" laten kloppen met de app; blok "Nagekeken" bijwerken. Winkelbeelden pas opnieuw maken uit de echte bouw nadat 1 t/m 10 af zijn. Oude beelden (dive, meet, tide, dive-profile) weg.
12. **Opruimen:** dode code (EbbTrouw.gezelschap, GETEKEND, hoe, wachtend, EbbDierData.vlakken, EbbStart.rondesKop, EbbTeken.dier/walvis/schildpad, "Box" in PATROON_NAMEN, `deleteValue("record")`). FIT: velden Rounds en Hold times alleen bij rondes; hartslagsensor uit na de sessie.

## Voor Mila
Dieren v8 op 7. Maak v8.2:
1. Zeeotter: geen blok met vlekken, herkenbare kop en pootjes.
2. Narwal: lijf 4 px hoger.
3. Dolfijn, zwaardvis en haai elk een eigen tint.
4. Zeepaardje voller in zijn vak.
5. Rog: leest als lolly, maak de vleugelvorm duidelijk.
Daarna gaan de dieren naar Gijs.
