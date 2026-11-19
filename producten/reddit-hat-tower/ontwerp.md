# Gloop's Hat Tower op Reddit: ontwerp van het dagspel

Bouwer, do 19 nov 2026. Voor Reddit Game of the Day 2026, categorie "Best Ported Daily Game" ($6.000, GEZIEN in de rules deel 8). Deadline di 8 dec 18:00 PST (wo 9 dec 03:00 NL). Bron van de port: Hat Tower op tak `claude/garmin-gloop-11` (b62bbdc1), `producten/garmin-gloop/source/Spel.mc` en `SpelView.mc`. Onderzoek en regels: `platformen/ideeen/snel-geld-2026-11-19/H-hackathons.md` deel 1 en `KEURING.md`.

## In twee zinnen (stap 1 van bouwen-in-stappen)
Een dagspel in een Reddit-post: elke dag één toren die voor iedereen gelijk is, één knop, 30 seconden, met een ranglijst per subreddit, een reeks dagen op rij, een uitslagkaart als reactie en een gezamenlijke toren van de subreddit. Voor redditors die elke dag even iets kleins willen spelen en willen vergelijken in de reacties.

**Af voor fase 1 (toetsbaar):** de speltoetsen zijn groen (12 stuks, `npm test`); een ronde duurt precies 30 s; eerste hoed binnen 2,5 s; een goede speler haalt 15 of meer (dezelfde eisen als op het horloge); de server rekent dezelfde score uit als de browser uit alleen de tikken; het spel draait lokaal op telefoon en desktop zonder fouten in de browser; 3 schermbeelden en een filmpje bekeken.

## De kern blijft (zelfde gevoel als op het horloge)
Overgenomen uit `Spel.mc` met dezelfde getallen: vangzone 700 tot 900, voltreffer 780 tot 850, begin 0,50, elke vangst 6% sneller (max 1,30), missen 15% trager (min 0,40), te vroeg drukken sluit de bek 250 ms, slok 300 ms, wegloop 600 ms, pauze 100 tot 450 ms, ronde 30 s. Missen kost nooit een hoed. Zelfde plaatjes van Mila (kit 454: Gloop rust, hap, slok, blij, de held, de vliegende helm, tien hoeden), dezelfde ankers (toren op de kruin, 0,56 hoed per stap, wiebel van een paar pixels), dezelfde lichtbaan van linksboven naar de bek, dezelfde stilstand van 80 ms op het slikken, "GULP!" met de reeks, "bye!" bij missen, het gele "!" in de vangzone. Gloop, de held en de hoeden zijn eigen IP van Dortus (Mila, kit op main).

## Wat het Reddity en dagelijks maakt
| Wat | Hoe | Waarom (jury) |
|---|---|---|
| **Dagtoren** | Dag 1 is 19 nov 2026 (UTC). Uit het dagnummer volgen het ritme van de helden (pauze per held), welke helden goud zijn en de volgorde van de hoeden. Held 7 is voor iedereen dezelfde. | Daily Content: iedereen speelt dezelfde puzzel, dus vergelijken in de reacties betekent iets. |
| **Dagregel** | Vijf regels die rouleren, elke vijf dagen allemaal een keer: Classic, Rush Hour (kortere pauzes), Heavy Heroes (sneller vallen), Golden Hour (vijf gouden helden), Big Mouth (grotere bek, zelfde kleine voltreffer). | Daily Content: elke dag voelt anders, zonder nieuw werk per dag. |
| **Gouden helden** | Een paar helden per dag gloeien goud en zijn 3 hoeden waard. Het startscherm zegt welke ("#4 and #20"). | Gesprek in de reacties ("wie pakte #20?"), en een klein doel binnen de 30 s. |
| **Eén dagbeurt** | De eerste ronde van de dag telt; daarna oefenen zoveel je wilt (andere, willekeurige toren). Er is ook "Warm up first". | Eerlijk en deelbaar, zoals Wordle; geen eindeloos opnieuw voor de ranglijst. |
| **Ranglijst per dag** | Redis sorted set per subreddit per dag: eerst hoeden, dan beste reeks. Top 10 en je eigen plek. | Reddity: je subreddit tegen elkaar. |
| **Dagen op rij** | Per speler: laatste dag en aantal. Valt terug naar 0 als je een dag overslaat. | Terugkomen. |
| **Gezamenlijke toren** | Alle hoeden van alle dagbeurten van vandaag in deze subreddit tellen op: "r/... stacked 1,204 hats today, together. Your 16 are in it." Staat ook op de post in de feed. | Reddity: de hele subreddit bouwt één toren; dat is de grap van Hat Tower op gemeenschapsschaal. |
| **Uitslagkaart** | Platte tekst met per held een vakje (groen voltreffer, geel vangst, ster goud, zwart gemist), plus hoeden, beste reeks en dagen op rij. Knop "Comment my result" plaatst hem als reactie namens de speler (Devvit `submitComment` met `runAs: 'USER'`), en "Copy". | Reddity en gratis reclame in de draad. |
| **Eerlijke score** | De browser stuurt alleen de tikken (stapnummers van 4 ms). De server speelt het potje na met dezelfde code (`src/shared/spel.ts`). | Polish: geen nepscores op de ranglijst. |
| **Dagpost** | Een taak in `devvit.json` maakt elke dag om 00:00 UTC een post "Gloop's Hat Tower #N: Rush Hour". Moderators kunnen er ook een maken via het menu. | Daily Content zonder handwerk. |

