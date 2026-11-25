# Het Hol: wanneer de volgende held komt, en het graven in de demo-film (Olaf 15 nov, uit kern/strook.gd gehaald;
# regel: bestand onder ±400). Alleen statische functies met de strook als eerste argument (`s`); de toestand
# (volgende_held, volgende_graaf, lied_helden, rng) blijft in strook.gd. Zelfde volgorde van rng-trekkingen als
# voorheen, dus de film blijft gelijk.
extends RefCounted

const HOL := preload("res://hol/hol.gd")
const DEMO_EINDE := preload("res://kern/demo_einde.gd")
const KAARTJE := preload("res://kern/kaartje.gd")
const UPG := preload("res://systemen/upgrades.gd")
const BEGIN_VLOT := 2                       # zoveel vaste stappen van BEGIN krijgen een kort gat erna (vallen, opgegeten)
const BEGIN_VLOT_S := Vector2(18.0, 22.0)   # seconden tot de volgende held in die gaten (was 35 tot 45)
const BEGIN_HOED_S := Vector2(5.0, 7.0)     # na de eerste held (vallen): zo snel komt de held die Gloop opeet (Bram 16 nov)

const HELD_S := Vector2(28.0, 38.0)          # buiten de demo, na BEGIN-stap 3 en buiten het begin (Sanne 16 nov 20:00, was 35-45 en 40-60)
const PAAR_KANS := 0.15                       # zo vaak komt de volgende held kort na de vorige (Sanne 16 nov 20:00)
const PAAR_S := Vector2(6.0, 10.0)            # gat bij zo'n paar
const MAX_TEGELIJK := 2                       # gewoon spel: hooguit 2 helden tegelijk (Sanne 16 nov 20:10, was 3); demo en drukte 3

# Telt de helden in beeld (uit strook.gd _process gehaald, issue #79). Hoard-Toucher: de regel komt op het moment
# dat hij de schat aanraakt, niet pas als hij ontsnapt (toets 5); "hoard_toucher" blijft in de save voor de bijnaam,
# dus we kijken naar "wat". Slaapkop (Bram, versie 1): zijn dutje een lage regel, zoals binnenkomst.
static func tel_helden(s) -> int:
	var helden := 0
	for w in s.wezens.get_children():
		if not w.has_method("is_held"):
			continue
		helden += 1
		var hi = w.get("info")
		if not (hi is Dictionary):
			continue
		if String(hi.get("wat", "")).begins_with("touched") and not hi.has("schat_gemeld"):
			hi["schat_gemeld"] = true
			s._kroniek(s.regels.kies("schat", {"naam": hi.get("naam", "")}))
		if bool(hi.get("dutje", false)) and not hi.has("dutje_gemeld"):
			hi["dutje_gemeld"] = true
			s._kroniek(s.regels.kies("dutje", {"naam": hi.get("naam", "")}), true)
	return helden

static func max_tegelijk(s) -> int:
	return 3 if (s.demo or s.get("proef_drukte") == true) else MAX_TEGELIJK

