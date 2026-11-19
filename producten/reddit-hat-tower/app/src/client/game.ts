// Het spel in de post (Devvit-entrypoint "game"): startscherm, spelen, uitslag.
// De regels staan in shared/spel.ts; de server speelt de dagbeurt na en bewaart hem.
import type {
  InitRsp,
  RijRanglijst,
  ScoreRsp,
  UitslagOpslag,
} from '../shared/api.ts'
import {kaartTekst} from '../shared/kaart.ts'
import {
  begin,
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
import {deel, haalInit, stuurScore} from './net.ts'
import {type Beeld, laadPlaatjes, nieuwBeeld, Tekenaar} from './teken.ts'

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
let tekenaar: Tekenaar
let stilTot = 0
let laatsteTeller = 0
let simTijd = 0
let eindeSinds = 0

function getal(n: number): string {
  return n.toLocaleString('en-US')
}

function maakTekst(el: HTMLElement, html: string): void {
  el.innerHTML = html
}

function esc(s: string): string {
  return s.replace(/[&<>"']/g, c => `&#${c.charCodeAt(0)};`)
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
  const al = info?.vandaag
  const knop = $<HTMLButtonElement>('knop-speel')
  const oefen = $<HTMLButtonElement>('knop-oefen')
  const mijn = $('mijn-dag')
  if (al) {
    knop.hidden = true
    mijn.hidden = false
    maakTekst(
      mijn,
      `You stacked <b>${al.hoeden}</b> hats today, place ${al.plek}. Come back tomorrow for tower #${dag + 1}.`,
    )
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
  p.hoeden = Math.min(al?.hoeden ?? 4, 6)
  volgorde = hoedVolgorde(dag)
  beeld = nieuwBeeld()
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
  beeld = nieuwBeeld()
  begin(p)
  laatsteTeller = p.laatste.teller
  simTijd = performance.now()
  startLaag.hidden = true
  eindLaag.hidden = true
  tikHint.hidden = false
  tikHint.textContent =
    modus === 'dag'
      ? `Tower #${vandaagDag()}: tap when he reaches the mouth`
      : 'Practice: tap when he reaches the mouth'
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
    if (p.toestand === Toestand.Einde) break
  }
  verwerkGebeurtenis()
}

function verwerkGebeurtenis(): void {
  if (p.laatste.teller === laatsteTeller) return
  laatsteTeller = p.laatste.teller
  const soort = p.laatste.soort
  if (soort === 'raak' || soort === 'hap') {
    const goud = p.uitslagen[p.uitslagen.length - 1] === 'gold'
    beeld.kreet = 'GULP!'
    beeld.kreetSub = goud ? '+3 hats' : p.reeks > 1 ? `x${p.reeks}` : ''
    beeld.kreetMs = 0
    // Korte stilstand precies op het slikken (zoals op het horloge): 80 ms, alleen in beeld.
    stilTot = performance.now() + 80
    if (goud) geluid.goud()
    else geluid.gulp(soort === 'raak', p.reeks)
    if (soort === 'raak' || goud) tekenaar.strooiVonken(beeld, goud)
    navigator.vibrate?.(soort === 'raak' ? 22 : 10)
    tikHint.hidden = true
  } else if (soort === 'lucht') {
    geluid.lucht()
  } else if (soort === 'mis') {
    geluid.mis()
  } else if (soort === 'einde') {
    geluid.einde()
    eindeSinds = performance.now()
    void naEinde()
  }
}

function drukNu(t: number): void {
  if (p.toestand === Toestand.Klaar || p.toestand === Toestand.Einde) return
  rekenTot(t)
  druk(p)
  verwerkGebeurtenis()
}

let vorigBeeld = performance.now()
function lus(t: number): void {
  rekenTot(t)
  const dt = Math.min(50, t - vorigBeeld)
  vorigBeeld = t
  if (p.toestand === Toestand.Einde) {
    // Camera trekt terug tot de hele toren in beeld is, boven het uitslagvel.
    const f = Math.min(1, (t - eindeSinds) / 900)
    const e = 1 - (1 - f) ** 3
    const top = tekenaar.torenTop(p.hoeden, volgorde)
    const ruimte = tekenaar.h * 0.42 - 30
    const nodig = tekenaar.voet - top + 20
    const doelZoom = Math.min(1, ruimte / nodig)
    beeld.zoom = 1 + (doelZoom - 1) * e
    beeld.voetPlek = 1 + (0.44 - 1) * e
  }
  tekenaar.teken(p, beeld, volgorde, dt)
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
  // Wacht tot de camera klaar is, dan schuift het vel omhoog.
  const wacht = Math.max(0, 950 - (performance.now() - eindeSinds))
  setTimeout(() => toonEinde(rsp?.uitslag ?? eigen, rsp, fout), wacht)
}

function toonEinde(
  u: UitslagOpslag,
  rsp: ScoreRsp | undefined,
  fout: string,
): void {
  const dag = modus === 'dag' ? p.dag : 0
  $('eind-getal').textContent = String(u.hoeden)
  $('eind-woord').textContent = u.hoeden === 1 ? 'hat' : 'hats'
  const kop =
    modus === 'oefen'
      ? 'Practice tower'
      : rsp?.nieuwBeste
        ? 'New best tower!'
        : `Tower #${dag}, ${dagRegel(dag).naam}`
  $('eind-kop').textContent = kop
  const regels: string[] = []
  if (rsp) {
    regels.push(
      `Place ${rsp.uitslag.plek} of ${getal(rsp.gemeenschap.spelersVandaag)} today`,
    )
    if (rsp.dagenOpRij > 1) regels.push(`${rsp.dagenOpRij} days in a row`)
  }
  regels.push(`Best streak ${u.besteReeks}`)
  if (fout) regels.push(fout)
  $('eind-regels').textContent = regels.join('\n')

  // De vakjes van de uitslagkaart.
  const vak = $('eind-vakjes')
  vak.replaceChildren(
    ...u.uitslagen.map(s => {
      const el = document.createElement('i')
      el.className = `vak vak-${s}`
      el.title = s
      return el
    }),
  )

  const delen = $('eind-delen')
  delen.hidden = modus !== 'dag'
  const kaart = kaartTekst(
    dag,
    u.hoeden,
    u.besteReeks,
    u.uitslagen,
    rsp?.dagenOpRij ?? 1,
  )
  $<HTMLButtonElement>('knop-reactie').onclick = async () => {
    const knop = $<HTMLButtonElement>('knop-reactie')
    knop.disabled = true
    const a = await deel({dag})
    knop.textContent = a.ok
      ? 'Posted as a comment'
      : 'Could not post. Copy it instead.'
    if (!a.ok) knop.disabled = false
  }
  $<HTMLButtonElement>('knop-kopie').onclick = async () => {
    try {
      await navigator.clipboard.writeText(kaart)
      $('knop-kopie').textContent = 'Copied'
    } catch {
      $('knop-kopie').textContent = 'Copy failed'
    }
  }
  $('knop-reactie').textContent = 'Comment my result'
  $('knop-kopie').textContent = 'Copy'

  const g = rsp?.gemeenschap ?? info?.gemeenschap
  $('eind-samen').textContent =
    g && g.hoedenVandaag > 0
      ? `Today r/${info?.subreddit} stacked ${getal(g.hoedenVandaag)} hats in one tower. ${modus === 'dag' && rsp ? `Your ${u.hoeden} are in it.` : ''}`
      : ''
  toonTop(rsp?.top ?? info?.top ?? [])
  $<HTMLButtonElement>('knop-weer').textContent =
    modus === 'dag' ? 'Practice' : 'Practice again'
  eindLaag.hidden = false
  eindLaag.scrollTop = 0
}

function toonTop(top: RijRanglijst[]): void {
  const lijst = $('eind-top')
  if (top.length === 0) {
    lijst.replaceChildren()
    $('eind-top-kop').hidden = true
    return
  }
  $('eind-top-kop').hidden = false
  lijst.replaceChildren(
    ...top.map(r => {
      const li = document.createElement('li')
      const mij = info?.naam && r.naam === info.naam
      if (mij) li.className = 'mij'
      li.innerHTML = `<span class="naam">u/${esc(r.naam)}</span><span class="tal">${r.hoeden}</span>`
      return li
    }),
  )
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

// ---------- opstarten ----------

async function opstart(): Promise<void> {
  await document.fonts.load('40px "Lilita One"').catch(() => undefined)
  const pl = await laadPlaatjes()
  tekenaar = new Tekenaar(canvas, pl)
  tekenaar.pasAan()
  new ResizeObserver(() => tekenaar.pasAan()).observe(canvas)
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
