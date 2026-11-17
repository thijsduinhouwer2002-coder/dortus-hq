extends RefCounted
# Kroniekregels van Sanne (platformen/steam/kroniek-regels.md) voor de soorten die kern/regels.gd (Olaf) zelf niet heeft.
# Het spel kiest alles via kern/regels.gd kies(): eerst zijn eigen VOORRAAD, dan deze. Eén plek per regel: een soort staat
# hier of daar, nooit op beide (Bram 16 nov, opgeruimd: de dubbele soorten en de oude Kroniek zijn weg, zie git-geschiedenis).
# Afspraken van Sanne: hooguit 42 tekens na invullen, {bewoner} = "Gloop" (kort), {val} = "the Spike Pit".
# Alle tekst die het spel kan tonen staat vast in systemen/toetsen/kroniek_spel.json; toets_systemen vergelijkt hem.

const VOORRAAD := {
	"pensioen": ["{naam} retired. Opened a bakery.", "{naam} retired. Tells tall tales now.",
		"{naam} quit heroing. Sells maps.", "{naam} won't be back. Too scared."],
	# Heldensoorten (Bram 10 nov, versie 1, systemen/heldensoort.gd). Sanne mag ze herschrijven in kroniek-regels.md.
	"binnen_ridder": ["Sir {naam} clanks in.", "Sir {naam} polished his armor for this.", "Sir {naam} is very slow. Very sure."],
	"binnen_dief": ["{naam} the Thief tiptoes in.", "{naam} sneaks in. Nobody saw. You saw.", "{naam} picks the lock. It was open."],
	"binnen_magier": ["{naam} the Wizard sniffs for traps.", "{naam} casts Light. It is a candle.", "{naam} knows every trap. Almost."],
	"binnen_bard": ["{naam} the Bard tunes his lute.", "{naam} hums on the way in.", "{naam} is here for a story."],
	"binnen_slaapkop": ["{naam} yawns. Long walk.", "{naam} brought a pillow.", "{naam} the Sleepy shuffles in."],
	"binnen_wraakzuchtig": ["{naam} holds grudges. Hard.", "{naam} the Spiteful is here.", "{naam} keeps a list of names."],
	"binnen_opschepper": ["{naam} tells everyone he slew a dragon.", "{naam} the Boastful struts in.", "{naam} signs autographs. Nobody asked."],
	"dutje": ["{naam} took a nap in your hole.", "{naam} snored. Gloop watched.", "{naam} slept. Rude."],
	# Een bard die ontsnapt zingt over je hol: er komen helden bij (heldensoort.LIED_HELDEN).
	"lied": ["{naam} sang about your hole. More came.", "{naam}'s song got popular. Uh oh.", "A song about you! Heroes on the way."],
	# Sanne toets 9 punt 2b: hap en hoed in één regel op het moment van de hap ({hoed} = "crown", "bucket"...), zo komt de
	# hoed-regel niet 4 tot 6 s na de hap. Eerste hoed altijd de eerste regel. Kies via hap_regel() hieronder.
	"hap_hoed_eerste": ["{bewoner} ate {naam}. Kept the {hoed}."],
	"hap_hoed": ["{bewoner} ate {naam}. Kept the {hoed}.", "{bewoner} ate {naam}. The {hoed} fits.",
		"{bewoner} ate {naam}. Wears the {hoed} now.", "{naam} is gone. The {hoed} stays.", "{bewoner} ate {naam}, saved the {hoed}."],
	# Sanne toets 9 punt 3 (kroniek-regels.md, "Binnenkomst na het lied van een bard"): de afloop van het lied, vervalt niet.
	"binnen_lied": ["{naam} heard the song. Came to see.", "{naam} hums the song. Off-key.", "{naam} knows all the words. Sadly.",
		"{naam} came for the gold in the song.", "{naam} asks if this is the song hole."],
}

# Hoednamen voor in een regel, zelfde volgorde als held_hoeden.png en boek.gd HOED_NAMEN (toets vergelijkt ze).
const HOED_KORT := ["helmet", "pointy hat", "hood", "cap", "crown", "chef's hat", "bucket", "top hat", "pan", "feather cap"]

# Vullen voor de toetsen (lengte na invullen); {Val} = {val} met een hoofdletter.
static func vul(sjabloon: String, v: Dictionary) -> String:
	var r := sjabloon
	for sleutel in ["held", "naam", "bewoner", "val", "n", "bijnaam", "oud", "hoed"]:
		r = r.replace("{%s}" % sleutel, str(v.get(sleutel, "")))
	var val := str(v.get("val", ""))
	r = r.replace("{Val}", val.substr(0, 1).to_upper() + val.substr(1))
	return r
