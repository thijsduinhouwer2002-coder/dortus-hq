extends RefCounted
# (geen class_name: kroniek.gd laadt dit met preload, dan werkt het ook zonder import-cache)
# Voorraad kroniekregels van Sanne (platformen/steam/kroniek-regels.md), en de keuze daaruit (Bram).
# Afspraken van Sanne: hooguit 42 tekens na invullen, {bewoner} = "Gloop" (kort), {val} = "the Spike Pit",
# willekeurig binnen een soort maar niet twee keer dezelfde regel achter elkaar, nooit iets naar de speler toe.
# Een regel met {bewoner} komt alleen als het om een bewoner gaat, een regel met {val} alleen bij een val.

const MAX := 42

const VOORRAAD := {
	"binnen": ["{naam} climbs into your hole.", "{naam} is here for your gold.", "{naam} brought a torch. And hope.",
		"{naam} read about you in a tavern.", "{naam} has a map. It is wrong.", "{naam} knocks first. Polite.",
		"{naam} says this is a quick one."],
	"binnen_hebzuchtig": ["{naam} the Greedy smells gold."],
	"binnen_schijterig": ["{naam} the Timid peeks in."],
	"terug": ["{held} is back.", "{held} is back. Grudge: {bewoner}", "{naam} is back for {bewoner}.",
		"{naam} came back. Bigger sword.", "{naam} remembers {val}.", "{naam} is back. Still limping."],
	"aartsvijand": ["Your nemesis {naam} has arrived.", "{naam} again. Of course.", "{naam} trained all week for this."],
	"valt": ["{naam} fell to {val}.", "{naam} stays forever.", "{naam} found {val}. Hard.", "{bewoner} ate {naam}. Burp.",
		"{naam} left gold and one boot.", "{naam} will not be leaving.", "{bewoner} says thanks for the snack."],
	"naamgenoot": ["{naam} II climbs in. Family business.", "{naam} II. {naam} fell here once.",
		"{naam} II wants his dad's boot back."],
	"pensioen": ["{naam} retired. Opened a bakery.", "{naam} retired. Tells tall tales now.",
		"{naam} quit heroing. Sells maps.", "{naam} won't be back. Too scared."],
	"vlucht": ["{naam} fled. Grudge: {bewoner}.", "{naam} ran. Swore revenge.", "{naam} escaped with a limp.",
		"{naam} fled, crying a little."],
	"vlucht_zonder": ["{naam} left. Took nothing. Angry.", "{naam} ran. Swore revenge.", "{naam} fled, crying a little."],
	"schat": ["{naam} touched your hoard!", "{naam} tried to lift it. Too heavy.", "{naam} licked a coin and ran.",
		"{naam} is now the Hoard-Toucher."],
	"afgerekend": ["Grudge settled. {naam} rests.", "{bewoner} wins. {naam} is done.", "{naam}'s hat goes on the wall.",
		"Nemesis {naam}: finally stays."],
}

var rng := RandomNumberGenerator.new()
var vorige := {}       # soort -> laatst gekozen regel (sjabloon)

func _init(zaad := 0) -> void:
	rng.seed = zaad if zaad != 0 else hash("kroniek")

# "Gloop the Slime" -> "Gloop" (Sanne: nooit de lange naam, anders past het niet).
static func korte_bewoner(naam: String) -> String:
	var i := naam.find(" the ")
	return naam.substr(0, i) if i > 0 else naam

static func vul(sjabloon: String, v: Dictionary) -> String:
	var r := sjabloon
	for sleutel in ["held", "naam", "bewoner", "val", "n"]:
		r = r.replace("{%s}" % sleutel, str(v.get(sleutel, "")))
	return r

# Kies een regel uit een soort. v: naam, held, bewoner, val, n. achter: wordt erachter geplakt (" +7").
# Valt alles af (te lang, of de soort past niet), dan "" en kiest de beller iets anders.
func kies(soort: String, v: Dictionary, achter := "") -> String:
	var kandidaten: Array[String] = []
	for s in VOORRAAD.get(soort, []):
		if s.contains("{bewoner}") and String(v.get("bewoner", "")) == "":
			continue
		if s.contains("{val}") and String(v.get("val", "")) == "":
			continue
		if (vul(s, v) + achter).length() > MAX:
			continue
		kandidaten.append(s)
	if kandidaten.size() > 1 and vorige.has(soort):
		kandidaten.erase(vorige[soort])
	if kandidaten.is_empty():
		return ""
	var gekozen: String = kandidaten[rng.randi_range(0, kandidaten.size() - 1)]
	vorige[soort] = gekozen
	return vul(gekozen, v) + achter
