# Garmin: plakklaar voor de winkel (20 nov 2026)

Voor de hoofdchat, om letterlijk via Chrome te plakken in het formulier van Garmin (Connect IQ, app bewerken). Gemaakt door de Garmin-winkelmaker. Bron: `winkel-vindbaar-2026-11-20.md`. Keuring: `winkel-vindbaar-KEURING.md` (akkoord ja, geen moet-punten). Verwerkt: de kan-punten 1, 2, 3, 5, 6 en 7 van de keurder.

**Nieuw sinds de keuring, dus nog niet door de keurder gezien:** in de Engelse tekst van Ebb (kan-punt 6) staat nu de zin "Ebb has everything in the free Ebb Calm, plus breath hold rounds, My pattern and 24 sea animals." De kop "CALM BREATHING: 4-7-8 AND MY PATTERN" heet nu "4-7-8 AND MY PATTERN". Om onder 4.000 tekens te blijven zijn vier dingen ingekort: "That hold is not averaged." weg, "calm" weg uit de tags, "exactly" weg in de zin over de Sea log, en "For interest only; Ebb gives no score." is nu "For interest only, no score." Geen veiligheidszin is weggehaald. Alle andere blokken zijn de gekeurde tekst, met de wijzigingen die de keurder letterlijk opgaf.

## Zo plak je

- Plak alleen wat in de grijze blokken staat, precies zo, met de lege regels.
- **Wat is nieuw:** niet aanraken. We uploaden geen nieuwe versie; de huidige tekst bij 1.0.1 blijft staan.
- **Lengtegrens:** titel hoogstens 50 tekens, beschrijving hoogstens 4.000. Garmin publiceert die grenzen niet; ze zijn **afgeleid** uit 8.679 titels en teksten uit de zoek-API (de keurder telde er 18.106): geen enkele kwam boven 50 of 4.000. Alle blokken hieronder blijven eronder (langste titel 45, langste tekst 3.977).
- Volgorde van werken: eerst de taalvolgorde van Ebb, dan de teksten, dan de beeldvolgorde. Weigert het formulier iets, of vraagt het om een nieuwe versie: stop, plak niets meer en meld het aan de Garmin-winkelmaker. Niet raden.
- Na het opslaan controleren zonder in te loggen: `curl -s https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` (veld `appLocalizations`) en de pagina `https://apps.garmin.com/es-ES/apps/<id>` (moet een Engelse titel tonen).

## 1. Ebb Breathing & Breath Hold (betaald, id 5280653d-1681-452d-8c03-7cbdc7284641)

**Taalvolgorde: Engels, Duits, Nederlands, Frans.** Nu is het Duits, Nederlands, Engels, en daardoor ziet elke bezoeker in een andere taal (Frans, Spaans, Italiaans, Pools en meer) de Duitse pagina (GEZIEN, ook door de keurder). Hoe je de volgorde in het formulier verandert, heeft niemand van ons gezien. Probeer: (1) een veld voor standaardtaal of hoofdtaal op Engels zetten; (2) gaat dat niet: Frans toevoegen en daarna Duits en Nederlands weghalen en opnieuw toevoegen met de teksten hieronder, zodat Engels vooraan komt. Klaar als de API `en` als eerste `locale` geeft.

#### Engels (en)

Titel (27 tekens):
```
Ebb Breathing & Breath Hold
```

