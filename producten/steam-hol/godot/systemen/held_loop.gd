extends RefCounted
# Lopen van de held (Olaf 25 nov 2026, issue #25; bouwblad A en B van Sanne in platformen/steam/spelgevoel.md).
# Los van held.gd zodat dat bestand onder de ±400 regels blijft. Alleen statische functies met de held als eerste argument.
#
# Beeld en beweging zijn één ding (naar Shimeji-ee, New BSD: eerst verschuiven, dan het beeld zetten, anker onder de voeten):
# op een klok van loop_fps beelden per seconde schuift de held bij elke beeldwissel precies stap_px spelpixels op, en het
# loopbeeld volgt uit de afgelegde weg (stap1..stap6). Zo staat de steunvoet stil op de grond en glijdt niets (moet Daan #35).
# stap_px en loop_fps per blad komen uit kunst/3d/sprites.json (Mila #32); loop_fps is voor iedereen 12 (Sanne), dus
# gewone held 5,6, ridder en magier 3,9, bard 4,9, dief 7,5 spelpixels per seconde. Vluchten: zelfde beelden, 1,5 keer zo snel.
# Pixelheld (geen 3D-blad): 4 beelden, 1 hele pixel per beeld op 10 per s, zoals vroeger.
#
# Erbij (goob: draaipauze en hele clips; Sanne A): elke 3 tot 6 s lopen staat hij 1 s stil met het kijk-beeld, bij omdraaien
# eerst 0,25 s het draai-beeld. En (Sanne B) een val doet altijd iets: valt hij niet, dan springt hij er in 0,6 s overheen met
# het sprong-beeld en een teken waaraan je ziet waarom (dief strepen: te snel; magier een oog: ziet de val; rest "!": geluk).

const HELD_BEELD := preload("res://systemen/held_beeld.gd")

const LOOP_FPS := 12.0            # Sanne bouwblad A: voor alle soorten (sprites.json heeft Mila's voorstel, dat gebruiken we niet)
const VLUCHT_X := 1.5             # vluchten: zelfde beelden sneller (Sanne: tot 18 per s)
const PIXEL_STAP := 1.0           # pixelheld: hele pixels (Daan 13 nov)
const PIXEL_FPS := 10.0
const KIJK_ELKE := Vector2(3.0, 6.0)
const KIJK_S := 1.0
const DRAAI_S := 0.25
const SPRONG_S := 0.6
const SPRONG_HOOG := 5.0          # spelpixels boven de vloer op het hoogste punt
const SPRONG_VER := 12.0          # zo ver voorbij het midden van de val landt hij (een kolom is 16 breed)

# Eén keer bij start(): stap en klok uit het blad van deze held. Bij een 3D-blad zonder stap_px (oud blad): pixelwaarden.
static func kies(h) -> void:
	h.loop_stap = PIXEL_STAP
	h.loop_fps = PIXEL_FPS
	h.loop_n = 4
	if not HELD_BEELD.met_3d:
		return
	var naam: String = HELD_BEELD.blad_voor(String(h.soort_held), int(h.kleur_nr))
	if naam == "" or not HELD_BEELD.held3d.has(naam):
		return
	var info: Dictionary = HELD_BEELD.held3d[naam][1]
	if not info.has("stap_px") or not (info.get("frames", []) as Array).has("stap6"):
		return
	h.loop_stap = float(info["stap_px"])
	h.loop_fps = LOOP_FPS
	h.loop_n = 6

# Hoeveel beeldwissels in deze aanroep (echte tijd); de rest van de klok blijft staan voor de volgende.
static func wissels(h, echt: float, vluchten: bool) -> int:
	var fps: float = float(h.loop_fps) * clampf(float(h.info.get("snelheid", 1.0)), 0.25, 4.0) * (VLUCHT_X if vluchten else 1.0)
	h.loop_klok += echt * fps
	var n := int(h.loop_klok + 0.0001)
	h.loop_klok = maxf(0.0, h.loop_klok - n)
	return n

# Welk loopbeeld (0 tot loop_n - 1) bij de afgelegde weg.
static func beeld(h) -> int:
	return posmod(int(floor(float(h.afgelegd) / float(h.loop_stap) + 0.001)), int(h.loop_n))

# Loop n beeldwissels naar doel_x: precies n x stap_px, in stukjes van hooguit 8 pixels met na elk stukje h._onderweg()
# (anders sprong hij na een hapering over een hele kolom en dus over een val heen, Bram 16 nov).
static func loop(h, n: int, doel_x: float, kijk_onderweg: bool) -> void:
	var rest: float = n * float(h.loop_stap)
	while rest > 0.0:
		var stuk := minf(rest, 8.0)
		var voor: float = h.position.x
		h.position.x = move_toward(h.position.x, doel_x, stuk)
		h.afgelegd += absf(h.position.x - voor)
		rest -= stuk
		if kijk_onderweg:
			h._onderweg()
			if h.staat != "lopen" or h.spring_t >= 0.0:
				break
		elif terug_over_val(h):
			break
		if absf(h.position.x - doel_x) < 0.5:
			break

