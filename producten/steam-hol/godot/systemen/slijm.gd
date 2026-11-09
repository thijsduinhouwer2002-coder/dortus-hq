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
# Hoedentoren (Mila, ontwerp/steam/mila/stijl.md; Sanne toets 3): elke held die hij at, zijn hoed komt op zijn hoofd.
const HOEDEN := preload("res://kunst/held_hoeden.png")   # 4 hoeden, 16 x 16, zelfde index als held.gd hoed_nr
const HOED_TOP := [2, 0, 2, 3]     # bovenste zichtbare rij per hoed (uit het plaatje gemeten)
const HOED_ONDER := [5, 5, 6, 5]   # onderste zichtbare rij per hoed
const RUST_TOP := [6, 7, 6, 6, 3, 7]                          # bovenkant van Gloop per frame in slijm.png
const LEVEN_TOP := [6, 7, 7, 3, 3, 6, 3, 7, 6, 7, 6, 10, 7]   # idem slijm_leven.png (plat = 10)
const OP_HOOFD := 4                # hooguit 4 op zijn hoofd, de rest op de hoedenberg
const SCHEEF := [0, 1, -1, 1]      # x-verschuiving om en om, zodat het wiebelt
const BERG_MAAT := [5, 25, 100, 300, 1000]   # vanaf zoveel hoeden in totaal wordt de berg een maat groter
const BERG_ZICHTBAAR := [0, 3, 6, 10, 15, 21] # hoeveel hoeden je per maat op de berg ziet (piramide)

var hol
var soort := "slijm"
var bijnaam_naam := "Gloop"
var plat_s := 60.0          # in het spel 60 s; strook.gd mag dit in de demo versnellen (Sanne toets 2, punt 1: ±9 s)
var gegeten := 0            # helden die hij kreeg ("Gloop has eaten 12 heroes")
var hoeden: Array[int] = [] # elke hoed die hij kreeg, oudste eerst. Een hoed gaat er nooit meer af (Sanne).
var keer_plat := 0
var t := 0.0
var hap_van := -10.0
var leven := ""            # "", "slapen" of "spugen"
var leven_van := -10.0
var gespuugd := 0           # laarzen uitgespuugd; hij spuugt alleen als hij meer helden at dan laarzen spuugde
var laars_op_vloer := false   # ligt de laars naast hem (8 s, dan haalt een wekker hem weg)
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
		laars_kant = 1 if rng.randf() < 0.5 or berg_maat() > 0 else -1   # links ligt de hoedenberg
	set_process(true)
	return leven

func laars_ligt() -> bool:
	return laars_op_vloer

func laars_weg() -> void:
	laars_op_vloer = false
	queue_redraw()

# Waar de laars is (onder-midden, ten opzichte van Gloop), in hele pixels: boogje van 12 px opzij in 0,3 s.
func laars_pos() -> Vector2i:
	if leven != "spugen":
		return Vector2i(16 * laars_kant, 0)   # geland: blijft liggen, ook als hij daarna slaapt
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

# Hij at een held. hoed = index in held_hoeden.png, of -1 als de hoed niet naar hem gaat
# (een afgerekende aartsvijand gaat met zijn hoed naar de wand, Sanne). Geeft het aantal hoeden terug.
func raak(hoed := -1) -> int:
	gegeten += 1
	hap_van = t
	if hoed >= 0:
		hoeden.append(hoed % 4)
	set_process(true)
	return hoeden.size()

func hoeden_op_hoofd() -> Array:
	return hoeden.slice(maxi(0, hoeden.size() - OP_HOOFD))

func hoeden_op_berg() -> int:
	return maxi(0, hoeden.size() - OP_HOOFD)

# Maat van de hoedenberg: 0 (geen berg) tot 5.
func berg_maat() -> int:
	var m := 0
	for grens in BERG_MAAT:
		if hoeden.size() >= grens:
			m += 1
	return m

# Bijnaam bij 25 en 100 hoeden (kroniek-regels.md). naam() blijft "Gloop the Slime", want de wrok van helden hangt daaraan.
func hoed_bijnaam() -> String:
	if hoeden.size() >= 100:
		return "Milliner"
	if hoeden.size() >= 25:
		return "Hatted"
	return ""

# Voor de hover in de strook (features.md): "Gloop wears 4 hats. 212 more in the pile."
func hover_regel() -> String:
	if hoeden.is_empty():
		return "%s has no hats yet." % bijnaam_naam
	var r := "%s wears %d hat%s." % [bijnaam_naam, hoeden_op_hoofd().size(), "" if hoeden.size() == 1 else "s"]
	if hoeden_op_berg() > 0:
		r += " %d more in the pile." % hoeden_op_berg()
	return r

