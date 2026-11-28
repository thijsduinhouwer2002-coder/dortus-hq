# Hol 2.0 proef (Olaf, #401, Sanne punt 6): de muis zonder focus.
# - Gloop staat stil als de muis binnen 4 spelpx van zijn lijf is (stap afmaken, blijven staan, kijken).
#   Een muis die langer dan 3 s niet bewoog telt niet meer (Daan #414 kan 1): anders blijft Gloop voor altijd staan
#   als hij tegen een stilliggende muis aan loopt. Bij een nieuwe beweging telt hij weer.
# - Klikvak van Gloop is zijn lijf plus 4 spelpx; een klik op de troon met de goudberg opent ook het kaartje.
# - Terugvalpijltjes van 7 spelpx op een donker plaatje van 9 op de rechterrand, klikvak 14 x 12 (Daan #414 kan 2), voor wie geen muiswiel heeft (of als het wiel niet aankomt).
# - Meten of muisbewegingen aankomen zonder focus: de eerste beweging komt in de log, en het aantal per 10 s.
# De plek van de muis wordt elk beeld gelezen (DisplayServer.mouse_get_position, werkt ook zonder focus), dus Gloop
# stopt ook als het venster geen bewegingen krijgt. Statische functies met hol2.gd als eerste argument (`s`).
extends RefCounted

const RAND := 4.0
const PLAAT := 9.0     # donker plaatje achter het pijltje van 7
const VAK := Vector2(14, 12)   # klikvak per pijltje: de onderste 24 spelpx van de rechterrand, boven en onder
const STIL := 3.0      # s: zo lang telt een muis die niet beweegt nog als "bij Gloop"

# Waar staat de muis in spelpixels van het scherm (niet geschoven)? Vector2(-1, -1) als hij niet boven het hol is.
static func plek(s) -> Vector2:
	if s.film:
		return s.muis_film
	var m := DisplayServer.mouse_get_position() - DisplayServer.window_get_position()
	var w := DisplayServer.window_get_size()
	if m.x < 0 or m.y < 0 or m.x >= w.x or m.y >= w.y:
		return Vector2(-1, -1)
	return Vector2(m) / float(s.schaal)

static func werk(s) -> void:
	var p := plek(s)
	s.muis_scherm = p
	if p != s.muis_vorig:
		s.muis_vorig = p
		s.muis_beweeg_t = s.t
	var dicht := false
	if p.x >= 0.0 and not s.besturen and s.t - s.muis_beweeg_t <= STIL:
		var wp: Vector2 = p + Vector2(0, roundf(s.scroll))
		dicht = s.gloop.lijf().grow(RAND).has_point(wp)
		s.gloop.muis_x = wp.x
	if dicht != s.gloop.muis_dicht:
		s.gloop.muis_dicht = dicht
		var waarom := "muis weg" if p.x < 0.0 or not s.gloop.lijf().grow(RAND).has_point(p + Vector2(0, roundf(s.scroll))) else "muis 3 s stil"
		s.log_regel("HOL2 gloop %s gloop x=%d" % ["staat stil (muis bij Gloop)" if dicht else "gaat verder (%s)" % waarom, int(s.gloop.x)])

static func beweging(s) -> void:
	s.muis_n += 1
	if s.muis_n == 1:
		s.log_regel("HOL2 muisbeweging aangekomen (focus %s)" % ("ja" if s.get_window().has_focus() else "nee"))

# Klikvak van Gloop (lijf plus 4 spelpx) en van de troon met de goudberg, in spelpixels van de wereld.
static func op_gloop(s, wp: Vector2) -> bool:
	return s.gloop.lijf().grow(RAND).has_point(wp)

static func op_troon(s, wp: Vector2) -> bool:
	var k = s.kaart
	var v: int = k.voet_y(k.troon_niveau)
	return Rect2(k.troon_x - 18, v - 18, 48, 18).has_point(wp)

# Klikvakken van de terugvalpijltjes rechtsonder in de strook: [omhoog, omlaag], in spelpixels van het scherm.
static func pijlen(s) -> Array:
	var x: float = s.breed - VAK.x
	return [Rect2(Vector2(x, s.spel_h - 2.0 * VAK.y), VAK), Rect2(Vector2(x, s.spel_h - VAK.y), VAK)]

# Het donkere plaatje van 9 in het klikvak (omhoog bovenaan tegen de ander, omlaag onderaan): blijft bij elkaar.
static func plaat(r: Rect2, omhoog: bool) -> Rect2:
	return Rect2(r.position + Vector2(VAK.x - PLAAT - 2.0, VAK.y - PLAAT - 1.0 if omhoog else 1.0), Vector2(PLAAT, PLAAT))

static func pijl_aan(s, i: int) -> bool:
	return s.max_scroll > 0.0 and (s.scroll_doel > 0.0 if i == 0 else s.scroll_doel < s.max_scroll)

# Een klik op een pijltje schuift één verdieping. Geeft true als de klik op een pijltje was.
static func klik_pijl(s, p: Vector2) -> bool:
	var r: Array = pijlen(s)
	for i in 2:
		if pijl_aan(s, i) and r[i].has_point(p):
			s.scroll_doel = clampf(s.scroll_doel + (-48.0 if i == 0 else 48.0), 0.0, s.max_scroll)
			s.log_regel("HOL2 pijltje %s, schuif naar %d" % ["omhoog" if i == 0 else "omlaag", int(s.scroll_doel)])
			return true
	return false
