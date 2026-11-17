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
# Staat kunst/3d/gloop.png er, dan tekent hij dat lijf voor rust, slapen, plat, opstaan, hap, blij en knipper,
# en sinds 15 nov ook voor spugen (met knipper en hap, zie _spuug_3d). Filter lineair alleen voor dit lijf (CanvasTexture), de
# pixelhoeden blijven scherp. Klein lijf = 0,8 x het grote (zelfde verhouding als 16 en 20 breed).
const LIJF3D_JSON := "res://kunst/3d/sprites.json"
static var lijf3d: CanvasTexture = null
static var lijf3d_info := {}
static var lijf3d_gezocht := false
# Royal in 3D (Bram 14 nov, vraag Daan 08:55): eigen blad "royal" in sprites.json met een eigen, bredere cel dan het lijf.
# Frame "achter" (mantel, scepter, goud) komt achter het lijf, frame "voor" (broche) ervoor, onder de hoeden.
# Zolang dat blad er niet is: de pixel-cape en -bovenzoom uit UPG zoals altijd.
static var royal3d: CanvasTexture = null
static var royal3d_info := {}
static var royal3d_gezocht := false
const HB := preload("res://systemen/held_beeld.gd")   # laadt ook het 3D-hoedenblad (kunst/3d/sprites.json)
var met_3d := true                 # uit = de oude pixel-Gloop (toetsen, of terug als het tegenvalt)
# Standen van Daan (13 nov 16:30, gloop.py 7e woord): knipperen elke 4 tot 7 s, blij als er een hoed op de toren
# komt, hap bij opeten. Alleen in 3D en alleen als die stand in het blad staat (anders gewoon rust).
const KNIPPER_MIN_S := 4.0
const KNIPPER_MAX_S := 7.0
const KNIPPER_S := 0.2
const BLIJ_S := 1.2
# Leven in het spel, punt 2 (hoofdchat 15 nov): de hoed van de held die hij at vliegt in een boog van de held naar de top
# van de toren en wiebelt daar even na. Alleen met de 3D-toren. Tijden vanaf de hap (hap_van).
const VLUCHT_VAN := 0.35      # na de beet
const VLUCHT_S := 0.5         # zo lang vliegt de hoed (Daan juice.md: boog 0,5 s, uitlopend)
const VLUCHT_BOOG := 8.0      # zoveel spelpixels hoger dan de rechte lijn, halverwege
const PLAT_S := 0.05          # bij de landing één beeld plat (90% hoog, Daan)
const WIEBEL_S := 0.4         # zo lang wiebelt hij na op de toren: 3 slagen die uitdempen (Daan)
const WIEBEL_GRAAD := 8.0     # eerste uitslag ±8 graden, in stapjes van 4 graden
var knipper_tot := -10.0
var blij_tot := -10.0
var rng_oog := RandomNumberGenerator.new()   # eigen dobbelsteen, zodat de leven-wekker gelijk blijft

# Leven in het spel 3 (hoofdchat 15 nov 15:55, getallen Daan in ontwerp/steam/juice.md): knijpen en rekken vanaf de voet.
# Hap: plat en breed (1,25 x 0,8) 80 ms, dan via 0,9 / 1,1 terug naar 1,0 binnen 0,33 s. Blij: eerst rekken omhoog
# (0,9 x 1,15), zelfde terugveer. Ademen: elke 3 tot 4 s 0,6 s lang één spelpixel hoger, met twee wekkers (op en neer),
# dus in rust geen _process. Alleen in 3D; de pixel-Gloop blijft zoals hij was. Hele spelpixels: de kruin gaat een heel
# aantal spelpixels omhoog of omlaag, gemeten op de echte zichtbare hoogte van het lijf (controleur 15 nov), en de
# hoedentoren schuift precies zoveel mee (knijp_dy).
const KNIJP_HAP := [[0.08, 1.25, 0.8], [0.2, 0.9, 1.1], [0.33, 1.05, 0.95]]   # [tot s, breed, hoog]
const KNIJP_BLIJ := [[0.08, 0.9, 1.15], [0.2, 1.1, 0.9], [0.33, 0.97, 1.03]]
const ADEM_MIN_S := 3.0
const ADEM_MAX_S := 4.0
const ADEM_S := 0.6
var adem_aan := false
var rng_adem := RandomNumberGenerator.new()   # eigen dobbelsteen: de andere wekkers blijven gelijk
var _knijp := Vector2.ONE                     # de schaal waarmee nu getekend wordt (spiegel in _teken_3d zet hem terug)

