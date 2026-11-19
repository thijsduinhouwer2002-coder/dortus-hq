// Spelregels van Gloop's Hat Tower, overgezet uit Spel.mc van het horlogespel.
// Zelfde getallen en hetzelfde gevoel; nieuw is wat het een eerlijk dagspel maakt:
// - vaste stap van 4 ms, zodat client en server precies hetzelfde potje uitrekenen;
// - per held een eigen toevalsgetal uit de dagcode, zodat held 7 voor iedereen dezelfde is;
// - mikken loont: voltreffers en reeksen geven extra hoeden, vroeg happen geeft geen tempo;
// - gouden helden (2 hoeden extra) en een dagregel.
// Dit bestand draait in de browser en op de server (geen DOM, geen Node).

export const Toestand = {
  Klaar: 0,
  Valt: 1,
  Slok: 2,
  Weg: 3,
  Wacht: 4,
  Einde: 5,
} as const
export type Toestand = (typeof Toestand)[keyof typeof Toestand]

export const STAP_MS = 4
export const RONDE_MS = 30000
export const RAAK_BOVEN = 780
export const RAAK_ONDER = 850
export const SLOK_MS = 300
export const WEG_MS = 600
/** Te vroeg gehapt: zo lang blijft de bek dicht (horloge 250; hier 350, zodat blind tikken niet loont). */
export const DICHT_MS = 350
/** Een gouden held geeft zoveel hoeden extra. */
export const GOUD_EXTRA = 2
/** Een voltreffer geeft 1 + de reeks hoeden, tot deze grens (2, 3, 4, 4, ...). */
export const REEKS_MAX = 3

/**
 * Hoeveel hoeden een vangst oplevert. Mikken loont: een voltreffer telt dubbel en een reeks
 * voltreffers telt op. Een gewone vangst is 1 hoed, zoals op het horloge.
 */
export function waardeVangst(
  raak: boolean,
  reeks: number,
  goud: boolean,
): number {
  const basis = raak ? 1 + Math.min(reeks, REEKS_MAX) : 1
  return basis + (goud ? GOUD_EXTRA : 0)
}

/** Uitslag per held, voor de uitslagkaart. */
export const Uitslag = {
  Raak: 'perfect',
  Hap: 'gulp',
  Mis: 'miss',
  Goud: 'gold',
} as const
export type Uitslag = (typeof Uitslag)[keyof typeof Uitslag]

export type DagRegel = {
  id: string
  /** Naam in het spel (Engels). */
  naam: string
  /** Korte uitleg in het spel (Engels). */
  uitleg: string
  vangBoven: number
  vangOnder: number
  snelStart: number
  snelMin: number
  snelMax: number
  /** Factor na een vangst. */
  sneller: number
  wachtMin: number
  wachtSpreiding: number
  gouden: number
}

const BASIS: Omit<DagRegel, 'id' | 'naam' | 'uitleg'> = {
  vangBoven: 700,
  vangOnder: 900,
  snelStart: 0.5,
  snelMin: 0.4,
  snelMax: 1.3,
  sneller: 1.06,
  wachtMin: 100,
  wachtSpreiding: 350,
  gouden: 2,
}

export const DAGREGELS: readonly DagRegel[] = [
  {
    ...BASIS,
    id: 'classic',
    naam: 'Classic',
    uitleg: 'The original tower. Two golden heroes.',
  },
  {
    ...BASIS,
    id: 'rush',
    naam: 'Rush Hour',
    uitleg: 'Heroes come quicker. Barely time to swallow.',
    wachtMin: 40,
    wachtSpreiding: 160,
  },
  {
    ...BASIS,
    id: 'heavy',
    naam: 'Heavy Heroes',
    uitleg: 'They fall faster, and every gulp speeds them up more.',
    snelStart: 0.62,
    sneller: 1.08,
    snelMax: 1.4,
  },
  {
    ...BASIS,
    id: 'golden',
    naam: 'Golden Hour',
    uitleg: 'Five golden heroes today. Each one is worth 3 hats.',
    gouden: 5,
  },
  {
    ...BASIS,
    id: 'wide',
    naam: 'Big Mouth',
    uitleg: 'Gloop opens wider, but the perfect spot stays tiny.',
    vangBoven: 660,
    vangOnder: 920,
    snelStart: 0.58,
  },
]

/** Dag 1 is donderdag 19 november 2026 (UTC), de dag dat de port begon. */
export const DAG_EEN_MS = Date.UTC(2026, 10, 19)

