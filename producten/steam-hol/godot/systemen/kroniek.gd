extends RefCounted
class_name Kroniek
# Kroniek van het hol (Bram). Onthoudt elke held: hoe vaak hij kwam, wat hem raakte, zijn wrok en bijnaam.
# Geeft één korte regel voor in de strook. Puur rekenwerk, geen nodes, zodat het te toetsen is.
# Teksten in het spel zijn Engels (winkeltaal); commentaar Nederlands.

const MAX_REGELS := 200

var helden := {}        # naam -> {bezoeken, gevlucht, gevallen, wrok, littekens, bijnaam}
var regels: Array[String] = []

const TELWOORD := ["", "Once", "Twice", "Thrice", "Four-Times", "Five-Times", "Six-Times", "Seven-Times"]

func held(naam: String) -> Dictionary:
	if not helden.has(naam):
		helden[naam] = {"bezoeken": 0, "gevlucht": 0, "gevallen": 0, "wrok": "", "littekens": 0, "bijnaam": ""}
	return helden[naam]

# Een held komt binnen. Geeft de info terug die de held meekrijgt (bezoeken, wrok, bijnaam).
func binnen(naam: String) -> Dictionary:
	var h := held(naam)
	h["bezoeken"] += 1
	var regel := ""
	if h["bezoeken"] == 1:
		regel = "%s enters the lair." % naam
	elif h["wrok"] != "":
		regel = "%s is back, still furious at %s." % [volle_naam(naam), h["wrok"]]
	else:
		regel = "%s is back." % volle_naam(naam)
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
	var regel := "%s fled%s." % [volle_naam(naam), (" from " + waardoor) if waardoor != "" else ""]
	_schrijf(regel)
	return regel

# Een held valt. buit = wat hij achterlaat.
func gevallen(naam: String, waardoor: String, buit: int) -> String:
	var h := held(naam)
	h["gevallen"] += 1
	var regel := "%s fell to %s and left %d gold." % [volle_naam(naam), waardoor, buit]
	if h["gevlucht"] > 0 and waardoor == h["wrok"]:
		regel = "%s finally fell to %s. Grudge settled, %d gold left behind." % [volle_naam(naam), waardoor, buit]
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