Beschrijving (3977 tekens):
```
Breath hold rounds and calm breathing exercises on your Garmin, drawn as a small sea. Breathe in and the water rises, breathe out and it falls, hold your breath and you go under water; every phase has its own vibration, so you can follow with your eyes closed. One payment, no subscription. For practice on land only: sit or lie down, never in or near water, never while driving. Hold only while it feels easy.

Ebb has everything in the free Ebb Calm, plus breath hold rounds, My pattern and 24 sea animals. Try the sea first with Ebb Calm: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

BREATH HOLD ROUNDS
• Rounds of deep breaths at a steady pace, then breathe out and hold for as long as feels right.
• Press a button to end the hold, then take one big breath in and hold it briefly to recover.
• While you hold, you are under water with a sea animal. The picture stays the same however long you hold. From 3:00 on the watch shows "breathe" at the top. A hold stops by itself after five minutes; the session then ends and saves.
• Before every session Ebb reminds you: sit or lie down.

4-7-8 AND MY PATTERN
• 4-7-8: breathe in for 4, hold for 7, out for 8, with the sea rising and falling.
• My pattern: set your own seconds in, hold, out and hold in the settings, for example 4-4-4-4 for box breathing or 5-0-5-0 for slow, even breathing.

COLLECT SEA ANIMALS BY SHOWING UP
• 24 sea animals, earned with sessions and weeks in a row, never by holding longer. A small fish swims with you from your first session.
• Your streak counts weeks in which you reach your weekly goal (3 sessions, or set 2 to 7), so rest days never break it.
• A session counts with at least one hold, or one minute of calm breathing. Up to two sessions a day count.
• New animals appear at the end of a session, one at a time, plus one bonus animal to discover. The Sea log shows your animals and how to get the next one.

SEE YOUR PRACTICE
• After rounds: your hold time for every round and your week. After calm breathing: how long you breathed and your breaths.
• Today: the holds of your sessions today as bars. 8 weeks: your sessions per week and your average hold.

BREATHE WITH YOUR EYES CLOSED
• Every phase has its own vibration. The last three breaths before the hold feel different.
• A soft buzz every 30 seconds while you hold, if you like. Vibration can be turned off. One buzz stays on: every 30 s after 3:00 of holding, for your safety.
• While you breathe and hold, the touchscreen does nothing, so a sleeve cannot stop a hold; only the buttons work. Ebb makes no sound.

SAVED IN GARMIN CONNECT
• Each session is saved as a breathing activity with your heart rate. Rounds: one lap per round with its hold time and breaths. For interest only, no score.
• A finished session saves itself. Calm breathing, and a session left paused, save by themselves after 30 minutes. Press back to pause: resume, save or discard.

SETTINGS ON THE WATCH
Breaths per round, pace, rounds, recovery hold, weekly goal, vibration and My pattern. No phone needed.

ONE PAYMENT, NOTHING COLLECTED
• One payment in the Garmin store. No subscription, no unlock code by e-mail, no extra account, no phone app.
• Ebb collects nothing. Your sessions, animals and settings stay on your watch. Only a saved activity goes to Garmin Connect, under Garmin's privacy policy. No analytics, no ads.

SUPPORT AND REFUNDS
Mail thijs@dortus.com with your watch model. We aim to reply within 5 working days. Refunds follow Garmin's Connect IQ Store policy: a 48-hour return window after you buy.

SAFETY
Sit or lie down. Never practise breath holds in or near water, in the bath, or while driving. Feel dizzy or tingly? Stop and breathe normally. Not if pregnant, under 18, or with epilepsy, heart or blood pressure problems. Ebb has no CO2 or O2 tables and is not a medical device.

Tags: breathing exercises, breathing, breath hold, breathwork, box breathing, breath training, 4-7-8, 478, relaxation
```

Wat is nieuw: niet aanraken.

#### Duits (de)

Titel (44 tekens):
```
Ebb: Breathwork, Atemübungen & Atem anhalten
```

