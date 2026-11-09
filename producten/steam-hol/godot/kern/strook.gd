extends Node2D
# Kern van Het Hol (Olaf): de strook boven de taakbalk.
# - hoogte instelbaar (standaard 120 px, 96 tot 160), over de hele breedte, net boven de taakbalk
# - alleen de strook vangt klikken, de rest laat ze door
# - zuinig: 15 fps en alleen tekenen wat beweegt (proef 9 nov: stil beeld kost bijna niets)
# - geen kaartjes over andere vensters: alle tekst staat klein in de strook
# Argumenten na "--": hoogte=120 duur=60 log=<pad> demo=1 film=1 vers=1

const HOL := preload("res://hol/hol.gd")
const TEKST := preload("res://kern/tekst.gd")
const SLIJM := preload("res://kern/standin_slijm.gd")
const OPSLAG := "user://hol.json"

const NAMEN := ["Bram", "Odo", "Wil", "Gerda", "Pim", "Rik", "Mara", "Joost", "Fenna", "Ties", "Lotte", "Kees"]
const KLEUREN := ["#3f6fb5", "#8a4fb0", "#3f9a6a", "#c07a2a", "#6a6a7a", "#b0404a"]
const HOEDEN := ["#b33a3a", "#e0b040", "#2a5aa0", "#3a7a3a", "#7a3a8a", "#d06a2a"]

var hoogte := 120
var schaal := 3
var duur := 0.0
var logpad := ""
var demo := false
var film := false
var vers := false

var hol
var wezens: Node2D
var tekst
var rng := RandomNumberGenerator.new()
var t := 0.0
var volgende_held := 4.0
var volgende_graaf := 9.0
var volgende_opslag := 30.0
var kroniek: Array[String] = []
var terugkomers: Array = []   # ontsnapte helden die terugkomen
var held_script

func log_regel(tekst_: String) -> void:
	print(tekst_)
	if logpad != "":
		var f := FileAccess.open(logpad, FileAccess.READ_WRITE if FileAccess.file_exists(logpad) else FileAccess.WRITE)
		if f:
			f.seek_end()
			f.store_line(tekst_)
			f.close()

func _ready() -> void:
	for a in OS.get_cmdline_user_args():
		var kv := a.split("=", true, 1)
		if kv.size() < 2:
			continue
		match kv[0]:
			"hoogte": hoogte = clampi(int(kv[1]), 96, 160)
			"duur": duur = float(kv[1])
			"log": logpad = kv[1]
			"demo": demo = kv[1] == "1"
			"film": film = kv[1] == "1"
			"vers": vers = kv[1] == "1"
	rng.seed = 7 if demo else int(Time.get_unix_time_from_system())
	if not film:
		Engine.max_fps = 15
		OS.low_processor_usage_mode = true
	get_viewport().transparent_bg = true
	# Brams held als die er is, anders de stand-in
	held_script = load("res://systemen/held.gd") if ResourceLoader.exists("res://systemen/held.gd") else load("res://kern/standin_held.gd")

	var scherm := DisplayServer.screen_get_usable_rect()  # zonder taakbalk
	schaal = maxi(2, int(round(hoogte / 40.0)))
	var spel_h := int(hoogte / schaal)
	DisplayServer.window_set_size(Vector2i(scherm.size.x, hoogte))
	DisplayServer.window_set_position(Vector2i(scherm.position.x, scherm.position.y + scherm.size.y - hoogte))
	var boven := (spel_h - HOL.H) * schaal   # lege (doorzichtige) rand bovenaan bij 96 px
	DisplayServer.window_set_mouse_passthrough(PackedVector2Array([
		Vector2(0, boven), Vector2(scherm.size.x, boven), Vector2(scherm.size.x, hoogte), Vector2(0, hoogte)]))

	hol = Node2D.new()
	hol.set_script(HOL)
	hol.name = "Hol"
	hol.scale = Vector2(schaal, schaal)
	hol.position = Vector2(0, boven)
	add_child(hol)
	hol.maak(int(scherm.size.x / schaal))
	wezens = Node2D.new()
	wezens.name = "Wezens"
	hol.add_child(wezens)
	var slijm := Node2D.new()
	slijm.set_script(SLIJM)
	wezens.add_child(slijm)
	slijm.zet(hol, 10)

	tekst = Node2D.new()
	tekst.set_script(TEKST)
	tekst.breedte = scherm.size.x
	tekst.hoogte = hoogte
	add_child(tekst)

	if not vers:
		laad()
	if kroniek.is_empty():
		_kroniek("Your hole is open. Heroes will come.")
	hol.gegraven.connect(func(cel): log_regel("HOL gegraven kolom %d" % cel.x))
	log_regel("HOL start hoogte=%d schaal=%d spelpixels=%dx%d venster=%s pos=%s held=%s" % [hoogte, schaal,
		int(scherm.size.x / schaal), spel_h, DisplayServer.window_get_size(), DisplayServer.window_get_position(), held_script.resource_path])

func _kroniek(r: String) -> void:
	kroniek.append(r)
	if kroniek.size() > 40:
		kroniek.remove_at(0)
	tekst.zet(kroniek, hol.goud)
	log_regel("HOL kroniek: " + r)

func _bijnaam(n: int) -> String:
	match n:
		1: return "the Once-Fled"
		2: return "the Twice-Fled"
		3: return "the Thrice-Fled"
	return "the %d-Times-Fled" % n

