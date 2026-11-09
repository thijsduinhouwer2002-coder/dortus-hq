extends Node2D
# Kleine tekst in de strook zelf (geen kaartjes over andere vensters, eis Thijs 9 nov).
# Altijd: één regel kroniek en het goud. Bij hover binnen de strook: de laatste drie regels.

var regels: Array[String] = []
var goud := 0
var hover := false
var breedte := 1280.0
var hoogte := 120.0

func zet(r: Array[String], g: int) -> void:
	regels = r
	goud = g
	queue_redraw()

func _draw() -> void:
	var font := ThemeDB.fallback_font
	var maat := 12 if hoogte < 110 else 13
	var n := 3 if hover else 1
	var toon: Array[String] = []
	for i in range(max(0, regels.size() - n), regels.size()):
		toon.append(regels[i])
	var regel_h := maat + 4
	var bw := 430.0
	var x := breedte - bw - 8
	var y0 := hoogte - 8 - regel_h * (toon.size() + 1)
	draw_rect(Rect2(x - 6, y0 - 4, bw + 12, regel_h * (toon.size() + 1) + 6), Color("#1c120c"))
	draw_rect(Rect2(x - 6, y0 - 4, bw + 12, 1), Color("#5a3a26"))
	draw_string(font, Vector2(x, y0 + maat), "Hoard: %d gold" % goud, HORIZONTAL_ALIGNMENT_LEFT, bw, maat, Color("#f2c14e"))
	for i in toon.size():
		draw_string(font, Vector2(x, y0 + regel_h * (i + 1) + maat), toon[i], HORIZONTAL_ALIGNMENT_LEFT, bw, maat, Color("#e8dcc8"))
