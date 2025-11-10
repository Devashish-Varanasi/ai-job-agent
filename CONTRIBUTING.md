# Contributing to AI Job Agent

First off, thank you for considering contributing to AI Job Agent! It's people like you that make this tool better for everyone.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Python version and OS**
- **Error messages or logs**

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Use case**: Why is this enhancement useful?
- **Detailed description**: What should happen?
- **Examples**: Show how it would work
- **Alternatives considered**

### Pull Requests

1. **Fork the repository**
2. **Create a branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit**: `git commit -m 'Add amazing feature'`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/ai-job-agent.git
cd ai-job-agent

# Install dependencies
pip install -r requirements.txt

# Run tests
python final_test_results.py
```

## Coding Guidelines

### Python Style
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### Testing
- Test your changes before submitting
- Add test cases for new features
- Ensure existing tests pass

### Documentation
- Update README.md if adding features
- Add comments for complex logic
- Update docstrings

## Project Structure

```
src/
├── parse_resume.py      # Resume parsing
├── fetch_jobs.py        # Job API integration
├── match_jobs.py        # Similarity scoring
├── generate_cover.py    # Cover letter generation
└── export_results.py    # Output handling
```

## Areas for Contribution

### High Priority
- [ ] Additional job board integrations (Indeed, LinkedIn)
- [ ] Support for more resume formats
- [ ] Multi-language support
- [ ] Web interface

### Medium Priority
- [ ] Improved job matching algorithms
- [ ] Custom cover letter templates
- [ ] Email integration
- [ ] Application tracking

### Good First Issues
- [ ] Documentation improvements
- [ ] Test coverage expansion
- [ ] Error message enhancements
- [ ] Code refactoring

## Questions?

Feel free to open an issue with the `question` label if you need help!

---

**Thank you for contributing!** 🎉