Beschrijving (3438 tekens):
```
Atem anhalten in Runden und ruhige Atemübungen auf deiner Garmin, gezeichnet als kleines Meer. Beim Einatmen steigt das Wasser, beim Ausatmen sinkt es, beim Anhalten tauchst du unter; jede Phase hat ihre eigene Vibration, sodass du mit geschlossenen Augen folgen kannst. Einmal zahlen, kein Abo. Nur an Land üben: im Sitzen oder Liegen, nie im oder am Wasser, nie beim Autofahren. Halte den Atem nur an, solange es leichtfällt.

Erst das Meer ausprobieren? Ebb Calm ist kostenlos, nur mit 4-7-8-Atmung: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

• Atemrunden: tiefe Atemzüge in festem Tempo, dann ausatmen und halten, solange es sich gut anfühlt. Ab 3:00 zeigt die Uhr oben "breathe". Nach fünf Minuten endet das Anhalten von selbst: die Uhr geht zur Erholung über, beendet dann die Sitzung und speichert sie. Dieses Anhalten zählt nicht im Durchschnitt. Vor jeder Sitzung, auch bei Calm und My pattern, erinnert Ebb: setz oder leg dich hin.
• Sammle 24 Meerestiere durch Dranbleiben (Sitzungen und Wochen in Folge mit deinem Wochenziel, standardmäßig 3 Sitzungen, einstellbar 2 bis 7; Ruhetage unterbrechen die Serie nie), nie durch längeres Halten. Pro Tag zählen bis zu zwei Sitzungen. Neue Tiere kommen am Ende einer Sitzung, dazu ein Bonustier. Alle 24 gefunden: dein Meer ist komplett, deine Wochenserie zählt weiter.
• Calm 4-7-8: 4 ein, 7 halten, 8 aus. My pattern: eigene Sekunden in den Einstellungen, zum Beispiel 4-4-4-4 für Box-Atmung. Eine Sitzung zählt ab einem Anhalten oder einer Minute Calm.
• Nach Atemrunden deine Haltezeit pro Runde, nach Calm deine Dauer und Atemzüge; beim ersten kompletten Meer stattdessen ein Festbild mit allen 24 Tieren. Jederzeit im Menü: heute deine Sitzungen als Balken (bis drei) und über 8 Wochen Sitzungen pro Woche und deine durchschnittliche Haltezeit.
• Eigene Vibration für jede Phase, auch mit geschlossenen Augen; beim Halten auf Wunsch alle 30 Sekunden ein sanftes Vibrieren. Die Vibration lässt sich abschalten. Ein Signal bleibt an: alle 30 Sekunden ab 3:00 Anhalten, zu deiner Sicherheit. Beim Atmen und Halten reagiert der Touchscreen nicht; im Pausenmenü kannst du tippen. Ebb macht keinen Ton.
• Wird als Atemaktivität mit Herzfrequenz in Garmin Connect gespeichert; bei Atemrunden ein Lap pro Runde mit Haltezeit und Atemzügen, nur zur Info, ohne Bewertung. Eine fertige Sitzung speichert sich selbst, Calm und eine pausierte Sitzung nach 30 Minuten ebenfalls; Zurück-Taste für Pause: weiter, speichern oder verwerfen.
• Einmal zahlen. Kein Abo, kein Code per E-Mail, kein zusätzliches Konto, keine Handy-App.
• Datenschutz: Ebb sammelt nichts. Sitzungen, Tiere und Einstellungen bleiben auf der Uhr; nur eine gespeicherte Aktivität geht an Garmin Connect (Datenschutzerklärung von Garmin). Keine Analyse, keine Werbung.
• Support: thijs@dortus.com, mit deinem Uhrenmodell. Wir antworten möglichst innerhalb von 5 Werktagen. Erstattungen folgen den Regeln des Garmin Connect IQ Store: Garmin gibt dir nach dem Kauf 48 Stunden Rückgabefrist.

Die App ist auf Englisch. Keine CO2-Tabellen, kein Medizinprodukt. Sicherheit: im Sitzen oder Liegen. Nie im oder am Wasser, nie in der Badewanne, nie beim Autofahren. Schwindelig oder Kribbeln? Aufhören und normal atmen. Nicht bei Schwangerschaft, unter 18, bei Epilepsie, Herz- oder Blutdruckproblemen.

Tags: Atemübungen, Atemtraining, Atem anhalten, Box-Atmung, 4-7-8, 478, Entspannung, Atmung, breathing
```

Wat is nieuw: niet aanraken.

#### Nederlands (nl)

Titel (43 tekens):
```
Ebb: breathwork, ademhaling & adem inhouden
```

