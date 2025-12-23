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

    # GPIO slowdown (adjust for flickering - Pi 4 typically needs 4, Pi 5 may need 2-3)
    gpio_slowdown = int(os.getenv('GPIO_SLOWDOWN', '4'))
