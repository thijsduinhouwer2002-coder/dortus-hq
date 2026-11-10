extends RefCounted
# Het Heldenboek (Bram, 10 nov). Uitwerking van Sanne in platformen/steam/features.md ("Uitwerking: het Heldenboek",
# 10 nov 03:10 UTC, versie 1, vóór het fest). Dit bestand houdt bij wat er in het boek staat en geeft één regel
# voor de kroniek als er iets nieuws in komt. De bladzijde in het paneel tekent Olaf (zelfde weg als kern/kaartje.gd),
# boekje en stempels tekent Mila.
#
# Vier hoofdstukken:
#   1. helden: 5 bladzijden (gewoon, ridder, dief, magier, bard), elk drie stempels: door Gloop, door de put, ontsnapt.
#      Na de eerste vangst staat de zwakte erbij ("Weak to: Spike Pit"), uit heldensoort.gd, dus altijd eerlijk.
#   2. karakters: 6 trekken, per trek één moment dat je moet zien gebeuren (geen teller). Het boek bewaart de regel
#      met de naam van die held. "verdwaald" bestaat nog niet in het spel (één rij gangen), dus die bladzijde blijft leeg
#      en telt niet mee in het totaal tot hij er is (anders lijkt het boek onaf door iets dat niet kan).
#   3. hoeden: elke hoed die Gloop ooit droeg, met de eerste held die hem verloor; plus stempels van de hoedenberg
#      bij 1000, 3000 en 10.000.
#   4. aartsvijanden: elke held die aartsvijand werd (Thrice-Fled), ook als hij nog leeft; loopt nooit vol.
# Eerlijk (T3, T4): niets verloopt, geen dagelijkse stempels, wat er gebeurde terwijl je weg was telt gewoon mee
# (geef het door met dezelfde functies), alles in het basisspel is te halen.
#
# Gebruik (strook.gd of kaartje.gd van Olaf):
#   var r := boek.held(soort_held, "slijm" | "stekelput" | "ontsnapt", naam)   -> regel of ""
#   var r := boek.moment(trek, naam)            -> regel of ""   (trek: zie MOMENTEN)
#   var r := boek.hoed(hoed_nr, naam)           -> regel of ""
#   var r := boek.berg(aantal_hoeden)           -> regel of ""
#   var r := boek.aarts(naam, info)             -> regel of ""   (nieuwe aartsvijand; info met bijnaam, wrok, bezoeken, littekens)
#   var r := boek.aarts_af(naam, door, dag)     -> regel of ""   (afgerekend: door = "Gloop" of "the Spike Pit")
#   boek.paginas() geeft alle bladzijden als woordenboeken om te tekenen; boek.nieuw_sinds(n) voor "while you were away".
#   Opslaan: naar_dict() in de save, van_dict() bij laden.
# Regels zijn Engels, hooguit 42 tekens (past in het paneel); Sanne mag ze herschrijven in kroniek-regels.md.

const SOORT := preload("res://systemen/heldensoort.gd")
const REGEL_MAX := 42

const HELDEN := ["", "ridder", "dief", "magier", "bard"]
const HELD_NAAM := {"": "the Hero", "ridder": "the Knight", "dief": "the Thief", "magier": "the Wizard", "bard": "the Bard"}
const STEMPELS := ["slijm", "stekelput", "ontsnapt"]

# Per trek het moment dat je moet zien (Sanne): wat strook.gd doorgeeft als moment(trek, naam).
const MOMENTEN := {
	"hebzuchtig": "touched the hoard",            # de Hoard-Toucher
	"schijterig": "turned back at a trap",
	"slaapkop": "was caught napping",
	"wraakzuchtig": "fell to his own grudge",
	"opschepper": "bragged, then ran",
	"verdwaald": "got lost",
}
const MOMENT_BESTAAT := {"hebzuchtig": true, "schijterig": true, "slaapkop": true, "wraakzuchtig": true, "opschepper": true, "verdwaald": false}
const TREK_NAAM := {"hebzuchtig": "the Greedy", "schijterig": "the Timid", "slaapkop": "the Sleepy", "wraakzuchtig": "the Vengeful", "opschepper": "the Braggart", "verdwaald": "the Lost"}

# Hoeden in dezelfde volgorde als kunst/held_hoeden.png (Mila 21:55).
const HOED_NAMEN := ["Helmet", "Pointy hat", "Hood", "Cap", "Crown", "Chef's hat", "Bucket", "Top hat", "Pan", "Feather cap"]
const BERG_STEMPELS := [1000, 3000, 10000]

