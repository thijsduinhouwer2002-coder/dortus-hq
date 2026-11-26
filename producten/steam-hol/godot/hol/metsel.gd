extends RefCounted
# Metselwerk op de gangwand (Olaf 26 nov, #210, Daan #214 nee 7). Versie 3 zat in de lichtkaart (1 texel per 2 x 2
# spelpixels, lineair uitgerekt), dus de voegen waren wazig en lazen als zachte panelen (M1); de soorten verschilden
# alleen in helderheid (M2); en de voegen liepen over stut, houweel en ton (M3). Nu:
# - tekent achterwand.gd dit in het vaste beeld zelf, op hele spelpixels met nearest: een voeg is 1 spelpx breed en hard;
# - ná de koele wand en vóór stenen in de wand, stutten, spinrag en vloerdingen, en alleen op de gangwand (de kamers
#   hebben stut, houweel en ton in hun tegel), dus nooit een voeg over decor;
# - heeft elke soort een eigen tint: koel blauwgrijs, gewoon zoals de wand, leem oker. De lichtkaart maakt het daarna
#   donker of licht zoals de rest, dus het kost alleen iets als het vaste beeld opnieuw getekend wordt.
# Bekeken: hoe Rusty's Retirement en Spirit City (lat van Hats) een wand op 1x tekenen: harde voeg van 1 pixel, lichte
# bovenkant en donkere onderkant per blok, kleurverschil per steen in tint en niet alleen in licht.

const KOL := 16
const PLEK_KOL := 5.0         # zo veel tegels per plek steen (gemiddeld; elke rand schuift vast -0,75 tot +0,75 tegel)
const BLOK_B := 16            # blok in spelpx; de tweede rij een half blok verschoven
# rijen op de gangwand (wand van GANG_BOVEN 24 tot 35, daaronder de vloer): [boven, onder) in spelpx, voeg op boven - 1
const RIJEN := [[25, 30], [31, 35]]
const VOEG := Color(0.07, 0.04, 0.05, 0.62)
const BOVENKANT := Color(1.0, 0.93, 0.80, 0.16)    # bovenste rij van elk blok: licht valt erop
const ONDERKANT := Color(0.0, 0.0, 0.0, 0.16)      # onderste rij: schaduw, het blok steekt iets uit
# tint per soort over de wand (0 gewoon, 1 koel, 2 leem); gewoon houdt de wand zoals hij was
const TINT := [Color(0.0, 0.0, 0.0, 0.0), Color(0.30, 0.42, 0.62, 0.42), Color(0.92, 0.70, 0.30, 0.40)]
const VERSCHIL := 0.10        # elk blok tot zo veel donkerder (vast per blok), zodat het geen behang wordt

# Na de eerste blinde lezer ("plat tegelpatroon, geen diepte of slijtage, goedkoop behang"): blokken 13 tot 19 spelpx
# breed (vast per blok), schaduw onder en rechts, licht boven, en op ±1 op 3 blokken een afgebrokkelde hoek.
const ZIJKANT := Color(0.0, 0.0, 0.0, 0.10)        # rechterkolom van elk blok: zijkant in de schaduw
const SCHUIF_MAX := 3         # elke blokrand schuift vast -3 tot +3 spelpx

# linkerrand (spelpx) van blok n in rij r: om de BLOK_B, de tweede rij een half blok verschoven, met een vaste schuif
static func blok_rand(n: int, r: int) -> int:
	return (BLOK_B / 2) * r + n * BLOK_B + _hash(n * 7 + r * 1013, 5) % (2 * SCHUIF_MAX + 1) - SCHUIF_MAX

