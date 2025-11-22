# config_example.py
# Example configuration file - Copy this to config.py and fill in your details
# 
# Quick Setup:
# 1. Copy this file: cp config_example.py config.py
# 2. Add your resume to data/ folder
# 3. Update DEFAULT_RESUME path

# ============================================================================
# WEB SCRAPING SETTINGS
# ============================================================================
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

# ============================================================================
# SEARCH SETTINGS
# ============================================================================
SCRAPE_RESULTS_LIMIT = 20

# ============================================================================
# LOCAL LLM CONFIGURATION (OPTIONAL)
# ============================================================================
# Leave as-is to use template mode, or set path to GPT4All model
LOCAL_LLM_MODEL_PATH = "models/orca-mini-3b-gguf2-q4_0.gguf"

# ============================================================================
# OUTPUT DIRECTORIES
# ============================================================================
OUTPUT_CSV = "outputs/jobs.csv"
COVER_LETTERS_DIR = "cover_letters"

# ============================================================================
# RESUME PATH (REQUIRED)
# ============================================================================
DEFAULT_RESUME = "data/your_resume.pdf"
