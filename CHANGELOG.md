# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Personalized Cover Letters**: Each cover letter is now uniquely personalized for the specific company while strictly using exact resume details
- **Multiple Resume Support**: Automatic detection and selection when multiple resumes exist in the data folder
- **Exact Resume Details**: Cover letters now use exact name, email, phone, skills, and experience from parsed resume (no placeholders)
- Company watchlist feature with fuzzy matching
- Email alert system for watchlist companies
- Comprehensive README documentation with detailed setup instructions
- CHANGELOG file for tracking changes
- `.gitkeep` files for empty directories (data, outputs, cover_letters, models)
- Directory README files for better user guidance

### Changed
- **Cover Letter Formatting**: Fixed alignment issues in header (email/phone on separate lines) and signature (name stays together)
- **Template Generation**: Enhanced to use exact resume data with company-specific personalization
- **LLM Prompts**: Updated to emphasize using only exact resume information
- Replaced Adzuna API with BeautifulSoup web scraping
- Renamed `fetch_adzuna_jobs` function to `fetch_jobs`
- Updated configuration files to remove Adzuna API references
- Improved company matching with partial name support
- Enhanced error handling and user feedback
- Updated `.gitignore` to protect sensitive files (config.py, email_config.py, companies.txt, resume files)

### Removed
- All Adzuna API dependencies and references
- Unnecessary test and debug files (`check_cover.py`, `test_resume.py`)
- Real credentials from example configuration files
- Redundant documentation files

## [1.0.0] - 2025-11-21

### Added
- Initial release of AI Job Agent
- Resume parsing with automatic role detection
- Web scraping job fetching (BeautifulSoup)
- Semantic similarity matching
- Cover letter generation
- CSV export functionality
- Basic email notification system

### Changed
- Complete refactor from API-based to web scraping approach
- Improved code organization and modularity
- Enhanced documentation and user guidance

[Unreleased]: https://github.com/Devashish-Varanasi/ai-job-agent/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Devashish-Varanasi/ai-job-agent/releases/tag/v1.0.0