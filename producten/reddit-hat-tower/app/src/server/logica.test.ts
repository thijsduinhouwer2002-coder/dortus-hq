import assert from 'node:assert/strict'
import {test} from 'node:test'
import {speelProef} from '../shared/proefspeler.ts'
import {GeheugenOpslag} from './geheugen-opslag.ts'
import {deelTekst, init, type Opslag, score, start, type Wie} from './logica.ts'

const ana: Wie = {subreddit: 'test', naam: 'ana', userId: 't2_ana'}
const bas: Wie = {subreddit: 'test', naam: 'bas', userId: 't2_bas'}

/** Start en stuur in, zoals de client doet. */
async function speel(db: Opslag, wie: Wie, dag: number, drukken: number[]) {
  await start(db, wie, dag, {dag})
  return score(db, wie, dag, {dag, drukken})
}

test('dagbeurt: score komt van de server, één keer per dag, ranglijst en gemeenschap tellen op', async () => {
  const db = new GeheugenOpslag()
  const pa = speelProef(5, 815, 10, 0, 1)
  const ra = await speel(db, ana, 5, pa.drukken)
  assert.equal(ra.uitslag.hoeden, pa.hoeden)
  assert.equal(ra.uitslag.plek, 1)
  await assert.rejects(
    score(db, ana, 5, {dag: 5, drukken: pa.drukken}),
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
  const i = await init(db, ana, 5)
  assert.equal(i.vandaag?.hoeden, pa.hoeden)
})

test('verzonnen drukken leveren niet meer op dan het spel toelaat', async () => {
  const db = new GeheugenOpslag()
  const spam = Array.from({length: 2000}, (_, i) => i * 3)
  const r = await speel(db, ana, 5, spam)
  assert.ok(r.uitslag.hoeden < 40)
  await assert.rejects(
    score(db, bas, 5, {dag: 5, drukken: [5, 3]}),
    /bad presses/,
  )
  await assert.rejects(score(db, bas, 5, {dag: 3, drukken: []}), /another day/)
  await assert.rejects(
    score(db, {...bas, userId: undefined}, 5, {dag: 5, drukken: []}),
    /log in/,
  )
})

test('dagen op rij: telt door, en begint opnieuw na een gemiste dag', async () => {
  const db = new GeheugenOpslag()
  const dagbeurt = (d: number) => speel(db, ana, d, speelProef(d).drukken)
  assert.equal((await dagbeurt(1)).dagenOpRij, 1)
  assert.equal((await dagbeurt(2)).dagenOpRij, 2)
  assert.equal((await dagbeurt(3)).dagenOpRij, 3)
  assert.equal((await init(db, ana, 4)).dagenOpRij, 3)
  assert.equal((await init(db, ana, 5)).dagenOpRij, 0)
  assert.equal((await dagbeurt(5)).dagenOpRij, 1)
  const tekst = await deelTekst(db, ana, 5)
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
  assert.deepEqual(await start(db, ana, 5, {dag: 5}), {telt: true})
  // Herladen midden in de ronde: de dagbeurt staat als gebruikt.
  const i = await init(db, ana, 5)
  assert.equal(i.vandaag?.afgebroken, true)
  assert.equal(i.vandaag?.hoeden, 0)
  assert.deepEqual(await start(db, ana, 5, {dag: 5}), {telt: false})
  // Insturen zonder start kan niet.
  await assert.rejects(
    score(db, bas, 5, {dag: 5, drukken: []}),
    /start the tower first/,
  )
})

test('twee gelijktijdige inzendingen tellen één keer', async () => {
  const db = new GeheugenOpslag()
  const p = speelProef(5, 815, 10, 0, 1)
  await start(db, ana, 5, {dag: 5})
  const uitslagen = await Promise.allSettled([
    score(db, ana, 5, {dag: 5, drukken: p.drukken}),
    score(db, ana, 5, {dag: 5, drukken: p.drukken}),
  ])
  assert.equal(uitslagen.filter(u => u.status === 'fulfilled').length, 1)
  const i = await init(db, ana, 5)
  assert.equal(i.gemeenschap.spelersVandaag, 1)
  assert.equal(i.gemeenschap.hoedenVandaag, p.hoeden)
})

test('een ronde die voor middernacht begon, telt nog voor die dag', async () => {
  const db = new GeheugenOpslag()
  await start(db, ana, 5, {dag: 5})
  const r = await score(db, ana, 6, {dag: 5, drukken: speelProef(5).drukken})
  assert.ok(r.uitslag.hoeden > 0)
  assert.equal((await init(db, ana, 6)).topGisteren[0]?.naam, 'ana')
})
