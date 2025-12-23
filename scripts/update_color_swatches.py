#!/usr/bin/env python3
"""
Update README color swatches from color_schemes.py
Automatically generates shields.io badges from RGB values
"""

import re
import sys
from pathlib import Path

# Add parent directory to path to import color_schemes
sys.path.insert(0, str(Path(__file__).parent.parent))

from display.color_schemes import COLOR_SCHEMES, SHOW_COLOR_MAPPING


def rgb_to_hex(rgb_tuple):
    """Convert RGB tuple to hex color code"""
    r, g, b = rgb_tuple
    return f"{r:02X}{g:02X}{b:02X}"


def create_badge(hex_color, color_name):
    """Create a shields.io badge URL for a color"""
    # For light colors, add labelColor for better visibility
    light_colors = ['FFFFFF', 'FFFF00', 'FFD700', 'FFDAB9', 'FFEFD5',
                    'FFC34D', 'FCD116', '00FFFF', '00FF00', 'FFFF00',
                    '87CEEB', 'B0E0E6', '40E0D0', '00CED1', 'FFC864',
                    'D2B48C', 'B0C4DE', '66CDAA', '00FF7F']

    badge_url = f"https://img.shields.io/badge/-{hex_color}-{hex_color}?style=flat-square"
    if hex_color in light_colors:
        badge_url += f"&labelColor={hex_color}"

    return f"![#{hex_color}]({badge_url}) {color_name}"


