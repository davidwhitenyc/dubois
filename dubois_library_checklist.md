# DuBois Python Data Portraits Library - Project Checklist

## ✅ Essential Package Files (Completed)

- [x] **README.md** - PyPI project page content
  Comprehensive description of the library with installation instructions and usage examples for creating DuBois-style visualizations.

- [x] **LICENSE** - MIT License file
  Full MIT License text with copyright (c) 2025 David White. Required for PyPI distribution.

- [x] **pyproject.toml** - Modern Python packaging configuration
  Complete metadata including version (0.1.0), license field, keywords, classifiers, and project URLs pointing to GitHub. Uses uv_build as build backend.

- [x] **.gitignore** - Version control exclusions
  Excludes `__pycache__/`, `*.egg-info/`, `dist/`, `.venv/`, `.DS_Store`, IDE files, and personal tutorial.

- [x] **.python-version** - Python version specification
  Specifies Python 3.13 for development.

## ✅ GitHub Integration (Completed)

- [x] **GitHub Repository** - https://github.com/davidwhitenyc/dubois
  Public repository successfully created and code pushed.

- [x] **.github/workflows/publish.yml** - Automated PyPI publishing
  GitHub Actions workflow configured to auto-publish to PyPI when version tags (v*) are pushed. Uses PyPI Trusted Publishing (OIDC) - no secrets required.

- [x] **PyPI Trusted Publishing** - Configured
  Publisher configured on PyPI to accept publishes from davidwhitenyc/dubois repository via publish.yml workflow.

## ✅ Core Package Structure (Completed)

- [x] **src/dubois/__init__.py** - Package initialization
  Exposes main APIs: `use_style()` and `get_palette()`. Entry point for users importing the package.

- [x] **src/dubois/py.typed** - Type hints marker
  Empty file that signals type hint support to type checkers like mypy.

- [x] **src/dubois/palettes.py** - Color palette definitions
  Contains three palette categories:
  - qualitative_palettes - For categorical data
  - sequential_palettes - For continuous data
  - diverging_palettes - For data with meaningful midpoints
  All extracted from original Du Bois visualizations.

- [x] **src/dubois/dubois.mplstyle** - Matplotlib style file
  Defines fonts, colors, grid, and axes styling to match Du Bois aesthetic. Applied via `dubois.use_style()`.

## 📦 Release Status

- [x] **Version 0.1.0 published to PyPI**
  Package is live and installable via `pip install dubois`

- [x] **Automated release workflow active**
  Future releases automated: bump version → commit → tag → automatic PyPI publish

## 📝 Project Documentation

- [x] **A Visual Map of DuBois Python Data Portraits Library.md**
  Visual representation of current project structure and package information.

- [x] **dubois_library_checklist.md**
  This file - tracks project progress and completed items.

## Notes

This is a focused, lightweight package with no external dependencies. The simple structure makes it easy to maintain while providing essential functionality for DuBois-style data visualizations. Future expansions could include additional palettes, example datasets, or documentation enhancements as needed.