static func tik_held(s, helden: int) -> void:
	if s.t < s.volgende_held or helden >= max_tegelijk(s):
		return
	var begin: bool = s._begin_stap() != ""
	if not s._nieuwe_held():
		s.volgende_held = s.t + 2.0   # een vaste stap moet nog even wachten
		return
	var rng: RandomNumberGenerator = s.rng
	# ritme: gemiddeld een held per ±30 s (Sanne 16 nov 20:00, balans.md);
	# in de demo sneller zodat de film van een minuut iets laat zien
	if s.demo:
		s.volgende_held = s.t + (rng.randf_range(5.0, 7.0) if begin else rng.randf_range(6.0, 9.0))
	elif begin and s.begin_gedaan.size() <= BEGIN_VLOT:
		# Bram 15 nov (ja Olaf 23:30): de eerste hoed op de toren binnen de minuut, ook in het volle spel. Na de held
		# van "vallen" en die van "vluchten" komt de volgende sneller, dus "opgegeten" rond 45 s en de hap rond 60 s
		# (was ±96 s). Zelfde aantal rng-trekkingen als hiervoor; daarna weer 35 tot 45 s en buiten het begin 40 tot 60.
		# Bram 16 nov: "opgegeten" staat nu tweede in BEGIN en komt 5 tot 7 s na de eerste held, dus de hap rond 27 s
		# (hij loopt ±17 s naar Gloop) in plaats van rond 60 s. Daarna 18 tot 22 s tot "vluchten".
		var gat: Vector2 = BEGIN_HOED_S if s.begin_gedaan.size() <= 1 else BEGIN_VLOT_S
		s.volgende_held = s.t + rng.randf_range(gat.x, gat.y)
	else:
		# Sanne 16 nov 20:00: 28 tot 38 s, en buiten een BEGIN-stap 15% kans op een paar (6 tot 10 s). De extra trekking
		# zit alleen in deze tak (niet in de demo), dus de demo-film blijft gelijk.
		s.volgende_held = s.t + rng.randf_range(HELD_S.x, HELD_S.y)
		if not begin and s.lied_helden <= 0 and rng.randf() < PAAR_KANS:
			s.volgende_held = s.t + rng.randf_range(PAAR_S.x, PAAR_S.y)
	# na het lied van een bard: de volgende helden komen 8 tot 20 s na elkaar (Bram 02:30); in de demo blijft het
	# eigen snelle ritme staan (dat is al korter), alleen de teller loopt af
	if s.lied_helden > 0:
		s.lied_helden -= 1
		if s.lied_helden > 0 and not s.demo:
			s.volgende_held = s.t + rng.randf_range(8.0, 20.0)
	# drukte=1 (winkelopname week, Mila 16 nov punt 3): drie helden tegelijk in beeld. Een held loopt ±17 s door de gang,
	# dus elke 5 tot 8 s een nieuwe geeft er meestal drie (tik_held laat er nooit meer dan 3 toe). Alleen met het argument.
	if s.get("proef_drukte") == true and not s.demo:
		s.volgende_held = s.t + rng.randf_range(5.0, 8.0)

# demo: om en om een stuk gang erbij en een kamer boven de gang, zodat de film graven laat zien
static func tik_demo_graaf(s) -> void:
	if s.t < s.volgende_graaf:
		return
	s.volgende_graaf = s.t + 9.0
	var hol = s.hol
	var k: int = hol.ingang_kol - 1
	if DEMO_EINDE.weiger(s, "graven (film)"):
		return
	if int(s.t / 9.0) % 2 == 0 and k >= 1:
		hol.klik(hol.cel_naar_pos(Vector2i(k, 0)) - Vector2(0, 6))
		return
	for kk in range(hol.ingang_kol + 2, hol.schat_kol - 1):
		if not hol.boven[kk] and not hol.vallen.has(kk):
			hol.klik(Vector2(kk * HOL.KOL + 8, HOL.OPP + 6))
			break

# koper=1 (Iris keuring 7, alleen met het startargument): een speler die elke upgrade koopt zodra het goud er is,
# via hetzelfde kaartje als een klik (open, Buy). Elke 3 s kijken, niet als er al een kaartje open staat.
static func tik_koper(s) -> void:
	var wacht_aan: bool = float(s.get_meta("koper_wacht", 0.0)) > 0.0
	if s.t < s.volgende_koop or (s.kaart_soort != "" and not wacht_aan):
		return
	s.volgende_koop = s.t + (1.0 if wacht_aan else 3.0)
	var up = s.hol.upgrades
	# koper_wacht=<s> (Mila 25 nov, film voor Iris #7): koopt pas als het al zoveel seconden kan, zoals een mens die
	# eerst de ring en de les ziet en op Gloop klikt. Staat het kaartje van die soort al open, dan koopt hij daar.
	var wacht: float = s.get_meta("koper_wacht", 0.0)
	var sinds: Dictionary = s.get_meta("koper_sinds", {})
	for soort in UPG.SOORTEN:
		if up.kan_kopen(soort, s.hol.goud):
			if not sinds.has(soort):
				sinds[soort] = s.t
				s.set_meta("koper_sinds", sinds)
			if s.t - float(sinds[soort]) < wacht:
				continue
			sinds.erase(soort)
			s.set_meta("koper_sinds", sinds)
			if s.kaart_soort != soort:
				KAARTJE.open(s, soort)
			KAARTJE.koop(s)
			return
		elif sinds.has(soort):
			sinds.erase(soort)
			s.set_meta("koper_sinds", sinds)
