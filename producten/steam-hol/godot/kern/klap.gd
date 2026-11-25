extends Node2D
# Het Hol: het kernmoment van de val (Olaf 24 nov, issue 5; lijst in issue 4 van Sanne: klap, wit oplichten, poef,
# muntjes in een boog, reeksbonus). Dit is de laag erbovenop, in schermpixels, kind van de strook:
# - de klap-ster van Mila (kunst/klapster.png, 4 beelden van 16 x 16 spelpixels, 8 per seconde, één keer: 0,5 s) op de
#   plek van de val, wit-geel met een donkere rand (Iris #7: de oude witte stralen lazen als een stofwolk; Daan #45 ja);
# - "+9" in goud dat uit de aarde boven de val omhoog komt, eerst groot en dan op maat, en vervaagt;
# - bij een reeks (2 of meer vangsten op rij zonder dat er een ontsnapt) "x3" ernaast, warmer van kleur per stap.
# Alles blijft onder het maaiveld: op Windows tekent het venster niets buiten het muisvlak (kern/muisvlak.gd).
# Geen schermschudden, geen tijdsdruk. Rekent alleen als er iets te zien is (set_process uit als het leeg is: CPU).

const HOL := preload("res://hol/hol.gd")
const FREDOKA := preload("res://kunst/letters/Fredoka.ttf")
const KLAPSTER := preload("res://kunst/klapster.png")   # 4 beelden naast elkaar, 128 x 128 bladpixels per beeld
const STER_BEELDEN := 4
const STER_CEL := 16.0     # spelpixels per beeld (8 bladpixels per spelpixel)

const DUUR := 1.3          # zo lang staat het getal er
const POP_S := 0.12        # eerst groter, dan op maat
const VERVAAG_S := 0.35    # het laatste stuk vervaagt
const STER_S := 0.5        # de klap-ster: 4 beelden op 8 per seconde
const STIJG := 7.0         # spelpixels omhoog over de hele duur (blijft onder het maaiveld)
const GOUD := Color("#ffd75e")
const RAND := Color(0.16, 0.07, 0.02, 0.9)
# kleur van "x2", "x3", ... : van warm geel naar fel oranjerood
const REEKS_KLEUR := [Color("#ffe68a"), Color("#ffc23d"), Color("#ff9a2e"), Color("#ff6a2a"), Color("#ff4560")]

var schaal := 3
var hol_pos := Vector2.ZERO
var stil := false            # winkelbeeld: alles blijft staan op het hoogste punt
var bijs: Array = []         # {x, y (spelpixels, plek van de val), buit, reeks, t}
var letter: FontVariation
var ster_tex: CanvasTexture   # lineair gefilterd, net als de andere 3D-bladen (Mila)

func _ready() -> void:
	letter = FontVariation.new()
	letter.base_font = FREDOKA
	letter.variation_opentype = {TextServerManager.get_primary_interface().name_to_tag("wght"): 700}
	ster_tex = CanvasTexture.new()
	ster_tex.diffuse_texture = KLAPSTER
	ster_tex.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	set_process(false)

# Welk beeld van de klap-ster op tijd t (0 tot 3), of -1 als hij weg is.
static func ster_beeld(t: float) -> int:
	if t < 0.0 or t >= STER_S:
		return -1
	return clampi(int(t / STER_S * STER_BEELDEN), 0, STER_BEELDEN - 1)

# Een vangst op plek p (spelpixels van het hol): buit en de reeks na deze vangst.
func vangst(p: Vector2, buit: int, reeks: int) -> void:
	bijs.append({"x": p.x, "y": p.y, "buit": buit, "reeks": reeks, "t": 0.0})
	if bijs.size() > 3:
		bijs.pop_front()   # nooit meer dan drie tegelijk in beeld
	set_process(true)
	queue_redraw()

func bezig() -> bool:
	return not bijs.is_empty()

func _process(delta: float) -> void:
	var st = get_parent()
	if stil or (st != null and st.get("hol") != null and bool(st.hol.moment_val_vast)):
		return   # winkelbeeld: blijft staan zoals de muntjes
	for b in bijs:
		b.t += delta
	bijs = bijs.filter(func(b): return float(b.t) < DUUR)
	queue_redraw()
	if bijs.is_empty():
		set_process(false)

# maat van het getal in schermpixels: 8 spelpixels hoog, eerst 1,5 keer
static func maat(t: float, s: int) -> int:
	var basis := 8.0 * s
	if t < POP_S:
		var u := t / POP_S
		return int(round(basis * (1.5 - 0.5 * u)))
	return int(round(basis))

static func zicht(t: float) -> float:
	return clampf((DUUR - t) / VERVAAG_S, 0.0, 1.0)

static func reeks_kleur(r: int) -> Color:
	return REEKS_KLEUR[clampi(r - 2, 0, REEKS_KLEUR.size() - 1)]

func _draw() -> void:
	for b in bijs:
		var t: float = b.t
		var s := float(schaal)
		var mx: float = hol_pos.x + float(b.x) * s
		# klap-ster van Mila: midden van het beeld op de plek van de klap (midden van de gang)
		var sb := ster_beeld(t)
		if sb >= 0:
			var c := hol_pos + Vector2(float(b.x), float(HOL.GANG_BOVEN + 6)) * s
			var cel := float(KLAPSTER.get_width()) / STER_BEELDEN
			var maat_s := STER_CEL * s
			draw_texture_rect_region(ster_tex, Rect2(c - Vector2(maat_s, maat_s) / 2.0, Vector2(maat_s, maat_s)),
				Rect2(sb * cel, 0, cel, float(KLAPSTER.get_height())))
		# "+9" omhoog uit de aarde boven de val
		var omhoog := (1.0 - pow(1.0 - clampf(t / DUUR, 0.0, 1.0), 2.0)) * STIJG
		var y := hol_pos.y + (float(HOL.GANG_BOVEN) - 2.0 - omhoog) * s
		y = maxf(y, hol_pos.y + float(HOL.OPP + 7) * s)   # niet boven het maaiveld (dan tekent Windows het niet)
		var m := maat(t, schaal)
		var a := zicht(t)
		var tekst := "+%d" % int(b.buit)
		var breed := letter.get_string_size(tekst, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x
		var rt := ""
		var rm := int(round(m * 0.75))
		var rbreed := 0.0
		if int(b.reeks) >= 2:
			rt = "x%d" % int(b.reeks)
			rbreed = letter.get_string_size(rt, HORIZONTAL_ALIGNMENT_LEFT, -1, rm).x + s
		var x := mx - (breed + rbreed) / 2.0
		_omlijnd(Vector2(x, y), tekst, m, Color(GOUD, a), a)
		if rt != "":
			_omlijnd(Vector2(x + breed + s, y), rt, rm, Color(reeks_kleur(int(b.reeks)), a), a)

# tekst met een donkere rand van 1 schermpixel rondom en een schaduw eronder: leesbaar op aarde en op gras
func _omlijnd(p: Vector2, t: String, m: int, kleur: Color, a: float) -> void:
	var rand := Color(RAND, RAND.a * a)
	draw_string_outline(letter, p, t, HORIZONTAL_ALIGNMENT_LEFT, -1, m, maxi(2, schaal), rand)
	draw_string(letter, p + Vector2(0, maxf(1.0, schaal / 2.0)), t, HORIZONTAL_ALIGNMENT_LEFT, -1, m, rand)
	draw_string(letter, p, t, HORIZONTAL_ALIGNMENT_LEFT, -1, m, kleur)
