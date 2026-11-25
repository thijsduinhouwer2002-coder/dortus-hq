extends Node2D
# Warme gloed bovenop de lichtkaart (Olaf, 25 nov, issue #97). Optellen: maakt de plek bij de fakkel en het goud
# warmer en iets lichter dan de tegels zelf. Traag flakkeren, 90 tot 100 procent (bouwblad H), twee golven die niet
# gelijk lopen. Alleen een nieuw beeld als hol.anim verandert (de fakkel krijgt dan toch een nieuw beeld, #79), dus
# een stil hol kost niets extra.

const LICHT := preload("res://systemen/licht.gd")
# per bron (zelfde volgorde als licht.gd bronnen): kleur met dekking en of hij flakkert
const KLEUR_FAKKEL := Color(1.0, 0.62, 0.28, 0.20)
const KLEUR_GOUD := Color(1.0, 0.78, 0.35, 0.14)

var h
var vlek: GradientTexture2D
var laatste_anim := -1
var t := 0.0

func _ready() -> void:
	var g := Gradient.new()
	g.set_color(0, Color(1, 1, 1, 1))
	g.set_color(1, Color(1, 1, 1, 0))
	g.add_point(0.45, Color(1, 1, 1, 0.45))
	vlek = GradientTexture2D.new()
	vlek.gradient = g
	vlek.fill = GradientTexture2D.FILL_RADIAL
	vlek.fill_from = Vector2(0.5, 0.5)
	vlek.fill_to = Vector2(1.0, 0.5)
	vlek.width = 64
	vlek.height = 64
	texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR

func _process(delta: float) -> void:
	t += delta
	if h == null or h.anim == laatste_anim:
		return
	laatste_anim = h.anim
	queue_redraw()

# 0,9 tot 1,0, traag (golven van ±2,3 en ±3,7 s), per bron een eigen fase
static func flakker(tijd: float, i: int) -> float:
	var a := sin(tijd * 2.7 + i * 1.9) * 0.5 + 0.5
	var b := sin(tijd * 1.7 + i * 0.7) * 0.5 + 0.5
	return 0.9 + 0.1 * (a * 0.6 + b * 0.4)

func _draw() -> void:
	if h == null or vlek == null or h.kolommen <= 0:
		return
	var b: Array = LICHT.bronnen(h)
	b.pop_back()   # daglicht in de schacht zit alleen in de kaart
	for i in b.size():
		var p: Vector2 = b[i][0]
		var r: float = b[i][1]
		var c: Color
		c = KLEUR_FAKKEL if (b.size() == 2 and i == 0) else KLEUR_GOUD
		c.a *= flakker(t, i)
		r *= (0.97 + 0.03 * flakker(t * 0.8, i + 3)) * 0.75
		draw_texture_rect(vlek, Rect2(p.x - r, p.y - r, 2.0 * r, 2.0 * r), false, c)
