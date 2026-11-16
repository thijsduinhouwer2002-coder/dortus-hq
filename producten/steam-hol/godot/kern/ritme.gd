# Het Hol: wanneer de volgende held komt, en het graven in de demo-film (Olaf 15 nov, uit kern/strook.gd gehaald;
# regel: bestand onder ±400). Alleen statische functies met de strook als eerste argument (`s`); de toestand
# (volgende_held, volgende_graaf, lied_helden, rng) blijft in strook.gd. Zelfde volgorde van rng-trekkingen als
# voorheen, dus de film blijft gelijk.
extends RefCounted

const HOL := preload("res://hol/hol.gd")
const DEMO_EINDE := preload("res://kern/demo_einde.gd")
const BEGIN_VLOT := 2                       # zoveel vaste stappen van BEGIN krijgen een kort gat erna (vallen, opgegeten)
const BEGIN_VLOT_S := Vector2(18.0, 22.0)   # seconden tot de volgende held in die gaten (was 35 tot 45)
const BEGIN_HOED_S := Vector2(5.0, 7.0)     # na de eerste held (vallen): zo snel komt de held die Gloop opeet (Bram 16 nov)

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
	elif begin and s.begin_gedaan.size() <= BEGIN_VLOT:
		# Bram 15 nov (ja Olaf 23:30): de eerste hoed op de toren binnen de minuut, ook in het volle spel. Na de held
		# van "vallen" en die van "vluchten" komt de volgende sneller, dus "opgegeten" rond 45 s en de hap rond 60 s
		# (was ±96 s). Zelfde aantal rng-trekkingen als hiervoor; daarna weer 35 tot 45 s en buiten het begin 40 tot 60.
		# Bram 16 nov: "opgegeten" staat nu tweede in BEGIN en komt 5 tot 7 s na de eerste held, dus de hap rond 27 s
		# (hij loopt ±17 s naar Gloop) in plaats van rond 60 s. Daarna 18 tot 22 s tot "vluchten".
		var gat: Vector2 = BEGIN_HOED_S if s.begin_gedaan.size() <= 1 else BEGIN_VLOT_S
		s.volgende_held = s.t + rng.randf_range(gat.x, gat.y)
	else:
		s.volgende_held = s.t + (rng.randf_range(35.0, 45.0) if begin else rng.randf_range(40.0, 60.0))
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