var hol
var soort := "slijm"
var bijnaam_naam := "Gloop"
var plat_s := 30.0          # in het spel 30 s (Sanne 16 nov 20:00, was 60); strook.gd mag dit in de demo versnellen (Sanne toets 2, punt 1: ±9 s)
var gegeten := 0            # helden die hij kreeg ("Gloop has eaten 12 heroes")
var hoeden: Array[int] = [] # elke hoed die hij kreeg, oudste eerst. Een hoed gaat er nooit meer af (Sanne).
var keer_plat := 0
var t := 0.0
var hoed_vlucht_van := -99.0  # tijd van de hap met een nieuwe hoed (leven in het spel, punt 2)
var hoed_van := Vector2(-12, -10)   # waar de hoed vandaan vliegt (hoofd van de held), Gloop-coordinaten
var hap_van := -10.0
# Hoeden van de nacht (Sanne 17 nov 06:05, features.md; bouw Bram): de hoeden van terwijl je weg was staan niet meteen op
# de toren maar wachten hier en vallen na het openen een voor een van boven op de top, met de landing die er al is.
const NACHT_WACHT_S := 1.0    # na het openen: eerst de wip van het bordje (0,1 + 0,5 s), dan pas vallen
const NACHT_TUSSEN_S := 0.3   # de eerste NACHT_EEN_VOOR_EEN hoeden elk 0,3 s na elkaar
const NACHT_EEN_VOOR_EEN := 10   # de rest in één plof, na de tiende; samen nooit meer dan ±4 s
const VAL_S := 0.25           # zo lang valt een nachthoed recht omlaag (geland vóór de volgende komt)
const VAL_HOOG := 14.0        # zoveel spelpixels boven de bovenrand van het hol begint de val (buiten beeld)
var nacht_hoeden: Array[int] = []   # wachten nog, oudste eerst; tellen in de save gewoon mee (naar_dict)
var nacht_van := -1.0         # t van de eerste val; -1 = nog niet gestart
var nacht_gelegd := 0         # zoveel van deze nacht staan er al op
var hoed_valt := false        # de bovenste hoed valt recht omlaag (nacht) in plaats van de boog van de held
var blij_van := -10.0         # landing van de laatste nachthoed: dan pas blij (alleen als blij_nacht)
var blij_nacht := false       # blij komt van een nachthoed (anders, zoals altijd, na de hap)
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
	rng_adem.seed = hash([kol, "adem"])
	_plan_adem()
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

func _plan_adem() -> void:
	if is_inside_tree():
		get_tree().create_timer(rng_adem.randf_range(ADEM_MIN_S, ADEM_MAX_S)).timeout.connect(_adem)

func _adem() -> void:
	adem()
	_plan_adem()

# Eén keer ademen: alleen in rust (geen hap, blij, leven, plat of koop-moment), anders slaat hij deze beurt over.
func adem() -> bool:
	if not _heeft_3d("rust") or is_plat() or leven != "" or t < hap_van + HAP_S or t < blij_tot or t < koop_van + KOOP_S or t < plat_tot + OPSTAAN_S:
		return false
	adem_aan = true
	_teken_als_anders()
	if is_inside_tree():
		get_tree().create_timer(ADEM_S).timeout.connect(adem_uit)
	return true

