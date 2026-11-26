extends RefCounted
const VOORTGANG := preload("res://systemen/voortgang.gd")   # met_pensioen (Bram 04:35)
const HOL_NIVEAU := preload("res://systemen/hol_niveau.gd")
const GOUD_BASIS := 9   # goud per vangst zonder bonus (Sanne 25 nov, bouwblad I; was 6)
const GOUD_DEMO := 6    # in de demo-film (demo=1) de oude basis, Daan #109 M1
# Olaf 26 nov (#134, Iris aandacht 7): vanaf minuut 4 open tijd (speeltijd_s, ook over saves heen) GOUD_LAAT erbij per
# vangst, samen met de krappe droogte (kern/ritme.gd) en stap 3 voor 70: in minuut 4 tot 12
# een koop binnen ±3 min. Minuut 0 tot 4 blijft gelijk (geen koopgeluk weggeven).
const LAAT_VANAF_S := 240.0
const GOUD_LAAT := 4
# Deel van kern/strook.gd (Olaf), losgehaald bij het opruimen van 10 nov (strook.gd was 650 regels).
# Statische functies; `s` is de strook. Gedrag gelijk aan voor het splitsen (film.log gelijk).

# Faam erbij (een gevangen held, of wie er vielen terwijl je weg was). Faam gaat nooit omlaag.
# Nog geen bordje of feestje (Mila), alleen de log zodat de toetsen en de duurtest het hol-niveau kunnen volgen.
static func faam_erbij(s, n: int) -> void:
	if n <= 0:
		return
	var oud: int = s.faam
	s.faam += n
	for niv in HOL_NIVEAU.erbij(oud, s.faam):
		s.log_regel("HOL hol-niveau %d (faam %d, t %.1f)" % [niv, s.faam, s.t])

# Vangst of vlucht die terugslaat op de binnenkomst (Sanne 17 nov 09:02, features.md, Iris keuring 21): een held die
# bij binnenkomst een soort- of trekregel kreeg, krijgt bij zijn vangst in de put of vlucht een regel uit "val_<soort>" of
# "vlucht_<soort>" (systemen/kroniek_regels.gd). Afrekening, aartsvijand en hap-met-hoed gaan voor (die roepen dit niet
# aan). Een terugkomer heeft geen binnen_soort meer (wordt bij de afloop gewist): zijn opzet is te lang geleden.
static func terugslag(s, info: Dictionary, gewoon: String) -> String:
	var soort := String(info.get("binnen_soort", ""))
	if soort == "" or int(info.get("bezoeken", 0)) != 0 or s.get("demo") == true:
		return gewoon   # geen opzet, een terugkomer, of de demofilm (die houdt zijn vaste tekst, controleur 2 en 5)
	if soort == "bard" and gewoon == "vlucht":
		return gewoon   # de liedregel volgt meteen en een_per_held haalt de vluchtregel weg (controleur 3)
	var eigen := ("vlucht_" if gewoon == "vlucht" else "val_") + soort
	return eigen if s.regels.heeft(eigen) else gewoon

# Hap per soort (Sanne 17 nov 10:00, features.md): dezelfde voorwaarden als terugslag() (een opzet, geen terugkomer,
# niet in de demofilm), maar dan uit "hap_<soort>". Alleen als er geen hap_hoed kwam; anders val_bewoner.
static func hap_soort(s, info: Dictionary) -> String:
	var soort := String(info.get("binnen_soort", ""))
	if soort == "" or int(info.get("bezoeken", 0)) != 0 or s.get("demo") == true:
		return "val_bewoner"
	return "hap_" + soort if s.regels.heeft("hap_" + soort) else "val_bewoner"