Beschrijving (3367 tekens):
```
Rondes met adem inhouden en rustige ademhalingsoefeningen op je Garmin, getekend als een kleine zee. Adem in en het water stijgt, adem uit en het zakt, houd je adem in en je gaat onder water; elke fase heeft een eigen trilling, zodat je met je ogen dicht kunt volgen. Eén keer betalen, geen abonnement. Alleen op het droge: zittend of liggend, nooit in of bij water, nooit achter het stuur. Houd alleen in zolang het makkelijk gaat.

Eerst de zee proberen? Ebb Calm is gratis, alleen met 4-7-8-ademen: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

• Ademrondes: diepe ademhalingen in een vast tempo, dan uitademen en inhouden zolang het goed voelt. Vanaf 3:00 toont het horloge bovenaan "breathe". Na vijf minuten stopt het inhouden vanzelf: het horloge gaat door naar herstel, sluit dan de sessie af en slaat hem op. Die inhouding telt niet mee in je gemiddelde. Voor elke sessie, ook Calm en My pattern, zegt Ebb: ga zitten of liggen.
• Verzamel 24 zeedieren door vol te houden (sessies en weken op rij met je weekdoel, standaard 3 sessies, in te stellen van 2 tot 7; rustdagen breken je reeks nooit), nooit door langer in te houden. Per dag tellen hoogstens twee sessies. Nieuwe dieren komen aan het eind van een sessie, plus één bonusdier. Alle 24 gevonden: je zee is compleet en je reeks in weken telt door.
• Calm 4-7-8: 4 in, 7 vasthouden, 8 uit. My pattern: eigen seconden in de instellingen, bijvoorbeeld 4-4-4-4 voor box breathing. Een sessie telt vanaf één inhoud of één minuut Calm.
• Na ademrondes je inhoudtijd per ronde, na Calm je duur en ademhalingen; de eerste keer dat je zee compleet is krijg je in plaats daarvan een feestscherm met alle 24 dieren. Altijd in het menu: vandaag je sessies als staven (tot drie) en over 8 weken sessies per week en je gemiddelde inhoudtijd.
• Eigen trilling per fase, ook met je ogen dicht; tijdens inhouden als je wilt elke 30 seconden een zachte tril. Trillen kun je uitzetten. Eén tril blijft aan: elke 30 seconden na 3:00 inhouden, voor je veiligheid. Tijdens ademen en inhouden doet het aanraakscherm niets; in het pauzemenu kun je tikken. Ebb maakt geen geluid.
• Opgeslagen als ademactiviteit met hartslag in Garmin Connect; bij ademrondes één lap per ronde met inhoudtijd en ademhalingen, alleen ter info, zonder score. Een afgeronde sessie slaat zichzelf op, Calm en een sessie in pauze doen dat na 30 minuten ook; terugknop voor pauze: doorgaan, opslaan of weggooien.
• Eén keer betalen. Geen abonnement, geen code per mail, geen extra account, geen telefoonapp.
• Privacy: Ebb verzamelt niets. Sessies, dieren en instellingen blijven op je horloge; alleen een opgeslagen activiteit gaat naar Garmin Connect (privacybeleid van Garmin). Geen tracking, geen advertenties.
• Support: thijs@dortus.com, met je horlogemodel. We proberen binnen 5 werkdagen te antwoorden. Terugbetalen volgt de regels van de Garmin Connect IQ Store: Garmin geeft je na je aankoop 48 uur om terug te geven.

De app is in het Engels. Geen CO2-tabellen, geen medisch hulpmiddel. Veiligheid: zittend of liggend. Nooit in of bij water, nooit in bad, nooit achter het stuur. Duizelig of tintelingen? Stop en adem gewoon. Niet als je zwanger bent, onder de 18, of bij epilepsie, hart- of bloeddrukproblemen.

Tags: ademhalingsoefeningen, ademhaling, adem inhouden, box breathing, 4-7-8, 478, ontspanning, breathing
```

Wat is nieuw: niet aanraken.

#### Frans (fr, nieuw toevoegen)

Titel (41 tekens):
```
Ebb : rétention du souffle et respiration
```

