# Ebb: lijst voor versie 1.1

Besluit Thijs 12 nov 22:20: wat geen crash, veiligheid of onwaarheid in de winkel is, komt hier en niet meer in 1.0.

- **Orka groter en met meer wit** (flankvlek, witte buik boven water bij inademen). Wens van drie keurders in run 73. Hij is nu te zien (meting run 74: 68 tot 95), maar klein en bij inademen in de nacht geen duidelijke orka. Wijziging aan de tekening, dus eerst Mila.
- **Maanvis bij dag op AMOLED:** het lila lijf (AAAAFF) lijkt op de lila lucht erachter bij inademen (meting run 74: 43 op de fenix 8). Hij heeft een witte rand en valt niet weg. Kleinste stap: een eigen luchtband, zoals de dolfijn en het zeepaardje.
- **Narwal bij dag:** de witte buik valt samen met het lichte zand (FR255) en het schuim. De zwarte omtrek houdt hem leesbaar.
- **Meetscript `meet_dieren_beeld.py`:** de achtergrond uit een beeld zonder dier halen in plaats van uit de rand van het venster (nu meet hij te laag bij golfrand, schuim en zand). Ook de venu 3s en uitademen meenemen.
- **Bouwstraat:** `plaatjes-openbaar` schrijft voor elke proeftak naar dezelfde map op de tak `schermen`. Bij vijf proeftakken tegelijk verloor één run (43315475655) na vijf pogingen, en de job bleef toch groen. Per tak een eigen map, en rood worden als het schrijven niet lukt.
- Uit de taken van run 73: aparte toets voor het eindscherm; `_proefTimer` opruimen; sea complete en "Sit or lie down" op de oude achtergrond.
- **Groepsfoto sea complete op MIP-horloges groeit traag aan** (run 76, kandidaat e40269e1): op de fenix 7 stonden 12 seconden na het openen 16 van de 24 dieren op de foto, terwijl de tekst al "24 of 24 friends" zegt. Zo gebouwd vanwege de watchdog (één dier per beurt). Voor 1.1: meten hoe lang het duurt, en de tekst pas tonen als de foto af is of de foto sneller vullen waar het horloge het aankan.
- **Schermen zonder zee** (gezien run 76): "Sit or lie down" voor de start van Rounds en Calm, de drie veiligheidsschermen, Today en 8 weeks hebben een zwarte of effen achtergrond met alleen een golf onderaan. De rest van de app heeft de onderwaterachtergrond.
- **Scènes voor de bladen:** "fish stays with you" (eindscherm na sessie 1) en "5:00 auto" zitten niet in de volle plaatjesronde. Twee scènes erbij in `Scenes.mc`, zodat ze op elk horloge gezien worden.
- **Bouwstraat, tijdgrens plaatjesjob** (run 77): in run 43327097299 duurde de checkout bij één horloge (epix 2 pro) 20 minuten en haalde de job de grens van 75 minuten niet, waardoor de hele run op `cancelled` kwam. Een grens per stap in plaats van per job, of de checkout laten herhalen als hij na een minuut niet klaar is.
- **Hartslag op het inhoudscherm** (run 78): de app toont tijdens het inhouden de live hartslag, maar de winkeltekst noemt dat niet als functie. Eén regel erbij in de winkeltekst van 1.1. En gelijktrekken wat er staat als er geen meting is: het gewone scherm toont "--" (`Teken.hartRonde`), het wereldscherm laat de hartslag dan weg (`WereldSessie.mc` r.81).

## Resten uit de vervallen taken van 12 nov (nagelopen 13 nov, run 85)

De 33 regels die in run 76 op "vervallen" gingen zijn nu inhoudelijk gelezen. Wat hieronder staat stond nog nergens op deze lijst. Niets ervan is een crash, een veiligheidspunt of een onwaarheid in de winkel. Bij elk punt staat of het is nagekeken in de kandidaat; "niet nagekeken" betekent dat eerst in de code van e40269e1 gekeken moet worden of het nog geldt.

