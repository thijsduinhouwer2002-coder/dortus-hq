extends RefCounted
# Deel van kern/strook.gd (Olaf), losgehaald bij het opruimen van 10 nov (strook.gd was 650 regels).
# Statische functies; `s` is de strook. Gedrag gelijk aan voor het splitsen (film.log gelijk).
const REGELS := preload("res://kern/regels.gd")
# Geen namen met een Engelse betekenis: "Ties" leest als stropdassen, "Wil" als Will (Daan 23:45, keuring-build.md)
# 24 namen (Sanne 17 nov 16:50, Iris keuring 22 punt 1): met 12 hielden de vluchters te veel namen bezet en kwamen er
# families op een rij (Fenna, Fenna II, Fenna III). Allemaal 5 letters of minder, zodat elke regel met "Tibbe III" past.
const NAMEN := ["Bram", "Odo", "Wout", "Gerda", "Pim", "Rik", "Mara", "Joost", "Fenna", "Tibbe", "Lotte", "Kees",
	"Henk", "Geert", "Teun", "Siem", "Kobus", "Jop", "Femke", "Ineke", "Anouk", "Merel", "Elke", "Maud"]
# Vrouwennamen uit NAMEN: die krijgen "Dame" in plaats van "Sir" in de regels met {titel} (Sanne 17 nov 10:00, Iris
# keuring 21 punt 1, "Sir Gerda"). Voeg je een vrouwennaam toe aan NAMEN, zet hem dan ook hier (de toets ziet alleen
# of VROUW in NAMEN staat, niet of je hem vergat).
const VROUW := ["Gerda", "Mara", "Fenna", "Lotte", "Femke", "Ineke", "Anouk", "Merel", "Elke", "Maud"]

# "Sir" of "Dame", uit de voornaam (eerste woord, dus "Gerda II" en "Gerda the Twice-Fled" tellen mee).
static func titel(naam: String) -> String:
	return "Dame" if VROUW.has(naam.strip_edges().split(" ")[0]) else "Sir"

# "mom" of "dad" voor de naamgenoot: Fenna II komt voor haar moeder (Iris keuring 22 punt 2). "mom", niet "mum":
# de meeste kopers op Steam lezen Amerikaans Engels (Sanne).
static func ouder(naam: String) -> String:
	return "mom" if VROUW.has(naam.strip_edges().split(" ")[0]) else "dad"

# naam met bijnaam voor een terugkomer ("Kees the Twice-Fled", of "Pim the Hoard-Toucher")
static func bewoner(s) -> String:
	return String(s.slijm.get("bijnaam_naam")) if "bijnaam_naam" in s.slijm else "Gloop"

static func held_naam(s, info: Dictionary) -> String:
	if bool(info.get("hoard_toucher", false)):
		return "%s the Hoard-Toucher" % info.naam
	return "%s %s" % [info.naam, bijnaam(s, int(info.get("bezoeken", 0)))]

# Terugkomer-regel. De Hoard-Toucher komt terug met zijn bijnaam ("Tibbe the Hoard-Toucher is back for Gloop.",
# Sanne toets 7, punt 3), maar alleen als dat binnen 42 tekens past; anders zijn kale naam (nooit afgekapt).
static func terug_regel(s, soort: String, info: Dictionary, w: Dictionary) -> String:
	w["held"] = s._held_naam(info)
	if bool(info.get("hoard_toucher", false)):
		# eerst toetsen of een regel met bijnaam past, zodat de schudzak geen regel opslokt die niemand ziet (kan-punt 3)
		var hw := w.duplicate()
		hw["naam"] = s._held_naam(info)
		for r in REGELS.VOORRAAD.get(soort, []):
			if s.regels.vul(r, hw).length() <= REGELS.MAX:
				return s.regels.kies(soort, hw)
	w["naam"] = info.naam
	return s.regels.kies(soort, w)

static func bijnaam(_s, n: int) -> String:
	match n:
		1: return "the Once-Fled"
		2: return "the Twice-Fled"
		3: return "the Thrice-Fled"
	return "the %d-Times-Fled" % n

# Hoeveel nieuwe helden een voornaam niet terugkomt (Sanne 17 nov 16:50 punt 3).
const RECENT := 6

# Geen twee helden met dezelfde naam tegelijk (in het hol of bij de terugkomers), anders snap je de wrok niet.
# Regel Sanne 17 nov 16:50 (features.md "Namen zonder families op een rij"): uit de vrije namen een met de laagste
# telling in gevallen_namen (nooit gevallen = 0), niet een voornaam van de laatste 6 nieuwe helden tenzij er niets
# anders is, en staan alle vrije namen op 3 dan gaat gevallen_namen helemaal leeg (niet één naam tegelijk: dat gaf
# families op een rij). Achtervoegsel: telling 0 kaal, 1 II, 2 III.
static func vrije_naam(s) -> String:
	var bezet := {}
	for h in s.terugkomers:
		bezet[String(h.naam).split(" ")[0]] = true
	for w in s.wezens.get_children():
		if w.has_method("is_held"):
			bezet[String(w.info.get("naam", "")).split(" ")[0]] = true
	var vrij: Array = []
	for n in NAMEN:
		if not bezet.has(n):
			vrij.append(n)
	# pensioen-namen liever niet (anders loopt Mara binnen vlak na "Mara retired. Opened a bakery."), maar alleen als er
	# dan nog een naam over is (controleur 05:45)
	var pens := {}
	for p in s.pensioen_namen:
		pens[String(p).split(" ")[0]] = true
	var zonder: Array = vrij.filter(func(n): return not pens.has(n))
	if not zonder.is_empty():
		vrij = zonder
	if vrij.is_empty():
		return _onthoud(s, NAMEN[s.rng.randi_range(0, NAMEN.size() - 1)])
	# alle vrije namen vielen al drie keer: hele telling leeg, nieuwe ronde kale namen (vóór de recent-filter, zodat een
	# recente naam op 1 of 2 zijn II of III houdt; controleur 17 nov)
	if vrij.all(func(n): return int(s.gevallen_namen.get(n, 0)) >= 3):
		s.gevallen_namen.clear()
	var recent: Array = s.recente_namen.slice(-RECENT) if "recente_namen" in s else []
	var fris: Array = vrij.filter(func(n): return not recent.has(n))
	# niet uit de laatste 6, tenzij er anders niets is (of alleen namen op 3, dan zou er een vierde Gerda komen)
	if not fris.is_empty() and not fris.all(func(n): return int(s.gevallen_namen.get(n, 0)) >= 3):
		vrij = fris
	var laag := 99
	for n in vrij:
		laag = mini(laag, int(s.gevallen_namen.get(n, 0)))
	var groep: Array = vrij.filter(func(n): return int(s.gevallen_namen.get(n, 0)) == laag)
	var n: String = groep[s.rng.randi_range(0, groep.size() - 1)]
	_onthoud(s, n)
	match int(s.gevallen_namen.get(n, 0)):
		0: return n
		1: return n + " II"
	return n + " III"

static func _onthoud(s, n: String) -> String:
	if "recente_namen" in s:
		s.recente_namen.append(n)
		if s.recente_namen.size() > RECENT:
			s.recente_namen = s.recente_namen.slice(-RECENT)
	return n
