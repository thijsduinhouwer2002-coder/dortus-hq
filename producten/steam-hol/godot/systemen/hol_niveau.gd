extends RefCounted
class_name HolNiveau
# Hol-niveau (Olaf, 16 nov), naar Sanne `platformen/steam/voortgang.md` spoor 1 en Brams geijkte drempels
# (`producten/steam-hol/sim/voortgang-lagen-bram.json`, gelijk aan Sanne versie 3 tot niveau 20).
# Faam = gevangen helden (1 per held), ook als je weg was (voortgang.gd, kwart snelheid). Faam gaat nooit omlaag.
# Alleen de rekenkant: het bordje en het feestje tekent Mila, keuring Daan. Wat er per niveau echt bijkomt
# (ridder op 3, vleermuis op 4, ...) wordt pas aangesloten als Sanne en Daan dat voor de demo vastzetten.

# DREMPEL[i] = faam die nodig is voor niveau i + 1 (niveau 1 bij 0 faam)
const DREMPEL := [0, 3, 6, 10, 12, 20, 25, 31, 39, 53, 69, 88]
const DEMO_MAX := 12
# Hover-tekst per niveau ("Level 5: the Thief. 12 more heroes."), Engels (winkeltaal)
const WAT := ["", "Gloop and the pit", "the Hero Book", "the Knight", "a bat moves in", "the Thief",
	"a second pit", "the Rolling Stone", "the Mage", "your banner", "the Noble", "the Bard", "the Hat Wall"]

static func niveau(faam: int) -> int:
	var n := 1
	for i in DREMPEL.size():
		if faam >= int(DREMPEL[i]):
			n = i + 1
	return mini(n, DEMO_MAX)

# Hoeveel helden nog tot het volgende niveau; 0 als het laatste niveau van deze versie bereikt is.
static func nog(faam: int) -> int:
	var n := niveau(faam)
	if n >= DREMPEL.size():
		return 0
	return maxi(0, int(DREMPEL[n]) - faam)

# Balkje: 0,0 tot 1,0 binnen het huidige niveau.
static func deel(faam: int) -> float:
	var n := niveau(faam)
	if n >= DREMPEL.size():
		return 1.0
	var van := int(DREMPEL[n - 1])
	var tot := int(DREMPEL[n])
	return clampf(float(faam - van) / float(tot - van), 0.0, 1.0)

# "Level 5: the Thief. 12 more heroes." (hover op het bordje); op het laatste niveau zonder "more".
static func hover(faam: int) -> String:
	var n := niveau(faam)
	var naam: String = WAT[n] if n < WAT.size() else ""
	var r := "Level %d: %s." % [n, naam]
	var rest := nog(faam)
	if rest > 0:
		r += " %d more hero%s." % [rest, "" if rest == 1 else "es"]
	return r

# Niveaus die erbij kwamen als faam van `oud` naar `nieuw` gaat (voor het feestje en de log), oplopend.
static func erbij(oud: int, nieuw: int) -> Array[int]:
	var uit: Array[int] = []
	for n in range(niveau(oud) + 1, niveau(nieuw) + 1):
		uit.append(n)
	return uit
