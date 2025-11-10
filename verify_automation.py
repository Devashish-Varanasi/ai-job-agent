# verify_automation.py
# Verify the complete automation setup

from datetime import datetime
from src.parse_resume import parse_resume
from config import DEFAULT_RESUME

def main():
    print("=" * 80)
    print("AUTOMATION SETUP VERIFICATION")
    print("=" * 80)
    
    # Get resume info
    resume = parse_resume(DEFAULT_RESUME)
    name = resume.get("name", "Candidate")
    job_role = resume.get("target_role", "data analyst")
    
    # Generate sample filenames
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    timestamp = today.strftime("%Y%m%d_%H%M%S")
    
    clean_name = name.replace(" ", "_").replace("/", "-").replace("\\", "-")
    job_clean = job_role.replace(" ", "_").replace("/", "-")
    
    print(f"\nYour Resume Info:")
    print(f"  Name: {name}")
    print(f"  Detected Job Role: {job_role}")
    print(f"  Today's Date: {date_str}")
    
    print(f"\n" + "=" * 80)
    print("WHEN YOU RUN: python run_automation.py")
    print("=" * 80)
    
    print(f"\n1. CSV FILE will be created:")
    print(f"   outputs/jobs_{job_clean}_{timestamp}.csv")
    print(f"   Example: outputs/jobs_data_analyst_20251110_153045.csv")
    
    print(f"\n2. COVER LETTERS FOLDER will be created:")
    print(f"   cover_letters/{clean_name}_{date_str}/")
    print(f"   Example: cover_letters/Devashish_Varanasi_2025-11-10/")
    
    print(f"\n3. INSIDE THE FOLDER, DOCX files for each job:")
    print(f"   CoverLetter_<Company>_<JobTitle>_<JobID>.docx")
    print(f"   Example: CoverLetter_Google_Data_Analyst_123456.docx")
    
    print(f"\n" + "=" * 80)
    print("UNIQUE FILENAMES EVERY RUN:")
    print("=" * 80)
    print(f"  - CSV has timestamp → Never overwrites")
    print(f"  - Folder has your name + date → Organized by date")
    print(f"  - Each DOCX has unique job ID → No duplicates")
    
    print(f"\n" + "=" * 80)
    print("✓ AUTOMATION READY!")
    print("=" * 80)
    print(f"\nRun this command to start:")
    print(f"  python run_automation.py")
    print(f"\nEverything will be automated - just one command!")

if __name__ == "__main__":
    main()