export function dagNummer(nuMs: number): number {
  return Math.floor((nuMs - DAG_EEN_MS) / 86400000) + 1
}

export function dagDatum(dag: number): string {
  return new Date(DAG_EEN_MS + (dag - 1) * 86400000).toISOString().slice(0, 10)
}

/** Kleine hash (mulberry-achtig) van een getal naar 0..2^32-1. */
export function meng(a: number): number {
  let t = (a + 0x6d2b79f5) | 0
  t = Math.imul(t ^ (t >>> 15), t | 1)
  t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
  return (t ^ (t >>> 14)) >>> 0
}

export function dagZaad(dag: number): number {
  return meng(dag * 7919 + 1013)
}

export function dagRegel(dag: number): DagRegel {
  // Dag 1 en elke vijfde dag daarna is Classic; verder wisselt het per dag in vaste volgorde
  // na een husseling per week, zodat dezelfde weekdag niet altijd dezelfde regel heeft.
  const week = Math.floor((dag - 1) / DAGREGELS.length)
  const plek =
    (((dag - 1) % DAGREGELS.length) + DAGREGELS.length) % DAGREGELS.length
  const volgorde = [0, 1, 2, 3, 4]
  let z = meng(week * 31 + 7)
  for (let i = volgorde.length - 1; i > 1; i--) {
    z = meng(z)
    const j = 1 + (z % i)
    const a = volgorde[i] as number
    volgorde[i] = volgorde[j] as number
    volgorde[j] = a
  }
  return DAGREGELS[volgorde[plek] as number] as DagRegel
}

/** Welke helden vandaag goud zijn (nummers vanaf 1). */
export function goudenHelden(dag: number): number[] {
  const regel = dagRegel(dag)
  const uit = new Set<number>()
  let z = dagZaad(dag) ^ 0x51ed
  while (uit.size < regel.gouden) {
    z = meng(z)
    uit.add(4 + (z % 20))
  }
  return [...uit].sort((a, b) => a - b)
}

/** Volgorde van de tien hoeden in de toren vandaag (index in de kit). */
export function hoedVolgorde(dag: number): number[] {
  const basis = [4, 1, 9, 5, 2, 0, 6, 7, 3, 8]
  const draai = dagZaad(dag) % basis.length
  return [...basis.slice(draai), ...basis.slice(0, draai)]
}

export type Potje = {
  dag: number
  regel: DagRegel
  goud: ReadonlySet<number>
  toestand: Toestand
  y: number
  snelheid: number
  hoeden: number
  reeks: number
  besteReeks: number
  raak: boolean
  tijdOver: number
  fase: number
  wachtDuur: number
  hapDicht: number
  /** Nummer van de held die nu valt (vanaf 1). */
  held: number
  stap: number
  inhaal: number
  /** Hoeden van de laatste vangst (voor het scherm en de vliegende hoeden). */
  winst: number
  uitslagen: Uitslag[]
  /** Stappen waarop gedrukt is, voor de controle op de server. */
  drukken: number[]
  /** Telt op bij elke gebeurtenis, zodat het scherm geluid en beeld kan starten. */
  laatste: {
    soort: 'raak' | 'hap' | 'mis' | 'lucht' | 'einde' | null
    teller: number
  }
}

export function nieuwPotje(dag: number): Potje {
  const regel = dagRegel(dag)
  return {
    dag,
    regel,
    goud: new Set(goudenHelden(dag)),
    toestand: Toestand.Klaar,
    y: 0,
    snelheid: regel.snelStart,
    hoeden: 0,
    reeks: 0,
    besteReeks: 0,
    raak: false,
    tijdOver: RONDE_MS,
    fase: 0,
    wachtDuur: 300,
    hapDicht: 0,
    held: 0,
    stap: 0,
    inhaal: 0,
    winst: 0,
    uitslagen: [],
    drukken: [],
    laatste: {soort: null, teller: 0},
  }
}

function meld(p: Potje, soort: Potje['laatste']['soort']): void {
  p.laatste = {soort, teller: p.laatste.teller + 1}
}

export function begin(p: Potje): void {
  const vers = nieuwPotje(p.dag)
  Object.assign(p, vers, {laatste: {soort: null, teller: p.laatste.teller}})
  nieuweHeld(p)
}

function nieuweHeld(p: Potje): void {
  p.toestand = Toestand.Valt
  p.y = 0
  p.fase = 0
  p.held += 1
}

