extends Node2D
# Bewoner: slijm (Bram). strook.gd gebruikt dit bestand in plaats van kern/standin_slijm.gd.
# Zelfde vorm als de stand-in: zet(hol, kol), is_bewoner(), naam(), raak(); extra: plat(), kan_vechten(), soort.
# Regel van Sanne (features.md): een bewoner gaat nooit dood. Verliest hij, dan is hij even plat en staat weer op.
# Zuinig: staat stil als er niets gebeurt (alleen tekenen bij een hap, plat zijn of opstaan).
# Kunst (Daan 19:45, kunst/LEESMIJ.md): rust uit slijm.png (frame 0), hap, plat en opstaan uit slijm_leven.png.
# Nooit schalen: plat is een eigen frame, schalen maakt halve pixels.

const RUST := preload("res://kunst/slijm.png")          # 16 x 16, rust 0..3
const LEVEN := preload("res://kunst/slijm_leven.png")   # 16 x 16: slapen 0-1, spugen 2-5, hap 6-10, plat 11, opstaan 12
const HAP := [6, 7, 8, 9, 10]
const PLAT := 11
const OPSTAAN := 12
const FPS := 5.0
const HAP_S := 1.0          # 5 frames op 5 fps
const OPSTAAN_S := 0.4
const LAARS := preload("res://kunst/laars.png")         # 8 x 8, de laars van een held die hij at
const TEKENS := preload("res://kunst/tekens.png")       # zzz = frame 3
const SLAPEN := [0, 1]
const SPUGEN := [2, 3, 4, 5]
const SLAAP_S := 4.0
const SPUUG_S := 0.8        # 4 frames op 5 fps
const BOOG_S := 0.3
const LAARS_LIGT_S := 8.0
const LEVEN_MIN_S := 20.0   # Daan: een leven-animatie hooguit eens per 20 tot 40 s, alleen als er geen held is
const LEVEN_MAX_S := 40.0

var hol
var soort := "slijm"
var bijnaam_naam := "Gloop"
var plat_s := 60.0          # in het spel 60 s; strook.gd mag dit in de demo versnellen (Sanne toets 2, punt 1: ±9 s)
var gegeten := 0            # helden die hij kreeg ("Gloop has eaten 12 heroes")
var keer_plat := 0
var t := 0.0
var hap_van := -10.0
var leven := ""            # "", "slapen" of "spugen"
var leven_van := -10.0
var gespuugd := 0           # laarzen uitgespuugd; hij spuugt alleen als hij meer helden at dan laarzen spuugde
var laars_tot := -10.0      # tot wanneer de laars naast hem op de vloer ligt
var laars_kant := 1         # 1 rechts, -1 links
var rng := RandomNumberGenerator.new()
var plat_tot := -10.0       # was 0.0: dan stond hij bij de start in "opstaan" en bleef zo (Olaf 19:55, GEZIEN in run 42682511064)

func zet(h, kol: int) -> void:
	hol = h
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	position = hol.cel_naar_pos(Vector2i(kol, 0))
	set_process(false)
	queue_redraw()
	rng.seed = hash([kol, "gloop"])
	_plan_leven()

# Zuinig: geen _process tussendoor, alleen een wekker voor de volgende leven-animatie.
func _plan_leven() -> void:
	if is_inside_tree():
		get_tree().create_timer(rng.randf_range(LEVEN_MIN_S, LEVEN_MAX_S)).timeout.connect(_wek)

func _wek() -> void:
	begin_leven()
	_plan_leven()

func _held_in_de_buurt() -> bool:
	if get_parent() == null:
		return false
	for w in get_parent().get_children():
		if w != self and w.has_method("is_held"):
			return true
	return false

# Slapen of spugen, alleen als hij rustig is en er geen held is. Geeft terug wat hij deed ("" = niets).
func begin_leven() -> String:
	if is_plat() or t < hap_van + HAP_S or leven != "" or _held_in_de_buurt():
		return ""
	leven = "spugen" if gegeten > gespuugd else "slapen"
	leven_van = t
	if leven == "spugen":
		gespuugd += 1
		laars_kant = 1 if rng.randf() < 0.5 else -1
	set_process(true)
	return leven

func laars_ligt() -> bool:
	return t < laars_tot

# Waar de laars is (onder-midden, ten opzichte van Gloop), in hele pixels: boogje van 12 px opzij in 0,3 s.
func laars_pos() -> Vector2i:
	var u := clampf((t - (leven_van + 0.6)) / BOOG_S, 0.0, 1.0)   # vliegt na spugen-frame 3 (index 3 = 0,6 s)
	var x := int(round(12.0 * u)) * laars_kant
	var y := -int(round(8.0 * u * (1.0 - u) * 4.0 / 2.0))
	return Vector2i(x + 4 * laars_kant, y)

func is_bewoner() -> bool:
	return true

func naam() -> String:
	return "%s the Slime" % bijnaam_naam

func kan_vechten() -> bool:
	return t >= plat_tot

func is_plat() -> bool:
	return t < plat_tot

func raak() -> void:
	gegeten += 1
	hap_van = t
	set_process(true)

func plat() -> void:
	keer_plat += 1
	plat_tot = t + plat_s
	set_process(true)

func regel_plat() -> String:
	return "%s is flat. Back in a minute." % bijnaam_naam

func _process(delta: float) -> void:
	stap(delta)

func stap(delta: float) -> void:
	t += delta
	queue_redraw()
	if leven == "slapen" and (t > leven_van + SLAAP_S or _held_in_de_buurt() or is_plat()):
		leven = ""             # een held komt binnen: wakker
	elif leven == "spugen" and t > leven_van + 0.6 + BOOG_S:
		leven = ""
		laars_tot = t + LAARS_LIGT_S
		if is_inside_tree():
			get_tree().create_timer(LAARS_LIGT_S + 0.05).timeout.connect(queue_redraw)   # laars weg, zonder _process
	if leven == "" and t > hap_van + HAP_S and t > plat_tot + OPSTAAN_S:
		set_process(false)

# Welk frame uit welk blad: [blad, frame]. Los zodat de toetsen het kunnen nakijken.
func frame_nu() -> Array:
	if t < hap_van + HAP_S:
		return [LEVEN, HAP[mini(HAP.size() - 1, int((t - hap_van) * FPS))]]
	if t < plat_tot:
		return [LEVEN, PLAT]
	if t < plat_tot + OPSTAAN_S:
		return [LEVEN, OPSTAAN]
	if leven == "slapen":
		return [LEVEN, SLAPEN[int((t - leven_van) * 2.0) % 2]]
	if leven == "spugen":
		return [LEVEN, SPUGEN[mini(SPUGEN.size() - 1, int((t - leven_van) * FPS))]]
	return [RUST, 0]

func _draw() -> void:
	var f := frame_nu()
	draw_texture_rect_region(f[0], Rect2(-8, -16, 16, 16), Rect2(int(f[1]) * 16, 0, 16, 16))
	if leven == "slapen":
		draw_texture_rect_region(TEKENS, Rect2(-4, -25, 8, 8), Rect2(3 * 8, 0, 8, 8))   # zzz
	if (leven == "spugen" and t >= leven_van + 0.6) or laars_ligt():
		var p := laars_pos()
		draw_texture_rect_region(LAARS, Rect2(p.x - 4, p.y - 8, 8, 8), Rect2(0, 0, 8, 8))
