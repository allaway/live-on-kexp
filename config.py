"""
Configuration settings for KEXP Display
"""

import os


class Config:
    """Configuration class for KEXP Display"""

    # KEXP API settings
    KEXP_API_BASE = "https://api.kexp.org/v2"

    # Update interval in seconds
    update_interval = int(os.getenv('UPDATE_INTERVAL', '10'))

    # Display settings
    matrix_rows = int(os.getenv('MATRIX_ROWS', '32'))
    matrix_cols = int(os.getenv('MATRIX_COLS', '64'))
    matrix_chain_length = int(os.getenv('MATRIX_CHAIN_LENGTH', '1'))
    matrix_parallel = int(os.getenv('MATRIX_PARALLEL', '1'))

    # Brightness (0-100)
    brightness = int(os.getenv('BRIGHTNESS', '50'))

    # GPIO mapping (use adafruit-hat for Adafruit RGB Matrix Bonnet)
    gpio_mapping = os.getenv('GPIO_MAPPING', 'adafruit-hat')

    # Font settings
    font_path = os.getenv('FONT_PATH', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    small_font_size = int(os.getenv('SMALL_FONT_SIZE', '8'))
    medium_font_size = int(os.getenv('MEDIUM_FONT_SIZE', '10'))
    large_font_size = int(os.getenv('LARGE_FONT_SIZE', '12'))

    # Scroll settings
    scroll_speed = float(os.getenv('SCROLL_SPEED', '0.05'))
    scroll_pause_duration = float(os.getenv('SCROLL_PAUSE_DURATION', '2.0'))
