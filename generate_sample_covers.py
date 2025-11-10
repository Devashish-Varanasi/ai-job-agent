# generate_sample_covers.py
# Quick script to generate a few sample DOCX cover letters

from src.parse_resume import parse_resume
from src.fetch_jobs import fetch_adzuna_jobs
from src.generate_cover import generate_cover, save_cover_letter_docx
from config import DEFAULT_RESUME
import os

def main():
    print("Generating sample cover letters in DOCX format...\n")
    
    # Parse resume
    print("1. Parsing resume...")
    resume_summary = parse_resume(DEFAULT_RESUME)
    print(f"   Found {len(resume_summary.get('skills', []))} skills\n")
    
    # Fetch a few jobs
    print("2. Fetching jobs...")
    jobs = fetch_adzuna_jobs("data analyst", location="", page=1)
    print(f"   Fetched {len(jobs)} jobs\n")
    
    # Generate cover letters for first 3 jobs
    print("3. Generating DOCX cover letters for top 3 jobs...")
    for i, job in enumerate(jobs[:3]):
        print(f"\n   Job {i+1}: {job.get('title')} at {job.get('company')}")
        
        # Generate cover letter text (using template for speed)
        cover_text = generate_cover(resume_summary, job, prefer_local_llm=False)
        
        # Save as DOCX
        filepath = save_cover_letter_docx(cover_text, job, resume_summary)
        print(f"   ✓ Saved: {os.path.basename(filepath)}")
    
    print("\n✓ Done! Check the 'cover_letters' folder for the generated files.")

if __name__ == "__main__":
    main()
