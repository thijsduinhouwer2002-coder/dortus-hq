extends Node2D
# Het hol (Olaf). Een raster van kolommen van 16 spelpixels breed, met Daans kunst (producten/steam-hol/godot/kunst/).
# Opbouw op 40 spelpixels (strook 120 px, schaal 3): maaiveld 8, dan twee rijen cellen van 16.
# - de onderste rij is de gang waar helden lopen (in de afspraak met Bram is dat cel.y == 0);
# - de bovenste rij is aarde, behalve de schacht bij de ingang, de schatkamer achteraan (twee rijen hoog)
#   en kamers die je zelf graaft.
# Het hol groeit in de breedte, naar links: de schat staat rechts tegen het tekstvak (Sanne toets 2, punt 0 en 6),
# zodat het tekstvak nooit over de schat ligt en het rechterdeel van de strook nooit leeg is. Graven links van de
# ingang schuift de ingang mee naar links. Afspraak met Bram (platformen/steam/taken.md): alleen deze functies en signalen gebruiken.

signal gegraven(cel: Vector2i)

const KOL := 16          # breedte van een kolom in spelpixels
const H := 40            # hoogte van de strook in spelpixels
const OPP := 8           # maaiveld
const GANG_BOVEN := 24   # bovenkant van de onderste rij (de gang)
const GANG_ONDER := 38   # anker van een figuur: voeten op y 37, de bovenste vloerrij van Daans gangtegel
const PUT_VLOER_Y := 8     # in het 3D-putstuk (16 hoog) beginnen de stekels op rij 8: daaronder is de vloerstrook

const SCHAT := preload("res://kunst/schat.png")
const PUT := preload("res://kunst/stekelput.png")
const FAKKEL := preload("res://kunst/fakkel.png")
const DECO := preload("res://kunst/versiering.png")
const GLOED := preload("res://kunst/gloed.png")
const KOOP_MUNT := preload("res://kunst/koop_munt.png")            # Mila 03:15: munt van twee beelden die draait
const PUT_UPG := preload("res://kunst/stekelput_upgrades.png")     # Mila 03:05: rij niveau - 1, zelfde indeling als stekelput.png
# Het hol in 3D (hol/hol_3d.gd, afspraak Bram en Olaf 13 nov 18:50). Uit = de oude pixeltegels. Een stuk dat niet in het
# blad staat valt per cel terug op de pixeltegel.
const HOL3D := preload("res://hol/hol_3d.gd")
var met_3d := true
# Het vaste deel van het hol in een eigen beeld (hol/hol_vast.gd). Uit = elk beeld alles opnieuw, zoals voor 13 nov.
const HOLVAST := preload("res://hol/hol_vast.gd")
const STAP_TEKEN := preload("res://systemen/stap_teken.gd")   # stap 4 tot 6: gouden stenen op de put (#162)
const STAP_STENEN := preload("res://systemen/stap_stenen.gd")
var _stenen: Node2D = null
var met_vast := true   # alleen een testschakelaar: uit = geen gemeten bovenrand, dan is het gras op Windows weg (strook.gd muisvlak)
var deco_proef := false      # deco_proef=1 (strook.gd): vaste versiering in de gang om op te keuren, niet in het echte spel
var vast

var kolommen := 0
var gang: Array[bool] = []    # onderste rij
var boven: Array[bool] = []   # bovenste rij (schacht, kamers, schatkamer)
var vallen := {}              # kolom -> soort ("stekelput")
var ingang_kol := 2
var schat_kol := 12
var max_kol := 9999           # verder graven niet: daar staat de tekst van de strook
var goud := 0                 # buit van gevallen helden; nooit iets kwijt als je weg bent
var anim := 0                 # beeldje van fakkels en schat; loopt alleen als er toch al getekend wordt
var put_open := {}            # kolom -> tijd tot de put weer dicht gaat (na een klap)
var munten: Array = []        # vliegende muntjes van een val naar de schat: {van, t}
# Gekochte stappen per bewoner en val (Brams systemen/upgrades.gd). held.gd en slijm.gd lezen ze via deze eigenschap;
# alles op niveau 0 verandert niets. Kopen komt met het kaartje (features.md feature 5, Olaf).
var upgrades = load("res://systemen/upgrades.gd").new() if ResourceLoader.exists("res://systemen/upgrades.gd") else null
const MUNT_S := 0.9           # zo lang vliegt een muntje
const STUIT_S := 0.25         # daarna stuitert een muntje dat op de schat valt één keer (leven in het spel, punt 1; Daan juice.md)
const STUIT_H := 3.0          # stuiter 30% van de valhoogte (boog 12 hoog bij de schat: 3 spelpixels, hele pixels)
const GLINSTER_S := 0.05      # bij de landing één beeld een wit puntje (Daan)
const MUNT_DX := [-3.0, 2.0, -1.0, 4.0, 0.0, -4.0]   # elk muntje landt op een eigen plek op de stapel (vast, zodat de keurstrook gelijk blijft)
var koop_munt: Array = []     # kolommen met een klein muntje erboven: hier kun je iets kopen (kern/kaartje.gd)
var koop_munt_y := {}         # kolom -> bovenkant van wat daar staat (Gloop met hoeden); het muntje komt 3 erboven

