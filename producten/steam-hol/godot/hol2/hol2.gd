# Hol 2.0 proef (Olaf, #388, ontwerp Sanne: producten/steam-hol/ontwerp-hol2/LEESMIJ.md). Alleen op tak hol2-proef.
# Een strook van 120 spelpx: tuin, maaiveld, verdieping 1 en 2; een derde verdieping eronder zie je door te schuiven
# met het muiswiel. Klik in het hol en Gloop loopt erheen via de ladders; klik op Gloop voor de besturen-stand (WASD of
# pijltjes, W/S klimt, gouden rand, stopt bij Esc, klik buiten of 10 s geen toets). Gloop scharrelt zelf met de tabel.
# Retro: tekenen op breedte x spel_h spelpixels en vergroten met een heel getal (rekstand viewport), figuren op hele px.
# Startargumenten na "--": hoogte=120 (96 tot 240, spelpixels; het venster is hoogte x schaal) duur=<s> log=<pad> zaad=<n>
# film=1 schaal=<n> fps=<n> toetsproef=1 (Gloop staat stil tot de besturen-stand, voor de Windows-run van #401)
extends Node2D

const KAART := preload("res://hol2/kaart.gd")
const GLOOP := preload("res://hol2/gloop2.gd")
const HELD := preload("res://hol2/held2.gd")
const BORD := preload("res://hol2/bord.gd")
const FOCUS := preload("res://hol2/focus.gd")
const SOORTEN := ["held0", "held1", "held2", "dief", "bard", "heks", "ridder"]
const NAMEN := ["Bert", "Lot", "Fenna", "Joost", "Mira", "Kees", "Ada", "Wout", "Noor", "Pim", "Saar", "Teun"]

var hoogte := 120
var schaal := 1
var breed := 1920
var spel_h := 120
var duur := 0.0
var log_pad := ""
var film := false
var toetsproef := false
var fps := 12
var zaad := 0
var rng := RandomNumberGenerator.new()
var t := 0.0

var kaart
var wereld: Node2D
var leven: Node2D
var scherm_laag: Node2D
var gloop
var helden: Array = []
var tex_tegels: Texture2D
var tex_fig: Dictionary = {}
var info: Dictionary = {}
var goud := 10
var hoeden: Array = []      # soorten hoeden op de stapel naast de troon
var poef: Array = []        # [{pos, t}]
var volgende_held := 2.0
var held_n := 0

var scroll := 0.0
var scroll_doel := 0.0
var max_scroll := 0.0
var muis_t := -100.0
var besturen := false
var toets_t := 0.0
var links := false
var rechts := false
var beelden := 0
var meet_t := 0.0
var film_stap := 0

func log_regel(r: String) -> void:
	print(r)
	if log_pad == "":
		return
	var f := FileAccess.open(log_pad, FileAccess.READ_WRITE if FileAccess.file_exists(log_pad) else FileAccess.WRITE)
	if f:
		f.seek_end()
		f.store_line("%.1f %s" % [t, r])

func _lees_argumenten() -> void:
	for a in OS.get_cmdline_user_args():
		var kv := a.split("=", true, 1)
		if kv.size() != 2:
			continue
		match kv[0]:
			"hoogte": hoogte = clampi(int(kv[1]), 96, 240)
			"duur": duur = float(kv[1])
			"log": log_pad = kv[1]
			"zaad": zaad = int(kv[1])
			"film": film = kv[1] == "1"
			"toetsproef": toetsproef = kv[1] == "1"
			"schaal": schaal = maxi(1, int(kv[1]))
			"fps": fps = maxi(4, int(kv[1]))