var helden := {}      # soort_held -> {"slijm": naam, "stekelput": naam, "ontsnapt": naam} (eerste held die het deed)
var momenten := {}    # trek -> naam
var hoeden := {}      # "nr" -> naam van de eerste held die hem verloor
var berg_stempels: Array = []
var aartsvijanden: Array = []   # [{naam, bijnaam, wrok, bezoeken, littekens, af_door, af_dag}], oudste eerst
var log_nieuw: Array = []       # alle regels die iets nieuws in het boek zetten, oudste eerst (voor "while you were away")

# Varianten per soort regel (Sanne, kroniek-regels.md "Heldenboek", 10 nov 05:05): willekeurig binnen de soort, nooit twee
# keer achter elkaar dezelfde. De eerste variant is steeds de vaste regel van vroeger. vast >= 0 kiest altijd die variant
# (toetsen); rng mag strook.gd zaaien. Niet in de save: het maakt niet uit welke variant na het laden komt.
var rng := RandomNumberGenerator.new()
var vast := -1
var vorige := {}     # soort -> index van de laatst gekozen variant

func _init() -> void:
	rng.randomize()

func _kies(soort: String, opties: Array) -> String:
	if opties.is_empty():
		return ""
	var i := 0
	if vast >= 0:
		i = mini(vast, opties.size() - 1)
	elif opties.size() > 1:
		i = rng.randi_range(0, opties.size() - 2)
		if i >= int(vorige.get(soort, -1)) and vorige.has(soort):
			i += 1          # sla de vorige over, zonder vaker te herkansen
	vorige[soort] = i
	return String(opties[i])

func _past(t: String, kort: String) -> String:
	return t if t.length() <= REGEL_MAX else kort

func _bewaar(r: String) -> String:
	if r != "":
		log_nieuw.append(r)
	return r

# Hoofdstuk 1. wat = "slijm", "stekelput" of "ontsnapt". Geeft een regel als het een nieuwe stempel is.
func held(soort_held: String, wat: String, naam: String, bewoner := "Gloop") -> String:
	if not soort_held in HELDEN or not wat in STEMPELS:
		return ""
	var b: Dictionary = helden.get(soort_held, {})
	if b.has(wat):
		return ""
	var nieuwe_pagina := b.is_empty()
	b[wat] = naam
	helden[soort_held] = b
	var wie: String = HELD_NAAM[soort_held]
	var hoe := ""
	if wat == "slijm":
		hoe = _kies("hoe_slijm", ["%s got him." % bewoner, "%s says yum." % bewoner])
	elif wat == "stekelput":
		hoe = _kies("hoe_put", ["The pit got him.", "Spikes: one."])
	else:
		hoe = _kies("hoe_weg", ["He got away.", "Ran off. Counts."])
	var kort := "New stamp: %s." % wie.replace("the ", "")
	if nieuwe_pagina:
		return _bewaar(_past(_kies("pagina", ["New page: %s. %s", "Page for %s. %s", "Booked: %s. %s"]) % [wie, hoe], kort))
	return _bewaar(_past("New stamp for %s. %s" % [wie, hoe], kort))

# Zwakte zoals in heldensoort.gd: de verdediging waar hij het gevoeligst voor is, pas na zijn eerste vangst.
# Gelijk (gewone held, bard) geeft "".
func zwakte(soort_held: String, bewoner := "Gloop") -> String:
	var b: Dictionary = helden.get(soort_held, {})
	if not (b.has("slijm") or b.has("stekelput")):
		return ""
	var s: float = SOORT.kans_factor(soort_held, "slijm")
	var p: float = SOORT.kans_factor(soort_held, "stekelput")
	if is_equal_approx(s, p):
		return ""
	return "Weak to: %s" % (bewoner if s > p else "Spike Pit")

# Hoofdstuk 2. Een moment dat je zag gebeuren (alleen trekken die in het spel bestaan).
func moment(trek: String, naam: String) -> String:
	if not MOMENTEN.has(trek) or not MOMENT_BESTAAT[trek] or momenten.has(trek):
		return ""
	momenten[trek] = naam
	var zin := _kies("moment", ["New page: %s %s.", "Book: %s %s. Noted.", "%s %s. Filed."])
	return _bewaar(_past(zin % [naam, MOMENTEN[trek]], "New page: %s." % TREK_NAAM[trek].replace("the ", "")))