func maak(breedte_spelpixels: int) -> void:
	texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	kolommen = int(ceil(breedte_spelpixels / float(KOL)))
	gang.resize(kolommen)
	boven.resize(kolommen)
	for i in kolommen:
		gang[i] = i >= ingang_kol and i <= schat_kol
		boven[i] = false
	_schatkamer()
	vallen[7] = "stekelput"
	vast = HOLVAST.new()
	vast.h = self
	if met_vast:
		vast.maak_in(self)
	queue_redraw()

# leg het begin-hol aan met de schat op kolom s (rechts, tegen het tekstvak) en de ingang lengte kolommen ervoor
func leg_aan(s: int, lengte := 10) -> void:
	schat_kol = clampi(s, 3, kolommen - 1)
	# de ingang nooit op kolom 0: de ingang is breder dan een kolom en viel op een smal scherm half buiten beeld (Sanne toets 3, punt 4)
	ingang_kol = maxi(1, schat_kol - lengte)
	for i in kolommen:
		gang[i] = i >= ingang_kol and i <= schat_kol
		boven[i] = false
	_schatkamer()
	vallen.clear()
	vallen[maxi(ingang_kol + 1, mini(ingang_kol + 3, schat_kol - 5))] = "stekelput"   # 2 kolommen verder links dan eerst (Daan 10:50, Olaf 14:30): ruimte voor de hoedenberg
	queue_redraw()

# drie muntjes vliegen van kolom k naar de schat (Sanne toets 2, punt 2: goud zie je binnenkomen)
func munt_regen(k: int, n := 3) -> void:
	if moment_val_vast:
		return   # winkelbeeld staat stil: geen nieuwe muntjes die blijven hangen
	for i in n:
		munten.append({"van": float(k * KOL + KOL / 2.0), "t": -0.15 * i, "dx": MUNT_DX[i % MUNT_DX.size()]})
	set_process(true)

# na kopen: muntjes vliegen van de schat naar het object, omgekeerd van een val (Sanne, het kaartje)
func munt_naar(k: int, n := 3) -> void:
	for i in n:
		munten.append({"van": float(schat_kol * KOL + KOL / 2.0), "naar": float(k * KOL + KOL / 2.0), "t": -0.15 * i})
	set_process(true)

# de schatkamer achteraan is twee rijen hoog (Sanne, 9 nov 19:00), en Gloops plek ervoor ook (kolom schat - 2):
# daar is ruimte voor zijn hoedentoren van 4 hoog, anders steekt die in de aarde (Sanne toets 3, punt 3, besluit Olaf)
func _schatkamer() -> void:
	boven[schat_kol] = true
	for k in [schat_kol - 1, schat_kol - 2]:
		if k > ingang_kol:
			boven[k] = true

# ---- afspraak met de systemen ----
func is_gang(cel: Vector2i) -> bool:
	return cel.y == 0 and cel.x >= 0 and cel.x < kolommen and gang[cel.x]

func cel_naar_pos(cel: Vector2i) -> Vector2:
	# midden van de vloer van die cel, in spelpixels (anker van een figuur van 16 hoog)
	return Vector2(cel.x * KOL + KOL / 2.0, GANG_ONDER)

func pos_naar_cel(pos: Vector2) -> Vector2i:
	return Vector2i(clampi(int(pos.x / KOL), 0, kolommen - 1), 0)

func ingang() -> Vector2i:
	return Vector2i(ingang_kol, 0)

func schat() -> Vector2i:
	return Vector2i(schat_kol, 0)

func val_op(cel: Vector2i) -> String:
	return vallen.get(cel.x, "")

func pad(van: Vector2i, naar: Vector2i) -> Array[Vector2i]:
	var uit: Array[Vector2i] = []
	var stap := 1 if naar.x >= van.x else -1
	var x := van.x
	while true:
		if not is_gang(Vector2i(x, 0)):
			return []
		uit.append(Vector2i(x, 0))
		if x == naar.x:
			break
		x += stap
	return uit

# koop-moment van de put (Sanne toets 8 punt 1, toets 9): alle putten schudden 0,5 s heen en weer (1 spelpixel),
# want de gekochte stap geldt voor elke put. Alleen uiterlijk; tekent alleen zolang het schudt.
const SCHUD_S := 0.5
# Graven heeft een moment (Sanne toets 11, punt 2): een nieuwe cel brokkelt in 4 beelden open (aarde valt weg, steentjes
# vallen, een stofwolkje) en de ingang met zijn fakkel schuift in 0,4 s mee in plaats van te springen. Alleen uiterlijk:
# de cel is meteen open voor helden. Tekening in code tot Mila een blad `kunst/graaf.png` maakt (4 beelden van 16 x 16,
# de aarde die nog over is, links naar rechts); dan tekent _brokkel dat in plaats van de stippen.
const GRAAF_S := 0.45
const SCHUIF_S := 0.4
var brokkel := {}             # Vector2i(kolom, rij 0 of 1) -> tijd sinds graven
var ingang_van_x := -1.0      # x (spelpixels) waar de ingang vandaan schuift
var ingang_schuif := 0.0      # tijd die het schuiven nog duurt
var GRAAF_BLAD: Texture2D = load("res://kunst/graaf.png") if ResourceLoader.exists("res://kunst/graaf.png") else null
# Daan 14 nov: het graafmoment in de 3D-stijl, 4 beelden van 64 x 64 bladpixels (4 per spelpixel, zoals hol_proef.png),
# gemaakt uit het 3D-stuk aarde door ontwerp/steam/graaf-3d/maak_graaf.py. Steentjes en stof zitten in het blad.
# Lineair gefilterd zoals hol_3d.gd. Zonder blad (of met_3d uit) blijft het oude graafmoment.
const GRAAF3D_PAD := "res://kunst/3d/graaf_3d.png"
const GRAAF3D_PX := 64
var GRAAF3D: CanvasTexture = _laad_graaf3d()
var graaf_proef := false     # graaf_proef=1 (strook.gd): vier kamers staan stil in beeld 0 tot 3, alleen om op te keuren
var graaf_stil := {}         # cellen van de keurstrook die niet verder brokkelen
var graaf_rij_proef := {}    # keurstrook: gangcellen met een vaste rij (open naar links of rechts), anders graaf_rij()