func _ready() -> void:
	schaal = 0
	_lees_argumenten()
	var scherm := DisplayServer.screen_get_usable_rect()
	if schaal == 0:
		schaal = maxi(1, int(round(DisplayServer.screen_get_size().y / 1080.0)))
	var m := maten(hoogte, schaal, scherm.size)
	schaal = m.schaal
	breed = m.breed
	spel_h = m.spel_h
	var venster_h: int = m.venster_h
	rng.seed = zaad if zaad != 0 else int(Time.get_unix_time_from_system())
	if log_pad != "" and FileAccess.file_exists(log_pad):
		DirAccess.remove_absolute(log_pad)
	Engine.max_fps = fps
	if not film:
		OS.low_processor_usage_mode = true
	get_viewport().transparent_bg = true
	if schaal > 1:
		# op een scherm met schaal 2 of meer: tekenen op spelpixels en vergroten met een heel getal; op schaal 1 is
		# dat een extra kopie per beeld voor niets (meting #388), dan tekenen we direct
		var w := get_window()
		w.content_scale_size = Vector2i(breed, spel_h)
		w.content_scale_mode = Window.CONTENT_SCALE_MODE_VIEWPORT
		w.content_scale_aspect = Window.CONTENT_SCALE_ASPECT_KEEP
		w.content_scale_stretch = Window.CONTENT_SCALE_STRETCH_INTEGER
	DisplayServer.window_set_size(Vector2i(scherm.size.x, venster_h))
	DisplayServer.window_set_position(Vector2i(scherm.position.x, scherm.position.y + scherm.size.y - venster_h))

	info = JSON.parse_string(FileAccess.get_file_as_string("res://hol2/kunst/kunst.json"))
	tex_tegels = load("res://hol2/kunst/tegels.png")
	for s in SOORTEN + ["gloop", "hoeden"]:
		tex_fig[s] = load("res://hol2/kunst/%s.png" % s)

	var n_verd: int = m.n_verd
	wereld = Node2D.new()
	add_child(wereld)
	kaart = Node2D.new()
	kaart.set_script(KAART)
	kaart.tex = tex_tegels
	kaart.vak = info.tegels
	# de vaste achtergrond (duizenden tegels) één keer bakken in een eigen beeld en daarna als één plaatje tekenen;
	# anders stuurt Godot elk beeld alle tegels opnieuw naar de kaart (meting #388: +65 procent CPU)
	var bak := SubViewport.new()
	bak.size = Vector2i(breed, KAART.hoogte_wereld(n_verd))
	bak.transparent_bg = true
	bak.render_target_update_mode = SubViewport.UPDATE_ONCE
	bak.canvas_item_default_texture_filter = Viewport.DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST
	add_child(bak)
	bak.add_child(kaart)
	kaart.maak(breed, n_verd, rng)
	var achter := Sprite2D.new()
	achter.centered = false
	achter.texture = bak.get_texture()
	wereld.add_child(achter)
	max_scroll = maxf(0.0, KAART.hoogte_wereld(n_verd) - spel_h)
	leven = Node2D.new()
	leven.draw.connect(_teken_leven)
	wereld.add_child(leven)
	scherm_laag = Node2D.new()
	scherm_laag.draw.connect(_teken_scherm)
	add_child(scherm_laag)

	gloop = GLOOP.new()
	gloop.rng = rng
	gloop.log_f = log_regel
	gloop.helden_ref = helden
	gloop.zet(kaart, kaart.troon_niveau, kaart.troon_x - 8)
	gloop.kies()
	_muisvlak()
	var gp: Vector2 = (gloop.pos() + Vector2(0, -8)) * schaal
	log_regel("HOL2 gloop venster x=%d y=%d" % [int(gp.x), int(gp.y)])
	log_regel("HOL2 start hoogte=%d schaal=%d spelpixels=%dx%d verdiepingen=%d wereld=%d venster=%s zaad=%d" % [hoogte, schaal,
		breed, spel_h, n_verd, KAART.hoogte_wereld(n_verd), DisplayServer.window_get_size(), rng.seed])

# De maat van de strook (Daan #394 moet 1): hoogte is in spelpixels, dus op elk scherm 120 spelpx (tuin en 2
# verdiepingen); het venster is hoogte x schaal vensterpixels hoog. Past dat niet op het scherm (heel klein scherm met
# een grote schaal), dan gaat de schaal omlaag tot het past.
static func maten(h: int, s: int, scherm: Vector2i) -> Dictionary:
	s = maxi(1, s)
	while s > 1 and h * s > scherm.y / 2:
		s -= 1
	return {"schaal": s, "spel_h": h, "venster_h": h * s, "breed": int(scherm.x / s),
		"n_verd": maxi(3, int(ceil((h - 26) / 48.0)) + 1)}

# Hoeveel verdiepingen (tuin = 0) staan er zonder schuiven helemaal in beeld?
static func lagen_in_beeld(spel_h: int) -> int:
	var n := 0
	while n < 8 and KAART.voet_y(n) <= spel_h:
		n += 1
	return n

