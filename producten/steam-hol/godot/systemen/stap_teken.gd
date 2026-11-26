extends RefCounted
# Stap 4 tot 6 zichtbaar (Olaf 26 nov, issue #162; Iris keuring 499fd9f punt 1: "koop verandert niets").
# Stap 1 tot 3 hebben elk eigen kunst (groter, veren, troon; roest, diep, valluik). Stap 4 tot 6 waren alleen getallen,
# dus Royal Gloop en Gloop Prime zagen er gelijk uit. Nu krijgt Gloop en elke put per gekochte stap boven 3 één gouden
# steen op de vloer: stap 4 één, stap 5 twee, stap 6 drie. Tellen kan iedereen, dus de volgorde lees je zonder uitleg.
# Zelfde vier kleuren als het muntje (hol.gd munt_3d), zodat het bij het goud hoort; ruitvorm, zodat het geen
# munt is (een rond muntje boven Gloop of de put betekent "dit kun je kopen"). Geen beweging: kost niets extra per beeld.
# Getekend in schermpixels met een gladde rand, net als munt_3d (op schaal 3 tot 4 anders trappetjes).

const RAND := Color("#6e3f0e")      # donkerder dan de munt-rand, anders verdwijnt hij op de gele veren van Gloop
const GOUD := Color("#f2b632")
const GLIM := Color("#fff0aa")
const SCHADUW := Color(0.12, 0.04, 0.12, 0.5)
const HALF := 2.0        # halve breedte van een steen in spelpixels (4 breed, 12 schermpixels op 120)
const AFSTAND := 4.5     # midden tot midden

# Hoeveel stenen bij dit niveau (0 tot 6): alleen boven stap 3.
static func aantal(niveau: int, beeld_max: int = 3) -> int:
	return clampi(niveau - beeld_max, 0, 3)

# Midden van steen i van n, ten opzichte van het midden van de rij (spelpixels).
static func plek(i: int, n: int) -> float:
	return (float(i) - float(n - 1) / 2.0) * AFSTAND

# Teken n stenen in een rij met het midden op c (spelpixels, lokaal van doek).
static func teken(doek: CanvasItem, c: Vector2, n: int) -> void:
	if n <= 0:
		return
	var k := maxf(doek.get_global_transform().get_scale().x, 1.0)
	for i in n:
		var m := c + Vector2(plek(i, n), 0.0)
		doek.draw_set_transform(m, 0.0, Vector2.ONE / k)
		var h := HALF * k
		_ruit(doek, Vector2(0.5, 1.0), h, SCHADUW)
		_ruit(doek, Vector2.ZERO, h, RAND)
		_ruit(doek, Vector2.ZERO, h - 1.6, GOUD)
		# glimvlak linksboven: een kleine driehoek, leest als een geslepen steen
		var g := h - 1.6
		doek.draw_colored_polygon(PackedVector2Array([Vector2(0, -g), Vector2(-g, 0), Vector2(-g * 0.25, -g * 0.25)]), GLIM)
	doek.draw_set_transform(Vector2.ZERO, 0.0, Vector2.ONE)

static func _ruit(doek: CanvasItem, o: Vector2, h: float, kleur: Color) -> void:
	var p := PackedVector2Array([o + Vector2(0, -h), o + Vector2(h, 0), o + Vector2(0, h), o + Vector2(-h, 0)])
	doek.draw_colored_polygon(p, kleur)
	var r := p.duplicate()
	r.append(p[0])
	doek.draw_polyline(r, kleur, 1.0, true)   # gladde rand van 1 schermpixel
