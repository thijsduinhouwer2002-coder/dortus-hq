# Hol 2.0 proef (Olaf, #388, #401): het vaste script voor film=1 (lopen, muis bij Gloop, klimmen, besturen,
# schuiven met wiel en pijltje). Uit hol2.gd gehaald om dat bestand onder de 400 regels te houden.
# Statische functies met hol2.gd als eerste argument (`s`).
extends RefCounted

const KAART := preload("res://hol2/kaart.gd")
const MUIS := preload("res://hol2/muis.gd")

static func stap(s) -> void:
	var plan := [
		[5.0, func(): s._klik(Vector2(s.breed * 0.35, KAART.voet_y(2) - 5))],
		[22.0, func(): s._klik(Vector2(s.breed * 0.5, KAART.voet_y(1) - 5))],
		[28.0, func(): s.muis_film = s.gloop.pos() + Vector2(10, -6 - roundf(s.scroll))],   # muis vlak naast Gloop
		[29.0, func(): s.log_regel("HOL2 film gloop x=%d na 1 s muis" % int(s.gloop.x))],
		[33.0, func(): s.log_regel("HOL2 film gloop x=%d na 5 s muis" % int(s.gloop.x))],
		[33.5, func(): s.muis_film = Vector2(-1, -1)],
		[40.0, func(): s.muis_film = s.BORD.knop_rect(s).get_center()],   # muis boven de stuurknop: uitleg
		[43.0, func(): s.muis_film = Vector2(-1, -1)],
		[45.0, func(): s._klik(Vector2(s.breed * 0.55, KAART.voet_y(0) - 5))],
		[70.0, func(): s._zet_besturen(true, "film")],
		[70.5, func(): toets(s, KEY_D, true)],
		[73.0, func(): toets(s, KEY_D, false)],
		[74.0, func(): toets(s, KEY_A, true)],
		[76.0, func(): toets(s, KEY_A, false)],
		[79.0, func(): toets(s, KEY_ESCAPE, true)],
		[82.0, func(): s._klik(Vector2(s.breed * 0.4, KAART.voet_y(3) - 5))],
		[84.0, func(): wiel(s, false, 4)],
		[100.0, func(): wiel(s, true, 4)],
		[104.0, func(): klik_scherm(s, MUIS.pijlen(s)[1].get_center())],
		[110.0, func(): klik_scherm(s, MUIS.pijlen(s)[0].get_center())],
	]
	while s.film_stap < plan.size() and s.t >= plan[s.film_stap][0]:
		plan[s.film_stap][1].call()
		s.film_stap += 1

static func toets(s, k: Key, aan: bool) -> void:
	var e := InputEventKey.new()
	e.physical_keycode = k
	e.keycode = k
	e.pressed = aan
	s._unhandled_input(e)

static func wiel(s, op: bool, n: int) -> void:
	for i in n:
		var e := InputEventMouseButton.new()
		e.button_index = MOUSE_BUTTON_WHEEL_UP if op else MOUSE_BUTTON_WHEEL_DOWN
		e.pressed = true
		s._unhandled_input(e)

# een klik op een plek in spelpixels van het scherm (zoals een echte linkerklik)
static func klik_scherm(s, p: Vector2) -> void:
	var e := InputEventMouseButton.new()
	e.button_index = MOUSE_BUTTON_LEFT
	e.pressed = true
	e.position = p
	s._unhandled_input(e)
