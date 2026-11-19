// Alles wat de server doet, los van Devvit, zodat het lokaal en in de toets draait.
// Opslag gaat via Opslag: op Reddit is dat Redis (redis-opslag.ts), lokaal een Map (geheugen-opslag.ts).
import type {
  GemeenschapStand,
  InitRsp,
  RijRanglijst,
  ScoreReq,
  ScoreRsp,
  StartReq,
  StartRsp,
  UitslagOpslag,
} from '../shared/api.ts'
import {kaartTekst} from '../shared/kaart.ts'
import {RONDE_MS, STAP_MS, speelNa} from '../shared/spel.ts'

/** Het deel van Redis dat we gebruiken. Zelfde namen en betekenis als @devvit/redis. */
export interface Opslag {
  get(key: string): Promise<string | undefined>
  set(key: string, value: string): Promise<void>
  /** Zet alleen als de sleutel nog niet bestaat; true als deze aanroep hem zette. */
  setNX(key: string, value: string): Promise<boolean>
  incrBy(key: string, value: number): Promise<number>
  zAdd(key: string, member: string, score: number): Promise<void>
  zScore(key: string, member: string): Promise<number | undefined>
  /** Hoogste scores eerst. */
  zTop(key: string, aantal: number): Promise<{member: string; score: number}[]>
  /** Plek (0 = hoogste). */
  zPlekHoog(key: string, member: string): Promise<number | undefined>
  expire(key: string, seconden: number): Promise<void>
}

export type Wie = {
  subreddit: string
  naam: string | undefined
  userId: string | undefined
}

const BEWAAR_DAG_S = 60 * 60 * 24 * 40

const sleutel = {
  rang: (sub: string, dag: number) => `rang:${sub}:${dag}`,
  uitslag: (sub: string, dag: number, user: string) =>
    `uitslag:${sub}:${dag}:${user}`,
  start: (sub: string, dag: number, user: string) =>
    `start:${sub}:${dag}:${user}`,
  hoedenDag: (sub: string, dag: number) => `hoeden:${sub}:${dag}`,
  spelersDag: (sub: string, dag: number) => `spelers:${sub}:${dag}`,
  hoedenOoit: (sub: string) => `hoeden:${sub}:ooit`,
  reeks: (user: string) => `reeks:${user}`,
  beste: (user: string) => `beste:${user}`,
  naam: (user: string) => `naam:${user}`,
}

/** Score in de ranglijst: eerst hoeden, dan beste reeks. */
function rangScore(hoeden: number, reeks: number): number {
  return hoeden * 1000 + Math.min(reeks, 999)
}

export class FoutVerzoek extends Error {
  status: number
  constructor(bericht: string, status = 400) {
    super(bericht)
    this.status = status
  }
}

async function gemeenschap(
  db: Opslag,
  sub: string,
  dag: number,
): Promise<GemeenschapStand> {
  const [a, b, c] = await Promise.all([
    db.get(sleutel.hoedenDag(sub, dag)),
    db.get(sleutel.spelersDag(sub, dag)),
    db.get(sleutel.hoedenOoit(sub)),
  ])
  return {
    hoedenVandaag: Number(a ?? 0),
    spelersVandaag: Number(b ?? 0),
    hoedenOoit: Number(c ?? 0),
  }
}

async function top(
  db: Opslag,
  sub: string,
  dag: number,
): Promise<RijRanglijst[]> {
  const rijen = await db.zTop(sleutel.rang(sub, dag), 10)
  return Promise.all(
    rijen.map(async r => ({
      naam: (await db.get(sleutel.naam(r.member))) ?? 'someone',
      hoeden: Math.floor(r.score / 1000),
      reeks: r.score % 1000,
    })),
  )
}

type Reeks = {laatsteDag: number; dagen: number}

async function leesReeks(db: Opslag, user: string): Promise<Reeks> {
  const ruw = await db.get(sleutel.reeks(user))
  if (!ruw) return {laatsteDag: 0, dagen: 0}
  try {
    return JSON.parse(ruw) as Reeks
  } catch {
    return {laatsteDag: 0, dagen: 0}
  }
}

/** Dagen op rij zoals de speler het nu ziet: telt niet meer als hij gisteren oversloeg. */
function reeksNu(r: Reeks, dag: number): number {
  return r.laatsteDag >= dag - 1 ? r.dagen : 0
}

export async function init(
  db: Opslag,
  wie: Wie,
  dag: number,
): Promise<InitRsp> {
  const sub = wie.subreddit
  let vandaag: UitslagOpslag | undefined
  let dagenOpRij = 0
  let besteOoit = 0
  if (wie.userId) {
    vandaag = await leesUitslag(db, sub, dag, wie.userId)
    dagenOpRij = reeksNu(await leesReeks(db, wie.userId), dag)
    besteOoit = Number((await db.get(sleutel.beste(wie.userId))) ?? 0)
  }
  return {
    dag,
    subreddit: sub,
    naam: wie.naam,
    vandaag,
    dagenOpRij,
    besteOoit,
    gemeenschap: await gemeenschap(db, sub, dag),
    top: await top(db, sub, dag),
    topGisteren: await top(db, sub, dag - 1),
  }
}

