# src/export_results.py
import pandas as pd
from typing import List, Dict

# Import config with defaults for CI/testing
try:
    from config import OUTPUT_CSV
except ImportError:
    OUTPUT_CSV = "outputs/jobs.csv"

def export_to_csv(enriched_jobs: List[Dict], path: str = None):
    if path is None:
        path = OUTPUT_CSV
    rows = []
    for j in enriched_jobs:
        rows.append({
            "job_id": j.get("id"),
            "title": j.get("title"),
            "company": j.get("company"),
            "location": j.get("location"),
            "similarity": j.get("similarity"),
            "link": j.get("redirect_url"),
            "cover_letter": j.get("cover_letter", "")
        })
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    return df

if __name__ == "__main__":
    print("Example export")
