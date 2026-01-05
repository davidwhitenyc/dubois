# Tutorial: Automating PyPI Releases with GitHub Actions

A step-by-step guide to pushing a Python package to GitHub and setting up automated PyPI publishing using GitHub Actions and PyPI Trusted Publishing.

## Table of Contents

1. [What You'll Learn](#what-youll-learn)
2. [Prerequisites](#prerequisites)
3. [Understanding the Components](#understanding-the-components)
4. [Step-by-Step Implementation](#step-by-step-implementation)
5. [How to Release New Versions](#how-to-release-new-versions)
6. [Troubleshooting](#troubleshooting)
7. [Best Practices](#best-practices)

---

## What You'll Learn

By the end of this tutorial, you'll know how to:

- Prepare a Python package for GitHub with proper licensing and metadata
- Push your package to a GitHub repository
- Set up GitHub Actions for continuous deployment
- Configure PyPI Trusted Publishing (modern, secure, no tokens needed)
- Automate PyPI releases by simply pushing git tags

**The result:** Release new versions by running `git tag v0.1.1 && git push origin v0.1.1`

---

## Prerequisites

Before starting, ensure you have:

- **A Python package** with `pyproject.toml` configured
- **Git installed** on your machine
- **A GitHub account** (https://github.com)
- **A PyPI account** with 2FA enabled (https://pypi.org)
- **SSH keys** set up with GitHub (recommended) or a Personal Access Token
- **Basic git knowledge** (commit, push, tags)

---

## Understanding the Components

### 1. Git & GitHub

**Git** is version control - it tracks changes to your code over time.
**GitHub** is a hosting service for git repositories, adding collaboration features.

### 2. GitHub Actions

GitHub Actions is GitHub's CI/CD (Continuous Integration/Continuous Deployment) platform. It runs automated workflows when certain events occur (like pushing a tag).

**How it works:**
- You define workflows in `.github/workflows/*.yml` files
- GitHub runs these workflows on their servers
- Workflows can build, test, and deploy your code

### 3. PyPI (Python Package Index)

PyPI is the official repository for Python packages. When users run `pip install your-package`, pip downloads from PyPI.

### 4. PyPI Trusted Publishing (OIDC)

**The old way:** Create an API token on PyPI, store it as a GitHub secret, use it to authenticate.

**The new way (Trusted Publishing):** PyPI and GitHub use OpenID Connect (OIDC) to authenticate. GitHub provides temporary tokens to your workflow - no long-lived secrets needed!

**Benefits:**
- More secure (no secrets to leak)
- Easier to manage (no token rotation)
- Modern best practice (recommended by PyPI since 2023)

### 5. Semantic Versioning

Version numbers follow the pattern `MAJOR.MINOR.PATCH`:

- **MAJOR** (1.0.0): Breaking changes - incompatible API changes
- **MINOR** (0.1.0): New features - backward-compatible additions
- **PATCH** (0.0.1): Bug fixes - backward-compatible fixes

Examples:
- `0.1.0` → `0.1.1`: Fixed a bug
- `0.1.1` → `0.2.0`: Added a new feature
- `0.2.0` → `1.0.0`: First stable release or breaking changes

---

## Step-by-Step Implementation

### Phase 1: Prepare Your Package Files

#### Step 1.1: Create a LICENSE File

**Why:** Open source requires explicit licensing. PyPI displays your license, and it clarifies how others can use your code.

**How:** Create a file named `LICENSE` in your project root.

For MIT License:
```text
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Other license options:**
- **MIT**: Very permissive, popular for libraries
- **Apache 2.0**: Permissive with explicit patent grant
- **GPL-3.0**: Copyleft - derivatives must also be open source

#### Step 1.2: Update pyproject.toml

**Why:** PyPI uses this metadata to display your package properly and help users find it.

**How:** Add these fields to your `[project]` section:

```toml
[project]
name = "your-package"
version = "0.1.0"
description = "Short description of your package"
readme = "README.md"
license = { text = "MIT" }  # ADD THIS
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
requires-python = ">=3.9"
dependencies = []

# ADD THESE FOR BETTER DISCOVERABILITY
keywords = ["keyword1", "keyword2", "keyword3"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

# ADD THESE TO LINK TO YOUR GITHUB
[project.urls]
Homepage = "https://github.com/username/repo"
Repository = "https://github.com/username/repo"
Issues = "https://github.com/username/repo/issues"

[build-system]
# Your existing build backend configuration
```

**Key points:**
- `license = { text = "MIT" }` tells PyPI your license
- `classifiers` help users filter packages on PyPI
- `keywords` improve search discoverability
- `project.urls` creates clickable links on your PyPI page

#### Step 1.3: Update .gitignore

**Why:** Prevent committing build artifacts, OS files, and IDE configurations that don't belong in version control.

**How:** Ensure your `.gitignore` includes:

```gitignore
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
venv/
env/

# macOS files
.DS_Store

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# Type checking
.mypy_cache/
```

#### Step 1.4: Clean Unwanted Files

**Why:** Build artifacts should be regenerated, not version-controlled.

**How:**
```bash
# Remove .DS_Store files (macOS)
find . -name .DS_Store -type f -delete

# Remove old build artifacts
rm -rf dist/* build/* *.egg-info
```

### Phase 2: Initialize Git and Create Initial Commit

#### Step 2.1: Initialize Git Repository (if not already done)

```bash
cd /path/to/your/package
git init
```

#### Step 2.2: Stage All Files

```bash
git add .
```

**What this does:** Marks all files to be included in the next commit.

#### Step 2.3: Create Initial Commit

```bash
git commit -m "Initial commit: package-name

Brief description of what your package does.

Version: 0.1.0
License: MIT"
```

**Why write good commit messages:**
- Documents the history of your project
- Helps collaborators understand changes
- Professional practice for open source

### Phase 3: Create GitHub Repository and Push

#### Step 3.1: Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** Same as your package name (recommended)
   - **Description:** One-line description of your package
   - **Visibility:** **Public** (required for PyPI Trusted Publishing)
   - **Do NOT check:** "Add a README", "Add .gitignore", or "Choose a license"
     (You already have these locally)
3. Click "Create repository"

**Why public?** PyPI Trusted Publishing requires public repositories for security reasons.

#### Step 3.2: Configure Git Remote

If using SSH (recommended):
```bash
git remote add origin git@github.com:username/repo.git
```

If using HTTPS:
```bash
git remote add origin https://github.com/username/repo.git
```

**What this does:** Tells git where to push your code (your GitHub repository).

#### Step 3.3: Rename Branch to Main

```bash
git branch -M main
```

**Why:** Modern convention uses `main` instead of `master`.

#### Step 3.4: Push to GitHub

```bash
git push -u origin main
```

**What this does:**
- Uploads your code to GitHub
- Sets `origin main` as the default upstream
- After this, you can just use `git push`

**If using SSH:** You may be prompted for your SSH key passphrase.

**If using HTTPS:** You'll need a Personal Access Token (GitHub no longer accepts passwords).

### Phase 4: Create GitHub Actions Workflow

#### Step 4.1: Create Workflow Directory

```bash
mkdir -p .github/workflows
```

**Why this path?** GitHub Actions automatically looks for workflows in `.github/workflows/`.

#### Step 4.2: Create Workflow File

Create `.github/workflows/publish.yml` with this content:

```yaml
name: Publish to PyPI

on:
  push:
    tags:
      - 'v*'  # Trigger when tags like v0.1.0, v1.2.3 are pushed

permissions:
  contents: read
  id-token: write  # Required for PyPI Trusted Publishing

jobs:
  build-and-publish:
    name: Build and publish to PyPI
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install build tools
        run: |
          python -m pip install --upgrade pip
          pip install build

      - name: Build package
        run: python -m build

      - name: Check build artifacts
        run: |
          ls -lh dist/
          echo "Built packages:"
          ls dist/

      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          print-hash: true
          verbose: true
```

**If you use uv as your build backend** (like `uv_build`), replace the install and build steps:

```yaml
      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          version: "latest"

      - name: Build package
        run: uv build
```

#### Understanding the Workflow

**Trigger (`on`):**
```yaml
on:
  push:
    tags:
      - 'v*'
```
- Only runs when you push a tag starting with 'v'
- Examples: `v0.1.0`, `v1.2.3`, `v2.0.0-beta.1`
- Regular commits to `main` won't trigger this

**Permissions:**
```yaml
permissions:
  contents: read
  id-token: write  # Critical for Trusted Publishing!
```
- `contents: read` - Allows reading your repository
- `id-token: write` - Allows GitHub to generate OIDC tokens for PyPI

**Steps breakdown:**

1. **Checkout code** - Downloads your repository
2. **Set up Python** - Installs Python in the runner
3. **Install build tools** - Gets the tools needed to build your package
4. **Build package** - Creates wheel and source distribution in `dist/`
5. **Check artifacts** - Lists what was built (for debugging)
6. **Publish to PyPI** - Uploads to PyPI using OIDC authentication

#### Step 4.3: Commit and Push Workflow

```bash
git add .github/workflows/publish.yml
git commit -m "Add GitHub Actions workflow for automated PyPI publishing"
git push origin main
```

### Phase 5: Configure PyPI Trusted Publishing

This is where the magic happens - connecting GitHub to PyPI securely.

#### Step 5.1: Log into PyPI

Go to https://pypi.org and log in.

#### Step 5.2: Navigate to Your Project Settings

**If your project already exists on PyPI** (you've published manually before):
1. Go to https://pypi.org/manage/projects/
2. Click on your project name
3. Click "Settings" in the left sidebar
4. Scroll to "Publishing" section
5. Click "Add a new publisher"

**If this is a new project** (never published before):
1. Go to https://pypi.org/manage/account/publishing/
2. Click "Add a new pending publisher"

#### Step 5.3: Fill in Publisher Details

Enter these values **exactly**:

- **Owner:** Your GitHub username (e.g., `davidwhitenyc`)
- **Repository name:** Your repository name (e.g., `dubois`)
- **Workflow name:** `publish.yml`
- **Environment name:** Leave blank (unless you use GitHub Environments)

Click "Add".

**What this does:**
- Creates a trust relationship between your GitHub repo and PyPI project
- When your workflow runs, GitHub provides a temporary token
- PyPI verifies the token matches this configuration
- If verified, allows the publish

**Security note:** This is more secure than API tokens because:
- No long-lived secrets to steal
- Tokens expire immediately after use
- Tied to specific repository and workflow

#### Step 5.4: Verify Configuration

You should see your publisher listed with:
- GitHub icon
- Your username/repo
- Workflow name
- Status: Active

---

## How to Release New Versions

Now that everything is set up, releasing a new version is simple:

### Step 1: Update Version Number

Edit `pyproject.toml`:
```toml
version = "0.1.1"  # Bump from 0.1.0
```

**Semantic versioning reminder:**
- Bug fixes: `0.1.0` → `0.1.1`
- New features: `0.1.0` → `0.2.0`
- Breaking changes: `0.1.0` → `1.0.0`

### Step 2: Commit the Version Bump

```bash
git add pyproject.toml
git commit -m "Bump version to 0.1.1"
git push origin main
```

### Step 3: Create and Push a Tag

```bash
# Create annotated tag (recommended)
git tag -a v0.1.1 -m "Release version 0.1.1

- Bug fix: Fixed color palette loading
- Improved documentation
- Updated examples"

# Push the tag
git push origin v0.1.1
```

**Important:** The tag name should match the version in `pyproject.toml` (with a `v` prefix).

### Step 4: Watch the Workflow

1. Go to https://github.com/username/repo/actions
2. You'll see the "Publish to PyPI" workflow running
3. Click on it to see real-time logs
4. Wait for all steps to complete (usually 2-3 minutes)

### Step 5: Verify on PyPI

1. Go to https://pypi.org/project/your-package/
2. Refresh the page
3. Your new version should appear!
4. Test installation: `pip install --upgrade your-package`

---

## Troubleshooting

### Problem: Workflow Doesn't Trigger

**Symptom:** You pushed a tag, but no workflow runs.

**Solutions:**
- Check tag format: Must start with `v` (e.g., `v0.1.1`)
- Verify workflow file is in `.github/workflows/` on main branch
- Check YAML syntax: https://www.yamllint.com/

### Problem: Build Fails

**Symptom:** Workflow runs but fails at "Build package" step.

**Solutions:**
- Verify `pyproject.toml` syntax is valid
- Check that all required files are committed
- Ensure build backend is specified correctly
- Test build locally: `python -m build` or `uv build`

### Problem: Publish Fails with "Authentication failed"

**Symptom:** Build succeeds, but publish step fails with authentication error.

**Solutions:**
- Verify Trusted Publisher is configured on PyPI
- Check that repository is **public** (required for Trusted Publishing)
- Ensure workflow has `id-token: write` permission
- Verify Owner/Repository names match exactly

**Fallback - Use API Token:**
1. Create token: https://pypi.org/manage/account/token/
2. Add to GitHub: Repo Settings → Secrets → Actions → New secret
3. Name it `PYPI_API_TOKEN`
4. Update workflow publish step:
   ```yaml
   - name: Publish to PyPI
     uses: pypa/gh-action-pypi-publish@release/v1
     with:
       password: ${{ secrets.PYPI_API_TOKEN }}
   ```

### Problem: "Version already exists" Error

**Symptom:** Publish fails because version is already on PyPI.

**Cause:** You can't re-upload the same version to PyPI.

**Solutions:**
- Bump version in `pyproject.toml`
- Create a new tag with the new version
- Delete the old tag if needed:
  ```bash
  git tag -d v0.1.1           # Delete locally
  git push --delete origin v0.1.1  # Delete on GitHub
  ```

### Problem: SSH Authentication Issues

**Symptom:** `git push` asks for username/password or fails with "Permission denied".

**Solutions:**
- Check SSH key is loaded: `ssh-add -l`
- Add SSH key: `ssh-add ~/.ssh/id_rsa`
- Test GitHub connection: `ssh -T git@github.com`
- Or use HTTPS with Personal Access Token

---

## Best Practices

### 1. Always Test Locally Before Releasing

```bash
# Test build
python -m build  # or: uv build

# Test installation
pip install dist/your_package-0.1.0-py3-none-any.whl

# Test import
python -c "import your_package; print(your_package.__version__)"
```

### 2. Use Annotated Tags

**Good:**
```bash
git tag -a v0.1.1 -m "Release notes here"
```

**Less good:**
```bash
git tag v0.1.1  # Lightweight tag - no metadata
```

**Why:** Annotated tags store author, date, and message - useful for history.

### 3. Write Meaningful Commit Messages

**Good:**
```
Fix color palette loading bug

The get_palette() function was failing when called with
sequential palette names. Updated palette dictionary keys
to match documented names.

Fixes #42
```

**Less good:**
```
fix bug
```

### 4. Keep a CHANGELOG.md

Document what changed in each version:

```markdown
# Changelog

## [0.1.1] - 2025-01-15
### Fixed
- Fixed color palette loading bug
- Corrected documentation typos

### Added
- New diverging palette: dubois_div_02

## [0.1.0] - 2025-01-10
### Added
- Initial release
- Qualitative, sequential, and diverging palettes
- Matplotlib integration
```

### 5. Use Pre-releases for Testing

Test risky changes before stable release:

```bash
# Pre-release version
version = "0.2.0-beta.1"

git tag v0.2.0-beta.1
git push origin v0.2.0-beta.1
```

Users can install pre-releases with:
```bash
pip install --pre your-package
```

### 6. Enable GitHub Releases

After your workflow succeeds, create a GitHub Release:

1. Go to https://github.com/username/repo/releases
2. Click "Draft a new release"
3. Select your tag (e.g., `v0.1.1`)
4. Title: "Version 0.1.1"
5. Description: Copy from CHANGELOG
6. Publish

**Why:** Makes it easy to see what changed and download source code.

### 7. Monitor Your Workflows

- Check Actions tab regularly
- Fix failing workflows quickly
- Read logs to understand failures

### 8. Document Your Release Process

Create `RELEASING.md` in your repo:

```markdown
# Release Process

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Commit: `git commit -m "Release version X.Y.Z"`
4. Tag: `git tag -a vX.Y.Z -m "Release X.Y.Z"`
5. Push: `git push origin main --tags`
6. Watch GitHub Actions
7. Verify on PyPI
8. Create GitHub Release
```

---

## Summary

You've learned how to:

✅ **Prepare a package** with proper licensing and metadata
✅ **Push to GitHub** with git and SSH/HTTPS authentication
✅ **Create GitHub Actions workflows** for automation
✅ **Configure PyPI Trusted Publishing** for secure, token-free publishing
✅ **Release new versions** with simple git commands

**The modern Python packaging workflow:**

```bash
# 1. Make changes to your code
vim src/your_package/module.py

# 2. Bump version
vim pyproject.toml  # version = "0.2.0"

# 3. Commit
git add .
git commit -m "Add new feature"
git push origin main

# 4. Tag and release
git tag -a v0.2.0 -m "Release 0.2.0"
git push origin v0.2.0

# 5. Wait 2 minutes - package is live on PyPI! 🎉
```

---

## Additional Resources

- **Python Packaging Guide:** https://packaging.python.org/
- **PyPI Trusted Publishing Docs:** https://docs.pypi.org/trusted-publishers/
- **GitHub Actions Docs:** https://docs.github.com/en/actions
- **Semantic Versioning:** https://semver.org/
- **Writing Good Commit Messages:** https://cbea.ms/git-commit/

---

**Tutorial created:** January 2025
**Based on:** Setting up automated publishing for the `dubois` package
**Modern best practices:** Uses PyPI Trusted Publishing (OIDC) instead of API tokens
