import assert from 'node:assert/strict'
import {test} from 'node:test'
import {speelProef} from '../shared/proefspeler.ts'
import {GeheugenOpslag} from './geheugen-opslag.ts'
import {
  deelTekst,
  init,
  type Opslag,
  postDag,
  score,
  start,
  type Wie,
  zetPostDag,
} from './logica.ts'

const ana: Wie = {subreddit: 'test', naam: 'ana', userId: 't2_ana'}
const bas: Wie = {subreddit: 'test', naam: 'bas', userId: 't2_bas'}

const D = (post: number, nu = post) => ({post, nu})
const T0 = 1_000_000

/** Start en stuur 31 s later in, zoals de client doet. */
async function speel(
  db: Opslag,
  wie: Wie,
  dag: number,
  drukken: number[],
  nu = dag,
) {
  await start(db, wie, D(dag, nu), {dag}, T0)
  return score(db, wie, D(dag, nu), {dag, drukken}, T0 + 31_000)
}

test('dagbeurt: score komt van de server, één keer per dag, ranglijst en gemeenschap tellen op', async () => {
  const db = new GeheugenOpslag()
  const pa = speelProef(5, 815, 10, 0, 1)
  const ra = await speel(db, ana, 5, pa.drukken)
  assert.equal(ra.uitslag.hoeden, pa.hoeden)
  assert.equal(ra.uitslag.plek, 1)
  await assert.rejects(
    score(db, ana, D(5), {dag: 5, drukken: pa.drukken}, T0 + 31_000),
    /already/,
  )

  const pb = speelProef(5, 760, 60, 0.4, 2)
  const rb = await speel(db, bas, 5, pb.drukken)
  assert.ok(pb.hoeden < pa.hoeden)
  assert.equal(rb.uitslag.plek, 2)
  assert.equal(rb.gemeenschap.hoedenVandaag, pa.hoeden + pb.hoeden)
  assert.equal(rb.gemeenschap.spelersVandaag, 2)
  assert.deepEqual(
    rb.top.map(r => r.naam),
    ['ana', 'bas'],
  )
  const i = await init(db, ana, D(5))
  assert.equal(i.vandaag?.hoeden, pa.hoeden)
})

test('verzonnen drukken leveren niet meer op dan het spel toelaat', async () => {
  const db = new GeheugenOpslag()
  const spam = Array.from({length: 2000}, (_, i) => i * 3)
  const r = await speel(db, ana, 5, spam)
  assert.ok(r.uitslag.hoeden < 40)
  await assert.rejects(
    score(db, bas, D(5), {dag: 5, drukken: [5, 3]}, T0 + 31_000),
    /bad presses/,
  )
  await assert.rejects(
    score(db, bas, D(5), {dag: 3, drukken: []}, T0 + 31_000),
    /not the tower/,
  )
  await assert.rejects(
    score(
      db,
      {...bas, userId: undefined},
      D(5),
      {dag: 5, drukken: []},
      T0 + 31_000,
    ),
    /log in/,
  )
})

