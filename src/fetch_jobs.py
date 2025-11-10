# src/fetch_jobs.py
import requests
from typing import List, Dict
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY, ADZUNA_COUNTRY, ADZUNA_RESULTS_PER_PAGE

def fetch_adzuna_jobs(query: str, location: str = "", page: int = 1, results_per_page: int = None) -> List[Dict]:
    if results_per_page is None:
        results_per_page = ADZUNA_RESULTS_PER_PAGE
    url = f"https://api.adzuna.com/v1/api/jobs/{ADZUNA_COUNTRY}/search/{page}"
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": results_per_page,
        "what": query
    }
    if location:
        params["where"] = location
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for r in data.get("results", []):
        results.append({
            "id": r.get("id"),
            "title": r.get("title"),
            "company": r.get("company", {}).get("display_name"),
            "location": r.get("location", {}).get("display_name"),
            "description": r.get("description"),
            "redirect_url": r.get("redirect_url")
        })
    return results

if __name__ == "__main__":
    jobs = fetch_adzuna_jobs("data analyst", "remote", page=1)
    print(len(jobs))
    for j in jobs[:3]:
        print(j["title"], "-", j["company"])
