extends Node2D
# Bewoner: slijm (Bram). strook.gd gebruikt dit bestand in plaats van kern/standin_slijm.gd.
# Zelfde vorm als de stand-in: zet(hol, kol), is_bewoner(), naam(), raak(); extra: plat(), kan_vechten(), soort.
# Regel van Sanne (features.md): een bewoner gaat nooit dood. Verliest hij, dan is hij even plat en staat weer op.
# Zuinig: staat stil als er niets gebeurt (alleen tekenen bij een hap, plat zijn of opstaan).
# Kunst (Daan 19:45, kunst/LEESMIJ.md): rust uit slijm.png (frame 0), hap, plat en opstaan uit slijm_leven.png.
# Nooit schalen: plat is een eigen frame, schalen maakt halve pixels.

const RUST := preload("res://kunst/slijm.png")          # 16 x 16, rust 0..3
const LEVEN := preload("res://kunst/slijm_leven.png")   # 16 x 16: slapen 0-1, spugen 2-5, hap 6-10, plat 11, opstaan 12
# Upgrades per stap (Mila 10 nov 02:55, ontwerp/steam/mila/gloop-upgrades-10x.png). Stappen stapelen: Royal heeft ook Big en Bouncy.
# Big Gloop (niveau 1+): eigen bladen, lijf 1 spelpixel groter rondom getekend (niet geschaald), zelfde indeling en frames.
const RUST_GROOT := preload("res://kunst/slijm_groot2.png")    # frames 20 x 16 (Mila 04:55: 2 spelpixels groter rondom)
const LEVEN_GROOT := preload("res://kunst/slijm_leven_groot2.png")
const UPG := preload("res://kunst/slijm_upgrades2.png")  # cel 0 (x 0, 20 breed) glansster, cel 1 (x 20, 28 breed) mantel achter, cel 2 (x 48, 20 breed) bovenzoom met gesp voor
const KOOP_S := 0.6         # het moment van kopen: 3 beelden op 5 fps (Sanne toets 8 punt 1: Gloop wipt en zwelt)
const KOOP_WIP := [-2, -3, -1]   # hoeveel spelpixels hij omhoog is per beeld; in beeld 0 nog het oude lijf, daarna het nieuwe
const HAP := [6, 7, 8, 9, 10]
const PLAT := 11
const OPSTAAN := 12
const FPS := 5.0
const HAP_S := 1.0          # 5 frames op 5 fps
const OPSTAAN_S := 0.4
const LAARS := preload("res://kunst/laars.png")         # 8 x 8, de laars van een held die hij at
const TEKENS := preload("res://kunst/tekens.png")       # zzz = frame 3
const HELD_BEELD := preload("res://systemen/held_beeld.gd")   # teken_3d(): zzz in 3D als het blad er is
const SLAPEN := [0, 1]
const SPUGEN := [2, 3, 4, 5]
const SLAAP_S := 4.0
const SPUUG_S := 0.8        # 4 frames op 5 fps
const BOOG_S := 0.3
const LAARS_LIGT_S := 8.0
const LEVEN_MIN_S := 20.0   # Daan: een leven-animatie hooguit eens per 20 tot 40 s, alleen als er geen held is
const LEVEN_MAX_S := 40.0
# Hoedentoren (Mila, ontwerp/steam/mila/stijl.md; Sanne toets 3): elke held die hij at, zijn hoed komt op zijn hoofd.
const HOEDEN := preload("res://kunst/held_hoeden.png")   # 10 hoeden, 16 x 16, zelfde index als held.gd hoed_nr
const HOED_SOORTEN := 10           # Mila 21:55: helm, puntmuts, kap, pet, kroon, koksmuts, emmer, hoge hoed, pan, veermuts
const HOED_TOP := [0, 0, 2, 3, 2, 0, 0, 0, 2, 0]     # bovenste zichtbare rij per hoed (Mila; 23:00 helm met kam 0, 23:10 kroon 2 zodat de hoed erboven tussen de punten zakt)
const HOED_ONDER := [5, 5, 6, 5, 5, 5, 5, 5, 5, 5]   # onderste zichtbare rij per hoed
const RUST_TOP := [6, 7, 6, 6, 3, 7]                          # bovenkant van Gloop per frame in slijm.png
const LEVEN_TOP := [6, 7, 7, 3, 3, 6, 3, 7, 6, 7, 6, 10, 7]   # idem slijm_leven.png (plat = 10)
const OP_HOOFD := 4                # hooguit 4 op zijn hoofd, de rest op de hoedenberg
const SCHEEF := [0, 1, -1, 1]      # x-verschuiving om en om, zodat het wiebelt
const BERG_MAAT := [5, 25, 100, 300, 1000, 3000]   # vanaf zoveel hoeden wordt de berg een maat groter (Sanne 21:50: zesde maat bij 3000)
const BERG_ZICHTBAAR := [0, 3, 6, 10, 15, 21, 33] # hoeveel hoeden je per maat op de berg ziet
const BERG_RIJEN := 6              # maat 6 wordt breder, niet hoger dan maat 5 (Gloops plek is twee rijen, Sanne)
# 3D-lijf (Bram 13 nov, besluit Thijs 13:35, ontwerp/steam/3d-stijl.md): gerenderd door producten/steam-hol/pijplijn/.
# Staat kunst/3d/gloop.png er, dan tekent hij dat lijf voor rust, slapen, plat, opstaan, hap, blij en knipper;
# spugen blijft voorlopig het pixelbeeld tot Daan die in 3D heeft. Filter lineair alleen voor dit lijf (CanvasTexture), de
# pixelhoeden blijven scherp. Klein lijf = 0,8 x het grote (zelfde verhouding als 16 en 20 breed).
const LIJF3D_JSON := "res://kunst/3d/sprites.json"
static var lijf3d: CanvasTexture = null
static var lijf3d_info := {}
static var lijf3d_gezocht := false
const HB := preload("res://systemen/held_beeld.gd")   # laadt ook het 3D-hoedenblad (kunst/3d/sprites.json)
var met_3d := true                 # uit = de oude pixel-Gloop (toetsen, of terug als het tegenvalt)
# Standen van Daan (13 nov 16:30, gloop.py 7e woord): knipperen elke 4 tot 7 s, blij als er een hoed op de toren
# komt, hap bij opeten. Alleen in 3D en alleen als die stand in het blad staat (anders gewoon rust).
const KNIPPER_MIN_S := 4.0
const KNIPPER_MAX_S := 7.0
const KNIPPER_S := 0.2
const BLIJ_S := 1.2
var knipper_tot := -10.0
var blij_tot := -10.0
var rng_oog := RandomNumberGenerator.new()   # eigen dobbelsteen, zodat de leven-wekker gelijk blijft

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
var koop_van := -10.0       # wanneer de laatste upgrade gekocht werd (vier_koop)
var laatste_beeld := []      # wat er het laatst getekend is (sleutel in _teken_als_anders); alleen opnieuw tekenen als dat verandert
var plat_tot := -10.0       # was 0.0: dan stond hij bij de start in "opstaan" en bleef zo (Olaf 19:55, GEZIEN in run 42682511064)

