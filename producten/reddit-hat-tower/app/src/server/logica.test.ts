import assert from 'node:assert/strict'
import {test} from 'node:test'
import {speelProef} from '../shared/proefspeler.ts'
import {GeheugenOpslag} from './geheugen-opslag.ts'
import {deelTekst, init, score, type Wie} from './logica.ts'

const ana: Wie = {subreddit: 'test', naam: 'ana', userId: 't2_ana'}
const bas: Wie = {subreddit: 'test', naam: 'bas', userId: 't2_bas'}

test('dagbeurt: score komt van de server, één keer per dag, ranglijst en gemeenschap tellen op', async () => {
  const db = new GeheugenOpslag()
  const pa = speelProef(5, 815, 10, 0, 1)
  const ra = await score(db, ana, 5, {dag: 5, drukken: pa.drukken})
  assert.equal(ra.uitslag.hoeden, pa.hoeden)
  assert.equal(ra.uitslag.plek, 1)
  await assert.rejects(
    score(db, ana, 5, {dag: 5, drukken: pa.drukken}),
    /already/,
  )

  const pb = speelProef(5, 760, 60, 0.4, 2)
  const rb = await score(db, bas, 5, {dag: 5, drukken: pb.drukken})
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
  const r = await score(db, ana, 5, {dag: 5, drukken: spam})
  assert.ok(r.uitslag.hoeden < 40)
  await assert.rejects(
    score(db, bas, 5, {dag: 5, drukken: [5, 3]}),
    /bad presses/,
  )
  await assert.rejects(score(db, bas, 5, {dag: 4, drukken: []}), /another day/)
  await assert.rejects(
    score(db, {...bas, userId: undefined}, 5, {dag: 5, drukken: []}),
    /log in/,
  )
})

test('dagen op rij: telt door, en begint opnieuw na een gemiste dag', async () => {
  const db = new GeheugenOpslag()
  const speel = (d: number) =>
    score(db, ana, d, {dag: d, drukken: speelProef(d).drukken})
  assert.equal((await speel(1)).dagenOpRij, 1)
  assert.equal((await speel(2)).dagenOpRij, 2)
  assert.equal((await speel(3)).dagenOpRij, 3)
  assert.equal((await init(db, ana, 4)).dagenOpRij, 3)
  assert.equal((await init(db, ana, 5)).dagenOpRij, 0)
  assert.equal((await speel(5)).dagenOpRij, 1)
  const tekst = await deelTekst(db, ana, 5)
  assert.match(tekst, /^Gloop's Hat Tower #5/)
  assert.doesNotMatch(tekst, /garmin|steam|http/i)
})
