extends RefCounted
class_name Voortgang
# Voortgang terwijl je weg bent (Bram). Regels van Thijs: nooit straffen als je weg bent, niets kwijtraken,
# geen dagelijkse plicht. Dus: bij openen rekenen we uit hoeveel helden er kwamen en hoeveel goud ze achterlieten.
# - Alleen winst, nooit verlies (ontsnapte helden nemen niets mee).
# - Klok terugzetten: verstreken tijd < 0 telt als 0, en de bewaarde tijd gaat nooit achteruit.
# - Plafond van 12 uur: wie een week weg is krijgt niet meer dan wie een nacht weg was, zodat
#   niemand zich verplicht voelt om dagelijks te kijken, en klok vooruitzetten niets oplevert boven die 12 uur.
# - Vast zaad: dezelfde save en dezelfde tijd geven dezelfde uitkomst (geen herladen om beter te gooien).

const PLAFOND_S := 12 * 3600
const HELD_ELKE_S := 47.5          # gemiddeld, zelfde orde als in het spel (25 tot 70 s)

# vallen: aantal vallen, bewoners: aantal bewoners. Meer verdediging = meer helden vallen.
static func reken(laatst_unix: int, nu_unix: int, vallen: int, bewoners: int, zaad: int) -> Dictionary:
	var weg := nu_unix - laatst_unix
	var teruggezet := weg < 0
	weg = clampi(weg, 0, PLAFOND_S)
	var helden := int(floor(weg / HELD_ELKE_S))
	var kans_val := clampf(0.15 + 0.12 * vallen + 0.10 * bewoners, 0.0, 0.85)
	var rng := RandomNumberGenerator.new()
	rng.seed = hash([zaad, laatst_unix, helden])
	var gevallen := 0
	var goud := 0
	for i in helden:
		if rng.randf() < kans_val:
			gevallen += 1
			goud += rng.randi_range(3, 9)
		else:
			goud += 1   # wie vlucht, laat in de haast één munt vallen
	var nieuwe_laatst := maxi(laatst_unix, nu_unix)
	return {
		"weg_s": weg, "helden": helden, "gevallen": gevallen, "gevlucht": helden - gevallen,
		"goud": goud, "nieuwe_laatst": nieuwe_laatst, "teruggezet": teruggezet,
		"regel": samenvatting(weg, helden, gevallen, goud),
	}

static func samenvatting(weg: int, helden: int, gevallen: int, goud: int) -> String:
	if helden == 0:
		return "All quiet while you were away."
	var tijd := "%d min" % int(weg / 60.0) if weg < 3600 else "%d h" % int(weg / 3600.0)
	return "While you were away (%s): %d heroes came, %d fell, %d fled. +%d gold." % [tijd, helden, gevallen, helden - gevallen, goud]