func zet(h, kol: int) -> void:
	hol = h
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	position = hol.cel_naar_pos(Vector2i(kol, 0))
	set_process(false)
	queue_redraw()
	rng.seed = hash([kol, "gloop"])
	rng_oog.seed = hash([kol, "oog"])
	_plan_leven()
	_plan_knipper()
	_toren_uit_argument(OS.get_cmdline_user_args())

# Alleen voor de strooktest (Daan 13 nov 22:55: de 3D-toren keuren met 4 tot 6 hoeden): argument toren=0,4,5,1,6 geeft Gloop
# die hoeden, oudste eerst (nummers als in held.gd). Alleen samen met vers=1. Zonder argument niets.
func _toren_uit_argument(args: PackedStringArray) -> void:
	if not args.has("vers=1"):
		return   # alleen in een vers spel, anders komen de hoeden voorgoed in een echte save (controleur Olaf 23:40)
	for a in args:
		if a.begins_with("toren="):
			for h in a.substr(6).split(",", false):
				if h.is_valid_int():
					hoeden.append(absi(int(h)) % HOED_SOORTEN)
			gegeten = maxi(gegeten, hoeden.size())
			queue_redraw()

# Zuinig: geen _process tussendoor, alleen een wekker voor de volgende leven-animatie.
func _plan_leven() -> void:
	if is_inside_tree():
		get_tree().create_timer(rng.randf_range(LEVEN_MIN_S, LEVEN_MAX_S)).timeout.connect(_wek)

