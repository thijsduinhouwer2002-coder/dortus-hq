extends RefCounted
# Reuzen: na minuut 25 elke 10 tot 15 min iets wat je nog niet zag (Sanne 27 nov 2026, issue #291 punt 2, Iris #286).
# Iris: "minuut 50 is dezelfde scène als minuut 25 met een grotere berg". Hol-niveau 9 tot 12 komt in de film van 60 min
# (zaad 7, koper) op 24, 34, 43 en 57 min (GEZIEN, bewijs-robijn/nieuw-60min-zaad7-kort.log). Bij elk van die niveaus komt
# één keer een reus binnen: een held anderhalf keer zo groot, met de kroon, een eigen naam en een eigen regel. Hij is
# goud waard (2 keer de buit, veel muntjes), loopt langzaam en zijn kroon komt op de berg. Ontsnapt hij, dan komt hij als terugkomer
# weer even groot terug. Geen nieuwe kunst: de bladen van ridder, dief, magier en bard, groter getekend (node-schaal,
# zoals de keurstand figuur=<factor>). Lat: Iris noemde "baas"; tempo-regel 3 en 5 (`organisatie/lat/hats-tempo.md`).
# Spelerstekst is concept tot Thijs hem schrijft. Niet in de demo-film.

const SCHAAL := 1.5
const BUIT_X := 2
const LOOP := 0.6         # hij loopt langzaam (factor op lopen), zo zie je hem langer dan een gewone held
const KROON := 4          # hoed_nr van de kroon (held_hoeden.png, zie binnenkomst.gd "opgegeten")
const KOMT_NA_S := 6.0    # zo snel na het nieuwe hol-niveau komt hij binnen

# hol-niveau: soort, naam (ridder zonder "Sir": de regels zetten {titel} ervoor), binnenkomstregel, vangstregel (hooguit 42 tekens met " +27" erachter)
const REUZEN := {
	9: {"soort": "ridder", "naam": "Hulk", "binnen": "Sir Hulk ducks in. He does not fit.",
		"val": "Sir Hulk fell. The hole shook."},
	10: {"soort": "dief", "naam": "Big Pip", "binnen": "Big Pip tiptoes in. Loudly.",
		"val": "Big Pip fell. Big hole, big loot."},
	11: {"soort": "magier", "naam": "Grand Mage Oom", "binnen": "Grand Mage Oom floats in. Huge.",
		"val": "Oom fell. His crown stays here."},
	12: {"soort": "bard", "naam": "Bard Colossus", "binnen": "Bard Colossus brings a giant lute.",
		"val": "The Colossus fell. Encore!"},
}

static func is_reus(info: Dictionary) -> bool:
	return int(info.get("reus", 0)) > 0

# Nieuw hol-niveau (afloop.faam_erbij): zet de reus klaar, één keer per niveau per spel.
static func niveau_erbij(s, niv: int) -> void:
	if bool(s.get("demo")) or not REUZEN.has(niv) or s.reuzen_gezien.has(niv):
		return
	s.reuzen_gezien.append(niv)
	s.reus_wacht = niv
	s.volgende_held = minf(float(s.volgende_held), float(s.t) + KOMT_NA_S)
	s.log_regel("HOL reus klaar: niveau %d (t %.1f)" % [niv, s.t])

# Binnenkomst: is er een reus aan de beurt, maak dan zijn info (anders leeg).
static func neem(s) -> Dictionary:
	var niv: int = int(s.reus_wacht)
	if niv <= 0 or not REUZEN.has(niv):
		return {}
	s.reus_wacht = 0
	var r: Dictionary = REUZEN[niv]
	return {"naam": String(r.naam), "bezoeken": 0, "wrok": "", "kleur": "#c9a227", "hoed": "#e0b040",
		"taai": 1, "hoed_nr": KROON, "soort_held": String(r.soort), "reus": niv, "snelheid": LOOP}

static func binnen_regel(info: Dictionary) -> String:
	return String(REUZEN.get(int(info.get("reus", 0)), {}).get("binnen", ""))

static func val_regel(info: Dictionary) -> String:
	return String(REUZEN.get(int(info.get("reus", 0)), {}).get("val", ""))

static func schaal(info: Dictionary) -> float:
	return SCHAAL if is_reus(info) else 1.0
