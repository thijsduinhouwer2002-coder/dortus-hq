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

func _regel(soort: String, v: Dictionary, reserve: String, achter := "") -> String:
	var r: String = stem.kies(soort, v, achter)
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
func binnen(naam: String, trek := "") -> Dictionary:
	var h := held(naam)
	h["bezoeken"] += 1
	var v := _vars(naam, String(h["wrok"]))
	var regel := ""
	if h["bezoeken"] == 1 and naam.ends_with(" II"):
		v["naam"] = naam.trim_suffix(" II")
		regel = _regel("naamgenoot", v, "%s climbs in." % naam)
	elif h["bezoeken"] == 1:
		var soort := "binnen_" + trek if trek != "" and stem.rng.randf() < 0.3 else "binnen"
		regel = _regel(soort, v, "%s climbs in." % naam)
	elif int(h["gevlucht"]) >= 3:
		regel = _regel("aartsvijand", v, "%s is back." % naam)
	else:
		regel = _regel("terug", v, "%s is back." % naam)
	_schrijf(regel)
	return {"naam": naam, "bezoeken": h["bezoeken"] - 1, "wrok": h["wrok"], "bijnaam": h["bijnaam"], "littekens": h["littekens"]}

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
	var achter := " +%d" % buit
	var regel := ""
	if h["gevlucht"] > 0 and waardoor == h["wrok"]:
		regel = _regel("afgerekend", _vars(naam, waardoor), "Grudge settled." + achter, achter)
	else:
		regel = _regel("valt", _vars(naam, waardoor), "%s fell.%s" % [naam, achter], achter)
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
