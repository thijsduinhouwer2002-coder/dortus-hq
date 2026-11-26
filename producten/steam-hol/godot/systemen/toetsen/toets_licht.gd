extends SceneTree
# Olaf 25 nov 2026 (issue #97): licht en klein leven in een echt hol.
# - lichtkaart: gras blijft 1, gang donkerder dan aarde ver van licht, bij de fakkel lichter dan ver weg;
# - flakkeren blijft tussen 0,9 en 1,0;
# - lichtplas om de fakkel groot genoeg (Daan #106);
# - leven: elk ding vindt een plek in een gewoon hol, de vleermuis wiegt zacht in en uit;
#   in 10 min spel nooit twee tegelijk, gaten tussen 5 en 15 s, alle vijf soorten komen voor (worm en mot sinds #190).
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
	# Daan #183 M2: soort per plek uit een hash, nooit gelijk aan de buur, geen vast ritme van drie
	# Olaf #210 (Daan #214): de soorten en het metselwerk staan scherp in de wandkunst (hol/metsel.gd), niet in de kaart
	var M = load("res://hol/metsel.gd")
	var buur_gelijk := 0
	var ritme_anders := 0
	var smal := 99.0
	var breed := 0.0
	for i in range(-3, 40):
		if M.plek_soort(i) == M.plek_soort(i + 1):
			buur_gelijk += 1
		if M.plek_soort(i) != M.plek_soort(i + 3):
			ritme_anders += 1
		var w: float = M.plek_begin(i + 1) - M.plek_begin(i)
		smal = minf(smal, w)
		breed = maxf(breed, w)
	ok(buur_gelijk == 0, "nooit twee plekken met dezelfde steen naast elkaar (%d keer)" % buur_gelijk)
	ok(ritme_anders >= 10, "geen vaste volgorde om de drie plekken (%d van 43 anders)" % ritme_anders)
	ok(smal >= 3.4 * M.KOL and breed <= 6.6 * M.KOL and breed - smal > M.KOL, "plekken verschillend breed (%.0f tot %.0f spelpx)" % [smal, breed])
	var soorten := {}
	for nb in range(0, 50):
		soorten[M.blok_soort(nb, 0)] = true
	ok(soorten.size() == 3, "alle drie soorten steen komen voor (%d)" % soorten.size())
	# M2: verschil in tint, niet alleen in licht: koel blauwer dan rood, leem geler (rood en groen boven blauw)
	var tk: Color = M.TINT[1]
	var tl: Color = M.TINT[2]
	ok(tk.b > tk.r + 0.2 and tk.a >= 0.3, "koele steen blauwgrijs (r %.2f, b %.2f, dekking %.2f)" % [tk.r, tk.b, tk.a])
	ok(tl.r > tl.b + 0.4 and tl.g > tl.b + 0.3 and tl.a >= 0.3, "leem oker (r %.2f, g %.2f, b %.2f)" % [tl.r, tl.g, tl.b])
	ok(M.TINT[0].a == 0.0, "gewone steen houdt de wand zoals hij was")
	# M1: een voeg is 1 spelpx en hard (hele spelpixels, donker genoeg); rijen een half blok verschoven
	ok(M.VOEG.a >= 0.5 and M.VOEG.r + M.VOEG.g + M.VOEG.b < 0.3, "voeg donker en dekkend (dekking %.2f)" % M.VOEG.a)
	ok(M.RIJEN.size() == 2 and M.RIJEN[0][0] > 24 and M.RIJEN[1][1] <= 35 and M.RIJEN[1][0] == M.RIJEN[0][1] + 1, "twee rijen blokken op de gangwand (y 24 tot 35), voeg van 1 spelpx ertussen")
	# blokken diep in een plek hebben de soort van die plek; vlak bij de rand mag de buur (in elkaar grijpen)
	var gelijk := true
	var gemengd := 0
	for nb in range(0, 60):
		var m: float = (M.blok_rand(nb, 0) + M.blok_rand(nb + 1, 0)) / 2.0
		var pn: int = M.plek_nr(m)
		var diep: bool = m - M.plek_begin(pn) > M.MENG and M.plek_begin(pn + 1) - m > M.MENG
		if diep and M.blok_soort(nb, 0) != M.plek_soort(pn):
			gelijk = false
		if M.blok_soort(nb, 0) != M.plek_soort(pn):
			gemengd += 1
	ok(gemengd >= 2, "bij de rand van een plek grijpen de soorten in elkaar (%d blokken van 60)" % gemengd)
	ok(gelijk, "soort per heel blok, diep in een plek altijd de soort van die plek")
	var bmin := 99
	var bmax := 0
	for nb in range(-5, 60):
		for rb in 2:
			bmin = mini(bmin, M.blok_breed(nb, rb))
			bmax = maxi(bmax, M.blok_breed(nb, rb))
	ok(bmin >= 10 and bmax <= 22 and bmax - bmin >= 4, "blokken verschillend breed, geen tegelpatroon (%d tot %d spelpx)" % [bmin, bmax])
	# de kaart zelf heeft geen voegen meer (die waren wazig): op één hoogte is de gang overal even donker
	var g0: Color = L.gang_kleur(Vector2(81, 29))
	ok(g0 == L.gang_kleur(Vector2(89, 29)) and g0 == L.gang_kleur(Vector2(300, 29)), "lichtkaart zonder voegen of plekken (die staan scherp in de wandkunst)")
	var vl: Color = L.gang_kleur(Vector2(100.0, 37))
	ok(vl.r / vl.b > 1.15, "vloerstrook warm, niet grijspaars (r/b %.2f)" % (vl.r / vl.b))
	ok(helder(L.gang_kleur(Vector2(100, 39))) < helder(L.gang_kleur(Vector2(100, 29))) - 0.03, "gang donkerder naar de vloer")
	var gc: Color = L.gang_kleur(Vector2(100, 30))
	ok(gc.r / gc.g < 0.62 / 0.59, "minder rood dan de oude gangkleur (r/g %.2f, was %.2f)" % [gc.r / gc.g, 0.62 / 0.59])
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
	# #190: worm en mot terug met de bladen van Mila (Daan #180 ja); kruimels blijven eruit (Daan #106)
	ok("worm" in V.SOORTEN and "mot" in V.SOORTEN and not "kruimels" in V.SOORTEN, "worm en mot terug, kruimels niet (#190)")
	var B = load("res://systemen/leven_beest.gd")
	ok(B.laad() != null, "bladen van worm en mot laden")
	var wk: Array = B.worm_kolommen(hol)
	var HV = load("res://hol/hol_vast.gd")
	var wk_goed := not wk.is_empty()
	for k in wk:
		if HV.vloer_dicht(hol, k) or k <= hol.ingang_kol + 1 or k >= hol.schat_kol - B.TROON:
			wk_goed = false
	ok(wk_goed, "worm alleen op vrije gangtegels, niet bij val, schacht, vloerding of Gloop (%d plekken)" % wk.size())
	var reeks: Array = []
	for i in 42:
		var wf: int = B.worm_stand(i * 0.1, 4.2) / 10
		if reeks.is_empty() or reeks[-1] != wf:
			reeks.append(wf)
	ok(reeks == [1, 0, 2, 0, 3, 0, 1], "worm: piek, op, links, op, rechts, op, piek (%s)" % str(reeks))
	var nieuw := 0
	var vorig := -1
	for i in 420:
		var st: int = B.worm_stand(i * 0.01, 4.2)
		if st != vorig:
			nieuw += 1
			vorig = st
	ok(nieuw <= 16, "worm tekent zuinig: %d nieuwe beelden in 4,2 s" % nieuw)
	var hoog := 99.0
	var mb = B.laad()
	for i in 450:
		var mp: Vector2 = B.mot_plek(L.fakkel_punt(hol), i * 0.01)
		hoog = minf(hoog, mp.y - float(mb.mot["nul_y"][0]))
	ok(hoog >= 24.5, "mot blijft rond de vlam en onder het plafond (bovenkant %.1f, plafond 24, klem op 25)" % hoog)
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
	# #190 CPU: worm en mot komen in de plaats van een ander ding (zelfde gaten van 5 tot 15 s) en tekenen niet vaker
	# (worm ±14 beelden, mot 54 zoals een stofje). Zelfde 30 min met en zonder hun bladen: tekenbeurten van deze laag.
	var tel := {}
	for met in [true, false]:
		var lt = V.maak_in(hol, 11)
		if not met:
			lt.beest = null
		for i in 18000:
			lt._process(0.1)
			vm._process(0.1)
		tel[met] = lt.beurten
		lt.queue_free()
	ok(int(tel[true]) <= int(tel[false]), "met worm en mot niet meer tekenbeurten in 30 min (%d tegen %d zonder)" % [tel[true], tel[false]])
	print("[licht] klaar: FOUT %d" % fout)
	quit(1 if fout > 0 else 0)
