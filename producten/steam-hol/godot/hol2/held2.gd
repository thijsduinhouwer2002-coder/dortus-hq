# Hol 2.0 proef (Olaf, #388): een held komt binnen via de tuin, zakt af via ladders naar de schat van Gloop,
# en kan op elke verdieping in een val vallen (luik of stekels). Haalt hij de schat, dan pakt hij een munt en gaat
# terug naar boven en de tuin uit.
extends "res://hol2/loper.gd"

const F_RUST := 0
const F_SCHRIK := 7
const F_VAL := 8
const F_KIJK := 9

var soort := "held0"
var leeft := true
var weg := false          # klaar om uit de lijst te halen
var fase := "binnen"      # binnen, naar_schat, terug, valt
var val: Dictionary = {}
var val_t := 0.0
var t := 0.0
var gehad: Array = []     # vallen waar hij al overheen liep (één kans per val)
var rng: RandomNumberGenerator
var naam := ""

func _init() -> void:
	snel = 20.0
	klim_snel = 14.0

func start(k, r: RandomNumberGenerator, s: String, n: String) -> void:
	rng = r
	soort = s
	naam = n
	var van_rechts := rng.randf() < 0.5
	zet(k, 0, k.breed + 12.0 if van_rechts else -12.0)
	naar_rechts = not van_rechts
	ga_naar(kaart.troon_niveau, kaart.troon_x - 4 - rng.randf_range(0.0, 20.0))
	fase = "naar_schat"

# Geeft een gebeurtenis terug voor hol2.gd: "", "val", "schat", "weg".
func werk(delta: float) -> String:
	t += delta
	if fase == "valt":
		val_t += delta
		if val.soort == "luik":
			y += 34.0 * delta
			if val_t > 0.7:
				leeft = false
				weg = true
		else:
			if val_t > 0.45:
				y += 20.0 * delta
			if val_t > 0.9:
				leeft = false
				weg = true
		return ""
	var x_voor := x
	var klaar := stap(delta)
	if not klimt:
		for v in kaart.vallen:
			if v.niveau != niveau or gehad.has(v):
				continue
			var mid: float = v.x + 6.0
			if (x_voor - mid) * (x - mid) <= 0.0 and x_voor != x:
				gehad.append(v)
				if rng.randf() < v.kans:
					fase = "valt"
					val = v
					val_t = 0.0
					x = mid
					v.open = 1.2
					pad.clear()
					return "val"
	if klaar != "" and not loopt():
		if fase == "naar_schat":
			fase = "terug"
			ga_naar(0, -20.0 if x < kaart.breed / 2.0 else kaart.breed + 20.0)
			return "schat"
		if fase == "terug":
			leeft = false
			weg = true
			return "weg"
	return ""

func teken(laag: CanvasItem, tex: Texture2D, info: Dictionary) -> void:
	var w: int = info.w
	var h: int = info.h
	var p := pos()
	var f := F_RUST
	if fase == "valt":
		f = F_VAL if val.soort == "luik" else F_SCHRIK
	elif klimt:
		f = 1 + int(t * 4.0) % 2
	elif loopt():
		f = 1 + int(t * 6.0) % 6
	var dst := Rect2(p.x - info.anker_x, p.y - h, w, h)
	var src := Rect2(f * w, 0, w, h)
	if fase == "valt":
		# alleen het deel boven de vloer van de val tekenen: hij zakt erin weg
		var vloer: float = kaart.voet_y(val.niveau) + 2.0
		var zicht := vloer - dst.position.y
		if zicht <= 0.0:
			return
		if zicht < h:
			dst.size.y = zicht
			src.size.y = zicht
	if not naar_rechts:
		laag.draw_set_transform(Vector2(2.0 * p.x, 0), 0.0, Vector2(-1, 1))
	laag.draw_texture_rect_region(tex, dst, src)
	laag.draw_set_transform(Vector2.ZERO)
