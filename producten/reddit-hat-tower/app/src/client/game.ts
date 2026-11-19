// Het spel in de post (Devvit-entrypoint "game"): startscherm, spelen, uitslag.
// De regels staan in shared/spel.ts; de server speelt de dagbeurt na en bewaart hem.
import type {InitRsp, ScoreRsp, UitslagOpslag} from '../shared/api.ts'
import {
  begin,
  dagDatum,
  dagNummer,
  dagRegel,
  druk,
  goudenHelden,
  hoedVolgorde,
  nieuwPotje,
  type Potje,
  STAP_MS,
  stap,
  Toestand,
} from '../shared/spel.ts'
import * as geluid from './geluid.ts'
import {laadKunst} from './kunst.ts'
import {haalInit, stuurScore, stuurStart} from './net.ts'
import {type Beeld, nieuwBeeld, Scene} from './scene.ts'
import {maakSlot} from './slot.ts'
import {toonEinde} from './uitslag.ts'

const $ = <T extends HTMLElement>(id: string): T =>
  document.getElementById(id) as T

const stage = $('stage')
const canvas = $<HTMLCanvasElement>('canvas')
const startLaag = $('start')
const eindLaag = $('einde')
const tikHint = $('tik-hint')

type Modus = 'dag' | 'oefen'

let info: InitRsp | undefined
let netFout = ''
const vandaagDag = (): number => {
  const q = new URLSearchParams(location.search).get('dag')
  return q ? Number(q) : (info?.dag ?? dagNummer(Date.now()))
}

let modus: Modus = 'dag'
let p: Potje = nieuwPotje(vandaagDag())
let volgorde = hoedVolgorde(p.dag)
let beeld: Beeld = nieuwBeeld()
let scene: Scene
let stilTot = 0
let laatsteTeller = 0
let simTijd = 0
let eindeSinds = 0

const getal = (n: number): string => n.toLocaleString('en-US')

function vulBeeld(b: Beeld): Beeld {
  b.samen = info?.gemeenschap.hoedenVandaag ?? 0
  b.samenTeller = b.samen
  b.sub = info?.subreddit ?? ''
  return b
}

// ---------- startscherm ----------

function toonStart(): void {
  const dag = vandaagDag()
  const regel = dagRegel(dag)
  const goud = goudenHelden(dag)
  $('dag-titel').textContent = `Tower #${dag}`
  $('dag-regel').textContent = regel.naam
  $('dag-uitleg').textContent = regel.uitleg
  $('dag-goud').textContent = `Golden heroes today: ${goud
    .map(g => `#${g}`)
    .join(', ')
    .replace(/, ([^,]*)$/, ' and $1')}`
  // Een oude post speelt de toren van zijn eigen dag; zeg dat er een nieuwere is.
  const oud = $('dag-oud')
  oud.hidden = !info || info.dag >= info.dagVandaag
  if (info && !oud.hidden) {
    oud.textContent = `This is tower #${info.dag} from ${dagDatum(info.dag)}. Today's tower #${info.dagVandaag} is in the newest post.`
  }
  const al = info?.vandaag
  const knop = $<HTMLButtonElement>('knop-speel')
  const oefen = $<HTMLButtonElement>('knop-oefen')
  const mijn = $('mijn-dag')
  if (al) {
    knop.hidden = true
    mijn.hidden = false
    mijn.innerHTML = al.afgebroken
      ? `Your run for tower #${dag} was started and not finished, so it counts as 0.`
      : `You stacked <b>${al.hoeden}</b> hats on tower #${dag}, place ${al.plek}. A new tower comes every day.`
    oefen.textContent = 'Practice'
    oefen.classList.add('hoofd')
  } else {
    knop.hidden = false
    knop.textContent = `Play tower #${dag}`
    mijn.hidden = true
    oefen.textContent = 'Warm up first'
    oefen.classList.remove('hoofd')
  }
  const g = info?.gemeenschap
  $('samen').textContent = netFout
    ? 'Leaderboard is offline right now. You can still play.'
    : g && g.hoedenVandaag > 0
      ? `r/${info?.subreddit} stacked ${getal(g.hoedenVandaag)} hats today, together.`
      : `Be the first in r/${info?.subreddit ?? 'here'} to stack a hat today.`
  $('reeks').textContent =
    info && info.dagenOpRij > 1 ? `${info.dagenOpRij} days in a row` : ''
  // Achter het startscherm staat Gloop met een kleine toren: je ziet meteen waar het om gaat.
  p = nieuwPotje(dag)
  volgorde = hoedVolgorde(dag)
  beeld = vulBeeld(nieuwBeeld())
  beeld.toren = 5
  beeld.bordje = false
  tikHint.hidden = true
  startLaag.hidden = false
  eindLaag.hidden = true
}

