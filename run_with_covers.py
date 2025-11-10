# run_with_covers.py
# Script to run the job matching pipeline with cover letter generation

from app import run_pipeline
import sys

def main():
    print(f"Running job matching pipeline with cover letter generation")
    print("-" * 50)
    
    # Check for command line arguments
    query = None
    location = ""
    
    if len(sys.argv) > 1:
        query = sys.argv[1]
        print(f"Using manual query: {query}")
    else:
        print("Auto-detecting job role from resume...")
    
    if len(sys.argv) > 2:
        location = sys.argv[2]
    
    # Run pipeline with cover letter generation enabled
    run_pipeline(query=query, location=location, generate_covers=True)

if __name__ == "__main__":
    main()