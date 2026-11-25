extends SceneTree
# Toetsen voor de aanloop naar een val (Olaf 25 nov, issue #25, keuring Iris build 46cdec1: "laat een held die de val
# nadert binnen 2 s kiezen: vallen of springen"). Draaien: godot --headless --path <godot-map> -s systemen/toetsen/toets_aanloop.gd
var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[aanloop-toets] OK ", wat)
	else:
		fout += 1
		print("[aanloop-toets] FOUT ", wat)

# Eén held door een nep-hol met een put op kolom 9 (en Gloop op 6 als met_slijm). Meet per val: tijd van "binnen 24 px"
# tot de keuze (vallen of springen), of hij binnen 64 px rondkeek, en of hij er ooit gewoon overheen liep.
func loop_een(info: Dictionary, met_slijm: bool) -> Dictionary:
	var hol := Node2D.new()
	hol.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	hol.schat_kol = 14
	hol.vallen[9] = "stekelput"
	var wezens := Node2D.new()
	hol.add_child(wezens)
	if met_slijm:
		var sl := Node2D.new()
		sl.set_script(load("res://systemen/slijm.gd"))
		sl.met_3d = false
		wezens.add_child(sl)
		sl.zet(hol, 6)
	var h := Node2D.new()
	h.set_script(load("res://systemen/held.gd"))
	wezens.add_child(h)
	h.start(hol, info)
	var rand_x: float = 9 * 16.0                 # linkerrand van de putkolom
	var nadert_t := -1.0
	var keuze_t := -1.0
	var keek_dichtbij := false
	var overgelopen := false
	var keek_ooit := false
	var n := 0
	while h.staat != "weg" and n < 6000 and is_instance_valid(h):
		h.stap(1.0 / 20.0)
		n += 1
		if h.staat == "weg":
			break
		var pose: String = h.HELD_LOOP.pose(h)
		if pose == "kijk":
			keek_ooit = true
		if h.staat == "lopen" and h.position.x < rand_x:
			var afst: float = rand_x - h.position.x
			if afst < 24.0 and nadert_t < 0.0:
				nadert_t = h.t
			if afst < 64.0 and pose == "kijk":
				keek_dichtbij = true
		if keuze_t < 0.0 and (h.staat == "vallen" or float(h.spring_t) >= 0.0) and h.gezien.has(9):
			keuze_t = h.t
		# over de put zonder vallen of springen: in de putkolom staan in lopen terwijl hij niet sprong
		if h.staat == "lopen" and float(h.spring_t) < 0.0 and hol.pos_naar_cel(h.position).x == 9 and keuze_t < 0.0:
			overgelopen = true
	var r := {"duur": (keuze_t - nadert_t) if (keuze_t >= 0.0 and nadert_t >= 0.0) else -1.0, "keuze": keuze_t >= 0.0,
		"keek_dichtbij": keek_dichtbij, "overgelopen": overgelopen, "keek_ooit": keek_ooit, "nadert": nadert_t >= 0.0}
	hol.free()
	return r

func _init() -> void:
	var langst := {}
	var alle_ok := true
	var geen_kijk := true
	var nooit_over := true
	var keuzes := 0
	for soort in ["", "ridder", "dief", "magier", "bard"]:
		langst[soort] = 0.0
		for z in 12:
			var info := {"naam": "Aan%s%d" % [soort, z], "trek": "hebzuchtig", "soort_held": soort, "zaad": 500 + z, "moet_doorlopen": z % 3 == 0}
			var r := loop_een(info, z % 2 == 1)
			if not r.nadert:
				continue   # Gloop at hem voor de put: geen aanloop te meten
			if not r.keuze:
				alle_ok = false
				print("[aanloop-toets] geen keuze: %s zaad %d" % [soort, z])
				continue
			keuzes += 1
			langst[soort] = maxf(float(langst[soort]), float(r.duur))
			if float(r.duur) > 2.0:
				alle_ok = false
			if r.keek_dichtbij:
				geen_kijk = false
			if r.overgelopen:
				nooit_over = false
	print("[aanloop-toets] langste tijd van 24 px voor de put tot de keuze, per soort (s): %s" % str(langst))
	ok(keuzes >= 30, "genoeg helden kwamen bij de put (%d)" % keuzes)
	ok(alle_ok, "elke held die de put nadert valt of springt binnen 2 s (Iris #25)")
	ok(geen_kijk, "binnen 64 px voor een val kijkt niemand rond (geen dralen)")
	ok(nooit_over, "geen enkele held loopt over de put zonder te vallen of te springen")
	# een held met een wrok kijkt nooit rond; een gewone held wel (elke 3 tot 6 s)
	var boos := loop_een({"naam": "Boos", "trek": "hebzuchtig", "wrok": "the Spike Pit", "zaad": 7, "moet_afgerekend": true}, false)
	ok(not boos.keek_ooit, "held met een wrok kijkt niet rond: hij weet waar hij heen wil")
	var eerste := loop_een({"naam": "Eerst", "trek": "hebzuchtig", "moet_vallen": true, "zaad": 8, "snelheid": 2.0}, false)
	ok(not eerste.keek_ooit and eerste.keuze, "eerste held van een vers spel kijkt niet rond en valt")
	# aanloop: zelfde beelden sneller, dus per beeldwissel nog steeds stap_px (voeten glijden niet)
	var hol := Node2D.new()
	hol.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	var h := Node2D.new()
	h.set_script(load("res://systemen/held.gd"))
	hol.add_child(h)
	h.start(hol, {"naam": "Fps", "trek": "hebzuchtig"})
	var gewoon: int = h.HELD_LOOP.wissels(h, 1.0, false)
	h.loop_klok = 0.0
	var snel: int = h.HELD_LOOP.wissels(h, 1.0, false, true)
	ok(snel > gewoon and snel <= int(h.HELD_LOOP.AANLOOP_FPS), "aanloop: meer beelden per seconde (%d tegen %d), hooguit %d" % [snel, gewoon, int(h.HELD_LOOP.AANLOOP_FPS)])
	hol.free()
	print("[aanloop-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
