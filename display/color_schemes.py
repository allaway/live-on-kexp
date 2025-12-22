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

    # Shakedown - True Reggae/Rasta colors
    'shakedown': ColorScheme(
        'Shakedown',
        artist_color=(252, 209, 22),   # Rasta gold
        song_color=(0, 155, 58),       # Rasta green
        info_color=(206, 17, 38)       # Rasta red
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

    # Overnight - Late night deep blues
    'overnight': ColorScheme(
        'Overnight',
        artist_color=(72, 61, 139),    # Dark slate blue
        song_color=(147, 112, 219),    # Medium purple
        info_color=(95, 158, 160)      # Cadet blue
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

    # Seeking Blue - Deep blues tradition
    'seeking_blue': ColorScheme(
        'Seeking Blue',
        artist_color=(65, 105, 225),   # Royal blue
        song_color=(218, 165, 32),     # Goldenrod
        info_color=(123, 104, 238)     # Medium slate blue
    ),

    # Mechanical Breakdown - Industrial (metallic, harsh)
    'mechanical_breakdown': ColorScheme(
        'Mechanical Breakdown',
        artist_color=(192, 192, 192),  # Silver
        song_color=(255, 99, 71),      # Tomato red
        info_color=(0, 206, 209)       # Dark turquoise
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
SHOW_COLOR_MAPPING = {
    # Morning programming
    'Morning Show': 'morning_show',
    'The Morning Show': 'morning_show',
    'Daytime': 'afternoon',
    'Afternoon Show': 'afternoon',
    'The Afternoon Show': 'afternoon',
    'Drive Time': 'drive_time',
    
    # Specialty shows - Electronic/Dance
    'Midnight in a Perfect World': 'midnight_perfect_world',
    'MIPW': 'midnight_perfect_world',
    'Mechanical Breakdown': 'mechanical_breakdown',
    
    # World Music
    'Audioasis': 'audioasis',
    'Global Music': 'audioasis',
    "Wo' Pop": 'wo_pop',
    'El Sonido': 'el_sonido',
    
    # Reggae/Dub
    'Shakedown': 'shakedown',
    
    # Hip-Hop/R&B/Soul
    'Street Sounds': 'street_sounds',
    
    # Jazz/Blues
    'Expansions': 'expansions',
    'Jazz Theater': 'expansions',
    'Seeking Blue': 'seeking_blue',
    
    # Rock/Metal/Punk
    'Seek and Destroy': 'seek_destroy',
    'Sonic Reducer': 'sonic_reducer',
    'Rockers': 'sonic_reducer',

    # Pacific Northwest/Indie
    'Pacific Notions': 'pacific_notions',
    
    # Late Night
    'Overnight': 'overnight',
    'Late Night': 'overnight',
    'Overnight: Live from the Archives': 'overnight',
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
