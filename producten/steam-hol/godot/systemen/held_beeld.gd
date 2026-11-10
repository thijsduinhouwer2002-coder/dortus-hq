extends RefCounted
# Tekenen van de held (Bram), los van held.gd zodat dat bestand klein blijft. held.gd roept in _draw()
# HELD_BEELD.teken(self) aan; alles wordt op de held zelf getekend (dat mag alleen tijdens zijn _draw).
# Kunst van Daan (kunst/LEESMIJ.md, Karakter-laag 19:45): lijf in 5 vaste kleuren, littekens als losse laag,
# hoed met een hap als Gloop hem beet, tekens (8 x 8) boven het hoofd. Nooit schalen (halve pixels).

const LIJF := preload("res://kunst/held_lijf_kleuren.png")   # 4 loopframes x 5 rijen (rood, groen, paars, oker, zeegroen)
const HOEDEN := preload("res://kunst/held_hoeden.png")
const HOEDEN_HAP := preload("res://kunst/held_hoeden_hap.png")
const LITTEKENS := preload("res://kunst/held_littekens.png")  # pleister, ooglap, schram, verband
const WAPENS := preload("res://kunst/held_wapens.png")
const POEF := preload("res://kunst/poef.png")                 # Mila 10 nov: boze wolkje knapt, 4 x (12 x 10)
const TEKENS := preload("res://kunst/tekens.png")            # boos, uitroep, zweet, zzz, ster
const TEKEN := {"boos": 0, "uitroep": 1, "zweet": 2, "zzz": 3, "ster": 4}

# Daans lijf + litteken + hoed + wapen (16 x 16, anker midden onder), teken erboven.
static func teken(h) -> void:
	var staat: String = String(h.staat)
	if staat == "weg":
		return
	var t: float = float(h.t)
	var frame := 0
	if staat in ["lopen", "vluchten"]:
		frame = int(t * 8) % 4
	var omlaag := 1 if frame in [1, 3] else 0
	var links := staat == "vluchten"
	var wapen := 2 if String(h.trek) == "schijterig" else 0       # schijterig neemt een fakkel mee, hebzuchtig een zwaard
	var kleur := Color.WHITE
	if t < float(h.geraakt_tot) and int(t * 10) % 2 == 0:
		kleur = Color(1, 0.55, 0.55)
	var vb: Dictionary = {}
	var zak := 0
	var hop := 0
	if staat == "vallen":
		vb = h.val_beeld(float(h.val_t))
		zak = int(vb.zak)
		hop = int(vb.hop)
	if links:
		h.draw_set_transform(Vector2.ZERO, 0, Vector2(-1, 1))   # spiegelen, geen halve pixels
	var y := -16 + zak + hop
	var hoed_nr: int = int(h.hoed_nr)
	# bij een hop staat hij boven de vloer: niets afsnijden; bij zakken alles onder y 0 weg
	_laag(h, LIJF, frame * 16, int(h.kleur_nr) * 16, y, zak, kleur)
	for l in h.littekens:
		_laag(h, LITTEKENS, int(l) * 16, 0, y + omlaag, zak, kleur)
	if vb.is_empty() or bool(vb.hoed):
		_laag(h, HOEDEN_HAP if bool(h.is_gebeten()) else HOEDEN, hoed_nr * 16, 0, y + omlaag, zak, kleur)
	if staat != "vallen":
		_laag(h, WAPENS, wapen * 16, 0, y + omlaag, 0, kleur)
	h.draw_set_transform(Vector2.ZERO, 0, Vector2.ONE)
	# teken: één lege rij boven de bovenkant van de hoed (Sanne toets 2: 1 tot 2 spelpixels boven het hoofd)
	var tk: String = String(h.teken_nu()) if staat != "vallen" else String(vb.teken)
	if tk == "":
		return
	var tops: Array = h.get_script().get_script_constant_map().get("HOED_TOP", [])   # HOED_TOP blijft in held.gd (strook.gd leest hem daar)
	var onder: int = y + (int(tops[hoed_nr]) if hoed_nr < tops.size() else 0) + omlaag - 1
	if tk == "poef":
		_poef(h, onder - 4, float(vb.poef_fase))
		return
	h.draw_texture_rect_region(TEKENS, Rect2(-4, onder - 8, 8, 8), Rect2(int(TEKEN[tk]) * 8, 0, 8, 8))

# Eén laag van 16 x 16 tekenen, onder de vloerlijn (y 0) afgesneden: zo zakt hij weg zonder te schalen.
static func _laag(h, tex: Texture2D, bron_x: int, bron_y: int, y: int, zak: int, kleur: Color) -> void:
	var hoogte := 16 - zak
	if hoogte <= 0:
		return
	h.draw_texture_rect_region(tex, Rect2(-8, y, 16, hoogte), Rect2(bron_x, bron_y, 16, hoogte), kleur)

# Het boze wolkje knapt: Mila's poef.png (kunst/LEESMIJ.md, 10 nov), 4 beelden van 12 x 10, 10 fps, één keer.
# Midden van het wolkje op (6, 3) in het beeld, dus op de plek van het oude wolkje min 2 px in x. Nooit schalen.
# fase loopt van 0 tot 1 in VAL_TEKEN_S (0,4 s), dus 4 beelden in 0,4 s = 10 fps.
static func poef_beeld(fase: float) -> int:
	return clampi(int(fase * 4.0), 0, 3)

static func _poef(h, midden_y: int, fase: float) -> void:
	h.draw_texture_rect_region(POEF, Rect2(-6, midden_y - 4, 12, 10), Rect2(poef_beeld(fase) * 12, 0, 12, 10))
