# Hol 2.0 proef (Olaf, #388): iets wat over de verdiepingen loopt en via ladders klimt (Gloop en de helden).
# Positie in spelpixels van de wereld: x is het midden, y de voeten. Getekend wordt altijd op hele spelpixels.
extends RefCounted

var kaart                  # hol2/kaart.gd
var niveau := 0
var x := 0.0
var y := 0.0
var naar_rechts := true
var snel := 14.0           # spelpixels per seconde lopen
var klim_snel := 12.0
var pad: Array = []        # [{soort: "loop", x} of {soort: "klim", naar, x}]
var klimt := false
var klim_van := 0

func zet(k, n: int, px: float) -> void:
	kaart = k
	niveau = n
	x = px
	y = kaart.voet_y(n)

func loopt() -> bool:
	return not pad.is_empty()

# Het pad naar (doel_niveau, doel_x): per verdieping de dichtstbijzijnde ladder.
func ga_naar(doel_niveau: int, doel_x: float) -> bool:
	var cur := niveau
	var cx := x
	if klimt and not pad.is_empty():
		var huidige: Dictionary = pad[0]   # eerst de ladder af waar hij op staat
		pad.clear()
		pad.append(huidige)
		cur = pad_klim_doel
	else:
		pad.clear()
	doel_x = clampf(doel_x, 4.0, kaart.breed - 4.0)
	while cur != doel_niveau:
		var volg := cur + (1 if doel_niveau > cur else -1)
		var l: Dictionary = kaart.ladder_tussen(cur, volg, cx)
		if l.is_empty():
			return false
		var lx: float = l.x + kaart.LAD_B / 2.0
		pad.append({"soort": "loop", "x": lx})
		pad.append({"soort": "klim", "naar": volg, "x": lx})
		cx = lx
		cur = volg
	pad.append({"soort": "loop", "x": doel_x})
	return true

var pad_klim_doel := 0

# Eén stap verder over het pad. Geeft de soort van wat net klaar is ("", "loop", "klim").
func stap(delta: float) -> String:
	if pad.is_empty():
		return ""
	var p: Dictionary = pad[0]
	if p.soort == "loop":
		var d: float = p.x - x
		if absf(d) > 0.5:
			naar_rechts = d > 0
		var s := snel * delta
		if absf(d) <= s:
			x = p.x
			pad.pop_front()
			return "loop"
		x += signf(d) * s
		return ""
	# klimmen
	if not klimt:
		klimt = true
		klim_van = niveau
		pad_klim_doel = p.naar
		x = p.x
	var doel_y: float = kaart.voet_y(p.naar)
	var s2 := klim_snel * delta
	if absf(doel_y - y) <= s2:
		y = doel_y
		niveau = p.naar
		klimt = false
		pad.pop_front()
		return "klim"
	y += signf(doel_y - y) * s2
	return ""

func stop() -> void:
	if klimt:
		return   # eerst de ladder af
	pad.clear()

func pos() -> Vector2:
	return Vector2(roundf(x), roundf(y))

# Staat hij bij een ladder op zijn niveau? Dan die ladder, anders leeg.
func ladder_hier(naar: int) -> Dictionary:
	for l in kaart.ladders:
		var lx: float = l.x + kaart.LAD_B / 2.0
		if absf(lx - x) <= 6.0 and ((l.boven == niveau and l.onder == naar) or (l.onder == niveau and l.boven == naar)):
			return l
	return {}
