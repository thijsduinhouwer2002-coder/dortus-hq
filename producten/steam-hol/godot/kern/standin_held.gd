extends Node2D
# Stand-in held van Olaf, alleen zodat de kern speelbaar is tot Bram systemen/held.gd levert.
# Zelfde vorm als Brams afspraak: start(hol, info) en signaal klaar(held, uitkomst, info).
# info: naam, bezoeken (hoe vaak eerder hier), wrok ("" of waartegen), kleur, hoed.

signal klaar(held, uitkomst: String, info: Dictionary)

var hol
var info := {}
var staat := "afdalen"   # afdalen, lopen, vluchten, klimmen
var hp := 2
var snelheid := 11.0     # spelpixels per seconde
var t := 0.0
var geraakt_tot := 0.0
var gezien := {}         # kolommen waar hij al iets meemaakte
const VLOER := 36        # VLOER

func start(h, i: Dictionary) -> void:
	hol = h
	info = i
	hp = 2 + int(info.get("bezoeken", 0)) + int(info.get("taai", 0))
	var p: Vector2 = hol.cel_naar_pos(hol.ingang())
	position = Vector2(p.x, 2)

func is_held() -> bool:
	return true

func _process(delta: float) -> void:
	t += delta
	match staat:
		"afdalen":
			position.y = move_toward(position.y, VLOER, snelheid * delta)
			if position.y >= VLOER:
				staat = "lopen"
		"lopen":
			var doel: Vector2 = hol.cel_naar_pos(hol.schat())
			position.x = move_toward(position.x, doel.x, snelheid * delta)
			_onderweg()
			if absf(position.x - doel.x) < 0.5:
				info["wat"] = "grabbed one coin, saw the hoard wake up and ran"
				staat = "vluchten"
		"vluchten":
			var terug: Vector2 = hol.cel_naar_pos(hol.ingang())
			position.x = move_toward(position.x, terug.x, snelheid * 1.4 * delta)
			_onderweg()
			if absf(position.x - terug.x) < 0.5:
				staat = "klimmen"
		"klimmen":
			position.y = move_toward(position.y, -4, snelheid * delta)
			if position.y <= -4:
				klaar.emit(self, "ontsnapt", info)
				queue_free()
	queue_redraw()

func _onderweg() -> void:
	if staat == "" or hp <= 0:
		return
	var cel: Vector2i = hol.pos_naar_cel(position)
	if gezien.has(cel.x):
		return
	# karakter: wie een wrok heeft tegen de stekelput, keert om als hij er een ziet
	if hol.val_op(cel) != "" and info.get("wrok", "") == "the Spike Pit" and staat == "lopen":
		gezien[cel.x] = true
		info["wat"] = "saw the Spike Pit again and turned back"
		staat = "vluchten"
		return
	if hol.val_op(cel) != "":
		gezien[cel.x] = true
		_au("the Spike Pit")
		if hp <= 0:
			return
	for w in get_parent().get_children():
		if w != self and w.has_method("is_bewoner") and hol.pos_naar_cel(w.position).x == cel.x:
			gezien[cel.x] = true
			_au(w.naam())
			w.raak()
			return

func _au(waardoor: String) -> void:
	hp -= 1
	geraakt_tot = t + 0.5
	info["laatst_geraakt"] = waardoor
	if hp <= 0:
		info["wat"] = "fell to " + waardoor
		klaar.emit(self, "gevallen", info)
		queue_free()

func _draw() -> void:
	# Blokjesfiguur van 16 spelpixels hoog, voeten op (0, 0). Daan vervangt dit door echte kunst.
	var lijf: Color = info.get("kleur", Color("#3f6fb5"))
	var hoed: Color = info.get("hoed", Color("#b33a3a"))
	if t < geraakt_tot and int(t * 10) % 2 == 0:
		lijf = Color.WHITE
	var stap := int(t * 6) % 2 if staat in ["lopen", "vluchten"] else 0
	var r := -1.0 if staat == "vluchten" else 1.0
	draw_rect(Rect2(-3, -2, 2, 2 - stap), Color("#3a2a20"))          # benen
	draw_rect(Rect2(1, -2, 2, 1 + stap), Color("#3a2a20"))
	draw_rect(Rect2(-3, -9, 6, 7), lijf)                               # lijf
	draw_rect(Rect2(-2, -13, 4, 4), Color("#f0c8a0"))                  # hoofd
	draw_rect(Rect2(-3, -15, 6, 2), hoed)                              # hoed
	draw_rect(Rect2(-1 + r, -16, 2, 1), hoed)
	draw_rect(Rect2(0.5 * r, -12, 1, 1), Color("#20140e"))             # oog
	draw_rect(Rect2(3 * r if r > 0 else -4, -9, 1, 6), Color("#cfd6dd")) # zwaard
	if int(info.get("bezoeken", 0)) > 0:
		draw_rect(Rect2(-2 if r > 0 else 1, -11, 1, 2), Color("#d2342c"))  # litteken
	if int(info.get("bezoeken", 0)) > 1:
		draw_rect(Rect2(-3, -6, 6, 1), Color("#d2342c"))                   # nog een (verband)
