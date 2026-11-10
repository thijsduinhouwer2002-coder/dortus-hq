extends RefCounted
# Upgrades per bewoner en val (Bram, 10 nov). Feature 5 van de eerste speelbare versie (platformen/steam/features.md),
# grootste gat tegenover de toppers (platformen/steam/toppers.md, gat 1): in een bezoek van 30 s iets te kiezen
# dat je de minuut erna terugziet.
#
# Getallen uit platformen/steam/balans.md (Sanne) en sim/sim.py: drie upgrades per soort, kost 45, 126, 353 (45 x 2,8^n, Sanne 10 nov),
# elke upgrade +7 procentpunt kans dat een held valt. Daarbovenop heeft elke stap iets eigens dat je ziet of merkt,
# zodat het een keuze is en geen getal:
#   slijm:     1 Big Gloop (groter, +7)  2 Bouncy Gloop (+7, en plat 40 s in plaats van 60)  3 Royal Gloop (+7, kroon van slijm)
#   stekelput: 1 Rusty Spikes (+7)       2 Deep Pit (+7, en een schijterige held keert er niet voor om)  3 Trick Lid (+7, dicht tot hij erop staat)
# Wat het spel ermee doet:
# - held.gd vraagt de kans erbij via het hol: als hol een eigenschap "upgrades" heeft (dit object), telt
#   kans_erbij(soort) mee. Zonder die eigenschap verandert er niets (ook niet in de oude films).
# - slijm.gd rekent bij plat() zelf plat_s x 2/3 vanaf Bouncy Gloop (40 s in het spel, ook korter in de demo).
# - de tekening van elke stap is van Mila (gevraagd in taken.md); tot die er is geeft niveau() het getal en tekent
#   slijm.gd niets anders.
# - opslaan: naar_dict() en van_dict() (in de save van strook.gd).
# Geen tijdsdruk en geen straf: kopen kan altijd, weghalen geeft de volle prijs terug (balans.md), dus niets is fout te kiezen.

const SOORTEN := ["slijm", "stekelput"]
const MAX_NIVEAU := 3
const BASIS := 45.0   # Sanne 10 nov 01:50 (balans.md): 45, 126, 353; was 60
const FACTOR := 2.8
const KANS_PER := 0.07

# Naam en korte uitleg per stap, Engels zoals in het spel (hooguit 22 en 34 tekens, past in het paneel).
const STAPPEN := {
	"slijm": [
		{"naam": "Big Gloop", "uitleg": "Bigger mouth. More heroes fall."},
		{"naam": "Bouncy Gloop", "uitleg": "Back up in 40 s instead of 60."},
		{"naam": "Royal Gloop", "uitleg": "A slime crown. Heroes gulp."},
	],
	"stekelput": [
		{"naam": "Rusty Spikes", "uitleg": "Rust hurts. More heroes fall."},
		{"naam": "Deep Pit", "uitleg": "Timid heroes forget to turn back."},
		{"naam": "Trick Lid", "uitleg": "Looks like floor until it isn't."},
	],
}

var niveaus := {"slijm": 0, "stekelput": 0}

func niveau(soort: String) -> int:
	return int(niveaus.get(soort, 0))

# Wat de volgende stap kost, of -1 als alles al gekocht is (of de soort onbekend is).
func kost(soort: String) -> int:
	if not niveaus.has(soort) or niveau(soort) >= MAX_NIVEAU:
		return -1
	return int(round(BASIS * pow(FACTOR, niveau(soort))))

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

# Wat de held erbij telt (procentpunten als fractie): 0,07 per stap.
func kans_erbij(soort: String) -> float:
	return KANS_PER * niveau(soort)

# Factor op de tijd dat de slijm plat ligt (slijm.gd plat()): Bouncy Gloop 2/3, dus 40 s in plaats van 60.
func plat_factor() -> float:
	return 2.0 / 3.0 if niveau("slijm") >= 2 else 1.0

# Deep Pit: een schijterige held keert na een klap van de put niet om.
func put_houdt_vast() -> bool:
	return niveau("stekelput") >= 2

# Trick Lid: de put ziet eruit als vloer tot er iemand op staat (alleen uiterlijk, voor hol.gd).
func put_verborgen() -> bool:
	return niveau("stekelput") >= 3

# De regel voor de kroniek als je iets koopt (hooguit 42 tekens): "Gloop is now Big Gloop."
func koop_regel(soort: String, bewoner := "Gloop") -> String:
	var n := niveau(soort)
	if n <= 0:
		return ""
	var naam: String = STAPPEN[soort][n - 1]["naam"]
	if soort == "slijm":
		return "%s is now %s." % [bewoner, naam.replace("Gloop", bewoner)]
	return "The Spike Pit got %s." % naam

func naar_dict() -> Dictionary:
	return niveaus.duplicate()

func van_dict(d: Dictionary) -> void:
	for s in SOORTEN:
		niveaus[s] = clampi(int(d.get(s, 0)), 0, MAX_NIVEAU)
