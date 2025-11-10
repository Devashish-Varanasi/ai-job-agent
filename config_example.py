# config_example.py
# Example configuration file - Copy this to config.py and fill in your details
# 
# Quick Setup:
# 1. Copy this file: cp config_example.py config.py
# 2. Get Adzuna API keys: https://developer.adzuna.com/
# 3. Update ADZUNA_APP_ID and ADZUNA_APP_KEY
# 4. Add your resume to data/ folder
# 5. Update DEFAULT_RESUME path

# ============================================================================
# ADZUNA API CONFIGURATION (REQUIRED)
# ============================================================================
ADZUNA_APP_ID = "your_app_id_here"
ADZUNA_APP_KEY = "your_app_key_here"
ADZUNA_COUNTRY = "us"  # 'us', 'gb', 'in', 'ca', 'au', etc.

# ============================================================================
# SEARCH SETTINGS
# ============================================================================
ADZUNA_RESULTS_PER_PAGE = 20

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
