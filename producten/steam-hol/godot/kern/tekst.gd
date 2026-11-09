extends Node2D
# Kleine tekst in de strook zelf (geen kaartjes over andere vensters, eis Thijs 9 nov).
# Altijd: één regel kroniek en het goud. Bij hover binnen de strook: de laatste drie regels.

var regels: Array[String] = []
var goud := 0
var hover := false
var breedte := 1280.0
var hoogte := 120.0
var schaal := 3
const PANEEL := preload("res://kunst/paneel.png")   # Daan: 12 x 12, 9-slice rand 4 (kunst.json)
const R := 4

# Daans paneel als 9-slice, met de schaal van de strook (scherpe pixels)
func _paneel(rect: Rect2) -> void:
	var m := R * schaal
	var xs := [rect.position.x, rect.position.x + m, rect.end.x - m, rect.end.x]
	var ys := [rect.position.y, rect.position.y + m, rect.end.y - m, rect.end.y]
	var bx := [0, R, 12 - R, 12]
	for i in 3:
		for j in 3:
			draw_texture_rect_region(PANEEL, Rect2(xs[i], ys[j], xs[i + 1] - xs[i], ys[j + 1] - ys[j]),
				Rect2(bx[i], bx[j], bx[i + 1] - bx[i], bx[j + 1] - bx[j]))

# muntje van 4 x 4 spelpixels: donkere rand, goud, één glimpixel
func _munt(p: Vector2) -> void:
	var px := float(schaal)
	var rand := Color("#7a4a12")
	var goudk := Color("#f2c14e")
	var vorm := [".XX.", "XGGX", "XGGX", ".XX."]
	for j in 4:
		for i in 4:
			var c: String = vorm[j][i]
			if c == "X":
				draw_rect(Rect2(p.x + i * px, p.y + j * px, px, px), rand)
			elif c == "G":
				draw_rect(Rect2(p.x + i * px, p.y + j * px, px, px), Color("#ffe07a") if (i == 1 and j == 1) else goudk)

func vak_breedte() -> float:
	return minf(430.0, breedte * 0.3)

func zet(r: Array[String], g: int) -> void:
	regels = r
	goud = g
	queue_redraw()

func _ready() -> void:
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST

func _draw() -> void:
	var font := ThemeDB.fallback_font
	var maat := 12 if hoogte < 110 else 13
	var n := 3 if hover else 1
	var toon: Array[String] = []
	for i in range(max(0, regels.size() - n), regels.size()):
		toon.append(regels[i])
	var regel_h := maat + 4
	var bw := vak_breedte()
	var x := breedte - bw - 8
	var binnen := 5 * schaal   # tekst begint 5 spelpixels binnen de buitenkant van Daans paneel (kunst.json)
	var y0 := hoogte - 2 - (binnen - 2) - regel_h * (toon.size() + 1)
	# paneel van x - binnen tot de rechterrand, van boven de kop tot onderaan de strook
	var links := x - binnen + 4
	var top := y0 - binnen + 2
	_paneel(Rect2(links, top, breedte - 2 - links, hoogte - 2 - top))
	# goud als muntje plus getal in plaats van "Hoard: 24 gold" (Mila 20:55, stijl.md punt 5); zelfde kleuren als de
	# vliegende muntjes in hol.gd, 4 x 4 spelpixels, op de schaal van de strook (scherpe pixels)
	var mx := x
	var my := y0 + maat / 2.0 - 2 * schaal + 1
	_munt(Vector2(mx, my))
	draw_string(font, Vector2(x + 5 * schaal + 2, y0 + maat), str(goud), HORIZONTAL_ALIGNMENT_LEFT, bw, maat, Color("#ffe07a"))
	for i in toon.size():
		# nooit afkappen (Sanne 9 nov): eerst kleiner tot 10 px, past het dan nog niet, dan op een woordgrens met "..."
		var r: String = toon[i]
		var m := maat
		while m > 10 and font.get_string_size(r, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bw:
			m -= 1
		if font.get_string_size(r, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bw:
			var woorden := r.split(" ")
			while woorden.size() > 1 and font.get_string_size(" ".join(woorden) + "...", HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bw:
				woorden.remove_at(woorden.size() - 1)
			r = " ".join(woorden) + "..."
		draw_string(font, Vector2(x, y0 + regel_h * (i + 1) + maat), r, HORIZONTAL_ALIGNMENT_LEFT, -1, m, Color("#f3e2c0"))
