extends RefCounted
# De achterwand van de gegraven cellen, uit hol_vast.gd gehaald (Olaf 26 nov, #210: hol_vast.gd was 835 regels).
# hol_vast.grond() roept achterwand(self, d, schat_3d) aan; hv is dat hol_vast-knooppunt (voor h, kamer_dingen, berg_links).
# Sinds #210 (Daan #214) komt hier ook het metselwerk van de gangwand (hol/metsel.gd): in de wandkunst zelf, scherp op
# spelpixels, ná de koele wand en vóór stenen in de wand, stutten en vloerdingen, dus nooit een voeg over decor.

const KOL := 16
const OPP := 8
const GANG_BOVEN := 24
const HOL3D := preload("res://hol/hol_3d.gd")
const METSEL := preload("res://hol/metsel.gd")
const KAMERWAND := preload("res://hol/kamerwand.gd")   # #252: korrel en harde rand op de buis van de bovenste gang
const GROND_VOCHT_KLEUR := Color(0.14, 0.06, 0.05)   # zelfde als in hol_vast.gd

# De lagen ook in de achterwand van wat je graaft (Mila 26 nov, issue 146; Iris: "mooi, maar weg na het graven"). Na
# 10 min is bijna de hele strook gang en kamer, en die stukken hadden één egale zalmroze wand. Nu is elke gegraven cel
# een snee door dezelfde lagen als de grond eromheen: de bovenste rij (kamer, vlak onder het gras) houdt de warme
# vochtige laag met dunne wortels uit het plafond; de onderste rij (gang) is koel zoals de diepe aarde, met hier en
# daar een steen half in de wand. Alles in het vaste beeld (hol_vast), dus alleen opnieuw getekend bij graven of een
# put: geen extra werk per beeld.
# Nakeuring Daan #153 (26 nov): M1 wortels lazen als stekels en hingen ook in de onderste gang (daar zit geen gras
# boven), dus nu dun, kronkelig, beige en alleen in de kamer; M2 stenen stonden op een rij op de vloer, nu minder, elk
# een andere maat en hoogte, in de wand en donkerder; M3 het verloop zag je niet, nu net zo sterk als in de grond.
# Wand van de 3D-stukken (gemeten in hol_proef.png): gang van GANG_BOVEN tot +11, daaronder de vloer; kamer van
# OPP + 4 tot OPP + 12. Stenen en wortels uit versiering.py (wand_steen, om en om gespiegeld, en wand_wortels); in een
# oud blad zonder die stukken de gewone steen en wortels kleiner.
const WAND_GANG := [GANG_BOVEN, GANG_BOVEN + 11]
const WAND_KAMER := [OPP + 4, OPP + 12]
const WAND_VOCHT_KAMER := [0.46, 0.42, 0.32, 0.22, 0.13, 0.06]   # warme vochtige laag onder het plafond, als GROND_VOCHT
const WAND_NAAD_GANG := [0.30, 0.14]          # dunne donkere naad bovenin de gang, als de naad in de diepe rij
const WAND_KOEL := Color(0.22, 0.25, 0.42)    # zelfde koel als GROND_KOEL in de diepe aarde
const WAND_KOEL_BASIS := 0.20                 # de hele gangwand, net als de diepe rij aarde
const WAND_KOEL_ONDER := 0.22                 # daar bovenop oplopend naar de vloer
const WAND_DING_KLEUR := Color(0.92, 0.89, 0.87)   # stenen donkerder, zodat ze in de wand zitten en geen los puin zijn

# Wat in de wand van de gegraven cellen komt: [naam, punt, hangend, schaal, gespiegeld]. Zelfde aanpak als grond_dingen: elk soort
# kiest zelf de afstand tot de volgende plek (hash per kolom), zodat er geen ritme in zit.
static func wand_dingen(hv, h, schat_3d: bool) -> Array:
	var uit := []
	var steen_vrij: int = 1 + h._hash(3, 81) % 4
	var wortel_vrij: int = h._hash(4, 82) % 3
	var bl: float = hv.berg_links(h)
	var kamer_bezet := {}
	for kd in hv.kamer_dingen(h, schat_3d):
		var kk: int = int(kd[1].x) / KOL
		for j in [kk - 1, kk, kk + 1]:
			kamer_bezet[j] = true
	for k in h.kolommen:
		if k <= h.ingang_kol + 1 or k * KOL + KOL > bl:
			continue
		var stuk: String = HOL3D.stuk(h, 1, k, schat_3d)
		if stuk == "gang" and not h.vallen.has(k) and k >= steen_vrij and k > h.ingang_kol + 2 \
				and not h.vallen.has(k - 1) and not h.vallen.has(k + 1):
			# stenen alleen in de koele gang (niet achter de gangfakkel vlak na de schacht): ver uit elkaar, elk een andere maat, en met de voet 1 tot 5 spelpixels
			# boven de vloer, dus in de wand en niet erop
			steen_vrij = k + 3 + h._hash(k, 83) % 5
			if h._hash(k, 84) % 4 != 0:
				var maat: float = 0.8 + 0.09 * float(h._hash(k, 85) % 5)
				var y: int = WAND_GANG[1] - 1 - h._hash(k, 86) % 5
				uit.append(["wand_steen", Vector2(k * KOL + 2 + h._hash(k, 87) % 12, y), false, maat, h._hash(k, 88) % 2 == 1])
		var boven: String = HOL3D.stuk(h, 0, k, schat_3d)
		if boven == "kamer_midden_c" and not kamer_bezet.has(k) and k >= wortel_vrij:
			# wortels alleen in de kamer, daar zit het gras recht boven; alleen in het kale middenstuk, want in a hangt
			# de stut en in b staan houweel en ton (fakkel en kistje staan in begin en eind)
			wortel_vrij = k + 2 + h._hash(k, 94) % 4
			if h._hash(k, 91) % 4 != 0:
				var lang: float = 0.8 + 0.1 * float(h._hash(k, 92) % 4)
				uit.append(["wand_wortels", Vector2(k * KOL + 2 + h._hash(k, 95) % 12, WAND_KAMER[0] - 1), true, lang, h._hash(k, 96) % 2 == 1])
	return uit