Beschrijving (3632 tekens):
```
Des cycles de rétention du souffle et des exercices de respiration calmes sur votre Garmin, représentés par une petite mer. L'eau monte quand vous inspirez, descend quand vous expirez, et quand vous retenez votre souffle, vous passez sous l'eau ; chaque phase a sa propre vibration, pour suivre les yeux fermés. Un seul paiement, sans abonnement. Uniquement sur la terre ferme : assis ou allongé, jamais dans l'eau ou près de l'eau, jamais en conduisant. Ne retenez votre souffle que tant que c'est facile.

Envie d'essayer la mer d'abord ? Ebb Calm est gratuit, avec seulement la respiration 4-7-8 : https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

L'application est en anglais.

CYCLES DE RÉTENTION
• Des cycles de respirations profondes à un rythme régulier, puis vous expirez et retenez votre souffle aussi longtemps que c'est agréable.
• Appuyez sur un bouton pour terminer la rétention, puis prenez une grande inspiration et retenez-la brièvement pour récupérer.
• Pendant la rétention, vous êtes sous l'eau avec un animal marin. L'image reste la même, quelle que soit la durée. À partir de 3:00, la montre affiche « breathe » en haut. Une rétention s'arrête d'elle-même après cinq minutes ; la séance se termine alors et s'enregistre.
• Avant chaque séance, Ebb vous rappelle : asseyez-vous ou allongez-vous.

RESPIRATION CALME : 4-7-8 ET MY PATTERN
• 4-7-8 : inspirez 4 secondes, retenez 7, expirez 8, avec la mer qui monte et descend.
• My pattern : réglez vous-même les secondes d'inspiration, de pause, d'expiration et de pause, par exemple 4-4-4-4 pour la respiration carrée ou 5-0-5-0 pour une respiration lente et régulière.

DES ANIMAUX MARINS EN PRATIQUANT RÉGULIÈREMENT
• 24 animaux marins, gagnés par vos séances et vos semaines d'affilée, jamais en retenant plus longtemps.
• Votre série compte les semaines où vous atteignez votre objectif (3 séances, ou de 2 à 7) : les jours de repos ne la cassent jamais.
• Le Sea log montre vos animaux et comment obtenir le suivant.

VOTRE PRATIQUE
• Après les cycles : votre temps de rétention par cycle et votre semaine. Today et 8 weeks : vos séances du jour et par semaine.
• Chaque séance est enregistrée dans Garmin Connect comme activité de respiration, avec votre fréquence cardiaque ; un circuit par cycle. À titre indicatif, sans score.

LES YEUX FERMÉS
• Chaque phase a sa propre vibration. Les vibrations peuvent être coupées, sauf une : toutes les 30 s après 3:00 de rétention, pour votre sécurité.
• Pendant la séance, l'écran tactile ne fait rien : seuls les boutons fonctionnent. Ebb ne fait aucun son.

UN SEUL PAIEMENT, RIEN N'EST COLLECTÉ
• Un paiement dans la boutique Garmin. Pas d'abonnement, pas de code, pas de compte, pas d'app sur le téléphone.
• Ebb ne collecte rien. Vos données restent sur la montre ; seule une activité enregistrée va vers Garmin Connect, selon la politique de confidentialité de Garmin.

ASSISTANCE ET REMBOURSEMENT
Écrivez à thijs@dortus.com (en anglais) avec le modèle de votre montre. Nous visons une réponse sous 5 jours ouvrés. Remboursements selon la politique du Connect IQ Store de Garmin : 48 heures après l'achat.

SÉCURITÉ
Assis ou allongé. Ne pratiquez jamais la rétention dans l'eau ou près de l'eau, dans le bain, ni en conduisant. Vertiges ou fourmillements ? Arrêtez et respirez normalement. Pas en cas de grossesse, avant 18 ans, ni en cas d'épilepsie, de problèmes cardiaques ou de tension. Ebb n'a pas de tables CO2 ou O2 et n'est pas un dispositif médical.

Tags : respiration, exercices de respiration, rétention du souffle, souffle, respiration carrée, 4-7-8, 478, relaxation, breathing
```

Wat is nieuw: niet aanraken.

**Beeldvolgorde Ebb** (alle vijf bestaande beelden blijven, niets nieuws uploaden; herken ze aan de kop):
1. "Hold. The sea closes over." (nu beeld 3)
2. "Breathe. Make sea friends." (nu beeld 1)
3. "Breathe with the sea." (nu beeld 2)
4. "Fill your sea log." (nu beeld 5)
5. "Come back. Meet a crab." (nu beeld 4)

Video, icoon en prijs: niet aanraken.

## 2. Ebb Calm: Breathing Exercises & Relaxation (gratis, id bcc58192-667b-4bd8-a824-e6fe26794466)

**Taalvolgorde: Engels, Duits, Nederlands, Frans.** De eerste drie staan al zo; Frans komt achteraan erbij.

#### Engels (en): titel blijft gelijk

Titel (42 tekens):
```
Ebb Calm: Breathing Exercises & Relaxation
```

