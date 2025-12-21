"""
Color schemes for different KEXP shows
UPDATED: More accurate show mappings and representative colors
"""

class ColorScheme:
    """Represents a color scheme with artist, song, and info colors"""
    def __init__(self, name, artist_color, song_color, info_color):
        self.name = name
        self.artist = artist_color  # (r, g, b)
        self.song = song_color
        self.info = info_color


# Define color schemes for different genres/themes
COLOR_SCHEMES = {
    # Morning Show - Bright, energetic sunrise colors
    'morning_show': ColorScheme(
        'Morning Show',
        artist_color=(255, 180, 50),   # Warm orange
        song_color=(255, 220, 100),    # Sunshine yellow
        info_color=(100, 200, 255)     # Sky blue
    ),

    # Afternoon Show - Balanced, clean midday colors
    'afternoon': ColorScheme(
        'Afternoon',
        artist_color=(255, 255, 255),  # White
        song_color=(100, 220, 255),    # Bright blue
        info_color=(200, 200, 100)     # Soft yellow
    ),

    # Drive Time - Bold, vibrant commute energy
    'drive_time': ColorScheme(
        'Drive Time',
        artist_color=(255, 100, 100),  # Bright red
        song_color=(255, 255, 255),    # White
        info_color=(255, 200, 0)       # Gold
    ),

    # Midnight in a Perfect World - Deep electronic blues and purples
    'midnight_perfect_world': ColorScheme(
        'Midnight in a Perfect World',
        artist_color=(150, 100, 255),  # Deep purple
        song_color=(0, 200, 255),      # Electric cyan
        info_color=(200, 150, 255)     # Lavender
    ),

    # Audioasis - Warm world music earth tones
    'audioasis': ColorScheme(
        'Audioasis',
        artist_color=(255, 150, 50),   # Terracotta
        song_color=(200, 255, 100),    # Lime green
        info_color=(255, 200, 100)     # Sandy gold
    ),

    # Shakedown - Reggae colors (green, yellow, red)
    'shakedown': ColorScheme(
        'Shakedown',
        artist_color=(255, 220, 0),    # Gold/yellow
        song_color=(100, 255, 100),    # Bright green
        info_color=(255, 80, 80)       # Red
    ),

    # Street Sounds - Hip-hop vibrant urban colors
    'street_sounds': ColorScheme(
        'Street Sounds',
        artist_color=(255, 50, 200),   # Hot magenta
        song_color=(100, 255, 255),    # Cyan
        info_color=(255, 200, 0)       # Gold
    ),

    # Expansions - Jazz warm sophisticated tones
    'expansions': ColorScheme(
        'Expansions',
        artist_color=(255, 180, 120),  # Warm peach
        song_color=(200, 150, 255),    # Soft purple
        info_color=(255, 200, 100)     # Amber
    ),

    # Seek and Destroy - Metal high contrast
    'seek_destroy': ColorScheme(
        'Seek and Destroy',
        artist_color=(255, 0, 0),      # Pure red
        song_color=(255, 255, 255),    # White
        info_color=(100, 100, 100)     # Gray
    ),

    # Sonic Reducer - Punk energy
    'sonic_reducer': ColorScheme(
        'Sonic Reducer',
        artist_color=(255, 255, 0),    # Bright yellow
        song_color=(255, 0, 255),      # Magenta
        info_color=(0, 255, 0)         # Neon green
    ),

    # Pacific Notions - Pacific Northwest indie vibes
    'pacific_notions': ColorScheme(
        'Pacific Notions',
        artist_color=(100, 200, 150),  # Pacific green
        song_color=(200, 220, 255),    # Misty blue
        info_color=(150, 180, 160)     # Mossy gray
    ),

    # Overnight - Late night subdued tones
    'overnight': ColorScheme(
        'Overnight',
        artist_color=(100, 150, 200),  # Midnight blue
        song_color=(150, 150, 255),    # Soft purple
        info_color=(120, 180, 180)     # Teal
    ),

    # Wo' Pop - World pop bright eclectic
    'wo_pop': ColorScheme(
        "Wo' Pop",
        artist_color=(255, 100, 150),  # Pink
        song_color=(100, 255, 200),    # Mint
        info_color=(255, 200, 50)      # Sunny yellow
    ),

    # El Sonido - Latin music warm vibrant
    'el_sonido': ColorScheme(
        'El Sonido',
        artist_color=(255, 100, 50),   # Salsa red-orange
        song_color=(255, 200, 0),      # Sunny gold
        info_color=(200, 100, 255)     # Purple
    ),

    # Seeking Blue - Blues deep rich tones
    'seeking_blue': ColorScheme(
        'Seeking Blue',
        artist_color=(100, 150, 255),  # Deep blue
        song_color=(200, 200, 100),    # Brass yellow
        info_color=(150, 100, 200)     # Purple
    ),

    # Stevie Wonder's House Party - Soul/Funk
    'stevie_wonder': ColorScheme(
        "Stevie Wonder's House Party",
        artist_color=(255, 150, 0),    # Funky orange
        song_color=(200, 100, 255),    # Purple
        info_color=(255, 200, 0)       # Gold
    ),

    # Rockabilly Revolt - Retro rock colors
    'rockabilly': ColorScheme(
        'Rockabilly Revolt',
        artist_color=(255, 50, 100),   # Hot pink
        song_color=(0, 255, 200),      # Turquoise
        info_color=(255, 200, 0)       # Gold
    ),

    # Mechanical Breakdown - Industrial/Electronic
    'mechanical_breakdown': ColorScheme(
        'Mechanical Breakdown',
        artist_color=(200, 200, 200),  # Metallic gray
        song_color=(255, 100, 0),      # Industrial orange
        info_color=(100, 255, 255)     # Electric blue
    ),

    # Default KEXP - Classic station colors
    'kexp_default': ColorScheme(
        'KEXP Default',
        artist_color=(255, 255, 255),  # White
        song_color=(100, 200, 255),    # KEXP blue
        info_color=(200, 200, 100)     # Warm yellow
    ),
}