static func held_klaar(s, _held, uitkomst: String, info: Dictionary) -> void:
	var b := info.duplicate()
	b["kleur"] = (info.kleur as Color).to_html(false)
	b["hoed"] = (info.hoed as Color).to_html(false)
	for v in ["moet_vallen", "moet_vluchten", "moet_doorlopen", "moet_opgegeten", "hoed_naar", "hoeden_bewoner", "schat_gemeld", "snelheid", "demo_clou", "lied", "dutje", "dutje_gemeld", "lied_held", "hoed_gemeld", "binnen_soort", "koop_geluk"]:
		b.erase(v)
	b.erase("wat")
	if uitkomst == "ontsnapt":
		if s.get("reeks") != null:   # nep-strook in de toetsen heeft geen reeks
			s.reeks = 0   # de reeks is voorbij als er een ontsnapt (kern/klap.gd)
		# bard: hij zingt over je hol en er komen helden bij (heldensoort.gd, Bram 02:30): de regel en de eerste extra
		# held binnen 8 tot 20 s (strook.gd telt lied_helden af). De lied-regel komt na de vlucht-regel.
		var lied := int(info.get("lied", 0))
		b.bezoeken = int(info.get("bezoeken", 0)) + 1
		var oud_wrok: String = String(info.get("wrok", ""))
		b.wrok = info.get("laatst_geraakt", oud_wrok if oud_wrok != "" else "your Hoard")
		b.erase("laatst_geraakt")
		# 60% van wie vlucht komt ooit terug, aartsvijanden altijd (sim/UITKOMST.md); in de demo iedereen.
		# Wie niet terugkomt gaat met pensioen: geen straf, later een grapje bij openen.
		if String(info.naam) == s.begin_vlucht:
			s.vlucht_t = s.t
		if s.demo:
			s.vlucht_tijd[String(info.naam)] = s.t
		if s.demo or b.bezoeken >= 3 or s.rng.randf() < 0.6 or String(info.naam) == s.begin_vlucht:
			s.terugkomers.append(b)
		else:
			s.pensioen_namen = VOORTGANG.met_pensioen(s.pensioen_namen, String(info.naam))
		# Heldenboek: wie drie keer vluchtte is een aartsvijand en krijgt een bladzijde, ook als hij niet terugkomt
		if int(b.bezoeken) >= 3:
			boek_regel(s, s.boek.aarts(String(info.naam), {"bijnaam": "Thrice-Fled", "wrok": String(b.wrok), "bezoeken": int(b.bezoeken)}))
		# plafond van 8: anders raken de namen op en groeit de save; de oudste die geen aartsvijand is gaat met pensioen
		if s.terugkomers.size() > 8:
			var weg_i := 0
			for i in s.terugkomers.size():
				if int(s.terugkomers[i].bezoeken) < 3:
					weg_i = i
					break
			if not s.demo:   # in de demo niet, anders veranderen de namen in de film
				s.pensioen_namen = VOORTGANG.met_pensioen(s.pensioen_namen, String(s.terugkomers[weg_i].naam))
			s.terugkomers.remove_at(weg_i)
		# Geen straf: wie ontsnapt neemt niets mee dat jij kwijt bent, alleen zijn wrok.
		if bool(info.get("hoard_toucher", false)) and String(info.get("wat", "")).begins_with("touched"):
			# de schat-regel kwam al op het moment van aanraken (_process); nu alleen dat hij wegrent
			s._kroniek(s.regels.kies("schat_weg", {"naam": info.naam}))
		else:
			var w: String = String(b.wrok)
			s._kroniek(s.regels.kies(terugslag(s, info, "vlucht"), {"naam": info.naam, "bewoner": w.replace(" the Slime", "") if w != "your Hoard" else "you"}))
		boek_regel(s, s.boek.held(String(info.get("soort_held", "")), "ontsnapt", String(info.naam), s._bewoner()))
		if lied > 0:
			# sfeerregel: je ziet het lied niet, dus laag zoals binnenkomst en mag vervallen (Sanne toets 9, besluit 2a);
			# de afloop zie je wel: de helden die erdoor komen krijgen een eigen regel die voorgaat (binnen_lied, strook.gd)
			s._kroniek(s.regels.kies("lied", {"naam": info.naam}), true, "lied")
			s.lied_helden += lied
			if s.get("geluid") != null:
				s.geluid.speel("lied")
			if not s.demo:
				s.volgende_held = minf(s.volgende_held, s.t + s.rng.randf_range(8.0, 20.0))
	else:
		# goud per val: 6, plus 3 per eerder bezoek; een held met een wrok is een beloning (balans.md punt 1, besluit Olaf)
		# plus graafbonus: +1 per 8 zelf gegraven cellen, hooguit +3 (Sanne 16 nov 21:00, balans.md)
		# plus reeksbonus: vangsten op rij zonder dat er een ontsnapt, vanaf de derde +1 per stap, hooguit +4 (Olaf 24 nov, issue 5)
		var reeks: int = int(s.get("reeks")) + 1 if s.get("reeks") != null else 1
		if s.get("reeks") != null:
			s.reeks = reeks
		# basis 9 (Sanne 25 nov, bouwblad I; was 6): koop 2 kwam 6 tot 8 min na koop 1 (Iris d27cfc3, GEZIEN)
		# demo=1 (film) houdt de oude 6, zodat de gekeurde demo-film gelijk blijft (Daan #109 M1)
		var buit := (GOUD_DEMO if bool(s.get("demo")) else goud_basis(s)) + 3 * int(info.get("bezoeken", 0)) + VOORTGANG.graafbonus(int(s.zelf_gegraven)) + reeks_bonus(reeks)
		s.set_meta("laatste_vangst_t", s.t)   # droogte (kern/ritme.gd, bouwblad I)
		s.hol.set_meta("droogte", false)
		s.hol.set_meta("droogte_bezig", false)
		if bool(info.get("koop_geluk", false)):
			buit *= 2   # koopgeluk: de eerste vangst bij een net gekocht ding brengt dubbel (systemen/held_val.gd)
			s.log_regel("HOL koopgeluk vangst +%d (t %.1f)" % [buit, s.t])
		s.hol.goud += buit
		faam_erbij(s, 1)
		var naam: String = String(info.naam)
		var basis := naam.split(" ")[0]
		s.gevallen_namen[basis] = int(s.gevallen_namen.get(basis, 0)) + 1
		s.hol.munt_regen(s.hol.pos_naar_cel(_held.position).x, 3 + mini(reeks - 1, 3))   # meer muntjes in een reeks
		if s.get("klap") != null and _held != null:
			s.klap.vangst(_held.position, buit, reeks)
		if s.get("geluid") != null:   # plof of hap, en net daarna de munt (kern/geluid.gd)
			s.geluid.vangst(String(info.get("wat", "fell")).ends_with(s.slijm.naam()))
		if reeks >= 2:
			s.log_regel("HOL reeks %d (+%d, t %.1f)" % [reeks, reeks_bonus(reeks), s.t])
		var wat: String = String(info.get("wat", "fell"))
		var r := ""
		var extra := " +%d" % buit
		if wat.begins_with("finally"):
			var vijand := wat.replace("finally fell to ", "")
			if int(info.get("bezoeken", 0)) >= 3:
				r = s.regels.kies("afgerekend_aarts", {"naam": naam}, extra.length())
			elif vijand.begins_with("the "):
				# "Bram came back. The Spike Pit won." (Sanne toets 6, punt 1: de grap moet af zijn)
				r = s.regels.kies("afgerekend_val", {"naam": naam, "Val": "The" + vijand.substr(3)}, extra.length())
			else:
				r = s.regels.kies("afgerekend", {"naam": naam}, extra.length())
		elif wat.ends_with(s.slijm.naam()):
			# hap en hoed in een regel op het moment van de hap (Sanne toets 9, besluit 2b): eerst kwam de hoed-regel 4 tot
			# 6 s na de hap, terwijl de hoed al op zijn kop stond. Wanneer: zoals de hoed-regel hieronder (eerste hoed, de
			# clou in de demo, anders een op de vier); bij 25 en 100 blijft de bijnaam een eigen regel.
			var n_h := int(info.get("hoeden_bewoner", 0))
			if String(info.get("hoed_naar", "")) == "bewoner" and n_h > 0 and n_h != 25 and n_h != 100:
				# de hoed die hij echt op had: held.gd rekent hem zelf uit als hoed_nr ontbreekt (oude save), controleur kan-punt 6
				var hn = _held.get("hoed_nr") if _held != null else null
				if hn == null:
					hn = info.get("hoed_nr", -1)
				if n_h == 1 or bool(info.get("demo_clou", false)) or s.rng.randf() < 0.25:
					r = s.regels.kies("hap_hoed_eerste" if n_h == 1 else "hap_hoed", {"naam": naam, "bewoner": s._bewoner(), "hoed": hoed_naam(int(hn))}, extra.length())
					if r.length() > RG.MAX - extra.length():
						r = ""   # te lang met deze namen: dan de gewone hap-regel (de hoed staat toch op de toren)
				info["hoed_gemeld"] = true   # geen losse hoed-regel meer, ook niet als de hap-regel de hoed niet noemde
			# alleen een gewone hap-regel als het geen hap_hoed werd (controleur kan-punt 1: anders verbruikt de schudzak een regel die niemand ziet)
			if r == "":
				# geen terugslag bij de hap (die regels gaan over de put, controleur 1), wel een eigen hap per soort (Sanne 10:00)
				r = s.regels.kies(hap_soort(s, info), {"naam": naam, "bewoner": s._bewoner()}, extra.length())
		else:
			r = s.regels.kies(terugslag(s, info, "val"), {"naam": naam, "val": wat.replace("fell to ", "")}, extra.length())
		s._kroniek(r + extra)
		if r.contains("boot"):   # dan mag zijn naamgenoot later "wants mom's boot back" zeggen (Iris 19 nov)
			s.laars_namen[naam] = true
		# Heldenboek: een stempel door Gloop of door de put (bij afgerekend: wie hem kreeg)
		# (put alleen als het echt de put was; anders Gloop, ook als zijn bijnaam net veranderde, controleur kan-punt 6)
		var door := "stekelput" if wat.ends_with("the Spike Pit") else "slijm"
		boek_regel(s, s.boek.held(String(info.get("soort_held", "")), door, naam, s._bewoner()))
		if door == "stekelput":
			put_hoed(s, _held)
		if wat.begins_with("finally") and int(info.get("bezoeken", 0)) >= 3:
			# eerst zorgen dat hij in het boek staat (aartsvijand uit een save van voor het boek), dan afrekenen.
			# Geen regel: er is nog geen dagteller en "settled on day 1" op dag 5 is niet waar (controleur kan-punt 5)
			s.boek.aarts(naam, {"bijnaam": "Thrice-Fled", "wrok": String(info.get("wrok", "")), "bezoeken": int(info.get("bezoeken", 3))})
			s.boek.aarts_af(naam, s._bewoner() if door == "slijm" else "the Spike Pit", 1)
		if String(info.get("hoed_naar", "")) == "bewoner" and int(info.get("hoeden_bewoner", 0)) > 0:
			var hb = _held.get("hoed_nr") if _held != null else null
			var rh: String = s.boek.hoed(int(hb) if hb != null else int(info.get("hoed_nr", -1)), naam)
			# noemde de kroniek de hoed al (hap_hoed of de eerste hoed), dan alleen in het boek, geen tweede regel (kan-punt 2)
			if not bool(info.get("hoed_gemeld", false)) and int(info.get("hoeden_bewoner", 0)) != 1:
				boek_regel(s, rh)
			boek_regel(s, s.boek.berg(int(info.get("hoeden_bewoner", 0))))
		# hoedentoren: zijn hoed staat nu op Gloop (slijm.gd, Bram). Eerste hoed altijd een regel, bij 25 en 100 de bijnaam,
		# anders hooguit een op de vier, zodat de val-regel niet verdrongen wordt (kroniek-regels.md)
		var n_hoed := int(info.get("hoeden_bewoner", 0))
		if String(info.get("hoed_naar", "")) == "bewoner" and n_hoed > 0 and not bool(info.get("hoed_gemeld", false)):
			var w := {"bewoner": s._bewoner(), "naam": basis}
			if n_hoed == 1:
				s._kroniek(s.regels.kies("hoed_eerste", w))
			elif n_hoed == 25 or n_hoed == 100:
				w["bijnaam"] = "Hatted" if n_hoed == 25 else "Milliner"
				s._kroniek(s.regels.kies("hoed_bijnaam", w))
			elif s.rng.randf() < 0.25 or bool(info.get("demo_clou", false)):
				# demo: de hoed van de clou-held (Mara) altijd een regel, de toren groeit in beeld (Sanne toets 7, punt 1)
				# "hat pile is taller than him" klopt pas bij een echte stapel (controleur punt 6)
				var soort := "hoed" if n_hoed >= 5 else "hoed_klein"
				s._kroniek(s.regels.kies(soort, w))