/** De uitslag van vandaag, of een lege als de dagbeurt gestart is maar nooit is ingestuurd. */
async function leesUitslag(
  db: Opslag,
  sub: string,
  dag: number,
  user: string,
): Promise<UitslagOpslag | undefined> {
  const ruw = await db.get(sleutel.uitslag(sub, dag, user))
  if (ruw && ruw !== BEZIG) return JSON.parse(ruw) as UitslagOpslag
  if (ruw === BEZIG || (await db.get(sleutel.start(sub, dag, user)))) {
    return {hoeden: 0, besteReeks: 0, uitslagen: [], plek: 0, afgebroken: true}
  }
  return undefined
}

const BEZIG = 'bezig'

/**
 * De dagbeurt begint. Eén sleutel per speler per dag, alleen gezet als hij nog niet bestaat:
 * herladen of een tweede tabblad geeft geen nieuwe dagbeurt, die speelt dan als oefening.
 */
export async function start(
  db: Opslag,
  wie: Wie,
  dagNu: number,
  req: StartReq,
): Promise<StartRsp> {
  if (!wie.userId) throw new FoutVerzoek('log in to save your tower', 401)
  if (req.dag !== dagNu)
    throw new FoutVerzoek('this tower is from another day', 409)
  const key = sleutel.start(wie.subreddit, dagNu, wie.userId)
  const eerste = await db.setNX(key, String(Date.now()))
  await db.expire(key, BEWAAR_DAG_S)
  return {telt: eerste}
}

export async function score(
  db: Opslag,
  wie: Wie,
  dagNu: number,
  req: ScoreReq,
): Promise<ScoreRsp> {
  if (!wie.userId) throw new FoutVerzoek('log in to save your tower', 401)
  // Een ronde die vlak voor middernacht (UTC) begon, telt nog voor de dag waarop hij begon.
  if (req.dag !== dagNu && req.dag !== dagNu - 1) {
    throw new FoutVerzoek('this tower is from another day', 409)
  }
  const max = RONDE_MS / STAP_MS
  if (
    !Array.isArray(req.drukken) ||
    req.drukken.length > 2000 ||
    req.drukken.some(
      (d, i) =>
        !Number.isInteger(d) ||
        d < 0 ||
        d > max ||
        (i > 0 && d < (req.drukken[i - 1] as number)),
    )
  ) {
    throw new FoutVerzoek('bad presses')
  }
  const sub = wie.subreddit
  const user = wie.userId
  const dag = req.dag
  if (!(await db.get(sleutel.start(sub, dag, user))))
    throw new FoutVerzoek('start the tower first', 409)
  // Eerst claimen, dan pas tellen: twee gelijktijdige inzendingen tellen zo maar één keer.
  const uitslagKey = sleutel.uitslag(sub, dag, user)
  if (!(await db.setNX(uitslagKey, BEZIG)))
    throw new FoutVerzoek('you already played today', 409)
  await db.expire(uitslagKey, BEWAAR_DAG_S)

  // De server speelt het potje zelf na; de client kan geen score verzinnen.
  const p = speelNa(dag, req.drukken)

  const rangKey = sleutel.rang(sub, dag)
  await db.zAdd(rangKey, user, rangScore(p.hoeden, p.besteReeks))
  await db.expire(rangKey, BEWAAR_DAG_S)
  await db.set(sleutel.naam(user), wie.naam ?? 'someone')
  const plek = ((await db.zPlekHoog(rangKey, user)) ?? 0) + 1
  const uitslag: UitslagOpslag = {
    hoeden: p.hoeden,
    besteReeks: p.besteReeks,
    uitslagen: p.uitslagen,
    plek,
  }
  await db.set(uitslagKey, JSON.stringify(uitslag))

  const hdKey = sleutel.hoedenDag(sub, dag)
  const spKey = sleutel.spelersDag(sub, dag)
  await db.incrBy(hdKey, p.hoeden)
  await db.incrBy(spKey, 1)
  await db.expire(hdKey, BEWAAR_DAG_S)
  await db.expire(spKey, BEWAAR_DAG_S)
  await db.incrBy(sleutel.hoedenOoit(sub), p.hoeden)

  const oud = await leesReeks(db, user)
  const nieuw: Reeks = {
    laatsteDag: dag,
    dagen: oud.laatsteDag === dag - 1 ? oud.dagen + 1 : 1,
  }
  await db.set(sleutel.reeks(user), JSON.stringify(nieuw))

  const besteOud = Number((await db.get(sleutel.beste(user))) ?? 0)
  // Pas een record als er al een vorige toren was; de eerste keer is geen "nieuw beste".
  const nieuwBeste = besteOud > 0 && p.hoeden > besteOud
  if (nieuwBeste) await db.set(sleutel.beste(user), String(p.hoeden))

  return {
    uitslag,
    dagenOpRij: nieuw.dagen,
    besteOoit: Math.max(besteOud, p.hoeden),
    nieuwBeste,
    gemeenschap: await gemeenschap(db, sub, dag),
    top: await top(db, sub, dag),
  }
}

/** Tekst van de uitslagkaart van deze speler voor vandaag, opgemaakt als Reddit-reactie. */
export async function deelTekst(
  db: Opslag,
  wie: Wie,
  dag: number,
): Promise<string> {
  if (!wie.userId) throw new FoutVerzoek('log in to share', 401)
  const u = await leesUitslag(db, wie.subreddit, dag, wie.userId)
  if (!u || u.afgebroken) throw new FoutVerzoek('play today first', 409)
  const r = reeksNu(await leesReeks(db, wie.userId), dag)
  return kaartTekst(dag, u.hoeden, u.besteReeks, u.uitslagen, r, 'reactie')
}
