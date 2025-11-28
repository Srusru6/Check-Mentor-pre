
import requests
import json

BASE_URL = "https://inspirehep.net/api"

def test_citations_endpoint(record_id):
    url = f"{BASE_URL}/literature/{record_id}/citations"
    print(f"Testing URL: {url}")
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            hits = data.get('hits', {}).get('hits', [])
            print(f"Hits count: {len(hits)}")
            if hits:
                print("First hit sample:", json.dumps(hits[0], indent=2)[:200])
        else:
            print("Response:", response.text[:500])
    except Exception as e:
        print(f"Error: {e}")

def test_search_refersto(record_id):
    url = f"{BASE_URL}/literature"
    params = {"q": f"refersto:recid:{record_id}", "size": 10}
    print(f"Testing Search URL: {url} with params {params}")
    try:
        response = requests.get(url, params=params)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            hits = data.get('hits', {}).get('hits', [])
            print(f"Hits count: {len(hits)}")
            if hits:
                print("First hit sample:", json.dumps(hits[0], indent=2)[:200])
        else:
            print("Response:", response.text[:500])
    except Exception as e:
        print(f"Error: {e}")

# GW150914 record id is 1410147
record_id = "1410147" 
print("--- Testing /citations endpoint ---")
test_citations_endpoint(record_id)
print("\n--- Testing search refersto ---")
test_search_refersto(record_id)
