extends RefCounted
class_name Voortgang
# Voortgang terwijl je weg bent (Bram). Regels van Thijs: nooit straffen als je weg bent, niets kwijtraken,
# geen dagelijkse plicht. Dus: bij openen rekenen we uit hoeveel helden er kwamen en hoeveel goud ze achterlieten.
# - Alleen winst, nooit verlies (ontsnapte helden nemen niets mee).
# - Klok terugzetten: verstreken tijd < 0 telt als 0, en de bewaarde tijd gaat nooit achteruit.
# - Plafond van 12 uur: wie een week weg is krijgt niet meer dan wie een nacht weg was, zodat
#   niemand zich verplicht voelt om dagelijks te kijken, en klok vooruitzetten niets oplevert boven die 12 uur.
# - Vast zaad: dezelfde save en dezelfde tijd geven dezelfde uitkomst (geen herladen om beter te gooien).

const PLAFOND_S := 12 * 3600
const HELD_ELKE_S := 47.5          # gemiddeld, zelfde orde als in het spel (25 tot 70 s)

# vallen: aantal vallen, bewoners: aantal bewoners. Meer verdediging = meer helden vallen.
# gangen en faam (optioneel) maken het goud gelijk aan het spel en sim/ (balans.md): per val
# 6 x (1 + 0,1 x faam) x (1 + gangen / 40), en faam maakt helden iets sterker (x 0,97 per niveau, bodem 0,75).
# Zo levert een uur weg ongeveer hetzelfde op als een uur kijken (zonder de +3 voor terugkomers: die kent de save niet).
# upg (optioneel): systemen/upgrades.gd; gekochte stappen tellen ook terwijl je weg bent (+7 procentpunt per stap).
static func reken(laatst_unix: int, nu_unix: int, vallen: int, bewoners: int, zaad: int, gangen := 6, faam := 0, upg = null) -> Dictionary:
	var weg := nu_unix - laatst_unix
	var teruggezet := weg < 0
	weg = clampi(weg, 0, PLAFOND_S)
	var helden := int(floor(weg / HELD_ELKE_S))
	# zelfde kansen als held.gd en sim/ (put 35%, slijm 45%), met een plafond zodat er altijd verhalen blijven
	var k_put := 0.35 + (upg.kans_erbij("stekelput") if upg != null else 0.0)
	var k_slijm := 0.45 + (upg.kans_erbij("slijm") if upg != null else 0.0)
	var kans_val := clampf((1.0 - pow(1.0 - k_put, vallen) * pow(1.0 - k_slijm, bewoners)) * maxf(0.75, pow(0.97, faam)), 0.0, 0.85)
	var per_val := goud_per_val(gangen, faam)
	var rng := RandomNumberGenerator.new()
	rng.seed = hash([zaad, laatst_unix, helden])
	var gevallen := 0
	var goud := 0
	for i in helden:
		if rng.randf() < kans_val:
			gevallen += 1
			goud += per_val
		else:
			goud += 1   # wie vlucht, laat in de haast één munt vallen
	# hoedentoren (Mila): wie door een bewoner viel, geeft zijn hoed. Aandeel bewoners naar hun kans (slijm 45, put 35).
	# Eigen rng, zodat goud en vallen per zaad hetzelfde blijven als voor de hoedentoren.
	var opgegeten := 0
	if bewoners > 0 and gevallen > 0:
		var deel := k_slijm * bewoners / (k_slijm * bewoners + k_put * vallen)
		var rh := RandomNumberGenerator.new()
		rh.seed = hash([zaad, laatst_unix, helden, "hoeden"])
		for i in gevallen:
			if rh.randf() < deel:
				opgegeten += 1
	var nieuwe_laatst := maxi(laatst_unix, nu_unix)
	return {
		"weg_s": weg, "helden": helden, "gevallen": gevallen, "gevlucht": helden - gevallen,
		"goud": goud, "nieuwe_laatst": nieuwe_laatst, "teruggezet": teruggezet, "opgegeten": opgegeten,
		"regel": samenvatting(weg, helden, gevallen, goud),
	}

# Hoeden voor wie weg was: verdeel `opgegeten` over de slijmen (om en om), willekeurige hoedsoort, vast zaad.
# slijmen = de slijm-nodes (slijm.gd). Geen hap-animatie: het gebeurde terwijl je weg was. Geeft per slijm het aantal.
# Daarna noemt verhaal() de hoeden pas: uitkomst.hoeden_gegeven wordt waar (anders belooft de kroniek iets wat je niet ziet).
static func geef_hoeden(slijmen: Array, uitkomst: Dictionary, zaad: int) -> Array[int]:
	var opgegeten := int(uitkomst.get("opgegeten", 0))
	var per: Array[int] = []
	for s in slijmen:
		per.append(0)
	if slijmen.is_empty():
		return per
	var rng := RandomNumberGenerator.new()
	rng.seed = hash([zaad, opgegeten, "geef_hoeden"])
	for i in opgegeten:
		var k := i % slijmen.size()
		if slijmen[k].has_method("krijg_hoed"):   # kern/standin_slijm.gd kent geen hoeden
			slijmen[k].krijg_hoed(rng.randi_range(0, 9))   # 10 hoedsoorten (Mila 21:55)
			per[k] += 1
	uitkomst["hoeden_gegeven"] = per.reduce(func(a, b): return a + b, 0) > 0
	return per