# Comprehensive mapping of KEXP show names to color schemes
SHOW_COLOR_MAPPING = {
    # Morning programming
    'Morning Show': 'morning_show',
    'The Morning Show': 'morning_show',
    'Daytime': 'afternoon',
    'Afternoon Show': 'afternoon',
    'The Afternoon Show': 'afternoon',
    'Drive Time': 'drive_time',
    
    # Electronic/Dance
    'Midnight in a Perfect World': 'midnight_perfect_world',
    'MIPW': 'midnight_perfect_world',
    'Mechanical Breakdown': 'mechanical_breakdown',
    'Positive Vibrations': 'wo_pop',
    
    # World Music
    'Audioasis': 'audioasis',
    'Global Music': 'audioasis',
    "Wo' Pop": 'wo_pop',
    'El Sonido': 'el_sonido',
    
    # Reggae/Dub
    'Shakedown': 'shakedown',
    'Dub Shack': 'shakedown',
    
    # Hip-Hop/R&B/Soul
    'Street Sounds': 'street_sounds',
    'Rap Attack': 'street_sounds',
    "Stevie Wonder's House Party": 'stevie_wonder',
    'Shake The Shack': 'stevie_wonder',
    
    # Jazz/Blues
    'Expansions': 'expansions',
    'Jazz Theater': 'expansions',
    'Seeking Blue': 'seeking_blue',
    
    # Rock/Metal/Punk
    'Seek and Destroy': 'seek_destroy',
    'Sonic Reducer': 'sonic_reducer',
    'Rockers': 'sonic_reducer',
    'Rockabilly Revolt': 'rockabilly',
    
    # Pacific Northwest/Indie
    'Pacific Notions': 'pacific_notions',
    'Local Show': 'pacific_notions',
    
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
    
    # Try genre/keyword detection from show name
    if any(word in show_lower for word in ['morning', 'breakfast', 'sunrise']):
        return COLOR_SCHEMES['morning_show']
    elif any(word in show_lower for word in ['afternoon', 'midday']):
        return COLOR_SCHEMES['afternoon']
    elif any(word in show_lower for word in ['drive', 'commute', 'rush hour']):
        return COLOR_SCHEMES['drive_time']
    elif any(word in show_lower for word in ['midnight', 'late night', 'overnight']):
        return COLOR_SCHEMES['overnight']
    elif any(word in show_lower for word in ['world', 'global', 'international', 'audioasis']):
        return COLOR_SCHEMES['audioasis']
    elif any(word in show_lower for word in ['reggae', 'dub', 'dancehall', 'shakedown']):
        return COLOR_SCHEMES['shakedown']
    elif any(word in show_lower for word in ['hip hop', 'hiphop', 'rap', 'street']):
        return COLOR_SCHEMES['street_sounds']
    elif any(word in show_lower for word in ['electronic', 'techno', 'house', 'edm', 'dance']):
        return COLOR_SCHEMES['midnight_perfect_world']
    elif any(word in show_lower for word in ['jazz', 'expansion']):
        return COLOR_SCHEMES['expansions']
    elif any(word in show_lower for word in ['soul', 'funk', 'stevie', 'r&b']):
        return COLOR_SCHEMES['stevie_wonder']
    elif any(word in show_lower for word in ['blues', 'seeking']):
        return COLOR_SCHEMES['seeking_blue']
    elif any(word in show_lower for word in ['metal', 'seek', 'destroy']):
        return COLOR_SCHEMES['seek_destroy']
    elif any(word in show_lower for word in ['punk', 'hardcore', 'sonic', 'reducer']):
        return COLOR_SCHEMES['sonic_reducer']
    elif any(word in show_lower for word in ['latin', 'sonido', 'spanish']):
        return COLOR_SCHEMES['el_sonido']
    elif any(word in show_lower for word in ['pacific', 'northwest', 'local', 'seattle']):
        return COLOR_SCHEMES['pacific_notions']
    elif any(word in show_lower for word in ['rockabilly', 'rock and roll', 'retro']):
        return COLOR_SCHEMES['rockabilly']
    elif any(word in show_lower for word in ['mechanical', 'industrial']):
        return COLOR_SCHEMES['mechanical_breakdown']
    
    # Default to KEXP standard colors
    return COLOR_SCHEMES['kexp_default']