# tekent het metselwerk op gangkolom k (alleen binnen die kolom; blokken lopen door over de kolomrand)
static func teken(d: CanvasItem, k: int) -> void:
	var x0 := k * KOL
	var x1 := x0 + KOL
	for r in RIJEN.size():
		var y0: int = RIJEN[r][0]
		var y1: int = RIJEN[r][1]
		if r > 0:
			d.draw_rect(Rect2(x0, y0 - 1, KOL, 1), VOEG)
		var n: int = int(floor(float(x0 - (BLOK_B / 2) * r) / BLOK_B)) - 1
		while blok_rand(n, r) < x1:
			var bl: int = blok_rand(n, r)
			var br: int = blok_rand(n + 1, r)
			n += 1
			if br <= x0:
				continue
			var a := maxi(bl, x0)
			var b := mini(br, x1)
			if r == 0:
				_bovenvoeg(d, n - 1, bl, br, y0, x0, x1)
			var t: Color = TINT[blok_soort(n - 1, r)]
			if t.a > 0.0:
				d.draw_rect(Rect2(a, y0, b - a, y1 - y0), t)
			var hb := _hash(n * 31 + r, 7)
			d.draw_rect(Rect2(a, y0, b - a, y1 - y0), Color(0, 0, 0, VERSCHIL * float(hb % 1000) / 1000.0))
			d.draw_rect(Rect2(a, y0, b - a, 1), BOVENKANT)
			d.draw_rect(Rect2(a, y1 - 1, b - a, 1), ONDERKANT)
			if br - 1 < x1:
				d.draw_rect(Rect2(br - 1, y0 + 1, 1, y1 - y0 - 1), ZIJKANT)
			if bl >= x0:
				d.draw_rect(Rect2(bl, y0, 1, y1 - y0), VOEG)
			# afgebrokkelde hoek: één spelpx in de kleur van de voeg, linksboven of rechtsonder
			if hb % 3 == 0:
				var hx: int = bl + 1 if hb % 2 == 0 else br - 1
				var hy: int = y0 if hb % 2 == 0 else y1 - 1
				_pix(d, hx, hy, 1, 1, VOEG, x0, x1)
			_binnen(d, n - 1, r, bl, br, y0, y1, x0, x1)
			if r == 0:
				_bovenrand(d, n - 1, bl, br, y0, x0, x1)

# Daan #224 K3: de blokken waren binnenin egaal (tegel). Per blok één of twee lichte vlekjes van 1 spelpx en op ±1 op
# 4 blokken een barstje van 2 tot 3 spelpx schuin naar beneden, binnen de rand van het blok, alles vast per blok.
const VLEK := Color(1.0, 0.95, 0.85, 0.20)
const BARST := Color(0.07, 0.04, 0.05, 0.45)
static func _binnen(d: CanvasItem, n: int, r: int, bl: int, br: int, y0: int, y1: int, x0: int, x1: int) -> void:
	var b := br - bl
	var h := y1 - y0
	if b < 6 or h < 4:
		return
	var hv := _hash(n * 41 + r * 331, 11)
	var vlekken: int = 1 + hv % 2
	for i in vlekken:
		var hx := _hash(n * 17 + r * 97 + i, 12)
		_pix(d, bl + 2 + hx % (b - 4), y0 + 1 + (hx / 7) % (h - 2), 1, 1, VLEK, x0, x1)
	if hv % 4 == 1:
		var bx: int = bl + 2 + (hv / 5) % (b - 5)
		var lang: int = 2 + (hv / 3) % 2
		var naar_rechts: bool = (hv / 11) % 2 == 0
		for j in lang:
			_pix(d, bx + (j if naar_rechts else -j), y0 + 1 + j, 1, 1, BARST, x0, x1)

# Daan #224 K1: de bovenkant van de muur was een rechte harde lijn tegen de aarde. Nu heeft ±1 op 3 blokken in de
# bovenste rij een afgebrokkelde bovenkant (een hap van 3 tot 6 spelpx breed, 1 tot 2 diep, in de kleur van de voeg)
# en ±1 op 5 steekt iets uit: zijn lichte bovenkant komt 1 spelpx hoger, over de bovenste voeg.
const BOVEN_HAP_KANS := 3
const BOVEN_UIT_KANS := 5
static func _bovenrand(d: CanvasItem, n: int, bl: int, br: int, y0: int, x0: int, x1: int) -> void:
	var b := br - bl
	var hb := _hash(n * 59, 13)
	if hb % BOVEN_HAP_KANS == 0 and b >= 8:
		var w: int = 3 + (hb / 3) % 4
		var hx: int = bl + 1 + (hb / 13) % (b - w - 1)
		var diep: int = 1 + (hb / 7) % 2
		_pix(d, hx, y0, w, diep, VOEG, x0, x1)
		if diep == 2:
			_pix(d, hx - 1, y0, 1, 1, VOEG, x0, x1)   # hap loopt schuin uit, geen rechte bak

# bovenste voeg boven blok n: gewoon een voeg, behalve bij een blok dat uitsteekt; daar komt zijn lichte bovenkant
# 1 spelpx hoger in plaats van de voeg (alleen tussen zijn randen, de voeg ernaast blijft)
static func uitsteker(n: int, b: int) -> bool:
	var hb := _hash(n * 59, 13)
	return hb % BOVEN_HAP_KANS != 0 and hb % BOVEN_UIT_KANS == 1 and b >= 6