func _wek() -> void:
	begin_leven()
	_plan_leven()

# Knipperen: een wekker, en alleen 0,2 s _process (zuinig, demolijst 2).
func _plan_knipper() -> void:
	if is_inside_tree():
		get_tree().create_timer(rng_oog.randf_range(KNIPPER_MIN_S, KNIPPER_MAX_S)).timeout.connect(_knipper)

func _knipper() -> void:
	knipper()
	_plan_knipper()

func knipper() -> bool:
	if not _heeft_3d("knipper") or is_plat() or leven != "" or t < blij_tot:
		return false
	knipper_tot = t + KNIPPER_S
	set_process(true)
	return true

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

# Keurstrook (Bram 14 nov, laars_proef=1 in strook.gd): de laars ligt vast rechts naast hem, zonder timer,
# zodat de 3D-laars in de echte strook te keuren is. Spuugt hij later echt, dan gaat alles weer zoals altijd.
func zet_laars_proef() -> void:
	laars_kant = 1
	laars_op_vloer = true
	queue_redraw()

# Waar de laars is (onder-midden, ten opzichte van Gloop), in hele pixels: boogje van 12 px opzij in 0,3 s.
func laars_pos() -> Vector2i:
	if leven != "spugen":
		return Vector2i(16 * laars_kant, 0)   # geland: blijft liggen, ook als hij daarna slaapt
	var u := clampf((t - (leven_van + 0.6)) / BOOG_S, 0.0, 1.0)   # vliegt na spugen-frame 3 (index 3 = 0,6 s)
	var x := int(round(12.0 * u)) * laars_kant
	var y := -int(round(8.0 * u * (1.0 - u) * 4.0 / 2.0))
	return Vector2i(x + 4 * laars_kant, y)

# Welke upgrade-stap Gloop heeft (0 tot 3), uit hol.upgrades (systemen/upgrades.gd). Zonder upgrades 0.
func niveau() -> int:
	if hol != null and "upgrades" in hol and hol.get("upgrades") != null:
		return int(hol.get("upgrades").niveau("slijm"))
	return 0

# Na "Buy" op het kaartje (kern/kaartje.gd): Gloop wipt omhoog en zwelt in 3 beelden (0,6 s) naar zijn nieuwe lijf.
func vier_koop() -> void:
	koop_van = t
	set_process(true)
	queue_redraw()

# Na "Undo" of laden: alleen opnieuw tekenen, zonder feestje. Een koop-moment dat nog liep stopt meteen
# (controleur 04:22: Undo binnen 0,6 s liet de wip doorlopen).
func upgrade_veranderd() -> void:
	koop_van = -10.0
	queue_redraw()

# Hoeveel spelpixels hij nu omhoog is door het koop-moment (0 of negatief).
func wip_nu() -> int:
	if _rust_som or t < koop_van or t >= koop_van + KOOP_S or is_plat():
		return 0
	return int(KOOP_WIP[mini(KOOP_WIP.size() - 1, int((t - koop_van) * FPS))])

# Het hoogste punt van Gloop met alles wat hij draagt (Gloop-coordinaten, y omhoog negatief): de bovenste hoed,
# anders zijn kruin, de glansster of de zzz niet meegerekend. Voor het muntje erboven (Sanne toets 8 punt 2: 3 spelpixels boven het bovenste).
func hoogste_punt() -> int:
	var y := -16 + top_nu() + wip_nu()
	var t3 := toren_3d()
	if not t3.is_empty():
		for h3 in t3:
			y = mini(y, int(floor(float(h3[3]) + 0.001)))   # marge: precies op het plafond niet 1 te hoog
		return y
	for h in toren():
		y = mini(y, int(h[2]) + int(HOED_TOP[int(h[0])]))
	return y