static func goud_per_val(gangen: int, faam: int) -> int:
	return int(round(6.0 * (1.0 + 0.1 * faam) * (1.0 + gangen / 40.0)))

static func samenvatting(weg: int, helden: int, gevallen: int, goud: int) -> String:
	if helden == 0:
		return "All quiet while you were away."
	var tijd := "%d min" % int(weg / 60.0) if weg < 3600 else "%d h" % int(weg / 3600.0)
	return "While you were away (%s): %d heroes came, %d fell, %d fled. +%d gold." % [tijd, helden, gevallen, helden - gevallen, goud]

# Drie korte regels met namen voor terwijl je weg was (Sanne 9 nov 19:00): niet alleen "+X gold", maar wie er terug was,
# welke wrok speelde en of er een aartsvijand kwam. helden = Kroniek.helden (naam -> {gevlucht, wrok, ...}).
# vijand_namen = namen van wat er staat ("Gloop the Slime", "the Spike Pit"). Vast zaad: zelfde save, zelfde verhaal.
# Er gaat niets verloren: een aartsvijand die kwam, vluchtte weer (of viel en werd afgerekend), nooit iets van jou weg.
static func verhaal(uitkomst: Dictionary, helden: Dictionary, vijand_namen: Array, zaad: int) -> Array[String]:
	var uit: Array[String] = []
	if int(uitkomst.get("helden", 0)) == 0:
		return uit
	var rng := RandomNumberGenerator.new()
	rng.seed = hash([zaad, int(uitkomst.get("nieuwe_laatst", 0)), "verhaal"])
	var terug: Array = []
	var aarts: Array = []
	for naam in helden:
		var g := int(helden[naam].get("gevlucht", 0))
		if g >= 3:
			aarts.append(naam)
		elif g >= 1:
			terug.append(naam)
	terug.sort()
	aarts.sort()
	var uren := float(uitkomst.get("weg_s", 0)) / 3600.0
	# hoeden alleen noemen als ze echt gegeven zijn (geef_hoeden), anders ziet de speler ze niet op Gloop
	var hoeden := int(uitkomst.get("opgegeten", 0)) if bool(uitkomst.get("hoeden_gegeven", false)) else 0
	# 1. wie er terug was
	if not terug.is_empty():
		var n: String = terug[rng.randi_range(0, terug.size() - 1)]
		var wrok: String = String(helden[n].get("wrok", ""))
		if wrok != "" and wrok in vijand_namen:
			# 2. welke wrok speelde
			if rng.randf() < 0.4:
				uit.append(_kort("%s vs %s: settled." % [n, wrok]))
			else:
				uit.append(_kort("%s vs %s: fled again." % [n, wrok]))
		else:
			uit.append(_kort("%s was back and left in a hurry." % n))
	elif hoeden > 0 and _bewoner(vijand_namen) != "":
		uit.append(_kort("%s got %d new hat%s." % [_bewoner(vijand_namen), hoeden, "" if hoeden == 1 else "s"]))
	elif not vijand_namen.is_empty() and int(uitkomst.get("gevallen", 0)) > 0:
		var v: String = vijand_namen[rng.randi_range(0, vijand_namen.size() - 1)]
		uit.append(_kort("%s had a busy shift." % v))
	# 3. aartsvijand: ongeveer 0,5 per uur (sim/), dus na een paar uur vaak wel, na tien minuten zelden
	if not aarts.is_empty() and rng.randf() < clampf(uren * 0.5, 0.0, 0.9):
		var a: String = aarts[rng.randi_range(0, aarts.size() - 1)]
		uit.append(_kort("Nemesis %s came by. Still free." % a))
	if hoeden > 0:
		uit.append(_kort("%d came, %d fell, %d hat%s. +%d gold." % [int(uitkomst.helden), int(uitkomst.gevallen), hoeden, "" if hoeden == 1 else "s", int(uitkomst.goud)]))
	else:
		uit.append(_kort("%d came, %d fell. +%d gold." % [int(uitkomst.helden), int(uitkomst.gevallen), int(uitkomst.goud)]))
	return uit

# Eerste bewoner uit de namen, kort ("Gloop the Slime" -> "Gloop"); vallen beginnen met "the ".
static func _bewoner(namen: Array) -> String:
	for n in namen:
		if not String(n).begins_with("the "):
			var i := String(n).find(" the ")
			return String(n).substr(0, i) if i > 0 else String(n)
	return ""

# Kroniekregels mogen niet langer zijn dan 42 tekens (Sanne, kroniek-regels.md), anders wordt er afgekapt.
static func _kort(r: String) -> String:
	return r if r.length() <= 42 else r.substr(0, 41) + "."

