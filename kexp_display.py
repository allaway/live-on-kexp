#!/usr/bin/env python3
"""
KEXP Now Playing Display
Main application for displaying current show and now playing on RGB LED matrix
"""

import time
import logging
from display.renderer import DisplayRenderer
from kexp.api_client import KEXPClient
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class KEXPDisplay:
    def __init__(self, config):
        self.config = config
        self.kexp_client = KEXPClient()
        self.renderer = DisplayRenderer(config)
        self.current_play = None

    def update_display(self):
        """Fetch latest data from KEXP and update display"""
        try:
            # Get current play (now playing)
            play_data = self.kexp_client.get_current_play()

            if play_data and play_data != self.current_play:
                self.current_play = play_data
                logger.info(f"Now playing: {play_data['artist']} - {play_data['song']}")

                # Update display with new data
                self.renderer.render_now_playing(play_data)

        except Exception as e:
            logger.error(f"Error updating display: {e}")

    def run(self):
        """Main loop"""
        logger.info("KEXP Display started")

        try:
            while True:
                self.update_display()
                time.sleep(self.config.update_interval)

        except KeyboardInterrupt:
            logger.info("KEXP Display stopped by user")
        except Exception as e:
            logger.error(f"Fatal error: {e}")
        finally:
            self.renderer.cleanup()


def main():
    config = Config()
    display = KEXPDisplay(config)
    display.run()


if __name__ == "__main__":
    main()
