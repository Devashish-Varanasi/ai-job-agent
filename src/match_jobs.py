# src/match_jobs.py
from sentence_transformers import SentenceTransformer, util
from typing import List, Dict
import torch

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def compute_similarity(resume_text: str, jobs: List[Dict], top_k:int=20) -> List[Dict]:
    model = get_model()
    # encode resume once
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    enriched = []
    for job in jobs:
        desc = job.get("description") or ""
        emb = model.encode(desc, convert_to_tensor=True)
        sim = util.cos_sim(resume_emb, emb).item()
        job_copy = job.copy()
        job_copy["similarity"] = float(sim)
        enriched.append(job_copy)
    enriched = sorted(enriched, key=lambda x: x["similarity"], reverse=True)
    return enriched[:top_k]

if __name__ == "__main__":
    test_resume = "Data analyst skilled in Python, SQL, Pandas, Power BI"
    sample_jobs = [{"description":"We need SQL and Power BI expertise for analytics.","title":"Analyst","company":"X"}]
    print(compute_similarity(test_resume, sample_jobs))
