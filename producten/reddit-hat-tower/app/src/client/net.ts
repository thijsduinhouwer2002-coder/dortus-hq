// Praten met de server. Op Reddit gaat dit naar de Devvit-server, lokaal naar dev/local.ts.
import {
  type DeelReq,
  type DeelRsp,
  Endpoint,
  type InitRsp,
  type ScoreReq,
  type ScoreRsp,
} from '../shared/api.ts'

/** Alleen lokaal: wie speelt er (?u=naam), zodat je met meer spelers kunt proeven. Reddit negeert dit. */
function lokaleNaam(): string {
  return new URLSearchParams(location.search).get('u') ?? 'you'
}

export type Antwoord<T> =
  | {ok: true; data: T}
  | {ok: false; fout: string; status: number}

async function vraag<T>(
  endpoint: string,
  body?: unknown,
): Promise<Antwoord<T>> {
  let rsp: Response
  try {
    rsp = await fetch(`/${endpoint}${location.search}`, {
      method: body === undefined ? 'GET' : 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'x-lokaal-naam': lokaleNaam(),
      },
      body: body === undefined ? undefined : JSON.stringify(body),
    })
  } catch (err) {
    return {
      ok: false,
      fout: err instanceof Error ? err.message : String(err),
      status: 0,
    }
  }
  let json: unknown
  try {
    json = await rsp.json()
  } catch {
    return {ok: false, fout: `HTTP ${rsp.status}`, status: rsp.status}
  }
  if (!rsp.ok) {
    const fout = (json as {error?: string}).error ?? `HTTP ${rsp.status}`
    return {ok: false, fout, status: rsp.status}
  }
  return {ok: true, data: json as T}
}

export const haalInit = (): Promise<Antwoord<InitRsp>> =>
  vraag<InitRsp>(Endpoint.Init)
export const stuurScore = (req: ScoreReq): Promise<Antwoord<ScoreRsp>> =>
  vraag<ScoreRsp>(Endpoint.Score, req)
export const deel = (req: DeelReq): Promise<Antwoord<DeelRsp>> =>
  vraag<DeelRsp>(Endpoint.Deel, req)