# Zelfde som als hoogste_punt(), maar met het rust-frame en zonder wip (Olaf 14 nov 01:50, voor kaartje.gd munt_top()):
# knipperen, blij, hap en het koop-moment laten het muntje dan niet meewippen, en het plafond telt wel mee.
# Plat telt gewoon (dan liggen de hoeden op de vloer). Gloop-coordinaten, y omhoog negatief.
var _rust_som := false
func hoogste_punt_rust() -> int:
	_rust_som = true
	var y := hoogste_punt()
	_rust_som = false
	return y

func is_bewoner() -> bool:
	return true

func naam() -> String:
	return "%s the Slime" % bijnaam_naam

func kan_vechten() -> bool:
	return t >= plat_tot

func is_plat() -> bool:
	return t < plat_tot

# Hij at een held. hoed = index in held_hoeden.png, of -1 als de hoed niet naar hem gaat
# (later: een afgerekende aartsvijand naar de wand, zodra die te zien is; tot dan krijgt de bewoner ook zijn hoed, Sanne 22:55). Geeft het aantal hoeden terug.
func raak(hoed := -1) -> int:
	gegeten += 1
	hap_van = t
	if hoed >= 0:
		hoeden.append(hoed % HOED_SOORTEN)
		blij_tot = t + HAP_S + BLIJ_S     # na de hap even blij om de nieuwe hoed
	set_process(true)
	return hoeden.size()

# Een hoed erbij zonder hap-animatie (voortgang terwijl je weg was, Voortgang.geef_hoeden).
func krijg_hoed(hoed: int) -> int:
	gegeten += 1
	hoeden.append(absi(hoed) % HOED_SOORTEN)
	queue_redraw()
	return hoeden.size()

func hoeden_op_hoofd() -> Array:
	return hoeden.slice(maxi(0, hoeden.size() - OP_HOOFD))

func hoeden_op_berg() -> int:
	return maxi(0, hoeden.size() - OP_HOOFD)

# Maat van de hoedenberg: 0 (geen berg) tot 6.
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
		hoeden.append(absi(int(h)) % HOED_SOORTEN)
	gegeten = maxi(int(d.get("gegeten", 0)), hoeden.size())
	gespuugd = int(d.get("gespuugd", 0))
	keer_plat = int(d.get("keer_plat", 0))
	queue_redraw()

func plat() -> void:
	keer_plat += 1
	var duur := plat_s
	if hol != null and "upgrades" in hol and hol.get("upgrades") != null:
		duur = plat_s * hol.get("upgrades").plat_factor()   # Bouncy Gloop (systemen/upgrades.gd): 40 s in plaats van 60
	plat_tot = t + duur
	set_process(true)

func regel_plat() -> String:
	return "%s is flat. Back in a minute." % bijnaam_naam

func _process(delta: float) -> void:
	stap(delta)

func stap(delta: float) -> void:
	t += delta
	if leven == "slapen" and (t > leven_van + SLAAP_S or _held_in_de_buurt() or is_plat()):
		leven = ""             # een held komt binnen: wakker
	elif leven == "spugen" and t > leven_van + 0.6 + BOOG_S:
		leven = ""
		laars_op_vloer = true
		if is_inside_tree():
			get_tree().create_timer(LAARS_LIGT_S).timeout.connect(laars_weg)   # laars weg, zonder _process
	if leven == "" and t > hap_van + HAP_S and t > plat_tot + OPSTAAN_S and t > koop_van + KOOP_S and t > blij_tot and t > knipper_tot:
		set_process(false)
	_teken_als_anders()

# Demolijst 2 (Olaf 13 nov, CPU): plat ligt hij 60 s stil in hetzelfde beeld, maar elk beeld werd opnieuw getekend
# (duurtest: 15 beelden per seconde zonder held). Nu alleen tekenen als wat je ziet verandert. Andere functies die
# de berg of de toren veranderen roepen zelf queue_redraw aan.
func _teken_als_anders() -> void:
	var nu := [frame_nu(), beeld_3d(), wip_nu(), leven, laars_ligt(), laars_pos() if leven == "spugen" else Vector2i.ZERO, hoeden.size(), niveau(), is_plat()]
	if nu != laatste_beeld:
		laatste_beeld = nu
		queue_redraw()

