"""
Color schemes for different KEXP shows
Each show has a unique, carefully crafted color palette
"""

class ColorScheme:
    """Represents a color scheme with artist, song, and info colors"""
    def __init__(self, name, artist_color, song_color, info_color):
        self.name = name
        self.artist = artist_color  # (r, g, b)
        self.song = song_color
        self.info = info_color


# Define color schemes for different shows with creative, precise colors
COLOR_SCHEMES = {
    # Morning Show - Sunrise gradient (warm coral to golden yellow)
    'morning_show': ColorScheme(
        'Morning Show',
        artist_color=(255, 127, 80),   # Coral
        song_color=(255, 215, 0),      # Gold
        info_color=(135, 206, 250)     # Light sky blue
    ),

    # Afternoon - Balanced midday brightness
    'afternoon': ColorScheme(
        'Afternoon',
        artist_color=(255, 255, 255),  # Pure white
        song_color=(70, 130, 180),     # Steel blue
        info_color=(255, 195, 77)      # Amber
    ),

    # Drive Time - Traffic light energy (bold primaries)
    'drive_time': ColorScheme(
        'Drive Time',
        artist_color=(220, 20, 60),    # Crimson
        song_color=(255, 255, 255),    # White
        info_color=(255, 165, 0)       # Orange
    ),

    # Midnight in a Perfect World - Deep space electronic
    'midnight_perfect_world': ColorScheme(
        'Midnight in a Perfect World',
        artist_color=(138, 43, 226),   # Blue violet
        song_color=(0, 191, 255),      # Deep sky blue
        info_color=(186, 85, 211)      # Medium orchid
    ),

    # Audioasis - Desert world music palette
    'audioasis': ColorScheme(
        'Audioasis',
        artist_color=(205, 92, 92),    # Indian red/terracotta
        song_color=(189, 183, 107),    # Dark khaki
        info_color=(244, 164, 96)      # Sandy brown
    ),

    # Street Sounds - Urban neon graffiti
    'street_sounds': ColorScheme(
        'Street Sounds',
        artist_color=(255, 20, 147),   # Deep pink
        song_color=(0, 255, 255),      # Cyan
        info_color=(255, 215, 0)       # Gold
    ),

    # Expansions - Smoky jazz club (warm, sophisticated)
    'expansions': ColorScheme(
        'Expansions',
        artist_color=(210, 180, 140),  # Tan
        song_color=(176, 196, 222),    # Light steel blue
        info_color=(218, 165, 32)      # Goldenrod
    ),

    # Seek and Destroy - Metal (high contrast, aggressive)
    'seek_destroy': ColorScheme(
        'Seek and Destroy',
        artist_color=(255, 0, 0),      # Pure red
        song_color=(255, 255, 255),    # Pure white
        info_color=(128, 128, 128)     # Gray
    ),

    # Sonic Reducer - Punk chaos (clashing colors)
    'sonic_reducer': ColorScheme(
        'Sonic Reducer',
        artist_color=(255, 255, 0),    # Yellow
        song_color=(255, 0, 255),      # Magenta
        info_color=(0, 255, 0)         # Lime green
    ),

    # Pacific Notions - Pacific Northwest (mossy, misty)
    'pacific_notions': ColorScheme(
        'Pacific Notions',
        artist_color=(102, 205, 170),  # Medium aquamarine
        song_color=(176, 224, 230),    # Powder blue
        info_color=(119, 136, 153)     # Light slate gray
    ),

    # Wo' Pop - Eclectic world pop (vibrant, playful)
    'wo_pop': ColorScheme(
        "Wo' Pop",
        artist_color=(255, 105, 180),  # Hot pink
        song_color=(64, 224, 208),     # Turquoise
        info_color=(255, 215, 0)       # Gold
    ),

    # El Sonido - Latin music (spicy, warm)
    'el_sonido': ColorScheme(
        'El Sonido',
        artist_color=(255, 69, 0),     # Red-orange
        song_color=(255, 215, 0),      # Gold
        info_color=(148, 0, 211)       # Dark violet
    ),

    # Mechanical Breakdown - Industrial (metallic, harsh)
    'mechanical_breakdown': ColorScheme(
        'Mechanical Breakdown',
        artist_color=(192, 192, 192),  # Silver
        song_color=(255, 99, 71),      # Tomato red
        info_color=(0, 206, 209)       # Dark turquoise
    ),

    # 90.TEEN - Youth energy (vibrant, bold)
    'ninety_teen': ColorScheme(
        '90.TEEN',
        artist_color=(255, 0, 127),    # Bright pink
        song_color=(0, 255, 255),      # Cyan
        info_color=(255, 255, 0)       # Yellow
    ),

    # Astral Plane - Cosmic psychedelic (space colors)
    'astral_plane': ColorScheme(
        'Astral Plane',
        artist_color=(138, 43, 226),   # Blue violet
        song_color=(255, 0, 255),      # Magenta
        info_color=(0, 191, 255)       # Deep sky blue
    ),

    # Early - Sunrise morning (dawn colors)
    'early': ColorScheme(
        'Early',
        artist_color=(255, 182, 193),  # Light pink
        song_color=(255, 218, 185),    # Peach
        info_color=(255, 239, 213)     # Papaya whip
    ),

    # Eastern Echoes - Asian Diaspora (Eastern-inspired)
    'eastern_echoes': ColorScheme(
        'Eastern Echoes',
        artist_color=(220, 20, 60),    # Crimson red
        song_color=(255, 215, 0),      # Gold
        info_color=(0, 128, 128)       # Teal
    ),

    # Live on KEXP - Stage lighting (vibrant performance)
    'live_on_kexp': ColorScheme(
        'Live on KEXP',
        artist_color=(255, 69, 0),     # Red-orange
        song_color=(255, 255, 255),    # White spotlight
        info_color=(138, 43, 226)      # Blue violet
    ),

    # Positive Vibrations - Reggae/Rasta (traditional colors)
    'positive_vibrations': ColorScheme(
        'Positive Vibrations',
        artist_color=(252, 209, 22),   # Rasta gold
        song_color=(0, 155, 58),       # Rasta green
        info_color=(206, 17, 38)       # Rasta red
    ),

    # Sounds of Survivance - Indigenous (earth and sky)
    'sounds_survivance': ColorScheme(
        'Sounds of Survivance',
        artist_color=(139, 69, 19),    # Saddle brown
        song_color=(210, 180, 140),    # Tan
        info_color=(135, 206, 235)     # Sky blue
    ),

    # Sound & Vision - Multimedia (bold visual)
    'sound_vision': ColorScheme(
        'Sound & Vision',
        artist_color=(255, 20, 147),   # Deep pink
        song_color=(0, 255, 127),      # Spring green
        info_color=(255, 165, 0)       # Orange
    ),

    # Sunday Soul - Smooth soul (warm vintage)
    'sunday_soul': ColorScheme(
        'Sunday Soul',
        artist_color=(184, 134, 11),   # Dark goldenrod
        song_color=(219, 112, 147),    # Pale violet red
        info_color=(255, 218, 185)     # Peach puff
    ),

    # The Continent - Afrobeat (African vibrant earthy)
    'the_continent': ColorScheme(
        'The Continent',
        artist_color=(255, 140, 0),    # Dark orange
        song_color=(34, 139, 34),      # Forest green
        info_color=(220, 20, 60)       # Crimson
    ),

    # The Midday Show - Bright midday (full sun)
    'midday_show': ColorScheme(
        'The Midday Show',
        artist_color=(255, 255, 0),    # Yellow
        song_color=(255, 165, 0),      # Orange
        info_color=(135, 206, 250)     # Light sky blue
    ),

    # The Roadhouse - Honky tonk roadhouse (rustic)
    'roadhouse': ColorScheme(
        'The Roadhouse',
        artist_color=(139, 69, 19),    # Saddle brown
        song_color=(210, 105, 30),     # Chocolate
        info_color=(255, 215, 0)       # Gold
    ),

    # Variety Mix - Eclectic mix (rainbow)
    'variety_mix': ColorScheme(
        'Variety Mix',
        artist_color=(255, 99, 71),    # Tomato
        song_color=(64, 224, 208),     # Turquoise
        info_color=(255, 215, 0)       # Gold
    ),

    # Vinelands - Wine country Bay Area (wine/vineyard)
    'vinelands': ColorScheme(
        'Vinelands',
        artist_color=(128, 0, 32),     # Dark wine red
        song_color=(107, 142, 35),     # Olive drab (vine green)
        info_color=(218, 165, 32)      # Goldenrod
    ),

    # Default KEXP - Classic station palette
    'kexp_default': ColorScheme(
        'KEXP Default',
        artist_color=(255, 255, 255),  # White
        song_color=(100, 200, 255),    # Bright blue
        info_color=(255, 200, 100)     # Warm yellow
    ),
}