# Staat hij nu stil om rond te kijken? Telt alleen in lopen (niet bij vluchten). Eigen dobbelsteen, zodat de uitkomsten
# van de vallen (h.rng) precies blijven wat ze waren.
const EPS := 0.000001             # t komt uit een som van beeldtijden; na bewaren in JSON kan hij 1e-15 anders zijn
static func kijkt(h) -> bool:
	if h.t < h.kijk_tot - EPS:
		return true
	if h.volgende_kijk <= 0.0:
		h.volgende_kijk = h.t + h.rng_loop.randf_range(KIJK_ELKE.x, KIJK_ELKE.y)
	if h.t >= h.volgende_kijk - EPS:
		h.kijk_tot = h.t + KIJK_S
		h.volgende_kijk = h.kijk_tot + h.rng_loop.randf_range(KIJK_ELKE.x, KIJK_ELKE.y)
		return true
	return false

# Begin van vluchten: eerst het draai-beeld, dan rennen.
static func draai(h) -> void:
	h.staat = "vluchten"
	h.draai_tot = h.t + DRAAI_S
	h.kijk_tot = 0.0

# Valt niet bij een val: sprong over het midden van de put heen, met het teken van zijn soort.
static func spring(h, val_midden_x: float) -> void:
	h.spring_t = 0.0
	h.spring_van = h.position.x
	h.spring_naar = val_midden_x + SPRONG_VER   # in lopen gaat hij altijd naar rechts (ingang links, schat rechts)
	h.spring_teken = teken_voor(String(h.soort_held))
	h.kijk_tot = 0.0

# Vluchten (naar links) over een val die hij al zag: niet gewoon eroverheen lopen (Iris, #25), maar terugspringen met het
# zweetdruppeltje. Geen nieuwe worp: de uitkomst van die val is al beslist. true = hij springt nu.
static func terug_over_val(h) -> bool:
	if h.staat != "vluchten":
		return false
	var cel: Vector2i = h.hol.pos_naar_cel(h.position)
	if h.hol.val_op(cel) == "" or h.terug_gesprongen.has(cel.x):
		return false
	h.terug_gesprongen[cel.x] = true
	var midden: float = round(h.hol.cel_naar_pos(cel).x)
	h.spring_t = 0.0
	h.spring_van = h.position.x
	h.spring_naar = midden - SPRONG_VER
	h.spring_teken = "zweet"
	return true

static func teken_voor(soort: String) -> String:
	if soort == "dief":
		return "streep"
	if soort == "magier":
		return "oog"
	return "uitroep"

# Een tik van de sprong; true zolang hij nog in de lucht is.
static func sprong_tik(h, echt: float) -> bool:
	h.spring_t += echt
	var u := clampf(float(h.spring_t) / SPRONG_S, 0.0, 1.0)
	h.position.x = lerpf(float(h.spring_van), float(h.spring_naar), u)
	if u < 1.0:
		return true
	h.spring_t = -1.0
	h.afgelegd = 0.0
	if String(h.na_sprong) == "vluchten":
		draai(h)
	h.na_sprong = ""
	if h.staat == "lopen":
		h._onderweg()   # de kolom waar hij landt (een bewoner vlak achter de val) telt gewoon
	return false

# Hoe hoog hij nu in de sprong is (negatief = omhoog, spelpixels); 0 buiten de sprong.
static func sprong_hop(h) -> float:
	if float(h.spring_t) < 0.0:
		return 0.0
	var u := clampf(float(h.spring_t) / SPRONG_S, 0.0, 1.0)
	return -SPRONG_HOOG * sin(PI * u)

# Welk beeld uit het blad in plaats van het loopbeeld ("" = gewoon lopen of de staat zelf).
static func pose(h) -> String:
	if float(h.spring_t) >= 0.0:
		return "sprong"
	if h.staat == "vluchten" and h.t < h.draai_tot - EPS:
		return "draai"
	if h.staat == "lopen" and h.t < h.kijk_tot - EPS:
		return "kijk"
	return ""

# Eigen tekens bij de sprong (Sanne B), getekend in de held (alleen tijdens zijn _draw). onder = rij net boven de hoed.
# streep: dief, twee witte strepen achter hem (te snel); oog: magier, een oog boven zijn hoofd (ziet de val).
# false = geen eigen teken, dan tekent held_beeld.gd het gewone teken.
static func teken_eigen(h, tk: String, onder: int) -> bool:
	if tk == "streep":
		var wit := Color(1, 1, 1, 0.9)
		h.draw_rect(Rect2(-12, -9, 6, 1), wit)
		h.draw_rect(Rect2(-14, -6, 7, 1), wit)
		h.draw_rect(Rect2(-11, -3, 5, 1), wit)
		return true
	if tk == "oog":
		var y := float(onder) - 3.0
		h.draw_rect(Rect2(-4, y - 2, 8, 5), Color(0.12, 0.08, 0.16))   # donkere rand
		h.draw_rect(Rect2(-3, y - 1, 6, 3), Color(1, 1, 1))
		h.draw_rect(Rect2(-1, y - 1, 2, 3), Color(0.35, 0.2, 0.75))    # paarse pupil, de kleur van de magier
		h.draw_rect(Rect2(-5, y, 1, 1), Color(0.12, 0.08, 0.16))
		h.draw_rect(Rect2(4, y, 1, 1), Color(0.12, 0.08, 0.16))
		return true
	return false
