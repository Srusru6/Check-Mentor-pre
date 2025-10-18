import requests
import os
import re
from bs4 import BeautifulSoup
import Levenshtein

def get_official_title_from_doi(doi):
    """
    Fetches the official title of an article from the CrossRef API.
    This is considered the ground truth for title comparison.
    """
    try:
        crossref_url = f"https://api.crossref.org/works/{doi}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(crossref_url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        title = data.get('message', {}).get('title', [None])[0]
        if title:
            print(f"Fetched official title from CrossRef: '{title}'")
            return title.strip()
    except Exception as e:
        print(f"Error fetching official title from CrossRef API: {e}")
    return None

def verify_title_similarity(official_title, downloaded_title):
    """
    Compares the official title with the downloaded title using Levenshtein distance.
    Returns True if they are similar enough, False otherwise.
    """
    if not official_title or not downloaded_title:
        print("Warning: Cannot verify title similarity because one of the titles is missing.")
        return False # Cannot verify

    similarity = Levenshtein.ratio(official_title.lower(), downloaded_title.lower())
    print(f"Title similarity ratio: {similarity:.2f}")
    if similarity < 0.8:
        print(f"Warning: Potential title mismatch!")
        print(f"  - Official Title:   '{official_title}'")
        print(f"  - Downloaded Title: '{downloaded_title}'")
        return False
    
    print("Titles match. Download is likely correct.")
    return True

def ExtractReferences(response_text):
    """
    Extract references from the response text and convert them to DOI format.
    """
    references = []
    try:
        soup = BeautifulSoup(response_text, 'html.parser')
        # Example: Find all links that might contain DOI references
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'doi.org' in href:
                doi = href.split('doi.org/')[-1]
                references.append(doi)
        # Remove duplicates and return
        references = list(set(references))
        print("Extracted References:", references)
    except Exception as e:
        print(f"Error extracting references: {e}")
    return references

def GetTitleFromDOI(DOI):
    doi_url = f"https://doi.org/{DOI}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    proxies = {
        # Uncomment and set your proxy if needed
        # 'http': 'http://your_proxy:port',
        # 'https': 'https://your_proxy:port'
    }

    # Try fetching title from DOI website
    try:
        response = requests.get(doi_url, headers=headers, proxies=proxies)
        print("DOI URL Status Code:", response.status_code)
        if response.status_code == 200:
            print("DOI URL Response Text:", response.text[:500])  # Print first 500 characters of the response
            references = ExtractReferences(response.text)  # Extract references
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')
            print("Extracted Title Tag:", title_tag)
            if title_tag and title_tag.text:
                return title_tag.text.strip(), references
    except Exception as e:
        print(f"Error fetching title from DOI: {e}")

    # Fallback: Try CrossRef API
    try:
        crossref_url = f"https://api.crossref.org/works/{DOI}"
        response = requests.get(crossref_url, headers=headers, proxies=proxies)
        print("CrossRef API Status Code:", response.status_code)
        if response.status_code == 200:
            data = response.json()
            title = data.get('message', {}).get('title', [None])[0]
            references = [item.get('DOI') for item in data.get('message', {}).get('reference', []) if item.get('DOI')]
            if title:
                print("Extracted Title from CrossRef:", title)
                print("Extracted References from CrossRef:", references)
                return title, references
    except Exception as e:
        print(f"Error fetching title from CrossRef API: {e}")

    # Fallback: Try Sci-Hub page
    try:
        sci_hub_url = f"https://sci-hub.se/{DOI}"
        response = requests.get(sci_hub_url, headers=headers, proxies=proxies)
        print("Sci-Hub URL Status Code:", response.status_code)
        if response.status_code == 200:
            references = ExtractReferences(response.text)  # Extract references
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')
            print("Extracted Title Tag from Sci-Hub:", title_tag)
            if title_tag and title_tag.text:
                return title_tag.text.strip(), references
    except Exception as e:
        print(f"Error fetching title from Sci-Hub: {e}")

    return "unknown_title", []

