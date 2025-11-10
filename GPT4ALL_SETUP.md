# GPT4ALL Setup Guide (Optional)

> **Note**: The template-based cover letter generation works excellently without GPT4All. This guide is for users who want to experiment with local LLM-powered cover letters.

## Prerequisites
- Python 3.8 or higher
- pip package manager
- At least 4GB free RAM (8GB+ recommended)
- Windows, macOS, or Linux

## What is GPT4All?

GPT4All is a local language model that runs on your computer without requiring internet or API calls. It can enhance cover letter generation with more natural, personalized language.

## Installation Steps

### 1. Install Python Dependencies

The `gpt4all` package is already in `requirements.txt`, so if you've installed dependencies, you're set:
```bash
pip install -r requirements.txt
```

### 2. Download a GPT4ALL Model

**Option A: Download via GPT4All App (Easiest)**
1. Download and install [GPT4All Desktop App](https://gpt4all.io/)
2. Open the app and go to "Models"
3. Download a model (recommended: **Orca Mini 3B** for 8GB RAM systems)
4. Models are auto-saved to:
   - Windows: `C:\Users\<YourName>\AppData\Local\nomic.ai\GPT4All\`
   - macOS: `~/Library/Application Support/nomic.ai/GPT4All/`
   - Linux: `~/.local/share/nomic.ai/GPT4All/`

**Option B: Direct Download**
1. Visit https://gpt4all.io/models/
2. Download one of these models:
   - **orca-mini-3b-gguf2-q4_0.gguf** (~1.8GB) - Best for 8GB RAM
   - **ggml-gpt4all-j-v1.3-groovy.bin** (~3.5GB) - Good quality
   - **mistral-7b-openorca.gguf2.Q4_0.gguf** (~4GB) - Higher quality, needs 16GB RAM

### 3. Update Configuration

Edit `config.py` and set the full path to your downloaded model:

**Windows example:**
```python
LOCAL_LLM_MODEL_PATH = r"C:\Users\Devashish\AppData\Local\nomic.ai\GPT4All\orca-mini-3b-gguf2-q4_0.gguf"
```

**macOS/Linux example:**
```python
LOCAL_LLM_MODEL_PATH = "/Users/yourname/Library/Application Support/nomic.ai/GPT4All/orca-mini-3b-gguf2-q4_0.gguf"
```

**Alternative: Use project models/ directory**
```python
LOCAL_LLM_MODEL_PATH = "models/orca-mini-3b-gguf2-q4_0.gguf"
```

### 4. Test the Installation

Run the test script:
```bash
python test_gpt4all.py
```

You should see:
```
✓ Model loaded successfully
✓ Model path: C:\Users\...\orca-mini-3b-gguf2-q4_0.gguf
✓ GPT4All is ready for cover letter generation
```

## Recommended Models by RAM

| RAM Available | Model | Size | Quality |
|---------------|-------|------|--------|
| 4-8 GB | orca-mini-3b-gguf2-q4_0.gguf | 1.8GB | Good |
| 8-16 GB | ggml-gpt4all-j-v1.3-groovy.bin | 3.5GB | Better |
| 16+ GB | mistral-7b-openorca.gguf2.Q4_0.gguf | 4GB | Best |

## Troubleshooting

### "Model file not found" Error
1. Verify the file exists at the path in `config.py`
2. Use absolute path (full path) instead of relative
3. On Windows, use raw string: `r"C:\path\to\model.gguf"`
4. Check filename exactly matches (case-sensitive on Linux/macOS)

### "Failed to load llamamodel-mainline-cuda" Warnings
**This is normal!** These are harmless warnings when CUDA GPU libraries aren't found. The model automatically falls back to CPU mode and works fine.

To suppress warnings:
```bash
python run_automation.py 2>$null  # PowerShell
python run_automation.py 2>/dev/null  # Linux/macOS
```

### Memory Errors
1. Close other applications
2. Try a smaller model (orca-mini-3b)
3. Disable LLM by setting in `app.py`:
   ```python
   prefer_local_llm=False
   ```

### Slow Generation
- **First run**: Model loading takes 30-60 seconds (one-time)
- **Subsequent runs**: Much faster (model stays in memory)
- **Speed tip**: CPU-only is slower than GPU, but produces same quality

### Finding Downloaded Models

Run this helper script to locate your model:
```bash
python find_model.py
```

It will search common locations and display the full path.

## Using Template Mode (No LLM)

If you prefer not to use GPT4All:
1. The system automatically falls back to template mode if model isn't found
2. Template mode generates excellent, professional cover letters
3. It's faster and uses less resources
4. Cover letters are still personalized with YOUR resume content

No changes needed—just run `python run_automation.py`!

## Performance Comparison

| Method | Speed | Quality | RAM Usage | Setup |
|--------|-------|---------|-----------|-------|
| Template | ⚡⚡⚡ Fast | 👍 Good | <100MB | None |
| GPT4All | 🐌 Moderate | 🌟 Excellent | 2-4GB | Download model |

## Additional Resources

- [GPT4All Official Site](https://gpt4all.io/)
- [GPT4All GitHub](https://github.com/nomic-ai/gpt4all)
- [Model Download Page](https://gpt4all.io/models/)
- [GPT4All Documentation](https://docs.gpt4all.io/)

---

**Questions?** Check the main [README.md](README.md) or open an issue on GitHub.