App:
- **Dode code weghalen** (nagekeken in e40269e1, run 85): echt dood is de tak "first friend" in `Start.mc` (r.128 tot 134; het commentaar zegt het zelf, `sessieDier` geeft altijd een dier). NIET zomaar dood: de oude `EbbWereld` (`Wereld.mc`, `WereldData.mc`) wordt nog aangeroepen vanuit `SessieScherm.mc` (r.46, 65, 93, 108, 144, 145), `EbbView.mc` r.173 en `Scenes.mc` r.280, en `KrabV2Thuis.laag` vanuit `KrabV2.mc` r.185. Eerst uitzoeken welke van die aanroepen in de gewone app nog bereikt worden (welk dier heeft nog een oude wereld), dan pas weghalen. Weghalen verschuift scènenummers en de lijst NAMEN in de workflow: in één commit, met een volle ronde.
- **Vanzelf gestopte inhouding in het FIT-bestand** (vraag e uit status 12 nov 17:25, nooit beantwoord): de inhouding die na 5 minuten vanzelf stopt staat in de activiteit als lap van 300 s en in "Hold times". Mijn keuze was: laten staan, de activiteit is een eerlijk verslag. Wil de hoofdchat het anders, dan is het één regel in `EbbView.bewaak`.
- **Vraag f uit dezelfde status** (telt een sessie met een vanzelf gestopte inhouding mee voor de reeks en de dieren): ook nooit beantwoord, nu zoals gebouwd. Bij 1.1 één keer voorleggen.
- **Gepauzeerde opname als de app gestopt wordt met het pauzemenu open** (nagekeken in e40269e1, run 85): in de code is het gedekt. `Opname.loopt()` is `_sessie != null` en dat blijft waar tijdens een pauze (`pauzeer` stopt de opname maar houdt hem vast); `EbbApp.onStop` roept dan `weggooien` aan, voor Rounds en voor Calm, en `weggooien` doet `discard()`. Wat nog ontbreekt is alleen het bewijs in de simulator (de regel `OPNAME weggegooid` in het log bij stoppen vanuit het pauzemenu, en geen FIT-bestand). Eén proef in de toetsbouw.
- **Bovenste knop op Venu 4 en vivoactive 6** (nagekeken in e40269e1, run 85): gebouwd. De teksten "top button to breathe", "Top button: breathe again." en "Top button: swims with you" staan in eigen strings voor venu2, venu3, venu3s, venu441mm, venu445mm, vivoactive5 en vivoactive6. Of het op elk van die horloges ook echt de bovenste knop is die de app bedient, is alleen op een echt horloge te zien: hoort bij het punt "nooit op een echt horloge gezien" hieronder.
- **Kopteksten in de code** (KAN 4 van de hoofdchat, 12 nov 13:20; nagekeken in e40269e1, run 85): de kop van `KrabV2.mc` is bijgewerkt en klopt ("zit sinds die dag in de gewone app"). `REGELS.md` niet nagelezen. Alleen commentaar.
- **Thuiswater en clownvis delen wereld 2** (`KrabV2View`, scène 75 en 76): het thuiswater een eigen nummer geven voordat er een wereld bijkomt. Hoort bij de 22 getekende werelden van 1.1.
- **Gele koppen ("hold", "Ebb", "3 rounds done") op de fenix 8 bij dag:** in run 54 gemeten op 4,4 tegen een norm van 4,5. De schermen zijn daarna vaak veranderd. Opnieuw meten, niet nagekeken.

Winkel:
- **Hero image van 1440 x 720 px** (staat in Garmins merkregels, gevonden in run 71): niet gemaakt, in `ontwerp/garmin/winkel-echt/` staan alleen poster, vijf kaarten en het icoon. Het formulier vroeg er in onze voorbereiding niet om. Vraagt Garmin er toch om: uit de echte schermen maken, met Mila.
- **Versienummer:** nog steeds een gok dat je het bij het uploaden invult en dat het niet in het manifest staat (Garmins documentatie is met curl niet te lezen). Thijs ziet het in het formulier; daarna hier opschrijven hoe het zit.
- **Mila de nachtregel v1.4 laten zien** (koele dieren houden bij nacht hun kleur): is gebouwd zonder dat zij hem zag.

