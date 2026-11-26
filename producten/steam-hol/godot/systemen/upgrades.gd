extends RefCounted
# Upgrades per bewoner en val (Bram, 10 nov). Feature 5 van de eerste speelbare versie (platformen/steam/features.md),
# grootste gat tegenover de toppers (platformen/steam/toppers.md, gat 1): in een bezoek van 30 s iets te kiezen
# dat je de minuut erna terugziet.
#
# Getallen uit platformen/steam/balans.md (Sanne) en sim/sim.py: drie upgrades per soort, kost 45, 60, 70 (Olaf 26 nov #134; Sanne 26 nov 45, 60, 90; 25 nov 45, 60, 160; daarvoor 45, 126, 353),
# elke upgrade +7 procentpunt kans dat een held valt. Daarbovenop heeft elke stap iets eigens dat je ziet of merkt,
# zodat het een keuze is en geen getal:
#   slijm:     1 Big Gloop (groter, +7)  2 Bouncy Gloop (+7, en plat 20 s in plaats van 30)  3 Royal Gloop (+7, paarse cape van Mila; eerst een kroon, maar die botste met de hoedentoren)
#   stekelput: 1 Rusty Spikes (+7)       2 Deep Pit (+7, en een schijterige held keert er niet voor om)  3 Trick Lid (+7, dicht tot hij erop staat)
# Wat het spel ermee doet:
# - held.gd vraagt de kans erbij via het hol: als hol een eigenschap "upgrades" heeft (dit object), telt
#   kans_erbij(soort) mee. Zonder die eigenschap verandert er niets (ook niet in de oude films).
# - slijm.gd rekent bij plat() zelf plat_s x 2/3 vanaf Bouncy Gloop (20 s in het spel, ook korter in de demo).
# - de tekening van elke stap is van Mila (kunst/slijm_groot2.png, slijm_upgrades2.png, stekelput_upgrades.png);
#   slijm.gd tekent Gloop per stap, hol.gd (Olaf) de put.
# - opslaan: naar_dict() en van_dict() (in de save van strook.gd).
# Geen tijdsdruk en geen straf: kopen kan altijd, weghalen geeft de volle prijs terug (balans.md), dus niets is fout te kiezen.

