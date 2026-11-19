/** Generic error detail for all responses. */
export type ErrorRsp = {error: string; status: number}

export type RijRanglijst = {naam: string; hoeden: number; reeks: number}

/** Wat het spel bij het openen ophaalt. */
export type InitRsp = {
  /** De toren van deze post. */
  dag: number
  /** De toren van vandaag (nieuwste post). */
  dagVandaag: number
  subreddit: string
  /** undefined als de speler niet is ingelogd. */
  naam: string | undefined
  /** Heeft deze speler de dagbeurt al gespeeld? Dan staat hier de uitslag. */
  vandaag: UitslagOpslag | undefined
  dagenOpRij: number
  besteOoit: number
  gemeenschap: GemeenschapStand
  top: RijRanglijst[]
  topGisteren: RijRanglijst[]
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
  /** Dagbeurt gestart maar nooit ingestuurd (herladen of weggegaan): telt als gebruikt, 0 hoeden. */
  afgebroken?: boolean
}

/** Begin van de dagbeurt. Telt alleen de eerste keer per speler per dag. */
export type StartReq = {dag: number}
export type StartRsp = {telt: boolean}

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

/** Word lid van deze subreddit (namens de speler, na een tik). */
export type LidRsp = {ok: boolean}

export type Endpoint = (typeof Endpoint)[keyof typeof Endpoint]
export const Endpoint = {
  Init: 'api/init',
  Start: 'api/start',
  Score: 'api/score',
  Lid: 'api/join',
  Deel: 'api/share',
  OnAppInstall: 'internal/on/app/install',
  OnMenuNewPost: 'internal/on/menu/new-post',
  OnDagPost: 'internal/scheduler/daily-post',
} as const

export const EndpointMethod = {
  [Endpoint.Init]: 'GET',
  [Endpoint.Start]: 'POST',
  [Endpoint.Score]: 'POST',
  [Endpoint.Lid]: 'POST',
  [Endpoint.Deel]: 'POST',
  [Endpoint.OnAppInstall]: 'POST',
  [Endpoint.OnMenuNewPost]: 'POST',
  [Endpoint.OnDagPost]: 'POST',
} as const satisfies {[endpoint: string]: 'GET' | 'POST'}
