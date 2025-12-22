#!/usr/bin/env python3
"""
Test script to display KEXP logo on the LED matrix
Run this to verify the logo appears correctly on the hardware
"""

import time
import sys
from display.renderer import DisplayRenderer
from config import Config

def main():
    """Display the KEXP logo for testing"""
    print("KEXP Logo Test")
    print("=" * 60)
    print("This will display the KEXP logo on the LED matrix for 10 seconds")
    print("Press Ctrl+C to exit early")
    print("=" * 60)

    config = Config()
    renderer = DisplayRenderer(config)

    try:
        print("\nDisplaying KEXP logo...")

        # Draw the logo
        renderer._draw_kexp_logo()

        # Swap the buffer to show it
        if renderer.canvas and renderer.matrix:
            renderer.canvas = renderer.matrix.SwapOnVSync(renderer.canvas)

        # Keep it displayed for 10 seconds
        print("Logo should now be visible on the display")
        print("Waiting 10 seconds...")
        time.sleep(10)

        print("\nTest complete!")

    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\nError during test: {e}", exc_info=True)
    finally:
        renderer.cleanup()
        print("Display cleaned up")

if __name__ == "__main__":
    sys.exit(main())
