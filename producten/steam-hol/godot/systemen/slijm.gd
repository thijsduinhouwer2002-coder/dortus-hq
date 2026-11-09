extends Node2D
# Bewoner: slijm (Bram). Vervangt kern/standin_slijm.gd als strook.gd dit bestand gebruikt.
# Zelfde vorm als de stand-in: zet(hol, kol), is_bewoner(), naam(), raak(); extra: plat(), kan_vechten(), soort.
# Regel van Sanne (features.md): een bewoner gaat nooit dood. Verliest hij, dan is hij even plat en staat weer op.
# Zuinig: staat stil als er niets gebeurt (alleen tekenen bij een hap, plat zijn of opstaan).

const PLAATJE := preload("res://kunst/slijm.png")   # 16 x 16, rust 0..3 (3 fps), hap 4..5
const PLAT_S := 60.0

var hol
var soort := "slijm"
var bijnaam_naam := "Gloop"
var gegeten := 0          # helden die hij kreeg ("Gloop has eaten 12 heroes")
var keer_plat := 0
var t := 0.0
var hap_tot := 0.0
var plat_tot := 0.0

func zet(h, kol: int) -> void:
	hol = h
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	position = hol.cel_naar_pos(Vector2i(kol, 0))
	set_process(false)

func is_bewoner() -> bool:
	return true

func naam() -> String:
	return "%s the Slime" % bijnaam_naam

func kan_vechten() -> bool:
	return t >= plat_tot

func raak() -> void:
	gegeten += 1
	hap_tot = t + 0.7
	set_process(true)

func plat() -> void:
	keer_plat += 1
	plat_tot = t + PLAT_S
	set_process(true)

func regel_plat() -> String:
	return "%s is flat. Back in a minute." % bijnaam_naam

func _process(delta: float) -> void:
	stap(delta)

func stap(delta: float) -> void:
	t += delta
	queue_redraw()
	if t > hap_tot and t > plat_tot + 0.5:
		set_process(false)

func _draw() -> void:
	var frame := 0
	var sy := 1.0
	if t < hap_tot:
		frame = 4 + int(t * 6) % 2
	elif t < plat_tot:
		sy = 0.3
	elif t < plat_tot + 0.5:
		sy = 0.3 + 1.4 * (t - plat_tot)   # weer opveren
		sy = minf(sy, 1.0)
	draw_set_transform(Vector2.ZERO, 0, Vector2(1.0 + (1.0 - sy) * 0.5, sy))
	draw_texture_rect_region(PLAATJE, Rect2(-8, -16, 16, 16), Rect2(frame * 16, 0, 16, 16))
	draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