func adem_uit() -> void:
	adem_aan = false
	_teken_als_anders()

# Zichtbare maat van het 3D-lijf nu in spelpixels (breed = cel, hoog = cel min de lege rand boven de kruin in rust).
func lijf_maat() -> Vector2:
	if lijf3d_info.is_empty():
		return Vector2(20, 16)
	var px: float = lijf3d_info["px"]
	var k := 1.0 if is_groot() else 0.8
	var top3: float = lijf3d_info["top"][lijf3d_info["frames"].find("rust")] if lijf3d_info.has("top") else 0.0
	return Vector2(float(lijf3d_info["cel_px"][0]) / px * k, (float(lijf3d_info["cel_px"][1]) - top3) / px * k)

# De schaal van het lijf nu (breed, hoog), vanaf de voet. Vector2.ONE als er niets knijpt.
func knijp_nu() -> Vector2:
	if beeld_3d() == "" or is_plat() or _rust_som:
		return Vector2.ONE
	var k := _knijp_uit(KNIJP_HAP, t - hap_van)
	if k == Vector2.ONE and blij_tot > 0.0:
		k = _knijp_uit(KNIJP_BLIJ, t - _blij_start()) if t < blij_tot and t >= _blij_start() else Vector2.ONE
	if k == Vector2.ONE and adem_aan and not (t < hap_van + HAP_S or t < blij_tot or leven != ""):
		var m := lijf_maat()
		k = Vector2(1.0, (m.y + 1.0) / m.y)
	return k

func _knijp_uit(tabel: Array, dt: float) -> Vector2:
	if dt < 0.0:
		return Vector2.ONE
	var m := lijf_maat()
	for r in tabel:
		if dt < float(r[0]):
			return Vector2(round(m.x * float(r[1])) / m.x, (m.y + round(m.y * (float(r[2]) - 1.0))) / m.y)
	return Vector2.ONE

# Hoeveel spelpixels de kruin nu hoger (negatief) of lager staat door het knijpen; de toren gaat mee.
func knijp_dy() -> int:
	return -int(round(lijf_maat().y * (knijp_nu().y - 1.0)))

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

# Keurstrook spugen (Bram 15 nov, spuug_proef=<1-3> in strook.gd, wens Daan "zo wil ik hem in de echte strook zien"):
# hij blijft in één spuugmoment staan, 1 = kneep (0,1 s), 2 = spuug met de laars achter het lijf (0,65 s),
# 3 = spuug met de laars midden in de boog. De tijd loopt gewoon door (een hap of plat gaat voor), alleen
# leven_van schuift mee zodat het moment blijft. Nooit in het echte spel.
# Winkelbeeld "de hap" (Bram 15 nov, moment=hap in strook.gd, winkelschermen wo 18 nov): bij de eerste hap met een
# nieuwe hoed blijft Gloop staan op het mooiste moment: de hoed bijna bovenaan zijn boog boven hem, Gloop nog in de hap.
# Zijn eigen tijd staat dan stil (de helden en het hol lopen door); tekenen kost niets meer. Nooit in het echte spel.
const MOMENT_HAP_S := VLUCHT_VAN + VLUCHT_S * 0.45
var moment_hap := false
var moment_vast := -1.0

const SPUUG_PROEF_S := [0.1, 0.65, 0.6 + BOOG_S * 0.5]
var spuug_vast := -1.0

func zet_spuug_proef(n: int) -> void:
	spuug_vast = SPUUG_PROEF_S[clampi(n, 1, 3) - 1]
	laars_kant = 1
	laars_op_vloer = false
	leven = "spugen"
	leven_van = t - spuug_vast
	set_process(true)
	queue_redraw()

