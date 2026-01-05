# DuBois Python Data Portraits Library - Project Checklist

##  [  ] Project Root Configuration

These files form the foundation of your Python package and ensure it can be properly distributed and maintained.

### Essential Package Files

- [ ] **README.md** - PyPI project page content
  The README serves as your package's landing page on PyPI. Include a compelling description of what the library does, clear installation instructions, and concrete usage examples showing how to create DuBois-style visualizations.

- [ ] **LICENSE** - Open source license file
  Choose an appropriate license (MIT, Apache 2.0, or BSD are common choices). PyPI requires a license file for package distribution, and it clarifies how others can use your work.

- [ ] **pyproject.toml** - Modern Python packaging configuration
  This file replaces the old setup.py approach and contains all package metadata, dependencies, and build configuration. It's the single source of truth for your package configuration.

### Development Support Files

- [ ] **.gitignore** - Version control exclusions
  Prevent unnecessary files from being committed to your repository. Include patterns for `__pycache__/`, `*.egg-info/`, `dist/`, `.venv/`, and other build artifacts or local development files.

- [ ] **CHANGELOG.md** - Version history tracking
  Document what changes in each release. Users appreciate knowing what's new, what's fixed, and what might break when they upgrade.

- [ ] **MANIFEST.in** - Non-Python file inclusion rules
  Only needed if pyproject.toml doesn't automatically include all necessary files. Use this to explicitly include data files, style sheets, or other resources in your package distribution.

##  [  ] GitHub Integration

Automate your development workflow with GitHub-specific features.

### CI/CD Configuration

- [ ] **.github/workflows/publish.yml** - Automated PyPI publishing
  Set up GitHub Actions to automatically publish new releases to PyPI when you create a GitHub release. This ensures consistent and reliable package deployment.

##  [  ] Documentation

Clear documentation helps users understand and effectively use your library.

### Documentation Structure

- [ ] **docs/index.md** - Main documentation entry point
  Provide comprehensive documentation beyond what's in the README. Include API reference, detailed examples, and theoretical background on DuBois's visualization principles.

- [ ] **docs/examples/getting_started.ipynb** - Basic usage tutorial
  Create an interactive Jupyter notebook that walks new users through creating their first DuBois-style visualization, from data loading to final styling.

- [ ] **docs/examples/advanced_features.ipynb** - Complex examples
  Demonstrate advanced features like custom color palettes, complex data transformations, and combining multiple visualization types in the DuBois style.

##  [  ] Testing Infrastructure

A robust test suite ensures your library works correctly and continues to work as you add features.

### Test Organization

- [ ] **tests/__init__.py** - Test package initialization
  Makes the tests directory a proper Python package, enabling relative imports between test modules.

- [ ] **tests/conftest.py** - pytest configuration and shared fixtures
  Define common test fixtures, configuration options, and helper functions used across multiple test files.

- [ ] **tests/test_themes.py** - Theme functionality tests
  Test color palette loading, style application, and theme switching functionality. Ensure matplotlib styles apply correctly.

- [ ] **tests/test_datasets.py** - Data loading tests
  Verify that sample datasets load correctly, handle missing files gracefully, and return data in expected formats.

- [ ] **tests/test_analytics.py** - Calculation tests
  Test statistical functions, metrics calculations, and data transformations. Include edge cases and error handling.

- [ ] **tests/data/test_sample.csv** - Test-specific data
  Create minimal test data files separate from production data. This keeps tests fast and predictable.

##  [  ] Source Code Structure

The actual Python code that implements your library's functionality.

### Package Root

- [ ] **src/dubois/__init__.py** - Package initialization
  Define what gets imported with `import dubois`. Set `__version__`, expose main APIs like `from .themes import get_palette`. This is users' first point of contact with your code.

- [ ] **src/dubois/__version__.py** - Version definition
  Single source of truth for version numbering. Contains just `__version__ = "0.1.0"` to avoid circular imports.