def generate_color_table():
    """Generate the color schemes section for README"""

    # Organize shows by category
    categories = {
        'Daily Programming': [
            'Early', 'The Morning Show', 'The Midday Show', 'The Afternoon Show', 'Drive Time'
        ],
        'Electronic & Dance': [
            'Midnight in a Perfect World', 'Mechanical Breakdown', 'Astral Plane'
        ],
        'World Music': [
            'Audioasis', "Wo' Pop", 'El Sonido', 'Eastern Echoes',
            'Sounds of Survivance', 'The Continent'
        ],
        'Reggae & Caribbean': [
            'Positive Vibrations'
        ],
        'Hip-Hop, R&B & Soul': [
            'Street Sounds', 'Sunday Soul'
        ],
        'Jazz, Blues & Roots': [
            'Expansions', 'Jazz Theatre', 'The Roadhouse'
        ],
        'Rock, Metal & Punk': [
            'Seek & Destroy', 'Sonic Reducer', '90.TEEN'
        ],
        'Pacific Northwest & Local': [
            'Pacific Notions', 'Vinelands'
        ],
        'Special Programming': [
            'Live on KEXP', 'Sound & Vision', 'Variety Mix'
        ],
        'Default': [
            'KEXP Default'
        ]
    }

    # Color name mapping for display
    color_names = {
        'morning_show': ('Coral', 'Gold', 'Light Sky Blue'),
        'afternoon': ('White', 'Steel Blue', 'Amber'),
        'drive_time': ('Crimson', 'White', 'Orange'),
        'midnight_perfect_world': ('Blue Violet', 'Deep Sky Blue', 'Medium Orchid'),
        'audioasis': ('Indian Red', 'Dark Khaki', 'Sandy Brown'),
        'street_sounds': ('Deep Pink', 'Cyan', 'Gold'),
        'expansions': ('Tan', 'Light Steel Blue', 'Goldenrod'),
        'seek_destroy': ('Pure Red', 'Pure White', 'Gray'),
        'sonic_reducer': ('Yellow', 'Magenta', 'Lime Green'),
        'pacific_notions': ('Medium Aquamarine', 'Powder Blue', 'Light Slate Gray'),
        'wo_pop': ('Hot Pink', 'Turquoise', 'Gold'),
        'el_sonido': ('Red-Orange', 'Gold', 'Dark Violet'),
        'mechanical_breakdown': ('Silver', 'Tomato Red', 'Dark Turquoise'),
        'ninety_teen': ('Bright Pink', 'Cyan', 'Yellow'),
        'astral_plane': ('Blue Violet', 'Magenta', 'Deep Sky Blue'),
        'early': ('Light Pink', 'Peach', 'Papaya Whip'),
        'eastern_echoes': ('Crimson Red', 'Gold', 'Teal'),
        'live_on_kexp': ('Red-Orange', 'White Spotlight', 'Blue Violet'),
        'positive_vibrations': ('Rasta Gold', 'Rasta Green', 'Rasta Red'),
        'sounds_survivance': ('Saddle Brown', 'Tan', 'Sky Blue'),
        'sound_vision': ('Deep Pink', 'Spring Green', 'Orange'),
        'sunday_soul': ('Dark Goldenrod', 'Pale Violet Red', 'Peach Puff'),
        'the_continent': ('Dark Orange', 'Forest Green', 'Crimson'),
        'midday_show': ('Yellow', 'Orange', 'Light Sky Blue'),
        'roadhouse': ('Saddle Brown', 'Chocolate', 'Gold'),
        'variety_mix': ('Tomato', 'Turquoise', 'Gold'),
        'vinelands': ('Dark Wine Red', 'Olive Drab', 'Goldenrod'),
        'kexp_default': ('White', 'Bright Blue', 'Warm Yellow'),
    }

    # Theme descriptions
    themes = {
        'Early': 'Sunrise morning',
        'The Morning Show': 'Warm sunrise gradient',
        'The Midday Show': 'Bright midday sun',
        'The Afternoon Show': 'Balanced brightness',
        'Drive Time': 'Bold primaries',
        'Midnight in a Perfect World': 'Deep space electronic',
        'Mechanical Breakdown': 'Industrial metallic',
        'Astral Plane': 'Cosmic psychedelic',
        'Audioasis': 'Desert palette',
        "Wo' Pop": 'Vibrant eclectic',
        'El Sonido': 'Spicy Latin warmth',
        'Eastern Echoes': 'Eastern-inspired',
        'Sounds of Survivance': 'Earth and sky',
        'The Continent': 'African vibrant',
        'Positive Vibrations': 'Rasta colors',
        'Street Sounds': 'Urban neon graffiti',
        'Sunday Soul': 'Warm vintage soul',
        'Expansions': 'Smoky jazz club',
        'Jazz Theatre': 'Smoky jazz club',
        'The Roadhouse': 'Rustic honky tonk',
        'Seek & Destroy': 'Aggressive metal',
        'Sonic Reducer': 'Punk chaos',
        '90.TEEN': 'Youth energy',
        'Pacific Notions': 'Mossy, misty PNW',
        'Vinelands': 'Wine country',
        'Live on KEXP': 'Stage lighting',
        'Sound & Vision': 'Bold multimedia',
        'Variety Mix': 'Eclectic rainbow',
        'KEXP Default': 'Classic station',
    }

    output = []
    output.append("## Color Schemes\n")
    output.append("Each KEXP show has a unique, carefully crafted color palette that reflects its musical style and vibe. The display uses three colors for each show:")
    output.append("- **Artist Color**: Used for the artist name (top line)")
    output.append("- **Song Color**: Used for the song title (middle line)")
    output.append("- **Info Color**: Used for show name or station ID (bottom line)\n")

    for category, shows in categories.items():
        output.append(f"### {category}\n")
        output.append("| Show | Theme | Artist Color | Song Color | Info Color |")
        output.append("|------|-------|--------------|------------|------------|")

        for show in shows:
            # Find the scheme for this show
            scheme_key = None
            if show in SHOW_COLOR_MAPPING:
                scheme_key = SHOW_COLOR_MAPPING[show]
            elif show == 'KEXP Default':
                scheme_key = 'kexp_default'

            if not scheme_key or scheme_key not in COLOR_SCHEMES:
                continue

            scheme = COLOR_SCHEMES[scheme_key]
            theme = themes.get(show, '')

            # Get color names
            names = color_names.get(scheme_key, ('Color 1', 'Color 2', 'Color 3'))

            # Convert RGB to hex and create badges
            artist_hex = rgb_to_hex(scheme.artist)
            song_hex = rgb_to_hex(scheme.song)
            info_hex = rgb_to_hex(scheme.info)

            artist_badge = create_badge(artist_hex, names[0])
            song_badge = create_badge(song_hex, names[1])
            info_badge = create_badge(info_hex, names[2])

            output.append(f"| **{show}** | {theme} | {artist_badge} | {song_badge} | {info_badge} |")

        output.append("")

    output.append("*Used for shows without a specific color scheme or when show information is unavailable.*")

    return '\n'.join(output)


def update_readme():
    """Update the README.md file with new color schemes"""
    readme_path = Path(__file__).parent.parent / 'README.md'

    if not readme_path.exists():
        print("ERROR: README.md not found")
        return False

    # Read current README
    with open(readme_path, 'r') as f:
        content = f.read()

    # Generate new color schemes section
    new_color_section = generate_color_table()

    # Find and replace the color schemes section
    # Pattern: from "## Color Schemes" to "## Troubleshooting"
    pattern = r'(## Color Schemes.*?)(?=## Troubleshooting)'

    if not re.search(pattern, content, re.DOTALL):
        print("ERROR: Could not find Color Schemes section in README")
        return False

    updated_content = re.sub(pattern, new_color_section + '\n', content, flags=re.DOTALL)

    # Write updated README
    with open(readme_path, 'w') as f:
        f.write(updated_content)

    print("✓ README.md updated successfully")
    return True


if __name__ == '__main__':
    success = update_readme()
    sys.exit(0 if success else 1)
