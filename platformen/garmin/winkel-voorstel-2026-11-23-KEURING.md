akkoord: ja

# Keuring winkelvoorstel Garmin (Ebb, Spaans en Italiaans), 23 nov 2026, keurder (Claude)
Wat ik keurde: `platformen/garmin/winkel-voorstel-2026-11-23.md` (lokaal bestand, nog niet gecommit). Vergeleken met de gekeurde Engelse en Franse tekst van Ebb in `winkel-plak-2026-11-20.md` (deel 1), de keuring `winkel-vindbaar-KEURING.md` en de meting `meting-weekronde.md`. Zelf nagemeten met `curl` op de winkel-API en de winkelpagina, 23 nov ±10:00 UTC. Ik heb niets gebouwd of veranderd.
Akkoord: ja

## Deel A: doet het wat beloofd is?

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | **Alle veiligheidszinnen staan er, in beide talen.** Eerste alinea: alleen op het land, zittend of liggend, nooit in of bij water, nooit tijdens het rijden, alleen inhouden zolang het makkelijk is. Laatste alinea: zittend of liggend, nooit in of bij water, nooit in bad (bañera / vasca), nooit tijdens het rijden, duizelig of tintelend dan stoppen en gewoon ademen, niet bij zwangerschap, onder 18, epilepsie, hart- of bloeddrukproblemen, geen medisch hulpmiddel, geen CO2-tabellen. Ook "Ebb herinnert je voor elke sessie: ga zitten of liggen", "nooit door langer inhouden", de stop na vijf minuten en de tril elke 30 s na 3:00 staan erin. | feit | hoog | |
| 2 | **Geen functie die de app niet heeft.** Alles komt uit de gekeurde Engelse tekst: rondes, herstelademhaling, "breathe" vanaf 3:00, 4-7-8, My pattern met 4-4-4-4, 24 zeedieren op trouw, weekdoel 3 (2 tot 7), max twee sessies per dag, Today en 8 weeks, tril per fase, aanraakscherm uit, geen geluid, Garmin Connect met lap per ronde, eenmalig betalen, niets verzameld, 48 uur terug. Weggelaten (mag, geen belofte): bonusdier, kleine vis, opslaan na 30 minuten, de lijst instellingen, 5-0-5-0. | feit | hoog | |
| 3 | **Eén stukje functie is in de vertaling weggevallen:** de korte herstel-inhouding. Engels: "take one big breath in and hold it briefly to recover". Spaans: "toma una gran inspiración para recuperarte", Italiaans: "fai un grande respiro per recuperare". Niet fout, wel minder precies (kan-punt 3). | feit | hoog | |
| 4 | **Geen medische claim en geen verboden woord.** Gezocht op apnea/apnee, freediving, estrés, ansiedad/ansia, curar/guarire, salud/salute, sueño/sonno, terapia, pulmón/polmone, oxígeno/ossigeno: niets. "relajación" en "rilassamento" in de tags staan gelijk aan "relaxation" in de gekeurde Engelse tekst. Het besluit van 12 nov (Ebb nooit apneatrainer) is gevolgd: ook het Spaanse en Italiaanse gangbare woord "apnea" is bewust gemeden. | feit | hoog | |
| 5 | **Lengtes binnen de grens (zelf geteld, tekens).** Spaans: titel 46, tekst 3.154. Italiaans: titel 39, tekst 3.062. Gelijk aan het voorstel. Ruim onder 50 en 4.000, ook als het formulier regeleinden dubbel telt (16 regeleinden). | feit | hoog | |
| 6 | **"Wat er nu staat" klopt (zelf nagemeten).** API: `appLocalizations` = de, nl, en, fr, met de Duitse titel "Ebb: Breathwork, Atemübungen & Atem anhalten" vooraan; prijs $2.99 USD. De winkelpagina `/es-ES/` en `/it-IT/` geeft als titel "Ebb: Breathwork, Atemübungen & Atem anhalten \| Connect IQ Store" en de Duitse tekst. Zoek-API: respiración 994 treffers, respirazione 990, ejercicios de respiración 985, esercizi di respirazione 996; Ebb en Calm staan op alle vier niet alleen niet in de eerste 30, maar ook niet in de eerste 90. | feit (GEZIEN) | hoog | |
| 7 | **"Waarom" punt 2 klopt (zelf nagemeten).** breathwork: Ebb 7, Calm 42; souffle: Ebb 2, Calm 10; respiration: Ebb 12, Calm 17. Gelijk aan `meting-weekronde.md`. De verwachting voor respiración en respirazione staat eerlijk als GOK. | feit (GEZIEN) | hoog | Zelfde zoek-API drie dagen na plakken |
| 8 | **"Waarom" punt 3: "de twee grootste landen zonder eigen tekst" heeft geen label.** Of Spanje en Italië de grootste zijn voor Garmin is niet gemeten; Portugees (Brazilië) en Pools zijn ook groot. Het is een GOK (kan-punt 11). | feit | hoog | Verkoopcijfers per land (alleen Thijs) |
| 9 | **De gekeurde Engelse zin "Ebb has everything in the free Ebb Calm, plus breath hold rounds, My pattern and 24 sea animals." ontbreekt** in beide teksten. Daardoor zegt de tekst wel dat Calm gratis is, maar niet meteen wat de betaalde Ebb meer heeft. Dat kost mogelijk een verkoop (kan-punt 1). | feit (ontbreekt), vermoeden (effect) | midden | |
| 10 | **Spaans is goed en natuurlijk genoeg voor een winkel.** Goed: "respiración cuadrada (box breathing)", "sentado o tumbado", "¿Mareo u hormigueo?", "tensión arterial", "un solo pago, sin suscripción". Klein stroef: komma's ontbreken in "Al inspirar el agua sube, al espirar baja ..."; "en tierra" (gangbaar: "en tierra firme"); "4 dentro, 7 retener, 8 fuera" is telegramstijl; "toma una gran inspiración" klinkt vertaald. | feit (mijn lezing) | midden | Een Spaanstalige lezer |
| 11 | **Italiaans is goed, op een paar plekken stroef.** Goed: "seduto o sdraiato", "sulla terraferma", "capogiri o formicolii", "respirazione quadrata", "nessun abbonamento". Stroef: "Dopo cinque minuti la pausa finisce da sola": "pausa" kan gelezen worden als de pauzeknop van Ebb, bedoeld is het inhouden; "Premi un tasto per finire" (wat?); "Salvata in Garmin Connect ..." zonder onderwerp; "3 sessioni di base" (gangbaar: "predefinite"); "il tuo tempo medio" (gemiddelde van wat?). De titel zet een zelfstandig naamwoord naast een werkwoord ("respirazione e trattenere il fiato"); begrijpelijk, maar niet mooi. | feit (mijn lezing) | midden | Een Italiaanstalige lezer |
| 12 | **De mail is Engels, maar dat staat er niet bij.** In het Frans staat "(en anglais)" bij het mailadres; hier niet. Wel staat "La app está en inglés" / "L'app è in inglese" onderaan. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens; het mailadres is het zakelijke adres dat al live staat. `organisatie/controle/check.py`: "Controle openbare repo: OK". De woonplaats op de Garmin-pagina is niet overgenomen. | feit | hoog | harde regel 2 |
| 2 | Cijfers hebben GEZIEN of GOK, met bron en tijd. Eén zin zonder label (A8). | feit | hoog | harde regel 5 |
| 3 | Niets uitgegeven, niets geplakt; plakken doet de hoofdchat na keuring. Stopregel bij een vraag om een nieuwe versie staat erin. | feit | hoog | harde regels 1 en 4 |
| 4 | Geen apnea, freediving of medische claim. | feit | hoog | besluit 12 nov, 16 nov |
| 5 | Toetst aan de hoofdzaak geld: kopers in Spanje en Italië zien nu een Duitse pagina; klein werk, geen kosten. Eerlijk dat het effect een GOK is. | feit | midden | hoofdzaak 19 nov |

