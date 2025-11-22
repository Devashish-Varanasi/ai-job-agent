# Security Policy

## 🛡️ Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it as soon as possible. We take all security issues seriously and will work to address them promptly.

### How to Report

1. **Do not** create a public GitHub issue for the vulnerability
2. Use GitHub Security Advisories or contact the maintainer:
   - Go to https://github.com/Devashish-Varanasi/ai-job-agent/security/advisories/new
   - Or create a private security advisory on GitHub
   - Include:
     - A detailed description of the vulnerability
     - Steps to reproduce the issue
     - Potential impact of the vulnerability
     - Any suggested fixes (if you have them)

### What to Expect

- You will receive a response within 48 hours acknowledging your report
- We will investigate the issue and provide an estimated timeline for a fix
- We will keep you informed of our progress
- Once the issue is resolved, we will publish a security advisory

## 🔒 Security Considerations

### Email Configuration
- Never commit email credentials to the repository
- Use App Passwords for Gmail (not regular passwords)
- Store sensitive configuration in `email_config.py` (not committed to git)

### Web Scraping
- Respect robots.txt and rate limits of job boards
- Use appropriate User-Agent headers
- Handle rate limiting and timeouts gracefully

### Data Privacy
- Resume files are processed locally and never sent to external services
- Job data is fetched directly from job boards
- No personal data is collected or stored by the application

## 📋 Best Practices

### For Users
- Keep your Python environment updated
- Use virtual environments
- Regularly update dependencies
- Never share your `email_config.py` file
- Use strong, unique passwords for email accounts

### For Developers
- Review dependencies for security vulnerabilities
- Follow secure coding practices
- Validate and sanitize all inputs
- Use parameterized queries where applicable
- Keep development tools updated

## 🔄 Updates and Patches

Security updates will be released as patch versions (e.g., 1.0.1). All users are encouraged to update to the latest version to ensure they have the latest security fixes.

## 📞 Contact

For security-related questions or concerns, please use:
- **GitHub Security Advisories**: https://github.com/Devashish-Varanasi/ai-job-agent/security/advisories/new
- **GitHub Issues**: https://github.com/Devashish-Varanasi/ai-job-agent/issues (for non-security issues)

Thank you for helping keep AI Job Agent secure! 🛡️