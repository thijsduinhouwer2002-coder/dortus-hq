# Garmin: winkelvoorstel van de week (23 nov 2026)

> **Let op, hoofdchat: plak de Spaanse en Italiaanse blokken hieronder NIET.** Na het schrijven en keuren vond ik dat Chris dezelfde klus al groter deed: Ebb en Ebb Calm in 10 extra talen (es, it, pt, pl, sv, da, fi, nb, cs, ja) in `platformen/garmin/upload/ebb-<taal>.md` en `calm-<taal>.md`, door Daan herkeurd met akkoord ja voor alle 20 (`ontwerp/garmin/talen-10-herkeuring-daan-2026-11-23.md`, 23 nov 10:25 NL). **De verbetering van deze week is dus: die 20 gekeurde teksten plakken**, eerst Ebb es en it (daar zien bezoekers nu Duits), dan de rest. Mijn eigen es/it hieronder blijft alleen als reserve, voor het geval een tekst van Chris in het formulier niet past.

Gemaakt door de Garmin-ronde (maandag). Eén verbetering: **Ebb krijgt een Spaanse en een Italiaanse winkeltekst.** Voor de hoofdchat om in Chrome te plakken, na keuring (onderaan).

## Wat er nu staat (GEZIEN, 23 nov ±09:30 UTC, `curl` op `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/5280653d-1681-452d-8c03-7cbdc7284641`, veld `appLocalizations`)

- Ebb heeft vier talen in deze volgorde: `de`, `nl`, `en`, `fr`. Frans is er sinds 20 nov bij, maar Duits staat nog steeds vooraan.
- De winkel toont een bezoeker zonder eigen taal de eerste taal uit de lijst (code van de winkel: `appLocalizations.find(...) || appLocalizations[0]`, GEZIEN op 20 nov in `winkel-vindbaar-2026-11-20.md`). Een Spaanse of Italiaanse bezoeker ziet dus de Duitse titel "Ebb: Breathwork, Atemübungen & Atem anhalten" en de Duitse tekst.
- Op de Spaanse en Italiaanse zoekwoorden staat Ebb nergens in de eerste 30: "respiración" (994 treffers), "respirazione" (990), "ejercicios de respiración" (985), "esercizi di respirazione" (996). Ebb Calm ook niet (GEZIEN, 23 nov).

## Wat het wordt

Twee talen toevoegen aan Ebb: Spaans (`es`) en Italiaans (`it`), met de teksten hieronder. Niets anders aanraken (geen andere taal, geen beelden, geen "wat is nieuw", geen nieuwe versie).

## Waarom

1. **Geld:** een Spaanse of Italiaanse koper die een Duitse pagina ziet over een app van $2,99, koopt minder snel (GOK; hoeveel bezoekers uit die landen komen, ziet niemand van ons). Met een eigen tekst ziet hij zijn eigen taal, met "un solo pago, sin suscripción".
2. **Vindbaar:** de zoeker kijkt in de titels van alle talen tegelijk (GEZIEN 20 nov: "atem" en "ademhaling" geven Ebb op 1 via de Duitse en Nederlandse titel). Dat werkte deze week opnieuw: sinds "Breathwork" in de Duitse en Nederlandse titel staat, ging Ebb op "breathwork" van 33 naar 7, en via de Franse titel staat Ebb op "souffle" op 2 en op "respiration" op 12 (was niet in de eerste 90) (GEZIEN, `meting-weekronde.md`). Een Spaanse en Italiaanse titel geven dus waarschijnlijk treffers op "respiración" en "respirazione", waar Ebb nu niet staat (GOK tot gemeten).
3. **Het lost de taalvolgorde niet op, maar omzeilt hem** voor twee grote landen zonder eigen tekst (GOK: welke landen het meest kopen, ziet alleen Thijs). Pools, Portugees en de rest blijven Duits zien zolang Duits vooraan staat. Lukt het de hoofdchat in het formulier toch om Engels vooraan te zetten, dan is dat nog beter; het plakblok van 20 nov beschrijft hoe je dat kunt proberen.

## Zo plak je

