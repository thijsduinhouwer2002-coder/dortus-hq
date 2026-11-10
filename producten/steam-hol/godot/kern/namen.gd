extends RefCounted
# Deel van kern/strook.gd (Olaf), losgehaald bij het opruimen van 10 nov (strook.gd was 650 regels).
# Statische functies; `s` is de strook. Gedrag gelijk aan voor het splitsen (film.log gelijk).
const REGELS := preload("res://kern/regels.gd")
# Geen namen met een Engelse betekenis: "Ties" leest als stropdassen, "Wil" als Will (Daan 23:45, keuring-build.md)
const NAMEN := ["Bram", "Odo", "Wout", "Gerda", "Pim", "Rik", "Mara", "Joost", "Fenna", "Tibbe", "Lotte", "Kees"]

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

# geen twee helden met dezelfde naam tegelijk (in het hol of bij de terugkomers), anders snap je de wrok niet
static func vrije_naam(s) -> String:
	var bezet := {}
	for h in s.terugkomers:
		bezet[String(h.naam).split(" ")[0]] = true
	for n in s.pensioen_namen:   # anders loopt Mara binnen vlak na "Mara retired. Opened a bakery."
		bezet[String(n).split(" ")[0]] = true
	for w in s.wezens.get_children():
		if w.has_method("is_held"):
			bezet[String(w.info.get("naam", "")).split(" ")[0]] = true
	var vrij: Array = []
	for n in NAMEN:
		if not bezet.has(n):
			vrij.append(n)
	if vrij.is_empty():
		return NAMEN[s.rng.randi_range(0, NAMEN.size() - 1)]
	# eerst namen die nog nooit vielen; anders een naamgenoot met II of III, na III een andere naam
	var nooit: Array = vrij.filter(func(n): return not s.gevallen_namen.has(n))
	if not nooit.is_empty():
		return nooit[s.rng.randi_range(0, nooit.size() - 1)]
	var kan: Array = vrij.filter(func(n): return int(s.gevallen_namen[n]) < 3)
	if kan.is_empty():
		# alle namen vielen al drie keer: opnieuw tellen, dan weer een kale naam
		var n0: String = vrij[s.rng.randi_range(0, vrij.size() - 1)]
		s.gevallen_namen.erase(n0)
		return n0
	var n: String = kan[s.rng.randi_range(0, kan.size() - 1)]
	return n + (" II" if int(s.gevallen_namen.get(n, 0)) == 1 else " III")