# Wegkijken (issue #86, tempo-regel 5): ook de hoed van wie in de put viel gaat naar de hoedentoren, zodat het hol
# zichtbaar groeit voor een speler die niets koopt (toren, berg en hoedenwand tellen alle hoeden van Gloop). Hij valt
# 1,2 s na de klap van boven op de top, met de landing van de hoeden van de nacht (slijm.gd, al gekeurd); geen tekst,
# geen geluid. Pas als Gloop zijn eigen eerste hoed heeft (de eerste minuut en de regel "first hat" blijven gelijk),
# niet in de demo-film. Telt niet als opgegeten: gegeten blijft gelijk, anders spuugt Gloop laarzen van wie hij niet at.
const PUT_HOED_WACHT_S := 1.2
static func put_hoed(s, _held) -> void:
	var sl = s.get("slijm")
	if s.demo or sl == null or _held == null or not sl.has_method("krijg_hoed_later") or sl.get("hoeden") == null:
		return
	if (sl.hoeden as Array).is_empty() or sl.get("moment_vast") != null and float(sl.moment_vast) >= 0.0:
		return
	var hn = _held.get("hoed_nr")
	if hn == null or int(hn) < 0:
		return
	# loopt er al een rij (nachthoeden bij terugkomen, of een vorige put-hoed): achteraan, zonder de klok te herstarten,
	# anders pauzeert de rij die al valt (kan Daan #92 punt 4)
	var loopt: bool = not (sl.nacht_hoeden as Array).is_empty() and float(sl.nacht_van) >= 0.0
	sl.krijg_hoed_later(int(hn))
	sl.gegeten -= 1
	if not loopt:
		sl.start_nacht(PUT_HOED_WACHT_S)
	else:
		sl.set_process(true)
	s.log_regel("HOL put-hoed %d naar de toren (hoeden nu %d, t %.1f)" % [int(hn), sl.hoeden.size() + sl.nacht_hoeden.size(), s.t])

