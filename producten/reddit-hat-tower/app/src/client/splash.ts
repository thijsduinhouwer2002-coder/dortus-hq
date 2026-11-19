// De post in de feed (Devvit-entrypoint "default"): Gloop met zijn toren, de dag, en een knop.
// Een tik opent het spel groot (requestExpandedMode). Lokaal gaat de knop gewoon naar game.html.
import {requestExpandedMode} from '@devvit/web/client'
import {dagNummer, dagRegel, hoedVolgorde, nieuwPotje} from '../shared/spel.ts'
import {laadKunst} from './kunst.ts'
import {haalInit} from './net.ts'
import {nieuwBeeld, Scene} from './scene.ts'

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
  const beeld = nieuwBeeld()
  beeld.toren = 5
  beeld.bordje = false
  if (a.ok) {
    const g = a.data.gemeenschap
    $('samen').textContent =
      g.hoedenVandaag > 0
        ? `${g.hoedenVandaag.toLocaleString('en-US')} hats stacked in r/${a.data.subreddit} today`
        : 'No hats yet today. Stack the first one.'
    if (a.data.vandaag) $('knop-speel').textContent = 'See the towers'
  }
  await document.fonts.load('40px "Lilita One"').catch(() => undefined)
  const canvas = $('canvas') as HTMLCanvasElement
  const scene = new Scene(canvas, await laadKunst())
  const p = nieuwPotje(dag)
  const volgorde = hoedVolgorde(dag)
  let vorige = performance.now()
  const lus = (t: number): void => {
    // Gloop rechts, de tekst en de knop links. Op een smalle post minder ver opzij.
    const vol = canvas.clientWidth >= document.body.clientWidth * 0.95
    beeld.opzij = vol ? Math.min(96, Math.max(50, (scene.h - 380) * 0.45)) : 30
    scene.teken(p, beeld, volgorde, Math.min(50, t - vorige), t)
    vorige = t
    requestAnimationFrame(lus)
  }
  scene.pasAan()
  new ResizeObserver(() => scene.pasAan()).observe(canvas)
  requestAnimationFrame(lus)
  document.body.classList.add('klaar')
}

void opstart()
