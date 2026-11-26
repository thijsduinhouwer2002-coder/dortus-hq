extends RefCounted
# Dichte put = luik van hout met een donkere rand (Mila 26 nov, issue #209; Iris keuring bb298d3 punt 1: "een dichte put
# is onzichtbaar, je ziet niet waar je val staat en wat je kocht"). Blad kunst/luik.png uit modellen/luik.py (Blender):
# vier beelden naast elkaar, één per stap van de put (0 gewoon, 1 roest met roestpunten, 2 diep met lange stalen
# punten, 3 Trick Lid met aarde en gras erop; stap 4 tot 6 houden beeld 3, de gouden ruiten liggen erop).
# Klapt de put open, dan tekent hol.gd geen luik en zie je de stekels zoals altijd.
# Eén plaatje per put, alleen als hol.gd toch al tekent (geen eigen beweging, geen extra tekenbeurt per beeld).
# Startargument luik=0 zet het luik uit (oude put), voor de meting tegen zonder.

const BLAD := preload("res://kunst/luik.png")
const CEL_W := 18.0      # spelpixels per beeld (modellen/luik.py)
const CEL_H := 12.0      # 12 sinds Daan #213 M1: de dikke stalen punten van Deep Pit passen erin
const BEELDEN := 4
const MIDDEN_Y := 34.5   # midden van de cel; onderkant op 40,5 zoals toen (voeten staan op 37)

const OPLICHT := 0.3     # het luik licht iets meer op dan de put (PUT_OPLICHT 0,2 bovenop): ook ver van de fakkel lees je het hout

static var _tex: CanvasTexture = null
static var _aan := -1

static func aan() -> bool:
	if _aan < 0:
		_aan = 0 if "luik=0" in OS.get_cmdline_user_args() else 1
	return _aan == 1

static func _blad() -> CanvasTexture:
	if _tex == null:
		_tex = CanvasTexture.new()
		_tex.diffuse_texture = BLAD
		_tex.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
	return _tex

# Teken het luik voor stap `niv` met het midden van de kolom op x; dy = schok of schudden. false = luik uit.
static func teken(doek: CanvasItem, x: float, dy: float, niv: int, kleur: Color = Color.WHITE) -> bool:
	if not aan():
		return false
	var b := clampi(niv, 0, BEELDEN - 1)
	var bw := float(BLAD.get_width()) / BEELDEN
	var bron := Rect2(b * bw, 0.0, bw, float(BLAD.get_height()))
	doek.draw_texture_rect_region(_blad(), Rect2(x - CEL_W / 2.0, MIDDEN_Y - CEL_H / 2.0 + dy, CEL_W, CEL_H), bron, kleur)
	return true

# kleur van het luik: het licht van de gang (hol.gd put_kleur) nog wat lichter, zodat het hout ook in het donker opvalt
static func kleur(put_kleur: Color) -> Color:
	return put_kleur.lerp(Color.WHITE, OPLICHT)