static func _laad_graaf3d() -> CanvasTexture:
	if not ResourceLoader.exists(GRAAF3D_PAD):
		return null
	var t := CanvasTexture.new()
	t.diffuse_texture = load(GRAAF3D_PAD)
	t.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	return t

# welk beeld (0 tot 3) bij `tijd` seconden na het graven
static func graaf_beeld(tijd: float) -> int:
	return clampi(int(tijd / GRAAF_S * 4.0), 0, 3)

# welke rij van het 3D-graafblad: 0 midden, 1 open naar links, 2 open naar rechts, 3 open naar onder.
# Een kamer (rij 0 van het hol) ligt altijd boven een open gang; een gangcel opent naar de buur die al gang was.
# Zijn beide buren open (een gat dichtgraven), dan het midden.
static func graaf_rij(cel: Vector2i, gang_rij: Array) -> int:
	if cel.y == 0:
		return 3
	var l: bool = cel.x > 0 and gang_rij[cel.x - 1]
	var r: bool = cel.x < gang_rij.size() - 1 and gang_rij[cel.x + 1]
	if l and not r:
		return 1
	if r and not l:
		return 2
	return 0

# keurstrook: vier kamers boven de gang, links van de schatkamer, elk stil in een ander beeld van het graafmoment
func zet_graaf_proef() -> void:
	var gezet := 0
	for k in range(ingang_kol + 1, schat_kol - 1):
		if gezet >= 4:
			break
		if gang[k] and not boven[k] and not vallen.has(k):
			boven[k] = true
			brokkel[Vector2i(k, 0)] = (gezet + 0.5) / 4.0 * GRAAF_S
			graaf_stil[Vector2i(k, 0)] = true
			gezet += 1
	# Bram 14 nov: ook twee gangcellen rechts van de ingang, open naar links (beeld 1) en naar rechts (beeld 2), zodat de
	# rechte kant naast een gegraven buur in het echte beeld te keuren is (alleen keurstrook, de gang blijft open)
	var proef := [[ingang_kol + 2, 1, 1], [ingang_kol + 4, 2, 2]]
	for p in proef:
		var c := Vector2i(p[0], 1)
		if p[0] < schat_kol - 2 and gang[p[0]] and not vallen.has(p[0]):
			brokkel[c] = (p[2] + 0.5) / 4.0 * GRAAF_S
			graaf_stil[c] = true
			graaf_rij_proef[c] = p[1]
	queue_redraw()

func _graaf_moment(cel: Vector2i) -> void:
	brokkel[cel] = 0.0
	set_process(true)

func _ingang_x() -> float:
	if ingang_schuif <= 0.0 or ingang_van_x < 0.0:
		return float(ingang_kol * KOL)
	var f := 1.0 - ingang_schuif / SCHUIF_S
	f = 1.0 - (1.0 - f) * (1.0 - f)   # rustig uitlopen
	return lerpf(ingang_van_x, float(ingang_kol * KOL), f)

