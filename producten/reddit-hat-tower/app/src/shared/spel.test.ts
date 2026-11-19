import assert from 'node:assert/strict'
import {test} from 'node:test'
import {speelProef} from './proefspeler.ts'
import {
  begin,
  DAGREGELS,
  dagNummer,
  dagRegel,
  druk,
  goudenHelden,
  nieuwPotje,
  RONDE_MS,
  STAP_MS,
  speelNa,
  stap,
  Toestand,
  waardeVangst,
} from './spel.ts'

test('dag 1 is 19 november 2026 (UTC)', () => {
  assert.equal(dagNummer(Date.UTC(2026, 10, 19, 0, 0, 1)), 1)
  assert.equal(dagNummer(Date.UTC(2026, 11, 8, 23, 0)), 20)
})

test('elke dagregel komt binnen vijf dagen een keer voor, dag 1 is Classic', () => {
  assert.equal(dagRegel(1).id, 'classic')
  assert.ok(dagRegel(0) && dagRegel(-7))
  for (let w = 0; w < 6; w++) {
    const ids = new Set(
      Array.from({length: 5}, (_, i) => dagRegel(w * 5 + i + 1).id),
    )
    assert.equal(ids.size, DAGREGELS.length)
  }
})

test('gouden helden: juist aantal, vast per dag', () => {
  for (let d = 1; d < 40; d++) {
    const g = goudenHelden(d)
    assert.equal(g.length, dagRegel(d).gouden)
    assert.deepEqual(g, goudenHelden(d))
    assert.ok(g.every(n => n >= 4 && n < 24))
  }
})

test('ronde eindigt na precies 30 seconden', () => {
  const p = nieuwPotje(3)
  begin(p)
  let n = 0
  while (p.toestand !== Toestand.Einde) {
    stap(p)
    n++
  }
  assert.equal(n * STAP_MS, RONDE_MS)
  assert.equal(p.hoeden, 0)
})

test('mikken loont: op elke dagregel haalt mikken (spreiding 45) 25% meer dan het beste vaste tikritme', () => {
  // Dag 1 tot 5 zijn de vijf regels een keer (zie de toets hierboven).
  for (let dag = 1; dag <= 5; dag++) {
    let blind = 0
    for (let ms = 200; ms <= 400; ms += 4) {
      for (const fase of [0, 13, 29, 41, 57]) {
        const drukken: number[] = []
        for (let t = fase; t < RONDE_MS / STAP_MS; t += ms / STAP_MS)
          drukken.push(Math.round(t))
        blind = Math.max(blind, speelNa(dag, drukken).hoeden)
      }
    }
    let som = 0
    for (let z = 1; z <= 10; z++)
      som += speelProef(dag, 815, 45, 0.1, z * 31).hoeden
    const mik = som / 10
    assert.ok(
      mik >= blind * 1.25,
      `${dagRegel(dag).naam}: mikken ${mik}, blind ${blind}`,
    )
  }
})

test('waarde van een vangst: gewoon 1, voltreffer 1 + reeks (max 3 erbij), goud 2 extra', () => {
  assert.equal(waardeVangst(false, 0, false), 1)
  assert.equal(waardeVangst(true, 1, false), 2)
  assert.equal(waardeVangst(true, 2, false), 3)
  assert.equal(waardeVangst(true, 7, false), 4)
  assert.equal(waardeVangst(false, 0, true), 3)
})

test('te vroeg happen breekt de reeks, maar kost geen hoed', () => {
  const p = nieuwPotje(1)
  begin(p)
  p.reeks = 3
  const voor = p.hoeden
  druk(p)
  assert.equal(p.reeks, 0)
  assert.equal(p.hoeden, voor)
})

test('missen kost nooit een hoed, te vroeg drukken ook niet', () => {
  const p = nieuwPotje(1)
  begin(p)
  druk(p) // te vroeg
  assert.equal(p.hoeden, 0)
  assert.ok(p.hapDicht > 0)
  const goed = speelProef(1, 815, 0, 0.5, 4)
  assert.ok(goed.uitslagen.includes('miss'))
  const gevangen = goed.uitslagen.filter(u => u !== 'miss').length
  assert.ok(goed.hoeden >= gevangen)
})

test('eerste hoed binnen 2,5 seconde (eis van het horloge)', () => {
  const p = nieuwPotje(1)
  begin(p)
  while (p.hoeden === 0) {
    if (p.toestand === Toestand.Valt && p.y >= 815) druk(p)
    stap(p)
  }
  assert.ok(p.stap * STAP_MS <= 2500, `eerste hoed na ${p.stap * STAP_MS} ms`)
})

test('een goede speler haalt 15 of meer hoeden op Classic (zoals op het horloge)', () => {
  const p = speelProef(1, 815, 0, 0, 1)
  assert.ok(p.hoeden >= 15, `${p.hoeden} hoeden`)
})

test('de server speelt hetzelfde potje na uit alleen de drukken', () => {
  for (let d = 1; d <= 10; d++) {
    const p = speelProef(d, 800, 60, 0.2, d * 13)
    const na = speelNa(d, p.drukken)
    assert.equal(na.hoeden, p.hoeden)
    assert.deepEqual(na.uitslagen, p.uitslagen)
    assert.equal(na.besteReeks, p.besteReeks)
  }
})

test('zelfde dag, zelfde ritme: held n wacht voor iedereen even lang', () => {
  const a = speelProef(7, 815, 0, 0, 1)
  const b = speelProef(7, 815, 0, 0, 999)
  assert.deepEqual(a.drukken, b.drukken)
  const c = speelProef(8, 815, 0, 0, 1)
  assert.notDeepEqual(a.drukken, c.drukken)
})