static func _bovenvoeg(d: CanvasItem, n: int, bl: int, br: int, y0: int, x0: int, x1: int) -> void:
	if uitsteker(n, br - bl):
		_pix(d, bl, y0 - 1, 1, 1, VOEG, x0, x1)
		_pix(d, br - 1, y0 - 1, 1, 1, VOEG, x0, x1)
		_pix(d, bl + 1, y0 - 1, br - bl - 2, 1, BOVENKANT, x0, x1)
	else:
		_pix(d, bl, y0 - 1, br - bl, 1, VOEG, x0, x1)

# rechthoek, afgeknipt op de gangkolom [x0, x1)
static func _pix(d: CanvasItem, x: int, y: int, w: int, h: int, c: Color, x0: int, x1: int) -> void:
	var a := maxi(x, x0)
	var b := mini(x + w, x1)
	if b > a:
		d.draw_rect(Rect2(a, y, b - a, h), c)

# soort van blok n in rij r. Diep in een plek de soort van die plek. Bij elke rand grijpen de soorten in elkaar als
# tanden (Daan #224 K2: met een willekeurige schuif van 12 spelpx wisselden de soorten nog vaak recht op een staande
# voeg, bij 11 van 60 randen helemaal schoon): in de ene rij steekt het eerste blok over de rand in de soort van links,
# in de andere rij het laatste blok vóór de rand in de soort van rechts; welke rij welke kant op gaat, kiest de rand
# zelf. Op ±1 op 3 randen gaat ook het tweede blok mee, zodat het geen vast ritme wordt. Alles binnen MENG spelpx.
const MENG := 24
static func blok_soort(n: int, r: int) -> int:
	var m := _midden(n, r)
	var pn := plek_nr(m)
	var gl := plek_begin(pn)
	var gr := plek_begin(pn + 1)
	if m - gl < MENG:
		var kant := _hash(pn, 3) % 2
		var stap: int = 1 if _midden(n - 1, r) < gl else (2 if _midden(n - 2, r) < gl and _hash(pn, 4) % 3 == 0 else 0)
		if stap > 0 and r == kant:
			return plek_soort(pn - 1)
	if gr - m < MENG:
		var kant := _hash(pn + 1, 3) % 2
		var stap: int = 1 if _midden(n + 1, r) >= gr else (2 if _midden(n + 2, r) >= gr and _hash(pn + 1, 4) % 3 == 0 else 0)
		if stap > 0 and r != kant:
			return plek_soort(pn + 1)
	return plek_soort(pn)

static func _midden(n: int, r: int) -> float:
	return (blok_rand(n, r) + blok_rand(n + 1, r)) / 2.0

# breedte van blok n in rij r (toets)
static func blok_breed(n: int, r: int) -> int:
	return blok_rand(n + 1, r) - blok_rand(n, r)

# nummer van de plek steen waar x (spelpixels) in ligt
static func plek_nr(x: float) -> int:
	var i := int(floor(x / (KOL * PLEK_KOL)))
	if x < plek_begin(i):
		return i - 1
	if x >= plek_begin(i + 1):
		return i + 1
	return i

# linkerrand van plek i in spelpixels: om de PLEK_KOL tegels, met een vaste schuif van -0,75 tot +0,75 tegel
static func plek_begin(i: int) -> float:
	return (i * PLEK_KOL + (_hash(i, 1) % 1000) / 1000.0 * 1.5 - 0.75) * KOL

# 0 gewoon, 1 koele steen, 2 leem. Even plekken uit de hash; een oneven plek kiest uit wat zijn twee buren niet zijn,
# dus nooit twee keer dezelfde soort naast elkaar en geen vast ritme (Daan #183 M2).
static func plek_soort(i: int) -> int:
	if posmod(i, 2) == 0:
		return _hash(i, 0) % 3
	var l := _hash(i - 1, 0) % 3
	var r := _hash(i + 1, 0) % 3
	var vrij: Array = []
	for s in 3:
		if s != l and s != r:
			vrij.append(s)
	return vrij[_hash(i, 2) % vrij.size()]

static func _hash(i: int, zout: int) -> int:
	var v := (i * 73856093) ^ (zout * 19349663) ^ 83492791
	v = (v ^ (v >> 13)) * 1274126177
	return absi(v ^ (v >> 16)) % 100000