function start(nieuweModus: Modus): void {
  geluid.wekGeluid()
  modus = nieuweModus
  const dag =
    modus === 'dag' ? vandaagDag() : 100000 + Math.floor(Math.random() * 100000)
  p = nieuwPotje(dag)
  volgorde = hoedVolgorde(modus === 'dag' ? dag : vandaagDag())
  beeld = vulBeeld(nieuwBeeld())
  begin(p)
  if (modus === 'dag' && !netFout) {
    // De dagbeurt telt vanaf nu. Was hij al gestart (herladen, tweede tabblad), dan wordt dit oefenen.
    void stuurStart({dag}).then(a => {
      if (a.ok && !a.data.telt) modus = 'oefen'
    })
  }
  laatsteTeller = p.laatste.teller
  simTijd = performance.now()
  startLaag.hidden = true
  eindLaag.hidden = true
  tikHint.hidden = false
  tikHint.textContent =
    'Tap when he reaches the mouth. Perfect gulps stack more hats.'
}

// ---------- spelen ----------

/** Rekent het spel bij tot tijd t (ms, performance.now), in vaste stappen. */
function rekenTot(t: number): void {
  if (t < stilTot) {
    simTijd = t
    return
  }
  if (t - simTijd > 250) simTijd = t - 250 // tab was weg: niet in één klap doorspelen
  while (simTijd + STAP_MS <= t) {
    stap(p)
    simTijd += STAP_MS
    verwerkGebeurtenis(t)
    if (p.toestand === Toestand.Einde) break
  }
  verwerkGebeurtenis(t)
}

function verwerkGebeurtenis(nu: number): void {
  if (p.laatste.teller === laatsteTeller) return
  laatsteTeller = p.laatste.teller
  const soort = p.laatste.soort ?? ''
  scene.gebeurtenis(soort, p, beeld, volgorde, nu)
  if (soort === 'raak' || soort === 'hap') {
    const goud = p.uitslagen[p.uitslagen.length - 1] === 'gold'
    // Korte stilstand precies op het slikken (zoals op het horloge): 80 ms, alleen in beeld.
    stilTot = nu + 80
    if (goud) geluid.goud()
    else geluid.gulp(soort === 'raak', p.reeks)
    navigator.vibrate?.(soort === 'raak' ? 22 : 10)
    tikHint.hidden = true
  } else if (soort === 'lucht') {
    geluid.lucht()
  } else if (soort === 'mis') {
    geluid.mis()
  } else if (soort === 'einde') {
    geluid.einde()
    eindeSinds = nu
    // Alleen een dagbeurt telt mee voor de gezamenlijke toren; dan vliegen je hoeden erheen.
    beeld.slot = maakSlot(
      scene,
      p,
      beeld,
      volgorde,
      nu,
      modus === 'dag' && !netFout,
    )
    void naEinde()
  }
}

function drukNu(t: number): void {
  if (p.toestand === Toestand.Klaar || p.toestand === Toestand.Einde) return
  rekenTot(t)
  druk(p)
  verwerkGebeurtenis(t)
}

