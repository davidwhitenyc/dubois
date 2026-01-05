# __init__.py
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import os
from .palettes import palettes

# 1. Dynamic Path Finding for .mplstyle
_PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
_STYLE_PATH = os.path.join(_PACKAGE_DIR, 'dubois.mplstyle') # Must match your filename!

def use_style():
    """Applies the package's custom .mplstyle file."""
    if os.path.exists(_STYLE_PATH):
        plt.style.use(_STYLE_PATH)
    else:
        print(f"Error: Style file not found at {_STYLE_PATH}")

# 2. Register Palettes
def register_custom_palettes():
    for category, palette_dict in palettes.items():
        for name, colors in palette_dict.items():
            if category == "qualitative":
                cmap = ListedColormap(colors, name=name)
            else:
                cmap = LinearSegmentedColormap.from_list(name, colors)
            try:
                plt.colormaps.register(name=name, cmap=cmap)
            except (ValueError, AttributeError):
                pass

# Run on import
register_custom_palettes()

# Helper for Seaborn
def get_palette(name):
    for category in palettes:
        if name in palettes[category]:
            return palettes[category][name]
    raise ValueError(f"Palette '{name}' not found.")