func _process(delta: float) -> void:
	delta = minf(delta, 0.25)
	t += delta
	beelden += 1
	if film:
		_film()
	if besturen or not toetsproef:
		gloop.werk(delta)
	# helden
	volgende_held -= delta
	if volgende_held <= 0.0 and helden.size() < 10:
		var h = HELD.new()
		var s: String = SOORTEN[held_n % SOORTEN.size()]
		h.start(kaart, rng, s, NAMEN[held_n % NAMEN.size()])
		helden.append(h)
		held_n += 1
		volgende_held = rng.randf_range(5.0, 9.0) if film else rng.randf_range(9.0, 16.0)
		log_regel("HOL2 held %s (%s) komt binnen via de tuin" % [h.naam, s])
	for h in helden.duplicate():
		var e: String = h.werk(delta)
		match e:
			"val":
				goud += 3
				hoeden.append(rng.randi_range(0, 9))
				log_regel("HOL2 val: %s valt in een %s op verdieping %d (goud %d, hoeden %d)" % [h.naam, h.val.soort, h.niveau, goud, hoeden.size()])
			"schat":
				goud = maxi(0, goud - 1)
				log_regel("HOL2 %s pakt een munt van de schat (goud %d)" % [h.naam, goud])
			"weg":
				log_regel("HOL2 %s gaat de tuin uit" % h.naam)
		if h.weg:
			if h.fase == "valt":
				poef.append({"pos": Vector2(h.x, kaart.voet_y(h.val.niveau) - 3), "t": 0.0})
			helden.erase(h)
	for v in kaart.vallen:
		v.open = maxf(0.0, v.open - delta)
	for p in poef.duplicate():
		p.t += delta
		if p.t > 0.5:
			poef.erase(p)
	_werk_scroll(delta)
	if besturen:
		toets_t += delta
		gloop.stuur_dx = (1 if rechts else 0) - (1 if links else 0)
		if toets_t > 10.0:
			_zet_besturen(false, "10 s geen toets")
	leven.queue_redraw()
	scherm_laag.queue_redraw()
	meet_t += delta
	if meet_t >= 10.0:
		log_regel("HOL2 beelden %d in %.1f s, helden %d, goud %d" % [beelden, meet_t, helden.size(), goud])
		beelden = 0
		meet_t = 0.0
	if duur > 0.0 and t > duur:
		log_regel("HOL2 einde na %d s, goud=%d, hoeden=%d" % [int(duur), goud, hoeden.size()])
		get_tree().quit()

func _werk_scroll(delta: float) -> void:
	if besturen:
		# de camera volgt Gloop als hij onder de strook loopt
		scroll_doel = clampf(gloop.y - spel_h + 10.0, 0.0, max_scroll) if gloop.y > spel_h - 6 + scroll_doel else scroll_doel
		if gloop.y - 30.0 < scroll_doel:
			scroll_doel = clampf(gloop.y - 30.0, 0.0, max_scroll)
	elif t - muis_t > 10.0 and scroll_doel != 0.0:
		scroll_doel = 0.0   # 10 s zonder muis: zacht terug naar tuin en verdieping 1 en 2
		log_regel("HOL2 schuift terug")
	var oud := roundf(scroll)
	scroll = move_toward(scroll, scroll_doel, maxf(24.0, absf(scroll_doel - scroll) * 3.0) * delta)
	wereld.position.y = -roundf(scroll)
	if roundf(scroll) != oud and (oud < 8.0) != (roundf(scroll) < 8.0):
		_muisvlak()

# Klikken gaan door de lucht boven de tuin heen naar het venster erachter.
func _muisvlak() -> void:
	var top := maxi(0, 8 - int(roundf(scroll))) * schaal
	var w := DisplayServer.window_get_size()
	DisplayServer.window_set_mouse_passthrough(PackedVector2Array([Vector2(0, top), Vector2(w.x, top), Vector2(w.x, w.y), Vector2(0, w.y)]))

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.pressed:
		var p: Vector2 = event.position + Vector2(0, roundf(scroll))
		match event.button_index:
			MOUSE_BUTTON_WHEEL_UP, MOUSE_BUTTON_WHEEL_DOWN:
				muis_t = t
				var d := -12.0 if event.button_index == MOUSE_BUTTON_WHEEL_UP else 12.0
				scroll_doel = clampf(scroll_doel + d, 0.0, max_scroll)
				log_regel("HOL2 schuif naar %d" % int(scroll_doel))
			MOUSE_BUTTON_LEFT:
				muis_t = t
				_klik(p)
			MOUSE_BUTTON_RIGHT:
				# proef: geen menu of systeemvak, rechtsklik stopt (staat in LEES-MIJ-EERST.txt)
				log_regel("HOL2 stop met rechtsklik")
				get_tree().quit()
	elif event is InputEventMouseMotion:
		muis_t = t
	elif event is InputEventKey and besturen:
		# plek op het toetsenbord (WASD ook op azerty); zonder scancode (sommige hulpprogramma's) de letter zelf
		var k: int = event.physical_keycode if event.physical_keycode != KEY_NONE else event.keycode
		if event.pressed:
			toets_t = 0.0
		match k:
			KEY_A, KEY_LEFT: links = event.pressed
			KEY_D, KEY_RIGHT: rechts = event.pressed
			KEY_W, KEY_UP:
				if event.pressed and not event.echo:
					gloop.klim_toets(true)
			KEY_S, KEY_DOWN:
				if event.pressed and not event.echo:
					gloop.klim_toets(false)
			KEY_ESCAPE:
				if event.pressed:
					_zet_besturen(false, "Esc")