const SOORTEN := ["slijm", "stekelput"]
const MAX_NIVEAU := 6
# Olaf 26 nov (#145, Iris aandacht 7): na de zesde koop (±11 min) was er 4 tot 9 min niets te kopen. Daarom per soort
# stap 4, 5 en 6, alleen getallen, geen nieuwe kunst: het beeld blijft dat van stap 3 (beeld_niveau()) en het koopmoment
# (wip van Gloop, schudden van de put, kroniekregel) is hetzelfde.
# Olaf 26 nov (#162, Iris 499fd9f punt 1): wel blijvend te zien, per stap boven 3 één gouden steen voor Gloop en op elke put
# (systemen/stap_teken.gd), dus stap 4, 5 en 6 tel je af aan 1, 2 en 3 stenen. Elk +2 goud per vangst (GOUD_STAP), geen extra
# kans (dan ontsnapte bijna niemand meer, wrok weg); Sticky Gloop ligt ook maar 15 s plat. Prijs hoger dan stap 3.
const BEELD_MAX := 3
const BASIS := 45.0   # Sanne 10 nov 01:50 (balans.md): 45, 126, 353; was 60
const FACTOR := 2.8   # niet meer gebruikt voor de prijs, zie PRIJZEN
# Sanne 25 nov (bouwblad I "minuut 4 tot 15", spelgevoel.md): koop 2 kwam pas 6 tot 8 min na koop 1 (Iris, 4 zaden,
# GEZIEN); Ropuka krijgt precies die klacht ("1 upgrade every 6 minutes", DERDEN, lat hats-tempo.md). Stap 2 en 3 goedkoper.
# Sanne 26 nov (Iris keuring 369bfca, aandacht 7): na de vierde koop 5 tot 7 min niets te kiezen, want stap 3 (160)
# haalde geen zaad in 900 s. Stap 3 naar 90: tot minuut 15 elke ±3 min een keuze (meting in spelgevoel.md, bouwblad I).
# Olaf 26 nov (#134, Iris aandacht 7): stap 3 naar 70 (was 90). Een held brengt na minuut 4 ±15 tot 18
# goud (kern/afloop.gd GOUD_LAAT); 90 vroeg 6 tot 7 vangsten en gaf het langste gat (meting platformen/steam/data/minuut4-15/olaf-134/).
# Olaf 26 nov (#145): stap 4, 5 en 6 kosten 75, 95 en 115 (de put 10 meer, PUT_LATER); 2 of 4 stappen erbij gaf
# steeds een lege winkel of een lang gat (meting en geprobeerde varianten in platformen/steam/data/minuut11-20/olaf-145/).
# Sanne 26 nov (Iris keuring 499fd9f punt 3): van koop 1 naar koop 2 zat 175 tot 197 s bij 4 van 6 zaden. Stap 1 naar 40
# (was 45): koop 2 mediaan 257 naar 219 s, gat koop 1 tot 2 mediaan 183 naar 145 s, boven 170 s in 17 van 48 runs
# (was 41 van 48); koop 1 blijft 73 tot 79 s, minuut 11 tot 20 gelijk (meting platformen/steam/data/koop2/).
# De demo-film houdt 45 (DEMO_EERSTE), zodat hij gelijk blijft aan de gekeurde (Daan #109 M1).
const PRIJZEN := [40, 60, 70, 75, 95, 115]
const DEMO_EERSTE := 45
var demo := false   # kern/strook.gd zet dit bij demo=1
const KANS_PER := 0.07
# Per stap wat hij erbij doet (#145): stap 1 tot 3 elk +7 procentpunt kans; stap 4 tot 6 elk +2 goud per vangst.
const KANS_STAP := [0.07, 0.07, 0.07, 0.0, 0.0, 0.0]
const GOUD_STAP := [0, 0, 0, 2, 2, 2]   # goud erbij per vangst (kern/afloop.gd)

# Naam en korte uitleg per stap, Engels zoals in het spel (hooguit 22 en 34 tekens, past in het paneel).
const STAPPEN := {
	"slijm": [
		{"naam": "Big Gloop", "uitleg": "Bigger mouth. More heroes fall."},
		{"naam": "Bouncy Gloop", "uitleg": "Back up in 20 s instead of 30."},
		{"naam": "Royal Gloop", "uitleg": "A royal cape. Heroes gulp."},
		{"naam": "Sticky Gloop", "uitleg": "15 s nap. Heroes drop 2 more gold."},
		{"naam": "Greedy Gloop", "uitleg": "Heroes drop 2 more gold."},
		{"naam": "Gloop Prime", "uitleg": "Heroes drop 2 more gold. Again."},
	],
	"stekelput": [
		{"naam": "Rusty Spikes", "uitleg": "Rust hurts. More heroes fall."},
		{"naam": "Deep Pit", "uitleg": "Timid heroes forget to turn back."},
		{"naam": "Trick Lid", "uitleg": "Looks like floor until it isn't."},
		{"naam": "Sharp Spikes", "uitleg": "Shiny. Heroes drop 2 more gold."},
		{"naam": "Endless Pit", "uitleg": "Endless. Heroes drop 2 more gold."},
		{"naam": "Doom Pit", "uitleg": "Heroes drop 2 more gold. For doom."},
	],
}

var niveaus := {"slijm": 0, "stekelput": 0}

func niveau(soort: String) -> int:
	return int(niveaus.get(soort, 0))

# Welk beeld de soort krijgt: stap 4 tot 6 hebben geen eigen kunst, dus het beeld van stap 3 (#145).
func beeld_niveau(soort: String) -> int:
	return mini(niveau(soort), BEELD_MAX)