## Deel C: zou een koper het fijn en duidelijk vinden?

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een Spaanse of Italiaanse koper ziet nu Duits; met deze tekst ziet hij zijn eigen taal, de prijs zonder abonnement en de veiligheid. Grote stap vooruit. | Plakken | klein |
| 2 | Hij leest dat Calm gratis is, maar niet wat Ebb meer heeft. | Kan-punt 1 | klein |
| 3 | Hij leest niet dat hij in het Engels moet mailen. | Kan-punt 10 | klein |

## Moet (blokkeert akkoord)
Geen. De vertaling klopt inhoudelijk met de gekeurde Engelse tekst, alle veiligheidszinnen staan erin, er is geen medische claim of verboden woord, de lengtes passen en de cijfers kloppen met mijn eigen meting.

## Kan (liefst vóór het plakken; alle lengtes blijven ruim onder 4.000)
1. **Wat Ebb meer heeft (A9).**
   Spaans, oud: `¿Quieres probar el mar primero? Ebb Calm es gratis, solo con respiración 4-7-8:`
   nieuw: `Ebb tiene todo lo de Ebb Calm, más rondas de retención, My pattern y 24 animales marinos. ¿Quieres probar el mar primero? Ebb Calm es gratis, solo con respiración 4-7-8:`
   Italiaans, oud: `Vuoi provare prima il mare? Ebb Calm è gratuita, solo con la respirazione 4-7-8:`
   nieuw: `Ebb ha tutto ciò che c'è in Ebb Calm, più i cicli di respiro trattenuto, My pattern e 24 animali marini. Vuoi provare prima il mare? Ebb Calm è gratuita, solo con la respirazione 4-7-8:`