# de aarde die nog over is in een cel die net gegraven is, plus steentjes en stof
func _brokkel(cel: Vector2i, tijd: float) -> void:
	var x := float(cel.x * KOL)
	var y := float(OPP if cel.y == 0 else GANG_BOVEN)
	var beeld := graaf_beeld(tijd)
	if met_3d and GRAAF3D != null:
		# Bram 14 nov (kan Daan 09:35): rij 1 tot 3 van het blad zijn open naar de buur die al gang is, dus een rechte kant
		# en geen aardkorst tussen twee open cellen; een oud blad van één rij geeft altijd rij 0
		var rij: int = graaf_rij_proef.get(cel, graaf_rij(cel, gang)) if GRAAF3D.diffuse_texture.get_height() >= GRAAF3D_PX * 4 else 0
		draw_texture_rect_region(GRAAF3D, Rect2(x, y, KOL, KOL),
			Rect2(beeld * GRAAF3D_PX, rij * GRAAF3D_PX, GRAAF3D_PX, GRAAF3D_PX))
		return
	if GRAAF_BLAD != null:
		draw_texture_rect_region(GRAAF_BLAD, Rect2(x, y, KOL, KOL), Rect2(beeld * KOL, 0, KOL, KOL))
	else:
		# beeld 0 bijna dicht, beeld 3 nog een paar kruimels; welke stip blijft staan is vast per cel (geen geflikker)
		var over: float = [0.85, 0.55, 0.28, 0.08][beeld]
		for py in range(0, KOL, 2):
			for px in range(0, KOL, 2):
				if float(_hash(cel.x * 31 + px, cel.y * 17 + py) % 100) / 100.0 < over:
					draw_rect(Rect2(x + px, y + py, 2, 2), Color("#3f2846"))
	# steentjes vallen naar de vloer van de cel
	var vloer_y := y + KOL - 3
	for i in 3:
		var sx0 := x + 3 + i * 5
		var start := y + 2 + (i * 3) % 5
		var f := clampf(tijd / GRAAF_S * (1.0 + i * 0.25), 0.0, 1.0)
		var sy := lerpf(start, vloer_y, f * f)
		draw_rect(Rect2(sx0, sy, 2, 2), Color("#6e4a6a"))
		draw_rect(Rect2(sx0, sy, 1, 1), Color("#9a7090"))
	# stofwolkje dat uitdijt en vervaagt, op de vloer van de nieuwe cel
	var d := clampf(tijd / GRAAF_S, 0.0, 1.0)
	var stof := Color("#c9a27a", 0.45 * (1.0 - d))
	draw_circle(Vector2(x + 4, vloer_y), 2.0 + d * 3.0, stof)
	draw_circle(Vector2(x + KOL - 4, vloer_y), 2.0 + d * 3.0, stof)
	draw_circle(Vector2(x + KOL / 2.0, vloer_y - 2), 1.5 + d * 4.0, stof)

const SCHUD_X := [1, -1, 1, -1, 0]
var put_schud := 0.0
func put_koop() -> void:
	put_schud = SCHUD_S
	set_process(true)
	queue_redraw()

# Leven in het spel 5 (hoofdchat 15 nov 15:55, getallen Daan in ontwerp/steam/juice.md): bij de klap van de val een
# stofwolkje van 5 stofjes in een lichte aardetint, naar buiten en omhoog, 0,35 s en vervagend, en de put zelf 1 spelpixel
# omlaag en terug in 2 beelden (0,1 s). Geen schok van de strook; alles in hele spelpixels.
const STOF_S := 0.35
const SCHOK_S := 0.1
const STOF_KLEUR := Color("#ecc3a4")   # nog een trede lichter (kan Daan 15 nov 18:50: dan lezen ze als korrels)
# per stofje: [start x, start y, verschuiving x, verschuiving y over 0,35 s, maat]; x ten opzichte van het midden van de put,
# y ten opzichte van de bovenste vloerrij
# 5 stofjes (was 7; kan Daan 15 nov 19:55: 4 tot 5): de twee die het schuinst naar buiten waaiden eruit
const STOF := [[-4, 0, -5, -3, 1], [-2, -1, -3, -6, 1], [0, -1, 0, -5, 1], [2, -1, 3, -6, 1], [3, 0, 5, -3, 1]]   # alle stofjes 1 spelpixel (kan Daan 18:50)
var val_stof := {}             # kolom -> tijd sinds de klap
func stof_stofjes(kol: int) -> Array:
	var uit := []
	if not val_stof.has(kol):
		return uit
	var d := clampf(float(val_stof[kol]) / STOF_S, 0.0, 1.0)
	var u := 1.0 - (1.0 - d) * (1.0 - d)   # uitlopend: snel weg, dan zacht
	var mx := kol * KOL + int(KOL / 2.0)
	var vy := GANG_ONDER - 1
	for st in STOF:
		var x := mx + int(st[0]) + int(round(float(st[2]) * u))
		var y := vy + int(st[1]) + int(round(float(st[3]) * u))
		uit.append([Vector2i(x, y), int(st[4]), 1.0 - d])
	return uit

func put_schok(kol: int) -> int:
	return 1 if val_stof.has(kol) and float(val_stof[kol]) < SCHOK_S else 0

# een put klapt even open als er een held op komt (alleen uiterlijk)
func put_klap(kol: int) -> void:
	put_open[kol] = 2.0   # stekels blijven langer omhoog, zodat de val van de terugkomer een moment is (Sanne toets 7, punt 2)
	val_stof[kol] = 0.0
	set_process(true)
	queue_redraw()

# Winkelbeelden (Bram 15 nov, strook.gd), nooit in het echte spel:
# moment=val: strook.gd zet de vallende held boven de stekels stil en daarna moment_val_vast; de stekels blijven omhoog.
# moment=munt: bij de eerste val blijven de muntjes midden in hun boog hangen.
var moment_val := false
var moment_munt := false
var moment_val_vast := false
const MOMENT_VAL_F := 0.5     # muntjes op de helft van hun vlucht (hoogste punt van de boog)