Beschrijving (2251 tekens):
```
Free 4-7-8 breathing exercises on your Garmin, drawn as a small sea. Breathe in for 4, hold for 7, out for 8: the water rises as you breathe in and falls as you breathe out, and every phase has its own vibration, so you can follow with your eyes closed. A simple breathing exercise for relaxation, to wind down in a calm moment. Sit or lie down while you practise.

Want more? The full Ebb, a separate paid app, adds breath hold rounds, your own breathing pattern (such as box breathing 4-4-4-4) and 24 sea animals to collect: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641

CALM 4-7-8 BREATHING
• Breathe in for 4 seconds, hold for 7, breathe out for 8. The watch counts every phase down.
• Your round watch face becomes a small sea. The water rises and falls with your breath, and a small fish keeps you company.
• Breathe as long as you like. Press back to pause: resume, save or discard.

BREATHE WITH YOUR EYES CLOSED
• In, hold and out each have their own vibration. Vibration can be turned off in the settings.
• While you breathe, the touchscreen does nothing, so a sleeve cannot stop your session; only the buttons work. Ebb Calm makes no sound.

SAVED IN GARMIN CONNECT
• Save a session and it becomes a breathing activity in Garmin Connect, with your heart rate.
• A session that keeps running saves itself after 30 minutes, and so does a session left paused.

FREE AND PRIVATE
• Free. No account, no subscription, no unlock code, no phone app, no ads.
• Ebb Calm collects nothing. Your settings stay on your watch. Only a saved activity goes to Garmin Connect, under Garmin's privacy policy. No analytics.

THE FULL EBB
Ebb Calm is the calm part of Ebb. The full Ebb, a separate paid app in this store, adds breath hold rounds, your own breathing pattern and 24 sea animals to collect.

SUPPORT
Mail thijs@dortus.com with your watch model. We aim to reply within 5 working days.

SAFETY
Sit or lie down. Never practise in or near water, in the bath, or while driving. Feel dizzy or tingly? Stop and breathe normally. Not if pregnant, under 18, or with epilepsy, heart or blood pressure problems. Ebb Calm is not a medical device.

Tags: breathing exercises, breathing, relaxation, calm, 4-7-8, 478, breathwork, wind down
```

Wat is nieuw: niet aanraken.

#### Duits (de): titel blijft gelijk

Titel (35 tekens):
```
Ebb Calm: Atemübungen & Entspannung
```

Beschrijving (2599 tekens):
```
Kostenlose 4-7-8-Atmung auf deiner Garmin, gezeichnet als kleines Meer. 4 Sekunden einatmen, 7 halten, 8 ausatmen: Das Wasser steigt beim Einatmen und sinkt beim Ausatmen, und jede Phase hat ihre eigene Vibration, sodass du mit geschlossenen Augen folgen kannst. Eine einfache Atemübung zur Entspannung, um in einem ruhigen Moment herunterzukommen. Setz dich oder leg dich hin, während du übst.

Lust auf mehr? Das ganze Ebb, eine eigene kostenpflichtige App, bietet zusätzlich Runden mit Atemanhalten, dein eigenes Atemmuster (zum Beispiel Box-Atmung 4-4-4-4) und 24 Meerestiere zum Sammeln: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641

RUHIGE 4-7-8-ATMUNG
• 4 Sekunden einatmen, 7 halten, 8 ausatmen. Die Uhr zählt jede Phase herunter.
• Dein rundes Display wird zu einem kleinen Meer. Das Wasser steigt und sinkt mit deinem Atem, und ein kleiner Fisch leistet dir Gesellschaft.
• Atme, so lange du möchtest. Mit Zurück pausierst du: fortsetzen, speichern oder verwerfen.

ATMEN MIT GESCHLOSSENEN AUGEN
• Einatmen, Halten und Ausatmen haben jeweils eine eigene Vibration. Die Vibration lässt sich in den Einstellungen ausschalten.
• Während du atmest, reagiert der Touchscreen nicht, sodass ein Ärmel deine Sitzung nicht beenden kann; nur die Tasten funktionieren. Ebb Calm macht kein Geräusch.

GESPEICHERT IN GARMIN CONNECT
• Speicherst du eine Sitzung, wird sie eine Atemaktivität in Garmin Connect, mit deiner Herzfrequenz.
• Eine Sitzung, die weiterläuft, speichert sich nach 30 Minuten von selbst, ebenso eine pausierte Sitzung.

KOSTENLOS UND PRIVAT
• Kostenlos. Kein Konto, kein Abo, kein Freischaltcode, keine Handy-App, keine Werbung.
• Ebb Calm sammelt nichts. Deine Einstellungen bleiben auf deiner Uhr. Nur eine gespeicherte Aktivität geht an Garmin Connect, nach der Datenschutzerklärung von Garmin. Keine Analyse.

DAS GANZE EBB
Ebb Calm ist der ruhige Teil von Ebb. Das ganze Ebb, eine eigene kostenpflichtige App in diesem Store, bietet zusätzlich Runden mit Atemanhalten, dein eigenes Atemmuster und 24 Meerestiere zum Sammeln.

SUPPORT
Schreib an thijs@dortus.com und nenne dein Uhrenmodell. Wir antworten in der Regel innerhalb von 5 Werktagen, auf Englisch.

SICHERHEIT
Setz dich oder leg dich hin. Übe nie im oder am Wasser, in der Badewanne oder beim Autofahren. Wird dir schwindlig oder kribbelt es? Hör auf und atme normal. Nicht in der Schwangerschaft, unter 18 oder bei Epilepsie, Herz- oder Blutdruckproblemen. Ebb Calm ist kein Medizinprodukt. Die App selbst ist auf Englisch.

Tags: Atmung, Atemübungen, Entspannung, ruhig, 4-7-8, 478, breathing
```

