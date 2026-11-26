extends SceneTree
# Toetsen voor kroniek en voortgang (Bram). Draaien: godot --headless --path <map met project.godot> -s systemen/toetsen/toets_systemen.gd
var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[hol-toets] OK ", wat)
	else:
		fout += 1
		print("[hol-toets] FOUT ", wat)

func _init() -> void:
	var K = load("res://systemen/kroniek.gd")
	var V = load("res://systemen/voortgang.gd")
	var k = K.new()
	var i1: Dictionary = k.binnen("Bram")
	ok(i1["bezoeken"] == 0 and i1["wrok"] == "", "eerste bezoek zonder wrok")
	ok(k.laatste_soort.begins_with("binnen") and k.laatste().contains("Bram"), "regel binnenkomst: " + k.laatste())
	k.gevlucht("Bram", "the Spike Pit")
	ok(k.volle_naam("Bram") == "Bram the Spooked", "bijnaam na 1 keer vluchten: " + k.volle_naam("Bram"))
	var i2: Dictionary = k.binnen("Bram")
	ok(i2["bezoeken"] == 1 and i2["wrok"] == "the Spike Pit" and i2["littekens"] == 1, "terug met wrok en litteken")
	ok(k.laatste_soort == "terug" and k.laatste().contains("Bram"), "regel terugkomst: " + k.laatste())
	k.gevlucht("Bram", "Gloop the Slime")
	k.binnen("Bram")
	k.gevlucht("Bram", "")
	ok(k.volle_naam("Bram") == "Bram the Thrice-Fled", "drie keer gevlucht: " + k.volle_naam("Bram"))
	ok(k.held("Bram")["wrok"] == "Gloop the Slime", "wrok blijft bij vluchten zonder raak")
	k.binnen("Bram")
	k.gevallen("Bram", "Gloop the Slime", 7)
	ok(k.laatste_soort == "afgerekend_aarts" and k.laatste().ends_with(" +7") and not k.laatste().contains("wall"),
		"aartsvijand vereffend, eigen lijst (Sanne 21:50): " + k.laatste())
	k.binnen("Wim")
	k.gevlucht("Wim", "Gloop the Slime")
	k.binnen("Wim")
	k.gevallen("Wim", "Gloop the Slime", 5)
	ok(k.laatste_soort == "afgerekend_bewoner" and k.laatste().ends_with(" +5") and not k.laatste().contains("wall")
		and not k.laatste().contains("Nemesis"), "wrok vereffend, gewone held zonder wand of Nemesis: " + k.laatste())
	# regels van Sanne: hooguit 42 tekens, goud in dezelfde regel, niet twee keer dezelfde achter elkaar
	var k3 = K.new()
	var te_lang := 0
	var dubbel := 0
	var vorige := ""
	for z in 300:
		var nm: String = ["Kees", "Gerda", "Joost", "Fenna", "Lotte"][z % 5]
		k3.binnen(nm, "hebzuchtig" if z % 2 == 0 else "schijterig")
		var r_: String = k3.laatste()
		if z % 3 == 0:
			r_ = k3.gevlucht(nm, "Gloop the Slime")
		elif z % 3 == 1:
			r_ = k3.gevallen(nm, "the Spike Pit", 15)
		else:
			r_ = k3.schat(nm)
		for regel in k3.regels.slice(-2):
			if regel.length() > 42:
				te_lang += 1
		if r_ == vorige:
			dubbel += 1
		vorige = r_
	ok(te_lang == 0, "alle kroniekregels hooguit 42 tekens (%d te lang)" % te_lang)
	ok(dubbel == 0, "niet twee keer dezelfde regel achter elkaar")
	var k4 = K.new()
	k4.binnen("Kees")
	ok(k4.gevallen("Kees", "the Spike Pit", 7).ends_with(" +7") and not k4.laatste().contains("Gloop"), "val en goud in één regel, geen bewonersregel bij de put: " + k4.laatste())
	ok(k4.vrije_naam("Kees") == "Kees II", "gevallen naam komt terug als Kees II")
	k4.binnen("Kees II")
	ok(k4.laatste_soort == "naamgenoot" and k4.laatste().begins_with("Kees II"), "naamgenoot-regel: " + k4.laatste())
	k4.gevallen("Kees II", "Gloop the Slime", 6)
	k4.binnen("Kees III")
	k4.gevallen("Kees III", "Gloop the Slime", 6)
	ok(k4.vrije_naam("Kees") == "", "na Kees III een andere naam")
	k4.binnen("Mara")
	ok(k4.schat("Mara") != "" and k4.held("Mara")["hoard_toucher"] and k4.laatste_soort == "schat", "schat aangeraakt: Hoard-Toucher-regel: " + k4.laatste())
	ok(k4.volle_naam("Mara") == "Mara the Hoard-Toucher", "bijnaam na de schat: " + k4.volle_naam("Mara"))
	ok(k4.pensioen("Mara").begins_with("Mara") and k4.held("Mara")["pensioen"], "pensioen-regel: " + k4.laatste())
	ok(k4.gevallen("Odo", "Gloop the Slime", 6).find("Gloop the Slime") < 0, "bewoner kort als Gloop, nooit Gloop the Slime")
	var k2 = K.new()
	k2.van_dict(JSON.parse_string(JSON.stringify(k.naar_dict())))
	ok(k2.volle_naam("Bram") == "Bram the Thrice-Fled" and k2.laatste() == k.laatste(), "kroniek opslaan en laden via JSON")

	var t0 := 1_800_000_000
	var r: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42)
	ok(r["helden"] == 14 and r["goud"] >= r["helden"], "een uur weg op weg-snelheid 0,12: 14 helden (HELD_ELKE_S 30, Sanne 16 nov 22:00), goud >= helden (%s)" % r["regel"])
	ok(r["faam"] == r["gevallen"], "faam weg = gevangen helden")
	var acht: Dictionary = V.reken(t0, t0 + 8 * 3600, 1, 1, 42)
	# Sanne 16 nov 22:00 (balans.md): weg op 0,12, een nacht is ±een uur spelen en blijft onder de winkel (1048),
	# ook met de volle graafbonus (+3 per val). De oude grens van anderhalve winkel (1572) vervalt.
	ok(acht["helden"] == 115 and acht["goud"] < 1048, "8 uur weg: 115 helden, minder goud dan de winkel (%d)" % acht["goud"])
	var acht_gb: Dictionary = V.reken(t0, t0 + 8 * 3600, 1, 1, 42, 6, 0, null, 41)
	ok(int(acht_gb["goud"]) < 1048, "8 uur weg met graafbonus +3: minder goud dan de winkel (%d)" % int(acht_gb["goud"]))
	# faam uit één keer weg: hooguit 2 hol-niveaus (Sanne 16 nov 22:00)
	var HNw = load("res://systemen/hol_niveau.gd")
	ok(HNw.niveau(HNw.weg_faam(0, int(acht["faam"]))) <= 3 and HNw.weg_faam(0, 74) == 5, "8 uur weg vanaf 0: hooguit hol 3 (faam %d van %d)" % [HNw.weg_faam(0, int(acht["faam"])), int(acht["faam"])])
	ok(HNw.niveau(17 + HNw.weg_faam(17, 74)) == 8 and HNw.weg_faam(17, 3) == 3 and HNw.weg_faam(5, 0) == 0, "vanaf hol 6: hooguit hol 8; weinig faam blijft heel")
	ok(V.tempo_regel(acht) == "" and V.TEMPO_REGEL.length() <= 42, "regel kwart snelheid uit (moet Daan 17:45), tekst blijft kort")
	ok(V.tempo_regel(V.reken(t0, t0 + 600, 1, 1, 42)) == "", "geen regel kwart snelheid na 10 min weg")
	# hol-niveau (Sanne voortgang.md spoor 1, drempels Bram): faam = gevangen helden
	var HN = load("res://systemen/hol_niveau.gd")
	ok(HN.niveau(0) == 1 and HN.niveau(2) == 1 and HN.niveau(3) == 2 and HN.niveau(12) == 5 and HN.niveau(88) == 12, "hol-niveau op de drempels")
	ok(HN.niveau(100000) == 12 and HN.nog(100000) == 0, "demo stopt op hol-niveau 12")
	ok(HN.hover(0) == "Level 1: a damp hole. 3 heroes to go.", "hover niveau 1: " + HN.hover(0))
	ok(HN.hover(11) == "Level 4: a bad idea. 1 hero to go.", "hover enkelvoud: " + HN.hover(11))
	ok(HN.erbij(2, 12) == [2, 3, 4, 5] and HN.erbij(5, 5).is_empty(), "niveaus erbij, oplopend")
	ok(absf(HN.deel(6) - 0.5) < 0.01, "balkje halverwege tussen 5 en 7")
	ok(HN.niveau(4) == 2 and HN.niveau(5) == 3 and HN.niveau(7) == 4 and HN.niveau(16) == 5 and HN.niveau(17) == 6, "drempels hol 3, 4 en 6 op 5 / 7 / 17 (Bram 18:50, speeltestbuild)")
	# bordje (Mila 16 nov 16:20): één cijfer in het midden, twee cijfers -2,5 en +2,5; blad met 11 cellen
	var HB = load("res://systemen/holbord.gd")
	ok(HB.cijfers(5) == [[5, 0.0]] and HB.cijfers(12) == [[1, -2.5], [2, 2.5]], "bordje: cijfers en hun plek")
	# wachtkaartje (Mila 16 nov 16:55)
	ok(HB.kaart_cellen(0).is_empty() and HB.kaart_cellen(7) == [["kaart1", 0.0], ["k7", 0.0]], "kaartje: leeg zonder rij, +7 met kaart1")
	ok(HB.kaart_cellen(10) == [["kaart2", 0.0], ["k1", 0.0], ["k0", 4.0]], "kaartje: +10 met kaart2, eenheden 4 spelpixels rechts")
	var sp = JSON.parse_string(FileAccess.get_file_as_string("res://kunst/3d/sprites.json"))
	ok(sp.has("holbord") and sp["holbord"]["frames"].size() == 11 and ResourceLoader.exists(String(sp["holbord"]["blad"])), "bordje: blad holbord met leeg en c0 tot c9")
	ok(sp.has("holkaart") and sp["holkaart"]["frames"].size() == 12 and ResourceLoader.exists(String(sp["holkaart"]["blad"])), "kaartje: blad holkaart met kaart1, kaart2, k0 tot k9")
	var kp: Vector2 = HB.kaart_plek(sp["holbord"], sp["holkaart"])
	ok(absf(kp.x - (-6.25)) < 0.01 and absf(kp.y - 13.34) < 0.01, "kaartje: plek uit anker_x en nul_y (%s)" % str(kp))
	var hb = HB.new()
	ok(not hb.actief() and hb.plank_x() == 4.0, "bordje zonder blad of hol doet niets")
	hb.free()
	# doelregel als alles gekocht is (Sanne 16 nov 16:10, punt 6c)
	var KA = load("res://kern/kaartje.gd")
	ok(KA.niveau_doel(12) == "Next: a hat museum, 5 heroes", "doelregel volgend niveau: " + KA.niveau_doel(12))
	ok(KA.niveau_doel(11) == "Next: a tavern tale, 1 hero", "doelregel enkelvoud: " + KA.niveau_doel(11))
	ok(KA.niveau_doel(100000) == "", "doelregel leeg op het laatste niveau")
	var lang_d := 0
	for f_ in range(0, 90):
		if KA.niveau_doel(f_).length() > KA.DOEL_MAX:
			lang_d += 1
	ok(lang_d == 0, "doelregel altijd binnen 34 tekens")
	var lang_h := 0
	for f_ in range(0, 90):
		if HN.hover(f_).length() > HN.HOVER_MAX:
			lang_h += 1
	ok(lang_h == 0 and HN.HOVER_MAX == 43, "hover hooguit 43 tekens (Daan 18:40)")
	ok(HN.hover(25) == "Level 7: a hero shortage. 6 heroes to go." and HN.hover(88) == "Level 12: Gloop's Empire.", "hover langste geval en laatste niveau zonder staart")
	# optocht na weg zijn (Sanne 16 nov 14:50): 2 naar 12 is één optocht, geen tien feestjes
	ok(HN.weg_regel(3, 88) == "Grew 10 levels while you were away." and HN.weg_regel(3, 88).length() == 35, "weg-regel 10 niveaus, 35 tekens")
	ok(HN.weg_regel(10, 12) == "Hole level 5: a tavern tale." and HN.weg_regel(5, 5) == "", "weg-regel bij één niveau de gewone regel, bij geen niveau leeg")
	var op: Dictionary = HN.optocht(3, 88)
	var op_n: Array = []
	for p_ in op.poef:
		op_n.append(int(p_.niveau))
	ok(bool(op.wip) and op_n == [4, 9, 12], "optocht 2 naar 12: poef bij vleermuis, vaandel, hoedenwand (%s)" % str(op_n))
	ok(op.helden == [3, 5, 8, 10, 11], "nieuwe heldensoorten als bezoekers, in volgorde, geen poef")
	ok(absf(float(op.poef[0].t) - 1.2) < 0.01 and absf(float(op.poef[2].t) - 3.6) < 0.01 and float(op.duur) <= 12.0, "1,2 s na elkaar, hooguit 12 s")
	ok(bool(op.poef[0].munt) and not bool(op.poef[1].munt) and bool(op.poef[2].munt), "muntjes alleen bij eerste en laatste ding")
	ok(not bool(HN.optocht(5, 5).wip) and HN.optocht(10, 12).poef.is_empty(), "geen optocht zonder niveau; dief alleen als bezoeker")
	# rij bij de ingang (Sanne 16 nov 16:00): hooguit 4 meteen, rest wacht; zichtbaar = niveau - rij
	var rq: Dictionary = HN.weg(0, 136, 0)
	ok(rq.meteen == [2, 3, 4, 5] and int(rq.rij) == 7, "eerste nacht: hol 5 meteen, 7 in de rij (%s, %d)" % [str(rq.meteen), int(rq.rij)])
	# "Grew N levels" eruit (Iris keuring 6 tot 8, ja Daan 16 nov 20:50): alleen de rij-regel blijft
	ok(rq.regels == ["7 more to come as you play."], "regels na weg met rij (Daan 16:50 en 20:50): " + str(rq.regels))
	ok(HN.weg(0, 12, 0).rij == 0 and HN.weg(0, 12, 0).meteen.size() == 4 and HN.weg(0, 12, 0).regels.is_empty(), "4 niveaus zonder rij: geen regel (Daan 20:50) " + str(HN.weg(0, 12, 0)))
	ok(HN.zichtbaar(136, 7) == 5 and HN.zichtbaar(136, 0) == 12, "zichtbaar niveau = niveau min rij")
	var op4: Dictionary = rq.optocht
	ok(op4.helden == [3, 5] and op4.poef.size() == 1 and float(op4.duur) <= 5.0, "optocht met 4 niveaus: ridder, dief, vleermuis, kort")
	var rq2: Dictionary = HN.weg(136, 140, 7)
	ok(rq2.meteen == [6, 7, 8, 9] and int(rq2.rij) == 3, "tweede nacht met rij: weer hooguit 4 (%s, %d)" % [str(rq2.meteen), int(rq2.rij)])
	ok(HN.weg(10, 12, 0).rij == 0 and HN.weg(10, 12, 0).regels == ["Hole level 5: a tavern tale."], "één niveau: geen rij, gewone regel")
	ok(HN.rij_regel(1) == "1 more to come as you play." and HN.rij_hover(136, 7, 60.0) == "7 more to come. Next: a hat museum, in 2 min.", "rij-regel en hover: " + HN.rij_hover(136, 7, 60.0))
	ok(HN.rij_doel(136, 7, 60.0) == "Next: a hat museum, in 2 min", "doelregel met rij noemt wat komt (Iris 17:40): " + HN.rij_doel(136, 7, 60.0))
	ok(HN.rij_doel(136, 8, 179.0) == "Next: a tavern tale, in 1 min" and HN.REGELS_AAN, "doelregel rij: dief, 1 min; regels na weg aan (Daan 16:50)")
	for r_ in range(1, 12):
		ok(HN.rij_doel(136, r_, 0.0).length() <= HN.NAAM_MAX, "doelregel rij past in 34 tekens (rij %d)" % r_)
	var lang_n := 0
	for n_ in range(2, 13):
		if HN.niveau_regel(n_).length() > 42:
			lang_n += 1
	ok(lang_n == 0, "niveauregels hooguit 42 tekens")
	ok(r["gevallen"] + r["gevlucht"] == r["helden"], "gevallen + gevlucht = helden")
	var r2: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42)
	ok(r2["goud"] == r["goud"], "zelfde save, zelfde uitkomst")
	var terug: Dictionary = V.reken(t0, t0 - 86400, 3, 2, 42)
	ok(terug["helden"] == 0 and terug["goud"] == 0 and terug["teruggezet"] and terug["nieuwe_laatst"] == t0, "klok terug: niets kwijt, tijd gaat niet achteruit")
	var week: Dictionary = V.reken(t0, t0 + 7 * 86400, 1, 1, 42)
	var nacht: Dictionary = V.reken(t0, t0 + 12 * 3600, 1, 1, 42)
	ok(week["helden"] == nacht["helden"] and week["goud"] == nacht["goud"], "plafond 12 uur: week = nacht")
	ok(week["goud"] > 0, "na lang weg altijd winst, nooit verlies")
	var stil: Dictionary = V.reken(t0, t0 + 10, 0, 0, 1)
	ok(stil["regel"] == "All quiet while you were away.", "korte afwezigheid: rustige regel")
	# verhaal terwijl je weg was: regels met namen, hooguit 42 tekens, zelfde save = zelfde verhaal
	var hd := {"Kees": {"gevlucht": 1, "wrok": "Gloop the Slime"}, "Mara": {"gevlucht": 3, "wrok": "the Spike Pit"}}
	var vu: Dictionary = V.reken(t0, t0 + 6 * 3600, 1, 1, 42)
	var vh: Array = V.verhaal(vu, hd, ["Gloop the Slime", "the Spike Pit"], 42)
	ok(vh.size() >= 2 and vh.size() <= 3, "verhaal: 2 tot 3 regels (%d)" % vh.size())
	ok(vh[0].begins_with("Kees"), "verhaal noemt wie er terug was: " + vh[0])
	var lang := 0
	for r_ in vh:
		print("[hol-toets]   ", r_)
		if r_.length() > 42:
			lang += 1
	ok(lang == 0, "alle regels hooguit 42 tekens")
	ok(V.verhaal(vu, hd, ["Gloop the Slime", "the Spike Pit"], 42) == vh, "zelfde save, zelfde verhaal")
	ok(V.verhaal(V.reken(t0, t0 + 10, 1, 1, 42), hd, [], 42).is_empty(), "niemand kwam: geen verhaal")
	var zonder: Array = V.verhaal(vu, {}, ["Gloop the Slime"], 42)
	ok(zonder.size() >= 1 and zonder[-1].contains("gold"), "zonder bekende helden toch een regel met goud: " + zonder[-1])
	# een val aan het begin van de zin krijgt een hoofdletter (Daan 15 nov: "the Spike Pit had a busy shift.")
	var alleen_val: Array = V.verhaal(vu, {}, ["the Spike Pit"], 42)
	ok(alleen_val.size() >= 1 and alleen_val[0] == "The Spike Pit had a busy shift.", "val vooraan met hoofdletter: " + str(alleen_val))
	var klein := 0
	for r_ in vh + zonder + alleen_val:
		var c0: String = String(r_).substr(0, 1)
		if c0 != c0.to_upper():
			klein += 1
	ok(klein == 0, "elke regel van het verhaal begint met een hoofdletter of cijfer")
	# goud weg = goud in het spel (balans.md): 6 per val bij de start, meer met gangen en faam
	# graafbonus (Sanne 16 nov 21:00): +1 per 8 zelf gegraven cellen, hooguit +3; weg krijgt hem ook (7 + graafbonus)
	ok(V.graafbonus(0) == 0 and V.graafbonus(7) == 0 and V.graafbonus(8) == 1 and V.graafbonus(23) == 2 and V.graafbonus(24) == 3 and V.graafbonus(99) == 3, "graafbonus 0/0/1/2/3/3")
	var gb0: Dictionary = V.reken(t0, t0 + 8 * 3600, 1, 1, 42)
	var gb3: Dictionary = V.reken(t0, t0 + 8 * 3600, 1, 1, 42, 6, 0, null, 41)
	ok(int(gb3.gevallen) == int(gb0.gevallen) and int(gb3.goud) - int(gb0.goud) == 3 * int(gb0.gevallen), "weg met 41 gegraven: zelfde vallen, 3 goud per val meer (%d, %d)" % [int(gb0.goud), int(gb3.goud)])
	ok(V.goud_per_val(0, 0) == 6 and V.goud_per_val(6, 0) == 7 and V.goud_per_val(40, 0) == 12 and V.goud_per_val(40, 10) == 24, "goud per val volgt balans.md")
	var veel: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42, 30, 0)
	ok(veel["goud"] > r["goud"], "meer gangen, meer goud terwijl je weg bent (%d tegen %d)" % [veel["goud"], r["goud"]])
	var sterk: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42, 6, 20)
	ok(sterk["gevallen"] <= r["gevallen"] and sterk["goud"] > 0, "faam: helden sterker, nog steeds winst (%d tegen %d gevallen)" % [sterk["gevallen"], r["gevallen"]])
	# toets 3 van Sanne: naamgenoot met wrok, laatste 4 overslaan, terugkomer noemt waarom, hoedregels
	var k5 = K.new()
	k5.binnen("Kees")
	k5.gevallen("Kees", "Gloop the Slime", 6)
	var ik: Dictionary = k5.binnen(k5.vrije_naam("Kees"))
	ok(ik["naam"] == "Kees II" and ik["wrok"] == "Gloop the Slime", "Kees II komt met een wrok tegen Gloop (%s)" % ik["wrok"])
	ok(k5.laatste_soort == "naamgenoot_hoed" and k5.laatste().begins_with("Kees II"), "naamgenoot-regel hoed: " + k5.laatste())
	k5.binnen("Joep")
	k5.gevallen("Joep", "the Spike Pit", 6)
	var ij: Dictionary = k5.binnen("Joep II")
	ok(ij["wrok"] == "" and k5.laatste_soort == "naamgenoot", "naamgenoot van een put-held: geen wrok (%s)" % k5.laatste())
	k5.gevallen("Kees II", "Gloop the Slime", 6)
	var ik3: Dictionary = k5.binnen("Kees III")
	ok(ik3["wrok"] == "Gloop the Slime", "Kees III na Kees II door Gloop: ook een wrok")
	var k6 = K.new()
	var laatst: Array[String] = []
	var herhaald := 0
	for z in 200:
		k6.binnen("Held%d" % z)
		var rg: String = k6.laatste().replace("Held%d" % z, "X")
		if laatst.has(rg):
			herhaald += 1
		laatst.append(rg)
		if laatst.size() > 4:
			laatst.pop_front()
	ok(herhaald == 0, "binnenkomst: niet een van de laatste 4 regels opnieuw (%d keer)" % herhaald)
	var zonder_waarom := 0
	for z in 100:
		var nm := "Terug%d" % z
		k6.binnen(nm)
		k6.gevlucht(nm, "Gloop the Slime" if z % 2 == 0 else "the Spike Pit")
		k6.binnen(nm)
		var rg: String = k6.laatste()
		if not (rg.contains("Gloop") or rg.contains("Spike Pit") or rg.contains("Spooked")):
			zonder_waarom += 1
	ok(zonder_waarom == 0, "terugkomer noemt altijd wrok of bijnaam (%d zonder)" % zonder_waarom)
	var k7 = K.new()
	ok(k7.hoed("Kees", "Gloop the Slime", 1) == "Gloop wears Kees's hat now.", "eerste hoed: " + k7.laatste())
	ok(k7.hoed("Pim", "Gloop the Slime", 25) == "Gloop is now known as the Hatted.", "25 hoeden: " + k7.laatste())
	ok(k7.hoed("Pim", "Gloop the Slime", 0) == "", "aartsvijand naar de wand: geen hoedregel")
	var vaak := 0
	for z in 400:
		if k7.hoed("Held%d" % z, "Gloop the Slime", 2 + z % 20) != "":
			vaak += 1
	ok(vaak > 60 and vaak < 140, "hoedregel hooguit een op de vier (%d van 400)" % vaak)
	var te_lang2 := 0
	for regel in k5.regels + k6.regels + k7.regels:
		if regel.length() > 42:
			te_lang2 += 1
	ok(te_lang2 == 0, "nieuwe regels hooguit 42 tekens (%d te lang)" % te_lang2)

	# hoeden terwijl je weg was (Mila: de toren groeit vanzelf terwijl je weg bent)
	var hw: Dictionary = V.reken(t0, t0 + 3 * 3600, 1, 1, 42)
	ok(int(hw.opgegeten) > 0 and int(hw.opgegeten) < int(hw.gevallen), "weg 3 uur: een deel van de gevallen helden gaf Gloop een hoed (%d van %d)" % [int(hw.opgegeten), int(hw.gevallen)])
	ok(int(V.reken(t0, t0 + 3 * 3600, 2, 0, 42).opgegeten) == 0, "zonder bewoners geen hoeden")
	ok(hw.goud == V.reken(t0, t0 + 3 * 3600, 1, 1, 42).goud and hw.opgegeten == V.reken(t0, t0 + 3 * 3600, 1, 1, 42).opgegeten, "hoeden en goud: zelfde save, zelfde uitkomst")
	var hv0: Array = V.verhaal(hw, {}, ["Gloop the Slime", "the Spike Pit"], 42)
	ok(not str(hv0).contains("hat"), "hoeden nog niet gegeven: het verhaal noemt ze niet " + str(hv0))
	var sl1 = load("res://systemen/slijm.gd").new()
	var sl2 = load("res://systemen/slijm.gd").new()
	var hw7 := hw.duplicate()
	hw7["opgegeten"] = 7
	var per: Array = V.geef_hoeden([sl1, sl2], hw7, 42)
	ok(per == [4, 3] and sl1.hoeden.size() == 4 and sl2.hoeden.size() == 3 and sl1.hap_van < 0.0 and hw7.hoeden_gegeven, "hoeden verdeeld over twee slijmen, zonder hap (%s)" % str(per))
	var hv: Array = V.verhaal(hw7, {}, ["Gloop the Slime", "the Spike Pit"], 42)
	# "Gloop got N new hats." eruit (Iris keuring 6 tot 8, ja Daan 16 nov 20:50): de telling noemt de hoeden
	ok(hv.size() >= 1 and hv.size() <= 2 and not str(hv).contains("new hat") and hv[-1].contains(" 7 hats."), "na geef_hoeden noemt alleen de telling de hoeden: " + str(hv))
	var hw1 := hw.duplicate()
	hw1["opgegeten"] = 1
	V.geef_hoeden([sl1], hw1, 42)
	ok(V.verhaal(hw1, {}, ["Gloop the Slime"], 42)[-1].contains(" 1 hat."), "enkelvoud: 1 hat " + str(V.verhaal(hw1, {}, ["Gloop the Slime"], 42)))
	sl1.free()
	sl2.free()

	# Sanne toets 5 punt 2: geen binnenkom-regel die in de laatste 10 regels van de kroniek al stond
	var k8 = K.new()
	var sjablonen: Array[String] = []
	var dubbel10 := 0
	for z in 300:
		var nm := "Held%d" % z
		k8.binnen(nm)
		var sj: String = k8.laatste().replace(nm, "{naam}")
		if k8.laatste_soort.begins_with("binnen") and sjablonen.slice(maxi(0, sjablonen.size() - 10)).has(sj):
			dubbel10 += 1
		sjablonen.append(sj)
		# zoals in het spel: elke held heeft ook een afloop-regel (vallen of vluchten)
		if z % 3 == 0:
			k8.gevallen(nm, "the Spike Pit", 6)
		else:
			k8.gevlucht(nm, "Gloop the Slime")
		sjablonen.append(k8.laatste().replace(nm, "{naam}"))
	ok(dubbel10 == 0, "binnenkomst: geen regel die in de laatste 10 al stond (%d keer)" % dubbel10)
	# demo-minuut: 7 binnenkom-regels op rij, alle 7 verschillend (eerst alle andere, dan pas een herhaling)
	var k10 = K.new()
	var zeven := {}
	for z in 7:
		k10.binnen("Demo%d" % z)
		zeven[k10.laatste().replace("Demo%d" % z, "{naam}")] = true
	ok(zeven.size() == 7, "7 helden op rij: 7 verschillende binnenkom-regels (%d)" % zeven.size())
	# Olaf 22:35: één voorraad; kern/strook.gd kan dezelfde soorten en de getal-vorm van kies() gebruiken
	var stem = load("res://systemen/kroniek_regels.gd").new()
	var mist: Array[String] = []
	for soort in ["binnen", "naamgenoot", "terug", "terug_bewoner", "terug_val", "aartsvijand", "val", "val_bewoner", "afgerekend",
			"afgerekend_aarts", "vlucht", "schat", "plat", "op", "hoed_eerste", "hoed", "hoed_klein", "hoed_bijnaam"]:
		if not stem.VOORRAAD.has(soort):
			mist.append(soort)
	ok(mist.is_empty(), "alle soorten van strook.gd staan in kroniek_regels.gd (mist: %s)" % str(mist))
	# Sanne toets 9: hap en hoed in één regel, binnenkomst na het lied, voorrang in de wachtrij
	var stem9 = load("res://systemen/kroniek_regels.gd").new()
	ok(stem9.VOORRAAD.has("hap_hoed") and stem9.VOORRAAD.has("hap_hoed_eerste") and stem9.VOORRAAD.has("binnen_lied"), "soorten hap_hoed en binnen_lied staan erin")
	var namen_boek: Array = load("res://systemen/boek.gd").HOED_NAMEN
	var hoed_gelijk: bool = namen_boek.size() == stem9.HOED_KORT.size()
	for hi in mini(namen_boek.size(), stem9.HOED_KORT.size()):
		hoed_gelijk = hoed_gelijk and String(namen_boek[hi]).to_lower() == stem9.HOED_KORT[hi]
	ok(hoed_gelijk, "hoednamen in de regels gelijk aan boek.gd (zelfde volgorde als held_hoeden.png)")
	var r_eerste: String = stem9.hap_regel("Odo", "Gloop", 4, 1, 3)
	ok(r_eerste == "Gloop ate Odo. Kept the crown." and not stem9.hoed_apart, "eerste hoed: vaste regel met de hoed erin (%s)" % r_eerste)
	var hap_te_lang := 0
	for sj in stem9.VOORRAAD["hap_hoed"] + stem9.VOORRAAD["hap_hoed_eerste"]:
		for hn in stem9.HOED_KORT:
			var vol9: String = stem9.vul(sj, {"naam": "Lotte", "bewoner": "Gloop", "hoed": hn}) + " +6"
			if vol9.length() > 42 or vol9.contains("{"):
				hap_te_lang += 1
	ok(hap_te_lang <= 3, "hap-hoed-regels met Lotte en +6: bijna alle hoeden passen (%d niet, die kiest hap_regel dan niet)" % hap_te_lang)
	var r_n: Array[String] = []
	var hap_ok := true
	for z in 12:
		var rr: String = stem9.hap_regel("Lotte", "Gloop", z % 10, 2 + z, 3)
		r_n.append(rr)
		hap_ok = hap_ok and rr != "" and rr.length() + 3 <= 42 and not rr.contains("{") and rr.contains(stem9.HOED_KORT[z % 10]) and not stem9.hoed_apart
	ok(hap_ok, "12 happen met hoed: altijd één regel met de hoed, past met +6 (%s)" % r_n[1])
	var r_lang: String = stem9.hap_regel("Bartholomew the Unbudged", "Gloop", 9, 7, 3)
	ok(r_lang != "" and stem9.hoed_apart and not r_lang.contains("feather"), "lange naam: gewone hap-regel en hoed_apart, de beller doet de hoed los (%s)" % r_lang)
	var r_geen: String = stem9.hap_regel("Pim", "Gloop", -1, 0, 3)
	ok(r_geen != "" and not stem9.hoed_apart and stem9.VOORRAAD["val_bewoner"].has(r_geen.replace("Pim", "{naam}").replace("Gloop", "{bewoner}")), "zonder hoed: gewone hap-regel (%s)" % r_geen)
	var lied_lang := 0
	for sj in stem9.VOORRAAD["binnen_lied"]:
		if stem9.vul(sj, {"naam": "Bartholomew"}).length() > 42:
			lied_lang += 1
	ok(lied_lang == 0, "binnen_lied: alle vijf passen met een lange naam (%d niet)" % lied_lang)
	ok(stem9.vervalt_nooit("plat") and stem9.vervalt_nooit("binnen_lied") and not stem9.vervalt_nooit("binnen"), "plat en binnen_lied vervallen nooit, binnen wel")
	ok(stem9.is_sfeer("lied") and not stem9.is_sfeer("plat"), "lied is een sfeerregel")
	var soort_s = load("res://systemen/heldensoort.gd")
	ok(soort_s.rij("ridder") == 0 and soort_s.rij("bard") == 3 and soort_s.rij("") == -1, "rij in held_soort.png volgt SOORTEN")
	ok(not soort_s.aarts_mag(0) and not soort_s.aarts_mag(59) and soort_s.aarts_mag(60), "geen aartsvijand voor de 60e nieuwe held (±1 uur, sim.py aarts)")
	# pensioen bij openen (Sanne kroniek-regels.md): hooguit één, alleen na 30 min weg
	var Vp = load("res://systemen/voortgang.gd")
	var rp = load("res://systemen/kroniek_regels.gd").new()
	var lijst_p: Array = []
	for np in ["Kees", "Odo", "Mara", "Tibbe", "Pim", "Lotte", "Odo"]:
		lijst_p = Vp.met_pensioen(lijst_p, np)
	ok(lijst_p == ["Mara", "Tibbe", "Pim", "Lotte", "Odo"], "pensioenlijst: hooguit 5, oudste eraf, geen dubbele (%s)" % str(lijst_p))
	ok(Vp.pensioen(lijst_p, {"weg_s": 600}, rp).is_empty() and Vp.pensioen([], {"weg_s": 7200}, rp).is_empty(), "pensioen: niet na 10 min weg, niet zonder namen")
	var pp: Dictionary = Vp.pensioen(lijst_p, {"weg_s": 7200}, rp)
	ok(pp.get("naam", "") == "Mara" and String(pp.regel).begins_with("Mara ") and String(pp.regel).length() <= 42 and rp.VOORRAAD["pensioen"].has(String(pp.regel).replace("Mara", "{naam}")), "pensioen na 2 uur: de oudste, regel uit de voorraad (%s)" % str(pp))
	var pp2: Dictionary = Vp.pensioen(["Bartholomew the Unbudged"], {"weg_s": 7200}, rp)
	ok(String(pp2.get("regel", "")).length() <= 42 and String(pp2.get("regel", "")) != "", "pensioen met lange naam past (%s)" % str(pp2))
	var kleding := Image.load_from_file("res://kunst/held_soort.png")
	var rijen_vol: bool = kleding != null and kleding.get_width() == 64 and kleding.get_height() == 16 * soort_s.SOORTEN.size()
	if rijen_vol:
		for ri in soort_s.SOORTEN.size():
			for fi in 4:
				var gevuld := false
				for py in 16:
					for px in 16:
						if kleding.get_pixel(fi * 16 + px, ri * 16 + py).a > 0.5:
							gevuld = true
				rijen_vol = rijen_vol and gevuld
	ok(rijen_vol, "held_soort.png: 4 beelden per soort, elk met kleding (de luit zelf: Sanne op de film)")
	var rv: String = stem.kies("val", {"naam": "Bartholomew", "val": "the Spike Pit"}, 4)
	ok(rv != "" and rv.length() <= 38 and not rv.contains("+"), "kies met getal: ruimte voor ' +12', niets erachter (%s)" % rv)
	ok(stem.kies("plat", {"bewoner": "Gloop"}) == "Gloop is flat. Back soon.", "plat-regel uit dezelfde voorraad")
	ok(stem.kies("val_bewoner", {"naam": "Maximiliaan-Theodoor", "bewoner": "Gloop"}, 30) != "", "kies met getal geeft nooit leeg")
	var k9 = K.new()
	k9.binnen("Kees")
	k9.gevallen("Kees", "the Spike Pit", 6)
	k9.binnen("Kees II")
	ok(not k9.laatste().contains("II II") and not k9.laatste().contains("{") and k9.laatste().contains("Kees II"), "naamgenoot met {oud}: " + k9.laatste())
	# Sanne toets 6 punt 1: de wrok krijgt een afloop, met een eigen regel die de vijand noemt
	var k11 = K.new()
	k11.binnen("Bram")
	k11.gevlucht("Bram", "the Spike Pit")
	k11.binnen("Bram")
	k11.gevallen("Bram", "the Spike Pit", 9)
	var ra: String = k11.laatste()
	ok(k11.laatste_soort == "afgerekend_val" and ra.contains("The Spike Pit") and ra.ends_with(" +9") and ra.length() <= 42
		and not ra.contains("{"), "wrok tegen de put: eigen afloop-regel met hoofdletter: " + ra)
	var af_lang := 0
	for soort in ["afgerekend_val", "afgerekend_bewoner"]:
		for sj in stem.VOORRAAD[soort]:
			var vol: String = stem.vul(sj, {"naam": "Bram", "val": "the Spike Pit", "bewoner": "Gloop"}) + " +12"
			if vol.length() > 42 or vol.contains("{"):
				af_lang += 1
				print("  te lang of open: ", vol)
	ok(af_lang == 0, "afloop-regels met Bram en +12 passen in 42 tekens (%d niet)" % af_lang)
	ok(stem.kies("afgerekend_val", {"naam": "Bram", "val": ""}) == "", "afloop-regel met {Val} komt niet zonder val")
	ok(stem.kies("afgerekend_val", {"naam": "Bartholomew-Maximus", "val": "the Spike Pit"}, 4) != "", "getal-vorm: afloop-regel nooit leeg")
	# upgrades (Bram 10 nov, feature 5, balans.md): 45, 126, 353 (Sanne 01:50), drie per soort, volle prijs terug, opslaan
	var u = load("res://systemen/upgrades.gd").new()
	ok(u.kost("slijm") == 40 and u.kost("stekelput") == 40 and u.kost("draak") == -1, "eerste upgrade kost 40 (Sanne 26 nov, Iris 499fd9f punt 3)")
	var udemo = load("res://systemen/upgrades.gd").new()
	udemo.demo = true
	ok(udemo.kost("slijm") == 45 and udemo.kost("stekelput") == 45, "demo-film houdt 45 voor stap 1 (Daan #109 M1)")
	ok(FileAccess.get_file_as_string("res://kern/strook.gd").find("hol.upgrades.demo = demo") > 0, "strook zet de demo-vlag op de upgrades")
	ok(u.koop("slijm", 39) == -1 and u.niveau("slijm") == 0, "te weinig goud: niets gekocht")
	ok(u.koop("slijm", 100) == 60 and u.niveau("slijm") == 1 and u.kost("slijm") == 60, "kopen: 60 over, volgende kost 60")
	ok(u.koop("slijm", 60) == 0 and u.kost("slijm") == 70, "derde kost 70 (#134, Iris aandacht 7)")
	ok(u.koop("slijm", 70) == 0 and u.kost("slijm") == 75 and u.beeld_niveau("slijm") == 3, "na stap 3 nog stap 4 voor 75 (#145)")
	ok(absf(u.kans_erbij("slijm") - 0.21) < 0.0001 and u.kans_erbij("stekelput") == 0.0, "+7 procentpunt per stap")
	ok(u.goud_erbij() == 0 and u.koop("slijm", 75) == 0 and u.goud_erbij() == 2 and absf(u.plat_factor() * 30.0 - 15.0) < 0.01, "Sticky Gloop: 15 s plat en +2 goud per vangst")
	ok(absf(u.kans_erbij("slijm") - 0.21) < 0.0001, "stap 4 tot 6: geen extra kans (wrok blijft)")
	ok(u.kost("slijm") == 95 and u.koop("slijm", 95) == 0 and u.kost("slijm") == 115 and u.koop("slijm", 115) == 0 and u.goud_erbij() == 6, "stap 5 en 6: 95 en 115, samen +6 goud")
	ok(u.kost("slijm") == -1 and u.volgende("slijm").is_empty() and u.beeld_niveau("slijm") == 3, "na zes stappen alles gekocht, beeld blijft stap 3")
	ok(u.verkoop("slijm") == 115 and u.verkoop("slijm") == 95 and u.verkoop("slijm") == 75 and u.verkoop("slijm") == 70 and u.niveau("slijm") == 2, "weghalen geeft de volle prijs terug")
	var up_put = load("res://systemen/upgrades.gd").new()
	for i in 3:
		up_put.koop("stekelput", 1000)
	ok(up_put.kost("stekelput") == 85 and up_put.terug("stekelput") == 70, "put stap 4 kost 10 meer dan Gloop (85), om en om klaar")
	var u2 = load("res://systemen/upgrades.gd").new()
	u2.van_dict(u.naar_dict())
	ok(u2.niveau("slijm") == 2 and absf(u2.plat_factor() * 30.0 - 20.0) < 0.01, "opslaan en laden, Bouncy Gloop 20 s")
	u2.van_dict({"slijm": 9, "stekelput": -3})
	ok(u2.niveau("slijm") == 6 and u2.niveau("stekelput") == 0, "kapotte save: niveaus tussen 0 en 6")
	var stap_lang := 0
	for soort in ["slijm", "stekelput"]:
		for st in u2.STAPPEN[soort]:
			if String(st.naam).length() > 22 or String(st.uitleg).length() > 34:
				stap_lang += 1
	ok(stap_lang == 0 and u2.STAPPEN["slijm"].size() == u2.MAX_NIVEAU and u2.PRIJZEN.size() == u2.MAX_NIVEAU, "elke stap heeft naam (22) en uitleg (34) die passen, en een prijs")
	var regels_ok := 0
	var u3 = load("res://systemen/upgrades.gd").new()
	for soort in ["slijm", "stekelput"]:
		for n in 3:
			var vg: Dictionary = u3.volgende(soort)
			u3.koop(soort, 1000)
			var kr: String = u3.koop_regel(soort)
			if kr.length() <= 42 and String(vg.naam).length() <= 22 and String(vg.uitleg).length() <= 34:
				regels_ok += 1
			else:
				print("  te lang: ", kr, " | ", vg)
	ok(regels_ok == 6, "namen, uitleg en kroniekregel passen (%d van 6)" % regels_ok)
	var kr2: String = u3.koop_regel("slijm")
	ok(kr2 == "All hail Royal Gloop. Burp." and u3.put_verborgen(), "tweede regel voor Royal is de tweede grap: " + kr2)
	var u45 = load("res://systemen/upgrades.gd").new()
	var r45 := 0
	for soort in ["slijm", "stekelput"]:
		for n in u45.MAX_NIVEAU:
			u45.koop(soort, 1000)
			var r45s: String = u45.koop_regel(soort)
			if n >= 3 and r45s.length() <= 42 and not r45s.begins_with("The Spike Pit got ") and not r45s.contains("is now Sticky") and not r45s.contains("is now Greedy") and not r45s.contains("is now Gloop Prime"):
				r45 += 1
			elif n >= 3:
				print("  stap 4 tot 6 zonder eigen regel: ", r45s)
	ok(r45 == 6, "stap 4 tot 6 hebben een eigen kroniekregel die past (%d van 6, #145)" % r45)
	var u5 = load("res://systemen/upgrades.gd").new()
	u5.koop("slijm", 1000)
	ok(u5.koop_regel("slijm") == "Gloop is now Big Gloop. Bigger mouth.", "eerste koop: eerste grap van Sanne")
	var u7 = load("res://systemen/upgrades.gd").new()
	u7.koop("slijm", 1000)
	ok(u7.koop_regel("slijm", "Bartholomew") == "Bartholomew grew. The hats fit better.", "lange naam: de eerste grap die in 42 tekens past")
	ok(u5.koop_regel("slijm", "Gloopsterwurmendraakwiggelaarxx").begins_with("Gloopsterwurmendraakwiggelaarxx is now Big"), "heel lange naam: de vaste korte regel, nooit leeg")
	# terug(): wat Undo teruggeeft, gelijk aan wat de bovenste stap kostte
	var u6 = load("res://systemen/upgrades.gd").new()
	ok(u6.terug("slijm") == 0, "niets gekocht: Undo geeft 0")
	var terug_ok := true
	for n in 3:
		var kost_u6: int = u6.kost("stekelput")
		u6.koop("stekelput", 1000)
		terug_ok = terug_ok and u6.terug("stekelput") == kost_u6
	ok(terug_ok and u6.terug("stekelput") == 70, "terug() is steeds de prijs van de bovenste stap (40, 60, 70)")
	ok(u6.verkoop("stekelput") == 70 and u6.terug("stekelput") == 60, "na weghalen: terug() de prijs van de stap eronder")
	# #134 (Iris aandacht 7): minuut 0 tot 4 gelijk, daarna meer goud en een krappe droogte zolang er iets te koop is
	var AFL134 := load("res://kern/afloop.gd")
	var RIT := load("res://kern/ritme.gd")
	ok(AFL134.GOUD_LAAT > 0 and AFL134.LAAT_VANAF_S == 240.0 and RIT.LAAT_VANAF_S == 240.0, "na minuut 4 meer goud per vangst (#134)")
	ok(RIT.DROOGTE_KRAP_S < RIT.DROOGTE_S and RIT.KRAP_NA_KOOP_S >= 60.0, "krappe droogte alleen na lang geen koop (#134)")
	var rit_src := FileAccess.get_file_as_string("res://kern/ritme.gd")
	ok(rit_src.find("alles gekocht") > 0 and FileAccess.get_file_as_string("res://kern/kaartje.gd").find("laatste_koop_t") > 0, "krappe droogte stopt als alles gekocht is, koop zet laatste_koop_t (#134)")
	# Daan #109 M1: de demo-film (demo=1) blijft gelijk: geen koopgeluk en de oude basis 6 in de demo
	var kaart_src := FileAccess.get_file_as_string("res://kern/kaartje.gd")
	var i_demo := kaart_src.find("if not s.demo:")
	var i_geluk := kaart_src.find('s.hol.set_meta("koop_geluk", soort)')
	ok(i_demo > 0 and i_geluk > i_demo and i_geluk - i_demo < 200, "M1: koopgeluk alleen buiten de demo (kaartje.koop)")
	var AFL = load("res://kern/afloop.gd")
	ok(AFL.GOUD_DEMO == 6 and AFL.GOUD_BASIS == 9, "M1: demo houdt goud 6 per vangst, het spel 9")
	# volgend doel in het paneel (Iris keuring 1, probleem 2)
	var ud = load("res://systemen/upgrades.gd").new()
	var d0: Dictionary = ud.doel(["slijm", "stekelput"], 20)
	ok(d0.get("soort") == "slijm" and int(d0.get("kost")) == 40 and int(d0.get("tekort")) == 20, "doel: nieuw spel Big Gloop, 40, nog 20")
	ok(ud.doel(["slijm"], 50).get("tekort") == 0, "doel: tekort 0 als het kan")
	ud.koop("slijm", 1000)
	ok(ud.doel(["slijm", "stekelput"], 0).get("soort") == "stekelput", "doel: goedkoopste wint (put 40 voor Bouncy 60)")
	ok(ud.doel(["slijm"], 0).get("naam") == "Bouncy Gloop", "doel: zonder put alleen Gloop")
	for i in ud.MAX_NIVEAU - 1:
		ud.koop("slijm", 1000)
	ok(ud.doel(["slijm"], 0).is_empty(), "doel: alles gekocht geeft niets")
	var KJD = load("res://kern/kaartje.gd")
	ok(KJD.doel_tekst("Big Gloop", "Gloop", 45, 20) == "Next: Big Gloop, 25 gold to go", "doel_tekst: nog goud nodig")
	ok(KJD.doel_tekst("Big Gloop", "Gloop", 45, 45) == "Big Gloop ready: click Gloop", "doel_tekst: kan, zeg waar klikken")
	ok(KJD.doel_tekst("x", "y", -1, 0) == "", "doel_tekst: alles gekocht leeg")
	# Gloop is klaar (Mila, issue #62): de ring komt zacht op en ademt rustig, nooit uit en nooit fel knipperend
	var GR = load("res://systemen/gloop_ring.gd")
	ok(GR.adem(0.0).x == 0.0, "gloopring: begint onzichtbaar (komt zacht op)")
	var amin := 9.0
	var amax := 0.0
	for i in range(1, 60):
		var a: Vector2 = GR.adem(GR.OPKOMEN_S + i * 0.1)
		amin = minf(amin, a.x)
		amax = maxf(amax, a.x)
	ok(amin >= 0.6 and amax <= 1.0 and amax - amin <= 0.4, "gloopring: ademt tussen 0,6 en 1 (%.2f tot %.2f)" % [amin, amax])
	ok(GR.ADEM_S >= 2.0, "gloopring: rustig, één keer ademen duurt minstens 2 s")
	ok(load("res://kunst/gloopring.png") != null, "gloopring: blad uit Blender staat erin")
	# munt op de ring (Iris e39939e): staat erin, naast zijn mond (niet ervoor) en helemaal in de onderste helft plus
	# hooguit de halve munt erboven, zodat hij vóór Gloop staat en niet achter zijn lijf verdwijnt
	ok(load("res://kunst/gloopmunt.png") != null, "gloopring: munt uit Blender staat erin")
	ok(absf(GR.MUNT_MIDDEN.x) >= 5.0, "gloopring: munt naast de mond van Gloop (x %.1f)" % GR.MUNT_MIDDEN.x)
	ok(GR.MUNT_MIDDEN.y >= 0.0 and GR.MUNT_MIDDEN.y + GR.MUNT_CEL / 2.0 <= GR.CEL_H / 2.0 + 1.5, "gloopring: munt staat vooraan op de ring")
	# Gloop-les (Daan #68): de eerste keer dat de ring aangaat één keer de regel met pijl, weg na klik, ring uit of 20 s
	var EM = load("res://kern/eerste_minuut.gd")
	ok(EM.gloop_les_mag(false, EM.KLAAR, true), "gloop-les: eerste keer ring aan na de les")
	ok(not EM.gloop_les_mag(true, EM.KLAAR, true), "gloop-les: nooit een tweede keer")
	ok(not EM.gloop_les_mag(false, EM.VAL, true), "gloop-les: niet tijdens de eerste minuut (één regel tegelijk)")
	ok(not EM.gloop_les_weg(5.0, "", true) and EM.gloop_les_weg(EM.GLOOP_MAX_S, "", true), "gloop-les: blijft tot 20 s")
	ok(EM.gloop_les_weg(1.0, "slijm", true) and EM.gloop_les_weg(1.0, "", false), "gloop-les: weg na klik of als de ring uitgaat")
	ok(EM.GLOOP_TEKST.length() <= 30, "gloop-les: regel kort (%d tekens)" % EM.GLOOP_TEKST.length())
	var langste := 0
	for st in ["slijm", "stekelput"]:
		for stap in load("res://systemen/upgrades.gd").STAPPEN[st]:
			langste = maxi(langste, KJD.doel_tekst(String(stap.naam), "the pit", 353, 0).length())
	ok(langste <= KJD.DOEL_MAX, "doel_tekst: hooguit %d tekens (langste %d)" % [KJD.DOEL_MAX, langste])
	# voortgang telt upgrades mee; zonder upgrades precies als voorheen
	var vz: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42)
	var vn: Dictionary = V.reken(t0, t0 + 3600, 1, 1, 42, 6, 0, null)
	var u4 = load("res://systemen/upgrades.gd").new()
	u4.van_dict({"slijm": 3, "stekelput": 3})
	var vm: Dictionary = V.reken(t0, t0 + 6 * 3600, 1, 1, 42, 6, 0, u4)
	var vz6: Dictionary = V.reken(t0, t0 + 6 * 3600, 1, 1, 42)
	ok(vz.goud == vn.goud and vz.gevallen == vn.gevallen, "voortgang zonder upgrades gelijk aan voorheen")
	ok(vm.gevallen >= vz6.gevallen and vm.goud >= vz6.goud, "voortgang met upgrades: minstens zoveel gevallen (%d tegen %d)" % [vm.gevallen, vz6.gevallen])

	# heldensoorten in de kroniek (Bram 10 nov)
	var ks = load("res://systemen/kroniek.gd").new()
	var ib: Dictionary = ks.binnen("Odo", "hebzuchtig", "ridder")
	ok(String(ib.soort_held) == "ridder" and ks.laatste().contains("Odo"), "ridder komt binnen met eigen regel: " + ks.laatste())
	ks.gevlucht("Odo", "the Spike Pit")
	var ib2: Dictionary = ks.binnen("Odo")
	ok(String(ib2.soort_held) == "ridder", "terugkomer houdt zijn soort")
	var lr: String = ks.lied("Fenna")
	ok(lr != "" and lr.length() <= 42, "bard zingt: " + lr)
	var dr: String = ks.dutje("Pim")
	ok(dr != "" and dr.length() <= 42, "slaapkop dutje: " + dr)
	var soort_lang := 0
	for sj in ["binnen_ridder", "binnen_dief", "binnen_magier", "binnen_bard", "lied", "binnen_slaapkop", "binnen_wraakzuchtig", "binnen_opschepper", "dutje"]:
		for rsj in ks.stem.VOORRAAD[sj]:
			if ks.stem.vul(rsj, {"naam": "Joost III", "held": "Joost III", "bewoner": "Gloop", "val": "the Spike Pit"}).length() > 42:
				soort_lang += 1
	ok(soort_lang == 0, "regels van de soorten passen met Joost III in 42 tekens (%d te lang)" % soort_lang)
	# Heldenboek (systemen/boek.gd, Sanne features.md 10 nov 03:10)
	var bk = load("res://systemen/boek.gd").new()
	bk.vast = 0   # de vaste regel (eerste variant)
	var bk_r1: String = bk.held("magier", "slijm", "Wout")
	ok(bk_r1 == "First wizard for Gloop!", "eerste vangst van een soort: nieuwe bladzijde (" + bk_r1 + ")")
	ok(bk.held("magier", "slijm", "Pim") == "", "zelfde stempel twee keer: geen regel")
	ok(bk.held("magier", "stekelput", "Pim") == "First wizard in the pit!", "tweede stempel op dezelfde bladzijde")
	ok(bk.zwakte("magier") == "Weak to: Gloop" and bk.zwakte("ridder") == "", "zwakte pas na de eerste vangst, uit heldensoort.gd")
	bk.held("ridder", "stekelput", "Odo")
	ok(bk.zwakte("ridder") == "Weak to: Spike Pit", "ridder is zwak tegen de put (Sanne 03:05)")
	bk.held("", "slijm", "Kees")
	bk.held("bard", "ontsnapt", "Lotte")
	ok(bk.zwakte("") == "" and bk.zwakte("bard") == "", "gewone held en bard: geen zwakte (gelijk)")
	ok(bk.moment("hebzuchtig", "Tibbe") == "Tibbe touched the hoard!" and bk.moment("hebzuchtig", "Mara") == "", "moment van een trek: één keer")
	ok(bk.moment("verdwaald", "Rik") == "", "verdwaald bestaat nog niet in het spel: geen bladzijde")
	ok(bk.hoed(5, "Kees") == "New hat: Chef's hat. Thanks, Kees." and bk.hoed(5, "Pim") == "", "eerste hoed met naam, daarna niet meer")
	ok(bk.berg(999) == "" and bk.berg(3500) == "The hat pile reached 3000!" and bk.berg(3600) == "", "hoedenberg: sprong geeft de hoogste stempel, één keer")
	ok(bk.aarts("Kees", {"wrok": "Gloop", "bezoeken": 3}) == "Kees is your nemesis now." and bk.aarts("Kees", {"bezoeken": 4}) == "", "nieuwe aartsvijand, bijwerken zonder regel")
	ok(bk.aarts_af("Kees", "the Spike Pit", 4) == "Kees won't be back. Day 4." and bk.aarts_af("Kees", "Gloop", 5) == "", "afgerekend één keer")
	var bk_lang := 0
	for bk_rr in bk.log_nieuw:
		if String(bk_rr).length() > 42:
			bk_lang += 1
	ok(bk_lang == 0 and bk.log_nieuw.size() == 10, "alle boekregels hooguit 42 tekens (%d te lang, %d regels)" % [bk_lang, bk.log_nieuw.size()])
	# Varianten (Sanne kroniek-regels.md "Heldenboek" 05:05): willekeurig, nooit twee keer achter elkaar, alle varianten komen,
	# met de langste gevallen alles in 42 tekens.
	var bv_dubbel := 0
	var bv_lang := 0
	var bv_zinnen := {}
	for zaad in 40:
		var bv = load("res://systemen/boek.gd").new()
		bv.rng.seed = zaad
		for sh in ["", "ridder", "dief", "magier", "bard"]:
			for w in ["slijm", "stekelput", "ontsnapt"]:
				var rr: String = bv.held(sh, w, "Tibbe")
				bv_zinnen[rr.split(".")[0] + "|" + rr.substr(rr.find(".") + 2)] = true
		for nr in 10:
			bv_zinnen[bv.hoed(nr, "Tibbe").left(6)] = true
		for tk in ["hebzuchtig", "schijterig", "slaapkop", "wraakzuchtig", "opschepper"]:
			bv_zinnen[bv.moment(tk, "Tibbe").left(6)] = true
		bv_zinnen[bv.berg(10000)] = true
		for nn in ["Tibbe", "Mara", "Odo", "Kees"]:
			bv_zinnen[bv.aarts(nn).right(10)] = true
			bv_zinnen[bv.aarts_af(nn, "Gloop", 123).left(5)] = true
		for rr in bv.log_nieuw:
			if String(rr).length() > 42:
				bv_lang += 1
		if zaad == 0:
			print("[hol-toets] boekregels zaad 0: ", bv.log_nieuw)
	# 3 pagina x 2 hoe-slijm + put/weg-varianten op stempels, 3 hoed, 3 moment, 3 berg, 3 aarts, 3 aarts_af
	ok(bv_zinnen.size() >= 3 + 3 + 3 + 3 + 3, "over 40 zaden komen veel varianten voor (%d verschillend)" % bv_zinnen.size())
	ok(bv_lang == 0, "alle varianten met Tibbe, dag 123 en 10000 hoeden in 42 tekens (%d te lang)" % bv_lang)
	var bv2 = load("res://systemen/boek.gd").new()
	var bv_vorige := -1
	for i in 200:
		bv2._kies("x", ["a", "b", "c"])
		if int(bv2.vorige["x"]) == bv_vorige:
			bv_dubbel += 1
		bv_vorige = int(bv2.vorige["x"])
	ok(bv_dubbel == 0, "nooit twee keer achter elkaar dezelfde variant (%d keer)" % bv_dubbel)
	var bv_tel := {}
	for i in 300:
		bv_tel[bv2._kies("y", ["a", "b", "c"])] = true
	ok(bv_tel.size() == 3, "alle drie de varianten komen voor")
	var bv3 = load("res://systemen/boek.gd").new()
	bv3.vast = 2
	ok(bv3.berg(1000, "Gloop") == "1000 hats. Gloop is very proud." and bv3.aarts("Odo") == "Odo will be back. Angry." and bv3.held("magier", "stekelput", "Pim") == "The pit's first wizard.", "derde varianten zoals Sanne ze schreef")
	var bk2 = load("res://systemen/boek.gd").new()
	bk2.vast = 0
	ok(bk2.held("", "slijm", "Bartholomew the Unbudged").length() <= 42 and bk2.hoed(9, "Bartholomew the Unbudged") == "New hat: Feather cap.", "lange naam: korte regel, nooit te lang")
	var bk_v: Dictionary = bk.vol()
	ok(bk_v.kan == 15 + 5 + 10 + 3 and bk_v.heb == 6 + 1 + 1 + 1, "vol(): %d van %d (aartsvijanden tellen niet mee)" % [bk_v.heb, bk_v.kan])
	var bk3 = load("res://systemen/boek.gd").new()
	bk3.van_dict(JSON.parse_string(JSON.stringify(bk.naar_dict())))
	ok(bk3.vol().heb == bk_v.heb and bk3.paginas().size() == bk.paginas().size() and bk3.aartsvijanden[0].af_dag == 4, "opslaan door JSON en terug: zelfde boek")
	bk3.van_dict({"helden": {"draak": {"slijm": "x"}, "dief": "kapot"}, "hoeden": {"99": "x", "a": "y"}, "berg": [7, 1000, 1000], "aarts": [3, {}]})
	ok(bk3.vol().heb == 1 and bk3.aartsvijanden.is_empty(), "kapotte save: alleen wat klopt blijft")
	var bk4 = load("res://systemen/boek.gd").new()
	bk4.van_dict({"berg": null, "aarts": null, "momenten": null})
	bk4.van_dict({"berg": [{}], "helden": {"dief": {"slijm": null}}, "hoeden": {"1": null}, "aarts": [{"naam": {}}, {"naam": "Kees", "bezoeken": [1]}]})
	ok(bk4.vol().heb == 0 and bk4.aartsvijanden.size() == 1 and bk4.aartsvijanden[0].bezoeken == 3, "save met null en verkeerde soorten: geen fout, standaardwaarden")
	var bk_p: Array = bk.paginas()
	ok(bk_p.size() == 5 + 5 + 10 + 1 + 1 and String(bk_p[3].titel) == "The Wizard" and bk_p[3].regels[0] == "Weak to: Gloop", "bladzijden in boekvolgorde, magier met zwakte")
	ok(bk.nieuw_sinds(8).size() == 2 and bk.nieuw_sinds(99).is_empty(), "nieuw_sinds voor while you were away")
	# demo-einde (Olaf 13 nov, kern/demo_einde.gd): alleen met steamdemo, precies één keer, startregel daarna
	var DE = load("res://kern/demo_einde.gd")
	ok(not DE.voorbij(false, 99999.0) and not DE.voorbij(true, 7199.9) and DE.voorbij(true, 7200.0), "demo voorbij alleen met steamdemo en na 7200 s")
	ok(DE.regel_bij_einde(true, 59.9, 60.1, 60.0) == DE.REGEL_EINDE and DE.regel_bij_einde(true, 60.1, 60.2, 60.0) == ""
		and DE.regel_bij_einde(false, 59.9, 60.1, 60.0) == "", "eindregel precies één keer, nooit zonder steamdemo")
	var keer := 0
	var st := 0.0
	for i in 1000:
		var de_r: String = DE.regel_bij_einde(true, st, st + 0.13, 60.0)
		st += 0.13
		if de_r != "":
			keer += 1
	ok(keer == 1, "eindregel één keer in 130 s met kleine stapjes: %d" % keer)
	ok(DE.regel_bij_start(true, 61.0, 60.0) == DE.REGEL_START and DE.regel_bij_start(true, 59.0, 60.0) == ""
		and DE.regel_bij_start(false, 99999.0) == "", "startregel alleen na het einde, alleen in de demo")
	ok(DE.REGEL_EINDE.length() <= 42 and DE.REGEL_START.length() <= 42 and DE.KAART.length() <= 42, "demo-regels hooguit 42 tekens")
	ok(DE.is_demo(PackedStringArray(["steamdemo=1"])) and not DE.is_demo(PackedStringArray(["demo=1", "steamdemo=0"])), "steamdemo=1 herkend, demo=1 is geen Steam-demo")
	# het vaste deel van het hol (Olaf, hol/hol_vast.gd): alleen opnieuw tekenen als er iets aan verandert
	var hvast = Node2D.new()
	hvast.set_script(load("res://hol/hol.gd"))
	hvast.scale = Vector2(3, 3)
	hvast.maak(320)
	hvast.leg_aan(15)
	hvast.vast.ververs()
	var k0: int = hvast.vast.keer
	hvast.vast.ververs()
	hvast.tik()
	hvast.vast.ververs()
	ok(k0 == 1 and hvast.vast.keer == 1, "hol_vast: één keer tekenen, tik en tweede beeld tekenen niet opnieuw (%d, %d)" % [k0, hvast.vast.keer])
	ok(hvast.vast.vp.size == Vector2i(hvast.kolommen * 16 * 3, 120), "hol_vast: eigen beeld op schermgrootte %s" % str(hvast.vast.vp.size))
	var put_k: int = hvast.vallen.keys()[0]
	hvast.put_klap(put_k)
	hvast.vast.ververs()
	ok(hvast.vast.keer == 2, "hol_vast: put klapt open, opnieuw (stuk put wordt gang)")
	# leven in het spel 5 (Olaf 15 nov, getallen Daan juice.md): stofwolkje en schok bij de klap
	var st0: Array = hvast.stof_stofjes(put_k)
	ok(st0.size() >= 4 and st0.size() <= 5, "val: 4 tot 5 stofjes bij de klap (%d)" % st0.size())   # kan Daan 15 nov 19:55
	ok(hvast.put_schok(put_k) == 1, "val: de put zakt 1 spelpixel bij de klap")
	ok(hvast.stof_stofjes(put_k + 1).is_empty() and hvast.put_schok(put_k + 1) == 0, "val: alleen bij die put")
	hvast._process(0.12)
	ok(hvast.put_schok(put_k) == 0, "val: na 2 beelden staat de put weer")
	var st1: Array = hvast.stof_stofjes(put_k)
	var stof_omhoog := st1.size() == st0.size()
	for i in mini(st0.size(), st1.size()):
		stof_omhoog = stof_omhoog and (st1[i][0] as Vector2i).y <= (st0[i][0] as Vector2i).y and float(st1[i][2]) < float(st0[i][2])
	ok(stof_omhoog, "val: stofjes gaan omhoog en vervagen")
	ok((st1[0][0] as Vector2i).x < (st0[0][0] as Vector2i).x and (st1[-1][0] as Vector2i).x > (st0[-1][0] as Vector2i).x, "val: stofjes gaan naar buiten")
	hvast._process(0.25)
	ok(hvast.stof_stofjes(put_k).is_empty() and hvast.val_stof.is_empty(), "val: na 0,35 s geen stof meer")
	hvast.klik(Vector2((hvast.ingang_kol - 1) * 16 + 8, 30))
	hvast.vast.ververs()
	ok(hvast.vast.keer == 3, "hol_vast: graven links, opnieuw")
	hvast.free()
	# kamerkeuze in het 3D-hol (Olaf 13 nov, moet 3 Daan): stuk volgt de buren; schacht (2) en 3D-schatkamer (10-12) dicht
	var H3 = load("res://hol/hol_3d.gd")
	var b := []
	b.resize(16)
	b.fill(false)
	for kk in [2, 4, 6, 7, 8, 10, 11, 12, 3]:
		b[kk] = true
	ok(H3.kamer_keuze(b, 3, 2, 12, true) == "kamer_begin", "naast de schacht begint de kamer: " + H3.kamer_keuze(b, 3, 2, 12, true))
	ok(H3.kamer_keuze(b, 4, 2, 12, true) == "kamer_eind", "cel 4 na 3: eind")
	b[3] = false
	ok(H3.kamer_keuze(b, 4, 2, 12, true) == "kamer_los", "losse kamer zonder buren")
	ok(H3.kamer_keuze(b, 6, 2, 12, true) == "kamer_begin" and H3.kamer_keuze(b, 8, 2, 12, true) == "kamer_eind",
		"rij 6-8: begin en eind")
	ok(H3.kamer_keuze(b, 7, 2, 12, true) == "kamer_midden_c", "kamer van drie: midden kaal")
	b[9] = true
	ok(H3.kamer_keuze(b, 8, 2, 12, true) == "kamer_midden_c", "rij 6-9: kamer van vier blijft kaal in het midden: " + H3.kamer_keuze(b, 8, 2, 12, true))
	ok(H3.kamer_keuze(b, 9, 2, 12, true) == "kamer_eind", "3D-schatkamer telt als dicht: eind")
	ok(H3.kamer_keuze(b, 9, 2, 12, false) == "kamer_midden_a", "zonder 3D-schatkamer loopt de kamer door (6-12, midden een stut)")
	# Daan 16 nov 23:40 (moet): bovenste rij per drie middencellen precies één ding, om en om, nooit twee gelijk na elkaar
	# kamers van 4 tot 9 cellen: nooit een ding naast fakkel of kistje, nooit twee dingen in drie cellen op een rij
	# (fakkel en kistje tellen als ding)
	var kort_ok := true
	for klang in range(4, 10):
		var kb2 := []
		for kk in 30:
			kb2.append(kk >= 5 and kk < 5 + klang)
		var rij2 := []
		for kk in range(5, 5 + klang):
			var n2: String = H3.kamer_keuze(kb2, kk, 1, 28, false)
			rij2.append(0 if n2 == "kamer_midden_c" else 1)
		for j in range(0, rij2.size() - 2):
			if rij2[j] + rij2[j + 1] + rij2[j + 2] > 1:
				kort_ok = false
	ok(kort_ok, "kamers van 4 tot 9 cellen: fakkel, dingen en kistje nooit twee in drie cellen")
	var kb7 := []
	for kk in 30:
		kb7.append(kk >= 5 and kk < 12)
	ok(H3.kamer_keuze(kb7, 8, 1, 28, false) != "kamer_midden_c", "kamer van zeven: ding precies in het midden")
	for kst in [3, 4, 5]:
		var klb := []
		for kk in 60:
			klb.append(kk >= kst and kk <= 50)
		var klijst := []
		for kk in range(kst + 1, 50):
			klijst.append(H3.kamer_keuze(klb, kk, 1, 58, false))
		var kdingen := []
		var kper_ok := true
		for g in range(0, klijst.size() - 2, 3):
			var n := 0
			for j in 3:
				if klijst[g + j] != "kamer_midden_c":
					n += 1
					kdingen.append(klijst[g + j])
			if n > 1:
				kper_ok = false
		var kwissel_ok := kdingen.size() >= 10
		for j in range(1, kdingen.size()):
			if kdingen[j] == kdingen[j - 1]:
				kwissel_ok = false
		ok(kper_ok and kwissel_ok, "bovenste rij vanaf %d: per drie middencellen hooguit één ding, om en om (%d dingen)" % [kst, kdingen.size()])
	b[14] = true
	b[15] = true
	ok(H3.kamer_keuze(b, 15, 2, 12, true) == "kamer_eind", "rechterrand telt niet als buur: " + H3.kamer_keuze(b, 15, 2, 12, true))
	ok(H3.kamer_keuze(b, 0, 2, 12, true) == "kamer_los", "kolom 0 kijkt niet buiten de rij")
	# rest van de versiering in 3D (Olaf 14 nov, kan Daan 13 nov 19:35): ankerpunt en terugval naar pixels
	H3.laad()
	ok(H3.DECO_GANG.size() == 9 and H3.DECO_GANG[6] == "spinrag" and H3.DECO_GANG[7] == "stut", "deco: namen op de vakken van versiering.png")
	ok(H3.DECO_MAAIVELD.size() == 5, "deco: vijf maaiveldnamen")
	ok(H3.deco_plek("bestaat_niet", Vector2(40, 39), false) == Vector2.INF, "deco: niet in het blad, dan pixels")
	var oud_blad = H3.deco_blad
	var oud_deco: Dictionary = H3.deco
	H3.deco_blad = CanvasTexture.new()
	H3.deco = {"proef": {"maat": [6, 12], "vak_px": [0, 0, 24, 48]}, "proef_voet": {"maat": [6, 12], "vak_px": [0, 0, 24, 48], "voet": [2, 10], "hang": [1, 2]}}
	ok(H3.deco_plek("proef", Vector2(40, 39), false) == Vector2(37, 27), "deco staand: midden onderkant op het punt: " + str(H3.deco_plek("proef", Vector2(40, 39), false)))
	ok(H3.deco_plek("proef", Vector2(40, 24), true) == Vector2(37, 24), "deco hangend: midden bovenkant op het punt")
	ok(H3.deco_plek("proef_voet", Vector2(40, 39), false) == Vector2(38, 29), "deco staand met voet uit de pijplijn")
	ok(H3.deco_plek("proef_voet", Vector2(40, 24), true) == Vector2(39, 22), "deco hangend met hang uit de pijplijn")
	ok(H3.deco_plek("proef", Vector2(40.5, 39), false) == Vector2(37, 27), "deco: hele spelpixels")
	H3.deco_blad = oud_blad
	H3.deco = oud_deco
	# put in 3D met gekochte stappen (Olaf 14 nov): geen pixel-put meer als het 3D-stuk er is
	var oud_hblad = H3.blad
	var oud_stukken: Dictionary = H3.stukken
	H3.blad = CanvasTexture.new()
	H3.stukken = {"put": {"maat": [16, 16], "vak_px": [0, 0, 64, 64]}, "gang": {"maat": [16, 16], "vak_px": [64, 0, 64, 64]}}
	var pu = load("res://systemen/upgrades.gd").new()
	var ph := {"met_3d": true, "vallen": {7: "stekelput"}, "put_open": {}, "upgrades": pu}
	ok(H3.put_stuk(ph, 7) == "vast" and H3.put_stuk(ph, 6) == "", "put 3D: dicht zonder stappen zit in het vaste beeld, geen put geen stuk")
	ph["put_open"] = {7: 1.0}
	ok(H3.put_stuk(ph, 7) == "put", "put 3D: open na een klap is de 3D-put, geen pixels")
	ph["put_open"] = {}
	pu.van_dict({"slijm": 0, "stekelput": 1})
	ok(H3.put_stuk(ph, 7) == "put", "put 3D: Rusty Spikes zonder eigen stuk valt terug op de 3D-put")
	H3.stukken["put_1"] = {"maat": [16, 16], "vak_px": [128, 0, 64, 64]}
	ok(H3.put_stuk(ph, 7) == "put_1", "put 3D: Rusty Spikes met eigen stuk put_1")
	pu.van_dict({"slijm": 0, "stekelput": 3})
	ok(H3.put_stuk(ph, 7) == "gang", "put 3D: Trick Lid dicht ziet eruit als vloer")
	ph["put_open"] = {7: 1.0}
	ok(H3.put_stuk(ph, 7) == "put", "put 3D: Trick Lid open toont de stekels")
	ph["met_3d"] = false
	ok(H3.put_stuk(ph, 7) == "", "put 3D: zonder 3D de pixel-put")
	ph["met_3d"] = true
	H3.stukken.erase("put")
	ok(H3.put_stuk(ph, 7) == "", "put 3D: zonder stuk put in het blad de pixel-put")
	# put in de 3D-schatkamer (Olaf 14 nov, moet Daan 13:50): geen pixel-plank onder de troon
	H3.stukken["put"] = {"maat": [16, 16], "vak_px": [0, 0, 64, 64]}
	var sh := {"met_3d": true, "schat_kol": 14, "vallen": {12: "stekelput", 7: "stekelput"}, "put_open": {}, "upgrades": pu}
	pu.van_dict({"slijm": 0, "stekelput": 0})
	ok(H3.put_in_schatkamer(sh, 12, true) == "weg", "put schatkamer: dicht zonder stappen niet tekenen")
	ok(H3.put_in_schatkamer(sh, 7, true) == "" and H3.put_in_schatkamer(sh, 12, false) == "", "put schatkamer: buiten de 3D-schatkamer de gewone weg")
	sh["put_open"] = {12: 1.0}
	ok(H3.put_in_schatkamer(sh, 12, true) == "put", "put schatkamer: open na een klap het 3D-stuk (alleen de vloerstrook)")
	sh["put_open"] = {}
	pu.van_dict({"slijm": 0, "stekelput": 1})
	ok(H3.put_in_schatkamer(sh, 12, true) == "put_1", "put schatkamer: Rusty Spikes het eigen stuk")
	pu.van_dict({"slijm": 0, "stekelput": 3})
	ok(H3.put_in_schatkamer(sh, 12, true) == "weg", "put schatkamer: Trick Lid dicht niet tekenen")
	pu.van_dict({"slijm": 0, "stekelput": 2})
	ok(H3.put_in_schatkamer(sh, 12, true) == "put", "put schatkamer: Deep Pit zonder eigen stuk de 3D-put")
	pu.van_dict({"slijm": 0, "stekelput": 3})
	sh["put_open"] = {12: 1.0}
	ok(H3.put_in_schatkamer(sh, 12, true) == "put", "put schatkamer: Trick Lid open toont de stekels")
	H3.stukken.erase("put")
	ok(H3.put_in_schatkamer(sh, 12, true) == "", "put schatkamer: zonder 3D-stuk de pixel-put als terugval")
	H3.stukken["put"] = {"maat": [16, 16], "vak_px": [0, 0, 64, 64]}
	sh["put_open"] = {}
	var orr: Array = H3.onder_rects("put", Vector2(192, 24), 8)
	ok(orr[0] == Rect2(192, 32, 16, 8) and orr[1] == Rect2(0, 32, 64, 32), "put schatkamer: alleen de onderste 8 rijen, blad 4 keer zo groot: " + str(orr))
	var orr1: Array = H3.onder_rects("put", Vector2(192, 24), 8, 1)
	ok(orr1[0] == Rect2(193, 32, 14, 8) and orr1[1] == Rect2(4, 32, 56, 32), "put schatkamer: rand 1 haalt links en rechts een spelpixel weg (kan 1 Daan): " + str(orr1))
	var br: Array = H3.boven_rij(orr1, 4.0)
	ok(br[0] == Rect2(193, 32, 14, 1) and br[1] == Rect2(4, 32, 56, 4) and br[2] == Rect2(193, 33, 14, 7) and br[3] == Rect2(4, 36, 56, 28), "put schatkamer: bovenste rij los (half doorzichtig, kan 2 Daan): " + str(br))
	ok(H3.ZACHTE_RAND > 0.0 and H3.ZACHTE_RAND < 1.0, "put schatkamer: bovenste rij is half doorzichtig")
	H3.blad = oud_hblad
	H3.stukken = oud_stukken
	# versiering dunner (Olaf 14 nov, Daan 02:50 en 03:55): één per twee tegels, geen vloerding op het looppad, lichtzwam weg bij Gloop
	var HV = load("res://hol/hol_vast.gd")
	var nh := {"ingang_kol": 2, "schat_kol": 14, "vallen": {7: "stekelput"}}
	ok(HV.deco_hh(nh, 5, 20, 4) == 99, "deco: niets direct naast het vorige stuk")
	ok(HV.deco_hh(nh, 5, 5, 3) == 5, "deco: twee tegels verder mag weer (stut)")
	ok(HV.deco_hh(nh, 3, 20, -99) == 99, "deco: geen vloerding op de eerste tegel na de schacht")
	ok(HV.deco_hh(nh, 3, 10, -99) == 10, "deco: stut aan het plafond mag op de eerste tegel na de schacht")
	ok(HV.deco_hh(nh, 6, 20, -99) == 99 and HV.deco_hh(nh, 8, 24, -99) == 99, "deco: geen vloerding naast de val")
	ok(HV.deco_hh(nh, 8, 32, -99) == 32, "deco: spinrag naast de val mag")
	ok(HV.deco_hh(nh, 10, 21, -99) == 20 and HV.deco_hh(nh, 13, 16, -99) == 15, "deco: lichtzwam binnen twee van Gloop wordt paddenstoel")
	ok(HV.deco_hh(nh, 9, 21, -99) == 21, "deco: lichtzwam drie tegels van Gloop blijft")
	nh["deco_proef"] = true
	ok(HV.deco_hh(nh, 5, 20, 4) == 20, "deco: keurstrook houdt de vaste rij")
	var hdk = Node2D.new()
	hdk.set_script(load("res://hol/hol.gd"))
	var dicht := 0
	var stukken := 0
	for breed in [320, 480, 640]:
		hdk.maak(breed)
		hdk.leg_aan(breed / 16 - 4)
		var vk := -99
		for kk in range(hdk.ingang_kol + 1, hdk.schat_kol - 1):
			if hdk.vallen.has(kk):
				continue
			var hk: int = HV.deco_hh(hdk, kk, hdk._hash(kk, 7), vk)
			if hk < 30 or (hk < 36 and not hdk.boven[kk]):
				if kk - vk < 2:
					dicht += 1
				if hk >= 14 and hk < 30 and (kk == hdk.ingang_kol + 1 or hdk.vallen.has(kk - 1) or hdk.vallen.has(kk + 1)):
					dicht += 1   # vloerding op het looppad
				if hk >= 14 and hk < 30 and hk % 5 == 1 and absi(kk - (hdk.schat_kol - 2)) <= 2:
					dicht += 1   # lichtzwam bij Gloop
				stukken += 1
				vk = kk
	ok(dicht == 0 and stukken > 0, "deco in een echt hol: %d stukken, %d tegen de regels (naast elkaar, looppad, lichtzwam bij Gloop)" % [stukken, dicht])
	hdk.free()
	# vol hol (Olaf 16 nov, Mila "het hol moet vol"): vanaf 20 gangtegels elke vrije tegel een vloerding, plafond los
	var vgk := []
	var vbk := []
	for i in 40:
		vgk.append(i >= 1 and i <= 29)
		vbk.append(i in [4, 5, 9, 10, 15, 16, 21, 22])
	var vvh := {"ingang_kol": 1, "schat_kol": 29, "vallen": {7: "stekelput", 13: "stekelput"}, "gang": vgk, "boven": vbk}
	ok(HV.is_vol(vvh), "vol: 29 gangtegels is vol")
	var vklein := {"gang": vgk.slice(0, 15), "deco_proef": false}
	ok(not HV.is_vol(vklein), "vol: 14 gangtegels is niet vol (uitdunning van 14 nov blijft)")
	ok(not HV.is_vol({"gang": vgk, "deco_proef": true}), "vol: keurstrook houdt de vaste rij")
	ok(HV.vol_vloer(vvh, 2, -1) == -1, "vol: geen vloerding op de eerste tegel na de schacht")
	ok(HV.vol_vloer(vvh, 6, -1) == -1 and HV.vol_vloer(vvh, 7, -1) == -1 and HV.vol_vloer(vvh, 8, -1) == -1, "vol: niets op of naast een val")
	ok(HV.vol_vloer(vvh, 24, -1) == -1 and HV.vol_vloer(vvh, 27, -1) == -1, "vol: niets bij de hoeden en Gloop, en één tegel vrij ervoor")
	# Daan 16 nov 20:50 (Iris keuring 8): geen behang meer. Los ding (alles behalve de stut) hooguit op 1 van de 3 tegels,
	# nooit twee losse kolommen naast elkaar, nooit twee keer dezelfde soort na elkaar; stutten mogen regelmatig blijven.
	var vplafond := 0
	var vnaast := 0
	var vvp := -99
	for kk in range(2, 28):
		var p: int = HV.vol_plafond(vvh, kk, vvp)
		if p >= 0:
			if kk - vvp < 2 or vbk[kk]:
				vnaast += 1
			if p == 7 and (vvh.vallen.has(kk) or vvh.vallen.has(kk - 1) or vvh.vallen.has(kk + 1)) or kk >= 24:
				vnaast += 1   # geen stut op of naast een val, één tegel vrij voor de troon (Daan 16 nov, regel c)
			vplafond += 1
			vvp = kk
		if HV.vol_vloer(vvh, kk, -1) >= 0 and not HV.is_los(vvh, kk):
			vnaast += 1
	ok(vplafond > 0 and vnaast == 0, "vol: plafond nooit naast elkaar of onder een kamer, vloer alleen op losse kolommen (%d stuks, %d fout)" % [vplafond, vnaast])
	var vrij: Array = HV.vol_rij(vvh)
	var vgroot := {}
	var vgfout := 0
	var vlos_k := []
	var vlos_s := []
	var vstut := 0
	for dd in vrij:
		if dd[1] in HV.GROOT:
			if vgroot.has(dd[0] - 1) or vgroot.has(dd[0]) or vgroot.has(dd[0] + 1):
				vgfout += 1
			vgroot[dd[0]] = true
		if dd[1] == 7:
			vstut += 1
		elif HV.is_los(vvh, dd[0]):
			vlos_k.append(dd[0])
			vlos_s.append(dd[1])
	ok(vgfout == 0, "vol: %d grote dingen, %d naast of op een ander groot ding" % [vgroot.size(), vgfout])
	var vlfout := 0
	for i in range(1, vlos_k.size()):
		if vlos_k[i] - vlos_k[i - 1] < 2 or vlos_s[i] == vlos_s[i - 1]:
			vlfout += 1
	ok(vlos_k.size() >= 6 and vlfout == 0, "vol: %d losse dingen op 26 tegels, mis (naast elkaar of zelfde soort): %d, %s" % [vlos_k.size(), vlfout, str(vlos_s)])
	# Daan 16 nov 22:45 (moet): per drie tegels precies één los kolom, op wisselende plek, nooit twee naast elkaar
	var vblok_fout := 0
	var vnaast_los := 0
	var vplekken := {}
	for z in 40:
		var hz := {"ingang_kol": 1 + z, "schat_kol": 60 + z, "vallen": {}, "gang": [], "boven": []}
		var vorig_los := -99
		for bb in 19:
			var tel := 0
			for j in 3:
				var kk: int = hz.ingang_kol + 1 + bb * 3 + j
				if HV.is_los(hz, kk):
					tel += 1
					vplekken[j] = true
					if kk - vorig_los < 2:
						vnaast_los += 1
					vorig_los = kk
			if tel != 1:
				vblok_fout += 1
	ok(vblok_fout == 0 and vnaast_los == 0 and vplekken.size() == 3, "vol: per drie tegels precies een los, nooit naast elkaar, alle drie plekken komen voor (%d blokken mis, %d naast elkaar)" % [vblok_fout, vnaast_los])
	var hs := {"ingang_kol": 1, "schat_kol": 40, "vallen": {}, "gang": [], "boven": []}
	for kk in 42:
		hs.gang.append(kk >= 1 and kk <= 40)
		hs.boven.append(false)
	var vst := 0
	for dd in HV.vol_rij(hs):
		if dd[1] == 7:
			vst += 1
	ok(vst >= 3, "vol: stutten blijven regelmatig in een hol zonder kamers (%d op 38 tegels)" % vst)
	# Daan 16 nov 22:45 (moet): kamers losser, 0, 1 of 2 dingen, ongeveer de helft leeg, nooit twee na elkaar gelijk
	var vkd: Array = HV.kamer_dingen(vvh, false)
	var vkok := true
	for kd in vkd:
		if kd[1].y != HV.KAMER_VLOER or kd[0] == "lichtzwam":
			vkok = false
	ok(vkd.size() <= 8 and vkok, "vol: hooguit twee dingen per kamer, op de kamervloer, geen lichtzwam (%d)" % vkd.size())
	var vlos := vbk.duplicate()
	vlos[5] = false
	for kd in HV.kamer_dingen({"boven": vlos, "ingang_kol": 1, "schat_kol": 29}, false):
		if int(kd[1].x) / 16 == 4 or int(kd[1].x) / 16 == 5:
			vkok = false
	ok(vkok, "vol: een losse kamer (kamer_los) krijgt niets extra")
	var vk_leeg := 0
	var vk_tot := 0
	var vk_gelijk := 0
	for z in 30:
		var kb := []
		for kk in 66:
			kb.append(kk >= 3 and kk < 60 and ((kk + z) % 3) != 2)   # kamers van twee kolommen, verschoven per z
		var kh := {"boven": kb, "ingang_kol": 1, "schat_kol": 63}
		var vk_per := {}
		for kd in HV.kamer_dingen(kh, false):
			var kol: int = int(kd[1].x) / 16
			var start: int = kol if kb[kol + 1] and not kb[kol - 1] else kol - 1   # links: a * 16 + 10, rechts: b * 16
			if not vk_per.has(start):
				vk_per[start] = []
			vk_per[start].append(kd[0] + ("L" if kol == start else "R"))
		var vorige_i := "x"
		for kk in range(4, 58):
			if not (kb[kk] and kb[kk + 1] and not kb[kk - 1]):
				continue
			var inr: String = ",".join(vk_per.get(kk, []))
			vk_tot += 1
			if inr == "":
				vk_leeg += 1
			if inr == vorige_i:
				vk_gelijk += 1
			vorige_i = inr
	ok(vk_gelijk == 0 and vk_leeg * 100 >= vk_tot * 30 and vk_leeg * 100 <= vk_tot * 55, "vol: kamers %d van %d leeg, %d keer twee na elkaar gelijk" % [vk_leeg, vk_tot, vk_gelijk])
	# hoedenwand (Olaf 16 nov, Mila punt 4): vaste plekken boven de gang, nooit naast elkaar, niet bij schacht en stapel
	var wvh := {"ingang_kol": 1, "schat_kol": 29, "max_kol": 9999, "gang": vgk, "boven": vbk}
	var wp: Array = HV.wand_plekken(wvh, true)
	var wkol := {}
	var wfout := 0
	for p in wp:
		var kk: int = int(p.x) / 16
		if vbk[kk] or kk <= 2 or kk >= 25 or p.y < HV.WAND_Y_MIN or p.y > HV.WAND_Y_MAX:
			wfout += 1
		wkol[kk] = p
	var wpaar := 0
	for kk in wkol:
		if wkol.has(kk + 1):
			wpaar += 1
			if wkol.has(kk + 2) or absf(wkol[kk].y - wkol[kk + 1].y) < 3:
				wfout += 1   # nooit drie op een rij, een paar op duidelijk andere hoogte
	var whoog := {}
	for p in wp:
		whoog[p.y] = true
	ok(wp.size() >= 5 and wfout == 0, "wand: %d plekken, %d tegen de regels (kamer, schacht, stapel, hoogte, drietal)" % [wp.size(), wfout])
	ok(whoog.size() >= 3, "wand: geen vast ritme, %d verschillende hoogtes, %d paren (Daan 16 nov)" % [whoog.size(), wpaar])
	ok(HV.wand_plekken(wvh, true) == wp, "wand: zelfde plekken bij opnieuw tekenen (vast, groeit zonder verschuiven)")
	var wvh2 := wvh.duplicate()
	wvh2["max_kol"] = 12
	ok(HV.wand_plekken(wvh2, true).size() < wp.size(), "wand: niet voorbij max_kol (onder het paneel)")
	# graafmoment in 3D (Daan 14 nov): beeld 0 tot 3 over GRAAF_S, keurstrook zet vier kamers stil in elk beeld
	var HG = load("res://hol/hol.gd")
	ok(HG.graaf_beeld(0.0) == 0 and HG.graaf_beeld(HG.GRAAF_S * 0.3) == 1 and HG.graaf_beeld(HG.GRAAF_S * 0.6) == 2 \
		and HG.graaf_beeld(HG.GRAAF_S * 0.99) == 3 and HG.graaf_beeld(9.0) == 3, "graaf: beelden 0 tot 3 over de graaftijd")
	var hg = Node2D.new()
	hg.set_script(HG)
	hg.maak(640)
	hg.leg_aan(640 / 16 - 4)
	hg.graaf_proef = true
	hg.zet_graaf_proef()
	var gb := []
	for c in hg.brokkel:
		if c.y == 0:
			gb.append(HG.graaf_beeld(hg.brokkel[c]))
	ok(gb.size() == 4 and gb.has(0) and gb.has(1) and gb.has(2) and gb.has(3), "graaf: keurstrook heeft vier kamers in beeld 0 tot 3 (%s)" % [gb])
	ok(hg.graaf_rij_proef.values().has(1) and hg.graaf_rij_proef.values().has(2), "graaf: keurstrook heeft een gangcel open naar links en een naar rechts")
	var nb: int = hg.brokkel.size()
	hg._process(5.0)
	ok(hg.brokkel.size() == nb and nb >= 4, "graaf: de keurstrook-cellen blijven staan")
	# rij van het graafblad (kan Daan 14 nov 09:35): kamer open naar onder, gangcel open naar de buur die al gang was
	var gr := [true, true, false, false, true, true]
	ok(HG.graaf_rij(Vector2i(2, 0), gr) == 3, "graaf: kamer boven de gang is open naar onder")
	ok(HG.graaf_rij(Vector2i(2, 1), [true, true, true, false]) == 1, "graaf: gangcel met open buur links is open naar links")
	ok(HG.graaf_rij(Vector2i(3, 1), gr) == 2 and HG.graaf_rij(Vector2i(0, 1), [true, true]) == 2, "graaf: gangcel met open buur rechts is open naar rechts (ook in kolom 0)")
	ok(HG.graaf_rij(Vector2i(1, 1), [true, true, true]) == 0 and HG.graaf_rij(Vector2i(5, 1), gr) == 1, "graaf: beide buren open geeft het midden; laatste kolom kijkt alleen links")
	ok(ResourceLoader.exists(HG.GRAAF3D_PAD) and hg.GRAAF3D != null, "graaf: 3D-blad geladen")
	# graafstippels als 3D-kiezeltjes (Bram 14 nov, Daan 13:42): blad met 2 vakken van 12 x 64
	ok(ResourceLoader.exists(HV.STIP3D_PAD) and HV.STIP3D != null and HV.STIP3D.diffuse_texture.get_size() == Vector2(24, 64), "graafstip: 3D-blad geladen, 24 x 64")
	hg.free()
	# muntje boven Gloop volgt hoogste_punt_rust() als slijm.gd die heeft (torenplafond, Olaf 14 nov), anders de oude som
	var KJ = load("res://kern/kaartje.gd")
	var nep_s := GDScript.new()
	nep_s.source_code = "extends RefCounted\nvar slijm\n"
	nep_s.reload()
	var nep_rust := GDScript.new()
	nep_rust.source_code = "extends Node2D\nvar plat := false\nfunc is_plat() -> bool:\n\treturn plat\nfunc hoogste_punt_rust() -> int:\n\treturn -30\n"
	nep_rust.reload()
	var nep_oud := GDScript.new()
	nep_oud.source_code = "extends Node2D\nfunc is_plat() -> bool:\n\treturn false\n"
	nep_oud.reload()
	var ms = nep_s.new()
	var sl_r = nep_rust.new()
	sl_r.position = Vector2(0, 40)
	ms.slijm = sl_r
	ok(is_equal_approx(KJ.munt_top(ms), 10.0), "munt_top volgt hoogste_punt_rust: %s" % str(KJ.munt_top(ms)))
	sl_r.plat = true
	ok(is_equal_approx(KJ.munt_top(ms), 34.0), "munt_top plat blijft de platte kruin")
	# keurstand figuur=<factor> (Olaf 15 nov, kan-punt controleur): het muntje schaalt mee met Gloop, voetpunt gelijk
	sl_r.scale = Vector2.ONE * 1.15
	ok(is_equal_approx(KJ.munt_top(ms), 40.0 - 6.0 * 1.15), "munt_top plat met figuur 1,15: %s" % str(KJ.munt_top(ms)))
	sl_r.plat = false
	ok(is_equal_approx(KJ.munt_top(ms), 40.0 - 30.0 * 1.15), "munt_top met figuur 1,15 volgt de grotere toren: %s" % str(KJ.munt_top(ms)))
	sl_r.scale = Vector2.ONE
	var sl_o = nep_oud.new()
	sl_o.position = Vector2(0, 40)
	ms.slijm = sl_o
	ok(is_equal_approx(KJ.munt_top(ms), 30.0), "munt_top zonder hoogste_punt_rust: oude som (rust-frame)")
	sl_r.free()
	sl_o.free()
	# muisvlak volgt wat er boven het maaiveld staat (Olaf 14 nov; op Windows tekent alleen het vlak, Bram 02:35)
	var h2 = Node2D.new()
	h2.set_script(load("res://hol/hol.gd"))
	h2.scale = Vector2(3, 3)
	h2.maak(320)
	h2.leg_aan(15)
	var rimg := Image.create(6, 30, false, Image.FORMAT_RGBA8)
	rimg.fill(Color(0, 0, 0, 0))
	rimg.fill_rect(Rect2i(0, 24, 6, 6), Color(0.3, 0.2, 0.3, 1))   # aarde vanaf het maaiveld (rij 8 x schaal 3)
	rimg.fill_rect(Rect2i(2, 5, 1, 19), Color(0.2, 0.6, 0.2, 1))    # een spriet tot pixel 5
	rimg.set_pixel(4, 10, Color(1, 1, 1, 0.02))                     # bijna onzichtbaar: telt niet
	rimg.set_pixel(5, 0, Color(1, 1, 1, 0.5))                       # zachte 3D-rand: telt wel
	h2.vast.lees_rand(rimg, 3)
	var rr: PackedInt32Array = h2.vast.rand
	ok(rr.size() == 6 and rr[0] == 24 and rr[2] == 5 and rr[4] == 24 and rr[5] == 0, "hol_vast: bovenrand per kolom gemeten %s" % str(rr))
	# kan van de controleur (14 nov 02:35): munt_top met de echte slijm.gd, hoge toren tegen het plafond
	if ResourceLoader.exists("res://systemen/slijm.gd"):
		var ms2 = nep_s.new()
		var echt = Node2D.new()
		echt.set_script(load("res://systemen/slijm.gd"))
		echt.zet(h2, 10)
		for i in 12:
			echt.krijg_hoed(i % 10)
		ms2.slijm = echt
		var mt: float = KJ.munt_top(ms2)
		ok(is_equal_approx(mt, echt.position.y + float(echt.hoogste_punt_rust())), "munt_top met echte slijm.gd en 12 hoeden volgt hoogste_punt_rust (%s)" % str(mt))
		ok(mt >= echt.position.y + echt.plafond_y() - 1.0, "toren van 12 hoeden blijft onder het plafond (%s tegen %s)" % [str(mt), str(echt.position.y + echt.plafond_y())])
		echt.free()
	h2.free()
	# paneel in de 3D-stijl (Olaf 14 nov, Daan ronde 2): Fredoka met gewicht, 3D-bron, terugval naar het pixelpaneel
	var TKS = load("res://kern/tekst.gd")
	ok(TKS.met_3d, "paneel 3D: schakelaar staat aan")
	ok(TKS.PANEEL_3D.get_width() == 384 and TKS.BRON_RAND == 128, "paneel 3D: bron 384 px met rand 128")
	var tk = Node2D.new()
	tk.set_script(TKS)
	var f6: Font = tk._letter(600)
	ok(f6 is FontVariation and f6.base_font == TKS.FREDOKA and tk._letter(600) == f6, "paneel 3D: Fredoka 600, één keer gemaakt")
	ok(tk._letter(450) != f6, "paneel 3D: tekst 450 is een eigen letter")
	ok(f6.get_string_size("Buy  45", HORIZONTAL_ALIGNMENT_LEFT, -1, 13).x > 20, "paneel 3D: Fredoka meet tekst")
	var d1: StyleBoxFlat = tk._doos("knop")
	ok(tk._doos("knop") == d1 and d1.border_color == Color("#e8b040"), "paneel 3D: knop-StyleBox één keer gemaakt en bewaard")
	ok(tk._doos("paneel_schaduw") != d1 and tk._doos("paneel_schaduw").shadow_offset == Vector2(1, 3), "paneel 3D: schaduw is een eigen doos, offset 1,3")
	# Daan ronde 3 (14 nov): op 160 groter, 120 gelijk, 96 knop 2 px hoger; knop houdt 8 px tot de gouden binnenrand
	tk.schaal = 4; tk.hoogte = 160.0
	var m160: Dictionary = tk.maten()
	ok(m160.kop == 18 and m160.tekst == 15 and m160.knop == 16 and m160.knop_h == 28.0, "paneel r3: op 160 kop 18, tekst 15, knop 16 en 28 hoog")
	var ky160: float = tk.hoogte - int(m160.onder) - int(m160.regel_h) * 4 + int(m160.regel_h) * 2 + int(m160.knop_dy)
	var rand160: float = tk.hoogte - 4.0 - 31.0 / 128.0 * roundf(4.5 * tk.schaal)   # binnenkant goud: 31 bronpixels vanaf de rand
	ok(rand160 - (ky160 + m160.knop_h) >= 8.0, "paneel r3: op 160 minstens 8 px tussen knop en goud (%s)" % str(rand160 - (ky160 + m160.knop_h)))
	ok(tk.hover_vak().position.y == 54.0, "paneel r3: op 160 blijft het paneel even hoog (top 54)")
	tk.schaal = 3; tk.hoogte = 120.0
	var m120: Dictionary = tk.maten()
	ok(m120.kop == 13 and m120.tekst == 13 and m120.uitleg == 12 and m120.knop_dy == 3 and m120.onder == 15 and m120.boven == 13 and m120.kop_dy == 0, "paneel r3: op 120 alles gelijk")
	tk.schaal = 2; tk.hoogte = 96.0
	ok(tk.maten().knop_dy == 1 and tk.maten().kop == 12, "paneel r3: op 96 knop 2 px hoger, letter 12")
	# bouwblad D (Sanne 25 nov, #19): dicht bord groot (hoofdletters 0,7 em: op 120 minstens 12 px), regel weg na 6 s
	tk.schaal = 3; tk.hoogte = 120.0
	ok(tk.bord_maten().tekst * 0.7 >= 12.0 and tk.bord_maten().kop == 18 and tk.maten().tekst == 13, "bord D: op 120 letter 18 (hoofdletter 12,6 px), kaartje en hover houden 13")
	tk.schaal = 4; tk.hoogte = 160.0
	ok(tk.bord_maten().tekst == 24 and tk.maten().tekst == 15, "bord D: op 160 letter 24")
	tk.schaal = 2; tk.hoogte = 96.0
	ok(tk.bord_maten().tekst == 15 and 96 - int(tk.bord_maten().onder) - tk.bord_maten().regel_h * 2 - int(tk.bord_maten().boven) >= 96 * 0.3, "bord D: op 96 letter 15 en het bord laat het gras vrij")
	ok(TKS.regel_zicht(0.0) == 1.0 and TKS.regel_zicht(5.3) == 1.0 and TKS.regel_zicht(5.7) > 0.0 and TKS.regel_zicht(5.7) < 1.0 and TKS.regel_zicht(6.0) == 0.0 and TKS.regel_zicht(60.0) == 0.0, "bord D: regel 5,4 s vol, dan zacht weg, op 6 s weg")
	var rz: Array[String] = ["Kees fell in."]
	tk.zet(rz, 5)
	ok(tk.regel_sinds == 0.0, "bord D: nieuwe regel begint opnieuw")
	tk.regel_sinds = 4.0
	tk.zet(rz, 9)
	ok(tk.regel_sinds == 4.0, "bord D: alleen meer goud zet de klok niet terug")
	var rz2: Array[String] = ["Kees fell in.", "Kees fell in."]
	tk.zet(rz2, 9)
	ok(tk.regel_sinds == 0.0, "bord D: dezelfde tekst als nieuwe regel telt wel als nieuw")
	tk.schaal = 2; tk.hoogte = 96.0
	TKS.met_3d = false
	ok(tk.maten().knop_dy == 3, "paneel r3 uit: oude knopplek")
	tk.schaal = 4; tk.hoogte = 160.0
	ok(tk.maten().kop == 13, "paneel r3 uit: op 160 de oude maat")
	ok(tk._letter(600) == ThemeDB.fallback_font, "paneel 3D uit: de oude letter")
	TKS.met_3d = true
	tk.free()
	# goudmuntjes in de 3D-stijl (Daan 14 nov 06:40): vliegend en koopmuntje rond als het paneelmuntje, draaien door in te drukken
	var HS = load("res://hol/hol.gd")
	ok(is_equal_approx(HS.munt_draai(0.0), 1.0) and is_equal_approx(HS.munt_draai(1.0), 1.0), "munt 3D: plat voor je bij hele slag")
	ok(is_equal_approx(HS.munt_draai(0.5), 0.3), "munt 3D: op zijn kant nooit dunner dan 0,3")
	var mmin := 1.0
	for i in 31:
		mmin = minf(mmin, HS.munt_draai(i / 10.0))
	ok(mmin >= 0.3 - 0.0001, "munt 3D: draai blijft tussen 0,3 en 1")
	# leven in het spel, punt 1 (hoofdchat 15 nov): muntjes op de schat stuiteren na, naast elkaar; naar een gekocht ding niet
	var mv := {"van": 20.0, "t": 0.0, "dx": -3.0}
	ok(is_equal_approx(HS.munt_duur(mv), HS.MUNT_S + HS.STUIT_S), "munt stuitert: leeft vliegen plus stuiteren")
	ok(is_equal_approx(HS.munt_duur({"van": 0.0, "naar": 9.0, "t": 0.0}), HS.MUNT_S), "munt naar gekocht ding: stuitert niet")
	mv.t = HS.MUNT_S
	var ml: Vector3 = HS.munt_plek(mv, 100.0, 50.0)
	ok(is_equal_approx(ml.x, 99.0) and is_equal_approx(ml.y, 44.0), "munt landt half op dx naast het midden op de vloer, hele spelpixel: %s" % str(ml))
	var hoogst := 0.0
	var omhoog := 0
	var vorig := 44.0
	var heel := true
	for i in 41:
		mv.t = HS.MUNT_S + HS.STUIT_S * i / 40.0
		var q: Vector3 = HS.munt_plek(mv, 100.0, 50.0)
		if q.y > 44.0 + 0.0001:
			ok(false, "munt stuitert nooit door de vloer (%s)" % str(q))
		hoogst = maxf(hoogst, 44.0 - q.y)
		if q.y < vorig and vorig >= 44.0:
			omhoog += 1
		vorig = q.y
		if not is_equal_approx(q.x, round(q.x)) or not is_equal_approx(q.y, round(q.y)):
			heel = false
	ok(is_equal_approx(hoogst, 3.0) and omhoog == 1, "munt stuitert één keer, 3 spelpixels hoog (Daan: 30%%): %.2f, %d keer" % [hoogst, omhoog])
	ok(heel, "munt stuitert op hele spelpixels")
	mv.t = HS.MUNT_S + 0.02
	ok(HS.munt_glinstert(mv), "munt glinstert bij de landing")
	mv.t = HS.MUNT_S + 0.1
	ok(not HS.munt_glinstert(mv) and not HS.munt_glinstert({"van": 0.0, "naar": 9.0, "t": HS.MUNT_S + 0.02}), "glinster maar één beeld, en niet bij kopen")
	mv.t = HS.MUNT_S + HS.STUIT_S
	var me: Vector3 = HS.munt_plek(mv, 100.0, 50.0)
	ok(is_equal_approx(me.x, 97.0) and is_equal_approx(me.y, 44.0) and is_equal_approx(me.z, 0.3), "munt ligt aan het eind op dx en op zijn kant: %s" % str(me))
	var dxs := {}
	for d in HS.MUNT_DX.slice(0, 3):
		dxs[d] = true
	ok(dxs.size() == 3, "de drie muntjes van een val landen op drie plekken")
	# leven in het spel, punt 4 (hoofdchat 15 nov): de fakkelgloed flakkert zacht, de twee fakkels niet gelijk
	var fl_min := 1.0
	var fl_max := 0.0
	var gelijk := 0
	for a in 14:
		var f0: Vector2 = HS.fakkel_flakker(a, 0)
		fl_min = minf(fl_min, f0.x)
		fl_max = maxf(fl_max, f0.x)
		if is_equal_approx(f0.x, HS.fakkel_flakker(a, 1).x):
			gelijk += 1
	ok(fl_min >= 0.18 - 0.0001 and fl_max <= 0.32 + 0.0001 and fl_max - fl_min > 0.11, "fakkel flakkert tussen 0,18 en 0,32 alfa (Daan 15 nov 16:40) (%.2f tot %.2f)" % [fl_min, fl_max])
	var sprong := 0.0
	for a in 24:
		sprong = maxf(sprong, absf(HS.fakkel_flakker(a + 1, 0).y - HS.fakkel_flakker(a, 0).y))
	ok(sprong <= 0.15 * 0.36, "fakkel: zachte overgang, maat springt per beeld hooguit een derde van 0,85 tot 1 (%.3f)" % sprong)
	ok(is_equal_approx(HS.fakkel_flakker(7, 0).y, 0.85) and is_equal_approx(HS.fakkel_flakker(3, 0).y, 1.0), "fakkel: sterkte tussen 0,85 en 1 (Daan juice.md)")
	ok(gelijk == 0, "de twee fakkels flakkeren niet gelijk")
	# issue #79, tempo-regel 1: ook in een leeg hol flakkert de vlam zelf, rustig en zonder sprong (Daan #80: de vlam
	# uit de 3D-render zelf, rekt alleen, krimpt nooit onder zijn eigen maat, dus geen stokje dat aan en uit springt)
	var BT = load("res://kern/beeldtempo.gd")
	var vl_min := 99.0
	var vl_max := 0.0
	var vl_sprong := 0.0
	var zw_max := 0.0
	for a in 24:
		var fa: float = HS.FLAKKER[a % HS.FLAKKER.size()]
		var fb: float = HS.FLAKKER[(a + 1) % HS.FLAKKER.size()]
		vl_min = minf(vl_min, H3.vlam_schaal(fa))
		vl_max = maxf(vl_max, H3.vlam_schaal(fa))
		vl_sprong = maxf(vl_sprong, absf(H3.vlam_schaal(fb) - H3.vlam_schaal(fa)))
		zw_max = maxf(zw_max, absf(H3.vlam_zwaai(fa)))
	ok(vl_min >= 1.0 and vl_max - vl_min >= 0.12, "vlam: rekt minstens 12 procent en krimpt nooit onder zijn maat (%.2f tot %.2f)" % [vl_min, vl_max])
	ok(vl_sprong <= 0.06, "vlam: per beeld hooguit 6 procent verschil, geen knipperen (%.2f)" % vl_sprong)
	ok(zw_max > 0.2 and zw_max <= 0.36, "vlam: punt wiegt hooguit een derde spelpixel (%.2f)" % zw_max)
	ok(BT.fakkel_tempo(0) > 0.0 and BT.fakkel_tempo(0) <= 3.0 and BT.fakkel_tempo(1) == 6.0, "fakkels: leeg hol 3 beeldjes per s (rustig), met held 6")
	# winkelbeeld moment=val (Bram 15 nov): bij de eerste val blijven de muntjes in hun boog hangen
	var hmv = Node2D.new()
	hmv.set_script(HS)
	hmv.moment_munt = true
	hmv.munt_regen(2)
	for i in 40:
		hmv._process(0.05)
	var tm: Array = hmv.munten.map(func(m): return float(m.t))
	ok(hmv.moment_val_vast and hmv.munten.size() == 3 and tm.min() >= HS.MUNT_S * 0.5 - 0.0001 and tm.max() < HS.MUNT_S, "moment=munt: na 2 s hangen drie muntjes in de lucht (%s)" % str(tm))
	hmv.munt_regen(5)
	ok(hmv.munten.size() == 3, "moment staat stil: geen nieuwe muntjes meer")
	hmv.free()
	var hm = Node2D.new()
	hm.set_script(HS)
	ok(hm.met_3d == true and hm.has_method("munt_3d"), "munt 3D: hol tekent munten rond als met_3d aan staat")
	hm.free()
	# koopmuntje boven Deep Pit hoger (stekels staken erin, Olaf 14 nov), andere putstukken op de oude plek
	ok(HS.munt_boven_put("put_2") == 3.0, "koopmuntje: boven put_2 3 spelpixels hoger")
	ok(HS.munt_boven_put("put_1") == 0.0 and HS.munt_boven_put("put") == 0.0 and HS.munt_boven_put("") == 0.0, "koopmuntje: andere putten oude plek")
	# save van een breder scherm schuift naar het tekstvak (kan Daan 14 nov 22:40, Olaf): week-save op 1920 (schat 29),
	# opname op 1280 bij 160 px (max_kol 12, 20 kolommen): niets meer rechts van de schat, putten mee geschoven
	var OP = load("res://kern/opslag.gd")
	var wg := []
	var wb := []
	for i in 40:
		wg.append(i >= 1 and i <= 29)
		wb.append(i in [4, 5, 9, 10, 15, 16, 21, 22])
	var sw: Dictionary = OP.schuif_naar_vak(wg, wb, {"7": "stekelput", "13": "stekelput", "19": "stekelput"}, 29, 2, 12, 20)
	ok(sw.schat_kol == 12 and sw.schuif == -17 and sw.ingang_kol == 1, "save schuift: schat 12, 17 naar links, ingang 1 (%s)" % [sw.schat_kol])
	var rechts_leeg := true
	for kr in range(13, 20):
		rechts_leeg = rechts_leeg and not sw.gang[kr] and not sw.boven[kr]
	ok(rechts_leeg, "save schuift: rechts van de schat geen gang of kamer (onder het paneel)")
	ok(sw.vallen.size() == 1 and sw.vallen.has(2), "save schuift: alleen de put van 19 blijft, op 2 (%s)" % [sw.vallen])
	ok(sw.boven[4] and sw.boven[5] and not sw.boven[3], "save schuift: kamers 21 en 22 op 4 en 5")
	ok(not sw.gang[0] and sw.gang[1] and sw.gang[12], "save schuift: gang van 1 tot de schat")
	var sz: Dictionary = OP.schuif_naar_vak(wg, wb, {"7": "stekelput"}, 29, 2, 29, 40)
	ok(sz.schuif == 0 and sz.gang == wg.map(func(x): return x) and sz.vallen.has(7) and sz.ingang_kol == 2, "save schuift niet als het scherm gelijk is")
	var sr: Dictionary = OP.schuif_naar_vak(wg.slice(0, 20), wb.slice(0, 20), {"7": "stekelput"}, 12, 2, 15, 24)
	ok(sr.schuif == 3 and sr.schat_kol == 15 and sr.ingang_kol == 5 and sr.vallen.has(10) and sr.gang[5] and not sr.gang[16], "save schuift naar rechts als er meer ruimte is")
	var sl: Dictionary = OP.schuif_naar_vak(wg, wb, {"7": "stekelput"}, 29, 2, 12, 20)
	ok(sl.vallen.size() == 1 and sl.vallen.has(6), "save schuift: alle vallen weg, dan één terug zoals leg_aan (%s)" % [sl.vallen])
	var sk: Dictionary = OP.schuif_naar_vak(wg, wb, {}, 29, 2, 25, 30)
	ok(not sk.boven[0], "save schuift: geen kamer op kolom 0")
	# eerste hoed binnen de minuut in het volle spel (Bram 15 nov, ja Olaf 23:30, eis 1 en 2): kern/ritme.gd met een
	# nagebootste strook. Echte spel (Linux, vers=1, 5 zaden, 15 nov): hap 59 tot 62 s, de held loopt ±17 s van de
	# ingang naar Gloop; dus aankomst van de held van "opgegeten" uiterlijk 52 s houdt de hap onder 75 s.
	var RI = load("res://kern/ritme.gd")
	var nep := GDScript.new()
	nep.source_code = """extends RefCounted
var t := 0.0
var volgende_held := 4.0
var demo := false
var lied_helden := 0
var rng := RandomNumberGenerator.new()
var begin_gedaan: Array = []
var aankomst := {}
const LIJST := ["vallen", "opgegeten", "vluchten", "terug", "doorlopen"]
func _begin_stap() -> String:
	for st in LIJST:
		if not begin_gedaan.has(st):
			return st
	return ""
func _nieuwe_held() -> bool:
	var st := _begin_stap()
	aankomst[st if st != "" else "vrij%d" % aankomst.size()] = t
	if st != "":
		begin_gedaan.append(st)
	return true
"""
	nep.reload()
	var laatst_opgegeten := 0.0
	var gat_na_opgegeten_ok := true
	var gat_na_vluchten_ok := true
	for zaad in 40:
		var ns = nep.new()
		ns.rng.seed = zaad
		while ns.t < 200.0:
			RI.tik_held(ns, 0)
			ns.t += 0.25
		laatst_opgegeten = maxf(laatst_opgegeten, float(ns.aankomst.get("opgegeten", 999.0)))
		var gat: float = float(ns.aankomst.get("vluchten", 0.0)) - float(ns.aankomst.get("opgegeten", 0.0))
		gat_na_opgegeten_ok = gat_na_opgegeten_ok and gat >= 18.0 and gat <= 22.5
		var gat2: float = float(ns.aankomst.get("terug", 0.0)) - float(ns.aankomst.get("vluchten", 0.0))
		gat_na_vluchten_ok = gat_na_vluchten_ok and gat2 >= 28.0 and gat2 <= 38.5
	# Bram 16 nov (hoofdchat, Fenna): "opgegeten" is nu de tweede held, 5 tot 7 s na de eerste. Echte spel (Linux, vers=1,
	# zaden 1 tot 3): hap op 26,3 tot 27,8 s. Aankomst uiterlijk 13 s houdt de hap rond 30 s.
	ok(laatst_opgegeten <= 13.0, "eerste hoed: held van 'opgegeten' uiterlijk 13 s binnen in 40 zaden (laatste %.1f s), hap rond 30 s" % laatst_opgegeten)
	ok(gat_na_opgegeten_ok, "eerste hoed: na 'opgegeten' 18 tot 22 s tot 'vluchten'")
	ok(gat_na_vluchten_ok, "eerste hoed: na 'vluchten' weer 28 tot 38 s tot de volgende held (Sanne 16 nov 20:00, was 35 tot 45)")
	# Sanne 16 nov 20:00 en 20:10: na het begin 28 tot 38 s, ±15% kans op een paar (6 tot 10 s), hooguit 2 helden tegelijk
	var gaten_ok := true
	var paren := 0
	var vrij_gaten := 0
	for zaad in range(1, 41):
		var nr = nep.new()
		nr.rng.seed = zaad
		while nr.t < 900.0:
			RI.tik_held(nr, 0)
			nr.t += 0.25
		var tijden: Array = []
		for sl_ in nr.aankomst:
			if String(sl_).begins_with("vrij"):
				tijden.append(float(nr.aankomst[sl_]))
		tijden.sort()
		tijden.push_front(float(nr.aankomst.get("doorlopen", 0.0)))
		for i in range(1, tijden.size()):
			var g: float = tijden[i] - tijden[i - 1]
			vrij_gaten += 1
			if g >= 6.0 and g <= 10.5:
				paren += 1
			elif g < 28.0 or g > 38.5:
				gaten_ok = false
	var paar_deel := float(paren) / maxf(1.0, float(vrij_gaten))
	ok(gaten_ok, "ritme na het begin: elk gat 28 tot 38 s of een paar van 6 tot 10 s")
	ok(paar_deel > 0.10 and paar_deel < 0.20, "ritme: ±15%% van de gaten is een paar (%.1f%% van %d)" % [paar_deel * 100.0, vrij_gaten])
	var nv = nep.new()
	nv.t = 999.0
	nv.volgende_held = 0.0
	RI.tik_held(nv, 2)
	ok(nv.volgende_held == 0.0, "gewoon spel: met 2 helden in beeld komt er geen derde (Sanne 16 nov 20:10)")
	nv.demo = true
	RI.tik_held(nv, 2)
	ok(nv.volgende_held > 999.0, "demo: met 2 helden mag er nog een derde komen")
	var nd = nep.new()
	nd.demo = true
	nd.rng.seed = 3
	while nd.t < 30.0:
		RI.tik_held(nd, 0)
		nd.t += 0.25
	ok(float(nd.aankomst.get("opgegeten", 999.0)) <= 4.0 + 3 * 7.25, "eerste hoed: demo houdt zijn eigen ritme van 5 tot 7 s")
	# kroniek (Iris keuring 1, 16 nov): een weggedrukte lied-regel komt alleen terug binnen 4 s; "op" vervalt niet
	var WR = load("res://kern/wachtrij.gd")
	var nep_k := GDScript.new()
	nep_k.source_code = "extends RefCounted\nvar wachtrij: Array = []\nvar t := 0.0\nvar regel_sinds := -99.0\nvar regel_binnen := false\nvar regel_nu := {}\nvar kroniek: Array[String] = []\nvar log: Array[String] = []\nvar tekst = null\nvar namen_recent: Array = []\nvar hol = null\nfunc log_regel(r: String) -> void:\n\tlog.append(r)\n"
	nep_k.reload()
	var nep_tekst := GDScript.new()
	nep_tekst.source_code = "extends RefCounted\nfunc zet(_r, _g) -> void:\n\tpass\n"
	nep_tekst.reload()
	var nk = nep_k.new()
	nk.tekst = nep_tekst.new()
	nk.hol = {"goud": 0}
	nk.wachtrij.append({"r": "SONG", "binnen": true, "sinds": 0.0, "soort": "lied"})
	WR.toon(nk)
	nk.t = 1.0
	nk.wachtrij.append({"r": "EVENT1", "binnen": false, "sinds": 1.0, "soort": ""})
	WR.toon(nk)   # lied stond 1 s, wordt weggedrukt en komt terug
	# daarna een rij gebeurtenissen van 10 s: de terugkomer moet vervallen in plaats van op 11 s terug te komen
	for i in 4:
		nk.t = 1.0 + 2.5 * (i + 1)
		nk.wachtrij.append({"r": "EVENT%d" % (i + 2), "binnen": false, "sinds": nk.t, "soort": ""})
		WR.toon(nk)
	nk.t = 14.0
	WR.toon(nk)
	ok(nk.log.filter(func(r): return r.ends_with("): SONG")).size() == 1 and not nk.wachtrij.any(func(w): return w.r == "SONG"), "kroniek: lied na 10 s wachten komt niet terug (Iris)")
	var nk2 = nep_k.new()
	nk2.tekst = nep_tekst.new()
	nk2.hol = {"goud": 0}
	nk2.wachtrij.append({"r": "OP", "binnen": true, "sinds": 0.0, "soort": "op"})
	nk2.regel_sinds = 0.0
	nk2.regel_nu = {"r": "X"}
	for i in 3:
		nk2.t = 1.0 + 2.5 * i
		nk2.wachtrij.append({"r": "E%d" % i, "binnen": false, "sinds": nk2.t, "soort": ""})
		WR.toon(nk2)
	nk2.t = 12.0
	WR.toon(nk2)
	nk2.t = 15.0
	WR.toon(nk2)
	ok(nk2.kroniek.has("OP"), "kroniek: 'up again' vervalt niet achter gebeurtenissen (Iris)")
	# Iris keuring 16 punt 2 (Olaf 17 nov): regels van vóór het weggaan niet meer op het kaartje
	var tel_w := "115 came, 74 fell, 39 hats. +559 gold."
	var kr_w: Array[String] = ["Odo fell.", "Joost climbs into your hole.", "Tibbe fled twice.", tel_w]
	var wr_w: Array[String] = ["Tibbe fled twice.", tel_w]
	ok(str(TKS.kies_toon(kr_w, tel_w, wr_w, tel_w, 3, true)) == str([tel_w, "Tibbe fled twice."]), "kaartje na weg: oude regel (Joost) niet onder de telling: %s" % str(TKS.kies_toon(kr_w, tel_w, wr_w, tel_w, 3, true)))
	kr_w.append("Kees brought a torch.")
	ok(str(TKS.kies_toon(kr_w, tel_w, wr_w, tel_w, 3, true)) == str([tel_w, "Tibbe fled twice.", "Kees brought a torch."]), "kaartje na weg: nieuwe regel na de telling telt wel")
	ok(str(TKS.kies_toon(kr_w, "", wr_w, tel_w, 3, true)) == str(["Tibbe fled twice.", tel_w, "Kees brought a torch."]), "na de eerste nieuwe held (vast leeg): nog steeds geen oude regel")
	var kr_g: Array[String] = ["Gerda says this is a quick one.", tel_w, "Kees brought a torch."]
	ok(str(TKS.kies_toon(kr_g, "", [tel_w] as Array[String], tel_w, 3, true)) == str([tel_w, "Kees brought a torch."]), "run 44017687872: Gerda van vóór de nacht niet meer boven de telling")
	ok(str(TKS.kies_toon(kr_w, "", [] as Array[String], "", 3, true)) == str(["Tibbe fled twice.", tel_w, "Kees brought a torch."])
		and str(TKS.kies_toon(kr_w, tel_w, wr_w, tel_w, 1, false)) == str(["Kees brought a torch."]), "zonder weg of zonder muis: gewoon de laatste regels")
	var bs := "Gloop had a busy shift."
	var kr_d: Array[String] = [bs, "Old tally.", "Joost climbs into your hole.", bs, tel_w]
	var wr_d: Array[String] = [bs, tel_w]
	ok(str(TKS.kies_toon(kr_d, tel_w, wr_d, tel_w, 3, true)) == str([tel_w, bs]), "kaartje na weg: zelfde tekst als vorige nacht komt maar één keer: %s" % str(TKS.kies_toon(kr_d, tel_w, wr_d, tel_w, 3, true)))
	# moet Daan 16 nov 23:30 (b): hooguit één regel per held op het kaartje (laatste drie), de telling blijft staan
	var nk3 = nep_k.new()
	nk3.tekst = nep_tekst.new()
	nk3.hol = {"goud": 0}
	nk3.namen_recent = ["Kees", "Kees II", "Lotte"]
	nk3.kroniek.assign(["115 came, 82 fell. +607 gold.", "Kees was back and left in a hurry.", "Lotte waddles in."])
	WR.een_per_held(nk3, "Kees fell into the Spike Pit.")
	ok(nk3.kroniek.size() == 2 and not nk3.kroniek.has("Kees was back and left in a hurry."), "kaartje: tweede regel over Kees vervangt de eerste (Daan 23:30 b)")
	WR.een_per_held(nk3, "Kees II waddles in.")
	ok(nk3.kroniek.size() == 2, "kaartje: Kees II is een andere held dan Kees")
	nk3.kroniek.assign(["Lotte waddles in.", "Pim waddles in.", "Mo waddles in."])
	WR.een_per_held(nk3, "Lotte fell.")
	ok(nk3.kroniek.size() == 3, "kaartje: alleen de twee regels ervoor tellen (Lotte drie terug blijft)")
	ok(WR._noemt("Sir Odo clanks in.", "Sir Odo") and not WR._noemt("Keesje hums.", "Kees") and not WR._noemt("Kees III runs.", "Kees"), "kaartje: naam als heel woord")
	# Daan 16 nov 20:35: "flat" alleen de eerste twee keer per speelbeurt, "up again" alleen na een getoonde "flat"
	var np = GDScript.new()
	np.source_code = "extends RefCounted\nvar wachtrij: Array = []\nvar plat_keer := 0\nvar plat_gemeld := false\nvar log: Array[String] = []\nfunc log_regel(r: String) -> void:\n\tlog.append(r)\n"
	np.reload()
	var pk = np.new()
	var pw: Array[String] = []
	for i in 4:
		for nu in [true, false]:
			var ps: String = WR.plat_wissel(pk, nu)
			pw.append(ps)
			pk.wachtrij.clear()   # alles getoond
	ok(pw == ["plat", "op", "plat", "op", "", "", "", ""], "plat en op alleen de eerste twee keer: " + str(pw))
	ok(pk.log.size() == 2 and pk.log[0].contains("plat zonder regel"), "derde en vierde keer plat staan in de log " + str(pk.log))
	var pk2 = np.new()
	pk2.wachtrij.append({"r": "P", "soort": "plat"})
	pk2.plat_keer = 1
	pk2.plat_gemeld = true
	ok(WR.plat_wissel(pk2, false) == "" and pk2.plat_keer == 0 and pk2.wachtrij.is_empty(), "plat nooit getoond: geen op en telt niet mee")
	ok(WR.plat_wissel(pk2, true) == "plat", "daarna mag plat nog")
	# savemap vast (Sanne 17 nov 05:00): demo en vol spel delen %APPDATA%\\Dortus\\Het Hol, anders is "The full game keeps it all." niet waar.
	# Hernoem je het project, laat deze map dan staan (of kopieer de oude map eenmalig) en pas pas daarna deze toets aan.
	ok(ProjectSettings.get_setting("application/config/use_custom_user_dir", false) == true, "savemap: eigen map aan")
	ok(ProjectSettings.get_setting("application/config/custom_user_dir_name", "") == "Dortus/Het Hol", "savemap blijft Dortus/Het Hol: " + str(ProjectSettings.get_setting("application/config/custom_user_dir_name", "")))
	print("[hol-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