func _process(delta: float) -> void:
	if moment_val_vast:
		return   # alles staat stil, er hoeft niets meer getekend te worden
	for k in put_open.keys():
		put_open[k] -= delta
		if put_open[k] <= 0.0:
			put_open.erase(k)
			queue_redraw()
	if put_schud > 0.0:
		put_schud = maxf(0.0, put_schud - delta)
		queue_redraw()
	for k in val_stof.keys():
		val_stof[k] += delta
		if val_stof[k] >= STOF_S:
			val_stof.erase(k)
		queue_redraw()
	for c in brokkel.keys():
		if graaf_stil.has(c):
			continue   # keurstrook: deze beelden blijven staan
		brokkel[c] += delta
		if brokkel[c] >= GRAAF_S:
			brokkel.erase(c)
		queue_redraw()
	if ingang_schuif > 0.0:
		ingang_schuif = maxf(0.0, ingang_schuif - delta)
		queue_redraw()
	for m in munten:
		m.t += delta
	if moment_munt and not munten.is_empty() and munten.all(func(m): return m.has("naar") == false):
		var laatste: float = munten.map(func(m): return float(m.t)).min()
		if laatste >= MUNT_S * MOMENT_VAL_F:
			# de laatste munt is op de helft, de eerdere 0,15 en 0,3 s verder: drie muntjes verspreid in de boog
			moment_val_vast = true
			queue_redraw()
			return
	munten = munten.filter(func(m): return m.t < munt_duur(m))
	if not munten.is_empty():
		queue_redraw()
	if put_open.is_empty() and munten.is_empty() and val_stof.is_empty() and put_schud <= 0.0 and brokkel.size() <= graaf_stil.size() and ingang_schuif <= 0.0:
		set_process(false)

# fakkels en schat bewegen alleen als er toch al getekend wordt (een held loopt); stil beeld kost bijna niets
func tik() -> void:
	anim += 1
	queue_redraw()

# ---- spelen (klikken komen van de strook, in spelpixels) ----
func klik(pos: Vector2) -> String:
	var k := pos_naar_cel(pos).x
	var bovenrij := pos.y < GANG_BOVEN
	if bovenrij:
		# een kamer graven boven de gang (naast een open cel), niet in de lucht
		if pos.y < OPP or boven[k] or not gang[k] or k > max_kol:
			return ""
		boven[k] = true
		_graaf_moment(Vector2i(k, 0))
		queue_redraw()
		gegraven.emit(Vector2i(k, -1))
		return "kamer"
	if not gang[k]:
		if k > max_kol:
			return ""
		# links van de ingang graven: de ingang schuift mee, zo groeit het hol naar links
		if k < 1:
			return ""   # kolom 0 blijft dicht, anders staat de ingang half buiten beeld
		if k == ingang_kol - 1:
			gang[k] = true
			ingang_van_x = _ingang_x()   # ook als hij nog schuift: vanaf waar hij nu staat, geen sprong
			ingang_kol = k
			ingang_schuif = SCHUIF_S
			_graaf_moment(Vector2i(k, 1))
			_graaf_moment(Vector2i(k, 0))   # de schacht schuift mee: die cel brokkelt ook open
			queue_redraw()
			gegraven.emit(Vector2i(k, 0))
			return "gegraven"
		# alleen graven naast een bestaande gang; de schat verhuist mee naar het einde, de oude kamer blijft staan
		if (k > 0 and gang[k - 1]) or (k < kolommen - 1 and gang[k + 1]):
			gang[k] = true
			_graaf_moment(Vector2i(k, 1))
			if k > schat_kol:
				schat_kol = k
				_schatkamer()
			queue_redraw()
			gegraven.emit(Vector2i(k, 0))
			return "gegraven"
		return ""
	if k != ingang_kol and k != schat_kol:
		if vallen.has(k):
			vallen.erase(k)
		else:
			vallen[k] = "stekelput"
		queue_redraw()
		return "val"
	return ""

func _hash(x: int, y: int) -> int:
	return int(abs(sin(x * 12.9898 + y * 78.233) * 43758.5453)) % 97

func _open(r: int, k: int) -> bool:
	if k < 0 or k >= kolommen:
		return false
	if r == 0:
		return boven[k] or k == ingang_kol
	return gang[k]

