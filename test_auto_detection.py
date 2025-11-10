# test_auto_detection.py
# Test the automatic job role detection from resume

from src.parse_resume import parse_resume
from config import DEFAULT_RESUME

def main():
    print("=" * 70)
    print("AUTO JOB ROLE DETECTION TEST")
    print("=" * 70)
    
    print("\nParsing your resume...")
    resume = parse_resume(DEFAULT_RESUME)
    
    print(f"\nName: {resume.get('name')}")
    print(f"Email: {resume.get('email')}")
    print(f"Phone: {resume.get('phone')}")
    
    print(f"\nSkills Found:")
    for i, skill in enumerate(resume.get('skills', [])[:10], 1):
        print(f"  {i}. {skill}")
    
    print(f"\n{'='*70}")
    print(f"DETECTED JOB ROLE: {resume.get('target_role', 'Unknown').upper()}")
    print(f"{'='*70}")
    
    print(f"\nThis means when you run the pipeline without specifying a query,")
    print(f"it will automatically search for '{resume.get('target_role')}' jobs!")
    
    print(f"\nHow it works:")
    print(f"  - Analyzes your resume content")
    print(f"  - Matches skills to job categories")
    print(f"  - Detects keywords and experience")
    print(f"  - Selects the best matching job role")
    
    print(f"\nSupported job roles:")
    roles = [
        "data analyst", "data scientist", "data engineer",
        "software engineer", "ml engineer", "web developer",
        "devops engineer"
    ]
    for role in roles:
        marker = "✓ DETECTED" if role == resume.get('target_role') else " "
        print(f"  {marker} {role}")
    
    print(f"\nTo run with auto-detection:")
    print(f"  python run_with_covers.py")
    print(f"\nOr override with manual query:")
    print(f"  python run_with_covers.py \"data scientist\"")

if __name__ == "__main__":
    main()
