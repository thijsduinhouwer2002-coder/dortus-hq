// Lokale versie zonder Reddit: serveert public/ en dezelfde /api-routes, met opslag in het geheugen.
// Start: npm run local   (daarna http://localhost:5173/splash.html of /game.html)
// Andere speler: ?u=naam. Andere dag: ?dag=12. Met proefspelers op de ranglijst: PROEF=1 npm run local
import {readFile} from 'node:fs/promises'
import {createServer, type IncomingMessage} from 'node:http'
import {extname, join, normalize} from 'node:path'
import {GeheugenOpslag} from '../src/server/geheugen-opslag.ts'
import {
  deelTekst,
  FoutVerzoek,
  init,
  score,
  type Wie,
} from '../src/server/logica.ts'
import {Endpoint} from '../src/shared/api.ts'
import {speelProef} from '../src/shared/proefspeler.ts'
import {dagNummer} from '../src/shared/spel.ts'

const POORT = Number(process.env.PORT ?? 5173)
const MAP = join(import.meta.dirname, '..', 'public')
const db = new GeheugenOpslag()
const SUB = 'GloopTowerTest'

const SOORT: Record<string, string> = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.png': 'image/png',
  '.ttf': 'font/ttf',
  '.map': 'application/json',
}

function wieVan(req: IncomingMessage): Wie {
  const naam = String(req.headers['x-lokaal-naam'] ?? 'you')
  return {subreddit: SUB, naam, userId: `t2_${naam}`}
}

async function leesJson(req: IncomingMessage): Promise<unknown> {
  const delen: Buffer[] = []
  for await (const d of req) delen.push(d as Buffer)
  try {
    return JSON.parse(Buffer.concat(delen).toString() || '{}')
  } catch {
    throw new FoutVerzoek('bad json')
  }
}

async function proefspelers(dag: number): Promise<void> {
  // Echte potjes van nep-spelers (zelfde regels, verschillend mikken), alleen lokaal.
  const spelers = [
    ['practice_bot_ada', 815, 20, 0.05],
    ['practice_bot_bo', 810, 45, 0.12],
    ['practice_bot_cy', 830, 60, 0.2],
    ['practice_bot_dee', 760, 50, 0.25],
    ['practice_bot_eli', 815, 35, 0.3],
  ] as const
  for (const [i, [naam, mik, ruis, mis]] of spelers.entries()) {
    const p = speelProef(dag, mik, ruis, mis, 11 + i * 97)
    await score(db, {subreddit: SUB, naam, userId: `t2_${naam}`}, dag, {
      dag,
      drukken: p.drukken,
    })
  }
}

const server = createServer(async (req, rsp) => {
  const url = new URL(req.url ?? '/', `http://localhost:${POORT}`)
  const pad = url.pathname.slice(1)
  const dag = url.searchParams.get('dag')
    ? Number(url.searchParams.get('dag'))
    : dagNummer(Date.now())
  const stuur = (status: number, json: unknown): void => {
    const body = JSON.stringify(json)
    rsp.writeHead(status, {'Content-Type': 'application/json'})
    rsp.end(body)
  }
  try {
    if (pad === Endpoint.Init && req.method === 'GET')
      return stuur(200, await init(db, wieVan(req), dag))
    if (pad === Endpoint.Score && req.method === 'POST') {
      return stuur(
        200,
        await score(db, wieVan(req), dag, (await leesJson(req)) as never),
      )
    }
    if (pad === Endpoint.Deel && req.method === 'POST') {
      const tekst = await deelTekst(db, wieVan(req), dag)
      console.log(`[reactie die op Reddit geplaatst zou worden]\n${tekst}\n`)
      return stuur(200, {ok: true, tekst})
    }
    if (pad.startsWith('api/'))
      return stuur(404, {error: 'not found', status: 404})
    const bestand = normalize(join(MAP, pad || 'splash.html'))
    if (!bestand.startsWith(MAP)) return stuur(403, {error: 'no', status: 403})
    const inhoud = await readFile(bestand)
    rsp.writeHead(200, {
      'Content-Type': SOORT[extname(bestand)] ?? 'application/octet-stream',
    })
    rsp.end(inhoud)
  } catch (err) {
    if (err instanceof FoutVerzoek)
      return stuur(err.status, {error: err.message, status: err.status})
    if ((err as NodeJS.ErrnoException).code === 'ENOENT')
      return stuur(404, {error: 'not found', status: 404})
    console.error(err)
    stuur(500, {error: 'server error', status: 500})
  }
})

if (process.env.PROEF) await proefspelers(dagNummer(Date.now()))
server.listen(POORT, () =>
  console.log(
    `Gloop's Hat Tower lokaal: http://localhost:${POORT}/splash.html`,
  ),
)