# Welk frame uit welk blad: [blad, frame]. Los zodat de toetsen het kunnen nakijken.
# Vanaf Big Gloop uit de grote bladen; in het eerste beeld van het koop-moment nog het oude (klein) lijf.
func frame_nu() -> Array:
	var f := _frame_klein()
	if is_groot():
		f[0] = RUST_GROOT if f[0] == RUST else LEVEN_GROOT
	return f

func is_groot() -> bool:
	var n := niveau()
	if n == 1 and not _rust_som and t >= koop_van and t < koop_van + 1.0 / FPS:
		return false     # net Big gekocht: beeld 0 nog klein, dan zwelt hij
	return n >= 1

func _frame_klein() -> Array:
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

# 3D-lijf laden (één keer voor alle slijmen). Leeg als de pijplijn nog niets maakte.
static func _laad_3d() -> void:
	if lijf3d_gezocht:
		return
	lijf3d_gezocht = true
	if not FileAccess.file_exists(LIJF3D_JSON):
		return
	var d = JSON.parse_string(FileAccess.get_file_as_string(LIJF3D_JSON))
	if typeof(d) != TYPE_DICTIONARY or not d.has("gloop") or not ResourceLoader.exists(str(d["gloop"]["blad"])):
		return
	lijf3d_info = d["gloop"]
	lijf3d = CanvasTexture.new()
	lijf3d.diffuse_texture = load(str(lijf3d_info["blad"]))
	lijf3d.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS

# Welk 3D-beeld nu (rust, plat, hap, blij, knipper), of "" als het pixelbeeld moet (spugen, of geen 3D).
func beeld_3d() -> String:
	if not met_3d:
		return ""
	_laad_3d()
	if lijf3d == null:
		return ""
	var f := _frame_klein()
	if _rust_som and not is_plat():
		return "rust" if _heeft_3d("rust") else ""
	if f[0] == LEVEN and HAP.has(f[1]) and t < hap_van + HAP_S:
		return "hap" if _heeft_3d("hap") else ""
	if f[0] == LEVEN and (f[1] == PLAT):
		return "plat"
	if f[0] == RUST or (f[0] == LEVEN and (f[1] == OPSTAAN or SLAPEN.has(f[1]))):
		if f[0] == RUST and t < blij_tot and _heeft_3d("blij"):
			return "blij"
		if (f[0] == RUST and t < knipper_tot or f[0] == LEVEN and SLAPEN.has(f[1])) and _heeft_3d("knipper"):
			return "knipper"     # slapen = ogen dicht
		return "rust"
	return ""

func _heeft_3d(naam: String) -> bool:
	_laad_3d()
	return met_3d and lijf3d != null and lijf3d_info["frames"].has(naam)

# Het 3D-lijf tekenen met de onderkant op de vloer (y = 0 + wip), x = 0 in het midden van Gloop.
func _teken_3d(naam: String, wip: int) -> void:
	var i: int = lijf3d_info["frames"].find(naam)
	var cw: float = lijf3d_info["cel_px"][0]
	var ch: float = lijf3d_info["cel_px"][1]
	var px: float = lijf3d_info["px"]
	var k := 1.0 if is_groot() else 0.8
	var w := cw / px * k
	var h := ch / px * k
	var x := -float(lijf3d_info["anker_x"]) / px * k
	draw_texture_rect_region(lijf3d, Rect2(x, -h + wip, w, h), Rect2(i * cw, 0, cw, ch))

# Bovenkant van Gloop in het huidige frame (de toren volgt hem: hap, spugen, opstaan).
func top_nu() -> int:
	var b3 := beeld_3d()
	if b3 != "":
		var ch: float = float(lijf3d_info["cel_px"][1]) / float(lijf3d_info["px"])
		var top3: float = lijf3d_info["top"][lijf3d_info["frames"].find(b3)]
		var k := 1.0 if is_groot() else 0.8
		return int(round(16.0 - (ch - top3) * k)) + 1   # +1: de onderste hoedrij zakt 1 px in zijn kruin, zoals bij de pixels
	var f := frame_nu()
	if _rust_som and not is_plat():
		f = [RUST_GROOT if is_groot() else RUST, 0]
	var tabel: Array = RUST_TOP if (f[0] == RUST or f[0] == RUST_GROOT) else LEVEN_TOP
	var top := int(tabel[int(f[1])])
	if f[0] == RUST_GROOT or f[0] == LEVEN_GROOT:
		top -= 2     # het grote lijf is 2 spelpixels hoger (Mila 04:55), dan zakt de toren niet in zijn kruin
	return top