- Formulier van Ebb (Connect IQ, app bewerken), taal toevoegen: Spaans, dan Italiaans. Plak alleen wat in de grijze blokken staat, precies zo, met de lege regels.
- Titel hoogstens 50 tekens, tekst hoogstens 4.000 (afgeleid, zie `winkel-plak-2026-11-20.md`). Beide blokken blijven eronder.
- Vraagt het formulier om een nieuwe versie of weigert het iets: stop en meld het in `berichten/hoofdchat.md` aan de Garmin-ronde. Niet raden.
- Controle na opslaan zonder inloggen: `curl -s https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/5280653d-1681-452d-8c03-7cbdc7284641` moet `es` en `it` in `appLocalizations` tonen.

### Spaans (es)

Titel (46 tekens; tekst 3.288 tekens):
```
Ebb: respiración y retención de la respiración
```

Beschrijving:
```
Rondas de retención de la respiración y ejercicios de respiración tranquila en tu Garmin, dibujados como un pequeño mar. Al inspirar, el agua sube; al espirar, baja; al retener la respiración, pasas bajo el agua. Cada fase tiene su propia vibración, para que puedas seguirla con los ojos cerrados. Un solo pago, sin suscripción. Practica solo en tierra firme: sentado o tumbado, nunca en el agua ni cerca de ella, nunca mientras conduces. Retén solo mientras te resulte fácil.

Ebb tiene todo lo de Ebb Calm, más rondas de retención, My pattern y 24 animales marinos. ¿Quieres probar el mar primero? Ebb Calm es gratis, solo con respiración 4-7-8: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

• Rondas de retención: respiraciones profundas a un ritmo fijo, luego espira y retén el tiempo que te parezca bien. Pulsa un botón para terminar la retención y haz una inspiración profunda y retenla un momento para recuperarte. A partir de 3:00 el reloj muestra "breathe" arriba. A los cinco minutos la retención termina sola; la sesión se cierra y se guarda. Antes de cada sesión Ebb te recuerda: siéntate o túmbate.
• 4-7-8: inspira 4, retén 7, espira 8. My pattern: tus propios segundos en los ajustes, por ejemplo 4-4-4-4 para la respiración cuadrada (box breathing).
• Colecciona 24 animales marinos por constancia (sesiones y semanas seguidas con tu objetivo semanal, 3 sesiones por defecto, ajustable de 2 a 7; los días de descanso nunca rompen tu racha), nunca por retener más tiempo. Cuentan como máximo dos sesiones al día.
• Después de las rondas, tu tiempo de retención por ronda; después de 4-7-8, la duración y tus respiraciones. En el menú: hoy tus sesiones como barras y 8 semanas de sesiones por semana y tu retención media.
• Vibración propia para cada fase; durante la retención, si quieres, una vibración suave cada 30 segundos. La vibración se puede desactivar. Una señal sigue activa: cada 30 segundos a partir de 3:00 de retención, por tu seguridad. Al respirar y retener, la pantalla táctil no hace nada; solo funcionan los botones. Ebb no hace ningún sonido.
• Se guarda en Garmin Connect como actividad de respiración con tu frecuencia cardiaca; en las rondas, una vuelta por ronda con su tiempo de retención. Solo informativo, sin puntuación.
• Un solo pago en la tienda de Garmin. Sin suscripción, sin código por correo, sin cuenta extra, sin app de móvil.
• Privacidad: Ebb no recoge nada. Tus sesiones, animales y ajustes se quedan en tu reloj; solo una actividad guardada va a Garmin Connect (política de privacidad de Garmin). Sin análisis, sin anuncios.
• Soporte: thijs@dortus.com (en inglés), con el modelo de tu reloj. Intentamos responder en 5 días laborables. Los reembolsos siguen las normas de la Connect IQ Store de Garmin: 48 horas para devolver tras la compra.

La app está en inglés. Sin tablas de CO2, no es un dispositivo médico. Seguridad: sentado o tumbado. Nunca en el agua ni cerca de ella, nunca en la bañera, nunca mientras conduces. ¿Mareo u hormigueo? Para y respira con normalidad. No si estás embarazada, eres menor de 18 años o tienes epilepsia, problemas de corazón o de tensión arterial.

Tags: ejercicios de respiración, respiración, retener la respiración, respiración cuadrada, 4-7-8, 478, relajación, breathing
```

### Italiaans (it)

Titel (39 tekens; tekst 3.287 tekens):
```
Ebb: respirazione e trattenere il fiato
```

