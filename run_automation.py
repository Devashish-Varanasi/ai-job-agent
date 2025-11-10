# run_automation.py
# Single command automation script - fetches jobs and generates cover letters

from app import run_pipeline
import sys
from datetime import datetime

def main():
    """
    Automated pipeline that:
    1. Auto-detects job role from your resume
    2. Fetches matching jobs
    3. Generates personalized cover letters
    4. Saves everything with unique timestamped filenames
    """
    
    print("=" * 80)
    print("AI JOB AGENT - AUTOMATED PIPELINE")
    print("=" * 80)
    print(f"Run started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Parse command line arguments
    query = None
    location = ""
    
    if len(sys.argv) > 1:
        query = sys.argv[1]
        print(f"Manual job type: {query}")
    else:
        print("Auto-detecting job role from resume...")
    
    if len(sys.argv) > 2:
        location = sys.argv[2]
        print(f"Location filter: {location}")
    
    print("-" * 80)
    
    try:
        # Run the full pipeline with all features enabled
        df, csv_path = run_pipeline(
            query=query,
            location=location,
            generate_covers=True  # Always generate cover letters
        )
        
        print("\n" + "=" * 80)
        print("AUTOMATION COMPLETED SUCCESSFULLY!")
        print("=" * 80)
        print(f"\nTotal jobs found: {len(df)}")
        print(f"Files generated:")
        print(f"  - CSV with job matches")
        print(f"  - DOCX cover letters for all jobs")
        print(f"\nRun completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n\u2713 All tasks completed! Check the outputs folder for results.")
        
    except Exception as e:
        print("\n" + "=" * 80)
        print("ERROR OCCURRED")
        print("=" * 80)
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