# Waar de laars is (onder-midden, ten opzichte van Gloop), in hele pixels: boogje van 12 px opzij in 0,3 s, landt op 15.
func laars_pos() -> Vector2i:
	if leven != "spugen":
		return Vector2i(15 * laars_kant, 0)   # geland: blijft liggen, ook als hij daarna slaapt (15: een spelpixel lucht naar de goudberg, Daan 14 nov)
	var u := clampf((t - (leven_van + 0.6)) / BOOG_S, 0.0, 1.0)   # vliegt na spugen-frame 3 (index 3 = 0,6 s)
	var y := -int(round(8.0 * u * (1.0 - u) * 4.0 / 2.0))
	if beeld_3d() != "":   # 3D (Daan 15 nov): begint achter het lijf op x 7, landt ook op 15
		return Vector2i((LAARS_START_3D + int(round(float(15 - LAARS_START_3D) * u))) * laars_kant, y)
	var x := int(round(12.0 * u)) * laars_kant
	return Vector2i(x + 3 * laars_kant, y)

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
	var y := -16 + top_nu() + wip_nu() + knijp_dy()
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
func raak(hoed := -1, van := Vector2(-12, -10)) -> int:
	if moment_vast >= 0.0:
		return hoeden.size()   # winkelbeeld moment=hap staat stil: een volgende hap verandert het beeld niet
	gegeten += 1
	hap_van = t
	if hoed >= 0:
		hoeden.append(hoed % HOED_SOORTEN)
		hoed_vlucht_van = t
		hoed_van = van
		hoed_valt = false
		if moment_hap and moment_vast < 0.0:
			moment_vast = t + MOMENT_HAP_S
		blij_tot = t + HAP_S + BLIJ_S     # na de hap even blij om de nieuwe hoed
		blij_nacht = false
	set_process(true)
	return hoeden.size()

# Een hoed erbij zonder hap-animatie (voortgang terwijl je weg was, Voortgang.geef_hoeden).
func krijg_hoed(hoed: int) -> int:
	gegeten += 1
	hoeden.append(absi(hoed) % HOED_SOORTEN)
	queue_redraw()
	return hoeden.size()

# Hoeden van de nacht: in de rij zetten (Voortgang.geef_hoeden met later=true); vallen pas na start_nacht().
func krijg_hoed_later(hoed: int) -> int:
	gegeten += 1
	nacht_hoeden.append(absi(hoed) % HOED_SOORTEN)
	return hoeden.size() + nacht_hoeden.size()

func start_nacht(wacht_s := NACHT_WACHT_S) -> void:
	if nacht_hoeden.is_empty():
		return
	nacht_van = t + wacht_s
	nacht_gelegd = 0
	set_process(true)

# Hoeveel nachthoeden er op tijd dt na de eerste val moeten liggen (los, zodat de toets het tempo kan nakijken).
static func nacht_aantal(dt: float, totaal: int) -> int:
	if dt < 0.0 or totaal <= 0:
		return 0
	var n := int(floor(dt / NACHT_TUSSEN_S + 0.0001)) + 1
	if n > NACHT_EEN_VOOR_EEN:
		return totaal   # na de tiende: de rest in één plof
	return mini(n, totaal)

func _nacht_stap() -> void:
	if nacht_hoeden.is_empty() or nacht_van < 0.0 or t < nacht_van:
		return
	var moet := nacht_aantal(t - nacht_van, nacht_gelegd + nacht_hoeden.size())
	if moet <= nacht_gelegd:
		return
	while nacht_gelegd < moet and not nacht_hoeden.is_empty():
		hoeden.append(nacht_hoeden.pop_front())
		nacht_gelegd += 1
	# alleen de bovenste valt in beeld (bij de plof gaan de andere er in één keer onder)
	hoed_vlucht_van = t - VLUCHT_VAN
	hoed_valt = true
	blij_van = t + VAL_S
	blij_tot = blij_van + BLIJ_S
	blij_nacht = true
	if nacht_hoeden.is_empty():
		nacht_van = -1.0
	queue_redraw()

