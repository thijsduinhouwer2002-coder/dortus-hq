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
	# {naam} is de volle naam ("Kees II"), {oud} de voornaam van wie hier viel ("Kees"); zo ook in kern/strook.gd
	"naamgenoot": ["{naam} climbs in. Family business.", "{naam}. {oud} fell here once.", "{naam} wants dad's boot back."],
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
	# Soorten die kern/strook.gd (Olaf) gebruikt; zo is dit de enige voorraad (Olaf 22:35, controleur punt 4).
	"terug_bewoner": ["{naam} is back for {bewoner}.", "{held} is back. Grudge: {bewoner}", "{naam} wrote a song about {bewoner}."],
	"terug_val": ["{naam} remembers {val}.", "{naam} is back for {val}.", "{naam} limps back to {val}."],
	"val": ["{naam} fell to {val}.", "{naam} found {val}. Hard.", "{naam} stays forever.", "{naam} left gold and one boot.",
		"{naam} will not be leaving."],
	"val_bewoner": ["{bewoner} ate {naam}. Burp.", "{bewoner} says thanks for the snack.", "{naam} stays forever."],
	"plat": ["{bewoner} is flat. Back soon."],
	"op": ["{bewoner} is up again. Wobbly."],
	"hoed_klein": ["{bewoner} tries on {naam}'s hat. Fits.", "{bewoner} adds {naam}'s hat to the pile."],
}

var rng := RandomNumberGenerator.new()
var vorige := {}       # soort -> laatst gekozen regels (sjablonen), nieuwste achteraan
const GEHEUGEN := 4    # Sanne toets 3 punt 3: per soort de laatste 4 regels overslaan ("knocks first. Polite." kwam twee keer in 15 s)
# Sanne toets 5 punt 2: geen regel die in de laatste 10 regels van de kroniek al stond, over alle soorten heen
# ("read about you in a tavern" kwam bij Ties en Lotte in dezelfde minuut). Valt dan alles af, dan alleen per soort.
const GEHEUGEN_ALLES := 10
var laatste_alles: Array[String] = []   # laatste gekozen sjablonen van alle soorten, nieuwste achteraan

# Hoeveel regels van deze soort onthouden worden: minstens 4, en bij een grote soort alles op één na, zodat een regel
# pas terugkomt als de andere allemaal geweest zijn (Sanne toets 5: in de demo-minuut geen binnenkom-regel twee keer).
func geheugen(soort: String) -> int:
	var lijst: Array = VOORRAAD.get(soort, [])
	return maxi(GEHEUGEN, lijst.size() - 1)

func _init(zaad := 0) -> void:
	rng.seed = zaad if zaad != 0 else hash("kroniek")

# "Gloop the Slime" -> "Gloop" (Sanne: nooit de lange naam, anders past het niet).
static func korte_bewoner(naam: String) -> String:
	var i := naam.find(" the ")
	return naam.substr(0, i) if i > 0 else naam

static func vul(sjabloon: String, v: Dictionary) -> String:
	var r := sjabloon
	for sleutel in ["held", "naam", "bewoner", "val", "n", "bijnaam", "oud"]:
		r = r.replace("{%s}" % sleutel, str(v.get(sleutel, "")))
	return r

# Noemt deze regel de wrok of de bijnaam? (Sanne toets 3 punt 6: een terugkomer zegt altijd waarom)
static func noemt_waarom(s: String, v: Dictionary) -> bool:
	if s.contains("{bewoner}") or s.contains("{val}"):
		return true
	return s.contains("{held}") and String(v.get("held", "")) != String(v.get("naam", ""))

# Kies een regel uit een soort. v: naam, held, bewoner, val, n, oud. achter: wordt erachter geplakt (" +7").
# moet_noemen: alleen regels die de wrok of bijnaam noemen (als die er zijn).
# Valt alles af (te lang, of de soort past niet), dan "" en kiest de beller iets anders.
# Voor kern/strook.gd mag achter ook een getal zijn (zoals in Olafs oude regels.gd): zoveel tekens houdt de regel vrij,
# er wordt niets achter geplakt, en er komt nooit "" terug (dan de kortste regel van de soort die past).
func kies(soort: String, v: Dictionary, achter = "", moet_noemen := false) -> String:
	var vrij: int = int(achter) if typeof(achter) == TYPE_INT else String(achter).length()
	var plak: String = "" if typeof(achter) == TYPE_INT else String(achter)
	var passend: Array[String] = []    # velden zijn er, lengte telt nog niet
	var kandidaten: Array[String] = []
	for s in VOORRAAD.get(soort, []):
		if s.contains("{bewoner}") and String(v.get("bewoner", "")) == "":
			continue
		if s.contains("{val}") and String(v.get("val", "")) == "":
			continue
		passend.append(s)
		if vul(s, v).length() + vrij > MAX:
			continue
		kandidaten.append(s)
	if moet_noemen:
		var noemers: Array[String] = []
		for s in kandidaten:
			if noemt_waarom(s, v):
				noemers.append(s)
		kandidaten = noemers   # niets past dat waarom noemt: "" en de beller neemt zijn reserve (met volle naam)
	# eerst: niets uit de laatste 10 van de kroniek en niets uit de laatste 4 van deze soort
	var geweest: Array = vorige.get(soort, [])
	var over: Array[String] = []
	for s in kandidaten:
		if not laatste_alles.has(s) and not geweest.has(s):
			over.append(s)
	# anders: de laatste regels van deze soort overslaan, maar er blijft er altijd minstens één over
	if over.is_empty():
		for n in range(mini(geheugen(soort), geweest.size()), -1, -1):
			over.clear()
			var recent: Array = geweest.slice(geweest.size() - n) if n > 0 else []
			for s in kandidaten:
				if not recent.has(s):
					over.append(s)
			if not over.is_empty():
				break
	if over.is_empty():
		if typeof(achter) != TYPE_INT or passend.is_empty():
			return "" if typeof(achter) != TYPE_INT else "..."
		var kort: String = passend[0]
		for s in passend:
			if vul(s, v).length() < vul(kort, v).length():
				kort = s
		over.append(kort)
	var gekozen: String = over[rng.randi_range(0, over.size() - 1)]
	geweest.append(gekozen)
	if geweest.size() > geheugen(soort):
		geweest.pop_front()
	vorige[soort] = geweest
	laatste_alles.append(gekozen)
	if laatste_alles.size() > GEHEUGEN_ALLES:
		laatste_alles.pop_front()
	return vul(gekozen, v) + plak
