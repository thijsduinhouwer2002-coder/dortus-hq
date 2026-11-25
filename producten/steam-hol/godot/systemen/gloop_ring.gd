extends Node2D
# Gloop is klaar (Mila, 25 nov 2026, issue #62): een ring van licht om zijn voet als je zijn volgende stap kunt kopen.
# Vervangt de regel "Big Gloop ready: click Gloop" op het bord en het muntje boven Gloop (kern/kaartje.gd), zodat
# Gloop het zelf laat zien (Iris: tekst 6, aandacht 6; Thijs: rustig).
# Blad kunst/gloopring.png uit modellen/gloopring.py (Blender, geen AI): één beeld, cel 36 x 12 spelpixels, midden van
# de ring = midden van de cel. Twee van deze knopen hangen onder Gloop: "achter" (bovenste helft van het beeld, de
# achterkant van de ring) tekent achter zijn lijf (show_behind_parent), "voor" (onderste helft) ervoor.
# Rustig: hij ademt in 2,8 s een beetje lichter en groter, geen knipperen, geen geluid. Zuinig: _draw draait één keer,
# het ademen is alleen modulate en scale, en alleen 10 keer per seconde (zoals de rest van het spel weinig tekent).

const BLAD := preload("res://kunst/gloopring.png")
const CEL_W := 36.0
const CEL_H := 12.0
const ADEM_S := 2.8         # één keer ademen
const STAP_S := 0.1         # zo vaak verandert het licht (10 per seconde)
const ZICHT := [0.62, 1.0]  # licht van zwak naar sterk
const MAAT := [0.97, 1.03]  # en een tikje groter
const OPKOMEN_S := 0.6      # zacht verschijnen als je net genoeg goud hebt

var helft := "achter"       # "achter" of "voor"
var tex: CanvasTexture
var t := 0.0
var _stap_t := 0.0
var basis := 1.0            # maat van Gloop: 1 groot, 0,8 klein (slijm.gd zet_klaar)

func _ready() -> void:
	tex = CanvasTexture.new()
	tex.diffuse_texture = BLAD
	tex.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	show_behind_parent = helft == "achter"
	visible = false
	set_process(false)

func _draw() -> void:
	var h := CEL_H / 2.0
	var bron_h := float(BLAD.get_height()) / 2.0
	var bron_w := float(BLAD.get_width())
	if helft == "achter":
		draw_texture_rect_region(tex, Rect2(-CEL_W / 2.0, -h, CEL_W, h), Rect2(0, 0, bron_w, bron_h))
	else:
		draw_texture_rect_region(tex, Rect2(-CEL_W / 2.0, 0, CEL_W, h), Rect2(0, bron_h, bron_w, bron_h))

# licht (0 tot 1) en maat op tijd t sinds aan; los zodat de toets het kan nakijken
static func adem(t_: float) -> Vector2:
	var u := 0.5 - 0.5 * cos(TAU * t_ / ADEM_S)   # 0 bij aan, 1 halverwege: begint zacht
	var op := clampf(t_ / OPKOMEN_S, 0.0, 1.0)
	return Vector2(lerpf(ZICHT[0], ZICHT[1], u) * op, lerpf(MAAT[0], MAAT[1], u))

func zet_aan(aan: bool) -> void:
	if aan == visible:
		return
	visible = aan
	t = 0.0
	_stap_t = 0.0
	_pas_toe()
	set_process(aan)

func _process(delta: float) -> void:
	t += delta
	_stap_t += delta
	if _stap_t >= STAP_S:
		_stap_t = 0.0
		_pas_toe()

func _pas_toe() -> void:
	var a := adem(t)
	modulate = Color(1, 1, 1, a.x)
	scale = Vector2(a.y, a.y) * basis
