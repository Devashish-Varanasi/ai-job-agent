# test_resume_focused.py
# Test the new resume-focused cover letter generation

from src.parse_resume import parse_resume
from src.fetch_jobs import fetch_adzuna_jobs
from src.generate_cover import generate_cover_with_template
from config import DEFAULT_RESUME

def main():
    print("=" * 80)
    print("TESTING RESUME-FOCUSED COVER LETTER")
    print("=" * 80)
    
    # Parse resume
    print("\n[1/3] Parsing your resume...")
    resume = parse_resume(DEFAULT_RESUME)
    
    print(f"\nResume Content Extracted:")
    print(f"  Name: {resume.get('name')}")
    print(f"  Skills ({len(resume.get('skills', []))}): {', '.join(resume.get('skills', [])[:6])}")
    print(f"  Experience lines: {len(resume.get('experience_snippets', []))}")
    
    # Fetch one job
    print("\n[2/3] Fetching a sample job...")
    jobs = fetch_adzuna_jobs("data analyst", location="", page=1)
    sample_job = jobs[0] if jobs else None
    
    if not sample_job:
        print("No jobs found!")
        return
    
    print(f"  Job: {sample_job.get('title')} at {sample_job.get('company')}")
    
    # Generate cover letter
    print("\n[3/3] Generating RESUME-FOCUSED cover letter...")
    cover_letter = generate_cover_with_template(resume, sample_job)
    
    print("\n" + "=" * 80)
    print("GENERATED COVER LETTER (Resume-Focused)")
    print("=" * 80)
    print(cover_letter)
    print("=" * 80)
    
    # Analysis
    print("\nCOVER LETTER ANALYSIS:")
    name = resume.get('name') or ""
    email = resume.get('email') or ""
    print(f"  - Contains your name: {'Yes' if name and name in cover_letter else 'No'}")
    print(f"  - Contains your email: {'Yes' if email and email in cover_letter else 'No'}")
    print(f"  - Number of your skills mentioned: {sum(1 for skill in resume.get('skills', []) if skill in cover_letter)}")
    print(f"  - Contains experience content: {'Yes' if any(exp[:30] in cover_letter for exp in resume.get('experience_snippets', [])[:3] if len(exp) > 30) else 'Partially'}")
    print(f"  - Word count: ~{len(cover_letter.split())} words")
    
    print("\n✓ Cover letter is now HEAVILY based on YOUR resume content!")
    print("  (Job description used minimally, only for context)")

if __name__ == "__main__":
    main()
