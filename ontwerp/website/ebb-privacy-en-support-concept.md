# Ebb for Garmin: privacy en support, concept voor dortus.com/ebb/ (hoofdchat, 13 nov 2026)

Status: CONCEPT. Er staat niets online. Thijs ziet dit eerst en zegt ja; daarna pas plaatsen (besluit 12 nov 23:30).

Waarom: de keuringsregels van Garmin vragen "your own privacy policy or other notice" en zeggen dat je niet op Garmins privacybeleid mag leunen (bron en citaat in `ontwerp/website/voorstel-ombouw-2026-11-13.md`, regel 89 en 90). In de winkeltekst van Ebb staat al een privacyzin. Een eigen pagina is de veilige aanvulling, en het uploadformulier vraagt er mogelijk om (dat formulier hebben we na stap 1 nog niet gezien).

Nalopen voor plaatsen: elke zin hieronder moet kloppen met de versie die de winkel in gaat. Gijs controleert punt voor punt tegen de code (rechten in het manifest: Fit, FitContributor, Sensor; geen internet).

## Pagina 1: dortus.com/ebb/privacy.html

**Ebb for Garmin: Privacy**

Last updated: 13 November 2026

Ebb is a breathing app for Garmin watches, made by Dortus.

**What Ebb collects: nothing.**
Ebb has no account, no analytics, no ads and no internet connection of its own. We, Dortus, never receive any data from your watch.

**What stays on your watch**
Your sessions, your sea animals and your settings are stored on your watch only. Removing the app removes them.

**Heart rate**
During a session Ebb switches on your watch's heart rate sensor. Ebb shows your heart rate on the hold screen, and your watch records it in the saved activity. Ebb keeps no copy of its own. It is not sent to us.

**Saved activities**
A finished session saves itself as a breathing activity on your watch. Your watch then syncs it to Garmin Connect like any other activity. That sync is done by Garmin and falls under Garmin's own privacy policy. Do not want a session saved? Press back to pause and choose Discard.

**Purchases**
Payment is handled by Garmin through the Connect IQ Store. We do not see your payment details.

**Children**
Ebb is not meant for anyone under 18.

**Your rights and contact**
Because we hold no personal data about you, there is nothing for us to show, correct or delete. If you have a question about privacy, mail thijs@dortus.com.

**Changes**
If this notice changes, the new version appears on this page with a new date.

## Pagina 2: dortus.com/ebb/support.html

**Ebb for Garmin: Support**

Mail thijs@dortus.com and tell us your watch model and what happened. We aim to reply within 5 working days.

**Refunds**
Refunds follow the Garmin Connect IQ Store policy: Garmin gives you a 48-hour return window after you buy.

**Safety**
Use Ebb on land only, sitting or lying down. Never in or near water, never while driving. Stop if you feel dizzy or unwell. Ebb is not a medical device and gives no medical advice. A hold stops by itself after 5 minutes.

**Which watches**
Ebb runs on 28 round Garmin watches. The list is on the store page.

## Open punten
- "Not meant for anyone under 18": staat zo in de winkeltekst; Gijs bevestigt.
- Het mailadres is het zakelijke supportadres van Dortus dat ook in de winkeltekst staat.
- Vraagt het uploadformulier om een privacy-URL, dan is dat dortus.com/ebb/privacy.html.
- Plaatsen kan los van de ombouw van de site: een nieuwe map /ebb/ raakt geen bestaande pagina.

## NAGELOPEN tegen e40269e1 (Gijs, 12 nov 23:00 UTC, run 75): klopt, op twee zinnen na

Punt voor punt tegen de code van de bouwtak op e40269e1:
- Rechten in het manifest: Fit, FitContributor, Sensor. Geen Communications, geen Positioning, geen UserProfile; in de code geen webverzoek en geen geluid. "No internet connection of its own" klopt.
- Opslag: sessies, dieren en instellingen staan in de opslag van de app op het horloge. Klopt.
- Onder de 18: staat zo op het veiligheidsscherm in de app ("Not if: pregnant, under 18, epilepsy, heart or blood pressure problems") en in de winkeltekst. Klopt.
- 5 minuten: `MAX_INHOUD_MS = 300000`. Klopt.
- 28 horloges: 28 producten in het manifest, alle 28 compileren (run 43315538179), allemaal rond. Klopt.
- 48 uur retour en 5 werkdagen: gelijk aan de winkeltekst. Klopt.

Twee zinnen kloppen NIET en moeten anders voor de pagina online gaat:
1. **Heart rate.** Ebb toont de hartslag niet op het scherm en leest hem zelf niet uit. De app zet alleen de hartslagsensor aan voor de opname (`Opname.mc` regel 50 en 51), zodat het horloge de hartslag in de activiteit zet. Nieuwe tekst: "During a session Ebb switches on your watch's heart rate sensor, so that the watch records your heart rate in the activity. Ebb does not show it and keeps no copy of it. It is not sent to us."
2. **Saved activities.** "If you choose to save a session" klopt niet: een afgeronde sessie slaat zichzelf op, en Calm en een sessie in pauze doen dat na 30 minuten ook. Kiezen kan alleen in het pauzemenu (Resume, Save, Discard). Nieuwe tekst: "A finished session saves itself as a breathing activity on your watch. Your watch then syncs it to Garmin Connect like any other activity. That sync is done by Garmin and falls under Garmin's own privacy policy. Do not want a session saved? Press back to pause and choose Discard." Pas ook bij Heart rate "if you save the session" niet meer toe (zie de nieuwe tekst bij 1).

Dezelfde fout stond in de winkeltekst ("Only an activity you choose to save goes to Garmin Connect"). In de plakbestanden voor Thijs is dat nu "Only a saved activity goes to Garmin Connect" (ook Duits en Nederlands), zie `platformen/garmin/upload/`.


## Eindversie (hoofdchat, 13 nov 02:25 NL)

De twee zinnen hierboven zijn aangepast. Bij "Heart rate" volg ik Gijs niet helemaal: de app leest de hartslag wel en toont hem op het inhoudscherm (`Opname.hartslag()` leest `currentHeartRate`, `SessieScherm.mc` regel 152 en `WereldSessie.mc` regel 77 tot 81 zetten "NN bpm" op het scherm; in de simulator komt er geen hartslag, daarom zie je daar alleen de nagebootste 61 in de testbeelden). De pagina zegt dus: sensor aan, hartslag op het inhoudscherm, het horloge legt hem vast in de activiteit, geen eigen kopie, niets naar ons. "Saved activities" is volgens Gijs' tekst.
Status blijft CONCEPT tot Thijs ja zegt.