static func achterwand(hv, d: CanvasItem, schat_3d: bool) -> void:
	var h = hv.h
	for k in h.kolommen:
		if k == h.ingang_kol:
			continue
		# ook boven een put (Sanne 26 nov, Daan #183 M1): hol.gd tekent de put met licht nu pas vanaf de stekelpunten,
		# dus zonder de koele wand stond de putkolom als lichtere rechthoek in de gang
		if HOL3D.stuk(h, 1, k, schat_3d) == "gang" and (not h.vallen.has(k) or hv._licht(h)):
			_wand_koel(d, k * KOL, KOL, WAND_GANG)
			METSEL.teken(d, k)   # #210: scherpe voegen en tint per soort, vóór stenen en decor
		var boven: String = HOL3D.stuk(h, 0, k, schat_3d)
		if boven.begins_with("kamer") and boven != "kamer_los":
			# op de ronde einden lopen de banden zacht uit naar de rand (een rechte rand gaf een harde hoek)
			var links: bool = boven in ["kamer_begin", "kamer_links"]
			var rechts: bool = boven in ["kamer_eind", "kamer_rechts"]
			if links or rechts:
				for x in KOL:
					var f: float = clampf((x - 5.0) / 9.0 if links else (10.0 - x) / 9.0, 0.0, 1.0)
					if f > 0.0:
						_wand_vocht(d, k * KOL + x, 1, WAND_KAMER, f)
			else:
				_wand_vocht(d, k * KOL, KOL, WAND_KAMER)
			KAMERWAND.teken(d, k, boven)   # #252: alleen op kale buiswand (masker), vóór wortels en kamer_dingen
	for ding in wand_dingen(hv, h, schat_3d):
		var naam: String = ding[0]
		var schaal: float = ding[3]
		var kleur := WAND_DING_KLEUR
		if HOL3D.deco_maat(naam) == Vector2.ZERO:
			# oud blad: de grond-dingen kleiner
			naam = "wortels_a" if naam == "wand_wortels" else "steen_diep"
			schaal *= 0.5 if naam == "wortels_a" else 0.62
		if naam == "wand_wortels" or naam == "wortels_a":
			kleur = Color.WHITE
		var punt: Vector2 = ding[1]
		if ding[4]:
			d.draw_set_transform(Vector2(2.0 * punt.x, 0.0), 0.0, Vector2(-1.0, 1.0))   # gespiegeld om het ankerpunt
		HOL3D.teken_deco_op(d, naam, punt, ding[2], schaal, kleur)
		if ding[4]:
			d.draw_set_transform(Vector2.ZERO)

# bovenste rij: de warme vochtige laag onder het gras loopt door in de achterwand
# Mila 28 nov (Iris #334 punt 1): vanaf schaal 4 een glad verloop op schermpixels in plaats van 6 treden van een
# spelpx (op schaal 5 banden van 5 schermpx); zelfde sterkte per rij in het midden van elke spelpx.
static func _wand_vocht(d: CanvasItem, x: float, b: float, wand: Array, f: float = 1.0) -> void:
	var s: float = d.scale.x if d is Node2D else 1.0
	var n := WAND_VOCHT_KAMER.size()
	if s < 4.0:
		for i in n:
			var c := GROND_VOCHT_KLEUR
			c.a = WAND_VOCHT_KAMER[i] * f
			d.draw_rect(Rect2(x, wand[0] + i, b, 1), c)
		return
	var stappen := int(roundf(s)) * n
	for j in stappen:
		var t := (float(j) + 0.5) / roundf(s) - 0.5     # plek in spelpx, 0 = midden van de eerste rij
		var i0 := clampi(int(floor(t)), 0, n - 1)
		var i1 := clampi(i0 + 1, 0, n - 1)
		var w := clampf(t - floor(t), 0.0, 1.0) if t >= 0.0 else 0.0
		var a: float = lerpf(WAND_VOCHT_KAMER[i0], WAND_VOCHT_KAMER[i1], w) if i1 != i0 else WAND_VOCHT_KAMER[i0] * (1.0 - clampf(t - float(n - 1), 0.0, 1.0))
		var c := GROND_VOCHT_KLEUR
		c.a = a * f
		d.draw_rect(Rect2(x, wand[0] + float(j) / roundf(s), b, 1.0 / roundf(s)), c)

# onderste rij: koel zoals de diepe aarde, met een donkere naad bovenin en nog koeler naar de vloer
static func _wand_koel(d: CanvasItem, x: float, b: float, wand: Array) -> void:
	var top: int = wand[0]
	var bodem: int = wand[1]
	var basis := WAND_KOEL
	basis.a = WAND_KOEL_BASIS
	d.draw_rect(Rect2(x, top, b, bodem - top), basis)
	for i in WAND_NAAD_GANG.size():
		var c := GROND_VOCHT_KLEUR
		c.a = WAND_NAAD_GANG[i]
		d.draw_rect(Rect2(x, top + i, b, 1), c)
	var midden: int = (top + bodem) / 2
	for y in range(midden, bodem):
		var c := WAND_KOEL
		c.a = WAND_KOEL_ONDER * float(y - midden + 1) / float(bodem - midden)
		d.draw_rect(Rect2(x, y, b, 1), c)
