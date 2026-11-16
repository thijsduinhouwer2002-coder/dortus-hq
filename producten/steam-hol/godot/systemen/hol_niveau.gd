extends RefCounted
class_name HolNiveau
# Hol-niveau (Olaf, 16 nov), naar Sanne `platformen/steam/voortgang.md` spoor 1 en Brams geijkte drempels
# (`producten/steam-hol/sim/voortgang-lagen-bram.json`, gelijk aan Sanne versie 3 tot niveau 20).
# Faam = gevangen helden (1 per held), ook als je weg was (voortgang.gd, kwart snelheid). Faam gaat nooit omlaag.
# Alleen de rekenkant: het bordje en het feestje tekent Mila, keuring Daan. Wat er per niveau echt bijkomt
# (ridder op 3, vleermuis op 4, ...) wordt pas aangesloten als Sanne en Daan dat voor de demo vastzetten.

# DREMPEL[i] = faam die nodig is voor niveau i + 1 (niveau 1 bij 0 faam)
# Hol 3, 4 en 6 omlaag naar 5 / 7 / 17 (Olaf 16 nov 18:35, voorstel Sanne 18:10, advies Bram 18:50 voor de speeltestbuild:
# graven gratis, upgrades 45/126/353, de eerste upgrade valt op vangst 4, dus geen drempel op 4; niets valt meer samen
# behalve hol 5 soms (3 van 40), ergste gat minuut 1 tot 20 van 11,8 naar 10,7 min, mediaan 7,0 naar 6,1; sim/samenval.py deel 3).
# Bij de v3-economie (graven kost goud) opnieuw kijken: daar gaf Bram 3/4/7/12/16.
const DREMPEL := [0, 3, 5, 7, 12, 17, 25, 31, 39, 53, 69, 88]
const DEMO_MAX := 12
# Titel per niveau ("Level 5: a tavern tale. 4 heroes to go."), Engels (winkeltaal).
# Titels in plaats van wat er bijkomt (voorstel Sanne 16 nov 19:00, ja Daan 19:50): in de speeltestbuild ontgrendelt een
# niveau nog niets (soorten na 10 helden in binnenkomst.gd, vleermuis en putten vanaf het begin), dus de oude namen
# (the Rolling Stone, the Noble, ...) beloofden dingen die niet kwamen. Oude lijst voor later: voortgang.md spoor 1.
const WAT := ["", "a damp hole", "a local rumor", "a known hazard", "a bad idea", "a tavern tale",
	"a hat museum", "a hero shortage", "a no-go zone", "a dare", "a local legend", "a royal problem", "Gloop's Empire"]

static func niveau(faam: int) -> int:
	var n := 1
	for i in DREMPEL.size():
		if faam >= int(DREMPEL[i]):
			n = i + 1
	return mini(n, DEMO_MAX)

# Faam uit één keer weg: hooguit tot net de drempel van huidig niveau + 2 (Sanne 16 nov 22:00, balans.md punt 2).
# Goud, hoeden en het verhaal van de nacht veranderen niet; alleen de faam boven die drempel telt niet.
const WEG_NIVEAUS := 2
static func weg_faam(faam_voor: int, n: int) -> int:
	var doel := niveau(faam_voor) + WEG_NIVEAUS   # niveau L begint op DREMPEL[L - 1]
	if doel - 1 >= DREMPEL.size():
		return maxi(0, n)
	return clampi(n, 0, maxi(0, int(DREMPEL[doel - 1]) - faam_voor))

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

# "Level 5: a tavern tale. 4 heroes to go." (hover op het bordje, Daan 16 nov 18:40); op het laatste niveau zonder staart.
# Langste geval: "Level 10: a local legend. 16 heroes to go." (42 tekens); grens blijft 43.
const HOVER_MAX := 43
static func hover(faam: int) -> String:
	var n := niveau(faam)
	var naam: String = WAT[n] if n < WAT.size() else ""
	var r := "Level %d: %s." % [n, naam]
	var rest := nog(faam)
	if rest > 0:
		r += " %d hero%s to go." % [rest, "" if rest == 1 else "es"]
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
# Daan 16 nov 16:50: het bordje staat, de regels mogen aan.
const REGELS_AAN := true

static func soort(n: int) -> String:
	return String(SOORT[n]) if n >= 0 and n < SOORT.size() else ""

# Gewone niveauregel van het feestje: "Hole level 4: a bad idea."
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
const RIJ_REGEL := "%d more to come as you play."   # Daan 16:50 (niveaus staan niet aan een deur)
const NAAM_MAX := 34   # gelijk aan kaartje.gd DOEL_MAX

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
	# Bij meer niveaus tegelijk geen "Grew N levels while you were away." meer (Iris keuring 6 tot 8, ja Daan 16 nov 20:50):
	# het bordje en de optocht laten het al zien. weg_regel() houdt de oude tekst voor wie hem nog vraagt.
	if meteen.size() == 1:
		regels.append(niveau_regel(meteen[0]))
	if rij > 0:
		regels.append(rij_regel(rij))
	return {"meteen": meteen, "rij": rij, "regels": regels, "optocht": plan(meteen)}

static func rij_regel(rij: int) -> String:
	return RIJ_REGEL % rij

# Naam van het volgende niveau uit de rij met de wachttijd (Iris 17:40: noem wat er komt, geen "door"):
# "Next: the Thief, in 2 min"; past het niet in NAAM_MAX, dan "Next: level 13, in 2 min".
static func rij_volgende(faam: int, rij: int, rij_t: float) -> String:
	var min_ := maxi(1, ceili((RIJ_S - rij_t) / 60.0))
	var n := zichtbaar(faam, rij) + 1
	var naam: String = String(WAT[n]) if n < WAT.size() else ""
	var r := "Next: %s, in %d min" % [naam, min_]
	if naam == "" or r.length() > NAAM_MAX:
		r = "Next: level %d, in %d min" % [n, min_]
	return r

# Hover op het bordje met iets in de rij: "7 more to come. Next: a second pit, in 2 min."
static func rij_hover(faam: int, rij: int, rij_t: float) -> String:
	return "%d more to come. %s." % [rij, rij_volgende(faam, rij, rij_t)]

# Doelregel (d): "Next: a second pit, in 2 min"
static func rij_doel(faam: int, rij: int, rij_t: float) -> String:
	return rij_volgende(faam, rij, rij_t)
