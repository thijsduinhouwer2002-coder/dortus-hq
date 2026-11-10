extends RefCounted
const VOORTGANG := preload("res://systemen/voortgang.gd")   # met_pensioen (Bram 04:35)
# Deel van kern/strook.gd (Olaf), losgehaald bij het opruimen van 10 nov (strook.gd was 650 regels).
# Statische functies; `s` is de strook. Gedrag gelijk aan voor het splitsen (film.log gelijk).

static func held_klaar(s, _held, uitkomst: String, info: Dictionary) -> void:
	var b := info.duplicate()
	b["kleur"] = (info.kleur as Color).to_html(false)
	b["hoed"] = (info.hoed as Color).to_html(false)
	for v in ["moet_vallen", "moet_vluchten", "moet_doorlopen", "moet_opgegeten", "hoed_naar", "hoeden_bewoner", "schat_gemeld", "snelheid", "demo_clou", "lied", "dutje", "dutje_gemeld", "lied_held", "hoed_gemeld"]:
		b.erase(v)
	b.erase("wat")
	if uitkomst == "ontsnapt":
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
			s._kroniek(s.regels.kies("vlucht", {"naam": info.naam, "bewoner": w.replace(" the Slime", "") if w != "your Hoard" else "you"}))
		boek_regel(s, s.boek.held(String(info.get("soort_held", "")), "ontsnapt", String(info.naam), s._bewoner()))
		if lied > 0:
			# sfeerregel: je ziet het lied niet, dus laag zoals binnenkomst en mag vervallen (Sanne toets 9, besluit 2a);
			# de afloop zie je wel: de helden die erdoor komen krijgen een eigen regel die voorgaat (binnen_lied, strook.gd)
			s._kroniek(s.regels.kies("lied", {"naam": info.naam}), true, "lied")
			s.lied_helden += lied
			if not s.demo:
				s.volgende_held = minf(s.volgende_held, s.t + s.rng.randf_range(8.0, 20.0))
	else:
		# goud per val: 6, plus 3 per eerder bezoek; een held met een wrok is een beloning (balans.md punt 1, besluit Olaf)
		var buit := 6 + 3 * int(info.get("bezoeken", 0))
		s.hol.goud += buit
		var naam: String = String(info.naam)
		var basis := naam.split(" ")[0]
		s.gevallen_namen[basis] = int(s.gevallen_namen.get(basis, 0)) + 1
		s.hol.munt_regen(s.hol.pos_naar_cel(_held.position).x)
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
				r = s.regels.kies("val_bewoner", {"naam": naam, "bewoner": s._bewoner()}, extra.length())
		else:
			r = s.regels.kies("val", {"naam": naam, "val": wat.replace("fell to ", "")}, extra.length())
		s._kroniek(r + extra)
		# Heldenboek: een stempel door Gloop of door de put (bij afgerekend: wie hem kreeg)
		# (put alleen als het echt de put was; anders Gloop, ook als zijn bijnaam net veranderde, controleur kan-punt 6)
		var door := "stekelput" if wat.ends_with("the Spike Pit") else "slijm"
		boek_regel(s, s.boek.held(String(info.get("soort_held", "")), door, naam, s._bewoner()))
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
