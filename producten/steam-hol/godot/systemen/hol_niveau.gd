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

# --- Optocht na weg zijn (Sanne 16 nov 14:50) -----------------------------------------------------------------
# De eerste nacht mag het hol van 2 naar 12 tillen, maar als één optocht, niet tien feestjes:
# na de weg-telling wipt het bordje één keer, dan verschijnt elk nieuw ding met de poef van graven, van laag naar hoog,
# 1,2 s na elkaar (meer dan 10 dingen: 0,6 s), samen hooguit 12 s. Niveaus zonder iets om te zien slaan over.
# Een nieuwe heldensoort komt als eerstvolgende bezoeker binnen (in volgorde), niet met een poef.
# Muntjes uit de schat alleen bij het eerste en laatste ding. Klikken mag tijdens de optocht (dit is alleen een plan).
# Soort per niveau (voortgang.md spoor 1): "poef" = iets nieuws in het hol, "held" = nieuwe heldensoort,
# "" = niets om te zien in de strook (Heldenboek, iets dat alleen te koop komt).
const SOORT := ["", "", "", "held", "poef", "held", "", "", "held", "poef", "held", "held", "poef"]
const OPTOCHT_STAP_S := 1.2
const OPTOCHT_STAP_VOL_S := 0.6
const OPTOCHT_VOL := 10
const OPTOCHT_MAX_S := 12.0
const WEG_REGEL := "Grew %d levels while you were away."
# Moet Daan 16 nov 15:33: geen niveautekst in de kroniek zolang er nergens een niveau te zien is.
# Zet op true zodra Mila's bordje in het spel staat en Daan de regel weer goed vindt. De rekenkant blijft gewoon werken.
const REGELS_AAN := false

static func soort(n: int) -> String:
	return String(SOORT[n]) if n >= 0 and n < SOORT.size() else ""

# Gewone niveauregel van het feestje: "Hole level 4: a bat moves in."
static func niveau_regel(n: int) -> String:
	var naam: String = WAT[n] if n >= 0 and n < WAT.size() else ""
	return "Hole level %d: %s." % [n, naam]

# Eén kroniekregel na weg zijn: "" als er geen niveau bijkwam, bij één niveau de gewone niveauregel.
static func weg_regel(oud_faam: int, nieuw_faam: int) -> String:
	var bij := erbij(oud_faam, nieuw_faam)
	if bij.is_empty():
		return ""
	if bij.size() == 1:
		return niveau_regel(bij[0])
	return WEG_REGEL % bij.size()

# Het plan van de optocht. Uit: {"wip": bool, "poef": [{niveau, wat, t, munt}], "helden": [niveau, ...], "duur": s}.
# t = seconden na de wip. Leeg (wip false) als er geen niveau bijkwam.
static func optocht(oud_faam: int, nieuw_faam: int) -> Dictionary:
	return plan(erbij(oud_faam, nieuw_faam))

# Het plan voor een rij niveaus (oplopend).
static func plan(bij: Array[int]) -> Dictionary:
	var poef: Array = []
	var helden: Array[int] = []
	for n in bij:
		match soort(n):
			"poef":
				poef.append({"niveau": n, "wat": String(WAT[n]), "t": 0.0, "munt": false})
			"held":
				helden.append(n)
	var stap := OPTOCHT_STAP_S if poef.size() <= OPTOCHT_VOL else OPTOCHT_STAP_VOL_S
	if poef.size() > 0:
		stap = minf(stap, OPTOCHT_MAX_S / float(poef.size()))
	for i in poef.size():
		poef[i].t = snappedf(stap * float(i + 1), 0.01)   # de eerste poef 1 stap na de wip
		poef[i].munt = i == 0 or i == poef.size() - 1
	var duur: float = poef[-1].t if not poef.is_empty() else 0.0
	return {"wip": not bij.is_empty(), "poef": poef, "helden": helden, "duur": duur}

# --- Rij bij de ingang (Sanne 16 nov 16:00, voortgang.md "Versie 3 definitief" punt 5) ---------------------------
# Per keer weg hooguit WEG_MEETEN hol-niveaus meteen (in de optocht); de rest wacht in de rij. Faam blijft helemaal binnen.
# Elk volgend niveau uit de rij komt na RIJ_S seconden open spelen (de rij wacht als de app dicht is).
# Zichtbaar niveau = niveau(faam) - rij: eigen vangsten tellen gewoon door.
const WEG_MEETEN := 4
const RIJ_S := 180.0
const RIJ_REGEL := "%d more levels wait at the door."

static func zichtbaar(faam: int, rij: int) -> int:
	return maxi(1, niveau(faam) - maxi(0, rij))

# Na weg zijn. Uit: {"meteen": [niveaus], "rij": nieuwe rij, "regels": [kroniekregels], "optocht": plan}.
static func weg(oud_faam: int, nieuw_faam: int, rij_voor: int) -> Dictionary:
	var van := zichtbaar(oud_faam, rij_voor)
	var tot := niveau(nieuw_faam)
	var meteen: Array[int] = []
	for n in range(van + 1, mini(tot, van + WEG_MEETEN) + 1):
		meteen.append(n)
	var rij := maxi(0, tot - van - meteen.size())
	var regels: Array[String] = []
	if meteen.size() == 1:
		regels.append(niveau_regel(meteen[0]))
	elif meteen.size() > 1:
		regels.append(WEG_REGEL % meteen.size())
	if rij > 0:
		regels.append(rij_regel(rij))
	return {"meteen": meteen, "rij": rij, "regels": regels, "optocht": plan(meteen)}

static func rij_regel(rij: int) -> String:
	return "1 more level waits at the door." if rij == 1 else RIJ_REGEL % rij

# Hover op het bordje met iets in de rij: "7 levels waiting. Next in 2 min."
static func rij_hover(rij: int, rij_t: float) -> String:
	var min_ := maxi(1, ceili((RIJ_S - rij_t) / 60.0))
	return "%d level%s waiting. Next in %d min." % [rij, "" if rij == 1 else "s", min_]

# Doelregel (d): "Level 6 at the door: 2 min"
static func rij_doel(faam: int, rij: int, rij_t: float) -> String:
	var min_ := maxi(1, ceili((RIJ_S - rij_t) / 60.0))
	return "Level %d at the door: %d min" % [zichtbaar(faam, rij) + 1, min_]