# Wat de volgende stap kost, of -1 als alles al gekocht is (of de soort onbekend is).
func kost(soort: String) -> int:
	if not niveaus.has(soort) or niveau(soort) >= MAX_NIVEAU:
		return -1
	return prijs(soort, niveau(soort))

# Prijs van stap i + 1 van een soort. Vanaf stap 4 kost de put PUT_LATER meer, zodat Gloop en de put om en om
# klaar zijn en niet twee kopen vlak na elkaar komen met daarna een lang gat (#145, meting olaf-145).
const PUT_LATER := 10
func prijs(soort: String, i: int) -> int:
	if demo and i == 0:
		return DEMO_EERSTE
	return int(PRIJZEN[i]) + (PUT_LATER if soort == "stekelput" and i >= BEELD_MAX else 0)

func kan_kopen(soort: String, goud: int) -> bool:
	var k := kost(soort)
	return k >= 0 and goud >= k

# Koop de volgende stap. Geeft het goud dat overblijft, of -1 als het niet kan (dan verandert er niets).
func koop(soort: String, goud: int) -> int:
	if not kan_kopen(soort, goud):
		return -1
	var k := kost(soort)
	niveaus[soort] = niveau(soort) + 1
	return goud - k

# Weghalen van de bovenste stap: de volle prijs terug (balans.md). Geeft het goud erbij, of 0 als er niets was.
func verkoop(soort: String) -> int:
	if niveau(soort) <= 0:
		return 0
	niveaus[soort] = niveau(soort) - 1
	return kost(soort)

# Naam en uitleg van de volgende stap (voor de knop of het kaartje), of {} als alles gekocht is.
func volgende(soort: String) -> Dictionary:
	if kost(soort) < 0:
		return {}
	var s: Dictionary = STAPPEN[soort][niveau(soort)].duplicate()
	s["kost"] = kost(soort)
	return s

# Het volgende doel voor het paneel (Iris keuring 1, probleem 2: zonder klik zien wat je hierna kunt kopen):
# de goedkoopste volgende stap van de soorten die er zijn, met wat er nog aan goud ontbreekt. {} als alles gekocht is.
# Bij gelijke prijs wint de eerste soort in de lijst (Gloop staat er altijd, dus eerst "slijm").
func doel(soorten: Array, goud: int) -> Dictionary:
	var beste := {}
	for soort in soorten:
		var v := volgende(String(soort))
		if v.is_empty():
			continue
		if beste.is_empty() or int(v.kost) < int(beste.kost):
			beste = v
			beste["soort"] = String(soort)
	if not beste.is_empty():
		beste["tekort"] = maxi(0, int(beste.kost) - goud)
	return beste

# Wat de held erbij telt (procentpunten als fractie): 0,07 per stap.
func kans_erbij(soort: String) -> float:
	var k := 0.0
	for i in niveau(soort):
		k += float(KANS_STAP[i])
	return k

# Goud erbij per vangst door stap 4 tot 6 van beide soorten samen (#145), voor kern/afloop.gd.
func goud_erbij() -> int:
	var g := 0
	for soort in SOORTEN:
		for i in niveau(soort):
			g += int(GOUD_STAP[i])
	return g

# Factor op de tijd dat de slijm plat ligt (slijm.gd plat()): Bouncy Gloop 2/3, dus 20 s in plaats van 30 (slijm.gd plat_s 30;
# tot 26 nov zei de tekst 40 en 60, dat klopte niet meer sinds plat_s 30 werd).
# Sticky Gloop (stap 4): 1/2, dus 15 s.
func plat_factor() -> float:
	if niveau("slijm") >= 4:
		return 0.5
	return 2.0 / 3.0 if niveau("slijm") >= 2 else 1.0

# Deep Pit: een schijterige held keert na een klap van de put niet om.
func put_houdt_vast() -> bool:
	return niveau("stekelput") >= 2

# Trick Lid: de put ziet eruit als vloer tot er iemand op staat (alleen uiterlijk, voor hol.gd).
func put_verborgen() -> bool:
	return niveau("stekelput") >= 3

