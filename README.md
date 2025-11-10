# 🤖 AI Job Agent - Automated Job Matching & Cover Letter Generator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent automation system that streamlines your job search by parsing your resume, finding relevant job listings, computing similarity scores, and generating personalized, professional cover letters—all with a single command.

## ✨ Features

- 📄 **Smart Resume Parsing** - Extracts name, contact info, skills, and experience from PDF, DOCX, or TXT
- 🎯 **Auto Job Role Detection** - Automatically identifies target job roles from your resume
- 🔍 **Job Fetching** - Integrates with Adzuna API to fetch relevant job listings
- 📊 **Similarity Scoring** - Ranks jobs by relevance using semantic text analysis
- ✍️ **AI-Powered Cover Letters** - Generates resume-focused cover letters (80-90% from YOUR resume)
- 📁 **Organized Outputs** - Unique timestamped CSVs and professionally formatted DOCX cover letters
- ⚡ **One-Command Automation** - Complete workflow in a single command

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Devashish-Varanasi/ai-job-agent.git
   cd ai-job-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   
   Edit `config.py` and add your Adzuna API credentials:
   ```python
   ADZUNA_APP_ID = "your_app_id_here"
   ADZUNA_APP_KEY = "your_app_key_here"
   ```
   
   Get free API keys at: https://developer.adzuna.com/

4. **Add your resume**
   
   Place your resume (PDF/DOCX/TXT) in the `data/` folder and update `config.py`:
   ```python
   DEFAULT_RESUME = "data/your_resume.pdf"
   ```

### Basic Usage

**Run the complete automation pipeline:**
```bash
python run_automation.py
```

That's it! The system will:
1. Parse your resume
2. Auto-detect your target job role
3. Fetch matching jobs
4. Generate personalized cover letters
5. Save everything in organized folders

**Manual job type selection:**
```bash
python run_automation.py "data scientist"
python run_automation.py "software engineer" "Bangalore"
```

## 📂 Output Structure

```
outputs/
└── jobs_data_analyst_20251110_143025.csv    # Timestamped CSV with job matches

cover_letters/
└── John_Doe_2025-11-10/           # Folder named with your name + date
    ├── CoverLetter_Google_Data_Analyst_123456.docx
    ├── CoverLetter_Microsoft_ML_Engineer_789012.docx
    └── ... (one DOCX per job)
```

### Output Details

**CSV File** (`outputs/jobs_<job_type>_<timestamp>.csv`):
- Job ID, Title, Company, Location
- Similarity Score (relevance to your resume)
- Application Link
- Generated Cover Letter Text

**Cover Letter Folder** (`cover_letters/<YourName>_<YYYY-MM-DD>/`):
- Professional DOCX files for each job
- Times New Roman, 12pt font
- Formal business letter format
- Includes YOUR actual name, email, phone
- Resume-focused content (80-90% from your resume)

## 🎯 Key Advantages

### Resume-Focused Cover Letters
Unlike generic templates, our cover letters:
- ✅ Showcase **YOUR** skills and experience (8-10 skills mentioned)
- ✅ Use **YOUR** actual achievements and background
- ✅ Include **YOUR** real name and contact information
- ✅ Minimize job description references (only 10-20%)
- ✅ No manual editing required—ready to send!

### Intelligent Automation
- **Auto-detection**: Analyzes your resume to identify the best job role
- **Unique filenames**: Never overwrites previous runs
- **Organized by date**: Easy to track applications over time
- **Professional formatting**: Industry-standard DOCX format

## 🛠️ Advanced Configuration

### GPT4All Local LLM (Optional)

For enhanced cover letter quality using a local AI model:

**⚠️ Note**: GPT4All and model files are NOT included in this repository due to their large size. You need to download them separately.

#### Option 1: Download GPT4All Desktop App (Recommended - Easiest)