# Na de laatste val (of meteen als er niets wachtte): leeg, en of er nog iets in de rij staat.
func nacht_bezig() -> bool:
	return not nacht_hoeden.is_empty()

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
	return {"hoeden": hoeden + nacht_hoeden, "gegeten": gegeten, "gespuugd": gespuugd, "keer_plat": keer_plat}

func van_dict(d: Dictionary) -> void:
	hoeden.clear()
	nacht_hoeden.clear()
	nacht_van = -1.0
	for h in d.get("hoeden", []):
		hoeden.append(absi(int(h)) % HOED_SOORTEN)
	gegeten = maxi(int(d.get("gegeten", 0)), hoeden.size())
	gespuugd = int(d.get("gespuugd", 0))
	keer_plat = int(d.get("keer_plat", 0))
	queue_redraw()

func plat() -> void:
	if moment_vast >= 0.0:
		return   # winkelbeeld moment=hap staat stil: niet meer plat (keurstap 885b227: dan viel de kroon op de vloer)
	keer_plat += 1
	var duur := plat_s
	if hol != null and "upgrades" in hol and hol.get("upgrades") != null:
		duur = plat_s * hol.get("upgrades").plat_factor()   # Bouncy Gloop (systemen/upgrades.gd): 20 s in plaats van 30
	plat_tot = t + duur
	set_process(true)

func regel_plat() -> String:
	return "%s is flat. Back in a minute." % bijnaam_naam

func _process(delta: float) -> void:
	stap(delta)

func stap(delta: float) -> void:
	t += delta
	if moment_vast >= 0.0 and t > moment_vast:
		t = moment_vast   # winkelbeeld moment=hap: Gloop en de vliegende hoed blijven staan
	_nacht_stap()
	if spuug_vast >= 0.0:
		leven = "spugen"
		leven_van = t - spuug_vast   # keurstrook: het moment blijft staan
	if leven == "slapen" and (t > leven_van + SLAAP_S or _held_in_de_buurt() or is_plat()):
		leven = ""             # een held komt binnen: wakker
	elif leven == "spugen" and t > leven_van + 0.6 + BOOG_S:
		leven = ""
		laars_op_vloer = true
		if is_inside_tree():
			get_tree().create_timer(LAARS_LIGT_S).timeout.connect(laars_weg)   # laars weg, zonder _process
	if leven == "" and t > hap_van + HAP_S and t > plat_tot + OPSTAAN_S and t > koop_van + KOOP_S and t > blij_tot and t > knipper_tot and nacht_hoeden.is_empty() and not hoed_vliegt():
		set_process(false)
	_teken_als_anders()

# Demolijst 2 (Olaf 13 nov, CPU): plat ligt hij 60 s stil in hetzelfde beeld, maar elk beeld werd opnieuw getekend
# (duurtest: 15 beelden per seconde zonder held). Nu alleen tekenen als wat je ziet verandert. Andere functies die
# de berg of de toren veranderen roepen zelf queue_redraw aan.
func _teken_als_anders() -> void:
	var nu := [frame_nu(), beeld_3d(), wip_nu(), knijp_nu(), leven, laars_ligt(), laars_pos() if leven == "spugen" else Vector2i.ZERO, hoeden.size(), niveau(), is_plat(), t if hoed_vliegt() else 0.0]
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

# Welk 3D-beeld nu (rust, plat, hap, blij, knipper), of "" als het pixelbeeld moet (geen 3D).
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
	if f[0] == LEVEN and leven == "spugen" and SPUGEN.has(f[1]):
		return _spuug_3d(SPUGEN.find(f[1]))
	if f[0] == RUST or (f[0] == LEVEN and (f[1] == OPSTAAN or SLAPEN.has(f[1]))):
		if f[0] == RUST and t < blij_tot and (not blij_nacht or t >= blij_van) and _heeft_3d("blij"):
			return "blij"
		if (f[0] == RUST and t < knipper_tot or f[0] == LEVEN and SLAPEN.has(f[1])) and _heeft_3d("knipper"):
			return "knipper"     # slapen = ogen dicht
		return "rust"
	return ""

