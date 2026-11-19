// De post in de feed (Devvit-entrypoint "default"): Gloop met zijn toren, de dag, en een knop.
// Een tik opent het spel groot (requestExpandedMode). Lokaal gaat de knop gewoon naar game.html.
import {requestExpandedMode} from '@devvit/web/client'
import {dagNummer, dagRegel, hoedVolgorde, nieuwPotje} from '../shared/spel.ts'
import {haalInit} from './net.ts'
import {laadPlaatjes, nieuwBeeld, Tekenaar} from './teken.ts'

const $ = (id: string): HTMLElement =>
  document.getElementById(id) as HTMLElement

function open(ev: MouseEvent): void {
  try {
    requestExpandedMode(ev, 'game')
  } catch {
    location.href = `game.html${location.search}`
  }
}

async function opstart(): Promise<void> {
  $('knop-speel').addEventListener('click', open)
  const q = new URLSearchParams(location.search).get('dag')
  let dag = q ? Number(q) : dagNummer(Date.now())
  const a = await haalInit()
  if (a.ok && !q) dag = a.data.dag
  $('dag').textContent = `Tower #${dag}: ${dagRegel(dag).naam}`
  if (a.ok) {
    const g = a.data.gemeenschap
    $('samen').textContent =
      g.hoedenVandaag > 0
        ? `${g.hoedenVandaag.toLocaleString('en-US')} hats stacked in r/${a.data.subreddit} today`
        : 'No hats yet today. Stack the first one.'
    if (a.data.vandaag) $('knop-speel').textContent = 'See today’s towers'
  }
  await document.fonts.load('40px "Lilita One"').catch(() => undefined)
  const canvas = $('canvas') as HTMLCanvasElement
  const t = new Tekenaar(canvas, await laadPlaatjes())
  const p = nieuwPotje(dag)
  p.hoeden = 5
  const beeld = nieuwBeeld()
  const teken = (): void => {
    t.pasAan()
    // Gloop rechts, de tekst en de knop links. Op een smalle post minder ver opzij.
    const vol = canvas.clientWidth >= document.body.clientWidth * 0.95
    beeld.opzij = vol ? Math.min(130, Math.max(60, (t.h - 380) * 0.5)) : 40
    t.teken(p, beeld, hoedVolgorde(dag), 16)
  }
  new ResizeObserver(teken).observe(canvas)
  teken()
  document.body.classList.add('klaar')
}

void opstart()
