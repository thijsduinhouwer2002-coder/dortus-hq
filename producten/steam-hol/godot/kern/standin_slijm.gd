extends Node2D
# Stand-in bewoner (Olaf) tot Bram zijn bewoners in systemen/ zet. Staat stil (kost niets) en wiebelt alleen als hij raakt.

var hol
var t := 0.0
var wiebel_tot := 0.0
var treffers := 0

func zet(h, kol: int) -> void:
	hol = h
	position = hol.cel_naar_pos(Vector2i(kol, 0))
	set_process(false)

func is_bewoner() -> bool:
	return true

func naam() -> String:
	return "Gloop the Slime"

func raak() -> void:
	treffers += 1
	wiebel_tot = t + 0.8
	set_process(true)

func _process(delta: float) -> void:
	t += delta
	queue_redraw()
	if t > wiebel_tot:
		set_process(false)
		queue_redraw()

func _draw() -> void:
	var op := 0.0
	if t < wiebel_tot:
		op = 1.0 if int(t * 8) % 2 == 0 else 0.0
	var groen := Color("#78c94a")
	draw_rect(Rect2(-6, -6 - op, 12, 6 + op), groen)
	draw_rect(Rect2(-5, -8 - op, 10, 2), groen)
	draw_rect(Rect2(-4, -9 - op, 8, 1), groen.lightened(0.2))
	draw_rect(Rect2(-4, -7 - op, 2, 1), groen.lightened(0.5))
	draw_rect(Rect2(-2, -5 - op, 1, 2), Color("#1d2a14"))   # ogen
	draw_rect(Rect2(2, -5 - op, 1, 2), Color("#1d2a14"))
	draw_rect(Rect2(-1, -2 - op, 3, 1), Color("#3e7a26"))   # mond