# Bewaren in de save van Olaf (strook.gd): naar_dict() erin, van_dict() na zet().
func naar_dict() -> Dictionary:
	return {"hoeden": hoeden.duplicate(), "gegeten": gegeten, "gespuugd": gespuugd, "keer_plat": keer_plat}

func van_dict(d: Dictionary) -> void:
	hoeden.clear()
	for h in d.get("hoeden", []):
		hoeden.append(int(h) % 4)
	gegeten = maxi(int(d.get("gegeten", 0)), hoeden.size())
	gespuugd = int(d.get("gespuugd", 0))
	keer_plat = int(d.get("keer_plat", 0))
	queue_redraw()

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
		laars_op_vloer = true
		if is_inside_tree():
			get_tree().create_timer(LAARS_LIGT_S).timeout.connect(laars_weg)   # laars weg, zonder _process
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
		return [LEVEN, SLAPEN[int((t - leven_van) * FPS) % 2]]
	if leven == "spugen":
		return [LEVEN, SPUGEN[mini(SPUGEN.size() - 1, int((t - leven_van) * FPS))]]
	return [RUST, 0]

# Bovenkant van Gloop in het huidige frame (de toren volgt hem: hap, spugen, opstaan).
func top_nu() -> int:
	var f := frame_nu()
	var tabel: Array = RUST_TOP if f[0] == RUST else LEVEN_TOP
	return int(tabel[int(f[1])])

# Waar elke hoed van de toren staat: [hoed, x, y] (y = bovenkant van het 16 x 16 frame, Gloop-coordinaten).
# Rechtop: elke hoed met zijn onderste rij 1 px in de bovenkant van wat eronder staat. Plat: de toren valt mee,
# de hoeden liggen op de vloer rechts naast hem en staan weer op als hij opstaat.
func toren() -> Array:
	var uit := []
	var op := hoeden_op_hoofd()
	if is_plat():
		for i in op.size():
			uit.append([op[i], 9 + 6 * i, -1 - int(HOED_ONDER[op[i]])])
		return uit
	var boven := -16 + top_nu()
	for i in op.size():
		var h: int = op[i]
		var y := boven - int(HOED_ONDER[h])
		uit.append([h, int(SCHEEF[i]), y])
		boven = y + int(HOED_TOP[h])
	return uit

# Hoedenberg links naast hem: een piramide van hoeden, groter per maat. [hoed, x, y].
func berg() -> Array:
	var uit := []
	var n: int = mini(int(BERG_ZICHTBAAR[berg_maat()]), hoeden_op_berg())
	if n <= 0:
		return uit
	var rij := 0
	var in_rij := 1
	while in_rij * (in_rij + 1) < 2 * n:
		in_rij += 1          # breedte van de onderste rij
	var k := 0
	var breedte := in_rij
	while k < n and breedte > 0:
		for j in breedte:
			if k >= n:
				break
			var h: int = hoeden[k]   # de oudste hoeden liggen op de berg
			var x := -10 - 6 * (in_rij - 1) + 6 * j + 3 * rij
			uit.append([h, x, -1 - int(HOED_ONDER[h]) - 3 * rij])
			k += 1
		rij += 1
		breedte -= 1
	return uit

func _draw() -> void:
	for b in berg():
		draw_texture_rect_region(HOEDEN, Rect2(int(b[1]) - 8, int(b[2]), 16, 16), Rect2(int(b[0]) * 16, 0, 16, 16))
	var f := frame_nu()
	draw_texture_rect_region(f[0], Rect2(-8, -16, 16, 16), Rect2(int(f[1]) * 16, 0, 16, 16))
	for h in toren():
		draw_texture_rect_region(HOEDEN, Rect2(int(h[1]) - 8, int(h[2]), 16, 16), Rect2(int(h[0]) * 16, 0, 16, 16))
	if leven == "slapen":
		var zy := -25
		for h in toren():
			zy = mini(zy, int(h[2]) + int(HOED_TOP[int(h[0])]) - 9)   # zzz boven de hoedentoren
		draw_texture_rect_region(TEKENS, Rect2(-4, zy, 8, 8), Rect2(3 * 8, 0, 8, 8))   # zzz
	if (leven == "spugen" and t >= leven_van + 0.6) or laars_ligt():
		var p := laars_pos()
		draw_texture_rect_region(LAARS, Rect2(p.x - 4, p.y - 8, 8, 8), Rect2(0, 0, 8, 8))