# Hoofdstuk 3. De eerste keer dat Gloop deze hoed kreeg.
func hoed(nr: int, naam: String) -> String:
	if nr < 0 or nr >= HOED_NAMEN.size() or hoeden.has(str(nr)):
		return ""
	hoeden[str(nr)] = naam
	var hn: String = HOED_NAMEN[nr]
	var zin := _kies("hoed", ["New hat: %s. Thanks, %s." % [hn, naam], "%s added. %s won't need it." % [hn, naam], "Book: %s's %s. Kept." % [naam, hn]])
	return _bewaar(_past(zin, "New hat in the book: %s." % hn))

func berg(aantal: int, bewoner := "Gloop") -> String:
	var hoogste := 0
	for g in BERG_STEMPELS:
		if aantal >= g and not g in berg_stempels:
			berg_stempels.append(g)
			hoogste = g   # bij een sprong (weg geweest) alleen de hoogste regel
	if hoogste == 0:
		return ""
	var zin := _kies("berg", ["The hat pile reached %d. Stamped." % hoogste, "%d hats. The pile has weather now." % hoogste, "%d hats. %s is very proud." % [hoogste, bewoner]])
	return _bewaar(_past(zin, "The hat pile reached %d." % hoogste))

# Hoofdstuk 4. Een nieuwe aartsvijand (Thrice-Fled). info mag bijnaam, wrok, bezoeken en littekens hebben.
func aarts(naam: String, info := {}) -> String:
	var a := _aarts_van(naam)
	if not a.is_empty():
		for k in ["bijnaam", "wrok", "bezoeken", "littekens"]:   # bijwerken, geen nieuwe regel
			if info.has(k):
				a[k] = info[k]
		return ""
	aartsvijanden.append({"naam": naam, "bijnaam": String(info.get("bijnaam", "Thrice-Fled")), "wrok": String(info.get("wrok", "")),
		"bezoeken": int(info.get("bezoeken", 3)), "littekens": int(info.get("littekens", 0)), "af_door": "", "af_dag": 0})
	var zin := _kies("aarts", ["New nemesis in the book: %s.", "%s is in the book. In red ink.", "%s got his own page. He'd love it."])
	return _bewaar(_past(zin % naam, "New nemesis in the book."))

func aarts_af(naam: String, door: String, dag: int) -> String:
	var a := _aarts_van(naam)
	if a.is_empty() or String(a.af_door) != "":
		return ""
	a.af_door = door
	a.af_dag = maxi(1, dag)
	var d := int(a.af_dag)
	var zin := _kies("aarts_af", ["Book: %s, settled on day %d." % [naam, d], "%s's page is closed. Day %d." % [naam, d], "Day %d: %s's grudge is filed." % [d, naam]])
	return _bewaar(_past(zin, "Book: a nemesis settled."))

func _aarts_van(naam: String) -> Dictionary:
	for a in aartsvijanden:
		if String(a.naam) == naam:
			return a
	return {}

# Hoeveel er in het boek staat van wat er te halen is (hoofdstuk 4 telt niet mee: dat loopt nooit vol).
func vol() -> Dictionary:
	var heb := 0
	var kan := 0
	for s in HELDEN:
		kan += STEMPELS.size()
		heb += (helden.get(s, {}) as Dictionary).size()
	for t in MOMENTEN:
		if MOMENT_BESTAAT[t]:
			kan += 1
			heb += 1 if momenten.has(t) else 0
	kan += HOED_NAMEN.size() + BERG_STEMPELS.size()
	heb += hoeden.size() + berg_stempels.size()
	return {"heb": heb, "kan": kan}