Beschrijving:
```
Cicli in cui trattieni il fiato ed esercizi di respirazione calma sul tuo Garmin, disegnati come un piccolo mare. Quando inspiri l'acqua sale, quando espiri scende e quando trattieni il fiato vai sott'acqua; ogni fase ha la sua vibrazione, così puoi seguirla a occhi chiusi. Un solo pagamento, nessun abbonamento. Pratica solo sulla terraferma: seduto o sdraiato, mai in acqua o vicino all'acqua, mai alla guida. Trattieni solo finché è facile.

Ebb ha tutto ciò che c'è in Ebb Calm, più i cicli di respiro trattenuto, My pattern e 24 animali marini. Vuoi provare prima il mare? Ebb Calm è gratuita, solo con la respirazione 4-7-8: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

• Cicli di respiro trattenuto: respiri profondi a ritmo fisso, poi espira e trattieni finché ti senti bene. Premi un tasto per smettere di trattenere, poi fai un respiro profondo e trattienilo per qualche secondo per recuperare. Da 3:00 l'orologio mostra "breathe" in alto. Dopo cinque minuti la ritenzione del respiro si ferma da sola; la sessione si chiude e viene salvata. Prima di ogni sessione Ebb ti ricorda: siediti o sdraiati.
• 4-7-8: inspira 4, trattieni 7, espira 8. My pattern: i tuoi secondi nelle impostazioni, per esempio 4-4-4-4 per la respirazione quadrata (box breathing).
• Colleziona 24 animali marini con la costanza (sessioni e settimane di fila con il tuo obiettivo settimanale, 3 sessioni predefinite, regolabile da 2 a 7; i giorni di riposo non interrompono mai la serie), mai trattenendo più a lungo. Contano al massimo due sessioni al giorno.
• Dopo i cicli, il tempo trattenuto per ciclo; dopo 4-7-8, la durata e i respiri. Nel menu: oggi le tue sessioni come barre e 8 settimane di sessioni per settimana e il tuo tempo medio trattenuto.
• Una vibrazione propria per ogni fase; mentre trattieni, se vuoi, una vibrazione leggera ogni 30 secondi. La vibrazione si può disattivare. Un segnale resta attivo: ogni 30 secondi dopo 3:00, per la tua sicurezza. Mentre respiri e trattieni, il touchscreen non fa nulla; funzionano solo i tasti. Ebb non emette suoni.
• Ogni sessione viene salvata in Garmin Connect come attività di respirazione con la frequenza cardiaca; nei cicli, un giro per ciclo con il suo tempo. Solo a titolo informativo, nessun punteggio.
• Un solo pagamento nello store di Garmin. Nessun abbonamento, nessun codice via e-mail, nessun account extra, nessuna app per telefono.
• Privacy: Ebb non raccoglie nulla. Sessioni, animali e impostazioni restano sull'orologio; solo un'attività salvata va a Garmin Connect (informativa privacy di Garmin). Nessuna analisi, nessuna pubblicità.
• Assistenza: thijs@dortus.com (in inglese), con il modello del tuo orologio. Cerchiamo di rispondere entro 5 giorni lavorativi. I rimborsi seguono le regole del Connect IQ Store di Garmin: 48 ore per il reso dopo l'acquisto.

L'app è in inglese. Nessuna tabella CO2, non è un dispositivo medico. Sicurezza: seduto o sdraiato. Mai in acqua o vicino all'acqua, mai nella vasca, mai alla guida. Capogiri o formicolii? Fermati e respira normalmente. Non in gravidanza, sotto i 18 anni o con epilessia, problemi cardiaci o di pressione.

Tags: esercizi di respirazione, respirazione, trattenere il respiro, respirazione quadrata, 4-7-8, 478, rilassamento, breathing
```

Wat is nieuw: niet aanraken.

## Keuring

Gekeurd door een aparte keurder met de skill `keuren` (23 nov 2026): **akkoord ja, geen moet-punten.** Verslag: `winkel-voorstel-2026-11-23-KEURING.md`. De kan-punten 1 tot 11 zijn daarna letterlijk overgenomen zoals de keurder ze opgaf; 12 (andere Italiaanse titel) niet, 13 (Spaanse en Italiaanse woorden meten in de eerste 90) doet de volgende ronde.
