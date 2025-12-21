"""
Display Renderer
Handles rendering of KEXP data to RGB LED matrix
"""

import time
import logging
from PIL import Image, ImageDraw, ImageFont

logger = logging.getLogger(__name__)

try:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions
    MATRIX_AVAILABLE = True
except ImportError:
    logger.warning("RGB Matrix library not available. Running in simulation mode.")
    MATRIX_AVAILABLE = False


class DisplayRenderer:
    """Renders KEXP data to RGB LED matrix display"""

    def __init__(self, config):
        self.config = config
        self.matrix = None
        self.canvas = None

        if MATRIX_AVAILABLE:
            self._init_matrix()
        else:
            logger.info("Running in simulation mode - display output will be logged")

    def _init_matrix(self):
        """Initialize the RGB matrix with configuration"""
        options = RGBMatrixOptions()
        options.rows = self.config.matrix_rows
        options.cols = self.config.matrix_cols
        options.chain_length = self.config.matrix_chain_length
        options.parallel = self.config.matrix_parallel
        options.hardware_mapping = self.config.gpio_mapping
        options.brightness = self.config.brightness
        options.gpio_slowdown = 4  # Needed for Pi 4

        self.matrix = RGBMatrix(options=options)
        self.canvas = self.matrix.CreateFrameCanvas()

        logger.info(f"Matrix initialized: {options.cols}x{options.rows}")

    def render_now_playing(self, play_data):
        """
        Render the currently playing track information

        Args:
            play_data: Dictionary containing artist, song, album, show info
        """
        if not MATRIX_AVAILABLE:
            self._simulate_display(play_data)
            return

        try:
            # Create image for rendering
            width = self.matrix.width
            height = self.matrix.height
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)

            # Load fonts (using bitmap fonts if PIL fonts not available)
            try:
                font_small = ImageFont.truetype(self.config.font_path, self.config.small_font_size)
                font_medium = ImageFont.truetype(self.config.font_path, self.config.medium_font_size)
            except:
                font_small = ImageFont.load_default()
                font_medium = ImageFont.load_default()

            # Draw artist (top line)
            artist = play_data.get('artist', 'Unknown')
            draw.text((2, 0), artist, fill=(255, 255, 255), font=font_medium)

            # Draw song (middle line)
            song = play_data.get('song', 'Unknown')
            draw.text((2, 12), song, fill=(100, 200, 255), font=font_small)

            # Draw album or show name (bottom line)
            album = play_data.get('album', '')
            if album:
                draw.text((2, 22), album, fill=(150, 150, 150), font=font_small)

            # Convert PIL image to matrix canvas
            self.canvas.SetImage(image.convert('RGB'))
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

        except Exception as e:
            logger.error(f"Error rendering display: {e}")

    def _simulate_display(self, play_data):
        """Simulate display output when matrix is not available"""
        logger.info("=" * 60)
        logger.info(f"NOW PLAYING:")
        logger.info(f"  Artist: {play_data.get('artist', 'Unknown')}")
        logger.info(f"  Song:   {play_data.get('song', 'Unknown')}")
        logger.info(f"  Album:  {play_data.get('album', 'N/A')}")
        if play_data.get('comment'):
            logger.info(f"  Note:   {play_data.get('comment')}")
        logger.info("=" * 60)

    def render_text(self, text, color=(255, 255, 255), y_position=0):
        """
        Render simple text to the display

        Args:
            text: Text to display
            color: RGB color tuple
            y_position: Vertical position
        """
        if not MATRIX_AVAILABLE:
            logger.info(f"Display: {text}")
            return

        image = Image.new('RGB', (self.matrix.width, self.matrix.height))
        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(self.config.font_path, self.config.medium_font_size)
        except:
            font = ImageFont.load_default()

        draw.text((2, y_position), text, fill=color, font=font)

        self.canvas.SetImage(image.convert('RGB'))
        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def clear(self):
        """Clear the display"""
        if MATRIX_AVAILABLE and self.canvas:
            self.canvas.Clear()
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def cleanup(self):
        """Clean up resources"""
        if MATRIX_AVAILABLE and self.matrix:
            self.clear()
            logger.info("Display cleaned up")
