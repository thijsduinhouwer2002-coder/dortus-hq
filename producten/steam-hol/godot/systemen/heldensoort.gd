extends RefCounted
# Heldensoorten (Bram, 10 nov). Versie 1 van features.md (Sanne): ridder, dief, magiër en bard, zodat het niet
# na 3 dagen op is. Olaf 10 nov 01:40: alles van [v1] komt vóór het fest (14 jan).
# Elke soort voelt anders in de strook, niet alleen een getal:
#   ridder:  sterk en traag. Loopt langzamer, vlucht pas na twee klappen (ook als hij schijterig is). Zwaar harnas: past niet in
#            Gloops mond (slijm 0,7) maar zakt door elke vloer (put 1,4). Zo heeft elke soort een eigen zwakte (Sanne 10 nov 03:05).
#   dief:    snel en glad. Ontwijkt de put vaak (springt erover), Gloop is zijn zwakke plek.
#   magiër:  ziet vallen. De put krijgt hem bijna nooit, maar tegen Gloop helpt geen spreuk.
#   bard:    zwak, maar vlucht hij, dan zingt hij een lied over je hol en komen er meer helden (info "lied").
# Leeg ("") is de held zoals hij al was: zonder soort verandert er niets, dus de demo en oude saves blijven gelijk.
#
# Gebruik in held.gd: info["soort_held"] (zo heet het, want "soort" is in held.gd al de soort val of bewoner).
# Kiezen moet strook.gd (Olaf) nog doen met kies(nr, r), gevraagd in taken.md; tot dan komt er geen soort in het spel: de eerste 10 helden van een nieuw spel zijn gewoon (de eerste tien
# minuten blijven zoals Sanne ze schreef), daarna af en toe een soort. Een terugkomer houdt zijn soort (in de kroniek).
#
# Getallen: ridder en bard van Sanne (balans.md, 10 nov 03:05), de rest een begin (GOK), nagerekend in sim/sim.py (python3 sim.py soorten): de doelen moeten blijven
# gelden (±1 op 3 vlucht, zie sim/UITKOMST.md). Sanne mag ze bijstellen in balans.md.

const SOORTEN := ["ridder", "dief", "magier", "bard"]

# kans_x: factor op de kans dat hij valt, per verdediging. snel: factor op lopen en klimmen.
# taai: vlucht pas na twee klappen. wapen: plaatje in held_wapens.png (0 zwaard, 1 staf, 2 fakkel), -1 = zoals nu.
const DATA := {
	"ridder": {"snel": 0.75, "kans_x": {"slijm": 0.7, "stekelput": 1.4}, "taai": true, "wapen": 0,
		"naam": "Knight", "uitleg": "Heavy armor. Too big for Gloop. Pits love him."},
	"dief": {"snel": 1.3, "kans_x": {"slijm": 1.15, "stekelput": 0.5}, "taai": false, "wapen": -1,
		"naam": "Thief", "uitleg": "Quick. Pits rarely catch him. Hates slime."},
	"magier": {"snel": 1.0, "kans_x": {"slijm": 1.25, "stekelput": 0.3}, "taai": false, "wapen": 1,
		"naam": "Wizard", "uitleg": "Sees traps. No spell works on Gloop."},
	"bard": {"snel": 1.0, "kans_x": {"slijm": 1.1, "stekelput": 1.1}, "taai": false, "wapen": -1,
		"naam": "Bard", "uitleg": "Weak. If he escapes, he sings about you."},
}

# Wegingen na de eerste 10 helden: gewoon blijft de meeste (zo blijft de wrok-grap het hart), een bard is zeldzaam.
const KIES_GEWICHT := {"": 55, "ridder": 15, "dief": 15, "magier": 10, "bard": 5}
const EERSTE_GEWOON := 10
const LIED_HELDEN := 2        # zoveel helden extra na een lied (strook.gd laat ze binnen de volgende minuut komen)

static func geldig(s: String) -> bool:
	return DATA.has(s)

static func kies(nr: int, r: RandomNumberGenerator) -> String:
	if nr <= EERSTE_GEWOON:
		return ""
	var totaal := 0
	for k in KIES_GEWICHT:
		totaal += int(KIES_GEWICHT[k])
	var x := r.randi_range(1, totaal)
	for k in KIES_GEWICHT:
		x -= int(KIES_GEWICHT[k])
		if x <= 0:
			return String(k)
	return ""

# Trick Lid (stap 3 van de put) ziet eruit als vloer: wie vallen ziet, ziet deze niet (idee Sanne 10 nov 03:10).
# De magier gaat van 0,3 naar 1,0 voor de put; zo heeft de put een echte tegenzet voor hem.
# Gemeten met sim.py (TRICK_MAGIER = 1.0, 8 zaden, 10 uur, GEZIEN): magier met Trick Lid in de put 10,6% wordt 19,3%,
# vluchten van de magier 27,9% wordt 22,2%, vluchten van alle helden 35,1% wordt 34,8%.
const VERBORGEN_X := {"magier": 1.0}

static func kans_factor(s: String, verdediging: String, verborgen := false) -> float:
	if not DATA.has(s):
		return 1.0
	if verborgen and verdediging == "stekelput" and VERBORGEN_X.has(s):
		return float(VERBORGEN_X[s])
	return float(DATA[s]["kans_x"].get(verdediging, 1.0))

static func snel(s: String) -> float:
	return float(DATA[s]["snel"]) if DATA.has(s) else 1.0

static func taai(s: String) -> bool:
	return DATA.has(s) and bool(DATA[s]["taai"])

static func wapen(s: String) -> int:
	return int(DATA[s]["wapen"]) if DATA.has(s) else -1

static func naam(s: String) -> String:
	return String(DATA[s]["naam"]) if DATA.has(s) else ""

static func zingt(s: String) -> bool:
	return s == "bard"

# Karaktertrekken erbij (versie 1, features.md: zes in totaal). hebzuchtig en schijterig kiest held.gd zelf (op naam);
# de drie hieronder geeft strook.gd mee als info["trek"], na de eerste 10 helden en dan 1 op 5:
#   slaapkop:     doet halverwege een dutje in je hol (4 s stil met zzz), een makkelijk doel voor wie wakker is.
#   wraakzuchtig: tegen zijn eigen vijand dubbel roekeloos (de wrok-grap krijgt vaker een afloop).
#   opschepper:   loopt langzaam en pocht (alleen in de kroniek); rent pas na twee klappen, net als hebzuchtig.
# "verdwaald" uit features.md komt later: in één rij gangen is "de verkeerde gang" nog niet te zien.
const TREKKEN_NIEUW := ["slaapkop", "wraakzuchtig", "opschepper"]
const TREK_KANS := 0.2
const DUT_S := 4.0

static func kies_trek(nr: int, r: RandomNumberGenerator) -> String:
	if nr <= EERSTE_GEWOON or r.randf() >= TREK_KANS:
		return ""
	return TREKKEN_NIEUW[r.randi_range(0, TREKKEN_NIEUW.size() - 1)]