func _draw() -> void:
	var vloer := GANG_ONDER - 1   # bovenste vloerrij
	# gras, tegels, schatkamer, stippels, ingang en versiering: hol/hol_vast.gd, een eigen beeld dat alleen opnieuw
	# getekend wordt als er iets aan verandert (demolijst 2)
	if vast == null:
		pass
	elif met_vast:
		vast.ververs()
	else:
		vast.teken(self)
	var schat_3d := HOL3D.schatkamer_aan(self)
	var ix := _ingang_x()
	# net gegraven cellen: de aarde brokkelt weg (over de open tegel heen, onder de figuren)
	for c in brokkel:
		_brokkel(c, float(brokkel[c]))
	# vallen: stekelput dicht, en even open na een klap
	# gekochte stappen (Rusty Spikes, Deep Pit, Trick Lid) hebben elk een eigen rij in stekelput_upgrades.png
	var put_niv: int = upgrades.beeld_niveau("stekelput") if upgrades != null else 0   # stap 4 tot 6: beeld van stap 3 (#145)
	var sx := 0
	if put_schud > 0.0:
		sx = int(SCHUD_X[mini(SCHUD_X.size() - 1, int((SCHUD_S - put_schud) / SCHUD_S * SCHUD_X.size()))])
	for k in vallen:
		var f := 2 if put_open.has(k) else 0
		var sy := put_schok(k)
		if HOL3D.stuk(self, 1, k, schat_3d) == "put":
			continue   # deze dichte put zit al in het 3D-stuk
		# open (na een klap) en gekochte stappen: het 3D-stuk over de 3D-gang, met het schudden van de koop (Olaf 14 nov)
		var ps := HOL3D.put_in_schatkamer(self, k, schat_3d)
		if ps == "weg":
			continue   # in de 3D-schatkamer: dicht of Trick Lid dicht, de vloer is daar al dicht (Daan 14 nov 13:50)
		if ps != "" and HOL3D.teken_onder(self, ps, Vector2(k * KOL + sx, GANG_BOVEN + sy), PUT_VLOER_Y, 1):
			continue   # open of met gekochte stappen: alleen de vloerstrook, de rode koepel blijft erachter
		var p3 := "" if schat_3d and k >= schat_kol - 2 and k <= schat_kol else HOL3D.put_stuk(self, k)
		if p3 == "vast" or p3 == "gang" and sx == 0:
			continue
		if p3 != "" and HOL3D.teken(self, p3, Vector2(k * KOL + sx, GANG_BOVEN + sy)):
			continue
		if put_niv > 0:
			draw_texture_rect_region(PUT_UPG, Rect2(k * KOL + sx, vloer - 7 + sy, KOL, 8), Rect2(f * KOL, (put_niv - 1) * 8, KOL, 8))
		else:
			draw_texture_rect_region(PUT, Rect2(k * KOL + sx, vloer - 7 + sy, KOL, 8), Rect2(f * KOL, 0, KOL, 8))
	# stap 4 tot 6 (#162): per stap boven Trick Lid één gouden steen op het luik, schudt mee met de koop
	var put_tekens: int = STAP_TEKEN.aantal(upgrades.niveau("stekelput")) if upgrades != null else 0
	var put_plekken := []
	for k in (vallen if put_tekens > 0 else {}):
		if vallen[k] == "stekelput":
			put_plekken.append(Vector2(k * KOL + KOL / 2.0 + sx, GANG_ONDER - 1 + put_schok(k)))
	if put_tekens > 0 or _stenen != null:
		if _stenen == null:
			_stenen = STAP_STENEN.maak(self)   # eigen laag: alleen opnieuw tekenen als er iets aan verandert (CPU)
		_stenen.zet(put_plekken, put_tekens)
	# stofwolkje van de val, voor de put (Olaf 15 nov, juice 5)
	for k in val_stof:
		for st in stof_stofjes(k):
			var c := STOF_KLEUR
			c.a = float(st[2])   # begint helemaal dekkend (was 0,9)
			draw_rect(Rect2(Vector2(st[0]), Vector2(st[1], st[1])), c)
	# fakkels met gloed: bij de ingang en in de schatkamer
	var fk := [ingang_kol + 1, schat_kol - 1]
	var lamp := Color(1, 0.75, 0.45, 0.35)
	for i in fk.size():
		var k: int = fk[i]
		if k <= ingang_kol or k >= kolommen:
			continue
		if i == 1 and schat_3d:
			continue   # de 3D-schatkamer heeft zijn eigen twee fakkels (Daan 13 nov 22:55: die voor de goudberg mag weg)
		var fx: float = k * KOL + 4
		if i == 0:
			fx = ix + KOL + 4   # de fakkel bij de ingang schuift mee
		# gloed alleen op de pixeltegels: de 3D-gang heeft zijn eigen licht, en de gloed stopte daar als een lichter
		# vierkant op de celrand (Daan 13 nov 19:35, moet 1)
		if not (met_3d and HOL3D.heeft("gang")):
			draw_texture_rect_region(GLOED, Rect2(fx + 4 - 20, GANG_BOVEN + 4 - 20, 40, 40), Rect2(0, 0, 52, 52), lamp)
		# 3D-fakkel uit het deco-blad (vast beeld, het licht zit in de 3D-gang); hoogte uit de render (`uit`), anders gelijk met de pixelfakkel
		var fm := HOL3D.deco_maat("fakkel")
		var fy := HOL3D.deco_y("fakkel", GANG_BOVEN + 13 - fm.y)
		var fs: int = anim + i * 5
		if met_3d and HOL3D.heeft("gang") and fm != Vector2.ZERO and HOL3D.teken_fakkel(self,
				Vector2(fx + 4 - floor(fm.x / 2.0), fy), FLAKKER[fs % FLAKKER.size()], FLAKKER[(fs + 4) % FLAKKER.size()]):
			# leven in het spel, punt 4: een kleine flakkerende gloed om de vlam (bovenste 4 van de 12 spelpixels). Rond en
			# klein, zodat hij niet als vierkant op de celrand stopt (Daan 13 nov 19:35); verandert alleen met anim (tik()).
			# Daan (juice.md, keuring 15 nov 16:40): gloedkring ±12 spelpixels, alfa 0,18 tot 0,32, sterkte 0,85 tot 1. Midden op de vlam (5 spelpixels
			# onder de bovenkant van het blad, nagemeten in de film van run 43731281126). Geen apart kernblokje: dat las als
			# een grijs vierkantje boven de vlam; de vlam in het blad is zelf al geel.
			var fl := fakkel_flakker(anim, i)
			var r := 12.0 * fl.y
			draw_texture_rect_region(GLOED, Rect2(fx + 4 - r, fy + 5.0 - r, 2.0 * r, 2.0 * r), Rect2(0, 0, 52, 52), Color(1.0, 0.8, 0.45, fl.x))
			continue
		draw_texture_rect_region(FAKKEL, Rect2(fx, GANG_BOVEN + 1, 8, 12), Rect2((anim % 4) * 8, 0, 8, 12))
	# schatkamer: vaandel aan het plafond en de schat op de vloer
	if boven[schat_kol] and not schat_3d:
		draw_texture_rect_region(DECO, Rect2(schat_kol * KOL, OPP + 1, KOL, KOL), Rect2(8 * KOL, 0, KOL, KOL))
	var sf := (anim / 2) % 4
	if not schat_3d:   # de 3D-schatkamer heeft de kist er zelf in
		draw_texture_rect_region(SCHAT, Rect2(schat_kol * KOL - 4, vloer - 15, 24, 16), Rect2(sf * 24, 0, 24, 16))
	# vliegende muntjes: een boogje van de val naar de schat, 2 bij 2 spelpixels met een donkere rand
	var doel := schat_kol * KOL + KOL / 2.0
	for m in munten:
		if m.t < 0.0:
			continue
		var mp := munt_plek(m, doel, vloer)
		var x: float = mp.x
		var y: float = mp.y
		if met_3d:
			# 3D-stijl (Daan 06:40): rond en glanzend zoals het paneelmuntje, draait in de vlucht
			munt_3d(Vector2(x + 0.5, y + 0.5), 1.6, mp.z)
			if munt_glinstert(m):
				draw_rect(Rect2(x + 1, y - 1, 1, 1), Color.WHITE)
			continue
		draw_rect(Rect2(x - 1, y - 1, 3, 3), Color("#7a4a12"))
		draw_rect(Rect2(x - 1, y - 1, 2, 2), Color("#f2c14e"))
	# kun je iets kopen, dan een klein muntje boven Gloop of de put (Sanne, het kaartje): 2 bij 2 spelpixels met rand, twee beelden
	# die rustig wisselen als er toch getekend wordt; geen getal, geen geluid, niets buiten de strook
	# Mila's koop_munt.png: twee beelden van 8 x 8 om en om, leest als een munt die draait. Boven Gloop 3 spelpixels boven
	# zijn bovenste hoed (kaartje.gd munt_top), boven een put net onder het plafond van de gang.
	for k in koop_munt:
		var mx: float = k * KOL + KOL / 2.0 - 1
		var onder_y: float = float(koop_munt_y[k]) - 3.0 if koop_munt_y.has(k) else float(GANG_BOVEN + 8)
		if not koop_munt_y.has(k) and met_3d:
			onder_y -= munt_boven_put(HOL3D.put_stuk(self, k))
		var my: float = maxf(onder_y - 6.0, float(OPP + 1))   # munt 6 hoog (rij 1 tot 6 van het beeld), nooit boven het gras
		if koop_munt_y.has(k) and onder_y - 6.0 < float(OPP + 1):
			mx += MUNT_OPZIJ   # moet Daan 17 nov 07:45 (Bram): toren tot het gras, dan het muntje rechts naast de toren, niet erin
		if met_3d:
			# zelfde plek en maat als Mila's munt (rij 1 tot 6 van het 8 x 8 beeld), rond; de twee beelden worden vol en op zijn kant
			munt_3d(Vector2(mx + 1, my + 3), 3.0, 1.0 if (anim / 3) % 2 == 0 else 0.67)
			continue
		draw_texture_rect_region(KOOP_MUNT, Rect2(mx - 3, my - 1, 8, 8), Rect2(((anim / 3) % 2) * 8, 0, 8, 8))

