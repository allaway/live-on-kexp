#!/usr/bin/env python3
"""
Utility script to verify KEXP show names from the API
This helps identify which shows in color_schemes.py are real vs made up
"""

import time
from collections import Counter
from kexp.api_client import KEXPClient


def main():
    """Fetch recent plays and identify actual show names"""
    print("KEXP Show Verification Utility")
    print("=" * 70)
    print("This script fetches recent plays from the KEXP API to identify")
    print("actual show names that are currently broadcasting.")
    print("=" * 70)
    print()

    client = KEXPClient()

    # Fetch a large sample of recent plays
    print("Fetching recent plays from KEXP API...")
    print("(This may take a minute...)")
    print()

    recent_plays = client.get_recent_plays(limit=200)

    if not recent_plays:
        print("ERROR: Could not fetch plays from API")
        print("Please check your internet connection and try again")
        return 1

    print(f"Successfully fetched {len(recent_plays)} recent plays")
    print()

    # Collect all show names
    show_ids = set()
    show_names = []

    for play in recent_plays:
        show_id = play.get('show')
        if show_id and show_id not in show_ids:
            show_ids.add(show_id)

            # Fetch show details
            show_details = client.get_show_details(show_id)
            if show_details:
                show_name = show_details.get('program_name', '')
                if show_name:
                    show_names.append(show_name)
                    print(f"  Found: {show_name}")

            # Be nice to the API
            time.sleep(0.2)

    print()
    print("=" * 70)
    print(f"SUMMARY: Found {len(show_names)} unique shows")
    print("=" * 70)
    print()

    # Count occurrences
    show_counter = Counter(show_names)

    print("Active KEXP Shows (sorted by frequency):")
    print("-" * 70)
    for show_name, count in show_counter.most_common():
        print(f"  {show_name:50} ({count} plays)")

    print()
    print("=" * 70)
    print("CURRENT COLOR SCHEMES IN color_schemes.py:")
    print("=" * 70)

    # Load current show mappings
    from display.color_schemes import SHOW_COLOR_MAPPING

    current_shows = set(SHOW_COLOR_MAPPING.keys())
    actual_shows = set(show_names)

    print()
    print("Shows in color_schemes.py that WERE FOUND in API:")
    print("-" * 70)
    found_shows = sorted(current_shows & actual_shows)
    for show in found_shows:
        print(f"  ✓ {show}")

    print()
    print("Shows in color_schemes.py that were NOT FOUND in API:")
    print("-" * 70)
    print("(These may be made up, retired, or just not recently aired)")
    not_found = sorted(current_shows - actual_shows)
    for show in not_found:
        print(f"  ✗ {show}")

    print()
    print("Shows in API that are NOT in color_schemes.py:")
    print("-" * 70)
    print("(Consider adding color schemes for these shows)")
    missing = sorted(actual_shows - current_shows)
    for show in missing:
        print(f"  + {show}")

    print()
    print("=" * 70)
    print("Python list of actual show names for reference:")
    print("=" * 70)
    print(sorted(show_names))

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