func _klik(p: Vector2) -> void:
	var g: Vector2 = gloop.pos()
	if Rect2(g.x - 9, g.y - 16, 18, 17).has_point(p) and not besturen:
		_zet_besturen(true, "klik op Gloop")
		return
	var n: int = kaart.niveau_bij(p.y)
	log_regel("HOL2 klik op %d,%d: niveau %d" % [int(p.x), int(p.y), n])
	gloop.bestuurd = false
	gloop.klik_naar(n, p.x)
	gloop.bestuurd = besturen

func _zet_besturen(aan: bool, waarom: String) -> void:
	if aan == besturen:
		return
	besturen = aan
	gloop.bestuurd = aan
	gloop.stop()
	links = false
	rechts = false
	toets_t = 0.0
	# alleen in deze stand pakt het spel de focus; anders blijft het venster no_focus (nooit toetsen van het werk)
	var f := ""
	if aan:
		f = "vorig venster " + FOCUS.neem()   # onthouden waar je werkte, vóór het hol de focus pakt
	DisplayServer.window_set_flag(DisplayServer.WINDOW_FLAG_NO_FOCUS, not aan)
	if aan:
		DisplayServer.window_move_to_foreground()
		get_window().grab_focus()
	else:
		gloop.doet = ""
		gloop.kies()
		# Daan #394 moet 2: no_focus aan geeft de focus niet terug; het hulpje zet het vorige venster weer vooraan
		# (niet bij "klik buiten": dan koos je zelf al een ander venster)
		if waarom != "klik buiten":
			f = "focus " + FOCUS.terug()
	log_regel("HOL2 besturen %s (%s) gloop x=%d niveau=%d %s" % ["aan" if aan else "uit", waarom, int(gloop.x), gloop.niveau, f])

func _notification(what: int) -> void:
	if what == NOTIFICATION_APPLICATION_FOCUS_OUT or what == NOTIFICATION_WM_WINDOW_FOCUS_OUT:
		if besturen:
			_zet_besturen(false, "klik buiten")

func _teken_leven() -> void:
	BORD.teken_leven(self)

func _teken_scherm() -> void:
	BORD.teken_scherm(self)

# film=1: een vast script voor de film van 2 minuten (lopen, klimmen, besturen, schuiven).
func _film() -> void:
	var plan := [
		[5.0, func(): _klik(Vector2(breed * 0.35, KAART.voet_y(2) - 5))],
		[22.0, func(): _klik(Vector2(breed * 0.5, KAART.voet_y(1) - 5))],
		[45.0, func(): _klik(Vector2(breed * 0.55, KAART.voet_y(0) - 5))],
		[70.0, func(): _zet_besturen(true, "film")],
		[70.5, func(): _toets(KEY_D, true)],
		[73.0, func(): _toets(KEY_D, false)],
		[74.0, func(): _toets(KEY_A, true)],
		[76.0, func(): _toets(KEY_A, false)],
		[79.0, func(): _toets(KEY_ESCAPE, true)],
		[82.0, func(): _klik(Vector2(breed * 0.4, KAART.voet_y(3) - 5))],
		[84.0, func(): _wiel(false, 4)],
		[100.0, func(): _wiel(true, 4)],
	]
	while film_stap < plan.size() and t >= plan[film_stap][0]:
		plan[film_stap][1].call()
		film_stap += 1

func _toets(k: Key, aan: bool) -> void:
	var e := InputEventKey.new()
	e.physical_keycode = k
	e.keycode = k
	e.pressed = aan
	_unhandled_input(e)

func _wiel(op: bool, n: int) -> void:
	for i in n:
		var e := InputEventMouseButton.new()
		e.button_index = MOUSE_BUTTON_WHEEL_UP if op else MOUSE_BUTTON_WHEEL_DOWN
		e.pressed = true
		_unhandled_input(e)