# Wat "Undo" teruggeeft: de volle prijs van de bovenste stap (balans.md), 0 als er niets gekocht is.
# kern/kaartje.gd gebruikt dit, zodat er geen tweede kopie van de formule is (vraag Olaf 10 nov 02:40).
func terug(soort: String) -> int:
	var n := niveau(soort)
	if n <= 0:
		return 0
	return prijs(soort, n - 1)

# Koopregels met een grap (Sanne, platformen/steam/kroniek-regels.md "Kopen", toets 8 punt 4). Elke regel zegt
# wat de stap echt doet. {b} = de naam van de bewoner. De eerste keer de eerste regel, daarna om de beurt.
const KOOP_REGELS := {
	"Big Gloop": ["{b} is now Big {b}. Bigger mouth.", "{b} grew. The hats fit better.", "More {b}. Same appetite. Worse."],
	"Bouncy Gloop": ["{b} bounces now. Back up in 20 s.", "{b} learned to bounce. Smug.", "Boing. {b} is Bouncy {b}."],
	"Royal Gloop": ["{b} wears a royal cape now.", "All hail Royal {b}. Burp.", "{b} is royalty now. Insufferable."],
	"Rusty Spikes": ["The Spike Pit got rusty. Ouch.", "Rust on the spikes. On purpose.", "The spikes are rusty now. Tetanus."],
	"Deep Pit": ["The pit got deeper. Echo, echo.", "Deeper pit. Nobody turns back now.", "The pit is very deep now. Hello?"],
	"Trick Lid": ["The pit has a lid. Looks like floor.", "New floor. Not floor.", "The Spike Pit hides now. Shh."],
	"Sticky Gloop": ["{b} is sticky now. Back up in 15 s.", "{b} got sticky. Nobody asked.", "Sticky {b}. Do not touch."],
	"Greedy Gloop": ["{b} got greedy. Heroes pay more.", "Greedy {b}. Shake those pockets.", "{b} wants more gold. As always."],
	"Gloop Prime": ["{b} Prime. Heroes pay even more.", "{b} is in its prime. Pay up.", "Prime {b}. Pockets empty faster."],
	"Sharp Spikes": ["The spikes got shiny. Ouch.", "Shiny spikes. Very rude.", "Shiny spikes. On purpose."],
	"Endless Pit": ["The pit has no bottom now.", "Endless pit. Hats still land.", "The pit goes down forever now."],
	"Doom Pit": ["The Spike Pit is the Doom Pit now.", "Doom Pit. Heroes pay on the way down.", "Doom. Also, gold."],
}
const REGEL_MAX := 42
var _regel_tel := {}   # hoe vaak elke stap al een regel gaf (niet bewaard: na herstart begint hij weer bij de eerste; Undo en opnieuw kopen geeft de volgende grap)

# De regel voor de kroniek als je iets koopt (hooguit 42 tekens). Past een grap niet (lange naam), dan de korte vaste regel.
func koop_regel(soort: String, bewoner := "Gloop") -> String:
	var n := niveau(soort)
	if n <= 0:
		return ""
	var naam: String = STAPPEN[soort][n - 1]["naam"]
	var passend: Array = []
	for r in KOOP_REGELS.get(naam, []):
		var t := String(r).replace("{b}", bewoner)
		if t.length() <= REGEL_MAX:
			passend.append(t)
	if passend.is_empty():
		if soort == "slijm":
			return "%s is now %s." % [bewoner, naam.replace("Gloop", bewoner)]
		return "The Spike Pit got %s." % naam
	var i := int(_regel_tel.get(naam, 0))
	_regel_tel[naam] = i + 1
	return passend[i % passend.size()]

func naar_dict() -> Dictionary:
	return niveaus.duplicate()

func van_dict(d: Dictionary) -> void:
	for s in SOORTEN:
		niveaus[s] = clampi(int(d.get(s, 0)), 0, MAX_NIVEAU)
