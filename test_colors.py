#!/usr/bin/env python3
"""
Color Scheme Test Script
Cycles through all KEXP show color palettes for visual verification on the LED matrix
"""

import time
import sys
import logging
from display.renderer import DisplayRenderer
from display.color_schemes import SHOW_COLOR_MAPPING
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Try to import keyboard input handling
try:
    import tty
    import termios
    import select
    KEYBOARD_AVAILABLE = True
except ImportError:
    KEYBOARD_AVAILABLE = False
    logger.warning("Keyboard input not available, using auto-cycle only")


class ColorTester:
    """Test all color schemes on the LED display"""

    def __init__(self, auto_cycle=True, cycle_delay=5):
        self.config = Config()
        self.renderer = DisplayRenderer(self.config)
        self.auto_cycle = auto_cycle
        self.cycle_delay = cycle_delay

        # Get all shows from SHOW_COLOR_MAPPING
        self.shows = sorted(SHOW_COLOR_MAPPING.keys())
        # Add default at the end
        self.shows.append('KEXP Default')

        self.current_index = 0

    def get_keyboard_input(self, timeout=0.1):
        """Non-blocking keyboard input (Unix/Linux only)"""
        if not KEYBOARD_AVAILABLE:
            return None

        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            if select.select([sys.stdin], [], [], timeout)[0]:
                return sys.stdin.read(1)
            return None
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    def display_show(self, show_name):
        """Display sample text for a given show"""
        # Create sample play data
        play_data = {
            'artist': 'Test Artist Name',
            'song': 'Test Song Title',
            'show_name': show_name if show_name != 'KEXP Default' else '',
            'album': 'Test Album',
            'play_type': 'trackplay'
        }

        logger.info(f"Displaying: {show_name}")
        self.renderer.render_now_playing(play_data)

    def run_manual_mode(self):
        """Run in manual mode with keyboard controls"""
        print("\n" + "="*60)
        print("Color Scheme Tester - Manual Mode")
        print("="*60)
        print("Controls:")
        print("  [SPACE] or [ENTER] - Next show")
        print("  [b] - Previous show")
        print("  [a] - Toggle auto-cycle")
        print("  [q] - Quit")
        print("="*60 + "\n")

        auto_cycle_enabled = self.auto_cycle
        last_cycle_time = time.time()

        try:
            while True:
                # Display current show
                show_name = self.shows[self.current_index]
                self.display_show(show_name)

                # Print current show info
                print(f"\r[{self.current_index + 1}/{len(self.shows)}] {show_name}", end='', flush=True)

                # Check for keyboard input
                key = self.get_keyboard_input(timeout=0.1)

                if key:
                    if key.lower() == 'q':
                        print("\n\nExiting...")
                        break
                    elif key == ' ' or key == '\n':
                        # Next show
                        self.current_index = (self.current_index + 1) % len(self.shows)
                        print()  # New line for next show
                    elif key.lower() == 'b':
                        # Previous show
                        self.current_index = (self.current_index - 1) % len(self.shows)
                        print()  # New line for next show
                    elif key.lower() == 'a':
                        # Toggle auto-cycle
                        auto_cycle_enabled = not auto_cycle_enabled
                        status = "enabled" if auto_cycle_enabled else "disabled"
                        print(f"\nAuto-cycle {status}")
                        last_cycle_time = time.time()

                # Auto-cycle if enabled
                if auto_cycle_enabled:
                    current_time = time.time()
                    if current_time - last_cycle_time >= self.cycle_delay:
                        self.current_index = (self.current_index + 1) % len(self.shows)
                        last_cycle_time = current_time
                        print()  # New line for next show

                time.sleep(0.05)  # Small delay to prevent CPU spinning

        except KeyboardInterrupt:
            print("\n\nStopped by user")
        finally:
            self.renderer.cleanup()

    def run_auto_cycle(self):
        """Run in auto-cycle mode only"""
        print("\n" + "="*60)
        print("Color Scheme Tester - Auto-Cycle Mode")
        print("="*60)
        print(f"Cycling through {len(self.shows)} shows")
        print(f"Display time: {self.cycle_delay} seconds per show")
        print("Press Ctrl+C to stop")
        print("="*60 + "\n")

        try:
            while True:
                show_name = self.shows[self.current_index]
                print(f"[{self.current_index + 1}/{len(self.shows)}] {show_name}")

                self.display_show(show_name)

                # Wait for the cycle delay
                time.sleep(self.cycle_delay)

                # Move to next show
                self.current_index = (self.current_index + 1) % len(self.shows)

        except KeyboardInterrupt:
            print("\n\nStopped by user")
        finally:
            self.renderer.cleanup()

    def run(self):
        """Run the color tester"""
        if KEYBOARD_AVAILABLE and not self.auto_cycle:
            self.run_manual_mode()
        else:
            self.run_auto_cycle()


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Test KEXP color schemes on LED display',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Auto-cycle through shows (5 seconds each)
  python3 test_colors.py

  # Auto-cycle with custom delay
  python3 test_colors.py --delay 10

  # Manual mode with keyboard controls
  python3 test_colors.py --manual
        """
    )

    parser.add_argument(
        '--manual',
        action='store_true',
        help='Enable manual mode with keyboard controls (default: auto-cycle)'
    )

    parser.add_argument(
        '--delay',
        type=int,
        default=5,
        help='Seconds to display each show in auto-cycle mode (default: 5)'
    )

    args = parser.parse_args()

    tester = ColorTester(
        auto_cycle=not args.manual,
        cycle_delay=args.delay
    )

    tester.run()


if __name__ == '__main__':
    main()
