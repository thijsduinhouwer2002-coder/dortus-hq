// Alles wat de server doet, los van Devvit, zodat het lokaal en in de toets draait.
// Opslag gaat via Opslag: op Reddit is dat Redis (redis-opslag.ts), lokaal een Map (geheugen-opslag.ts).
import type {
  GemeenschapStand,
  InitRsp,
  RijRanglijst,
  ScoreReq,
  ScoreRsp,
  UitslagOpslag,
} from '../shared/api.ts'
import {kaartTekst} from '../shared/kaart.ts'
import {RONDE_MS, STAP_MS, speelNa} from '../shared/spel.ts'

/** Het deel van Redis dat we gebruiken. Zelfde namen en betekenis als @devvit/redis. */
export interface Opslag {
  get(key: string): Promise<string | undefined>
  set(key: string, value: string): Promise<void>
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
    const ruw = await db.get(sleutel.uitslag(sub, dag, wie.userId))
    vandaag = ruw ? (JSON.parse(ruw) as UitslagOpslag) : undefined
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
  }
}

export async function score(
  db: Opslag,
  wie: Wie,
  dagNu: number,
  req: ScoreReq,
): Promise<ScoreRsp> {
  if (!wie.userId) throw new FoutVerzoek('log in to save your tower', 401)
  if (req.dag !== dagNu)
    throw new FoutVerzoek('this tower is from another day', 409)
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
  const al = await db.get(sleutel.uitslag(sub, dagNu, user))
  if (al) throw new FoutVerzoek('you already played today', 409)

  // De server speelt het potje zelf na; de client kan geen score verzinnen.
  const p = speelNa(dagNu, req.drukken)

  const rangKey = sleutel.rang(sub, dagNu)
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
  const uitslagKey = sleutel.uitslag(sub, dagNu, user)
  await db.set(uitslagKey, JSON.stringify(uitslag))
  await db.expire(uitslagKey, BEWAAR_DAG_S)

  const hdKey = sleutel.hoedenDag(sub, dagNu)
  const spKey = sleutel.spelersDag(sub, dagNu)
  await db.incrBy(hdKey, p.hoeden)
  await db.incrBy(spKey, 1)
  await db.expire(hdKey, BEWAAR_DAG_S)
  await db.expire(spKey, BEWAAR_DAG_S)
  await db.incrBy(sleutel.hoedenOoit(sub), p.hoeden)

  const oud = await leesReeks(db, user)
  const nieuw: Reeks = {
    laatsteDag: dagNu,
    dagen: oud.laatsteDag === dagNu - 1 ? oud.dagen + 1 : 1,
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
    gemeenschap: await gemeenschap(db, sub, dagNu),
    top: await top(db, sub, dagNu),
  }
}

/** Tekst van de uitslagkaart van deze speler voor vandaag. */
export async function deelTekst(
  db: Opslag,
  wie: Wie,
  dag: number,
): Promise<string> {
  if (!wie.userId) throw new FoutVerzoek('log in to share', 401)
  const ruw = await db.get(sleutel.uitslag(wie.subreddit, dag, wie.userId))
  if (!ruw) throw new FoutVerzoek('play today first', 409)
  const u = JSON.parse(ruw) as UitslagOpslag
  const r = reeksNu(await leesReeks(db, wie.userId), dag)
  return kaartTekst(dag, u.hoeden, u.besteReeks, u.uitslagen, r)
}
