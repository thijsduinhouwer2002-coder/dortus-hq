# Keuring R6 scorebord compleet en geluidscontrole, 19 nov 2026, keurder (losse Claude, ingezet door de hoofdchat)
Wat ik keurde: commits 713e878c (geluid_check.py, blokkade in filmpjes-geluid.yml en click-joints-pro-film-release.yml, GELUID.txt in click-joints-render.yml en click-joints-film-plak.yml) en 6316e7e5 (scorebord_bronnen.py, scorebord.py, scorebord.yml), plus organisatie/scorebord.md en scorebord-data.csv van run 44416182819 (commit 00af8c38).
Akkoord: nee (twee kleine moet-punten, verder goed werk)

Opdracht (organisatie/roestronde-2026-11-19.md, R6): scorebord meet elke dag alle openbare cijfers (Blender, JetBrains, Obsidian, Garmin, Gumroad, Kit-abonnees, Discord-leden, YouTube) met GEZIEN; filmpjes-workflows weigeren een filmpje zonder hoorbaar geluid.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Cijfers zonder sleutel kloppen met de bron (curl, 18 nov ±23:05 UTC): Blender Click Joints 240 downloads, versie 0.1.1 (productpagina `<dd>240</dd>`); JetBrains Bison & Flex 6 downloads, approve false = "in keuring"; Obsidian Rollwright 45; YouTube-RSS van UCTspMNCOwnBkGT2LZ7tB2dg 1 filmpje (sgcC965GVps, 56 weergaven). Alles gelijk aan scorebord.md. | feit | hoog | volgende dagrun naast curl leggen |
| A2 | Gumroad, Kit en Discord zitten erin; Gumroad 0 verkopen en Kit 0 abonnees kan ik zonder sleutel niet nameten. De code leest alleen `sales_count`, `sales_usd_cents`, naam, prijs (Gumroad) en aantallen (Kit). | feit (code), cijfer niet nagemeten | midden | Gumroad- en Kit-dashboard in Chrome (hoofdchat) |
| A3 | Discord-leden staan op "?": de invite-code ontbreekt, de widget van de server staat uit (403). R6 meldt dit eerlijk als open. Dit deel van de opdracht is dus nog niet af, maar hangt aan de hoofdchat. | feit | hoog | code invullen in variabele HATS_DISCORD_INVITE, dan run |
| A4 | Laatste runs (API zonder sleutel): scorebord 44416182819 groen; filmpjes-geluid 44415734049 groen met stap "Geluidscontrole" success vóór "In de release zetten"; click-joints-pro-film-release 44415734016 rood op de stap Geluidscontrole, stap "Release maken of bijwerken" skipped. Log (organisatie/actions-logs/click-joints-pro-film-release-44415734016.txt): "FOUT: click-joints-pro-demo.mp4: geen geluidsspoor". De blokkade werkt echt. | feit | hoog | |
| A5 | Zelf getest met ffmpeg: sinustoon GOED (gem -21,1 / piek -12,0 dB), stil spoor FOUT (-91 dB), geen spoor FOUT, 2 s geluid onder 10 s beeld FOUT, toon op -40 dB FOUT (-61 dB), zachte ruis FOUT (-66 dB), kapot bestand FOUT, lege glob FOUT. Echte release-bestanden: beide -geluid.mp4 GOED (-19 en -18 dB, piek -2 dB), het origineel FOUT (geen spoor). Faalt dicht: ontbreekt ffmpeg, dan crasht het met exit 1. | feit | hoog | |
| A6 | Grenzen zinnig: -50 dB gemiddeld ligt ruim onder onze filmpjes (-18 tot -21) en boven ruis en stilte (-60 tot -91); -30 dB piek vangt een te zacht spoor. Gat: een spoor van volle lengte met maar 1,5 s geluid en 8,5 s stilte slaagt (gem -29,3, piek -17,7 dB, zelf gemeten). Stille gaten vangt alleen toets.py van filmpjes-geluid. | feit | hoog | |
| A7 | Geen `continue-on-error` of `if: always()` vóór uploaden in filmpjes-geluid en pro-film-release. In click-joints-render staat "Openbaar zetten (tak schermen)" op `if: always()`: faalt het ophalen van geluid_check.py met curl, dan gaat de keurfilm toch naar de tak schermen zonder GELUID.txt. Dat is een keurfilm, geen post, dus klein. | feit | hoog | |
| A8 | **Het eigenlijke inplannen is niet gedekt.** Geen enkele workflow plaatst of plant in: dat doet de hoofdchat in Metricool. De stille bronfilmpjes van filmpjes-week-1 staan in dezelfde release naast de -geluid.mp4 (gezien in de release-lijst) en filmpjes-week-1 heeft geen controle (bewust). R6 vroeg Chris "draai het script even zelf voordat de hoofdchat iets inplant", maar Chris plant niet in; in planning.md, de rol van de hoofdchat of berichten/hoofdchat.md staat het niet. Het ongeluk van 17 nov (stil live) ging precies via die stap. | feit | hoog | regel "geluid_check.py op het bestand vóór inplannen" zichtbaar waar de hoofdchat leest |
| A9 | De Pro-demofilm-release blijft rood tot er geluid onder zit. Voor een winkelpagina (Superhive) is een stille demofilm gewoon; de blokkade maakt deze workflow vast rood en vult de rood/groen-lijst van R1 en actions-logs. Keuze van R6, wel bewust en gemeld. | vermoeden | midden | hoofdchat beslist: geluid eronder, of deze release buiten de regel |
| A10 | YouTube-RSS toont 1 filmpje terwijl planning.md er voor 17 en 18 nov twee op YouTube noemt. Ligt niet aan R6 (de RSS zelf geeft er 1), wel nagaan bij de hoofdchat. | vermoeden | laag | YouTube Studio |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Privacy in scorebord.md en de csv: alleen productnaam, aantallen, omzet per product, filmpje-id en titel (openbaar), Kit-tagnamen en Discord-servernaam. Geen namen, mailadressen of bedragen per koper: de Gumroad-productlijst en Kit-tellers geven geen kopers terug; de Kit-terugval telt alleen `len()`. De inviter uit het Discord-antwoord wordt niet opgeslagen. | feit | hoog | regel 2 |
| B2 | Sleutels: `_get` print nooit het adres (Gumroad-terugval `?access_token=` en Kit v3 `api_secret` staan in het adres), fouten worden alleen als code of naam van de fout bewaard; main slaat alleen `type(e).__name__` op. GitHub maskeert secrets in de logs, en actions-log haalt sleutels er nog eens uit. Ik vond geen pad waarlangs een sleutel of het webhook-adres in de repo of het log komt. | feit (code regel voor regel gelezen) | hoog | regel 2 |
| B3 | **DISCORD_WEBHOOK in de scorestap is overbodig en verbreedt wat die stap kan.** Hij dient alleen om de server-id op te halen (een vast, niet geheim getal dat R6 al kent: "webhook gaf de server"), en daarna de widget, die uit staat. Met het webhook-adres kan iedereen die code in die stap laat draaien posten in de Hats-Discord. De stap draait na `git reset --hard origin/main` de nieuwste scorebord.py van main, dus elke push van elke agent draait met deze sleutel. toegang.md: "Een sleutel mag maar één ding kunnen." Bovendien leest een GET op de webhook het token terug in het geheugen. Niet gelekt, wel onnodig. | feit | hoog | toegang.md, regel 2 |
| B4 | check.py vangt geen Discord-webhookadres (`discord.com/api/webhooks/<id>/<token>`) en geen Gumroad- of Kit-sleutel. Nu niet nodig (niets wordt geprint), wel een vangnet. | feit | hoog | regel 2 |
| B5 | `python3 organisatie/controle/check.py` op 713e878c, 6316e7e5 en t/m 00af8c38: "Controle openbare repo: OK". | feit | hoog | regel 2 |
| B6 | Omzet in USD per product komt openbaar in de repo. Geen regel verbiedt het (doelen.md noemt ook bedragen), maar het is een nieuwe keuze. Ook namen van niet-gepubliceerde Gumroad-producten zouden openbaar komen. | vermoeden | laag | regel 2, besluit hoofdchat |
| B7 | Label GEZIEN staat ook in de bronkolom van regels zonder meting ("?" bij Discord en Superhive, of "geen leessleutel"). Een "?" is niet gezien. | feit | hoog | regel 5 |
| B8 | Gumroad-naam is nu "Click Joints Pro for Blender" (was "Click Joints Pro" in de csv): de geschiedenis breekt bij elke titelwijziging. Garmin heeft daarvoor een vaste naam per id; Gumroad niet. Tagnamen en productnamen met `|` breken de tabel. | feit | hoog | netheid |
| B9 | Bestanden onder 400 regels (scorebord.py 327, scorebord_bronnen.py 212, geluid_check.py 100); geen tests aangepast; geen steam-workflow aangeraakt; Nederlands zonder gedachtestreepjes. | feit | hoog | bouwen.md |

