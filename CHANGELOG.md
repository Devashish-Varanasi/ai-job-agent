# Changelog

All notable changes to AI Job Agent will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-10

### Added
- 🎉 **Initial Release**
- Resume parsing from PDF, DOCX, and TXT formats
- Automatic job role detection from resume content
- Adzuna API integration for job fetching
- Semantic similarity scoring between resume and jobs
- AI-powered cover letter generation with GPT4All support
- Template-based cover letter fallback
- Professional DOCX cover letter output
- Unique timestamped CSV exports
- Organized output folders by applicant name and date
- Single-command automation (`run_automation.py`)
- Comprehensive test suite
- Resume-focused cover letters (80-90% resume content)

### Features
- **Smart Resume Parser**: Extracts name, email, phone, skills, experience
- **Auto Job Detection**: Analyzes resume to determine target role
- **Job Matching**: Fetches and ranks jobs by relevance
- **Cover Letter Generation**: 
  - Local LLM (GPT4All) support
  - Template-based fallback
  - Resume-centric content
  - Professional DOCX formatting
- **Organized Outputs**:
  - Timestamped CSV files
  - Name and date-based cover letter folders
  - No file overwrites

### Documentation
- Comprehensive README with quick start guide
- GPT4All setup guide
- Automation guide
- Contributing guidelines
- MIT License

### Supported Job Roles
- Data Analyst
- Data Scientist
- Data Engineer
- Software Engineer
- ML Engineer
- Web Developer
- DevOps Engineer

## Roadmap

### [1.1.0] - Planned
- [ ] LinkedIn job integration
- [ ] Indeed job integration
- [ ] Email sending capability
- [ ] Application tracking
- [ ] Custom cover letter templates

### [1.2.0] - Future
- [ ] Web interface
- [ ] Multi-language support
- [ ] Resume builder
- [ ] Interview preparation

---

For detailed changes, see [commit history](https://github.com/yourusername/ai-job-agent/commits/)
