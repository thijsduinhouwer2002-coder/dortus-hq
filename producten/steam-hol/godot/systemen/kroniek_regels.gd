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
	"hoed_eerste": ["{bewoner} wears {naam}'s hat now."],
	"hoed": ["{bewoner} tries on {naam}'s hat. Fits.", "{bewoner} adds {naam}'s hat to the pile.",
		"{bewoner}'s hat pile is taller than him."],
	"naamgenoot_hoed": ["{naam} wants dad's hat back.", "{naam} glares at the hat pile.",
		"{naam} can't find it. Too many hats."],
	"hoed_bijnaam": ["{bewoner} is now known as the {bijnaam}."],
	# Sanne 9 nov 21:50: "hat goes on the wall" pas terug voor aartsvijanden als de wand te zien is;
	# aartsvijanden (3 keer gevlucht) krijgen een eigen lijst, zoals afgerekend_aarts in kern/regels.gd.
	"afgerekend": ["Grudge settled. {naam} rests.", "{bewoner} wins. {naam} is done."],
	"afgerekend_aarts": ["Nemesis {naam}: finally stays.", "Grudge settled. Nemesis {naam} rests."],
}

var rng := RandomNumberGenerator.new()
var vorige := {}       # soort -> laatst gekozen regels (sjablonen), nieuwste achteraan
const GEHEUGEN := 4    # Sanne toets 3 punt 3: per soort de laatste 4 regels overslaan ("knocks first. Polite." kwam twee keer in 15 s)

func _init(zaad := 0) -> void:
	rng.seed = zaad if zaad != 0 else hash("kroniek")

# "Gloop the Slime" -> "Gloop" (Sanne: nooit de lange naam, anders past het niet).
static func korte_bewoner(naam: String) -> String:
	var i := naam.find(" the ")
	return naam.substr(0, i) if i > 0 else naam

static func vul(sjabloon: String, v: Dictionary) -> String:
	var r := sjabloon
	for sleutel in ["held", "naam", "bewoner", "val", "n", "bijnaam"]:
		r = r.replace("{%s}" % sleutel, str(v.get(sleutel, "")))
	return r

# Noemt deze regel de wrok of de bijnaam? (Sanne toets 3 punt 6: een terugkomer zegt altijd waarom)
static func noemt_waarom(s: String, v: Dictionary) -> bool:
	if s.contains("{bewoner}") or s.contains("{val}"):
		return true
	return s.contains("{held}") and String(v.get("held", "")) != String(v.get("naam", ""))

# Kies een regel uit een soort. v: naam, held, bewoner, val, n. achter: wordt erachter geplakt (" +7").
# moet_noemen: alleen regels die de wrok of bijnaam noemen (als die er zijn).
# Valt alles af (te lang, of de soort past niet), dan "" en kiest de beller iets anders.
func kies(soort: String, v: Dictionary, achter := "", moet_noemen := false) -> String:
	var kandidaten: Array[String] = []
	for s in VOORRAAD.get(soort, []):
		if s.contains("{bewoner}") and String(v.get("bewoner", "")) == "":
			continue
		if s.contains("{val}") and String(v.get("val", "")) == "":
			continue
		if (vul(s, v) + achter).length() > MAX:
			continue
		kandidaten.append(s)
	if moet_noemen:
		var noemers: Array[String] = []
		for s in kandidaten:
			if noemt_waarom(s, v):
				noemers.append(s)
		kandidaten = noemers   # niets past dat waarom noemt: "" en de beller neemt zijn reserve (met volle naam)
	# de laatste regels van deze soort overslaan, maar er blijft er altijd minstens één over
	var geweest: Array = vorige.get(soort, [])
	var over: Array[String] = []
	for n in range(mini(GEHEUGEN, geweest.size()), -1, -1):
		over.clear()
		var recent: Array = geweest.slice(geweest.size() - n) if n > 0 else []
		for s in kandidaten:
			if not recent.has(s):
				over.append(s)
		if not over.is_empty():
			break
	if over.is_empty():
		return ""
	var gekozen: String = over[rng.randi_range(0, over.size() - 1)]
	geweest.append(gekozen)
	if geweest.size() > GEHEUGEN:
		geweest.pop_front()
	vorige[soort] = geweest
	return vul(gekozen, v) + achter
