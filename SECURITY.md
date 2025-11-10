# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

1. **Do NOT** open a public issue
2. Email the maintainers directly with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will acknowledge your email within 48 hours and provide a detailed response within 7 days.

## Security Best Practices

### API Keys
- **Never commit** `config.py` with real API keys to GitHub
- Use `config_example.py` as a template
- Add `config.py` to `.gitignore` (already done)
- Consider using environment variables for production:
  ```python
  import os
  ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID', 'default_value')
  ```

### Resume Data
- Keep resume files in `data/` directory (excluded from git)
- Never commit personal resume information
- Clear `outputs/` and `cover_letters/` before committing

### Dependencies
- Regularly update dependencies: `pip install --upgrade -r requirements.txt`
- Review dependencies for known vulnerabilities
- Use virtual environments to isolate dependencies

### GPT4All Models
- Download models only from official sources (https://gpt4all.io/)
- Verify file integrity if possible
- Models are excluded from git (large files)

## Known Security Considerations

1. **API Keys in config.py**: Template includes placeholders. Users must add their own keys.
2. **Local File Access**: The app reads local resume files - ensure proper file permissions.
3. **Network Requests**: App makes API calls to Adzuna - ensure network security.
4. **LLM Privacy**: GPT4All runs locally - no data sent to external servers.

## Updates

Security updates will be released as patch versions (1.0.x). Please keep your installation up to date.