1. **Download GPT4All**: Visit https://gpt4all.io/ and download the desktop application for your OS
2. **Install and Open** the GPT4All application
3. **Download a Model**: 
   - Open GPT4All → Click "Models" tab
   - Download **"Orca Mini 3B"** (recommended for 8GB RAM systems) or **"Mistral 7B"** (for 16GB+ RAM)
   - Models are saved to:
     - Windows: `C:\Users\<YourName>\AppData\Local\nomic.ai\GPT4All\`
     - macOS: `~/Library/Application Support/nomic.ai/GPT4All/`
     - Linux: `~/.local/share/nomic.ai/GPT4All/`

4. **Update config.py**:
   ```python
   # Windows example
   LOCAL_LLM_MODEL_PATH = r"C:\Users\YourName\AppData\Local\nomic.ai\GPT4All\orca-mini-3b-gguf2-q4_0.gguf"
   
   # macOS/Linux example
   LOCAL_LLM_MODEL_PATH = "/Users/yourname/Library/Application Support/nomic.ai/GPT4All/orca-mini-3b-gguf2-q4_0.gguf"
   ```

#### Option 2: Direct Model Download (Advanced)

1. Visit https://gpt4all.io/models/
2. Download a model file (e.g., `orca-mini-3b-gguf2-q4_0.gguf`)
3. Place it anywhere on your computer
4. Update `LOCAL_LLM_MODEL_PATH` in `config.py` with the full path

**Recommended Models by RAM:**
- **4-8 GB RAM**: `orca-mini-3b-gguf2-q4_0.gguf` (~1.8GB)
- **8-16 GB RAM**: `mistral-7b-openorca.gguf2.Q4_0.gguf` (~4GB)
- **16+ GB RAM**: `mistral-7b-instruct-v0.1.Q4_0.gguf` (~4.1GB)

#### Why Not Include Models in the Repo?

- Model files are 1.8GB - 4GB each
- GitHub has a 100MB file size limit
- Users can choose models based on their RAM
- Keeps the repository lightweight and fast to clone

**Note**: The template-based cover letter generation works excellently without LLM setup - GPT4All is completely optional!

See [GPT4ALL_SETUP.md](GPT4ALL_SETUP.md) for detailed instructions.

## 📚 Project Structure

```
ai-job-agent/
├── src/
│   ├── parse_resume.py      # Resume parsing and job role detection
│   ├── fetch_jobs.py         # Adzuna API integration
│   ├── match_jobs.py         # Similarity scoring
│   ├── generate_cover.py     # Cover letter generation
│   ├── export_results.py     # CSV export
│   └── utils.py              # Helper functions
├── data/
│   └── your_resume.pdf       # Place your resume here
├── outputs/                  # Generated CSV files
├── cover_letters/            # Generated DOCX cover letters
├── models/                   # Optional: GPT4All models
├── app.py                    # Main pipeline orchestrator
├── run_automation.py         # Single-command automation
├── config.py                 # Configuration settings
└── requirements.txt          # Python dependencies
```

## 🧪 Testing

Verify your setup:

```bash
# Test auto-detection
python test_auto_detection.py

# Preview a cover letter
python preview_cover_letter.py

# Generate sample cover letters (3 jobs)
python generate_sample_covers.py

# Full system verification
python final_test_results.py
```

## 📋 Requirements

- Python 3.8+
- PyMuPDF (fitz) - PDF parsing
- python-docx - DOCX generation
- requests - API calls
- pandas - Data handling
- sentence-transformers - Similarity scoring
- gpt4all (optional) - Local LLM

All dependencies listed in `requirements.txt`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Adzuna API for job listings
- GPT4All for local LLM capabilities
- Sentence Transformers for semantic similarity

## 📞 Support

If you encounter issues:
1. Check the [GPT4ALL_SETUP.md](GPT4ALL_SETUP.md) guide
2. Review [AUTOMATION_GUIDE.txt](AUTOMATION_GUIDE.txt)
3. Open an issue on GitHub

## 🎓 Use Cases

- **Job Seekers**: Automate cover letter writing and job discovery
- **Career Coaches**: Generate customized applications for clients
- **Recruiters**: Quick candidate-job matching
- **Students**: Streamline internship/job applications

---

**Made with ❤️ to help you land your dream job faster!**