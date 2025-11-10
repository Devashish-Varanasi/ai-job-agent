# demonstrate_cover_letters.py
# Simple demonstration of cover letter generation functionality

from src.parse_resume import parse_resume
from src.generate_cover import generate_cover
from config import DEFAULT_RESUME

def main():
    print("=== AI Job Agent - Cover Letter Generation Demo ===\n")
    
    # Parse the resume
    print("1. Parsing resume...")
    resume_summary = parse_resume(DEFAULT_RESUME)
    print(f"   Parsed resume for: {resume_summary.get('name') or 'Candidate'}")
    print(f"   Skills found: {', '.join(resume_summary.get('skills', [])[:5])}")
    
    # Create sample job listings
    sample_jobs = [
        {
            "title": "Data Scientist",
            "company": "Tech Innovations Inc.",
            "description": "Seeking a Data Scientist with expertise in machine learning, Python, and statistical analysis. Experience with deep learning frameworks like TensorFlow or PyTorch is required."
        },
        {
            "title": "Business Analyst",
            "company": "Global Solutions Ltd.",
            "description": "Looking for a Business Analyst with strong SQL skills and experience in data visualization tools. Must have excellent communication skills and ability to translate data into actionable insights."
        }
    ]
    
    print("\n2. Generating cover letters...")
    for i, job in enumerate(sample_jobs, 1):
        print(f"\n   Job {i}: {job['title']} at {job['company']}")
        cover_letter = generate_cover(resume_summary, job, prefer_local_llm=False)
        print("   Generated cover letter:")
        print("   " + "-" * 50)
        # Print first 300 characters to keep output manageable
        print("   " + cover_letter[:300] + "..." if len(cover_letter) > 300 else cover_letter)
        print("   " + "-" * 50)
    
    print("\n3. Cover letter generation complete!")
    print("   The system can generate cover letters using either:")
    print("   - Template-based approach (shown above)")
    print("   - Local LLM (if configured with GPT4All)")
    print("\n   To use with the full job matching pipeline, ensure all dependencies are properly installed.")

if __name__ == "__main__":
    main()