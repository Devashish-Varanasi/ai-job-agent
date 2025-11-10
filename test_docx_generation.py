# test_docx_generation.py
# Test script to verify DOCX cover letter generation

from src.parse_resume import parse_resume
from src.generate_cover import generate_cover, save_cover_letter_docx
from config import DEFAULT_RESUME

def test_docx_generation():
    print("Testing DOCX cover letter generation...\n")
    
    # Parse the resume
    print("1. Parsing resume...")
    resume_summary = parse_resume(DEFAULT_RESUME)
    print(f"   Parsed resume for: {resume_summary.get('name', 'Unknown')}")
    
    # Create a mock job
    mock_job = {
        "id": "test123",
        "title": "Senior Data Analyst",
        "company": "Tech Solutions Inc",
        "description": "We are seeking an experienced Data Analyst with expertise in Python, SQL, and data visualization tools."
    }
    
    print("\n2. Generating cover letter...")
    cover_letter = generate_cover(resume_summary, mock_job, prefer_local_llm=False)
    print("   Cover letter generated successfully")
    
    print("\n3. Saving as DOCX file...")
    filepath = save_cover_letter_docx(cover_letter, mock_job, resume_summary)
    print(f"   Saved to: {filepath}")
    
    print("\n✓ Test completed successfully!")
    print(f"Check the 'cover_letters' folder for the generated DOCX file.")

if __name__ == "__main__":
    test_docx_generation()
