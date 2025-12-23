# Scripts

## update_color_swatches.py

Automatically updates the color swatches in README.md based on the RGB values defined in `display/color_schemes.py`.

### What it does

1. Parses `display/color_schemes.py` to extract all color scheme definitions
2. Converts RGB tuples to hex color codes
3. Generates shields.io badge URLs for each color
4. Updates the "Color Schemes" section in README.md with the generated badges

### Usage

Run manually:
```bash
python3 scripts/update_color_swatches.py
```

Or let GitHub Actions run it automatically when `display/color_schemes.py` changes.

### How it works

- Reads RGB values from `COLOR_SCHEMES` dictionary
- Maps shows to their color schemes using `SHOW_COLOR_MAPPING`
- Organizes shows by category (Daily Programming, Electronic & Dance, etc.)
- Generates markdown tables with shields.io badges
- Replaces the Color Schemes section in README.md

### Automatic Updates

The GitHub Action `.github/workflows/update-color-swatches.yml` automatically runs this script whenever:
- Changes are pushed to `display/color_schemes.py` on the main branch
- Manually triggered via workflow_dispatch

After running, if the README changed, the action commits and pushes the updates.
