#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a DOI, fetch the DOIs of all citing articles using the OpenAlex API.

Usage examples:
  - Single DOI -> print to stdout
      python cited_by_from_doi.py --doi 10.1038/nature12373

  - Multiple DOIs from a file -> write CSV
      python cited_by_from_doi.py --input dois.txt --out citing.csv

Notes:
- Uses OpenAlex (https://api.openalex.org). No API key required.
- You may optionally provide a contact email via --email to be polite (sent as `mailto` param).
- Output CSV columns: source_doi, citing_doi, citing_openalex_id, title, year
"""

import argparse
import csv
import os
import sys
import time
from typing import Dict, Iterable, List, Optional, Tuple

import requests

OPENALEX_BASE = "https://api.openalex.org"
UA = (
    "Check-Mentor/1.0 (cited-by script); "
    f"Python/{sys.version_info.major}.{sys.version_info.minor}; "
    "https://openalex.org"
)


def norm_doi(doi: Optional[str]) -> Optional[str]:
    if not doi:
        return None
    doi = doi.strip()
    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    doi = doi.replace("DOI:", "").strip()
    return doi.lower()


def get_openalex_id_for_doi(doi: str, email: Optional[str] = None) -> Optional[str]:
    """Resolve DOI to OpenAlex work ID (e.g., W2741809807). Returns None if not found."""
    doi = norm_doi(doi)
    if not doi:
        return None
    url = f"{OPENALEX_BASE}/works/doi:{requests.utils.quote(doi, safe='')}"
    params = {}
    if email:
        params["mailto"] = email
    headers = {"User-Agent": UA}
    r = requests.get(url, params=params, headers=headers, timeout=30)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    data = r.json()
    oid = data.get("id")
    if not oid:
        return None
    # id format: https://openalex.org/W2741809807
    return oid.rsplit("/", 1)[-1]


def iter_citing_works(openalex_id: str, email: Optional[str] = None) -> Iterable[Dict]:
    """Yield citing works (OpenAlex records) for a given OpenAlex work ID."""
    url = f"{OPENALEX_BASE}/works"
    params = {
        "filter": f"cites:{openalex_id}",
        "select": "id,doi,display_name,publication_year",
        "per_page": 200,
        "cursor": "*",
        # Use a stable sort to keep pagination deterministic
        "sort": "publication_year:desc"
    }
    if email:
        params["mailto"] = email
    headers = {"User-Agent": UA}

    retries = 0
    max_retries = 5
    backoff = 2

    while True:
        try:
            r = requests.get(url, params=params, headers=headers, timeout=60)
            if r.status_code in (429, 500, 502, 503, 504):
                # backoff and retry
                if retries < max_retries:
                    wait = backoff * (2 ** retries)
                    time.sleep(wait)
                    retries += 1
                    continue
                r.raise_for_status()
            r.raise_for_status()
            data = r.json()
            results = data.get("results", [])
            for item in results:
                yield item
            next_cursor = data.get("meta", {}).get("next_cursor")
            if not next_cursor:
                break
            params["cursor"] = next_cursor
            retries = 0  # reset after a successful page
        except requests.RequestException:
            if retries < max_retries:
                wait = backoff * (2 ** retries)
                time.sleep(wait)
                retries += 1
                continue
            raise


def citing_dois_for_one(doi: str, email: Optional[str] = None) -> List[Tuple[str, str, str, Optional[int]]]:
    """Return list of tuples: (source_doi, citing_doi, citing_openalex_id, year)."""
    src = norm_doi(doi)
    if not src:
        return []
    openalex_id = get_openalex_id_for_doi(src, email=email)
    if not openalex_id:
        return []
    rows: List[Tuple[str, str, str, Optional[int]]] = []
    for work in iter_citing_works(openalex_id, email=email):
        raw_doi = work.get("doi") or ""
        cdoi = norm_doi(raw_doi)
        if not cdoi:
            continue  # skip works without DOIs
        wid = (work.get("id") or "").rsplit("/", 1)[-1]
        year = work.get("publication_year")
        rows.append((src, cdoi, wid, year))
    return rows


def read_dois_from_file(path: str) -> List[str]:
    dois: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            dois.append(line)
    return dois


def write_csv(rows: List[Tuple[str, str, str, Optional[int]]], out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_doi", "citing_doi", "citing_openalex_id", "year"])
        for r in rows:
            w.writerow(r)


def main() -> int:
    parser = argparse.ArgumentParser(description="Find citing DOIs via OpenAlex")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--doi", help="Single DOI to query")
    g.add_argument("--input", help="Path to a text file containing DOIs (one per line)")
    parser.add_argument("--out", help="Path to write CSV results; if omitted, prints to stdout")
    parser.add_argument("--email", help="Contact email for OpenAlex mailto param (recommended)")
    args = parser.parse_args()

    email = args.email or os.environ.get("OPENALEX_MAILTO")

    all_rows: List[Tuple[str, str, str, Optional[int]]] = []
    sources: List[str]
    if args.doi:
        sources = [args.doi]
    else:
        sources = read_dois_from_file(args.input)

    if not sources:
        print("No DOIs to process.", file=sys.stderr)
        return 1

    # Process each DOI sequentially (OpenAlex allows decent throughput; keep it simple)
    for i, src in enumerate(sources, 1):
        try:
            rows = citing_dois_for_one(src, email=email)
            all_rows.extend(rows)
            print(f"[{i}/{len(sources)}] {src}: {len(rows)} citing DOIs found", file=sys.stderr)
            # brief courtesy pause between different source DOIs
            time.sleep(0.2)
        except Exception as e:
            print(f"Error processing {src}: {e}", file=sys.stderr)

    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        write_csv(all_rows, args.out)
        print(f"Saved {len(all_rows)} rows to {args.out}")
    else:
        # Print to stdout as simple list of citing DOIs (unique), one per line
        seen = set()
        for _src, cdoi, _wid, _year in all_rows:
            if cdoi not in seen:
                print(cdoi)
                seen.add(cdoi)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