# Waar elke hoed van de toren staat: [hoed, x, y] (y = bovenkant van het 16 x 16 frame, Gloop-coordinaten).
# Rechtop: elke hoed met zijn onderste rij 1 px in de bovenkant van wat eronder staat. Plat: de toren valt mee,
# de hoeden liggen op de vloer rechts naast hem en staan weer op als hij opstaat.
func toren() -> Array:
	var uit := []
	var op := hoeden_op_hoofd()
	if is_plat():
		for i in op.size():
			uit.append([op[i], (11 if is_groot() else 9) + 6 * i, -1 - int(HOED_ONDER[op[i]])])   # groot lijf is 20 breed
		return uit
	var extra := 0
	for ronde in 2:   # plafond, zoals in toren_3d(), in hele pixels
		uit.clear()
		var boven := -16 + top_nu() + wip_nu()
		for i in op.size():
			var h: int = op[i]
			var y := boven - int(HOED_ONDER[h])
			uit.append([h, int(SCHEEF[i]), y])
			boven = y + int(HOED_TOP[h]) + extra
		if ronde == 0:
			var stijg_px := 99
			for hp in op.slice(1):
				stijg_px = mini(stijg_px, int(HOED_ONDER[hp]) - int(HOED_TOP[hp]))
			extra = mini(int(ceil(toren_extra(float(uit[-1][2] + int(HOED_TOP[int(uit[-1][0])])) if uit else 0.0, op.size()))), maxi(0, stijg_px - 1))
			if extra <= 0:
				break
	return uit

# De toren met de 3D-hoeden (Bram 13 nov 22:40): zelfde volgorde en scheefstand als toren(), maar elke hoed staat met
# zijn nulpunt (midden van de onderrand) 1 spelpixel in de bovenkant van wat eronder staat, gemeten in het hoedenblad,
# zodat een hoed nooit zweeft (Daan). [hoed, x, y van het nulpunt, bovenkant]. Leeg als het blad er niet is.
func toren_3d() -> Array:
	var uit := []
	if not met_3d or beeld_3d() == "":
		return uit
	HB._laad_3d()
	if not HB.held3d.has(HB.HOEDEN3D):
		return uit
	var hi: Dictionary = HB.held3d[HB.HOEDEN3D][1]
	var px: float = float(hi["px"])
	var ch: float = float(hi["cel_px"][1]) / px
	var op := hoeden_op_hoofd()
	if is_plat():
		for i in op.size():
			uit.append([op[i], (11 if is_groot() else 9) + 6 * i, 0.0, -ch])
		return uit
	# Plafond (Daan 14 nov 00:40): eerst stapelen zoals altijd; komt de bovenste hoed hoger dan PLAFOND spelpixels onder de
	# bovenrand van het hol, dan schuiven alle hoeden gelijk verder in elkaar (extra overlap per hoed), nooit afsnijden.
	var extra := 0.0
	for ronde in 2:
		uit.clear()
		var boven := float(-16 + top_nu() + wip_nu())
		for i in op.size():
			var h: int = op[i]
			var ny: float = float(hi["nul_y"][h]) if hi.has("nul_y") else ch
			var top: float = float(hi["top"][h]) if hi.has("top") else 0.0
			var nul := boven
			var bovenkant := nul - (ny - top)
			uit.append([h, int(SCHEEF[i]), nul, bovenkant])
			boven = bovenkant + HB.HOED_IN_KOP + extra
		if ronde == 0:
			var stijg := 99.0   # kan-punt controleur: van elke hoed blijft minstens 1 spelpixel rand boven de vorige
			for k in range(1, uit.size()):
				stijg = minf(stijg, float(uit[k - 1][3]) - float(uit[k][3]))
			extra = minf(toren_extra(float(uit[-1][3]) if uit else 0.0, op.size()), maxf(0.0, stijg - 1.0))
			if extra <= 0.0:
				break
	return uit

