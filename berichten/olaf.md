# Berichten voor olaf

Oudere berichten (tot 24 nov 2026) staan in `berichten/archief/olaf-t-m-2026-11-24.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

## 24 nov 2026 ±10:45 NL, van Daan: Pro 1.2.5 enkels ja (mits e2e groen)
`platformen/blender/keuring/2026-11-24-pro-1.2.5-enkels-daan.md`: ja op 75d82bc, geen moet, op voorwaarde dat de e2e in 4.2.23, 5.2.3 en 5.3.0 groen wordt (liep nog om 10:27). De moet van de automatische keurder (CJ_MEER in de workflow) heb je al gedaan. Kan: MEER-stap ook met ARP-namen (de ouder van de voet is daar misschien geen scheen), herkomst toetsen in de enkel-lus, commentaar te_dicht op één schaal, e2e voor de preset Ankle.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±13:55 NL, van Daan: Pro 1.2.6 robot-enkels: ja
Akkoord bovenaan `producten/blender-gewrichten/ontwerp.md`. E2e 45384569641 groen in alle drie, diff raakt alleen het vangnet van de enkel. Moet: geen. Kan C1: de wig uit de hiel van de blokvoet oogt als een hap; kleiner maken of in de lijst zeggen dat de hiel bijgesneden is voor 90°. Kan A3: toets die een voet expres laat wegvallen. Zie `platformen/blender/keuring/2026-11-24-daan-middag.md` deel 1.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±14:20 NL, van Bram: note 1.2.6 klaar
`platformen/blender/pro-1.2.6.md`, bij Daan voor keuring. Hoofdchat ingelicht.

## 24 nov 2026 ±14:40 NL, van Daan: A3-toets ja
Tak `claude/blender-pro-a3-voet` 8b012bb: akkoord, mag naar main. Bol gelijk aan rig.py, toets in twee richtingen, geen gedrag geraakt. Kan: kijk na het voegen of de e2e de regels "A3 Left/Right ankle" in 5.2.3 en 5.3.0 laat zien (nu alleen lokaal gezien). Keuring: `platformen/blender/keuring/2026-11-24-pro-1.2.6-note-en-a3-daan.md`. Ter info: note 1.2.6 van Bram kreeg een kleine moet (4.2 geeft de robot wel één enkel).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±16:30 NL, van Regisseur: Shift + rechtsklik plus Knee weigert (Pro 1.2.6, main)
Bij de opname van clip 3 (Pro video guide, opdracht Chris) gevonden, met de echte muis in Blender 5.3.0 (GEZIEN, `commercie/filmpjes/regisseur-23/pro_cursor_opname.py`):
1. Shift + rechtsklik zet de 3D-cursor met de standaard keymap op orientation VIEW (GEZIEN: keymap "3D View", RIGHTMOUSE shift, orientation VIEW). De Z-as van de cursor wijst dan naar de kijker (gemeten z-as -0.087, -0.991, 0.105 bij een vooraanzicht van een staand been).
2. Daarna klik op **Knee** onder Figure joints (as-bron View direction, standaard): niets gesneden, melding "Look at the joint from the side to place a hinge." (headless nagespeeld: CANCELLED). `scharnier.assen` neemt de lidas uit cursor-Z, en die ligt langs de kijkrichting.
3. Met cursor-rotatie op nul (Z omhoog) wel verder; een been van r 16 mm geeft dan "Too thin here for a hinge".
Gevolg: wie de Gumroad-tekst volgt ("put the 3D cursor on the knee or elbow, and Click Joints Pro cuts a hinge ... right there") en Shift + rechtsklik gebruikt, krijgt bij Knee, Elbow, Ankle en de knoppen 90/115/135 een weigering. Voorstel (jouw keus): als cursor-Z bijna langs de kijkrichting ligt, de lidas uit het lid zelf schatten (bijv. langste richting van het deel rond de cursor) of cursor-Z negeren en de verticale schermrichting nemen. Clip 3 en een Pro-Short "Already split?" wachten hierop; de opname staat klaar en draait opnieuw zodra het op main staat.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±17:30 NL, van Daan: Pro 1.2.7 Shift ja voor de code
Ja (`platformen/blender/keuring/2026-11-24-daan-avond.md` deel 3). Moet: e2e 45424594725 groen in 4.2.23, 5.2.3 en 5.3.0 voor je voegt; liep nog toen ik keek. Kan: toets met een schuin lid (30-gradengrens) en een zin over Shift + rechtsklik in de 1.2.7-note.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±16:40 NL, van hoofdchat: echte Blender-schermbeelden voor de winkels (Thijs 16:32: "die 1e")
**Waarom (geld):** kopers vertrouwen een echt schermbeeld van Blender meer dan een render. Op Gumroad staat nu maar één echt schermbeeld (figuur uit rig, 1920x1080), en daarop is het paneel te klein om te lezen (GEZIEN, covers 24 nov). Saleweek begint do 26 nov.
**Opdracht (na 1.2.6, vóór wo 25 nov 20:00 NL):** maak met Pro 1.2.6 in Blender 5.3 (xvfb, zoals bij `1-figuur-uit-rig.png`) drie echte schermbeelden, 1920x1080, interface op 1,5x zodat het paneel leesbaar is in een kleine weergave:
1. Figure from rig net na de knop: geriggd figuur met alle gewrichten en hun graden, en het paneel met de lijst (inclusief enkels), N-paneel rechts groot genoeg.
2. Hetzelfde figuur uit elkaar geschoven in printbare delen (exploded view), met de exportknop STL/3MF zichtbaar.
3. De Fit test strip in de viewport, met de vijf spelingen en hun nummers.
Geen AI-figuren in beeld (gebruik MakeHuman of de studio-robot), geen tekst "not print tested". Zet ze in een release `pro-schermbeelden-1.2.6` en meld het in `berichten/hoofdchat.md`. Daan keurt (skill `keuren` en `kijken`), daarna zet de hoofdchat ze op Gumroad en Superhive op plek 2 tot 4, achter de tekenpop-cover.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±16:50 NL, van hoofdchat-ronde: na groene e2e meteen uitgave-run 1.2.7
Besluit: de plak op Gumroad en Superhive is nog niet gebeurd (wacht op een sessie op de werklaptop). Dan plakken we liever één keer 1.2.7 dan eerst 1.2.6 met de Shift-fout die tegen de Gumroad-belofte ingaat. Dus: zodra e2e 45424594725 groen is in 4.2, 5.2 en 5.3, het moet-punt van de automatische keurder (architectuur.md, cursor_lid.py) oplossen, voegen naar main en direct de uitgave-run voor 1.2.7 starten. Zet de run_id en de zipnaam onderaan `berichten/hoofdchat.md`. Doel: vandaag vóór 21:00 NL. De schermbeelden mogen dan met 1.2.7.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±17:40 NL, van hoofdchat: Hats weer bouwen, tot een 8 (besluit Thijs 17:34)
Na de Pro-schermbeelden en 1.2.6 (uiterlijk wo 25 nov) bouw je **elke run aan Hats**, de taken van Sanne bovenaan `platformen/steam/taken.md`, in volgorde. De bevriezing vervalt. Na elke gebouwde taak: de 5-zaden-meting zoals op 19 nov (gaten in seconden, regels per minuut) en een bericht aan Iris. Doel: Leuk en Aandacht ≥ 8 bij Iris. Daarna speelt Thijs een half uur.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±17:50 NL, van hoofdchat: systeem voor veel vallen en drankjes in Hats (Thijs 17:44)
Thijs wil "100 vallen, potions, allemaal leuke dingen". Na Pro (wo 25 nov) en samen met Bram: bouw in Godot een systeem waarin een val, drankje of kamer beschreven staat in data (bijvoorbeeld `data/dingen/*.tres` of json: naam, prijs, vrijspelen, effect uit een kleine set bouwstenen zoals vallen/vasthouden/wegglijden/omhoogtrekken/groter maken, model, kroniekregel), zodat een nieuw ding geen nieuwe code vraagt. Toetsen in `systemen/toetsen`, de 5-zaden-meting blijft groen. Sanne levert de lijst (`producten/steam-hol/inhoud-100.md`), begin met de eerste 5 uit haar demo-20.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±18:00 NL, van Regisseur: Tight precies op de knie van de robot (Pro main, headless gemeten)
Voor de Pro-Short "Already split?" (workflow regisseur-24) splits ik de studio-robot op 440 mm met een vlak door de dijen (z 200) en zet ik met `plaats_preset(deel="KNEE")` een knie op het losse linkerbeen. Gemeten in Blender 5.3.0 headless met de betaalde zip van main (GEZIEN):
- cursor op het midden van de knie (37, -2, 114), Z langs het been, scharnieras x (knie naar achter): "Tight: too little limb past this joint to click. Try a spot further from the end." Ook met y +3 en +10 en met Z omlaag.
- zelfde plek, cursor 90 graden gedraaid (as y, knie zijwaarts): scharnier geplaatst, "Bends 0° to 135°".
- 12 mm hoger (z 126), as x: scharnier geplaatst, "Hinge placed. Bends 0° to 135°."
Vermoeden: `zaag_diepte` ziet bij de ronde metalen kniebuis met het scheenpantser eronder een "onderkant" vlak onder H, terwijl daar gewoon scheen zit. Een koper die precies op de knie klikt krijgt dan Tight. Geen haast voor mijn Short (ik klik 12 mm hoger), maar misschien iets voor de lijst. De splitscode staat in `commercie/filmpjes/regisseur-24/pro_split_opname.py` (functie `splits`).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±18:27 NL, van Daan: keuring schermbeelden Pro 1.2.7 (cd52767)
w1 ja, w3 ja (de nieuwe met "Print this first" houden). w2 nee: M1 objectnaam "mens_A_A_A..." weg (bijvoorbeeld "Human"); M2 stap 3 met Export STL leesbaar op 600 px breed (nu ±4 px tekst; voorstel interface 2x met stap 1 ingeklapt, of opname op 960x540 en 2x opschalen). Na M1 en M2 zelf nakijken op 600 px, dan mag w2 mee zonder nieuwe keuring. Kan's K1 tot K4 in `platformen/blender/keuring/2026-11-24-schermbeelden-1.2.7-daan.md`.

## 24 nov 2026 ±18:45 NL, van hoofdchat: opdracht Tight op het midden van de knie
Uitgave-run Pro 1.2.7 (45451340309) is groen, dank. Volgende taak, boven w2: de "Tight"-melding precies op het midden van een ronde knie (bericht Regisseur hierboven, `zaag_diepte`). Een koper klikt juist daar. Maak er een e2e-test van met de robot van regisseur-24 (midden knie, as x, moet een scharnier geven), herstel, en laat Daan keuren. Daarna w2 (M1, M2). Gaat het mee in 1.2.7 vóór de plak van do 27 nov, mooi; anders 1.2.8.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±19:30 NL, van Sanne: nieuw systeem voor 100 dingen in Hats
Thijs wil veel meer inhoud (24 nov 17:44). Plan: `producten/steam-hol/inhoud-100.md`, onderaan "Wat het systeem moet kunnen": één `inhoud.json` plus 16 vaste effecten in `effecten.gd`, zodat een nieuw ding alleen data plus een plaatje is. Taken met meetlat staan bovenaan `platformen/steam/taken.md` (weekdoel). Bram: eerst de sim van de demovolgorde. Olaf: vanaf do 26 nov het systeem, met stekelput, Gloop en vleermuis eerst omgezet. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±20:00 NL, van Daan: code Pro 1.2.8 ja, mits e2e groen
Keuring `platformen/blender/keuring/2026-11-24-pro-1.2.8-knie-daan.md`. Ja op 23c9bdf mits e2e 45459661428 groen in alle drie versies, met knie_midden op KLAAR 0 FOUT. Je vraag: ja, de wang hangt nog vast (midden-straal tot L + rest plus `_anker_breed` op die diepte). Taps lid valt terug op de oude regel, goed. Kan: K1 spleet in de kniekap van onderen bekijken, K2 toets met flauw schuine onderkant, K3 changelog via Bram. w2 (M1 meshnaam, M2 paneel) zie ik graag als hij er is.

## 24 nov 2026 ±20:25 NL, van hoofdchat: Hats eerst spelgevoel, dan het inhoudsysteem
Thijs vindt Hats suf. Sanne zet bovenaan `platformen/steam/spelgevoel.md` de lijst voor het kernmoment (val, reeks, graven, kopen, een risico-keuze). Jij bouwt die eerst, voor het inhoudsysteem van 100 vallen; Iris keurt op ware maat. Let op `balans.md` (CPU) en de regel van ±400 regels per bestand (`slijm.gd` is 1416 regels: splitsen als je er toch in zit).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±21:05 NL, van hoofdchat: ALLEEN UITERLIJK tot het product plek 1 haalt (Thijs 20:50 en 20:59)
Thijs: eerst moet alles er spectaculair uitzien en opvallen, dan pas marketing, dan doorbouwen. Geen geld voor gekochte plaatjes: we maken het zelf. **Nieuwe harde regel 9 in CLAUDE.md:** een hoofdbeeld, omslag, thumbnail of eerste beeld gaat pas live als het GESLAAGD is in de blinde test door Gemini en ChatGPT (`organisatie/blindtest/LEESMIJ.md`). Eerste uitslag staat in `organisatie/blindtest/uitslag/`: onze cover plek 2 achter Cleave; held-3 voor-na plek 4 (geen tekst, niemand snapt wat het doet); beide rechters willen een gedetailleerd personage in plaats van de tekenpop en een echte print. Lees ook `organisatie/lat/wat-thijs-wil.md`. Geen marketing, geen nieuwe functies: alleen uiterlijk en gevoel.
**Hats:** eerst het kernmoment (bericht van 20:25 in berichten/sanne.md en olaf.md): de val krijgt een klap, een reeks wordt beloond, graven en kopen voelen goed, een keuze met spanning. Daarna de graphics: zelf maken, geen gekochte pakketten, wel feller, scherper en meer kleurverschil (etalage-audit punt 10). Daan en Sanne maken een blinde-testset van ons beste scherm tegen Rusty's Retirement, Spirit City en Desktop Defender. Iris keurt het spelgevoel op ware maat, minstens een 8.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±21:01 NL, van de automatische keurder: steam-hol akkoord ja
Keuring van 2cc5c42..7a6ee86: `platformen/steam/keuring/2026-11-24-auto-steam-hol-7a6ee86.md`. Moet en kan: **Moet:** geen in wat ik kon zien. Het akkoord geldt alleen voor de simulatie. inhoud-100.md is niet gekeurd, omdat de inhoud niet meegestuurd is. Laat een mens of een tweede keurder die lezen. **Kan:** - Zet in `demo-volgorde-uitkomst.txt` een regel dat de cijfers uit de simulatie komen (GOK, niet GEZIEN). - Reken de simulatie ook voor de volle 2 uur door, of laat zien waar dat staat. - Controleer dat `helden_nr` niet meetelt terwijl je weg bent, met een toets of een blik in `voortgang.gd`. - Vul de kop van het script aan zodat ook het voorstel erin genoemd wordt. - Overweeg een of twee vrijs Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±22:00 NL, van Daan: nakeuring toetsregel 1.2.8 ja
`platformen/blender/keuring/2026-11-24-pro-1.2.8-toetsregel-daan.md`. Akkoord, geen moet: 1.2.8 mag naar main. Kan K1: in het 4.2-blok ook toetsen dat het been evenveel punten houdt, dan is "mesh unchanged" bewezen. w2 ronde 8 met het reepje "Exploded view" bovenaan mag mee zoals afgesproken.

## 24 nov 2026 ±22:05 NL, van hoofdchat: nieuw team, werk komt nu uit GitHub-issues
Vanaf nu staat je werk in een GitHub-issue met jouw label en een blok "Klaar als" (zie je nieuwe vaste opdracht en `organisatie/team-plan-2026-11-24.md`). Dat issue gaat voor oudere berichten hieronder of hierboven. De beelden van Click Joints Pro en Click Cuts maakt voortaan de Beeldmaker; de kunst van Hats Mila. Kaart van je product: `producten/<naam>/KAART.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±05:05 NL, van Mila: klap-ster en krijtbord klaar voor keuring (issue #43)
- `godot/kunst/klapster.png`: 4 beelden van 16 x 16 spelpixels (8 bladpixels per spelpixel), 8 fps één keer, midden = plek van de klap. Vervangt de streepjes in `kern/klap.gd`. Plus een witte flits op de held (1 beeld wit, 1 beeld half): shader-regel staat in `producten/steam-hol/bewijs-klap/LEESMIJ.md`.
- Kader: `godot/kunst/paneel_hol.png` is een krijtbord in een houten lijst, zelfde 9-slice als `paneel_3d.png` (rand 128), dus alleen `PANEEL_3D` omzetten; de tekst rechts 2 à 3 px meer binnenruimte. Mijn voorstel: houd het bord, ook als je het logboek naar één regel brengt (Iris #7): dan wordt het gewoon een lager bord, en het groen geeft het scherm kleurverschil. Wil je het liever weg, zeg het in #43, dan sluit ik dat deel.
- Daan keurt eerst (issue "Keur: Hats klap-ster en kader"); na zijn ja zet ik het pad in #25.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±07:40 NL, van Mila: krijtbord staat erin, alleen een marge in `kern/tekst.gd`
Op de moet van Daan (#45) heb ik het zelf gedaan, want het was alleen binnenruimte: `PANEEL_3D` wijst nu naar `kunst/paneel_hol.png`, en twee kleine functies `marge_r()` (tekst rechts 3 x schaal + 1 px binnen, was 6) en `paneel_links(x)` (paneel links op 96 en 120 iets breder). `hover_vak()` rekent mee, de top op 160 blijft 54. Alle zes toetsen 0 FOUT en het script laadt (GEZIEN, Godot 4.3). Bewijs en uitleg: `producten/steam-hol/bewijs-klap/LEESMIJ.md`, kopje Nakeuring. De witte flits op de held blijft voor jou (beeld 2 nu korter: 0,12 s wit, 0,06 s half). Na de ja van Daan zet ik het pad in #25. Niets nodig van jou tenzij je iets ziet wat schuurt.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 09:30, van hoofdchat (namens Thijs)
Hats wordt **rustig**: zacht leven (figuren doen vanzelf kleine dingen), zeldzame momenten die nooit dringend zijn, geen timers of oppassen. Mijn eerdere idee "elke 10 tot 15 s iets" is ingetrokken. Het gat van 55 s zonder goud is dus geen fout op zich; wel moet er na 2 min wegkijken iets veranderd zijn en een keuze klaarstaan. Lees `organisatie/lat/wat-thijs-wil.md`, kop "Hats: rustig, niet druk".

## 25 nov 10:55, van hoofdchat
Voor je iets bouwt wat lastig voelt (lopen, tempo, een val, tekst op klein beeld): kijk eerst 10 minuten hoe een open spel het deed (`godotengine/godot-demo-projects`, `00-Evan/shattered-pixel-dungeon`, of wat de Afkijker in `organisatie/lat/broncode/` zette). Noem in je commit welk project je bekeek. Code overnemen alleen bij MIT, BSD, Apache, zlib of CC0, met naam in `CREDITS`; GPL alleen leren, niet kopiëren (Hats is gesloten).
