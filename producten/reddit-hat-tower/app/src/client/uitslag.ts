// Het uitslagvel na een ronde: score, vakjes met uitleg, reactie met voorbeeld, lid worden,
// de toren van de subreddit (vandaag en alle dagen) en de ranglijsten van vandaag en gisteren.
import type {
  InitRsp,
  RijRanglijst,
  ScoreRsp,
  UitslagOpslag,
} from '../shared/api.ts'
import {kaartTekst} from '../shared/kaart.ts'
import {dagRegel} from '../shared/spel.ts'
import {deel, wordLid} from './net.ts'

const $ = <T extends HTMLElement>(id: string): T =>
  document.getElementById(id) as T
const getal = (n: number): string => n.toLocaleString('en-US')

export type EindInfo = {
  modus: 'dag' | 'oefen'
  dag: number
  u: UitslagOpslag
  rsp: ScoreRsp | undefined
  fout: string
  info: InitRsp | undefined
}

function esc(s: string): string {
  return s.replace(/[&<>"']/g, c => `&#${c.charCodeAt(0)};`)
}

export function toonEinde(e: EindInfo): void {
  const {modus, dag, u, rsp, fout, info} = e
  $('eind-getal').textContent = String(u.hoeden)
  $('eind-woord').textContent = u.hoeden === 1 ? 'hat' : 'hats'
  $('eind-kop').textContent =
    modus === 'oefen'
      ? 'Practice tower'
      : rsp?.nieuwBeste
        ? 'New best tower!'
        : `Tower #${dag}, ${dagRegel(dag).naam}`
  const regels: string[] = []
  if (rsp) {
    regels.push(
      `Place ${rsp.uitslag.plek} of ${getal(rsp.gemeenschap.spelersVandaag)} today`,
    )
    if (rsp.dagenOpRij > 1) regels.push(`${rsp.dagenOpRij} days in a row`)
  }
  regels.push(`Best perfect streak ${u.besteReeks}`)
  if (fout) regels.push(fout)
  $('eind-regels').textContent = regels.join('\n')

  $('eind-vakjes').replaceChildren(
    ...u.uitslagen.map(s => {
      const el = document.createElement('i')
      el.className = `vak vak-${s}`
      el.title = s
      return el
    }),
  )

  // Reactie: eerst laten zien wat er geplaatst wordt, dan pas plaatsen (Reddit: "inform users").
  const delen = $('eind-delen')
  delen.hidden = modus !== 'dag' || !rsp
  const tekst = kaartTekst(
    dag,
    u.hoeden,
    u.besteReeks,
    u.uitslagen,
    rsp?.dagenOpRij ?? 1,
  )
  $('kaart-voorbeeld').textContent = tekst
  $('kaart-wie').textContent = info?.naam
    ? 'Posts as a comment from your account, under this post:'
    : 'Your result:'
  const plaats = $<HTMLButtonElement>('knop-reactie')
  plaats.disabled = false
  plaats.textContent = 'Post as comment'
  plaats.onclick = async () => {
    plaats.disabled = true
    plaats.textContent = 'Posting...'
    const a = await deel({dag})
    plaats.textContent = a.ok ? 'Posted' : 'Could not post. Copy it instead.'
    if (!a.ok) plaats.disabled = false
  }
  const kopie = $<HTMLButtonElement>('knop-kopie')
  kopie.textContent = 'Copy'
  kopie.onclick = async () => {
    try {
      await navigator.clipboard.writeText(tekst)
      kopie.textContent = 'Copied'
    } catch {
      kopie.textContent = 'Copy failed'
    }
  }

  const sub = info?.subreddit ?? 'here'
  const lid = $<HTMLButtonElement>('knop-lid')
  lid.hidden = !info?.naam
  lid.disabled = false
  lid.textContent = `Join r/${sub} for tomorrow's tower`
  lid.onclick = async () => {
    lid.disabled = true
    const a = await wordLid()
    lid.textContent = a.ok ? `Joined r/${sub}` : 'Could not join right now'
  }

  const g = rsp?.gemeenschap ?? info?.gemeenschap
  const samen: string[] = []
  if (g && g.hoedenVandaag > 0) {
    samen.push(
      `Today r/${sub} stacked ${getal(g.hoedenVandaag)} hats in one tower${modus === 'dag' && rsp ? `. Your ${u.hoeden} are in it.` : '.'}`,
    )
  }
  if (g && g.hoedenOoit > g.hoedenVandaag)
    samen.push(`Since tower #1: ${getal(g.hoedenOoit)} hats.`)
  $('eind-samen').textContent = samen.join(' ')
  lijst('eind-top', 'eind-top-kop', rsp?.top ?? info?.top ?? [], info?.naam, 10)
  lijst(
    'eind-gisteren',
    'eind-gisteren-kop',
    info?.topGisteren ?? [],
    info?.naam,
    3,
  )
  $<HTMLButtonElement>('knop-weer').textContent =
    modus === 'dag' ? 'Practice' : 'Practice again'
  const laag = $('einde')
  laag.hidden = false
  laag.scrollTop = 0
}

function lijst(
  id: string,
  kopId: string,
  rijen: RijRanglijst[],
  naam: string | undefined,
  max: number,
): void {
  const el = $(id)
  $(kopId).hidden = rijen.length === 0
  el.replaceChildren(
    ...rijen.slice(0, max).map(r => {
      const li = document.createElement('li')
      if (naam && r.naam === naam) li.className = 'mij'
      li.innerHTML = `<span class="naam">u/${esc(r.naam)}</span><span class="tal">${r.hoeden}</span>`
      return li
    }),
  )
}