- [ ] **src/dubois/py.typed** - Type hints marker
  Empty file that signals to type checkers that your package includes type hints. Enables better IDE support and type checking for users.

### Themes Sub-package

Manages the distinctive DuBois color schemes and visual styles.

- [ ] **src/dubois/themes/__init__.py** - Theme module initialization
  Expose main theme functions like `from .palettes import get_dubois_colors`.

- [ ] **src/dubois/themes/palettes.py** - Color definitions
  Define DuBois color schemes as constants (e.g., `DUBOIS_COLORS = ["#654321", "#DC143C", ...]`). Include multiple palettes for different visualization types.

- [ ] **src/dubois/themes/styles.py** - Matplotlib style management
  Implement functions to apply DuBois themes to matplotlib figures, such as `apply_dubois_theme()`. Handle style context managers and theme customization.

- [ ] **src/dubois/themes/assets/base.mplstyle** - Base matplotlib style
  Define the foundational DuBois style settings for matplotlib, including fonts, line weights, and grid properties.

- [ ] **src/dubois/themes/assets/vintage.mplstyle** - Vintage theme variant
  Create a style that closely mimics the original hand-drawn DuBois aesthetics with appropriate textures and colors.

- [ ] **src/dubois/themes/assets/modern.mplstyle** - Modern theme variant
  Provide a contemporary interpretation of DuBois principles suitable for digital presentations.

### Datasets Sub-package

Provides easy access to sample historical datasets for creating DuBois-style visualizations.

- [ ] **src/dubois/datasets/__init__.py** - Dataset module initialization
  Expose data loading functions like `from .loader import load_sample_data`.

- [ ] **src/dubois/datasets/loader.py** - Data loading utilities
  Implement functions like `load_csv()` and `get_available_datasets()`. Handle file paths, caching, and error cases.

- [ ] **src/dubois/datasets/registry.py** - Dataset catalog
  Maintain a registry of available datasets: `DATASETS = {"census_1900": "census_1900.csv", ...}`. Include metadata about each dataset.

- [ ] **src/dubois/datasets/files/census_1900.csv** - Historical census data
  Include actual historical data that DuBois might have used, properly formatted and cleaned.

- [ ] **src/dubois/datasets/files/income_data.csv** - Income statistics
  Provide economic data suitable for creating DuBois-style economic visualizations.

- [ ] **src/dubois/datasets/files/metadata.json** - Dataset descriptions
  Document each dataset's source, time period, variables, and suggested visualizations.

### Analytics Sub-package

Statistical and analytical functions tailored for the types of analyses DuBois performed.

- [ ] **src/dubois/analytics/__init__.py** - Analytics module initialization
  Expose main analytical functions for easy importing.

- [ ] **src/dubois/analytics/metrics.py** - Statistical calculations
  Implement functions like `calculate_disparity()` and `trend_analysis()` that align with DuBois's analytical approach.

- [ ] **src/dubois/analytics/statistics.py** - Advanced statistics
  Provide more complex statistical analyses relevant to social science data and historical comparisons.

- [ ] **src/dubois/analytics/validators.py** - Data validation
  Include functions like `validate_data_format()` and `check_nulls()` to ensure data quality before visualization.

### Utilities Sub-package

Shared helper functions used throughout the library.

- [ ] **src/dubois/utils/__init__.py** - Utilities initialization
  Make utility functions available to other modules.

- [ ] **src/dubois/utils/io_helpers.py** - File I/O utilities
  Implement `safe_read_csv()`, `get_resource_path()`, and other functions for reliable file operations across platforms.

- [ ] **src/dubois/utils/exceptions.py** - Custom exceptions
  Define library-specific exceptions like `DuboisError` and `DataNotFoundError` for better error handling and debugging.

##  Implementation Notes

This structure follows Python packaging best practices with clear separation of concerns. The `src/` layout prevents accidental local imports during development, while the modular organization makes the codebase maintainable and extensible. Each sub-package has a specific responsibility, making it easy for contributors to understand where to add new features or fix issues.