# zoveel spelpixels hoger komt het koopmuntje boven een put met dit 3D-stuk. De lange stekels van Deep Pit (`put_2`)
# steken ±3 spelpixels boven de gang uit en raakten het muntje (weekopname 43620350203, Olaf 14 nov 17:40). Daan 18:30:
# 3 in plaats van 4, want op 4 raakt de munt een kiezel in de aardrij (eikel met steeltje); op 3 prikken de stekels niet.
# Andere stukken blijven op de oude plek.
const MUNT_OPZIJ := 10.0   # spelpixels rechts van het midden van Gloop: naast de bovenste hoed (hoeden ±7 breed vanaf het midden)
static func munt_boven_put(stuk: String) -> float:
	return 3.0 if stuk == "put_2" else 0.0

# Muntje in de 3D-stijl (Daan 14 nov 06:40), zonder nieuw blad: dezelfde vier kleuren als het paneelmuntje (kern/tekst.gd
# _munt): schaduw, donkere rand, goud, één glimlicht linksboven. c is het midden en r de straal in spelpixels; breed (0 tot 1)
# drukt hem horizontaal in, zo lijkt hij te draaien. Het hol staat op schaal 4 of 5, dus de cirkels zijn op het scherm glad.
const MUNT_SCHADUW := Color(0.12, 0.04, 0.12, 0.45)
const MUNT_RAND := Color("#aa691e")
const MUNT_GOUD := Color("#f2b632")
const MUNT_GLIM := Color("#fff0aa")
# Gladde rand (Mila 14 nov 23:50, trappetjes in de 4,5x winkelschermen): draw_circle heeft in Godot 4.3 geen antialiasing.
# Daarom tekenen we in schermpixels (transform gedeeld door de schaal van het hol) en leggen we om elke cirkel een
# antialiased boog van 1 schermpixel breed, een halve pixel naar binnen; zo blijft de munt even groot. Een boog met
# breedte 0,3 in spelpixels werd 4 px wazig, want Godot rekent de zachte rand in plaatselijke eenheden (lokaal gemeten,
# `producten/steam-hol/bewijs-winkel3d/munt-glad/`).
func munt_3d(c: Vector2, r: float, breed := 1.0) -> void:
	var k := maxf(get_global_transform().get_scale().x, 1.0)
	draw_set_transform(c, 0.0, Vector2(clampf(breed, 0.2, 1.0), 1.0) / k)
	munt_laag(Vector2(0.15, 0.4) * k, r * k, MUNT_SCHADUW)
	munt_laag(Vector2.ZERO, r * k, MUNT_RAND)
	munt_laag(Vector2(-0.08, -0.08) * k, r * 0.72 * k, MUNT_GOUD)
	munt_laag(Vector2(-0.33, -0.38) * r * k, r * 0.24 * k, MUNT_GLIM)
	draw_set_transform(Vector2.ZERO, 0.0, Vector2.ONE)

