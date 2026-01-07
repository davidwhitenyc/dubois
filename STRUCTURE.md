# A Visual Map of DuBois Python Data Portraits Library

## Current Project Structure

```
dubois/
│
├── README.md                              # ✅ PyPI landing page with description, installation, usage
│                                          # Includes features, quick start, palette examples
│
├── LICENSE                                # ✅ MIT License - full text
│                                          # Copyright (c) 2025 David White
│
├── pyproject.toml                         # ✅ Modern Python packaging configuration
│                                          # Version: 0.1.0
│                                          # Includes: license, keywords, classifiers, project URLs
│                                          # Build backend: uv_build
│                                          # Python requirement: >=3.13
│
├── .gitignore                             # ✅ Excludes build artifacts, cache, IDE files
│                                          # Also excludes personal tutorial file
│
├── .python-version                        # ✅ Specifies Python 3.13
│
├── .github/                               # ✅ GitHub-specific configuration
│   └── workflows/                         # CI/CD automation
│       └── publish.yml                    # Auto-publishes to PyPI on git tag push (v*)
│                                          # Uses PyPI Trusted Publishing (OIDC)
│
├── dubois_library_checklist.md            # ✅ Development planning document
│
├── A Visual Map of DuBois Python Data Portraits Library.md  # ✅ This file
│
├── TUTORIAL_GitHub_PyPI_Automation.md     # ✅ Personal tutorial (gitignored)
│                                          # Step-by-step guide for GitHub/PyPI automation
│
└── src/                                   # ✅ Source directory (best practice layout)
    │
    └── dubois/                            # ✅ Main package (import dubois)
        │
        ├── __init__.py                    # ✅ Package initialization
        │                                  # Exposes: use_style(), get_palette()
        │
        ├── py.typed                       # ✅ Type hints marker
        │                                  # Enables mypy support for package users
        │
        ├── palettes.py                    # ✅ Color palette definitions
        │                                  # Contains:
        │                                  #   - qualitative_palettes (categorical data)
        │                                  #   - sequential_palettes (continuous data)
        │                                  #   - diverging_palettes (data with midpoint)
        │                                  # All palettes extracted from Du Bois originals
        │
        └── dubois.mplstyle                # ✅ Matplotlib style file
                                           # Defines: fonts, colors, grid, axes styling
                                           # Applied via dubois.use_style()
```

---

## Package Information

**Package Name:** dubois
**Version:** 0.1.0
**Published on PyPI:** ✅ Yes
**GitHub Repository:** https://github.com/davidwhitenyc/dubois
**Python Requirement:** >=3.13
**Dependencies:** None (lightweight package)
**License:** MIT                                       