def get_recent_dois_from_crossref(query="physics", num_articles=5):
    """
    Get recent article DOIs from CrossRef API based on a query.
    """
    try:
        # Query CrossRef API for recent works related to the query, sorted by publication date
        url = f"https://api.crossref.org/works?query.bibliographic={query}&sort=published&order=desc&rows={num_articles}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        dois = [item['DOI'] for item in data['message']['items']]
        print(f"Found {len(dois)} recent DOIs from CrossRef for query '{query}': {dois}")
        return dois
    except Exception as e:
        print(f"Error fetching recent DOIs from CrossRef: {e}")
        return []

def get_recent_dois_from_arxiv(category="physics", num_articles=5):
    """
    Get recent article DOIs from arXiv.
    Note: arXiv papers might not have a DOI immediately. This function gets arXiv IDs.
    The rest of the script can try to find a DOI or download directly if possible.
    """
    try:
        # Scrape the 'new' page for the given category
        url = f"https://arxiv.org/list/{category}/new"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find links to the abstracts
        arxiv_ids = []
        for dt in soup.find_all('dt'):
            span = dt.find('span', class_='list-identifier')
            if span:
                arxiv_id_tag = span.find('a', title='Abstract')
                if arxiv_id_tag:
                    arxiv_ids.append(arxiv_id_tag.text.replace('arXiv:', ''))
            if len(arxiv_ids) >= num_articles:
                break
        
        print(f"Found {len(arxiv_ids)} recent arXiv IDs from category '{category}': {arxiv_ids}")
        return arxiv_ids
    except Exception as e:
        print(f"Error fetching recent DOIs from arXiv: {e}")
        return []

