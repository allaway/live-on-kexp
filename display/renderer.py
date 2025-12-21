"""
Display Renderer
Handles rendering of KEXP data to RGB LED matrix
"""

import time
import logging
from PIL import Image, ImageDraw, ImageFont
from display.color_schemes import get_color_scheme_for_show

logger = logging.getLogger(__name__)

try:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
    MATRIX_AVAILABLE = True
except ImportError:
    logger.warning("RGB Matrix library not available. Running in simulation mode.")
    MATRIX_AVAILABLE = False
    # Create dummy graphics class for simulation
    class graphics:
        class Font:
            def __init__(self):
                pass
        class Color:
            def __init__(self, r, g, b):
                pass
        @staticmethod
        def DrawText(canvas, font, x, y, color, text):
            pass


class DisplayRenderer:
    """Renders KEXP data to RGB LED matrix display"""

    def __init__(self, config):
        self.config = config
        self.matrix = None
        self.canvas = None
        self.font = None
        self.current_scroll_pos = 0
        self.scroll_counter = 0  # Counter for slower scrolling
        self.last_play_id = None

        if MATRIX_AVAILABLE:
            self._init_matrix()
            self._load_fonts()
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
        options.disable_hardware_pulsing = True  # Better image quality

        self.matrix = RGBMatrix(options=options)
        # Create canvas once and reuse it
        self.canvas = self.matrix.CreateFrameCanvas()

        logger.info(f"Matrix initialized: {options.cols}x{options.rows}")

    def _load_fonts(self):
        """Load fonts for matrix display"""
        if not MATRIX_AVAILABLE:
            return

        logger.info("Attempting to load fonts...")
        font_loaded = False

        try:
            # Use absolute paths since we run as root
            font_paths = [
                "/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf",
                "/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf",
                "/home/pi/rpi-rgb-led-matrix/fonts/6x9.bdf",
                "/home/pi/rpi-rgb-led-matrix/fonts/5x8.bdf",
            ]

            for font_path in font_paths:
                try:
                    logger.info(f"Trying to load font from: {font_path}")
                    test_font = graphics.Font()
                    test_font.LoadFont(font_path)
                    self.font = test_font
                    logger.info(f"SUCCESS: Loaded font from {font_path}")
                    font_loaded = True
                    break
                except Exception as font_error:
                    logger.warning(f"Failed to load font {font_path}: {font_error}")
                    continue

            if not font_loaded:
                logger.error("=" * 60)
                logger.error("CRITICAL: Could not load any bitmap font!")
                logger.error("Text will NOT display on the matrix!")
                logger.error("Font paths tried:")
                for path in font_paths:
                    logger.error(f"  - {path}")
                logger.error("=" * 60)
                self.font = graphics.Font()
        except Exception as e:
            logger.error(f"Fatal error loading fonts: {e}")
            self.font = graphics.Font()

    def render_now_playing(self, play_data):
        """
        Render the currently playing track information

        Args:
            play_data: Dictionary containing artist, song, show info
        """
        if not MATRIX_AVAILABLE:
            self._simulate_display(play_data)
            return

        if not play_data:
            return

        try:
            # Check if this is a new track
            play_id = f"{play_data.get('artist', '')}:{play_data.get('song', '')}"
            if play_id != self.last_play_id:
                self.last_play_id = play_id
                self.current_scroll_pos = self.matrix.width
                self.scroll_counter = 0

            # Clear the canvas for this frame (reuse existing canvas)
            self.canvas.Clear()

            # Ensure font is loaded
            if not self.font:
                logger.warning("Font not loaded, attempting to reload")
                self._load_fonts()
                if not self.font:
                    logger.error("Cannot render without font")
                    return

            # Get color scheme based on current show
            show_name = play_data.get('show_name', '')
            try:
                color_scheme = get_color_scheme_for_show(show_name)
            except Exception as e:
                logger.error(f"Error getting color scheme: {e}")
                # Fallback to default colors
                from display.color_schemes import COLOR_SCHEMES
                color_scheme = COLOR_SCHEMES['indie_rock']

            # Define colors from scheme
            artist_color = graphics.Color(*color_scheme.artist)
            song_color = graphics.Color(*color_scheme.song)
            info_color = graphics.Color(*color_scheme.info)

            # Check if this is an airbreak
            play_type = play_data.get('play_type', '')
            is_airbreak = play_type == 'airbreak'

            if is_airbreak:
                # Show program/DJ info during airbreaks
                display_show_name = str(play_data.get('show_name', 'KEXP'))
                host_name = str(play_data.get('host_name', ''))

                # Draw show name (top line)
                show_width = len(display_show_name) * 6
                if show_width > self.matrix.width:
                    x_pos = self.current_scroll_pos
                    graphics.DrawText(self.canvas, self.font, x_pos, 8, artist_color, display_show_name)
                    # Scroll at moderate speed - advance every 2 frames
                    self.scroll_counter += 1
                    if self.scroll_counter >= 2:
                        self.current_scroll_pos -= 1
                        self.scroll_counter = 0
                    # Reset when completely off screen
                    if self.current_scroll_pos < -show_width:
                        self.current_scroll_pos = self.matrix.width
                else:
                    x_pos = max(0, (self.matrix.width - show_width) // 2)
                    graphics.DrawText(self.canvas, self.font, x_pos, 8, artist_color, display_show_name)

                # Draw host name (middle line) if available
                if host_name:
                    host_width = len(host_name) * 6
                    if host_width > self.matrix.width:
                        # Truncate if too long
                        max_chars = self.matrix.width // 6
                        host_name = host_name[:max_chars]
                    graphics.DrawText(self.canvas, self.font, 2, 18, song_color, host_name)
                else:
                    graphics.DrawText(self.canvas, self.font, 2, 18, song_color, "Now Playing...")

                # Show station ID at bottom
                graphics.DrawText(self.canvas, self.font, 2, 28, info_color, "90.3 FM")
            else:
                # Normal track display
                artist = str(play_data.get('artist', 'Unknown'))
                song = str(play_data.get('song', 'Unknown'))
                show_name_display = str(play_data.get('show_name', 'KEXP 90.3'))

                # Calculate text width for scrolling
                artist_width = len(artist) * 6
                song_width = len(song) * 6
                show_width = len(show_name_display) * 6

                # Determine if we need to scroll (any line is too long)
                needs_scrolling = (artist_width > self.matrix.width or 
                                 song_width > self.matrix.width or 
                                 show_width > self.matrix.width)

                # Position for artist (top line, y=8)
                if artist_width > self.matrix.width:
                    # Scroll the artist name
                    x_pos = self.current_scroll_pos
                    graphics.DrawText(self.canvas, self.font, x_pos, 8, artist_color, artist)
                else:
                    # Center the artist name if it fits
                    x_pos = max(0, (self.matrix.width - artist_width) // 2)
                    graphics.DrawText(self.canvas, self.font, x_pos, 8, artist_color, artist)

                # Position for song (middle line, y=18)
                if song_width > self.matrix.width:
                    # Use same scroll position for consistency
                    x_pos = self.current_scroll_pos
                    graphics.DrawText(self.canvas, self.font, x_pos, 18, song_color, song)
                else:
                    x_pos = max(0, (self.matrix.width - song_width) // 2)
                    graphics.DrawText(self.canvas, self.font, x_pos, 18, song_color, song)

                # Position for show name (bottom line, y=28) - CHANGED FROM ALBUM
                if show_width > self.matrix.width:
                    # Scroll the show name using same scroll position
                    x_pos = self.current_scroll_pos
                    graphics.DrawText(self.canvas, self.font, x_pos, 28, info_color, show_name_display)
                else:
                    # Center the show name if it fits
                    x_pos = max(0, (self.matrix.width - show_width) // 2)
                    graphics.DrawText(self.canvas, self.font, x_pos, 28, info_color, show_name_display)

                # Update scroll position if anything needs scrolling
                if needs_scrolling:
                    # Scroll at moderate speed - advance every 2 frames
                    self.scroll_counter += 1
                    if self.scroll_counter >= 2:
                        self.current_scroll_pos -= 1
                        self.scroll_counter = 0
                    # Reset when completely off screen (use the largest width)
                    max_width = max(artist_width, song_width, show_width)
                    if self.current_scroll_pos < -max_width:
                        self.current_scroll_pos = self.matrix.width

            # Swap buffer - this is atomic and thread-safe
            self.canvas = self.matrix.SwapOnVSync(self.canvas)

        except Exception as e:
            logger.error(f"Error rendering display: {e}", exc_info=True)

    def _simulate_display(self, play_data):
        """Simulate display output when matrix is not available"""
        logger.info("=" * 60)
        logger.info(f"NOW PLAYING:")
        logger.info(f"  Artist: {play_data.get('artist', 'Unknown')}")
        logger.info(f"  Song:   {play_data.get('song', 'Unknown')}")
        logger.info(f"  Show:   {play_data.get('show_name', 'KEXP')}")
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