# één cirkel met gladde rand, maten in schermpixels (zie munt_3d)
func munt_laag(c: Vector2, r: float, kleur: Color) -> void:
	var rr := maxf(r - 0.5, 0.5)
	# doorzichtig (de schaduw): schijf een halve pixel kleiner, anders mengt de rand dubbel (controleur 15 nov)
	draw_circle(c, rr - 0.5 if kleur.a < 1.0 else rr, kleur)
	draw_arc(c, rr, 0.0, TAU, 48, kleur, 1.0, true)

# hoe lang een muntje leeft: vliegen, en op de schat nog stuiteren (muntjes naar een gekocht ding stuiteren niet)
static func munt_duur(m: Dictionary) -> float:
	return MUNT_S + (0.0 if m.has("naar") else STUIT_S)

# plek van een muntje (x, y in spelpixels) en hoe breed het staat (z, 0,3 tot 1). Leven in het spel, punt 1: een muntje dat
# op de schat valt landt een paar spelpixels naast het midden (dx) en stuitert twee keer, 3 en 1 spelpixel hoog, dan is het
# weg in de stapel. Tijdens het stuiteren draait het langzamer en ligt het aan het eind plat (breed 0,3: op zijn kant).
static func munt_plek(m: Dictionary, doel: float, vloer: float) -> Vector3:
	var naar: float = float(m.get("naar", doel))
	var dx: float = float(m.get("dx", 0.0))
	var t: float = float(m.t)
	if t <= MUNT_S or m.has("naar"):
		var f: float = clampf(t / MUNT_S, 0.0, 1.0)
		return Vector3(round(lerpf(float(m.van), naar + dx * 0.5, f)), round(vloer - 6 - sin(f * PI) * 12), munt_draai(f * 3.0))
	var p: float = clampf((t - MUNT_S) / STUIT_S, 0.0, 1.0)
	var h: float = round(STUIT_H * sin(p * PI))
	return Vector3(round(naar + dx * (0.5 + 0.5 * p)), vloer - 6 - h, lerpf(munt_draai(3.0 + p * 1.5), 0.3, p * p))

# glinster: het eerste beeld na de landing op de schat (alleen muntjes die op de stapel vallen)
static func munt_glinstert(m: Dictionary) -> bool:
	return not m.has("naar") and float(m.t) > MUNT_S and float(m.t) <= MUNT_S + GLINSTER_S
# flakkeren van fakkel i bij beeld a: (alfa van de gloed, maat 0,85 tot 1). Vast patroon van 7 standen, de twee fakkels
# lopen niet gelijk. Alleen een nieuw beeld als er toch getekend wordt (tik()), dus stil beeld kost niets extra.
# Zachte overgang (Daan): buren in het patroon liggen dicht bij elkaar, geen sprong van donker naar fel.
const FLAKKER := [0.2, 0.45, 0.75, 1.0, 0.8, 0.55, 0.3, 0.0, 0.25, 0.55, 0.7, 0.45]
static func fakkel_flakker(a: int, i: int) -> Vector2:
	var f: float = FLAKKER[(a + i * 5) % FLAKKER.size()]
	return Vector2(0.18 + 0.14 * f, 0.85 + 0.15 * f)

# hoe breed een draaiend muntje is op draai d (1 = één halve slag): tussen 0,3 (op zijn kant) en 1 (plat voor je)
static func munt_draai(d: float) -> float:
	return 0.3 + 0.7 * absf(cos(d * PI))
