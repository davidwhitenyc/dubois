# A Visual Map of DuBois Python Data Portraits Library

dubois_python_data_portraits/              # Root directory - use underscores, not hyphens
│
├── README.md                              # REQUIRED: PyPI uses this for the project page
│                                          # Include: description, installation, usage examples
│
├── LICENSE                                # REQUIRED: Choose MIT, Apache 2.0, BSD, etc.
│                                          # PyPI won't accept packages without a license
│
├── pyproject.toml                         # REQUIRED: Modern Python packaging config
│                                          # Replaces old setup.py - contains all metadata
│
├── .gitignore                             # RECOMMENDED: Prevents committing unwanted files
│                                          # Include: __pycache__/, *.egg-info/, dist/, .venv/
│
├── CHANGELOG.md                           # OPTIONAL: Track version changes
│                                          # Users appreciate knowing what changed
│
├── MANIFEST.in                            # OPTIONAL: Only if pyproject.toml doesn't catch all files
│                                          # Explicitly includes non-Python files in package
│
├── .github/                               # OPTIONAL: GitHub-specific files
│   └── workflows/                         # GitHub Actions for CI/CD
│       └── publish.yml                    # Auto-publish to PyPI on release
│
├── docs/                                  # OPTIONAL: Documentation beyond README
│   ├── index.md                          # Main documentation page
│   └── examples/                         # Jupyter notebooks or Python scripts
│       ├── getting_started.ipynb         # Basic usage tutorial
│       └── advanced_features.ipynb       # Complex examples
│
├── tests/                                 # HIGHLY RECOMMENDED: Unit tests
│   ├── __init__.py                       # Makes tests a package (for imports)
│   ├── conftest.py                       # pytest configuration and fixtures
│   ├── test_themes.py                    # Test theme functionality
│   ├── test_datasets.py                  # Test data loading
│   ├── test_analytics.py                 # Test calculations
│   └── data/                             # Test-specific data files
│       └── test_sample.csv               # Don't use production data for tests
│
└── src/                                   # BEST PRACTICE: Isolated source directory
    │                                      # Prevents accidental local imports
    │
    └── dubois/                           # YOUR PACKAGE: This is what gets imported
        │                                 # Users will: `import dubois` or `from dubois import ...`
        │
        ├── __init__.py                   # REQUIRED: Makes this a package
        │                                 # Often contains: __version__ = "0.1.0"
        │                                 # Can expose main APIs: from .themes import get_palette
        │
        ├── __version__.py                # OPTIONAL: Single source of version truth
        │                                 # Contains: __version__ = "0.1.0"
        │
        ├── py.typed                      # OPTIONAL: Indicates package has type hints
        │                                 # Empty file that enables mypy support
        │
        ├── themes/                       # SUB-PACKAGE: Color and style management
        │   ├── __init__.py              # Can expose: from .palettes import get_dubois_colors
        │   ├── palettes.py              # MODULE: Color definitions
        │   │                            # Example: DUBOIS_COLORS = ["#654321", "#DC143C", ...]
        │   ├── styles.py                # MODULE: Matplotlib style management
        │   │                            # Functions to apply themes: apply_dubois_theme()
        │   └── assets/                  # RESOURCE DIR: Non-Python files
        │       ├── base.mplstyle       # Matplotlib style file
        │       ├── vintage.mplstyle    # Alternative theme
        │       └── modern.mplstyle     # Another variant
        │
        ├── datasets/                    # SUB-PACKAGE: Sample data management
        │   ├── __init__.py             # Expose: from .loader import load_sample_data
        │   ├── loader.py               # MODULE: Data loading utilities
        │   │                           # Functions like: load_csv(), get_available_datasets()
        │   ├── registry.py             # MODULE: Track available datasets
        │   │                           # DATASETS = {"census_1900": "census_1900.csv", ...}
        │   └── files/                  # RESOURCE DIR: Actual data files
        │       ├── census_1900.csv     # Historical census data
        │       ├── income_data.csv     # Income statistics
        │       └── metadata.json       # Describes each dataset
        │
        ├── analytics/                   # SUB-PACKAGE: Calculation functions
        │   ├── __init__.py             # Expose main functions
        │   ├── metrics.py              # MODULE: Statistical calculations
        │   │                           # Functions: calculate_disparity(), trend_analysis()
        │   ├── statistics.py           # MODULE: More complex stats
        │   └── validators.py           # MODULE: Data validation
        │                               # Functions: validate_data_format(), check_nulls()
        │
        └── utils/                       # SUB-PACKAGE: Shared utilities
            ├── __init__.py             
            ├── io_helpers.py           # MODULE: File I/O utilities
            │                           # Functions: safe_read_csv(), get_resource_path()
            └── exceptions.py           # MODULE: Custom exceptions
            # Classes: DuboisError, DataNotFoundError

​                                       