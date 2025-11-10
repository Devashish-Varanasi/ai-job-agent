# app.py (at project root)

from src.parse_resume import parse_resume
from src.fetch_jobs import fetch_adzuna_jobs
from src.match_jobs import compute_similarity
from src.generate_cover import generate_cover, save_cover_letter_docx
from src.export_results import export_to_csv
from config import DEFAULT_RESUME
from typing import Optional
from datetime import datetime
import os

def run_pipeline(resume_path: Optional[str] = None, query: Optional[str] = None, location: str = "", generate_covers: bool = True, output_csv: Optional[str] = None):
    resume_path = resume_path or DEFAULT_RESUME
    print("[1/6] Parsing resume:", resume_path)
    resume_summary = parse_resume(resume_path)
    print("Found skills:", resume_summary.get("skills"))
    
    # Auto-detect job role from resume if no query provided
    if query is None:
        detected_role = resume_summary.get("target_role", "data analyst")
        query = str(detected_role) if detected_role else "data analyst"
        print(f"Auto-detected target role: {query}")
    else:
        print(f"Using provided query: {query}")
    
    # Ensure query is a string at this point
    assert query is not None, "Query must be provided or auto-detected"
    
    # Generate unique filename with timestamp if not provided
    if output_csv is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        job_type_clean = query.replace(" ", "_").replace("/", "-")
        output_csv = f"outputs/jobs_{job_type_clean}_{timestamp}.csv"
        os.makedirs("outputs", exist_ok=True)
    
    # Initialize cover letters folder variable
    cover_letters_folder = None
    
    print(f"[2/6] Fetching jobs for query: {query}")
    jobs = fetch_adzuna_jobs(query, location=location, page=1)

    print(f"Got {len(jobs)} jobs — computing similarity...")
    enriched = compute_similarity(resume_summary.get("raw_text", ""), jobs, top_k=30)

    if generate_covers:
        print("[3/6] Generating cover letters for top matches (this may take time if using local LLM)…")
        # Create folder with resume name and today's date
        today_date = datetime.now().strftime("%Y-%m-%d")
        resume_name = resume_summary.get("name", "Candidate")
        # Clean name for folder (remove special characters)
        clean_name = resume_name.replace(" ", "_").replace("/", "-").replace("\\", "-")
        cover_letters_folder = f"cover_letters/{clean_name}_{today_date}"
        os.makedirs(cover_letters_folder, exist_ok=True)
        
        for i, job in enumerate(enriched):
            try:
                print(f"  Generating cover letter {i+1}/{len(enriched)}...")
                cover = generate_cover(resume_summary, job, prefer_local_llm=True)
                job["cover_letter"] = cover
                
                # Save as DOCX file in timestamped folder
                try:
                    save_cover_letter_docx(cover, job, resume_summary, output_dir=cover_letters_folder)
                except Exception as docx_error:
                    print(f"  Warning: Failed to save DOCX for {job.get('title', 'Unknown')}: {docx_error}")
                    
            except Exception as e:
                print(f"  Failed to generate cover letter for {job.get('title', 'Unknown')}: {e}")
                job["cover_letter"] = "Failed to generate cover letter."
        
        print(f"  ✓ Cover letters saved to: {cover_letters_folder}")
    else:
        print("[3/6] Skipping cover letter generation (disabled)")

    print("[5/6] Exporting results to CSV")
    df = export_to_csv(enriched, path=output_csv)

    print(f"[6/6] Done. Saved {df.shape[0]} jobs.")
    print(f"\n" + "="*70)
    print(f"✓ CSV saved to: {output_csv}")
    if generate_covers:
        print(f"✓ Cover letters saved to: {cover_letters_folder}")
    print("="*70)
    return df, output_csv

if __name__ == "__main__":
    # Basic run with default resume
    run_pipeline()