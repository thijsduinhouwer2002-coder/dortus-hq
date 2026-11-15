# Het Hol: wanneer de volgende held komt, en het graven in de demo-film (Olaf 15 nov, uit kern/strook.gd gehaald;
# regel: bestand onder ±400). Alleen statische functies met de strook als eerste argument (`s`); de toestand
# (volgende_held, volgende_graaf, lied_helden, rng) blijft in strook.gd. Zelfde volgorde van rng-trekkingen als
# voorheen, dus de film blijft gelijk.
extends RefCounted

const HOL := preload("res://hol/hol.gd")
const DEMO_EINDE := preload("res://kern/demo_einde.gd")

static func tik_held(s, helden: int) -> void:
	if s.t < s.volgende_held or helden >= 3:
		return
	var begin: bool = s._begin_stap() != ""
	if not s._nieuwe_held():
		s.volgende_held = s.t + 2.0   # een vaste stap moet nog even wachten
		return
	var rng: RandomNumberGenerator = s.rng
	# ritme: gemiddeld een held per ±50 s (balans.md), in de eerste tien minuten ±40 s;
	# in de demo sneller zodat de film van een minuut iets laat zien
	if s.demo:
		s.volgende_held = s.t + (rng.randf_range(5.0, 7.0) if begin else rng.randf_range(6.0, 9.0))
	else:
		s.volgende_held = s.t + (rng.randf_range(35.0, 45.0) if begin else rng.randf_range(40.0, 60.0))
	# na het lied van een bard: de volgende helden komen 8 tot 20 s na elkaar (Bram 02:30); in de demo blijft het
	# eigen snelle ritme staan (dat is al korter), alleen de teller loopt af
	if s.lied_helden > 0:
		s.lied_helden -= 1
		if s.lied_helden > 0 and not s.demo:
			s.volgende_held = s.t + rng.randf_range(8.0, 20.0)

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