# Hoeveel spelpixels elke hoed extra in de vorige moet zakken zodat de bovenkant van de toren (Gloop-coordinaten) niet
# boven het plafond komt. 0 als het past of als er maar één hoed is (die zit al op zijn kop). Hooguit TOREN_MAX_EXTRA,
# dan blijft van elke hoed nog een rand zichtbaar.
const PLAFOND := 2.0
const TOREN_MAX_EXTRA := 6.0
func plafond_y() -> float:
	return PLAFOND - position.y   # bovenrand van het hol (hol-y 0) in Gloop-coordinaten, plus 2
# Hoogste y voor de bovenkant van een teken (zzz): 1 spelpixel onder de bovenrand van het hol (Daan 14 nov 01:40).
const TEKEN_RAND := 1.0
func teken_rand_y() -> float:
	return TEKEN_RAND - position.y
func toren_extra(bovenkant: float, n: int) -> float:
	if n < 2 or bovenkant >= plafond_y():
		return 0.0
	return minf((plafond_y() - bovenkant) / float(n - 1), TOREN_MAX_EXTRA)

# Eén 3D-hoed tekenen met zijn nulpunt op (x, nul). hap = uit het blad met de tandbogen (als dat er is).
func _teken_hoed_3d(h: int, x: float, nul: float, hap: bool) -> void:
	var naam: String = HB.HOEDEN3D_HAP if hap and HB.held3d.has(HB.HOEDEN3D_HAP) else HB.HOEDEN3D
	var ct: CanvasTexture = HB.held3d[naam][0]
	var hi: Dictionary = HB.held3d[naam][1]
	var px: float = float(hi["px"])
	var cw: float = float(hi["cel_px"][0])
	var ch: float = float(hi["cel_px"][1])
	var ny: float = float(hi["nul_y"][h]) if hi.has("nul_y") else ch / px
	draw_texture_rect_region(ct, Rect2(x - float(hi["anker_x"]) / px, nul - ny, cw / px, ch / px), Rect2(h * cw, 0, cw, ch))

# Hoedenberg links naast hem: een piramide van hoeden, groter per maat. [hoed, x, y].
func berg() -> Array:
	var uit := []
	var n: int = mini(int(BERG_ZICHTBAAR[berg_maat()]), hoeden_op_berg())
	if n <= 0:
		return uit
	var rij := 0
	var in_rij := 1
	while _past_op_berg(in_rij) < n:
		in_rij += 1          # breedte van de onderste rij
	var links := -14 if is_groot() else -12   # groot lijf en mantel: berg 2 pixels verder naar links (Mila 04:55)
	var k := 0
	var breedte := in_rij
	while k < n and breedte > 0:
		for j in breedte:
			if k >= n:
				break
			var h: int = hoeden[k]   # de oudste hoeden liggen op de berg
			var x := links - 6 * (in_rij - 1) + 6 * j + 3 * rij
			uit.append([h, x, -1 - int(HOED_ONDER[h]) - 3 * rij])
			k += 1
		rij += 1
		breedte -= 1
		if rij >= BERG_RIJEN:
			break
	return uit

# Hoeveel hoeden er op een berg met deze onderste rij passen: een piramide, hooguit BERG_RIJEN hoog
# (daarboven wordt hij een afgeknotte piramide, dus breder en niet hoger).
func _past_op_berg(onder: int) -> int:
	var n := 0
	for r in mini(onder, BERG_RIJEN):
		n += onder - r
	return n

# De hoedenberg met de 3D-hoeden (Bram 14 nov, winkelbeeld Olaf 05:35: pixelhoeden naast de 3D-Gloop): zelfde plekken
# en volgorde als berg(), elke hoed met zijn nulpunt (midden van de onderrand) waar de onderrand van de pixelhoed lag,
# dus op de vloer of op de rij eronder. [hoed, x, nulpunt-y]. Leeg als er geen 3D-hoedenblad is (dan pixels).
const BERG_3D_LUCHT := 1.0   # kan Daan 07:40: de 3D-hoeden zijn ronder en breder, 1 spelpixel extra lucht tot Gloops flank