func _nieuwe_held() -> void:
	var info := {}
	if not terugkomers.is_empty() and rng.randf() < 0.5:
		info = terugkomers.pop_at(rng.randi_range(0, terugkomers.size() - 1))
		_kroniek("%s %s is back. Grudge: %s." % [info.naam, _bijnaam(int(info.bezoeken)), info.wrok])
	else:
		info = {"naam": NAMEN[rng.randi_range(0, NAMEN.size() - 1)], "bezoeken": 0, "wrok": "",
			"kleur": KLEUREN[rng.randi_range(0, KLEUREN.size() - 1)], "hoed": HOEDEN[rng.randi_range(0, HOEDEN.size() - 1)],
			"taai": rng.randi_range(0, 1)}
		_kroniek("%s the hero climbs into your hole." % info.naam)
	var d := info.duplicate()
	d["kleur"] = Color(info.kleur)
	d["hoed"] = Color(info.hoed)
	var held := Node2D.new()
	held.set_script(held_script)
	wezens.add_child(held)
	held.klaar.connect(_held_klaar)
	held.start(hol, d)

func _held_klaar(_held, uitkomst: String, info: Dictionary) -> void:
	var bewaar := info.duplicate()
	bewaar["kleur"] = (info.kleur as Color).to_html(false)
	bewaar["hoed"] = (info.hoed as Color).to_html(false)
	if uitkomst == "ontsnapt":
		bewaar.bezoeken = int(info.get("bezoeken", 0)) + 1
		var oud_wrok: String = String(info.get("wrok", ""))
		bewaar.wrok = info.get("laatst_geraakt", oud_wrok if oud_wrok != "" else "your Hoard")
		bewaar.erase("laatst_geraakt")
		terugkomers.append(bewaar)
		# Geen straf: wie ontsnapt neemt niets mee dat jij kwijt bent, alleen zijn wrok.
		_kroniek("%s escaped and is now %s %s. Grudge: %s." % [info.naam, info.naam, _bijnaam(bewaar.bezoeken), bewaar.wrok])
	else:
		var buit := 3 + 2 * int(info.get("bezoeken", 0))
		hol.goud += buit
		_kroniek("%s %s. +%d gold." % [info.naam, info.get("wat", "fell"), buit])

func _process(delta: float) -> void:
	t += delta
	var helden := 0
	for w in wezens.get_children():
		if w.has_method("is_held"):
			helden += 1
	if t >= volgende_held and helden < 3:
		_nieuwe_held()
		volgende_held = t + (rng.randf_range(5.0, 8.0) if demo else rng.randf_range(25.0, 70.0))
	if demo and t >= volgende_graaf:
		volgende_graaf = t + 9.0
		var k: int = hol.schat_kol + 1
		if k < hol.kolommen:
			hol.klik(hol.cel_naar_pos(Vector2i(k, 0)) - Vector2(0, 8))
	if t >= volgende_opslag:
		volgende_opslag = t + 30.0
		bewaar()
	if duur > 0.0 and t > duur:
		log_regel("HOL einde na %d s, fps=%d, goud=%d, terugkomers=%d" % [int(duur), Engine.get_frames_per_second(), hol.goud, terugkomers.size()])
		bewaar()
		get_tree().quit()

func _input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		var p: Vector2 = (event.position - hol.position) / schaal
		var wat: String = hol.klik(p)
		log_regel("HOL klik op %s: %s" % [event.position, wat if wat != "" else "niets"])
	elif event is InputEventMouseMotion and not tekst.hover:
		tekst.hover = true
		tekst.queue_redraw()

func _notification(what: int) -> void:
	if what == NOTIFICATION_WM_MOUSE_EXIT and tekst:
		tekst.hover = false
		tekst.queue_redraw()
	elif what == NOTIFICATION_WM_CLOSE_REQUEST:
		bewaar()

func bewaar() -> void:
	var data := {"versie": 1, "tijd": Time.get_unix_time_from_system(), "gang": hol.gang, "vallen": hol.vallen,
		"schat_kol": hol.schat_kol, "goud": hol.goud, "terugkomers": terugkomers, "kroniek": kroniek}
	var f := FileAccess.open(OPSLAG, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(data))
		f.close()

func laad() -> void:
	if not FileAccess.file_exists(OPSLAG):
		return
	var data = JSON.parse_string(FileAccess.get_file_as_string(OPSLAG))
	if typeof(data) != TYPE_DICTIONARY:
		log_regel("HOL opslag onleesbaar, vers begin")
		return
	var g: Array = data.get("gang", [])
	for i in mini(g.size(), hol.kolommen):
		hol.gang[i] = bool(g[i])
	hol.vallen.clear()
	for k in data.get("vallen", {}):
		hol.vallen[int(k)] = String(data.vallen[k])
	hol.schat_kol = clampi(int(data.get("schat_kol", hol.schat_kol)), 0, hol.kolommen - 1)
	hol.goud = int(data.get("goud", 0))
	terugkomers = data.get("terugkomers", [])
	for r in data.get("kroniek", []):
		kroniek.append(String(r))
	hol.queue_redraw()
	tekst.zet(kroniek, hol.goud)
	log_regel("HOL opslag geladen: %d terugkomers, %d goud" % [terugkomers.size(), hol.goud])
