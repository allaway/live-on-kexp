"""
Scrolling text renderer for long text that doesn't fit on display
"""

import time
from PIL import Image, ImageDraw, ImageFont
import logging

logger = logging.getLogger(__name__)


class ScrollingText:
    """Handles horizontal scrolling of text that's too long for the display"""

    def __init__(self, text, font, color, width, height, y_position=0):
        """
        Initialize scrolling text

        Args:
            text: Text to scroll
            font: PIL ImageFont to use
            color: RGB color tuple
            width: Display width in pixels
            height: Display height in pixels
            y_position: Vertical position for the text
        """
        self.text = text
        self.font = font
        self.color = color
        self.display_width = width
        self.display_height = height
        self.y_position = y_position

        # Measure text width
        dummy_img = Image.new('RGB', (1, 1))
        dummy_draw = ImageDraw.Draw(dummy_img)

        # Get text bounding box
        bbox = dummy_draw.textbbox((0, 0), text, font=font)
        self.text_width = bbox[2] - bbox[0]
        self.text_height = bbox[3] - bbox[1]

        self.x_offset = 0
        self.needs_scrolling = self.text_width > width

    def reset(self):
        """Reset scroll position to beginning"""
        self.x_offset = 0

    def render_frame(self, scroll_offset=None):
        """
        Render a single frame of the scrolling text

        Args:
            scroll_offset: Optional override for scroll position

        Returns:
            PIL Image of the rendered text
        """
        image = Image.new('RGB', (self.display_width, self.display_height))
        draw = ImageDraw.Draw(image)

        if scroll_offset is not None:
            x_pos = scroll_offset
        else:
            x_pos = self.x_offset

        # Draw the text at the current position
        draw.text((x_pos, self.y_position), self.text, fill=self.color, font=self.font)

        # If scrolling, also draw the text wrapped around
        if self.needs_scrolling and x_pos < 0:
            # Draw the text again after the first instance
            draw.text((x_pos + self.text_width + 20, self.y_position),
                     self.text, fill=self.color, font=self.font)

        return image

    def scroll_step(self, pixels=1):
        """
        Advance the scroll by the specified number of pixels

        Args:
            pixels: Number of pixels to scroll

        Returns:
            True if still scrolling, False if at end
        """
        if not self.needs_scrolling:
            return False

        self.x_offset -= pixels

        # Reset when text has completely scrolled off
        if self.x_offset < -(self.text_width + 20):
            self.x_offset = self.display_width

        return True

    def get_static_frame(self):
        """Get a frame with text centered (for non-scrolling text)"""
        image = Image.new('RGB', (self.display_width, self.display_height))
        draw = ImageDraw.Draw(image)

        # Center the text if it fits
        if not self.needs_scrolling:
            x_pos = (self.display_width - self.text_width) // 2
        else:
            x_pos = 2  # Small padding if scrolling is needed

        draw.text((x_pos, self.y_position), self.text, fill=self.color, font=self.font)

        return image
