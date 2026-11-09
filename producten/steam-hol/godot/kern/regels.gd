extends RefCounted
# Korte regels voor de kroniek in de strook (Olaf), uit de voorraad van Sanne (platformen/steam/kroniek-regels.md).
# Willekeurig binnen een soort, nooit twee keer dezelfde regel achter elkaar. Engels (winkeltaal).
# Vullers: {naam} voornaam, {held} naam met bijnaam, {bewoner} "Gloop", {val} "the Spike Pit", {oud} voornaam van een naamgenoot.
# Te lang na invullen (meer dan 42 tekens): dan de eerste regel van de soort die wel past (die zijn bewust kort).

const MAX := 42

const VOORRAAD := {
	"binnen": ["{naam} climbs into your hole.", "{naam} is here for your gold.", "{naam} brought a torch. And hope.",
		"{naam} read about you in a tavern.", "{naam} has a map. It is wrong.", "{naam} knocks first. Polite.",
		"{naam} says this is a quick one."],
	"naamgenoot": ["{naam} climbs in. Family business.", "{naam}. {oud} fell here once.", "{naam} wants dad's boot back."],
	"terug": ["{held} is back.", "{naam} came back. Bigger sword.", "{naam} is back. Still limping."],
	"terug_bewoner": ["{naam} is back for {bewoner}.", "{held} is back. Grudge: {bewoner}", "{naam} wrote a song about {bewoner}."],
	"terug_val": ["{naam} remembers {val}.", "{naam} is back for {val}.", "{naam} limps back to {val}."],
	"aartsvijand": ["Your nemesis {naam} has arrived.", "{naam} again. Of course.", "{naam} trained all week for this."],
	"val": ["{naam} fell to {val}.", "{naam} found {val}. Hard.", "{naam} stays forever.", "{naam} left gold and one boot.",
		"{naam} will not be leaving."],
	"val_bewoner": ["{bewoner} ate {naam}. Burp.", "{bewoner} says thanks for the snack.", "{naam} stays forever."],
	# "{naam}'s hat goes on the wall." komt pas terug als de wand te zien is (Sanne toets 4, punt 1)
	"afgerekend": ["Grudge settled. {naam} rests.", "{naam} came back once too often."],
	"afgerekend_aarts": ["Nemesis {naam}: finally stays.", "Grudge settled. {naam} rests."],
	"vlucht": ["{naam} fled. Grudge: {bewoner}.", "{naam} ran. Swore revenge.", "{naam} escaped with a limp.",
		"{naam} left. Took nothing. Angry.", "{naam} fled, crying a little."],
	"schat": ["{naam} touched your hoard!", "{naam} tried to lift it. Too heavy.", "{naam} licked a coin and ran.",
		"{naam} is now the Hoard-Toucher."],
	# bij het wegrennen van de Hoard-Toucher (toets 5, punt 4); de aanraak-regel kwam al op het moment zelf
	"schat_weg": ["{naam} the Hoard-Toucher ran.", "{naam} ran. Hands smell of gold.", "{naam} ran off, giggling."],
	"plat": ["{bewoner} is flat. Back soon."],
	"op": ["{bewoner} is up again. Wobbly."],
	# hoedentoren (Mila, kroniek-regels.md): bij de eerste hoed altijd "hoed_eerste", daarna hooguit een op de vier
	"hoed_eerste": ["{bewoner} wears {naam}'s hat now."],
	"hoed": ["{bewoner} tries on {naam}'s hat. Fits.", "{bewoner} adds {naam}'s hat to the pile.",
		"{bewoner}'s hat pile is taller than him."],
	"hoed_klein": ["{bewoner} tries on {naam}'s hat. Fits.", "{bewoner} adds {naam}'s hat to the pile."],
	"hoed_bijnaam": ["{bewoner} is now known as the {bijnaam}."],
}

var rng: RandomNumberGenerator
var vorige := {}   # soort -> indexen die deze ronde al geweest zijn (schudzak)

func vul(r: String, w: Dictionary) -> String:
	for k in w:
		r = r.replace("{%s}" % k, String(w[k]))
	return r

# Schudzak per soort (Sanne toets 5, punt 3: dezelfde grap twee keer in een minuut): elke regel van een soort komt een
# keer voor de zak weer vol is, en nooit twee keer achter elkaar (ook niet over de grens van de zak heen). Past er niets
# uit de zak binnen 42 tekens, dan een andere die past, en anders de eerste (die zijn bewust kort).
var vorig := {}    # soort -> laatst gekozen index

func kies(soort: String, w: Dictionary, erbij := 0) -> String:
	var lijst: Array = VOORRAAD.get(soort, ["..."])
	if rng == null:
		rng = RandomNumberGenerator.new()
	var geweest: Array = vorige.get(soort, [])
	if geweest.size() >= lijst.size():
		geweest = []
	var passen: Array = []
	var keuzes: Array = []
	for i in lijst.size():
		if vul(lijst[i], w).length() > MAX - erbij:
			continue
		passen.append(i)
		if not geweest.has(i) and (lijst.size() == 1 or i != int(vorig.get(soort, -1))):
			keuzes.append(i)
	if keuzes.is_empty():
		keuzes = passen
	var i: int = keuzes[rng.randi_range(0, keuzes.size() - 1)] if not keuzes.is_empty() else 0
	if not geweest.has(i):
		geweest.append(i)
	vorige[soort] = geweest
	vorig[soort] = i
	return vul(lijst[i], w)
