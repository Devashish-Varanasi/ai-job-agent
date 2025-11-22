# AI Job Agent 🤖

An intelligent job search automation tool that helps you find relevant job opportunities and generate personalized cover letters based on your resume. This tool automates the tedious parts of job searching by scraping job listings, matching them to your skills, and creating tailored cover letters.

## ✨ Features

- **📄 Smart Resume Parsing**: Automatically extracts skills, experience, education, and contact information from your resume (supports PDF, DOCX, and TXT formats)
- **🔍 Automated Job Scraping**: Fetches job listings from popular job boards using web scraping
- **🎯 AI-Powered Job Matching**: Ranks jobs by relevance to your resume using semantic similarity scoring (Sentence Transformers)
- **✍️ Personalized Cover Letter Generation**: Creates unique, personalized cover letters for each job (80-90% based on your resume, 10-20% job-specific)
- **🏢 Company Watchlist**: Monitors specific companies and sends email alerts when they post matching jobs
- **📊 Professional Output**: Generates CSV files with job details and professionally formatted DOCX cover letters
- **🎨 Multiple Resume Support**: Automatically detects and lets you choose if multiple resumes exist in the data folder

## 🛠️ Technology Stack

- **Python 3.8+**: Core programming language
- **BeautifulSoup4**: Web scraping for job listings
- **Sentence Transformers**: Semantic similarity scoring using AI embeddings
- **PyMuPDF (fitz)**: PDF parsing and text extraction
- **python-docx**: Professional DOCX cover letter generation
- **pandas**: Data manipulation and CSV export
- **GPT4All (Optional)**: Local LLM for enhanced cover letter generation

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for web scraping and downloading models)

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Devashish-Varanasi/ai-job-agent.git
cd ai-job-agent
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Configuration

1. **Copy the configuration template:**
   ```bash
   cp config_example.py config.py
   ```

2. **Update `config.py` with your settings:**
   ```python
   DEFAULT_RESUME = "data/your_resume.pdf"  # Update with your resume filename
   SCRAPE_RESULTS_LIMIT = 20  # Number of jobs to fetch
   ```

3. **Place your resume in the `data/` folder:**
   - Supported formats: PDF, DOCX, TXT
   - Name it according to what you set in `config.py`

### Step 5: (Optional) Set Up Email Alerts

1. **Copy the email configuration template:**
   ```bash
   cp email_config_example.py email_config.py
   ```

2. **For Gmail users:**
   - Enable 2-factor authentication in your Google Account
   - Generate an App Password at: https://myaccount.google.com/apppasswords
   - Update `email_config.py` with your email and app password (NOT your regular password)

3. **For other email providers:**
   - Update SMTP settings in `email_config.py`
   - See comments in the file for provider-specific settings

### Step 6: (Optional) Install GPT4All Model

For enhanced cover letter generation using local LLM:

1. Download the model file from [GPT4All](https://gpt4all.io/index.html)
2. Place it in the `models/` folder
3. Update `LOCAL_LLM_MODEL_PATH` in `config.py` to point to the model file

**Note:** If no model is found, the system will automatically use a template-based approach that still produces excellent, personalized cover letters.

## 📖 Usage

### Basic Usage

Simply run the automation script:

```bash
python run_automation.py
```

The script will:
1. ✅ Automatically detect and parse your resume
2. ✅ Auto-detect your target job role from resume content
3. ✅ Scrape relevant job listings
4. ✅ Match jobs to your resume using AI
5. ✅ Generate personalized cover letters for each job
6. ✅ Save results to CSV and DOCX files

### With Company Watchlist

1. Create `companies.txt` in the project root:
   ```
   Google
   Microsoft
   Amazon
   Apple
   ```

2. Run the automation:
   ```bash
   python run_automation.py
   ```

3. If any jobs match your watchlist companies, you'll receive email alerts (if configured).

### Multiple Resumes

If you have multiple resumes in the `data/` folder, the system will prompt you to select one:

```
📁 Found 3 resume files in the data directory:
  1. resume_dev.pdf
  2. resume_data_analyst.pdf
  3. resume_engineer.pdf

Please select a resume (1-3): 
```

### Custom Job Search

You can also run the automation with specific parameters (though auto-detection is recommended):

```bash
python app.py
```

Then modify the `run_pipeline()` call in `app.py` with your parameters.

## 📁 Project Structure

```
ai-job-agent/
├── src/                          # Source code modules
│   ├── parse_resume.py          # Resume parsing and role detection
│   ├── fetch_jobs.py            # Web scraping job listings
│   ├── match_jobs.py            # Semantic similarity scoring
│   ├── generate_cover.py        # Cover letter generation (LLM + template)
│   ├── export_results.py        # CSV export functionality
│   └── utils.py                 # Utility functions
├── app.py                       # Main pipeline orchestration
├── run_automation.py            # Entry point script (recommended)
├── config_example.py            # Configuration template
├── config.py                    # Your configuration (not in git)
├── email_config_example.py      # Email configuration template
├── email_config.py              # Your email config (not in git)
├── companies_example.txt        # Company watchlist template
├── companies.txt                # Your watchlist (not in git)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── CHANGELOG.md                 # Version history
├── CONTRIBUTING.md              # Contribution guidelines
├── SECURITY.md                  # Security policy
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore patterns
├── data/                        # Your resume files (not in git)
│   ├── .gitkeep
│   └── README.md
├── outputs/                     # Generated CSV files (not in git)
│   └── .gitkeep
├── cover_letters/               # Generated cover letters (not in git)
│   └── .gitkeep
└── models/                      # GPT4All models (not in git)
    └── .gitkeep
```

## 🎯 How It Works

1. **Resume Analysis** 📄
   - Parses your resume (PDF/DOCX/TXT)
   - Extracts: name, email, phone, skills, experience, education
   - Automatically detects your target job role based on content

2. **Job Scraping** 🔍
   - Scrapes job listings from job boards
   - Extracts: title, company, location, description, URL
   - Handles errors gracefully with fallback options

3. **Semantic Matching** 🎯
   - Uses Sentence Transformers to create embeddings
   - Computes cosine similarity between resume and job descriptions
   - Ranks jobs by relevance score

4. **Cover Letter Generation** ✍️
   - Creates personalized cover letters for each job
   - Uses exact details from your resume (name, skills, experience)
   - Personalizes for each specific company
   - Format: Professional DOCX files with proper formatting

5. **Company Monitoring** 🏢
   - Checks jobs against your watchlist
   - Sends email alerts for matches (if configured)
   - Uses fuzzy matching for company names

6. **Output Generation** 📊
   - Saves job listings to timestamped CSV files
   - Saves cover letters to organized folders (by date and name)
   - All files are professionally formatted and ready to use

## ⚙️ Configuration

### Main Configuration (`config.py`)

```python
# Resume path (required)
DEFAULT_RESUME = "data/your_resume.pdf"

# Web scraping settings
USER_AGENT = "Mozilla/5.0..."  # Browser user agent
SCRAPE_RESULTS_LIMIT = 20       # Number of jobs to fetch

# Local LLM (optional)
LOCAL_LLM_MODEL_PATH = "models/orca-mini-3b-gguf2-q4_0.gguf"

# Output directories
OUTPUT_CSV = "outputs/jobs.csv"
COVER_LETTERS_DIR = "cover_letters"
```

### Email Configuration (`email_config.py`)

```python
EMAIL_ENABLED = True
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Gmail App Password
RECIPIENT_EMAIL = "your_email@gmail.com"
```

**⚠️ Security Note:** Never commit `config.py` or `email_config.py` to git. They contain sensitive information and are already in `.gitignore`.

## 📝 Output Files

### CSV File (`outputs/jobs_[role]_[timestamp].csv`)

Contains:
- Job ID
- Title
- Company
- Location
- Similarity Score (0-1)
- Job URL
- Cover Letter Text

### Cover Letters (`cover_letters/[Name]_[Date]/`)

Each cover letter is saved as:
- `CoverLetter_[Company]_[Title]_[ID].docx`

Features:
- Professional formatting
- Your exact contact information from resume
- Company-specific personalization
- Ready to submit

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Security

- **Never commit sensitive files**: `config.py`, `email_config.py`, `companies.txt`, and resume files are already in `.gitignore`
- **Use App Passwords**: For Gmail, always use App Passwords, never your regular password
- **Keep credentials secure**: Store credentials only in local config files, never in version control

See [SECURITY.md](SECURITY.md) for more security information.

## 🐛 Troubleshooting

### Issue: Resume not found
**Solution:** Ensure your resume file is in the `data/` folder and the filename matches what's in `config.py`

### Issue: No jobs found
**Solution:** Check your internet connection. The scraper may need adjustments if job board structure changes.

### Issue: Email alerts not working
**Solution:** 
- Verify `email_config.py` is set up correctly
- For Gmail, ensure you're using an App Password, not your regular password
- Check that `EMAIL_ENABLED = True`

### Issue: Cover letters look wrong
**Solution:** Ensure your resume has a name, skills, and experience sections that can be parsed.

### Issue: Module not found errors
**Solution:** Make sure you've activated your virtual environment and installed all dependencies:
```bash
pip install -r requirements.txt
```

## 💡 Tips

- **Resume Format**: Ensure your resume has clear sections (Experience, Education, Skills) for best parsing results
- **Company Watchlist**: Use partial company names for better matching (e.g., "Tech" matches "Tech Innovations Inc.")
- **Cover Letters**: Review generated cover letters before sending - they're personalized but should be reviewed
- **Multiple Runs**: Each run creates new files with timestamps, so previous results are preserved
- **Local LLM**: For better cover letter quality, consider using GPT4All with a local model

## 📞 Support

- **Issues**: Open an issue on GitHub for bugs or feature requests
- **Questions**: Check existing issues or open a new one for questions
- **Contributions**: See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines

## 🙏 Acknowledgments

- **BeautifulSoup4**: For web scraping capabilities
- **Sentence Transformers**: For semantic similarity matching
- **PyMuPDF**: For PDF parsing
- **python-docx**: For DOCX generation
- **GPT4All**: For optional local LLM support

---

**Made with ❤️ for job seekers everywhere**

*Happy job hunting! 🚀*
