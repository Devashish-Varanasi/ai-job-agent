# quick_test_automation.py
# Quick test with just 3 jobs to verify folder naming

from app import run_pipeline

def main():
    print("Quick test - generating 3 cover letters with new folder naming...\n")
    
    # This will create folder: cover_letters/Devashish_Varanasi_2025-11-10
    df, csv_path = run_pipeline(generate_covers=True)
    
    print("\n✓ Test completed!")
    print(f"Check the cover_letters folder - it should be named with your name and today's date")

if __name__ == "__main__":
    main()
