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

    def fetch_new_data(self):
        """Fetch latest data from KEXP API"""
        try:
            # Get current play (now playing)
            play_data = self.kexp_client.get_current_play()

            if play_data and play_data != self.current_play:
                self.current_play = play_data
                logger.info(f"Now playing: {play_data['artist']} - {play_data['song']}")

        except Exception as e:
            logger.error(f"Error fetching data: {e}")

    def run(self):
        """Main loop"""
        logger.info("KEXP Display started")

        # Fetch initial data
        self.fetch_new_data()

        last_fetch_time = time.time()
        frame_delay = 0.05  # 20 FPS for smooth scrolling

        try:
            while True:
                # Fetch new data periodically
                current_time = time.time()
                if current_time - last_fetch_time >= self.config.update_interval:
                    self.fetch_new_data()
                    last_fetch_time = current_time

                # Render current data (for scrolling animation)
                if self.current_play:
                    self.renderer.render_now_playing(self.current_play)

                time.sleep(frame_delay)

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
