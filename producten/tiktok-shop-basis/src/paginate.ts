// Pagina's doorlopen met next_page_token, met een harde bovengrens.

export const MAX_PAGINAS = 500;

export interface Pagina<T> {
  items: T[];
  nextPageToken?: string;
}

/** Haalt pagina's op tot next_page_token leeg is of ontbreekt. */
export async function* allePaginas<T>(
  haal: (pageToken: string | undefined) => Promise<Pagina<T>>,
  maxPaginas = MAX_PAGINAS,
): AsyncGenerator<T> {
  let token: string | undefined;
  for (let i = 0; i < maxPaginas; i++) {
    const p = await haal(token);
    for (const item of p.items) yield item;
    if (!p.nextPageToken) return;
    token = p.nextPageToken;
  }
  throw new Error(`meer dan ${maxPaginas} pagina's: gestopt om een eindeloze lus te voorkomen`);
}

export async function verzamel<T>(it: AsyncIterable<T>): Promise<T[]> {
  const uit: T[] = [];
  for await (const x of it) uit.push(x);
  return uit;
}
