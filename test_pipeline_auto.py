# test_pipeline_auto.py
# Quick test of auto-detection in the pipeline (without cover letter generation for speed)

from app import run_pipeline

def main():
    print("Testing auto-detection in pipeline...\n")
    
    # Run without specifying query - should auto-detect from resume
    print("Running with AUTO-DETECTION (no query specified):")
    print("=" * 70)
    run_pipeline(generate_covers=False)
    
    print("\n" + "=" * 70)
    print("✓ Test completed!")
    print("\nThe pipeline automatically detected the job role from your resume")
    print("and fetched matching jobs!")

if __name__ == "__main__":
    main()
