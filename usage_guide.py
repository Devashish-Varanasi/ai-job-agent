# usage_guide.py
# Guide on how to use the AI Job Agent with cover letter generation

def main():
    print("=== AI Job Agent with Cover Letter Generation - Usage Guide ===\n")
    
    print("SETUP INSTRUCTIONS:")
    print("1. Install dependencies:")
    print("   pip install -r requirements.txt\n")
    
    print("2. Configure API keys in config.py:")
    print("   - Set your Adzuna App ID and Key for job fetching")
    print("   - Optionally configure a local LLM model path for better cover letters\n")
    
    print("3. GPT4ALL Setup (Optional but Recommended):")
    print("   - Download a GPT4All model file (e.g., ggml-gpt4all-j-v1.3-groovy.bin)")
    print("   - Place it in the models/ directory")
    print("   - Update LOCAL_LLM_MODEL_PATH in config.py to match your model filename")
    print("   - See GPT4ALL_SETUP.md for detailed instructions\n")
    
    print("USAGE:")
    print("1. Basic usage (no cover letters):")
    print("   python app.py\n")
    
    print("2. Run with cover letter generation:")
    print("   python run_with_covers.py\n")
    
    print("3. Custom search with cover letters:")
    print("   python run_with_covers.py \"software engineer\" \"New York\"\n")
    
    print("COVER LETTER GENERATION:")
    print("- Template-based (default fallback): Works out of the box")
    print("- Local LLM (enhanced quality): Requires GPT4All model\n")
    
    print("To use local LLM:")
    print("1. Download a GPT4All model (e.g., ggml-gpt4all-j-v1.3-groovy.bin)")
    print("2. Update LOCAL_LLM_MODEL_PATH in config.py to point to your model")
    print("3. Run the pipeline with cover letter generation enabled\n")
    
    print("OUTPUT:")
    print("- Results are saved to outputs/jobs.csv")
    print("- Each job entry includes a generated cover letter")
    print("- Failed cover letter generations are marked with error messages\n")
    
    print("EXTENDING FUNCTIONALITY:")
    print("- Add new cover letter templates in src/generate_cover.py")
    print("- Customize the prompt for LLM-based generation")
    print("- Modify export_results.py to change output format")

if __name__ == "__main__":
    main()