# Alle bladzijden om te tekenen, in boekvolgorde. Elk: {hoofdstuk, titel, regels: [..], stempels: [[naam, gehaald]], open}
# open = false: nog niets op de bladzijde (Olaf kan hem als silhouet tekenen).
func paginas(bewoner := "Gloop") -> Array:
	var uit := []
	for s in HELDEN:
		var b: Dictionary = helden.get(s, {})
		var st := []
		for w in STEMPELS:
			st.append([w, b.has(w)])
		var regels := []
		var zw := zwakte(s, bewoner)
		if zw != "":
			regels.append(zw)
		if s != "":
			regels.append(String(SOORT.DATA[s]["uitleg"]))
		uit.append({"hoofdstuk": 1, "titel": String(HELD_NAAM[s]).capitalize(), "regels": regels, "stempels": st, "open": not b.is_empty()})
	for t in MOMENTEN:
		if not MOMENT_BESTAAT[t]:
			continue
		var n: String = momenten.get(t, "")
		uit.append({"hoofdstuk": 2, "titel": String(TREK_NAAM[t]).capitalize(), "regels": [_past("%s %s." % [n, MOMENTEN[t]], n)] if n != "" else [],
			"stempels": [], "open": n != ""})
	for i in HOED_NAMEN.size():
		var n2: String = hoeden.get(str(i), "")
		uit.append({"hoofdstuk": 3, "titel": HOED_NAMEN[i], "regels": ["First worn by %s." % n2] if n2 != "" else [], "stempels": [], "open": n2 != "", "hoed": i})
	var bs := []
	for g in BERG_STEMPELS:
		bs.append([str(g), g in berg_stempels])
	uit.append({"hoofdstuk": 3, "titel": "The Hat Pile", "regels": [], "stempels": bs, "open": not berg_stempels.is_empty()})
	for a in aartsvijanden:
		var rg := []
		if String(a.wrok) != "":
			rg.append("Grudge: %s." % a.wrok)
		rg.append("Came %d times." % int(a.bezoeken))
		if String(a.af_door) != "":
			rg.append("Settled on day %d by %s." % [int(a.af_dag), a.af_door])
		uit.append({"hoofdstuk": 4, "titel": "%s the %s" % [a.naam, a.bijnaam], "regels": rg, "stempels": [], "open": true, "littekens": int(a.littekens)})
	return uit

# Regels die erbij kwamen na de eerste n (Voortgang: "while you were away", de eerste regel noemt nieuwe bladzijden).
func nieuw_sinds(n: int) -> Array:
	return log_nieuw.slice(clampi(n, 0, log_nieuw.size()))

func naar_dict() -> Dictionary:
	return {"helden": helden.duplicate(true), "momenten": momenten.duplicate(), "hoeden": hoeden.duplicate(),
		"berg": berg_stempels.duplicate(), "aarts": aartsvijanden.duplicate(true)}

# Kapotte of oude saves: alles wat niet klopt wordt overgeslagen of krijgt de standaardwaarde, nooit een fout.
static func _s(x, std := "") -> String:
	return x if x is String else std

static func _i(x, std := 0) -> int:
	return int(x) if (x is int or x is float) else std

func van_dict(d: Dictionary) -> void:
	helden.clear()
	var dh = d.get("helden", {})
	if dh is Dictionary:
		for s in dh:
			if s is String and s in HELDEN and dh[s] is Dictionary:
				var b := {}
				for w in dh[s]:
					if w is String and w in STEMPELS and dh[s][w] is String:
						b[w] = dh[s][w]
				helden[s] = b
	momenten.clear()
	var dm = d.get("momenten", {})
	if dm is Dictionary:
		for t in dm:
			if t is String and MOMENTEN.has(t) and dm[t] is String:
				momenten[t] = dm[t]
	hoeden.clear()
	var dho = d.get("hoeden", {})
	if dho is Dictionary:
		for k in dho:
			if k is String and k.is_valid_int() and int(k) >= 0 and int(k) < HOED_NAMEN.size() and dho[k] is String:
				hoeden[str(int(k))] = dho[k]
	berg_stempels.clear()
	var db = d.get("berg", [])
	if db is Array:
		for g in db:
			var gi := _i(g, -1)
			if gi in BERG_STEMPELS and not gi in berg_stempels:
				berg_stempels.append(gi)
	aartsvijanden.clear()
	var da = d.get("aarts", [])
	if da is Array:
		for a in da:
			if a is Dictionary and _s(a.get("naam")) != "":
				aartsvijanden.append({"naam": _s(a.get("naam")), "bijnaam": _s(a.get("bijnaam"), "Thrice-Fled"), "wrok": _s(a.get("wrok")),
					"bezoeken": _i(a.get("bezoeken"), 3), "littekens": _i(a.get("littekens")), "af_door": _s(a.get("af_door")), "af_dag": _i(a.get("af_dag"))})
	log_nieuw.clear()   # de regels zelf bewaren we niet (staan al in de kroniek); alleen het boek telt
