# run_automation.py
# Fully automated job search with resume analysis and optional company alerts

from app import run_pipeline
import sys
import os
from datetime import datetime
from config import SCRAPE_RESULTS_LIMIT

def load_company_watchlist(file_path="companies.txt"):
    """Load company watchlist from file if exists"""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            companies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return companies
    return []

def get_resume_files(data_dir="data"):
    """Get all resume files from the data directory"""
    resume_extensions = ['.pdf', '.docx', '.txt']
    resume_files = []
    
    if os.path.exists(data_dir):
        for file in os.listdir(data_dir):
            if any(file.lower().endswith(ext) for ext in resume_extensions):
                resume_files.append(file)
    
    return resume_files

def select_resume(resume_files):
    """Prompt user to select a resume when multiple options are available"""
    if len(resume_files) == 0:
        print("❌ No resume files found in the data directory!")
        print("Please add your resume file to the 'data' folder and try again.")
        sys.exit(1)
    elif len(resume_files) == 1:
        # Automatically select the only resume
        selected_resume = resume_files[0]
        print(f"✅ Found one resume: {selected_resume}")
        return f"data/{selected_resume}"
    else:
        # Multiple resumes - prompt user to select
        print(f"📁 Found {len(resume_files)} resume files in the data directory:")
        for i, resume in enumerate(resume_files, 1):
            print(f"  {i}. {resume}")
        
        while True:
            try:
                choice = input(f"\nPlease select a resume (1-{len(resume_files)}): ")
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(resume_files):
                    selected_resume = resume_files[choice_idx]
                    print(f"✅ Selected resume: {selected_resume}")
                    return f"data/{selected_resume}"
                else:
                    print(f"⚠️  Please enter a number between 1 and {len(resume_files)}")
            except ValueError:
                print("⚠️  Please enter a valid number")

def main():
    """
    Fully Automated Pipeline:
    1. Auto-detects job role from resume (NO manual input required)
    2. Scrapes all relevant jobs using BeautifulSoup
    3. Checks for company watchlist (companies.txt) for email alerts
    4. Generates CSV with all job matches
    5. Creates personalized cover letters for all jobs using GPT4All
    """
    
    print("=" * 80)
    print("AI JOB AGENT - FULLY AUTOMATED PIPELINE")
    print("=" * 80)
    print(f"Run started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Configured to fetch up to {SCRAPE_RESULTS_LIMIT} jobs")
    print()
    
    # Check for resume files and select one
    resume_files = get_resume_files("data")
    selected_resume_path = select_resume(resume_files)
    
    print(f"\n🤖 Automatic Mode: Analyzing resume and fetching all matching jobs...")
    print()
    
    # Load company watchlist if exists
    watchlist = load_company_watchlist()
    if watchlist:
        print(f"📋 Company Watchlist Loaded: {len(watchlist)} companies")
        for company in watchlist:
            print(f"   - {company}")
        print()
    
    # Always auto-detect from resume (no manual input)
    query = None
    location = ""
    
    print("🔍 Auto-detecting job role from resume...")
    print("-" * 80)
    
    try:
        # Run the full pipeline with all features enabled
        df, csv_path = run_pipeline(
            resume_path=selected_resume_path,
            query=query,
            location=location,
            generate_covers=True,  # Always generate cover letters using GPT4All
            company_watchlist=watchlist
        )
        
        print("\n" + "=" * 80)
        print("AUTOMATION COMPLETED SUCCESSFULLY!")
        print("=" * 80)
        print(f"\n📊 Total jobs found and processed: {len(df)}")
        print(f"📁 Files generated:")
        print(f"   ✓ CSV with all job matches: {csv_path}")
        print(f"   ✓ DOCX cover letters for all jobs (using GPT4All)")
        
        # Show watchlist matches if any
        if watchlist:
            # Fuzzy matching: check if any watchlist company name is contained in job company name or vice versa
            watchlist_matches = df[df['company'].apply(
                lambda job_company: any(
                    watchlist_name.lower() in str(job_company).lower() or 
                    str(job_company).lower() in watchlist_name.lower()
                    for watchlist_name in watchlist
                )
            )]
            if len(watchlist_matches) > 0:
                print(f"\n🎯 WATCHLIST MATCHES FOUND: {len(watchlist_matches)}")
                for idx, row in watchlist_matches.iterrows():
                    print(f"   ⚡ {row['company']} - {row['title']}")
                print(f"\n   📧 Email alerts will be sent for these matches!")
            else:
                print(f"\n   No watchlist companies found in current results.")
        
        print(f"\n⏰ Run completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n✅ All tasks completed! Check the outputs folder for results.")
        
    except Exception as e:
        print("\n" + "=" * 80)
        print("❌ ERROR OCCURRED")
        print("=" * 80)
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    print("\n💡 TIP: Create 'companies.txt' in the project root to monitor specific companies!")
    print("   Example companies.txt:")
    print("   # One company per line")
    print("   Google")
    print("   Microsoft")
    print("   Amazon\n")
    main()