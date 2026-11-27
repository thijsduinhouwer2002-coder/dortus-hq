extends SceneTree
# Toetsen voor tekens boven een held die oppoppen en zacht weggaan (Olaf 27 nov, issue #85, keuzes Sanne: komen 0,2 s,
# weg 0,15 s, pauze-wip elke 2,5 s, sprongteken alleen de komwip, pixeltekens schalen nooit).
# Draaien: godot --headless --path <godot-map> -s systemen/toetsen/toets_tekens.gd
const WIP := preload("res://systemen/held_wip.gd")
const NOOT := preload("res://systemen/held_noot.gd")
var fout := 0

class Nep:
	var wip := {}

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[tekens-toets] OK ", wat)
	else:
		fout += 1
		print("[tekens-toets] FOUT ", wat)

func _init() -> void:
	komen()
	pauze_wip()
	weggaan()
	in_het_spel()
	nootjes()
	print("[tekens-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)

func komen() -> void:
	var h := Nep.new()
	var eerste: Dictionary = WIP.stand(h, "uitroep", 10.0, false)[0]
	ok(float(eerste.s) <= 0.3 and float(eerste.a) <= 0.3, "eerste beeld: klein en doorzichtig (schaal %.2f, dekking %.2f), geen knip" % [eerste.s, eerste.a])
	var vorig := 0.0
	var stijgt := true
	var hops := {}
	var heel := true
	for i in range(0, 21):
		var v: Dictionary = WIP.stand(h, "uitroep", 10.0 + i * 0.01, false)[0]
		stijgt = stijgt and float(v.s) >= vorig - 0.0001
		vorig = float(v.s)
		hops[int(v.hop)] = true
		heel = heel and v.hop is int and v.dy is int
	ok(stijgt and absf(vorig - 1.0) < 0.001, "3D-teken groeit in 0,2 s tot vol, zonder terug te krimpen")
	var s10: float = float(WIP.stand(h, "uitroep", 10.1, false)[0].s)
	ok(s10 > 0.8, "zachte rem: halverwege al %.2f van vol (eerst snel, dan langzaam)" % s10)
	ok(heel and hops.has(-2) and hops.has(0) and not hops.has(-3) and not hops.has(1), "pixelteken wipt hele spelpixels: 0 tot 2 omhoog en terug (%s)" % str(hops.keys()))

func pauze_wip() -> void:
	var h := Nep.new()
	var wips: Array = []
	var bezig := false
	var t := 0.0
	while t < 10.2:
		var v: Dictionary = WIP.stand(h, "zweet", t, false)[0]
		if int(v.dy) != 0 and not bezig:
			wips.append(snappedf(t, 0.01))
		bezig = int(v.dy) != 0
		if int(v.dy) < -WIP.WIP_PX:
			ok(false, "pauze-wip hoger dan %d spelpixel" % WIP.WIP_PX)
		t += 0.01
	var tussen_ok := wips.size() >= 3
	for i in range(1, wips.size()):
		tussen_ok = tussen_ok and absf(float(wips[i]) - float(wips[i - 1]) - WIP.PAUZE_S) < 0.03
	ok(tussen_ok and float(wips[0]) > 2.0, "zolang het teken staat elke 2,5 s één wip van 1 spelpixel (%s)" % str(wips))
	var hs := Nep.new()
	var sprong_wip := false
	t = 0.0
	while t < 3.0:
		var v2: Dictionary = WIP.stand(hs, "uitroep", t, true)[0]
		if t >= WIP.IN_S and int(v2.dy) != 0:
			sprong_wip = true
		t += 0.01
	ok(not sprong_wip, "sprongteken: alleen de komwip, geen pauze-wip")

func weggaan() -> void:
	var h := Nep.new()
	WIP.stand(h, "boos", 0.0, false)
	var voor: Dictionary = WIP.stand(h, "boos", 1.0, false)[0]
	var l0: Array = WIP.stand(h, "", 1.0, false)
	ok(l0.size() == 1 and String(l0[0].tk) == "boos" and absf(float(l0[0].a) - float(voor.a)) < 0.01, "weg: op het moment zelf staat het teken er nog even vol (geen knip)")
	var l1: Array = WIP.stand(h, "", 1.1, false)
	ok(l1.size() == 1 and float(l1[0].a) < 0.5 and float(l1[0].s) < 1.0, "na 0,1 s bijna weg (dekking %.2f, schaal %.2f)" % [l1[0].a, l1[0].s])
	ok(WIP.stand(h, "", 1.16, false).is_empty(), "na 0,15 s helemaal weg")
	ok(WIP.UIT_S < WIP.IN_S, "weg (%.2f s) gaat korter dan komen (%.2f s)" % [WIP.UIT_S, WIP.IN_S])
	# midden in het groeien weg: krimpt vanaf waar hij was, springt niet eerst naar vol
	var hm := Nep.new()
	WIP.stand(hm, "zweet", 0.0, false)
	var half: Dictionary = WIP.stand(hm, "zweet", 0.05, false)[0]
	var weg: Dictionary = WIP.stand(hm, "", 0.05, false)[0]
	ok(absf(float(weg.s) - float(half.s)) < 0.01 and absf(float(weg.a) - float(half.a)) < 0.01, "weg midden in het komen: krimpt vanaf %.2f, geen sprong naar vol" % half.s)
	# wissel van teken: het oude gaat zacht weg terwijl het nieuwe komt
	var hw := Nep.new()
	WIP.stand(hw, "uitroep", 0.0, false)
	var twee: Array = WIP.stand(hw, "zweet", 1.0, false)
	ok(twee.size() == 2 and String(twee[0].tk) == "uitroep" and String(twee[1].tk) == "zweet", "wissel: uitroep gaat weg, zweet komt op")

# Echte held door een nep-hol met een put: het teken van elk beeld (20 per seconde) door de wip. Geen beeld waarin een
# teken van bijna vol ineens weg is, of uit het niets bijna vol staat.
func in_het_spel() -> void:
	var gezien := {}
	var knip := 0
	var wissels := 0
	for info in [{"naam": "Kees", "trek": "hebzuchtig", "moet_vallen": true}, {"naam": "Joost", "trek": "schijterig", "moet_vluchten": true},
			{"naam": "Mia", "trek": "hebzuchtig", "soort_held": "dief"}, {"naam": "Lot", "trek": "hebzuchtig", "soort_held": "magier"}]:
		var hol := Node2D.new()
		hol.set_script(load("res://systemen/toetsen/nep_hol.gd"))
		hol.schat_kol = 14
		hol.vallen[9] = "stekelput"
		var wezens := Node2D.new()
		hol.add_child(wezens)
		var h := Node2D.new()
		h.set_script(load("res://systemen/held.gd"))
		wezens.add_child(h)
		h.start(hol, info)
		var vorig := {}
		var vorig_tk := ""
		var n := 0
		while is_instance_valid(h) and h.staat != "weg" and n < 4000:
			h.stap(1.0 / 20.0)
			n += 1
			if h.staat == "weg":
				break
			var tk: String = String(h.teken_nu()) if h.staat != "vallen" else String(h.val_beeld(float(h.val_t)).teken)
			if tk != vorig_tk:
				wissels += 1
				if tk != "":
					gezien[tk] = true
			vorig_tk = tk
			var nu := {}
			for v in WIP.stand(h, tk, float(h.t), float(h.spring_t) >= 0.0):
				nu[String(v.tk)] = float(v.a)
			for k in vorig:
				if k != "poef" and float(vorig[k]) > 0.5 and not nu.has(k):
					knip += 1
			for k in nu:
				if k != "poef" and not vorig.has(k) and float(nu[k]) > 0.5:
					knip += 1
			vorig = nu
		hol.free()
	ok(gezien.has("uitroep") and gezien.has("zweet") and wissels >= 6, "in het spel: tekens komen en gaan (%s, %d wissels)" % [str(gezien.keys()), wissels])
	ok(knip == 0, "in het spel: geen teken knipt aan of uit (%d keer)" % knip)

# Daan #237 (kan): het nootje van een lied-held knipte weg naast de zachte tekens. Geen nootje springt meer meer dan
# 0,4 dekking tussen twee beelden van 50 per s (komen 0,2 s = 0,25 per beeld, weg 0,15 s = 0,33 per beeld).
func nootjes() -> void:
	var sprong := 0.0
	var vorig := 0.0
	for i in range(0, 121):
		var t := i * 0.02
		var l: Array = NOOT.nootjes("", true, "lopen", t)
		var a: float = float(l[0][2]) if not l.is_empty() else 0.0
		sprong = maxf(sprong, absf(a - vorig))
		vorig = a
	ok(sprong <= 0.4 and vorig == 0.0, "lied-nootje komt en gaat zacht (grootste stap %.2f per beeld)" % sprong)
	sprong = 0.0
	vorig = 0.0
	for i in range(0, 121):
		var t := i * 0.02
		var l: Array = NOOT.nootjes("", true, "lopen", t, 1.0)   # teken komt op t = 1,0
		var a: float = float(l[0][2]) if not l.is_empty() else 0.0
		sprong = maxf(sprong, absf(a - vorig))
		vorig = a
	ok(sprong <= 0.4 and NOOT.lied_alfa(1.2, 1.0) == 0.0 and NOOT.lied_alfa(0.99, 1.0) == 1.0, "lied-nootje gaat in 0,15 s weg als een teken het overneemt (grootste stap %.2f)" % sprong)
	sprong = 0.0
	for k in range(0, 4):
		var l: Array = NOOT.nootjes("bard", false, "lopen", k * NOOT.NOOT_ELKE_S + 0.01)
		sprong = maxf(sprong, float(l[0][2]))   # eerst in de lijst = het nieuwste nootje
	ok(sprong <= 0.1, "bard: een nieuw nootje begint bijna doorzichtig (%.2f)" % sprong)
	var w := {}
	var y0 := NOOT.glij(w, -24.0, 5.0)
	var y1 := NOOT.glij(w, -26.0, 5.05)   # kruin van het sprongbeeld 2 hoger
	var y2 := NOOT.glij(w, -26.0, 5.10)
	ok(y0 == -24 and y1 == -25 and y2 == -26, "nootjes glijden 1 spelpx per beeld naar een hogere kruin (%d, %d, %d), springen niet" % [y0, y1, y2])