# Spugen in 3D (Bram 15 nov, laatste pixelmoment van Gloop): geen eigen stand nodig, de vier spuug-beelden
# (0,2 s elk) worden kneep, kneep (oog dichtgeknepen, wangen bol, lijf plat en breed: persen), spuug, spuug
# (getuite mond, lijf iets omhoog gerekt) op het moment dat de laars eruit vliegt (vanaf 0,6 s). Standen en schaal
# van Daan (15 nov 11:35, gloop.py en pijplijn/sprites.json). Ontbreekt een stand, dan rust.
# In 3D vliegt de laars achter het lijf en begint op x 6 (aan zijn rechterkant, nooit over zijn oog); landt op 15.
# Spuugt hij naar links (laars_kant -1), dan wordt het spuug-beeld gespiegeld zodat hij de laars nakijkt.
const SPUUG_3D := ["kneep", "kneep", "spuug", "spuug"]
const LAARS_START_3D := 6   # kan Daan 15 nov 12:45: x 6 leest meer als "komt uit hem" (was 7)
func _spuug_3d(i: int) -> String:
	var naam: String = SPUUG_3D[clampi(i, 0, SPUUG_3D.size() - 1)]
	return naam if _heeft_3d(naam) else "rust"

static func _laad_royal() -> void:
	if royal3d_gezocht:
		return
	royal3d_gezocht = true
	if not FileAccess.file_exists(LIJF3D_JSON):
		return
	var d = JSON.parse_string(FileAccess.get_file_as_string(LIJF3D_JSON))
	if typeof(d) != TYPE_DICTIONARY or not d.has("royal") or not ResourceLoader.exists(str(d["royal"]["blad"])):
		return
	royal3d_info = d["royal"]
	royal3d = CanvasTexture.new()
	royal3d.diffuse_texture = load(str(royal3d_info["blad"]))
	royal3d.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS

# Bouncy-glansster: vanaf niveau 2, niet plat. Bij Royal in 3D niet meer: de saffier van de scepter glanst al,
# en hoger vecht hij met de rugleuning (Daan 14 nov 10:45, moet 2). Royal zonder 3D-blad houdt de pixelster.
func ster_aan(b3: String) -> bool:
	var n := niveau()
	if n < 2 or is_plat():
		return false
	return not (n >= 3 and royal_3d_aan(b3))

# Royal in 3D aan: alleen met het 3D-lijf in beeld en het blad "royal" geladen. Dan geen pixel-cape of -zoom meer.
func royal_3d_aan(b3: String) -> bool:
	_laad_royal()
	return b3 != "" and royal3d != null and not royal3d_info.is_empty()

# Waar een Royal-frame komt (spelpixels, Gloop-coordinaten): onderkant op de vloer, anker_x onder zijn midden,
# klein lijf 0,8 zoals _teken_3d. Leeg als het frame niet in het blad staat.
func royal_rect(naam: String, wip: int) -> Rect2:
	if royal3d_info.is_empty() or not (royal3d_info["frames"] as Array).has(naam):
		return Rect2()
	var px: float = royal3d_info["px"]
	var k := 1.0 if is_groot() else 0.8
	var w: float = float(royal3d_info["cel_px"][0]) / px * k
	var h: float = float(royal3d_info["cel_px"][1]) / px * k
	return Rect2(-float(royal3d_info["anker_x"]) / px * k, -h + wip, w, h)

