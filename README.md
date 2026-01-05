# DuBois Python Data Portraits

A Python library for creating data visualizations inspired by W.E.B. Du Bois' iconic data portraits from the 1900 Paris Exposition.

## Overview

This library provides tools to help create visualizations in the distinctive style of W.E.B. Du Bois' groundbreaking work, which combined statistical rigor with striking visual design to tell the story of African Americans at the turn of the 20th century.

## Features

- **Custom Color Palettes**: Pre-defined color schemes extracted from Du Bois' original visualizations
  - Qualitative palettes for categorical data
  - Sequential palettes for continuous data
  - Diverging palettes for data with meaningful midpoints

- **Typography Support**: Access to Baskerville font recommendations matching Du Bois' original style

- **Matplotlib Integration**: Custom matplotlib style file (`.mplstyle`) for consistent theming

- **Easy Palette Access**: Simple helper functions to retrieve and apply color palettes

## Installation

```bash
pip install dubois
```

## Quick Start

```python
import dubois
import matplotlib.pyplot as plt

# Apply DuBois style to matplotlib
dubois.use_style()

# Get a color palette
palette = dubois.get_palette('dubois_cat_01')

# Use in your visualizations
plt.plot(x, y, color=palette[0])
```

## Color Palettes

The library includes multiple palette categories:

- **Qualitative**: For categorical data (e.g., `dubois_cat_01`)
- **Sequential**: For continuous data (e.g., `dubois_seq_01`)
- **Diverging**: For data with meaningful center points (e.g., `dubois_div_01`)

## Inspiration

This project draws inspiration from W.E.B. Du Bois' "Data Portraits Visualizing Black America," which showcased innovative data visualization techniques including choropleth maps, bar charts, and area charts to represent demographic, economic, and social data about African Americans.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

This library is inspired by the pioneering data visualization work of W.E.B. Du Bois and the comprehensive analysis found in "W.E.B. Du Bois's Data Portraits: Visualizing Black America" edited by Whitney Battle-Baptiste and Britt Rusert.