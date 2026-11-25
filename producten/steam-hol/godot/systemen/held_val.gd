extends RefCounted
# Wat er gebeurt als een held bij een val of bewoner komt (los van held.gd sinds 25 nov, Olaf #25: held.gd bleef anders
# boven de 400 regels). held.gd roept HELD_VAL.onderweg(self) aan vanuit _onderweg(); alles staat op de held zelf.
# Regels: zie de kop van held.gd (kans, vaste uitkomsten van een vers spel, wrok, vluchten, hoedentoren).

static func onderweg(h) -> void:
	var cel: Vector2i = h.hol.pos_naar_cel(h.position)
	if h.gezien.has(cel.x):
		return
	var soort: String = h.hol.val_op(cel)
	var b = h._bewoner_op(cel.x)
	if soort == "" and b == null:
		return
	h.gezien[cel.x] = true
	if soort != "":
		b = null   # val en bewoner in dezelfde kolom: hij vecht tegen de val
	var naam_vijand: String = h.NAAM_PUT if soort != "" else b.naam()
	var soort_vd: String = soort if soort != "" else String(b.get("soort") if "soort" in b else "slijm")
	var upg = h._upgrades()
	var verborgen: bool = upg != null and soort_vd == "stekelput" and upg.put_verborgen()
	var kans: float = h.KANS.get(soort_vd, h.KANS_ANDERS) * h.SOORT.kans_factor(h.soort_held, soort_vd, verborgen)
	if upg != null:
		kans += upg.kans_erbij(soort_vd)   # systemen/upgrades.gd: +7 procentpunt per gekochte stap (balans.md)
	var is_vijand: bool = h.vijand_kol >= 0 and cel.x == h.vijand_kol
	if is_vijand:
		h.info["gezien_vijand"] = true
		kans += h.ROEKELOOS * (2.0 if h.trek == "wraakzuchtig" else 1.0)
	if bool(h.info.get("hoard_toucher", false)):
		kans *= h.BRUTAAL
	h.verdedigingen += 1
	var valt: bool = h.rng.randf() < kans
	# vaste uitkomsten voor de eerste tien minuten (Olaf 20:25 en 20:45, Sanne features.md); strook.gd zet ze alleen bij een vers spel
	if bool(h.info.get("moet_vallen", false)) and h.verdedigingen == 1:
		valt = true
	if bool(h.info.get("moet_vluchten", false)) and h.verdedigingen == 1:
		valt = false           # één klap en hij rent (hieronder)
	if bool(h.info.get("moet_doorlopen", false)):
		valt = false           # overleeft alles en raakt de schat aan: Hoard-Toucher
	if bool(h.info.get("moet_opgegeten", false)):
		valt = b != null       # een bewoner krijgt hem (held 5: eerste hoed op Gloop); een val overleeft hij
	if bool(h.info.get("moet_afgerekend", false)):
		valt = is_vijand       # alles onderweg overleeft hij, zijn eigen vijand krijgt hem
	if valt:
		h.info["laatst_geraakt"] = naam_vijand
		h.info["wat"] = ("finally fell to " if is_vijand else "fell to ") + naam_vijand
		h.val_teken = h.teken_nu()
		h.staat = "vallen"
		if soort != "":
			h.val_x = round(h.hol.cel_naar_pos(cel).x) - 1.0   # 1 spelpixel links van het midden: het lijf steekt anders rechts buiten de stekels (kan Daan 18:50)
		if b != null and b.has_method("raak"):
			# hoedentoren: zijn hoed gaat naar de bewoner; een aartsvijand pas naar de wand als die te zien is (WAND_ER)
			var naar_wand: bool = h.WAND_ER and h.is_aartsvijand()
			var n = null
			if b.has_method("hoeden_op_hoofd"):   # slijm.gd met hoedentoren
				# de hoed vliegt vanaf zijn hoofd naar de toren (leven in het spel, punt 2); Gloop-coordinaten, y omhoog negatief
				var van: Vector2 = Vector2(clampf(h.position.x - b.position.x, -16.0, 16.0), -10.0) if b is Node2D else Vector2(-12, -10)
				n = b.raak(-1 if naar_wand else h.hoed_nr, van)
			else:
				b.raak()          # stand-in van Olaf (kern/standin_slijm.gd) kent geen hoeden
			if b.has_method("hoeden_op_hoofd") or naar_wand:
				h.info["hoed_naar"] = "wand" if naar_wand else "bewoner"   # stand-in zonder toren: hoed blijft op zijn hoofd
			h.info["hoeden_bewoner"] = 0 if naar_wand or n == null else int(n)   # voor kroniek.hoed(naam, bewoner, aantal)
		return
	# overleefd: geraakt, wrok tegen dit ding; een bewoner die verliest is even plat
	if soort != "":
		h.HELD_LOOP.spring(h, round(h.hol.cel_naar_pos(cel).x))   # een val doet altijd iets: hij springt er zichtbaar overheen (#25)
	h.klappen += 1
	h.geraakt_tot = h.t + 0.5
	h.info["laatst_geraakt"] = naam_vijand
	if b != null and b.has_method("plat"):
		b.plat()
	if b != null and String(b.get("soort")) == "slijm":
		h.info["gebeten"] = true   # door Gloop gebeten: vanaf nu (ook bij terugkomst) een hoed met een hap eruit
	if is_vijand:
		h.vijand_kol = -1
		h.doel_kol = h.hol.schat().x
	# schijterig draait na een klap de helft van de keren om, hebzuchtig pas na twee klappen
	var rent: bool = (h.trek == "schijterig" and h.rng.randf() < 0.5) or h.klappen >= 2
	if h.SOORT.taai(h.soort_held) and h.klappen < 2:
		rent = false           # ridder: rent pas na twee klappen, ook als hij schijterig is
	if soort == "stekelput" and upg != null and upg.put_houdt_vast() and h.klappen < 2:
		rent = false           # Deep Pit: een schijterige held keert na zijn eerste klap (van de put) niet om
	if bool(h.info.get("moet_vluchten", false)):
		rent = true
	if bool(h.info.get("moet_doorlopen", false)) or bool(h.info.get("moet_opgegeten", false)) or bool(h.info.get("moet_afgerekend", false)):
		rent = false
	if rent:
		h.info["wat"] = "got hurt by %s and ran" % naam_vijand
		if h.spring_t >= 0.0:
			h.na_sprong = "vluchten"   # eerst over de put heen, dan omdraaien
		else:
			h.HELD_LOOP.draai(h)
		if h.SOORT.zingt(h.soort_held):
			h.info["lied"] = h.SOORT.LIED_HELDEN   # bard: zingt over je hol, strook.gd laat er zoveel extra komen
