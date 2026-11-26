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
				if hx >= x0 and hx < x1:
					d.draw_rect(Rect2(hx, hy, 1, 1), VOEG)

# soort van blok n in rij r: de soort van de plek waar het midden van het blok in ligt, met een vaste schuif van
# -MENG tot +MENG spelpx, zodat blokken vlak bij de rand van een plek soms de soort van de buur hebben en de soorten
# in elkaar grijpen (tweede blinde lezer: "de kleur verspringt zonder reden").
const MENG := 12
static func blok_soort(n: int, r: int) -> int:
	var m := (blok_rand(n, r) + blok_rand(n + 1, r)) / 2.0
	return plek_soort(plek_nr(m + _hash(n * 13 + r * 517, 9) % (2 * MENG + 1) - MENG))

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