Wat is nieuw: niet aanraken.

#### Nederlands (nl): nieuwe titel

Titel (45 tekens):
```
Ebb Calm: ademhalingsoefeningen & ontspanning
```

Beschrijving (2360 tekens):
```
Gratis 4-7-8-ademhaling op je Garmin, getekend als een kleine zee. 4 tellen in, 7 vasthouden, 8 uit: het water stijgt als je inademt en zakt als je uitademt, en elke fase heeft een eigen trilling, zodat je met je ogen dicht kunt volgen. Een eenvoudige ademoefening om te ontspannen op een rustig moment. Ga zitten of liggen terwijl je oefent.

Meer willen? De volle Ebb, een aparte betaalde app, heeft daarnaast rondes met adem inhouden, je eigen adempatroon (bijvoorbeeld box breathing 4-4-4-4) en 24 zeedieren om te verzamelen: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641

RUSTIG 4-7-8-ADEMEN
• 4 seconden inademen, 7 vasthouden, 8 uitademen. Het horloge telt elke fase af.
• Je ronde scherm wordt een kleine zee. Het water stijgt en zakt met je adem, en een kleine vis houdt je gezelschap.
• Adem zo lang je wilt. Met terug pauzeer je: doorgaan, opslaan of weggooien.

ADEMEN MET JE OGEN DICHT
• In, vasthouden en uit hebben elk een eigen trilling. Trillen kan uit in de instellingen.
• Terwijl je ademt doet het aanraakscherm niets, zodat een mouw je sessie niet kan stoppen; alleen de knoppen werken. Ebb Calm maakt geen geluid.

OPGESLAGEN IN GARMIN CONNECT
• Sla je een sessie op, dan wordt het een ademactiviteit in Garmin Connect, met je hartslag.
• Een sessie die blijft lopen slaat zichzelf na 30 minuten op, en een sessie die op pauze blijft staan ook.

GRATIS EN PRIVÉ
• Gratis. Geen account, geen abonnement, geen code, geen telefoon-app, geen reclame.
• Ebb Calm verzamelt niets. Je instellingen blijven op je horloge. Alleen een opgeslagen activiteit gaat naar Garmin Connect, onder het privacybeleid van Garmin. Geen meetprogramma's.

DE VOLLE EBB
Ebb Calm is het rustige deel van Ebb. De volle Ebb, een aparte betaalde app in deze winkel, heeft daarnaast rondes met adem inhouden, je eigen adempatroon en 24 zeedieren om te verzamelen.

HULP
Mail thijs@dortus.com en noem je horlogemodel. We proberen binnen 5 werkdagen te antwoorden.

VEILIGHEID
Ga zitten of liggen. Oefen nooit in of bij water, in bad of tijdens het rijden. Duizelig of tintelingen? Stop en adem gewoon. Niet als je zwanger bent, jonger dan 18, of bij epilepsie, hart- of bloeddrukproblemen. Ebb Calm is geen medisch hulpmiddel. De app zelf is in het Engels.

Tags: ademhalingsoefeningen, ademhaling, ademen, ontspanning, rustig, 4-7-8, 478, breathing
```

Wat is nieuw: niet aanraken.

#### Frans (fr, nieuw toevoegen)

Titel (42 tekens):
```
Ebb Calm : respiration 4-7-8 et relaxation
```

