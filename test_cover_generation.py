# test_cover_generation.py
# Test script to verify cover letter generation functionality

from src.parse_resume import parse_resume
from src.generate_cover import generate_cover
from config import DEFAULT_RESUME

def test_cover_generation():
    print("Testing cover letter generation...")
    
    # Parse the resume
    print("Parsing resume...")
    resume_summary = parse_resume(DEFAULT_RESUME)
    print(f"Parsed resume for: {resume_summary.get('name', 'Unknown')}")
    print(f"Skills found: {resume_summary.get('skills', [])}")
    
    # Create a mock job
    mock_job = {
        "title": "Data Analyst",
        "company": "Tech Corp",
        "description": "We are looking for a skilled Data Analyst with experience in Python, SQL, and data visualization. The candidate should have experience with statistical analysis and machine learning."
    }
    
    print("\nGenerating cover letter with template...")
    template_cover = generate_cover(resume_summary, mock_job, prefer_local_llm=False)
    print("Template-based cover letter:")
    print("-" * 40)
    print(template_cover)
    print("-" * 40)
    
    print("\nGenerating cover letter with LLM (if available)...")
    llm_cover = generate_cover(resume_summary, mock_job, prefer_local_llm=True)
    print("LLM-based cover letter:")
    print("-" * 40)
    print(llm_cover)
    print("-" * 40)

if __name__ == "__main__":
    test_cover_generation()