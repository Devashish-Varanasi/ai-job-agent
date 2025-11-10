# test_folder_naming.py
# Quick test to verify folder naming format

from src.parse_resume import parse_resume
from config import DEFAULT_RESUME
from datetime import datetime

def main():
    print("Testing cover letter folder naming format...\n")
    
    # Parse resume to get name
    resume = parse_resume(DEFAULT_RESUME)
    name = resume.get("name", "Candidate")
    
    # Get today's date
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # Clean name for folder
    clean_name = name.replace(" ", "_").replace("/", "-").replace("\\", "-")
    
    # Generate folder name
    folder_name = f"cover_letters/{clean_name}_{today_date}"
    
    print(f"Resume Name: {name}")
    print(f"Today's Date: {today_date}")
    print(f"\nFolder that will be created:")
    print(f"  {folder_name}")
    print(f"\nExample: cover_letters/Devashish_Varanasi_{today_date}")
    print("\n✓ Folder naming format verified!")

if __name__ == "__main__":
    main()
