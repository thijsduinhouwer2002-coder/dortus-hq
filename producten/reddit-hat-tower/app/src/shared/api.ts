/** Generic error detail for all responses. */
export type ErrorRsp = {error: string; status: number}

export type RijRanglijst = {naam: string; hoeden: number; reeks: number}

/** Wat het spel bij het openen ophaalt. */
export type InitRsp = {
  dag: number
  subreddit: string
  /** undefined als de speler niet is ingelogd. */
  naam: string | undefined
  /** Heeft deze speler de dagbeurt al gespeeld? Dan staat hier de uitslag. */
  vandaag: UitslagOpslag | undefined
  dagenOpRij: number
  besteOoit: number
  gemeenschap: GemeenschapStand
  top: RijRanglijst[]
}

export type GemeenschapStand = {
  /** Alle hoeden van alle dagbeurten vandaag in deze subreddit. */
  hoedenVandaag: number
  spelersVandaag: number
  /** Alle hoeden sinds de eerste dag. */
  hoedenOoit: number
}

export type UitslagOpslag = {
  hoeden: number
  besteReeks: number
  uitslagen: string[]
  plek: number
}

/** De dagbeurt: de server speelt hem zelf na uit de drukken, dus de score komt niet van de client. */
export type ScoreReq = {dag: number; drukken: number[]}
export type ScoreRsp = {
  uitslag: UitslagOpslag
  dagenOpRij: number
  besteOoit: number
  nieuwBeste: boolean
  gemeenschap: GemeenschapStand
  top: RijRanglijst[]
}

/** Plaats de uitslagkaart als reactie onder de post (namens de speler, fase 2). */
export type DeelReq = {dag: number}
export type DeelRsp = {ok: boolean; tekst: string}

export type Endpoint = (typeof Endpoint)[keyof typeof Endpoint]
export const Endpoint = {
  Init: 'api/init',
  Score: 'api/score',
  Deel: 'api/share',
  OnAppInstall: 'internal/on/app/install',
  OnMenuNewPost: 'internal/on/menu/new-post',
  OnDagPost: 'internal/scheduler/daily-post',
} as const

export const EndpointMethod = {
  [Endpoint.Init]: 'GET',
  [Endpoint.Score]: 'POST',
  [Endpoint.Deel]: 'POST',
  [Endpoint.OnAppInstall]: 'POST',
  [Endpoint.OnMenuNewPost]: 'POST',
  [Endpoint.OnDagPost]: 'POST',
} as const satisfies {[endpoint: string]: 'GET' | 'POST'}