func _teken_royal(naam: String, wip: int) -> void:
	var r := royal_rect(naam, wip)
	if r.size.x <= 0.0 or royal3d == null:
		return
	var i: int = (royal3d_info["frames"] as Array).find(naam)
	var cw: float = royal3d_info["cel_px"][0]
	var ch: float = royal3d_info["cel_px"][1]
	draw_texture_rect_region(royal3d, r, Rect2(i * cw, 0, cw, ch))

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
	var spiegel := naam == "spuug" and laars_kant < 0
	if spiegel:
		draw_set_transform(Vector2.ZERO, 0.0, Vector2(-_knijp.x, _knijp.y))
	draw_texture_rect_region(lijf3d, Rect2(x, -h + wip, w, h), Rect2(i * cw, 0, cw, ch))
	if spiegel:
		draw_set_transform(Vector2.ZERO, 0.0, _knijp)

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
		var boven := -16 + top_nu() + wip_nu() + knijp_dy()
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
		var boven := float(-16 + top_nu() + wip_nu() + knijp_dy())
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
	return (PLAFOND - position.y) / scale.y   # scale: keurstand figuur=<factor> (Olaf 15 nov), anders 1; bovenrand van het hol (hol-y 0) in Gloop-coordinaten, plus 2
# Hoogste y voor de bovenkant van een teken (zzz): 1 spelpixel onder de bovenrand van het hol (Daan 14 nov 01:40).
const TEKEN_RAND := 1.0
func teken_rand_y() -> float:
	return (TEKEN_RAND - position.y) / scale.y   # scale: keurstand figuur=<factor>, anders 1
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

# Vlucht van de nieuwe bovenste hoed (leven in het spel, punt 2): [zichtbaar, x, nul, hoek] voor een hoed die op de toren
# op (doel_x, doel_nul) hoort. Voor de vlucht nog niet te zien (de held heeft hem nog op), dan een boog met een halve
# draai naar de toren, dan wiebelen om zijn nulpunt met een uitslag die uitdooft. Daarna gewoon op zijn plek.
func hoed_vlucht(doel_x: float, doel_nul: float) -> Array:
	var s := t - hoed_vlucht_van - VLUCHT_VAN
	var vs := _vlucht_s()
	# [zichtbaar, x, nul, hoek, hoogte]; x en nul op hele spelpixels (Daan: geen halve pixels), hoek in stapjes
	if s < -VLUCHT_VAN or s >= vs + WIEBEL_S or is_plat():
		return [true, doel_x, doel_nul, 0.0, 1.0]
	if s < 0.0:
		return [false, doel_x, doel_nul, 0.0, 1.0]
	if hoed_valt and s < vs:
		# nachthoed: recht omlaag van boven het hol op de top, steeds sneller (vallen), zonder draai
		var fv := s / vs
		var van_y := plafond_y() - VAL_HOOG
		return [true, doel_x, round(lerpf(van_y, doel_nul, fv * fv)), 0.0, 1.0]
	if not hoed_valt and s < VLUCHT_S:
		var f := s / VLUCHT_S
		var g := f * (2.0 - f)   # snel weg, zacht neer
		var hoek := snappedf(-PI * (1.0 - g), PI / 8.0)
		return [true, round(lerpf(hoed_van.x, doel_x, g)), round(lerpf(hoed_van.y, doel_nul, g) - sin(f * PI) * VLUCHT_BOOG), hoek, 1.0]
	var w := s - vs
	if w < PLAT_S:
		return [true, doel_x, doel_nul, 0.0, 0.9]
	var p := (w - PLAT_S) / (WIEBEL_S - PLAT_S)
	var graad := snappedf(WIEBEL_GRAAD * (1.0 - p) * sin(p * 3.0 * PI), 4.0)
	return [true, doel_x, doel_nul, deg_to_rad(graad), 1.0]

func hoed_vliegt() -> bool:
	var s := t - hoed_vlucht_van
	return s >= 0.0 and s < VLUCHT_VAN + _vlucht_s() + WIEBEL_S

func _blij_start() -> float:
	return blij_van if blij_nacht else hap_van + HAP_S