export function inVangzone(p: Potje): boolean {
  return p.y >= p.regel.vangBoven && p.y <= p.regel.vangOnder
}

export function isGoud(p: Potje): boolean {
  return p.goud.has(p.held)
}

/** Eén druk (tik, klik, spatie). Alleen tijdens het spel telt hij mee voor de controle. */
export function druk(p: Potje): void {
  if (p.toestand === Toestand.Klaar || p.toestand === Toestand.Einde) return
  p.drukken.push(p.stap)
  if (p.toestand !== Toestand.Valt || p.hapDicht > 0) return
  if (inVangzone(p)) {
    const goud = isGoud(p)
    p.raak = p.y >= RAAK_BOVEN && p.y <= RAAK_ONDER
    p.reeks = p.raak ? p.reeks + 1 : 0
    p.winst = waardeVangst(p.raak, p.reeks, goud)
    p.hoeden += p.winst
    p.besteReeks = Math.max(p.besteReeks, p.reeks)
    // Vroeg vangen geeft geen tempo: de pauze erna duurt zolang de held nog tot de onderkant van de
    // bek had moeten vallen. Zo levert vroeg happen (blind tikken) geen extra helden op.
    p.inhaal = Math.round((p.regel.vangOnder - p.y) / p.snelheid)
    p.snelheid = Math.min(p.snelheid * p.regel.sneller, p.regel.snelMax)
    p.uitslagen.push(goud ? Uitslag.Goud : p.raak ? Uitslag.Raak : Uitslag.Hap)
    p.toestand = Toestand.Slok
    p.fase = 0
    meld(p, p.raak ? 'raak' : 'hap')
  } else {
    // Te vroeg: Gloop hapt in de lucht en heeft even zijn bek dicht. Kost niets.
    p.hapDicht = DICHT_MS
    // Kost geen hoed, wel de reeks: wie blind tikt, bouwt nooit een reeks voltreffers op.
    p.reeks = 0
    meld(p, 'lucht')
  }
}

/** Wachttijd na held n, voor iedereen gelijk op dezelfde dag. */
function wachtNa(p: Potje): number {
  return (
    p.regel.wachtMin +
    (meng(dagZaad(p.dag) + p.held * 104729) % p.regel.wachtSpreiding)
  )
}

/** Eén vaste stap van STAP_MS. */
export function stap(p: Potje): void {
  if (p.toestand === Toestand.Klaar || p.toestand === Toestand.Einde) {
    p.fase += STAP_MS
    return
  }
  p.stap += 1
  const dt = STAP_MS
  p.tijdOver -= dt
  if (p.tijdOver <= 0) {
    p.tijdOver = 0
    p.toestand = Toestand.Einde
    p.fase = 0
    meld(p, 'einde')
    return
  }
  if (p.hapDicht > 0) p.hapDicht = Math.max(0, p.hapDicht - dt)
  if (p.toestand === Toestand.Valt) {
    p.y += p.snelheid * dt
    if (p.y > p.regel.vangOnder) {
      // Gemist: de held loopt weg, de volgende valt iets langzamer. Nooit een hoed kwijt.
      p.toestand = Toestand.Weg
      p.fase = 0
      p.reeks = 0
      p.snelheid = Math.max(p.snelheid * 0.85, p.regel.snelMin)
      p.uitslagen.push(Uitslag.Mis)
      meld(p, 'mis')
    }
  } else if (p.toestand === Toestand.Slok) {
    p.fase += dt
    if (p.fase >= SLOK_MS) wacht(p)
  } else if (p.toestand === Toestand.Weg) {
    p.fase += dt
    if (p.fase >= WEG_MS) wacht(p)
  } else if (p.toestand === Toestand.Wacht) {
    p.fase += dt
    if (p.fase >= p.wachtDuur) nieuweHeld(p)
  }
}

function wacht(p: Potje): void {
  p.toestand = Toestand.Wacht
  p.fase = 0
  p.wachtDuur = wachtNa(p) + p.inhaal
  p.inhaal = 0
}

/** Speelt een heel potje na uit de stappen waarop gedrukt is. Gebruikt door de server. */
export function speelNa(dag: number, drukken: readonly number[]): Potje {
  const p = nieuwPotje(dag)
  begin(p)
  let i = 0
  while (p.toestand !== Toestand.Einde) {
    while (i < drukken.length && drukken[i] === p.stap) {
      druk(p)
      i++
    }
    stap(p)
  }
  return p
}