2. **Italiaans "pausa" (A11).** Oud: `Dopo cinque minuti la pausa finisce da sola;` nieuw: `Dopo cinque minuti la ritenzione del respiro si ferma da sola;`
3. **Herstel-inhouding terug (A3).**
   Spaans, oud: `toma una gran inspiración para recuperarte.` nieuw: `haz una inspiración profunda y retenla un momento para recuperarte.`
   Italiaans, oud: `poi fai un grande respiro per recuperare.` nieuw: `poi fai un respiro profondo e trattienilo per qualche secondo per recuperare.`
4. **4-7-8 als zin.** Spaans, oud: `4-7-8: 4 dentro, 7 retener, 8 fuera.` nieuw: `4-7-8: inspira 4, retén 7, espira 8.` Italiaans, oud: `4-7-8: 4 dentro, 7 trattieni, 8 fuori.` nieuw: `4-7-8: inspira 4, trattieni 7, espira 8.`
5. **Spaanse komma's.** Oud: `Al inspirar el agua sube, al espirar baja y al retener la respiración pasas bajo el agua; cada fase tiene su propia vibración` nieuw: `Al inspirar, el agua sube; al espirar, baja; al retener la respiración, pasas bajo el agua. Cada fase tiene su propia vibración`
6. **Spaans "tierra firme".** Oud: `Practica solo en tierra:` nieuw: `Practica solo en tierra firme:`
7. **Italiaans knop.** Oud: `Premi un tasto per finire,` nieuw: `Premi un tasto per smettere di trattenere,`
8. **Italiaans onderwerp.** Oud: `• Salvata in Garmin Connect come attività` nieuw: `• Ogni sessione viene salvata in Garmin Connect come attività`
9. **Italiaans kleine woorden.** Oud: `3 sessioni di base` nieuw: `3 sessioni predefinite`. Oud: `e il tuo tempo medio.` nieuw: `e il tuo tempo medio trattenuto.`
10. **Mail in het Engels (A12).** Spaans, oud: `Soporte: thijs@dortus.com, con` nieuw: `Soporte: thijs@dortus.com (en inglés), con`. Italiaans, oud: `Assistenza: thijs@dortus.com, con` nieuw: `Assistenza: thijs@dortus.com (in inglese), con`
11. **Label in "Waarom" punt 3 (A8).** Oud: `voor de twee grootste landen zonder eigen tekst.` nieuw: `voor twee grote landen zonder eigen tekst (GOK: welke landen het meest kopen, ziet alleen Thijs).`
12. **Italiaanse titel (A11), alleen als je het mooier wilt:** `Ebb: respirazione e respiro trattenuto` (38 tekens) is grammaticaal netter, maar verliest het woord "trattenere" uit de titel. Laten staan mag; de huidige titel is begrijpelijk en eerlijk.
13. **Meten:** zet respiración, respirazione, ejercicios de respiración, esercizi di respirazione en (Italiaans) trattenere il fiato in de meting van volgende week, eerste 90, zodat de GOK uit "Waarom" punt 2 een GEZIEN wordt.

akkoord ja (geen moet-punten; kan-punten 1 tot 13, punt 1 tot 3 het liefst vóór het plakken)