## Hoe het eruitziet (frontend-design)
- **Kleur** (uit de grot van Mila en de kit): grot diep #24110a, grot warm #a85a2a, gloed #d98a45, Gloop-mint #6fe0b0, goud #ffc93c, room #fff6e6, rand #2b1206. Geen crème met terracotta, geen zwart met neon: het is de warme grot van het horloge.
- **Letters:** Lilita One voor koppen, getallen en knoppen (dezelfde letter als de Hats-beelden op Steam, OFL), Fredoka voor lopende tekst (OFL). Beide zitten in het pakket, want een Devvit-app mag niets van buiten laden.
- **Opbouw:** de speelstrook is altijd staand (breedte 454 eenheden zoals de kit, hoogte volgt het scherm), dus op een telefoon mag de toren veel hoger worden dan op het horloge. Op desktop staat de strook in het midden. Teksten staan los op de grot met een donkere rand, zonder kaartjes. De knoppen zijn dik en speelgoedachtig met een harde schaduw die inzakt bij een tik.
- **Het ene moment dat blijft hangen:** aan het eind trekt de camera terug tot je hele toren in beeld is, en dan schuift het uitslagvel omhoog. Dat is ook het beeld voor het filmpje en de Devpost-pagina.
- **Geluid zonder bestanden** (Web Audio): een zakkende "gulp", hoger bij een langere reeks, een tinkel bij goud, een zacht toontje bij missen. Uit te zetten; trilling op Android.

## Drie aanpakken (stap 4)
1. **Phaser-template van Reddit.** Voordeel: kant-en-klare sprites en tweens. Nadeel: een motor van ±1 MB voor een spel van één scherm, en de regels moeten toch los van de motor blijven voor de server. Niet gekozen.
2. **React-template.** Voordeel: menu's zijn makkelijk. Nadeel: het spel zelf is canvas; React voegt niets toe aan de kern en maakt de bundel groter. Niet gekozen.
3. **Bare-template met eigen canvas (gekozen).** De officiële `reddit/devvit-template-bare` (51e9aab, opgehaald zonder login van GitHub), TypeScript en een canvas, zoals `SpelView.mc` ook direct tekent. De regels in één gedeeld bestand voor browser en server. Opslag via een klein `Opslag`-koppelvlak: op Reddit Redis, lokaal een Map. Reden: het kleinst, het dichtst bij de Garmin-code, en de server kan elke ronde naspelen.

## Getoetst tegen de jury
| Punt | Wat we doen | Wat nog zwak is |
|---|---|---|
| Delightful UX | Eén tik, uitleg op het startscherm in één zin, nooit straffen, opverend "GULP!", vonken bij voltreffer, camera die terugtrekt naar je toren, geluid. | Er is nog geen korte uitleg in beeld bij de allereerste held behalve één regel tekst. |
| Polish | Geen fouten in de browser (GEZIEN met Playwright), werkt op 390x780 en 1280x760, eerlijke score, toetsen groen. | Sprites zijn 454 px van het horloge; op een telefoon met 3x scherm iets zacht. Er bestaan renders van 400 px (`ontwerp/garmin/gloop-spel/bron-renders/`) om scherper te maken. |
| Reddity | Ranglijst per subreddit, gezamenlijke toren, uitslag als reactie, dagpost. | De gezamenlijke toren is nu een getal, nog geen beeld. Fase 2: een toren van de subreddit tekenen (bijvoorbeeld elke 100 hoeden één hoed). |
| Daily Content | Dagtoren, dagregel, gouden helden, dagen op rij, elke dag een post. | Vijf regels rouleren; na een paar weken zie je ze terug. Genoeg voor de jury (GOK). |

**"AI slop":** geen gegenereerde plaatjes of teksten; alles is het bestaande, gekeurde werk van Mila, met een eigen figuur en eigen grap (de toren die hoger wordt dan je scherm). Geen standaard-UI: de grot, de letter en de knoppen komen uit het spel. **"Clone":** het is geen bekend spel na; de dagregel, gouden helden en de gezamenlijke toren zijn eigen. Het vakjesraster lijkt op Wordle; dat is bewust, omdat redditors dat al kennen als deelvorm, maar het spel zelf is anders.

## Devvit-regels
- Geen link of verwijzing naar Garmin of Steam in het spel of in de README van de app ("Apps should not link out to other apps, or promote other versions of the app on external platforms", devvit_rules). Dat het een port is, staat alleen in de Devpost-tekst, zoals de wedstrijd vraagt.
- Geen verzoeken naar buiten: letters en plaatjes zitten in `public/`.
- Scores in Redis, niet in de browser (die opslag verdwijnt bij een update).
- Geen taalmodel in de app; nergens een AI-melding (besluit 19 nov 01:30).

## Open vragen, zelf beantwoord
- *Mag je spammen?* Op het horloge vang je alles door elke ±260 ms te tikken (de bek gaat maar 250 ms dicht). Hier ook: je vangt dan veel, maar bijna nooit een voltreffer, dus geen reeks. Zo laten, omdat het horloge zo gekeurd is; wel opnieuw bekijken na het eerste echte spel van een mens.
- *Niet ingelogd?* Je kunt spelen; opslaan en delen vragen om inloggen ("Log in to Reddit to save your tower.").
- *Server niet bereikbaar?* Het spel werkt gewoon als oefening en zegt dat de ranglijst even weg is.
- *Welke tijd geldt voor de dag?* UTC, zoals de taak voor de dagpost om 00:00 UTC.