func berg_3d() -> Array:
	var uit := []
	if not met_3d or beeld_3d() == "":
		return uit
	HB._laad_3d()
	if not HB.held3d.has(HB.HOEDEN3D):
		return uit
	for b in berg():
		var h: int = int(b[0])
		uit.append([h, float(b[1]) - BERG_3D_LUCHT, float(int(b[2]) + 1 + int(HOED_ONDER[h]))])
	return uit

func _draw() -> void:
	var berg3 := berg_3d()
	if berg3.is_empty():
		for b in berg():
			draw_texture_rect_region(HOEDEN, Rect2(int(b[1]) - 8, int(b[2]), 16, 16), Rect2(int(b[0]) * 16, 0, 16, 16))
	else:
		for b3 in berg3:
			_teken_hoed_3d(int(b3[0]), float(b3[1]), float(b3[2]), false)
	var f := frame_nu()
	var wip := wip_nu()
	var n := niveau()
	if n >= 3 and not is_plat():
		draw_texture_rect_region(UPG, Rect2(-14, -16 + wip, 28, 16), Rect2(20, 0, 28, 16))   # Royal: cape erachter, op de vloer (wipt mee bij het koop-moment)
	var b3 := beeld_3d()
	if b3 != "":
		_teken_3d(b3, wip)
	elif f[0] == RUST_GROOT or f[0] == LEVEN_GROOT:
		draw_texture_rect_region(f[0], Rect2(-10, -16 + wip, 20, 16), Rect2(int(f[1]) * 20, 0, 20, 16))
	else:
		draw_texture_rect_region(f[0], Rect2(-8, -16 + wip, 16, 16), Rect2(int(f[1]) * 16, 0, 16, 16))
	if n >= 3 and not is_plat():
		draw_texture_rect_region(UPG, Rect2(-10, -16 + top_nu() - 4 + wip, 20, 16), Rect2(48, 0, 20, 16))   # Royal: bovenzoom met gouden gesp voor hem, vóór de hoeden
	var t3 := toren_3d()
	if t3.is_empty():
		for h in toren():
			draw_texture_rect_region(HOEDEN, Rect2(int(h[1]) - 8, int(h[2]), 16, 16), Rect2(int(h[0]) * 16, 0, 16, 16))
	else:
		for i in t3.size():
			var h3: Array = t3[i]
			_teken_hoed_3d(int(h3[0]), float(h3[1]), float(h3[2]), i == t3.size() - 1 and not is_plat())   # bovenste hoed met hap
	if n >= 2 and not is_plat():
		# Bouncy: glansster tegen zijn kruin. Na de hoeden getekend, anders dekt de onderste hoed de bovenarm af en leest hij als een T.
		draw_texture_rect_region(UPG, Rect2(-10, -16 + top_nu() - 4 + wip, 20, 16), Rect2(0, 0, 20, 16))
	if leven == "slapen":
		var zy := -25
		var t3z := toren_3d()
		if t3z.is_empty():
			for h in toren():
				zy = mini(zy, int(h[2]) + int(HOED_TOP[int(h[0])]) - 9)   # zzz boven de hoedentoren
		else:
			for h3 in t3z:
				zy = mini(zy, int(floor(float(h3[3]))) - 9)
		zy = maxi(zy, int(ceil(teken_rand_y())))   # Daan 14 nov 01:40: teken minstens 1 spelpixel onder de bovenrand
		if not HELD_BEELD.teken_3d(self, "zzz", 0.0, float(zy + 8)):   # 3D-wolkje uit het blad tekens, anders pixels
			draw_texture_rect_region(TEKENS, Rect2(-4, zy, 8, 8), Rect2(3 * 8, 0, 8, 8))   # zzz
	if (leven == "spugen" and t >= leven_van + 0.6) or laars_ligt():
		var p := laars_pos()
		# 3D-laars uit het tekens-blad zodra daar een beeld "laars" in staat (Daan 06:40, volgorde 3; Olaf 14 nov),
		# zelfde voetpunt (onder-midden); anders de pixel-laars zoals altijd
		if not (met_3d and HB.teken_3d(self, "laars", float(p.x), float(p.y))):
			draw_texture_rect_region(LAARS, Rect2(p.x - 4, p.y - 8, 8, 8), Rect2(0, 0, 8, 8))
