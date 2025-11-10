# preview_cover_letter.py
# Preview what a generated cover letter looks like

from src.parse_resume import parse_resume
from src.fetch_jobs import fetch_adzuna_jobs
from src.generate_cover import generate_cover
from config import DEFAULT_RESUME

def main():
    print("=" * 70)
    print("PREVIEW: Personalized Cover Letter")
    print("=" * 70)
    
    # Parse resume
    print("\nParsing your resume...")
    resume_summary = parse_resume(DEFAULT_RESUME)
    print(f"Name: {resume_summary.get('name')}")
    print(f"Email: {resume_summary.get('email')}")
    print(f"Phone: {resume_summary.get('phone')}")
    print(f"Skills: {', '.join(resume_summary.get('skills', [])[:5])}")
    
    # Fetch one job
    print("\nFetching a sample job...")
    jobs = fetch_adzuna_jobs("data analyst", location="", page=1)
    job = jobs[0] if jobs else None
    
    if job:
        print(f"\nJob: {job.get('title')} at {job.get('company')}")
        print(f"Location: {job.get('location')}")
        
        # Generate cover letter
        print("\nGenerating personalized cover letter...")
        print("=" * 70)
        cover_letter = generate_cover(resume_summary, job, prefer_local_llm=False)
        print(cover_letter)
        print("=" * 70)
        
        print("\n✓ This cover letter includes:")
        print("  - Your actual name from resume")
        print("  - Your contact information")
        print("  - Your specific skills")
        print("  - Job-specific content")
        print("  - Formal business format")

if __name__ == "__main__":
    main()