static func goud_basis(s) -> int:
	if float(s.get("speeltijd_s")) < LAAT_VANAF_S:
		return GOUD_BASIS
	return GOUD_BASIS + GOUD_LAAT

# Reeksbonus (issue 5): 1 en 2 op rij niets extra, de derde +1, de vierde +2, ... hooguit +4.
static func reeks_bonus(r: int) -> int:
	return clampi(r - 2, 0, 4)

# Engelse naam van hoed i voor "hap_hoed": Brams lijst (kroniek_regels.gd HOED_KORT, zijn toets vergelijkt hem met boek.gd).
const KR := preload("res://systemen/kroniek_regels.gd")
const RG := preload("res://kern/regels.gd")
static func hoed_naam(i: int) -> String:
	return String(KR.HOED_KORT[i]) if i >= 0 and i < KR.HOED_KORT.size() else "hat"

# Een regel uit het Heldenboek: laag, zoals binnenkomst (een nieuwe bladzijde is fijn om te lezen, maar wat je ziet
# gaat voor; Sanne toets 9). Vervalt hij, dan staat hij nog steeds in het boek. Soort "boek" voor de log.
# Demo: geen boekregels (wel in het boek). Zelfs een enkele drukte "Odo climbs into your hole." weg (film 3296de5),
# en Odo is de held met de kroon. In de film komt het boek pas in beeld met het boekje in het paneel (stap 2).
static func boek_regel(s, r: String) -> void:
	if r == "" or s.demo:
		return
	s._kroniek(r, true, "boek")