def get_recent_dois_from_pubmed(query="cancer", num_articles=5):
    """
    Get recent article DOIs from PubMed.
    """
    try:
        # Step 1: Search for PubMed IDs (PMIDs)
        search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        search_params = {
            'db': 'pubmed',
            'term': query,
            'sort': 'pub_date',
            'retmax': num_articles,
            'retmode': 'json'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(search_url, params=search_params, headers=headers)
        response.raise_for_status()
        search_data = response.json()
        pmids = search_data.get('esearchresult', {}).get('idlist', [])
        
        if not pmids:
            print(f"No articles found on PubMed for query '{query}'.")
            return []

        # Step 2: Fetch details for the PMIDs to get the DOIs
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        summary_params = {
            'db': 'pubmed',
            'id': ','.join(pmids),
            'retmode': 'json'
        }
        response = requests.get(summary_url, params=summary_params, headers=headers)
        response.raise_for_status()
        summary_data = response.json()
        
        dois = []
        results = summary_data.get('result', {})
        for pmid in pmids:
            article_info = results.get(pmid, {})
            article_ids = article_info.get('articleids', [])
            for article_id in article_ids:
                if article_id.get('idtype') == 'doi':
                    dois.append(article_id.get('value'))
                    break # Found DOI, move to next PMID
        
        print(f"Found {len(dois)} recent DOIs from PubMed for query '{query}': {dois}")
        return dois
    except Exception as e:
        print(f"Error fetching recent DOIs from PubMed: {e}")
        return []

def get_recent_dois_from_semantic_scholar(query="quantum computing", num_articles=5):
    """
    Get recent article DOIs from Semantic Scholar.
    Note: The API's default sort is by relevance, which often includes recent papers.
    """
    try:
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            'query': query,
            'limit': num_articles,
            'fields': 'externalIds'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        dois = []
        papers = data.get('data', [])
        for paper in papers:
            external_ids = paper.get('externalIds', {})
            if 'DOI' in external_ids:
                dois.append(external_ids['DOI'])
        
        print(f"Found {len(dois)} DOIs from Semantic Scholar for query '{query}': {dois}")
        return dois
    except Exception as e:
        print(f"Error fetching DOIs from Semantic Scholar: {e}")
        return []

def get_pdf_from_publisher(doi):
    """
    Tries to find the direct PDF download link from the publisher's website.
    This method is most effective when run from an academic network (e.g., via University VPN).
    """
    try:
        landing_url = f"https://doi.org/{doi}"
        print(f"Attempting to find PDF via publisher page: {landing_url}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Use a session to handle potential redirects gracefully
        session = requests.Session()
        response = session.get(landing_url, headers=headers, allow_redirects=True, timeout=20)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # --- Heuristics to find the PDF link ---
        # This may need to be expanded for different publishers
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Rule 1: Direct link to a .pdf file
            if href.lower().endswith('.pdf'):
                print(f"Found potential PDF link (ends with .pdf): {href}")
                # Handle relative URLs
                return requests.compat.urljoin(response.url, href)
            
            # Rule 2: Link contains '/pdf/' which is common (e.g., Wiley, Springer)
            if '/pdf/' in href or '/content/pdf/' in href:
                print(f"Found potential PDF link (contains /pdf/): {href}")
                return requests.compat.urljoin(response.url, href)

            # Rule 3: Link text suggests it's a PDF download
            if 'pdf' in link.text.lower() or 'full text' in link.text.lower():
                 print(f"Found potential PDF link (text match): {href}")
                 return requests.compat.urljoin(response.url, href)

        print("Could not find a direct PDF link on the publisher page.")
        return None

    except Exception as e:
        print(f"Error fetching from publisher page: {e}")
        return None

# function: Download English-paper by DOI
def GetDownloadUrl(doi):
    base_urls = [
        "https://sci-hub.se",
        "https://sci-hub.st",
        "https://sci-hub.ru"
    ]
    for base_url in base_urls:
        url = f"{base_url}/{doi}"
        try:
            print(f"Trying URL: {url}")
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                return url
            else:
                print(f"Failed with status code: {r.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")
    raise ConnectionError("All Sci-Hub domains failed.")

# Example usage
try:
    paperDownloadUrl = GetDownloadUrl("10.1126/science.177.4047.393")
    print(f"Download URL: {paperDownloadUrl}")
except ConnectionError as e:
    print(f"Error: {e}")

def DownloadFileByUrl(DownloadUrl, FileTitle):
    """
    Downloads a file from a URL and saves it.
    Returns the full path to the saved file, or None if download fails.
    """
    if not DownloadUrl or 'http' not in DownloadUrl:
        print("Invalid download URL provided.")
        return None

    # Sanitize the file name to remove illegal characters
    sane_title = re.sub(r'[\\/:*?"<>|#&]', '_', FileTitle)
    # Prevent extremely long filenames
    sane_title = (sane_title[:150] + '..') if len(sane_title) > 150 else sane_title
    file_name = f"{sane_title}.pdf"

    # Ensure the save path exists
    save_path = os.path.join(os.getcwd(), "Downloads_pdf")
    os.makedirs(save_path, exist_ok=True)
    full_path = os.path.join(save_path, file_name)

    try:
        print(f"Downloading from: {DownloadUrl}")
        r = requests.get(DownloadUrl, timeout=60) # Increased timeout for large files
        r.raise_for_status()

        # Crucial check: Ensure we are actually downloading a PDF
        if 'application/pdf' not in r.headers.get('Content-Type', ''):
            print(f"Error: The content at the URL is not a PDF. Content-Type: {r.headers.get('Content-Type')}")
            print("Skipping download.")
            return None

        with open(full_path, "wb") as code:
            code.write(r.content)
        print(f"File '{file_name}' has been downloaded successfully to '{save_path}'.")
        return full_path
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")
        return None

def download_and_process_doi(doi):
    """Helper function to get title, download, verify, and process one DOI."""
    print(f"\n--- Processing DOI: {doi} ---")
    
    # 1. Get the official title from CrossRef as the ground truth
    official_title = get_official_title_from_doi(doi)
    if not official_title:
        print("Could not retrieve official title. Aborting processing for this DOI.")
        return

    # 2. Get the title from the source page (this will be used for verification)
    page_title, _ = GetTitleFromDOI(doi)
    
    # Use the official title for the filename for consistency
    print(f"Using official title for filename: '{official_title}'")
    
    # 3. Attempt to get a download URL
    paperDownloadUrl = None
    
    # Strategy A: Prioritize direct download from publisher
    print("\nStep 1: Trying to download directly from publisher (requires VPN for off-campus).")
    paperDownloadUrl = get_pdf_from_publisher(doi)
    
    # Strategy B: Fallback to Sci-Hub if direct download fails
    if not paperDownloadUrl:
        print("Step 2: Direct download failed. Falling back to Sci-Hub.")
        try:
            paperDownloadUrl = GetDownloadUrl(doi)
        except ConnectionError as e:
            print(f"Could not get a download URL from any source for {doi}: {e}")
            return # Stop processing this DOI

    # 4. Download the file
    downloaded_file_path = DownloadFileByUrl(paperDownloadUrl, official_title)
    
    # 5. Verify and Cleanup
    if downloaded_file_path:
        # Compare the official title with the title scraped from the download page
        is_verified = verify_title_similarity(official_title, page_title)
        
        if not is_verified:
            print(f"Verification failed. Deleting downloaded file: {downloaded_file_path}")
            try:
                os.remove(downloaded_file_path)
                print("File deleted successfully.")
            except OSError as e:
                print(f"Error deleting file: {e}")
        else:
            print("Verification successful. File has been kept.")


# --- Main Execution ---

# Strategy 1: Download a specific paper (original behavior)
print("\n=== Strategy 1: Downloading a specific DOI ===")
doi_EnglishPaper = '10.53846/goediss-2917'
download_and_process_doi(doi_EnglishPaper)


# Strategy 2: Download recent papers from CrossRef based on a query
print("\n=== Strategy 2: Downloading recent papers from CrossRef ===")
recent_dois_crossref = get_recent_dois_from_crossref(query="physics", num_articles=2)
for doi in recent_dois_crossref:
    download_and_process_doi(doi)


# Strategy 3: Download recent papers from arXiv
# Note: We use the arXiv ID as the 'DOI' here, which Sci-Hub often understands.
print("\n=== Strategy 3: Downloading recent papers from arXiv ===")
recent_arxiv_ids = get_recent_dois_from_arxiv(category="physics", num_articles=2)  # Physics category
for arxiv_id in recent_arxiv_ids:
    download_and_process_doi(arxiv_id)

# Strategy 4: Download recent papers from PubMed
print("\n=== Strategy 4: Downloading recent papers from PubMed ===")
recent_dois_pubmed = get_recent_dois_from_pubmed(query="physics", num_articles=2)
for doi in recent_dois_pubmed:
    download_and_process_doi(doi)

# Strategy 5: Download recent papers from Semantic Scholar
print("\n=== Strategy 5: Downloading recent papers from Semantic Scholar ===")
recent_dois_semantic = get_recent_dois_from_semantic_scholar(query="physics", num_articles=2)
for doi in recent_dois_semantic:
    download_and_process_doi(doi)

print("\n--- All tasks completed. ---")

# The original final lines are now part of the helper function and strategies above.
# doi_EnglishPaper = '10.53846/goediss-2917'
# articleTitle, references = GetTitleFromDOI(doi_EnglishPaper)
# print("Article Title:", articleTitle)
# print("References (DOI format):", references)
# paperDownloadUrl = GetDownloadUrl(doi_EnglishPaper) #doi_EnglishPaper
# DownloadFileByUrl(paperDownloadUrl, articleTitle)