Beschrijving (2334 tekens):
```
Respiration 4-7-8 gratuite sur votre Garmin, représentée par une petite mer. Inspirez 4 secondes, retenez 7, expirez 8 : l'eau monte quand vous inspirez et descend quand vous expirez, et chaque phase a sa propre vibration, pour suivre les yeux fermés. Un exercice de respiration simple pour se détendre dans un moment calme. Asseyez-vous ou allongez-vous pendant l'exercice.

Envie de plus ? L'Ebb complet, une app payante à part, ajoute des cycles de rétention du souffle, votre propre rythme (par exemple la respiration carrée 4-4-4-4) et 24 animaux marins à collectionner : https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641

L'application est en anglais.

RESPIRATION 4-7-8
• Inspirez 4 secondes, retenez 7, expirez 8. La montre décompte chaque phase.
• L'écran rond devient une petite mer. L'eau monte et descend avec votre souffle, et un petit poisson vous tient compagnie.
• Respirez aussi longtemps que vous voulez. Le bouton retour met en pause : reprendre, enregistrer ou supprimer.

LES YEUX FERMÉS
• Inspiration, pause et expiration ont chacune leur vibration. Les vibrations peuvent être coupées dans les réglages.
• Pendant la séance, l'écran tactile ne fait rien : seuls les boutons fonctionnent. Ebb Calm ne fait aucun son.

ENREGISTRÉ DANS GARMIN CONNECT
• Enregistrez une séance et elle devient une activité de respiration dans Garmin Connect, avec votre fréquence cardiaque.
• Une séance qui continue, ou laissée en pause, s'enregistre d'elle-même après 30 minutes.

GRATUIT ET PRIVÉ
• Gratuit. Pas de compte, pas d'abonnement, pas de code, pas d'app sur le téléphone, pas de publicité.
• Ebb Calm ne collecte rien. Vos réglages restent sur la montre ; seule une activité enregistrée va vers Garmin Connect, selon la politique de confidentialité de Garmin.

ASSISTANCE
Écrivez à thijs@dortus.com (en anglais) avec le modèle de votre montre. Nous visons une réponse sous 5 jours ouvrés.

SÉCURITÉ
Asseyez-vous ou allongez-vous. Ne pratiquez jamais dans l'eau ou près de l'eau, dans le bain, ni en conduisant. Vertiges ou fourmillements ? Arrêtez et respirez normalement. Pas en cas de grossesse, avant 18 ans, ni en cas d'épilepsie, de problèmes cardiaques ou de tension. Ebb Calm n'est pas un dispositif médical.

Tags : respiration, exercices de respiration, relaxation, calme, 4-7-8, 478, breathing
```

Wat is nieuw: niet aanraken.

**Beeldvolgorde Calm** (alle vijf bestaande beelden blijven, geen nieuw beeld maken of uploaden; bestanden in `ontwerp/garmin/winkel-calm/`):
1. `1-breathe-in.png`: "Breathe in. The sea rises."
2. `5-free.png`: "Free. One button."
3. `3-calm-done.png`: "A few calm minutes." Dit eindscherm van Calm zegt al "The full Ebb adds breath hold rounds and 24 sea animals" en is daarmee het beeld dat naar Ebb verwijst (kan-punt 5 van de keurder: geen beeld van Ebb in de lijst van Calm).
4. `2-eyes-closed.png`: "Sit down. Close your eyes."
5. `4-pause.png`: "Pause. The sea waits."

Icoon en prijs (gratis): niet aanraken.

## 3. Gloop's Hat Tower (gratis, id c39ac502-5043-4222-82bf-af42abc2cc51)

**Niets plakken.** Titel, teksten, taalvolgorde (Engels, Duits, Nederlands; Engels staat al eerst, GEZIEN) en beelden blijven zoals ze live staan. Reden: hij staat al op plek 4 bij "stacking game" en 3 bij "one button game" (GEZIEN), en een link naar een ademapp in een spel levert weinig op (oordeel keurder en mij).

## 4. Meten op 23 nov en 1 dec

Zoek-API, meest relevant, eerste 90, alle soorten, plek van Ebb en Calm op: breathing, breath, breath hold, breathwork, breathing exercises, box breathing, breath training, 478, relaxation, calm, en Duits en Nederlands: atem, atemübungen, atem anhalten, breathwork (om de nieuwe titels te zien), ademhaling, ademhalingsoefeningen, adem inhouden, ontspanning, en Frans: respiration, souffle. Daarnaast de downloads van Ebb, Calm en Hat Tower (API), en **de verkopen van Ebb** (uit het overzicht van Garmin, via de hoofdchat; staat bij Thijs), naast de downloads van Calm, om te zien of de link naar de gratis Calm kopers kost. Terugzetten: zakt Ebb op breath hold onder 5, of op atem, atemübungen, ademhaling of adem inhouden meer dan 3 plekken, zet dan de Duitse en Nederlandse titel van Ebb terug naar `Ebb Atemübungen & Atem anhalten` en `Ebb Ademhaling & Adem inhouden`. Nulmeting: de tabel in `winkel-vindbaar-2026-11-20.md` deel 2 (20 nov).
