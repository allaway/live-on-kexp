"""
Color schemes for different KEXP shows based on genre/theme
"""

class ColorScheme:
    """Represents a color scheme with artist, song, and info colors"""
    def __init__(self, name, artist_color, song_color, info_color):
        self.name = name
        self.artist = artist_color  # (r, g, b)
        self.song = song_color
        self.info = info_color  # For album/station ID/etc


# Define color schemes for different genres/themes
COLOR_SCHEMES = {
    # Indie/Alternative Rock - Current default (bright, clean)
    'indie_rock': ColorScheme(
        'Indie Rock',
        artist_color=(255, 255, 255),  # White
        song_color=(100, 200, 255),    # Light blue
        info_color=(150, 150, 150)     # Gray
    ),

    # World Music - Warm, earthy tones
    'world': ColorScheme(
        'World Music',
        artist_color=(255, 200, 100),  # Warm orange/gold
        song_color=(200, 255, 150),    # Soft green
        info_color=(180, 140, 100)     # Earthy brown
    ),

    # Reggae/Dancehall - Reggae colors (green, yellow, red)
    'reggae': ColorScheme(
        'Reggae',
        artist_color=(255, 220, 0),    # Yellow/gold
        song_color=(100, 255, 100),    # Bright green
        info_color=(255, 100, 100)     # Red
    ),

    # Hip-Hop/R&B - Bold, vibrant
    'hiphop': ColorScheme(
        'Hip-Hop',
        artist_color=(255, 100, 255),  # Magenta
        song_color=(100, 255, 255),    # Cyan
        info_color=(200, 200, 100)     # Yellow
    ),

    # Electronic/Dance - Cool neon colors
    'electronic': ColorScheme(
        'Electronic',
        artist_color=(0, 255, 200),    # Neon teal
        song_color=(255, 0, 255),      # Neon purple
        info_color=(100, 200, 255)     # Electric blue
    ),

    # Jazz/Soul - Smooth, warm tones
    'jazz': ColorScheme(
        'Jazz',
        artist_color=(255, 180, 120),  # Warm peach
        song_color=(150, 200, 255),    # Soft blue
        info_color=(200, 150, 200)     # Lavender
    ),

    # Classic/Psychedelic Rock - Retro colors
    'classic_rock': ColorScheme(
        'Classic Rock',
        artist_color=(255, 150, 0),    # Orange
        song_color=(200, 100, 255),    # Purple
        info_color=(255, 200, 0)       # Gold
    ),

    # Metal/Punk - High contrast, intense
    'metal': ColorScheme(
        'Metal',
        artist_color=(255, 50, 50),    # Bright red
        song_color=(255, 255, 255),    # White
        info_color=(150, 150, 150)     # Gray
    ),

    # Folk/Americana - Natural, muted tones
    'folk': ColorScheme(
        'Folk',
        artist_color=(220, 200, 150),  # Tan
        song_color=(150, 200, 150),    # Sage green
        info_color=(180, 150, 120)     # Wood brown
    ),

    # Experimental/Avant-garde - Unusual color combinations
    'experimental': ColorScheme(
        'Experimental',
        artist_color=(200, 255, 0),    # Lime
        song_color=(255, 100, 200),    # Hot pink
        info_color=(100, 200, 200)     # Teal
    ),

    # Morning/Daytime - Bright, energetic
    'morning': ColorScheme(
        'Morning',
        artist_color=(255, 200, 0),    # Sunshine yellow
        song_color=(100, 200, 255),    # Sky blue
        info_color=(255, 150, 100)     # Coral
    ),

    # Late Night - Cool, subdued
    'late_night': ColorScheme(
        'Late Night',
        artist_color=(150, 150, 255),  # Soft purple
        song_color=(100, 200, 200),    # Teal
        info_color=(120, 120, 180)     # Muted blue
    ),
}


# Map KEXP show names to color schemes
# Based on common KEXP programs
SHOW_COLOR_MAPPING = {
    # Morning shows
    'Morning Show': 'morning',
    'The Sunray Show': 'indie_rock',

    # World music
    'Audioasis': 'world',
    'Global Music': 'world',

    # Reggae
    'Shakedown': 'reggae',
    'Dub Shack': 'reggae',

    # Hip-Hop/R&B
    'Street Sounds': 'hiphop',
    'Rap Attack': 'hiphop',
    'Soul Serenade': 'jazz',

    # Electronic
    'Midnight in a Perfect World': 'electronic',
    'Techno': 'electronic',
    'Electronic': 'electronic',

    # Jazz
    'Expansions': 'jazz',
    'Jazz': 'jazz',

    # Classic Rock
    'Psychedelic Shack': 'classic_rock',
    'Classic Rock': 'classic_rock',

    # Metal/Punk
    'Seek and Destroy': 'metal',
    'Sonic Reducer': 'metal',

    # Folk/Americana
    'Roots & Wires': 'folk',
    'Americana': 'folk',

    # Experimental
    'Audio Oasis': 'experimental',
    'Overnight': 'late_night',
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
        return COLOR_SCHEMES['indie_rock']  # Default

    # Try exact match first
    if show_name in SHOW_COLOR_MAPPING:
        scheme_name = SHOW_COLOR_MAPPING[show_name]
        return COLOR_SCHEMES[scheme_name]

    # Try partial match (case insensitive)
    show_lower = show_name.lower()
    for show_key, scheme_name in SHOW_COLOR_MAPPING.items():
        if show_key.lower() in show_lower or show_lower in show_key.lower():
            return COLOR_SCHEMES[scheme_name]

    # Try genre detection from show name
    if any(word in show_lower for word in ['world', 'global', 'international']):
        return COLOR_SCHEMES['world']
    elif any(word in show_lower for word in ['reggae', 'dub', 'dancehall']):
        return COLOR_SCHEMES['reggae']
    elif any(word in show_lower for word in ['hip hop', 'hiphop', 'rap', 'r&b']):
        return COLOR_SCHEMES['hiphop']
    elif any(word in show_lower for word in ['electronic', 'techno', 'house', 'edm']):
        return COLOR_SCHEMES['electronic']
    elif any(word in show_lower for word in ['jazz', 'soul', 'blues']):
        return COLOR_SCHEMES['jazz']
    elif any(word in show_lower for word in ['metal', 'punk', 'hardcore']):
        return COLOR_SCHEMES['metal']
    elif any(word in show_lower for word in ['folk', 'americana', 'country']):
        return COLOR_SCHEMES['folk']
    elif any(word in show_lower for word in ['morning', 'breakfast']):
        return COLOR_SCHEMES['morning']
    elif any(word in show_lower for word in ['midnight', 'overnight', 'late night']):
        return COLOR_SCHEMES['late_night']

    # Default to indie rock
    return COLOR_SCHEMES['indie_rock']
