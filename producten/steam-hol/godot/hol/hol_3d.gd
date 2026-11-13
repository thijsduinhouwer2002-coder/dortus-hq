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

static func laad() -> void:
	if gezocht:
		return
	gezocht = true
	if not FileAccess.file_exists(JSON_PAD):
		return
	var d = JSON.parse_string(FileAccess.get_file_as_string(JSON_PAD))
	if typeof(d) != TYPE_DICTIONARY or not d.has("hol_proef"):
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
