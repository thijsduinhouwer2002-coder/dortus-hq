// De server op Reddit (Devvit Web). Dun: leest wie het is, roept logica.ts aan met Redis als opslag.
// Bouwt op de officiele template reddit/devvit-template-bare (51e9aab).
import {once} from 'node:events'
import type {IncomingMessage, ServerResponse} from 'node:http'
import {context, reddit} from '@devvit/web/server'
import type {
  PartialJsonValue,
  TriggerResponse,
  UiResponse,
} from '@devvit/web/shared'
import {
  type DeelReq,
  type DeelRsp,
  Endpoint,
  EndpointMethod,
  type ErrorRsp,
  type InitRsp,
  type LidRsp,
  type ScoreReq,
  type ScoreRsp,
  type StartReq,
  type StartRsp,
} from '../shared/api.ts'
import {dagNummer, dagRegel} from '../shared/spel.ts'
import {deelTekst, FoutVerzoek, init, score, start, type Wie} from './logica.ts'
import {redisOpslag} from './redis-opslag.ts'

type AnyRsp =
  | StartRsp
  | LidRsp
  | InitRsp
  | ScoreRsp
  | DeelRsp
  | UiResponse
  | TriggerResponse
  | ErrorRsp

function wie(): Wie {
  return {
    subreddit: context.subredditName,
    naam: context.username,
    userId: context.userId,
  }
}

export async function onReq(
  reqMsg: IncomingMessage,
  rspMsg: ServerResponse,
): Promise<void> {
  try {
    await route(reqMsg, rspMsg)
  } catch (err) {
    if (err instanceof FoutVerzoek) {
      writeJson<ErrorRsp>(
        err.status,
        {error: err.message, status: err.status},
        rspMsg,
      )
      return
    }
    const msg = `server error; ${err instanceof Error ? err.stack : err}`
    console.error(msg)
    writeJson<ErrorRsp>(500, {error: 'server error', status: 500}, rspMsg)
  }
}

async function route(
  reqMsg: IncomingMessage,
  rspMsg: ServerResponse,
): Promise<void> {
  const endpoint = reqMsg.url?.slice(1).split('?')[0] as Endpoint
  const method = EndpointMethod[endpoint]
  const dag = dagNummer(Date.now())

  let rsp: AnyRsp
  if (method !== reqMsg.method) {
    rsp = {error: 'not found', status: 404}
  } else {
    switch (endpoint) {
      case Endpoint.Init:
        rsp = await init(redisOpslag, wie(), dag)
        break
      case Endpoint.Start:
        rsp = await start(
          redisOpslag,
          wie(),
          dag,
          await readJson<StartReq>(reqMsg),
        )
        break
      case Endpoint.Lid:
        // Alleen na een tik op "Join r/...": Reddit vraagt dat de speler weet wat er gebeurt.
        await reddit.subscribeToCurrentSubreddit()
        rsp = {ok: true}
        break
      case Endpoint.Score:
        rsp = await score(
          redisOpslag,
          wie(),
          dag,
          await readJson<ScoreReq>(reqMsg),
        )
        break
      case Endpoint.Deel: {
        const req = await readJson<DeelReq>(reqMsg)
        const tekst = await deelTekst(redisOpslag, wie(), req.dag)
        const postId = context.postId
        if (!postId) throw new FoutVerzoek('no post')
        // Fase 2: werkt pas na `devvit upload`; Reddit plaatst de reactie namens de speler.
        await reddit.submitComment({id: postId, text: tekst, runAs: 'USER'})
        rsp = {ok: true, tekst}
        break
      }
      case Endpoint.OnMenuNewPost:
        rsp = await maakDagPost()
        break
      case Endpoint.OnAppInstall:
        await maakDagPost()
        rsp = {}
        break
      case Endpoint.OnDagPost:
        await maakDagPost()
        rsp = {}
        break
      default:
        endpoint satisfies never
        rsp = {error: 'not found', status: 404}
        break
    }
  }

  writeJson<PartialJsonValue>('status' in rsp ? rsp.status : 200, rsp, rspMsg)
}

/** Elke dag om 00:00 UTC een nieuwe post (scheduler in devvit.json), of via het menu. */
async function maakDagPost(): Promise<UiResponse> {
  const dag = dagNummer(Date.now())
  const post = await reddit.submitCustomPost({
    title: `Gloop's Hat Tower #${dag}: ${dagRegel(dag).naam}`,
  })
  return {
    showToast: {text: `Tower #${dag} posted.`, appearance: 'success'},
    navigateTo: post.url,
  }
}

async function readJson<T>(reqMsg: IncomingMessage): Promise<T> {
  const chunks: Uint8Array[] = []
  reqMsg.on('data', chunk => chunks.push(chunk))
  await once(reqMsg, 'end')
  try {
    return JSON.parse(`${Buffer.concat(chunks)}`) as T
  } catch {
    throw new FoutVerzoek('bad json')
  }
}

function writeJson<T extends PartialJsonValue>(
  status: number,
  json: Readonly<T>,
  rsp: ServerResponse,
): void {
  const body = JSON.stringify(json)
  rsp.writeHead(status, {
    'Content-Length': Buffer.byteLength(body),
    'Content-Type': 'application/json',
  })
  rsp.end(body)
}
