extends RefCounted
# Het hol in 3D (Olaf, 13 nov; voorstel Bram 18:30, besluit Olaf 18:50 in platformen/steam/taken.md).
# De stukken komen uit Mila's hol.py via Brams pijplijn: blad kunst/3d/hol_proef.png, per stuk `vak_px` (plek in het
# blad, 4 bladpixels per spelpixel) en `maat` (spelpixels) in kunst/3d/sprites.json.
# Ontbreekt het blad of een stuk, dan geeft teken() false en tekent hol.gd de oude pixeltegel: main gaat nooit kapot
# als het blad half af is. De schatkamer telt pas als hij 48 breed is (3 kolommen, afspraak 1 met Bram).

const JSON_PAD := "res://kunst/3d/sprites.json"
const SCHATKAMER_B := 48

static var blad: CanvasTexture = null
static var stukken := {}
static var gezocht := false
# losse versiering op een doorzichtig blad (Bram 13 nov 23:30, Daan 22:55): fakkel, ladder; zelfde schaal en licht
static var deco_blad: CanvasTexture = null
static var deco := {}

static func laad() -> void:
	if gezocht:
		return
	gezocht = true
	if not FileAccess.file_exists(JSON_PAD):
		return
	var d = JSON.parse_string(FileAccess.get_file_as_string(JSON_PAD))
	if typeof(d) != TYPE_DICTIONARY:
		return
	if d.has("deco") and typeof(d["deco"]) == TYPE_DICTIONARY and typeof(d["deco"].get("stukken")) == TYPE_DICTIONARY \
			and ResourceLoader.exists(str(d["deco"].get("blad", ""))):
		deco_blad = CanvasTexture.new()
		deco_blad.diffuse_texture = load(str(d["deco"]["blad"]))
		deco_blad.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
		deco = d["deco"]["stukken"]
	if not d.has("hol_proef"):
		return
	var info: Dictionary = d["hol_proef"]
	if not info.has("stukken") or not ResourceLoader.exists(str(info.get("blad", ""))):
		return
	blad = CanvasTexture.new()
	blad.diffuse_texture = load(str(info["blad"]))
	blad.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	stukken = info["stukken"]

static func heeft(naam: String) -> bool:
	laad()
	if blad == null or not stukken.has(naam):
		return false
	if naam.begins_with("schatkamer"):
		return int(stukken[naam]["maat"][0]) == SCHATKAMER_B
	return true

# Teken stuk `naam` met de linkerbovenhoek op `plek` (spelpixels), op zijn eigen maat. false = niet getekend.
static func teken(doek: CanvasItem, naam: String, plek: Vector2) -> bool:
	if not heeft(naam):
		return false
	var s: Dictionary = stukken[naam]
	var v: Array = s["vak_px"]
	var m: Array = s["maat"]
	doek.draw_texture_rect_region(blad, Rect2(plek, Vector2(m[0], m[1])), Rect2(v[0], v[1], v[2], v[3]))
	return true

# Versiering uit het deco-blad met de linkerbovenhoek op `plek`, op zijn eigen maat. false = niet getekend (dan pixels).
static func teken_deco(doek: CanvasItem, naam: String, plek: Vector2) -> bool:
	laad()
	if deco_blad == null or not deco.has(naam):
		return false
	var v: Array = deco[naam]["vak_px"]
	var m: Array = deco[naam]["maat"]
	doek.draw_texture_rect_region(deco_blad, Rect2(plek, Vector2(m[0], m[1])), Rect2(v[0], v[1], v[2], v[3]))
	return true

# bovenkant van het stuk in spelpixels zoals de render hem zette (`uit`, beeld = spel), of `anders` als die er niet is
static func deco_y(naam: String, anders: float) -> float:
	laad()
	if not deco.has(naam) or not deco[naam].has("uit"):
		return anders
	return float(deco[naam]["uit"][1])

static func deco_maat(naam: String) -> Vector2:
	laad()
	if not deco.has(naam):
		return Vector2.ZERO
	return Vector2(deco[naam]["maat"][0], deco[naam]["maat"][1])

# De pixelversiering die nog over is (Daan 13 nov 19:35, kan: "pixels met zwarte rand staan hard op de zachte 3D-grond").
# Namen in het deco-blad, op de volgorde van de vakken in kunst/versiering.png en kunst/maaiveld.png. Staat een naam niet
# in het blad, dan blijft dat ding pixels; zo werkt main met elk blad.
const DECO_GANG := ["paddenstoel", "lichtzwam", "ton", "krat", "schedel", "kristal", "spinrag", "stut", "vaandel"]
const DECO_MAAIVELD := ["bloemen", "struik", "steen", "bordje", "vliegenzwam"]