test('dagen op rij: telt door, en begint opnieuw na een gemiste dag', async () => {
  const db = new GeheugenOpslag()
  const dagbeurt = (d: number) => speel(db, ana, d, speelProef(d).drukken)
  assert.equal((await dagbeurt(1)).dagenOpRij, 1)
  assert.equal((await dagbeurt(2)).dagenOpRij, 2)
  assert.equal((await dagbeurt(3)).dagenOpRij, 3)
  assert.equal((await init(db, ana, D(4))).dagenOpRij, 3)
  assert.equal((await init(db, ana, D(5))).dagenOpRij, 0)
  assert.equal((await dagbeurt(5)).dagenOpRij, 1)
  const tekst = await deelTekst(db, ana, D(5))
  assert.match(tekst, /^Gloop's Hat Tower #5/)
  assert.match(
    tekst,
    /\n\n🎩/,
    'witregels, anders loopt de reactie op Reddit aan elkaar',
  )
  assert.doesNotMatch(tekst, /garmin|steam|http/i)
})

test('dagbeurt telt vanaf de start: herladen geeft geen nieuwe beurt', async () => {
  const db = new GeheugenOpslag()
  assert.deepEqual(await start(db, ana, D(5), {dag: 5}, T0), {telt: true})
  // Herladen midden in de ronde: de dagbeurt staat als gebruikt.
  const i = await init(db, ana, D(5))
  assert.equal(i.vandaag?.afgebroken, true)
  assert.equal(i.vandaag?.hoeden, 0)
  assert.deepEqual(await start(db, ana, D(5), {dag: 5}, T0), {telt: false})
  // Insturen zonder start kan niet.
  await assert.rejects(
    score(db, bas, D(5), {dag: 5, drukken: []}, T0 + 31_000),
    /start the tower first/,
  )
})

test('twee gelijktijdige inzendingen tellen één keer', async () => {
  const db = new GeheugenOpslag()
  const p = speelProef(5, 815, 10, 0, 1)
  await start(db, ana, D(5), {dag: 5}, T0)
  const uitslagen = await Promise.allSettled([
    score(db, ana, D(5), {dag: 5, drukken: p.drukken}, T0 + 31_000),
    score(db, ana, D(5), {dag: 5, drukken: p.drukken}, T0 + 31_000),
  ])
  assert.equal(uitslagen.filter(u => u.status === 'fulfilled').length, 1)
  const i = await init(db, ana, D(5))
  assert.equal(i.gemeenschap.spelersVandaag, 1)
  assert.equal(i.gemeenschap.hoedenVandaag, p.hoeden)
})

test('een ronde die voor middernacht begon, telt nog voor die dag', async () => {
  const db = new GeheugenOpslag()
  await start(db, ana, D(5), {dag: 5}, T0)
  const r = await score(
    db,
    ana,
    D(5, 6),
    {dag: 5, drukken: speelProef(5).drukken},
    T0 + 31_000,
  )
  assert.ok(r.uitslag.hoeden > 0)
  assert.equal((await init(db, ana, D(6))).topGisteren[0]?.naam, 'ana')
})

test('insturen alleen binnen een redelijke tijd na de start', async () => {
  const db = new GeheugenOpslag()
  const p = speelProef(5)
  await start(db, ana, D(5), {dag: 5}, T0)
  await assert.rejects(
    score(db, ana, D(5), {dag: 5, drukken: p.drukken}, T0 + 5_000),
    /too early/,
  )
  await assert.rejects(
    score(db, ana, D(5), {dag: 5, drukken: p.drukken}, T0 + 30_000 + 61_000),
    /too late/,
  )
  // Te laat telt als afgebroken: 0 hoeden, geen nieuwe beurt.
  assert.equal((await init(db, ana, D(5))).vandaag?.afgebroken, true)
  await start(db, bas, D(5), {dag: 5}, T0)
  const r = await score(
    db,
    bas,
    D(5),
    {dag: 5, drukken: p.drukken},
    T0 + 30_000 + 59_000,
  )
  assert.equal(r.uitslag.hoeden, p.hoeden)
})

test('een oude post speelt zijn eigen toren; dagen op rij tellen alleen vandaag', async () => {
  const db = new GeheugenOpslag()
  await zetPostDag(db, 't3_oud', 3)
  assert.equal(await postDag(db, 't3_oud', 9), 3)
  assert.equal(await postDag(db, 't3_onbekend', 9), 9)
  assert.equal(await postDag(db, undefined, 9), 9)
  const i = await init(db, ana, D(3, 9))
  assert.equal(i.dag, 3)
  assert.equal(i.dagVandaag, 9)
  const r = await speel(db, ana, 3, speelProef(3).drukken, 9)
  assert.ok(r.uitslag.hoeden > 0)
  assert.equal(r.dagenOpRij, 0)
  assert.equal((await speel(db, ana, 9, speelProef(9).drukken)).dagenOpRij, 1)
  // Een post uit de toekomst bestaat niet: dan geldt vandaag.
  await zetPostDag(db, 't3_raar', 40)
  assert.equal(await postDag(db, 't3_raar', 9), 9)
})

test('beste toren wordt ook de eerste keer bewaard', async () => {
  const db = new GeheugenOpslag()
  const r1 = await speel(db, ana, 1, speelProef(1, 815, 0, 0, 1).drukken)
  assert.equal(r1.nieuwBeste, false)
  assert.equal((await init(db, ana, D(2))).besteOoit, r1.besteOoit)
  assert.ok(r1.besteOoit > 0)
})

test('pauzeren tijdens de beurt telt niet als te laat (tot 10 minuten)', async () => {
  const db = new GeheugenOpslag()
  const p = speelProef(5)
  await start(db, ana, D(5), {dag: 5}, T0)
  const r = await score(
    db,
    ana,
    D(5),
    {dag: 5, drukken: p.drukken, pauzeMs: 300_000},
    T0 + 31_000 + 300_000,
  )
  assert.equal(r.uitslag.hoeden, p.hoeden)
  await start(db, bas, D(5), {dag: 5}, T0)
  await assert.rejects(
    score(
      db,
      bas,
      D(5),
      {dag: 5, drukken: p.drukken, pauzeMs: 3_600_000},
      T0 + 31_000 + 3_600_000,
    ),
    /too late/,
  )
})