# Map KEXP show names to color schemes
# Only includes exact show names from KEXP Programs API
SHOW_COLOR_MAPPING = {
    # Morning programming
    'The Morning Show': 'morning_show',
    'Early': 'early',
    'The Midday Show': 'midday_show',
    'The Afternoon Show': 'afternoon',
    'Drive Time': 'drive_time',

    # Specialty shows - Electronic/Dance
    'Midnight in a Perfect World': 'midnight_perfect_world',
    'Mechanical Breakdown': 'mechanical_breakdown',
    'Astral Plane': 'astral_plane',

    # World Music
    'Audioasis': 'audioasis',
    "Wo' Pop": 'wo_pop',
    'El Sonido': 'el_sonido',
    'Eastern Echoes': 'eastern_echoes',
    'Sounds of Survivance': 'sounds_survivance',
    'The Continent': 'the_continent',

    # Reggae
    'Positive Vibrations': 'positive_vibrations',

    # Hip-Hop/R&B/Soul
    'Street Sounds': 'street_sounds',
    'Sunday Soul': 'sunday_soul',

    # Jazz/Blues/Roots
    'Expansions': 'expansions',
    'Jazz Theatre': 'expansions',
    'The Roadhouse': 'roadhouse',

    # Rock/Metal/Punk
    'Seek & Destroy': 'seek_destroy',
    'Sonic Reducer': 'sonic_reducer',
    '90.TEEN': 'ninety_teen',

    # Pacific Northwest/Indie/Local
    'Pacific Notions': 'pacific_notions',
    'Vinelands': 'vinelands',

    # Live/Special Programming
    'Live on KEXP': 'live_on_kexp',
    'Sound & Vision': 'sound_vision',
    'Variety Mix': 'variety_mix',
}


def get_color_scheme_for_show(show_name):
    """
    Get the appropriate color scheme for a given show name
    
    Args:
        show_name: Name of the show
        
    Returns:
        ColorScheme object
    """
    if not show_name:
        return COLOR_SCHEMES['kexp_default']
    
    # Try exact match first (case sensitive)
    if show_name in SHOW_COLOR_MAPPING:
        scheme_name = SHOW_COLOR_MAPPING[show_name]
        return COLOR_SCHEMES[scheme_name]
    
    # Try case-insensitive exact match
    show_lower = show_name.lower()
    for show_key, scheme_name in SHOW_COLOR_MAPPING.items():
        if show_key.lower() == show_lower:
            return COLOR_SCHEMES[scheme_name]
    
    # Try partial match (case insensitive)
    for show_key, scheme_name in SHOW_COLOR_MAPPING.items():
        if show_key.lower() in show_lower or show_lower in show_key.lower():
            return COLOR_SCHEMES[scheme_name]
    
    # Default fallback
    return COLOR_SCHEMES['kexp_default']