# Linkerbovenhoek voor stuk `naam` zodat zijn ankerpunt op `punt` valt (spelpixels). Staand: het voetpunt (standaard
# midden onderkant, of `voet` [x, y] binnen het stuk uit de pijplijn). Hangend: het hangpunt (standaard midden bovenkant,
# of `hang` [x, y]). Hele spelpixels, zoals de rest van het hol. Vector2.INF als het stuk niet in het blad staat.
static func deco_plek(naam: String, punt: Vector2, hangend: bool) -> Vector2:
	var m := deco_maat(naam)
	if m == Vector2.ZERO or deco_blad == null:
		return Vector2.INF
	var sleutel := "hang" if hangend else "voet"
	var a := Vector2(m.x / 2.0, 0.0 if hangend else m.y)
	var s: Dictionary = deco[naam]
	if s.has(sleutel) and typeof(s[sleutel]) == TYPE_ARRAY and s[sleutel].size() == 2:
		a = Vector2(float(s[sleutel][0]), float(s[sleutel][1]))
	return (punt - a).floor()

# Teken versiering met het ankerpunt op `punt`; false = niet in het blad (dan tekent de aanroeper de pixels).
static func teken_deco_op(doek: CanvasItem, naam: String, punt: Vector2, hangend: bool) -> bool:
	var plek := deco_plek(naam, punt, hangend)
	if plek == Vector2.INF:
		return false
	return teken_deco(doek, naam, plek)

# 3D-stuk voor cel (rij r, kolom k), of "" als die cel de pixeltegel houdt
# (de schacht houdt de pixeltegel als het 3D-stuk ingang ontbreekt; een open put of een put met gekochte stappen krijgt de
# 3D-gang en de pixel-put erover, zodat je niet twee putten door elkaar ziet en het schudden van de koop te zien is)
static func stuk(h, r: int, k: int, schat_3d: bool) -> String:
	if not h.met_3d or schat_3d and k >= h.schat_kol - 2 and k <= h.schat_kol:
		return ""
	if k == h.ingang_kol and not heeft("ingang"):
		return ""
	var naam := "aarde"
	if r == 1 and h.gang[k]:
		var put_niv: int = h.upgrades.niveau("stekelput") if h.upgrades != null else 0
		naam = "put" if h.vallen.has(k) and not h.put_open.has(k) and put_niv == 0 and heeft("put") else "gang"
	elif r == 0 and h.boven[k] and k != h.ingang_kol:
		# één brede kamer (moet 3, Daan 20:50, Bram 21:30): het stuk volgt de buren; ontbreekt het, dan kamer_los,
		# dan de oude losse kommen (zolang een blad die nog heeft)
		for n in [kamer_keuze(h.boven, k, h.ingang_kol, h.schat_kol, schat_3d), "kamer_los",
				"kamer_links" if k % 2 == 0 else "kamer_rechts"]:
			if heeft(n):
				return n
		return ""
	return naam if heeft(naam) else ""

# welk kamerstuk een open cel k in de bovenste rij krijgt, alleen op de buren (zonder te kijken of het blad het heeft).
# Schacht en 3D-schatkamer tellen als niet gegraven. Midden wisselt a en b op k % 2, zodat een lange kamer niet
# steeds hetzelfde stuk herhaalt.
static func kamer_keuze(boven: Array, k: int, ingang_kol: int, schat_kol: int, schat_3d: bool) -> String:
	var l := _kamer_open(boven, k - 1, ingang_kol, schat_kol, schat_3d)
	var r := _kamer_open(boven, k + 1, ingang_kol, schat_kol, schat_3d)
	if l and r:
		return "kamer_midden_a" if k % 2 == 0 else "kamer_midden_b"
	if r:
		return "kamer_begin"
	if l:
		return "kamer_eind"
	return "kamer_los"

static func _kamer_open(boven: Array, k: int, ingang_kol: int, schat_kol: int, schat_3d: bool) -> bool:
	if k < 0 or k >= boven.size() or k == ingang_kol or not boven[k]:
		return false
	return not (schat_3d and k >= schat_kol - 2 and k <= schat_kol)

# de schatkamer in 3D beslaat 3 kolommen en 2 rijen; alleen als het blad hem 48 breed heeft en de 3 kolommen open zijn
static func schatkamer_aan(h) -> bool:
	if not h.met_3d or h.schat_kol - 2 <= h.ingang_kol or not heeft("schatkamer"):
		return false
	return h.boven[h.schat_kol] and h.boven[h.schat_kol - 1] and h.boven[h.schat_kol - 2]
