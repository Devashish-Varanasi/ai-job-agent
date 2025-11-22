# Data Directory

Place your resume files in this directory.

## Supported Formats

- **PDF** (`.pdf`) - Recommended
- **DOCX** (`.docx`) - Microsoft Word
- **TXT** (`.txt`) - Plain text

## Usage

1. Copy your resume file to this directory
2. Update `DEFAULT_RESUME` in `config.py` to point to your resume file
   ```python
   DEFAULT_RESUME = "data/your_resume.pdf"
   ```

## Multiple Resumes

If you have multiple resumes:
- The system will automatically detect all resume files
- You'll be prompted to select which one to use when running the automation

## Privacy

**Note:** Resume files in this directory are automatically ignored by Git (see `.gitignore`) to protect your privacy.

