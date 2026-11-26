extends SceneTree
# Olaf 25 nov 2026 (issue #97): licht en klein leven in een echt hol.
# - lichtkaart: gras blijft 1, gang donkerder dan aarde ver van licht, bij de fakkel lichter dan ver weg;
# - flakkeren blijft tussen 0,9 en 1,0;
# - lichtplas om de fakkel groot genoeg (Daan #106);
# - leven: elk ding vindt een plek in een gewoon hol, de vleermuis wiegt zacht in en uit;
#   in 10 min spel nooit twee tegelijk, gaten tussen 5 en 15 s, alle drie soorten komen voor.
# Gebruik: godot --headless --path . -s systemen/toetsen/toets_licht.gd  (0 fouten = groen)

var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[licht] OK " + wat)
	else:
		fout += 1
		print("[licht] FOUT " + wat)

func helder(c: Color) -> float:
	return (c.r + c.g + c.b) / 3.0

func _init() -> void:
	var L = load("res://systemen/licht.gd")
	var G = load("res://systemen/licht_gloed.gd")
	var V = load("res://systemen/leven.gd")
	var hol := Node2D.new()
	hol.set_script(load("res://hol/hol.gd"))
	root.add_child(hol)
	hol.maak(480)
	hol.leg_aan(26)
	var licht = L.maak_in(hol)
	licht._maak_kaart()
	var img: Image = licht.tex.get_image()
	var px := func(x: float, y: float) -> Color:
		return img.get_pixel(int(x / L.STAP), int(y / L.STAP))
	ok(helder(px.call(100, 2)) > 0.99, "gras en lucht blijven ongemoeid (%.2f)" % helder(px.call(100, 2)))
	var f: Vector2 = L.fakkel_punt(hol)
	var ver_gang := Vector2((hol.schat_kol - 5) * 16 + 8, 32)
	ok(f.distance_to(ver_gang) > 40, "meetplek in de gang ver van de fakkel (%.0f)" % f.distance_to(ver_gang))
	var bij: float = helder(px.call(f.x + 6, 30))
	var ver: float = helder(px.call(ver_gang.x, ver_gang.y))
	ok(bij > ver + 0.15, "gang bij de fakkel lichter dan ver weg (%.2f tegen %.2f)" % [bij, ver])
	var aarde: float = helder(px.call(40, 20))
	ok(hol.boven[2] == false, "meetplek aarde is dicht")
	ok(ver < aarde, "gang ver van licht donkerder dan aarde ver van licht (%.2f tegen %.2f)" % [ver, aarde])
	ok(ver > 0.4, "nooit zwart: donkerste gang %.2f (ook op een voeg, Daan #183)" % ver)
	# Sanne 26 nov (Iris 499fd9f mooi 7, "één zalmroze buis"): plekken steen, donkerder naar de vloer, minder rood
	# Daan #183 M2: soort per plek uit een hash, nooit gelijk aan de buur, geen vast ritme van drie, harde voeg ertussen
	var vk := func(x: Color, y: Color) -> float:
		return absf(x.r - y.r) + absf(x.g - y.g) + absf(x.b - y.b)
	var buur_gelijk := 0
	var ritme_anders := 0
	var smal := 99.0
	var breed := 0.0
	for i in range(-3, 40):
		if L.plek_soort(i) == L.plek_soort(i + 1):
			buur_gelijk += 1
		if L.plek_soort(i) != L.plek_soort(i + 3):
			ritme_anders += 1
		var w: float = L.plek_begin(i + 1) - L.plek_begin(i)
		smal = minf(smal, w)
		breed = maxf(breed, w)
	ok(buur_gelijk == 0, "nooit twee plekken met dezelfde steen naast elkaar (%d keer)" % buur_gelijk)
	ok(ritme_anders >= 10, "geen vaste volgorde om de drie plekken (%d van 43 anders)" % ritme_anders)
	ok(smal >= 3.4 * L.KOL and breed <= 6.6 * L.KOL and breed - smal > L.KOL, "plekken verschillend breed (%.0f tot %.0f spelpx)" % [smal, breed])
	var m0: float = (L.plek_begin(4) + L.plek_begin(5)) / 2.0
	var m1: float = (L.plek_begin(5) + L.plek_begin(6)) / 2.0
	ok(vk.call(L.gang_kleur(Vector2(m0, 27)), L.gang_kleur(Vector2(m1, 27))) > 0.08, "twee plekken naast elkaar zie je als andere steen (%.2f)" % vk.call(L.gang_kleur(Vector2(m0, 27)), L.gang_kleur(Vector2(m1, 27))))
	var rand: Color = L.gang_kleur(Vector2(L.plek_begin(5) + 0.3, 27))
	var vlak: Color = L.gang_kleur(Vector2(L.plek_begin(5) + 6.0, 27))
	ok(helder(rand) < helder(vlak) - 0.08, "donkere voeg op de rand van een plek (%.2f tegen %.2f)" % [helder(rand), helder(vlak)])
	var liggend := 0
	for i in range(0, 20):
		var mx: float = (L.plek_begin(i) + L.plek_begin(i + 1)) / 2.0
		for y in [29, 31, 33]:
			if helder(L.gang_kleur(Vector2(mx, y))) < helder(L.gang_kleur(Vector2(mx, 27))) - 0.08:
				liggend += 1
	ok(liggend >= 10, "liggende voegjes in de plekken (%d van 20)" % liggend)
	var vl: Color = L.gang_kleur(Vector2(m0 + 3.0, 37))
	ok(vl.r / vl.b > 1.15, "vloerstrook warm, niet grijspaars (r/b %.2f)" % (vl.r / vl.b))
	ok(L.gang_kleur(Vector2(200, 30)) == L.gang_kleur(Vector2(200, 30)), "plekken liggen vast (geen flikkeren)")
	ok(helder(L.gang_kleur(Vector2(200, 39))) < helder(L.gang_kleur(Vector2(200, 25))) - 0.05, "gang donkerder naar de vloer")
	var rood_meest := 0.0
	for x in range(0, 480, 4):
		var c: Color = L.gang_kleur(Vector2(x, 30))
		rood_meest = maxf(rood_meest, c.r / c.g)
		ok(helder(c) > (0.38 if c != L.gang_kleur(Vector2(L.plek_begin(L.plek_nr(x)) + 6.0, 30)) else 0.45), "steen nooit te donker op x %d (%.2f; een voeg mag tot 0,38)" % [x, helder(c)]) if x % 80 == 0 else null
	ok(rood_meest < 0.62 / 0.59, "minder rood dan de oude gangkleur (r/g hooguit %.2f, was %.2f)" % [rood_meest, 0.62 / 0.59])
	var lo := 9.0
	var hi := 0.0
	for i in 2000:
		var v: float = G.flakker(i * 0.037, i % 3)
		lo = minf(lo, v)
		hi = maxf(hi, v)
	ok(lo >= 0.9 - 0.001 and hi <= 1.0 + 0.001, "flakkeren tussen 0,9 en 1,0 (%.3f tot %.3f)" % [lo, hi])
	var kaart: int = licht.keer
	licht._process(1.0)
	licht._process(1.0)
	ok(licht.keer == kaart + 1, "kaart niet opnieuw zonder verandering (%d keer)" % licht.keer)

	# Daan #106 moet 3: de plas om de fakkel is groot en fel genoeg (2 tegels, dekking 0,4 tegen 0,2 eerst)
	ok(G.FAKKEL_R >= 30.0 and G.KLEUR_FAKKEL.a >= 0.35, "lichtplas om de fakkel: straal %.0f, dekking %.2f" % [G.FAKKEL_R, G.KLEUR_FAKKEL.a])
	# vleermuis in het hol (zelfde als hol_lagen.gd), zodat hij kan wiegen
	var wz := Node2D.new()
	var vm := Node2D.new()
	vm.set_script(load("res://systemen/vleermuis.gd"))
	vm.name = "Vleermuis"
	hol.add_child(vm)
	hol.add_child(wz)
	vm.zet(hol, wz)
	ok(vm.vm.size() >= 1, "vleermuis hangt in het hol (%d)" % vm.vm.size())
	for s in V.SOORTEN:
		ok(V.kies_plek(hol, s) != null, "plek voor %s in een gewoon hol" % s)
	ok(not ("worm" in V.SOORTEN or "mot" in V.SOORTEN or "kruimels" in V.SOORTEN), "worm, mot en kruimels zijn eruit (Daan #106)")
	var VM = load("res://systemen/vleermuis.gd")
	var hk := 0.0
	for i in 300:
		hk = maxf(hk, absf(VM.wieg_hoek(i * 0.01)))
	ok(hk <= VM.WIEG_HOEK + 0.001 and hk > 0.1 and VM.wieg_hoek(0.0) == 0.0 and VM.wieg_hoek(VM.WIEG_S) == 0.0,
			"vleermuis wiegt zacht in en uit (grootste hoek %.2f)" % hk)

	var lv = V.maak_in(hol, 3)
	var gaten: Array = []
	var stil := 0.0
	var was := ""
	for i in 6000:   # 10 min op 10 beelden per s
		lv._process(0.1)
		vm._process(0.1)
		if lv.soort == "":
			stil += 0.1
		elif was == "":
			if i > 1:
				gaten.append(stil)
			stil = 0.0
		was = lv.soort
	var lo_g := 99.0
	var hi_g := 0.0
	for g in gaten:
		lo_g = minf(lo_g, g)
		hi_g = maxf(hi_g, g)
	ok(gaten.size() >= 25, "in 10 min %d kleine dingen" % (gaten.size() + 1))
	ok(lo_g >= 4.9 and hi_g <= 15.2, "gaten tussen 5 en 15 s (%.1f tot %.1f)" % [lo_g, hi_g])
	for s in V.SOORTEN:
		ok(int(lv.gedaan.get(s, 0)) >= 3, "%s kwam %d keer" % [s, int(lv.gedaan.get(s, 0))])
	print("[licht] klaar: FOUT %d" % fout)
	quit(1 if fout > 0 else 0)
