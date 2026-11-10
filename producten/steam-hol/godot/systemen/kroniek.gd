extends RefCounted
class_name Kroniek
# Kroniek van het hol (Bram). Onthoudt elke held: hoe vaak hij kwam, wat hem raakte, zijn wrok en bijnaam.
# Geeft één korte regel voor in de strook. Puur rekenwerk, geen nodes, zodat het te toetsen is.
# Teksten in het spel zijn Engels (winkeltaal); commentaar Nederlands.

const MAX_REGELS := 200
const Stem := preload("res://systemen/kroniek_regels.gd")

var helden := {}        # naam -> {bezoeken, gevlucht, gevallen, wrok, littekens, bijnaam}
var regels: Array[String] = []
var laatste_soort := ""  # uit welke soort van kroniek_regels.gd de laatste regel kwam (voor de toetsen en strook.gd)
var stem = Stem.new()   # de regels van Sanne (kroniek-regels.md), hooguit 42 tekens

const TELWOORD := ["", "Once", "Twice", "Thrice", "Four-Times", "Five-Times", "Six-Times", "Seven-Times"]

func held(naam: String) -> Dictionary:
	if not helden.has(naam):
		helden[naam] = {"bezoeken": 0, "gevlucht": 0, "gevallen": 0, "wrok": "", "littekens": 0, "bijnaam": ""}
	return helden[naam]

# Voor de regels: {naam}, {held}, en {bewoner} of {val} uit wat hem raakte.
func _vars(naam: String, waardoor := "") -> Dictionary:
	var v := {"naam": naam, "held": volle_naam(naam), "bewoner": "", "val": ""}
	if waardoor.begins_with("the "):
		v["val"] = waardoor
	elif waardoor != "" and waardoor != "your Hoard":
		v["bewoner"] = Stem.korte_bewoner(waardoor)
	return v

func _regel(soort: String, v: Dictionary, reserve: String, achter := "", moet_noemen := false) -> String:
	var r: String = stem.kies(soort, v, achter, moet_noemen)
	laatste_soort = soort if r != "" else "reserve"
	return r if r != "" else reserve

# Naamgenoot (Sanne, toets 2): een gevallen naam komt terug als "Kees II", dan "Kees III", daarna "" (kies een andere naam).
func vrije_naam(naam: String) -> String:
	for n in [naam, naam + " II", naam + " III"]:
		if not helden.has(n) or int(helden[n]["gevallen"]) == 0:
			return n
	return ""

# Een held komt binnen. Geeft de info terug die de held meekrijgt (bezoeken, wrok, bijnaam).
# trek ("hebzuchtig" of "schijterig") mag mee voor een regel die bij hem past.
# soort_held ("ridder", "dief", "magier", "bard", systemen/heldensoort.gd) blijft bij hem: een terugkomer houdt zijn soort.
func binnen(naam: String, trek := "", soort_held := "") -> Dictionary:
	var h := held(naam)
	h["bezoeken"] += 1
	if soort_held != "" and h["bezoeken"] == 1:   # alleen bij zijn eerste bezoek; een oude terugkomer blijft gewoon
		h["soort_held"] = soort_held
	soort_held = String(h.get("soort_held", ""))
	var v := _vars(naam, String(h["wrok"]))
	var regel := ""
	var ouder := _ouder(naam)
	var door_ouder := String(helden[ouder].get("gevallen_door", "")) if ouder != "" and helden.has(ouder) else ""
	if h["bezoeken"] == 1 and door_ouder != "" and not door_ouder.begins_with("the ") and door_ouder != "your Hoard":
		# naamgenoot van een held die een bewoner at (Sanne toets 3 punt 2): komt met een wrok tegen die bewoner,
		# wil de hoed van zijn vader terug en vindt hem nooit (een hoed gaat nooit van de toren af)
		h["wrok"] = door_ouder
		v = _vars(naam, door_ouder)
		regel = _regel("naamgenoot_hoed", v, "%s wants dad's hat back." % naam)
	elif h["bezoeken"] == 1 and ouder != "":
		v["oud"] = naam.split(" ")[0]   # "Kees II" en "Kees III": Kees viel hier ooit
		regel = _regel("naamgenoot", v, "%s climbs in." % naam)
	elif h["bezoeken"] == 1 and soort_held != "":
		regel = _regel("binnen_" + soort_held, v, "%s climbs in." % naam)   # de soort zie je meteen (kies in heldensoort.gd)
	elif h["bezoeken"] == 1:
		var soort := "binnen_" + trek if trek != "" and stem.rng.randf() < 0.3 else "binnen"
		regel = _regel(soort, v, "%s climbs in." % naam)
	elif int(h["gevlucht"]) >= 3:
		regel = _regel("aartsvijand", v, "%s is back." % naam)
	else:
		# Sanne toets 3 punt 6: een terugkomer noemt altijd zijn wrok of bijnaam
		regel = _regel("terug", v, "%s is back." % volle_naam(naam), "", true)
	_schrijf(regel)
	return {"naam": naam, "bezoeken": h["bezoeken"] - 1, "wrok": h["wrok"], "bijnaam": h["bijnaam"], "littekens": h["littekens"],
		"soort_held": soort_held}

# Een slaapkop deed een dutje (held.gd zet info "dutje"): één regel, strook.gd kiest wanneer.
func dutje(naam: String) -> String:
	var r := _regel("dutje", _vars(naam), "%s took a nap." % naam)
	_schrijf(r)
	return r