let vorigBeeld = performance.now()
function lus(t: number): void {
  rekenTot(t)
  const dt = Math.min(50, t - vorigBeeld)
  vorigBeeld = t
  scene.teken(p, beeld, volgorde, dt, t)
  requestAnimationFrame(lus)
}

// ---------- uitslag ----------

async function naEinde(): Promise<void> {
  const eigen: UitslagOpslag = {
    hoeden: p.hoeden,
    besteReeks: p.besteReeks,
    uitslagen: p.uitslagen,
    plek: 0,
  }
  let rsp: ScoreRsp | undefined
  let fout = ''
  if (modus === 'dag' && !netFout) {
    const a = await stuurScore({dag: p.dag, drukken: p.drukken})
    if (a.ok) {
      rsp = a.data
      if (info) {
        info.vandaag = rsp.uitslag
        info.dagenOpRij = rsp.dagenOpRij
        info.besteOoit = rsp.besteOoit
        info.gemeenschap = rsp.gemeenschap
        info.top = rsp.top
      }
    } else {
      fout =
        a.status === 401
          ? 'Log in to Reddit to save your tower.'
          : `Not saved: ${a.fout}.`
    }
  }
  const wacht = Math.max(
    0,
    (beeld.slot?.klaarOp ?? eindeSinds + 950) - performance.now(),
  )
  setTimeout(() => {
    beeld.bordje = false
    toonEinde({modus, dag: p.dag, u: rsp?.uitslag ?? eigen, rsp, fout, info})
  }, wacht)
}

// ---------- invoer ----------

stage.addEventListener('pointerdown', ev => {
  if ((ev.target as HTMLElement).closest('button, a, .laag')) return
  ev.preventDefault()
  geluid.wekGeluid()
  drukNu(ev.timeStamp || performance.now())
})

window.addEventListener('keydown', ev => {
  if (ev.repeat) return
  if (ev.code === 'Space' || ev.code === 'Enter' || ev.code === 'ArrowUp') {
    if (p.toestand === Toestand.Klaar || p.toestand === Toestand.Einde) return
    ev.preventDefault()
    drukNu(performance.now())
  }
})

$('knop-speel').addEventListener('click', () => start('dag'))
$('knop-oefen').addEventListener('click', () => start('oefen'))
$('knop-weer').addEventListener('click', () => start('oefen'))
$('knop-terug').addEventListener('click', () => toonStart())

const geluidKnop = $<HTMLButtonElement>('knop-geluid')
function zetGeluidKnop(): void {
  geluidKnop.setAttribute('aria-pressed', String(geluid.geluidAan()))
  geluidKnop.textContent = geluid.geluidAan() ? 'Sound on' : 'Sound off'
}
geluidKnop.addEventListener('click', () => {
  geluid.zetGeluid(!geluid.geluidAan())
  geluid.wekGeluid()
  zetGeluidKnop()
})
zetGeluidKnop()
// In het filmpje geen knop in beeld.
if (new URLSearchParams(location.search).has('film')) geluidKnop.hidden = true

// ---------- opstarten ----------

async function opstart(): Promise<void> {
  await document.fonts.load('40px "Lilita One"').catch(() => undefined)
  scene = new Scene(canvas, await laadKunst())
  scene.pasAan()
  new ResizeObserver(() => scene.pasAan()).observe(canvas)
  const a = await haalInit()
  if (a.ok) info = a.data
  else netFout = a.fout
  toonStart()
  document.body.classList.add('klaar')
  requestAnimationFrame(lus)
}

// Alleen voor de schermbeelden en de keurder (?proef=1): laat de stand zien, verandert niets.
if (new URLSearchParams(location.search).has('proef')) {
  Object.assign(window, {
    gloopProef: () => ({
      toestand: p.toestand,
      y: p.y,
      hoeden: p.hoeden,
      held: p.held,
    }),
  })
}

void opstart()