func _vlucht_s() -> float:
	return VAL_S if hoed_valt else VLUCHT_S

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
	var b3 := beeld_3d()
	var royal3 := n >= 3 and not is_plat() and royal_3d_aan(b3)
	_knijp = knijp_nu() if b3 != "" else Vector2.ONE
	if _knijp != Vector2.ONE:
		draw_set_transform(Vector2.ZERO, 0.0, _knijp)   # vanaf de voet (y 0 = vloer): de onderkant blijft op de grond
	if royal3:
		_teken_royal("achter", wip)   # Royal in 3D: mantel en scepter achter hem
	elif n >= 3 and not is_plat():
		draw_texture_rect_region(UPG, Rect2(-14, -16 + wip, 28, 16), Rect2(20, 0, 28, 16))   # Royal: cape erachter, op de vloer (wipt mee bij het koop-moment)
	var laars_achter := leven == "spugen" and b3 != ""
	if laars_achter and t >= leven_van + 0.6:
		_teken_laars()   # 3D: de laars vliegt achter het lijf vandaan (Daan 15 nov, moet 2)
	if b3 != "":
		_teken_3d(b3, wip)
	elif f[0] == RUST_GROOT or f[0] == LEVEN_GROOT:
		draw_texture_rect_region(f[0], Rect2(-10, -16 + wip, 20, 16), Rect2(int(f[1]) * 20, 0, 20, 16))
	else:
		draw_texture_rect_region(f[0], Rect2(-8, -16 + wip, 16, 16), Rect2(int(f[1]) * 16, 0, 16, 16))
	if royal3:
		_teken_royal("voor", wip)     # Royal in 3D: broche voor hem, onder de hoeden
	elif n >= 3 and not is_plat():
		draw_texture_rect_region(UPG, Rect2(-10, -16 + top_nu() - 4 + wip, 20, 16), Rect2(48, 0, 20, 16))   # Royal: bovenzoom met gouden gesp voor hem, vóór de hoeden
	if _knijp != Vector2.ONE:
		draw_set_transform(Vector2.ZERO, 0.0, Vector2.ONE)   # hoeden niet knijpen: de toren schuift mee via knijp_dy()
		_knijp = Vector2.ONE
	var t3 := toren_3d()
	if t3.is_empty():
		for h in toren():
			draw_texture_rect_region(HOEDEN, Rect2(int(h[1]) - 8, int(h[2]), 16, 16), Rect2(int(h[0]) * 16, 0, 16, 16))
	else:
		for i in t3.size():
			var h3: Array = t3[i]
			var boven := i == t3.size() - 1
			if boven and hoed_vliegt():
				var v := hoed_vlucht(float(h3[1]), float(h3[2]))   # de nieuwe hoed vliegt erop (leven in het spel, punt 2)
				if v[0]:
					draw_set_transform(Vector2(float(v[1]), float(v[2])), float(v[3]), Vector2(1.0, float(v[4])))
					_teken_hoed_3d(int(h3[0]), 0.0, 0.0, not is_plat())
					draw_set_transform(Vector2.ZERO, 0.0, Vector2.ONE)
				continue
			_teken_hoed_3d(int(h3[0]), float(h3[1]), float(h3[2]), boven and not is_plat())   # bovenste hoed met hap
	if ster_aan(b3):
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
	if not laars_achter and ((leven == "spugen" and t >= leven_van + 0.6) or laars_ligt()):
		_teken_laars()

func _teken_laars() -> void:
	var p := laars_pos()
	# 3D-laars uit het tekens-blad zodra daar een beeld "laars" in staat (Daan 06:40, volgorde 3; Olaf 14 nov),
	# zelfde voetpunt (onder-midden); anders de pixel-laars zoals altijd
	if not (met_3d and HB.teken_3d(self, "laars", float(p.x), float(p.y))):
		draw_texture_rect_region(LAARS, Rect2(p.x - 4, p.y - 8, 8, 8), Rect2(0, 0, 8, 8))
