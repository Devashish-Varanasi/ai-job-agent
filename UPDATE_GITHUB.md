# Guide to Update GitHub Repository

This guide will help you update your existing GitHub repository at:
**https://github.com/Devashish-Varanasi/ai-job-agent**

## ⚠️ Important Notes

- Your local repository has been completely rewritten and improved
- The old version on GitHub will be replaced with the new version
- All sensitive files (config.py, email_config.py, resume files) are protected by .gitignore

## 🚀 Option 1: Complete Update (Recommended - Clean History)

This option replaces everything with the new version, giving you a clean repository.

### Step 1: Initialize Git (if not already done)

```bash
cd D:\resume_c
git init
```

### Step 2: Add the Remote Repository

```bash
git remote add origin https://github.com/Devashish-Varanasi/ai-job-agent.git
```

**Note:** If you get an error saying "remote origin already exists", use:
```bash
git remote set-url origin https://github.com/Devashish-Varanasi/ai-job-agent.git
```

### Step 3: Check Current Status

```bash
git status
```

### Step 4: Stage All Files

```bash
git add .
```

### Step 5: Check What Will Be Committed

```bash
git status
```

**Verify that sensitive files are NOT listed:**
- ❌ config.py should NOT be in the list
- ❌ email_config.py should NOT be in the list
- ❌ data/*.pdf should NOT be in the list
- ❌ companies.txt should NOT be in the list
- ✅ config_example.py SHOULD be in the list
- ✅ email_config_example.py SHOULD be in the list

### Step 6: Create Initial Commit

```bash
git commit -m "Major update: Complete refactor with personalized cover letters, multiple resume support, and improved formatting"
```

### Step 7: Force Push to Replace Old Version

**⚠️ WARNING: This will replace everything on GitHub!**

```bash
git branch -M main
git push -u origin main --force
```

**Alternative (if main branch already exists):**
```bash
git checkout -b main
git push -u origin main --force
```

---

## 🔄 Option 2: Update with History (Keep Old Commits)

If you want to keep the old commit history and just add new changes:

### Step 1: Fetch Existing Repository

```bash
cd D:\resume_c
git init
git remote add origin https://github.com/Devashish-Varanasi/ai-job-agent.git
git fetch origin
```

### Step 2: Check Existing Branches

```bash
git branch -r
```

### Step 3: Merge or Reset

**Option A: Merge (preserves old commits):**
```bash
git checkout -b main
git merge origin/main --allow-unrelated-histories
# Resolve any conflicts if they occur
git add .
git commit -m "Merge: Major update with new features"
git push -u origin main
```

**Option B: Reset (cleaner, but loses old commits):**
```bash
git checkout -b main
git reset --hard origin/main
git add .
git commit -m "Major update: Complete refactor"
git push -u origin main --force
```

---

## ✅ Option 3: Manual Update (Safest)

If you prefer to manually update files:

### Step 1: Clone Your Existing Repository

```bash
cd D:\
git clone https://github.com/Devashish-Varanasi/ai-job-agent.git ai-job-agent-old
cd ai-job-agent-old
```

### Step 2: Copy New Files

Copy all files from `D:\resume_c` to `D:\ai-job-agent-old` (overwrite existing)

### Step 3: Commit and Push

```bash
git add .
git commit -m "Major update: Complete refactor"
git push origin main
```

---

## 📋 Post-Update Checklist

After pushing to GitHub, verify:

1. ✅ **Repository Structure**: Check that all new files are visible
2. ✅ **README.md**: Verify it shows your username correctly
3. ✅ **Sensitive Files**: Ensure config.py, email_config.py, and resume files are NOT visible
4. ✅ **Documentation**: Check that all .md files are properly formatted
5. ✅ **Example Files**: Verify config_example.py and email_config_example.py are visible

## 🔍 Verify Your Upload

Visit your repository: https://github.com/Devashish-Varanasi/ai-job-agent

You should see:
- ✅ Updated README.md
- ✅ All source files in `src/` folder
- ✅ Configuration examples (config_example.py, email_config_example.py)
- ✅ Documentation files (CHANGELOG.md, CONTRIBUTING.md, SECURITY.md)
- ✅ .gitignore file
- ✅ Directory structure with .gitkeep files

You should NOT see:
- ❌ config.py (your personal config)
- ❌ email_config.py (your credentials)
- ❌ companies.txt (your watchlist)
- ❌ Resume files in data/ folder
- ❌ Generated output files

## 🎉 Done!

Your repository should now be updated with the new version!

---

## 💡 Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/Devashish-Varanasi/ai-job-agent.git
```

### Error: "Permission denied"
- Make sure you're logged into GitHub
- Check your Git credentials: `git config --global user.name` and `git config --global user.email`
- Use GitHub Personal Access Token instead of password

### Error: "refusing to merge unrelated histories"
```bash
git merge origin/main --allow-unrelated-histories
```

### Want to see what changed?
```bash
git log --oneline
git diff origin/main
```