## Moet (blokkeert akkoord)
1. **B3:** haal `DISCORD_WEBHOOK` uit de stap van scorebord.yml en de webhook-terugval uit scorebord_bronnen.py. Discord-leden alleen via de openbare invite-code (variabele HATS_DISCORD_INVITE). Klein werk.
2. **A8:** zet de controle op de plek waar echt ingepland wordt: een bericht onderaan `berichten/hoofdchat.md` (en een verzoek aan Chris voor één regel in `commercie/filmpjes/planning.md`) dat elk bestand vóór inplannen in Metricool door `geluid_check.py` gaat, en dat alleen `-geluid.mp4` uit release filmpjes-week-1 naar buiten mag. Of laat filmpjes-week-1 een GELUID.txt met "NIET PLAATSEN" bij de stille bronfilmpjes zetten.

## Kan (mag later)
- A6: stille delen meten (bijv. ffmpeg silencedetect: meer dan 50% stil is FOUT), zodat "1 tik in stilte" niet slaagt.
- A7: in click-joints-render `if: always()` laten staan maar GELUID.txt "niet nagekeken" schrijven als het ophalen mislukt; of het script uit de checkout nemen in plaats van curl.
- A9: hoofdchat beslist over de stille demofilm voor Superhive (geluid eronder, of buiten de regel), zodat die workflow niet vast rood staat.
- B4: patroon voor Discord-webhookadressen in check.py.
- B6: hoofdchat zegt of omzet per product openbaar mag; alleen gepubliceerde Gumroad-producten tonen.
- B7: bronkolom "niet gemeten" als de waarde leeg is.
- B8: vaste namen per Gumroad-product-id; `|` in namen vervangen.
- A3: Discord-code invullen (hoofdchat).
