import requests
import os
import re
from bs4 import BeautifulSoup

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
    if DownloadUrl != '' and DownloadUrl.find('http') >= 0:
        # Ensure the file name ends with .pdf
        FileName = f"{FileTitle}.pdf"
        # Sanitize the file name to remove illegal characters
        FileName = re.sub(r'[\\/:*?"<>|#&]', '_', FileName)

        # Ensure the save path exists
        save_path = os.path.join(os.getcwd(), "Downloads_pdf")
        os.makedirs(save_path, exist_ok=True)
        FileName = os.path.join(save_path, FileName)

        r1 = requests.get(DownloadUrl)
        if r1:
            with open(FileName, "wb") as code:
                code.write(r1.content)
                print(DownloadUrl + '  File ' + FileName + '  has been downloaded successfully！')
        else:
            print('Failed to download')
    print("Download URL:", DownloadUrl)

doi_EnglishPaper = '10.1126/science.177.4047.393'
articleTitle, references = GetTitleFromDOI(doi_EnglishPaper)
print("Article Title:", articleTitle)
print("References (DOI format):", references)
paperDownloadUrl = GetDownloadUrl(doi_EnglishPaper) #doi_EnglishPaper
DownloadFileByUrl(paperDownloadUrl, articleTitle)