# Een bard ontsnapte en zingt (held.gd zet info "lied"): één regel; strook.gd laat info.lied helden extra komen.
func lied(naam: String) -> String:
	var r := _regel("lied", _vars(naam), "%s sang about you." % naam)
	_schrijf(r)
	return r

# Een held ontsnapt. waardoor = wat hem het laatst raakte ("" als niets). Je verliest nooit iets: geen buit weg.
func gevlucht(naam: String, waardoor: String) -> String:
	var h := held(naam)
	h["gevlucht"] += 1
	if waardoor != "":
		h["wrok"] = waardoor
		h["littekens"] += 1
	h["bijnaam"] = _bijnaam(h)
	var regel := _regel("vlucht" if waardoor != "" else "vlucht_zonder", _vars(naam, waardoor), "%s fled." % naam)
	_schrijf(regel)
	return regel

# Een held raakte de schat aan, pakte niets en rende weg (Hoard-Toucher). Telt als vluchten, zonder nieuwe wrok.
func schat(naam: String) -> String:
	var h := held(naam)
	h["gevlucht"] += 1
	h["hoard_toucher"] = true
	h["bijnaam"] = _bijnaam(h)
	var regel := _regel("schat", _vars(naam), "%s touched your hoard!" % naam)
	_schrijf(regel)
	return regel

# Een held valt. buit = wat hij achterlaat; één regel met het goud erachter (Sanne, toets 2): "Kees fell to the Spike Pit. +7"
func gevallen(naam: String, waardoor: String, buit: int) -> String:
	var h := held(naam)
	h["gevallen"] += 1
	h["gevallen_door"] = waardoor   # voor de naamgenoot: at een bewoner hem, dan komt Kees II met een wrok
	var achter := " +%d" % buit
	var regel := ""
	if h["gevlucht"] > 0 and waardoor == h["wrok"]:
		# Sanne toets 6: eigen regel per soort vijand ("Bram came back. The Spike Pit won. +9"); aartsvijand apart
		var v := _vars(naam, waardoor)
		var soort := "afgerekend_aarts"
		if int(h["gevlucht"]) < 3:
			soort = "afgerekend_val" if String(v["val"]) != "" else "afgerekend_bewoner"
		regel = _regel(soort, v, "", achter)
		if regel == "":
			regel = _regel("afgerekend", v, "Grudge settled." + achter, achter)
	else:
		regel = _regel("valt", _vars(naam, waardoor), "%s fell.%s" % [naam, achter], achter)
	_schrijf(regel)
	return regel

# De ouder van een naamgenoot: "Kees II" -> "Kees", "Kees III" -> "Kees II", anders "".
static func _ouder(naam: String) -> String:
	if naam.ends_with(" III"):
		return naam.trim_suffix(" III") + " II"
	if naam.ends_with(" II"):
		return naam.trim_suffix(" II")
	return ""

# Hoedentoren (Mila, Sanne toets 3): een bewoner at naam en zet zijn hoed op. aantal = hoeden van die bewoner nu.
# Geeft een extra regel of "": bij de eerste hoed altijd, bij 25 en 100 de bijnaam, anders hooguit een op de vier
# (anders verdringt het de val-regel). Geen hoed (aantal 0; later een aartsvijand die naar de wand gaat, zodra die er is): "".
func hoed(naam: String, bewoner: String, aantal: int) -> String:
	var v := _vars(naam, bewoner)
	var regel := ""
	if aantal <= 0:
		return ""
	if aantal == 1:
		regel = _regel("hoed_eerste", v, "%s wears %s's hat now." % [v["bewoner"], naam])
	elif aantal == 25 or aantal == 100:
		v["bijnaam"] = "Hatted" if aantal == 25 else "Milliner"
		regel = _regel("hoed_bijnaam", v, "%s is now the %s." % [v["bewoner"], v["bijnaam"]])
	elif stem.rng.randf() < 0.25:
		regel = _regel("hoed", v, "")
	if regel != "":
		_schrijf(regel)
	return regel

# Met pensioen (bij openen, hooguit één per keer): geen straf, een grapje. Hij komt niet meer terug.
func pensioen(naam: String) -> String:
	var h := held(naam)
	h["pensioen"] = true
	var regel := _regel("pensioen", _vars(naam), "%s retired." % naam)
	_schrijf(regel)
	return regel

func volle_naam(naam: String) -> String:
	var b: String = held(naam)["bijnaam"]
	return naam if b == "" else "%s the %s" % [naam, b]

func laatste() -> String:
	return regels[-1] if regels.size() > 0 else ""

func _bijnaam(h: Dictionary) -> String:
	var n: int = h["gevlucht"]
	if n <= 0:
		return ""
	if bool(h.get("hoard_toucher", false)) and n < 3:
		return "Hoard-Toucher"   # Sanne: wie de schat aanraakt heet zo, tot hij aartsvijand wordt
	if n == 1:
		return "Spooked" if h["wrok"] != "" else "Lucky"
	var tel: String = TELWOORD[n] if n < TELWOORD.size() else "Ever"
	return "%s-Fled" % tel

func _schrijf(r: String) -> void:
	regels.append(r)
	if regels.size() > MAX_REGELS:
		regels.pop_front()

func naar_dict() -> Dictionary:
	return {"helden": helden, "regels": regels}

func van_dict(d: Dictionary) -> void:
	helden = d.get("helden", {})
	regels.clear()
	for r in d.get("regels", []):
		regels.append(String(r))