Bouwstraat:
- **Volle ronde korter:** de snelle proef van de hulp-Claude (`platformen/garmin/snelle-proef.md`, tak `claude/garmin-snel-proef`: toetsen in 6,5 minuut, scènes in stroken) is nooit overgenomen. Een volle ronde duurt nu ruim een uur.
- **Contrast van tekst als stap in de plaatjesrun:** `bron/contrast_tekst.py` staat alleen op tak `gijs/run52-klaar`, en Mila's toets op de pixels van het echte beeld (`ontwerp/garmin/bron/toets_veilige_zone_v32.py`) draait niet mee.
- **Een push met alleen tekst start ook de volle ronde** en houdt de rij ±40 minuten bezet: de workflow alleen laten starten als er code verandert.
- **Takken opruimen** (allemaal van Gijs, pas na de keuring van Garmin, en eerst nalopen dat alles wat telt op de bouwtak staat): `claude/garmin-2026-11-12-proef49` tot `proef74e` (31 takken), `claude/garmin-2026-11-12-vol65`, `gijs/run49-klaar`, en `gijs/run52-klaar` pas als het contrastscript op de bouwtak staat. De takken `claude/garmin-snel-proef`, `claude/garmin-thuis-proef-bas` en `claude/garmin-werelden-proef-wout` zijn van anderen: niet weghalen, vragen via de hoofdchat.

## Resten uit de oudere open taken van 10 tot 12 nov (nagelopen 13 nov, run 85)

- **Nooit op een echt horloge gezien.** Alles is bewezen in de simulator. Wat de simulator niet kan laten zien en dus open staat: of de trilpatronen goed voelen, hoe snel de schermen echt tekenen (de terugval op de FR255 is gemeten in de simulator), batterijverbruik, of het plaatje van sea complete op een echt horloge lukt, en of na een weggegooide opname de volgende opname een lege lap van 0 s krijgt (gezien in de simulator op 10 nov, daar toegeschreven aan de simulator). Zodra er een koper of tester met een horloge is: deze vijf als eerste vragen. Heeft Thijs of iemand in zijn omgeving een Garmin, dan is dit tien minuten werk en veel waard.
- **Beeldgeheugen op FR165 en Venu 3S** (graphics pool, open sinds keuring bouw 7): beide horloges zitten in de volle ronde en zijn groen, maar het is nooit apart gemeten. Niet nagekeken.
- **Toetsen:** de opslag van de app wordt in de toetsronde niet per horloge gewist (het eerste veiligheidsblad is daardoor alleen op de fenix 7 als eerste start getest), en de startcheck is op aanraakhorloges niet met een tik getest. Niet nagekeken of dat later is rechtgezet.
- **Venu X1** (448 x 486, niet rond): bewust niet in versie 1. Ebb tekent rond in de bovenste 448 px; eerst verticaal centreren. Kandidaat voor 1.1 als er vraag naar is.
- **Vervallen, ter info:** het oude voorstel "Ebb 1.0.1" van Mila (naam van het patroon boven het water bij laag water, `RustigView.mc`) ging over het oude Calm-scherm. Dat scherm is vervangen; niet meer nodig tenzij Mila het opnieuw vraagt.
- **Calm in de volle Ebb: de zee staat stil (gevonden run 90, 13 nov).** Bij Calm 4-7-8 en My pattern tekent Ebb 1.0.0 één plaatje voor in, vast en uit. In Ebb Calm is dat hersteld op de tak `claude/ebb-calm` (81a7637: bij uitademen het lagere plaatje). Voor Ebb 1.1 dezelfde drie regels overnemen.

