
import requests
import re
from urllib.parse import unquote

OPENALEX_BASE = "https://api.openalex.org"

def normalize_doi(doi: str) -> str:
    if not doi: return ""
    doi = unquote(doi).strip()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi, flags=re.I)
    return doi.strip().strip(' .;')

def get_openalex_id_for_doi(doi: str):
    doi = normalize_doi(doi)
    print(f"Normalized DOI: {doi}")
    if not doi: return None
    try:
        url = f"{OPENALEX_BASE}/works/doi:{requests.utils.quote(doi, safe='')}"
        print(f"Fetching OpenAlex ID from: {url}")
        r = requests.get(url, headers={'User-Agent': 'CheckMentor/1.0'}, timeout=30)
        print(f"Status: {r.status_code}")
        if r.status_code == 404: return None
        r.raise_for_status()
        data = r.json()
        oid = data.get("id")
        print(f"Found OID: {oid}")
        return oid.rsplit("/", 1)[-1] if oid else None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_citing_dois_openalex(doi: str, limit: int = 100):
    oid = get_openalex_id_for_doi(doi)
    if not oid: 
        print("No OID found.")
        return []
    
    url = f"{OPENALEX_BASE}/works"
    params = {
        "filter": f"cites:{oid}",
        "select": "doi",
        "per_page": min(limit, 200),
        "sort": "publication_year:desc",
    }
    
    dois = set()
    try:
        print(f"Fetching citing works for {oid}...")
        r = requests.get(url, params=params, headers={'User-Agent': 'CheckMentor/1.0'}, timeout=60)
        print(f"Status: {r.status_code}")
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        print(f"Results count: {len(results)}")
        
        for item in results:
            d = item.get("doi")
            if d:
                nd = normalize_doi(d)
                if nd: dois.add(nd)
        
    except Exception as e:
        print(f"OpenAlex error: {e}")
        
    return list(dois)[:limit]

# Test with a known DOI
doi = "10.1103/PhysRevLett.116.061102" # GW150914
print(f"Testing DOI: {doi}")
cited = get_citing_dois_openalex(doi, limit=5)
print(f"Cited DOIs: {cited}")
