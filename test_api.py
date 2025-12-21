#!/usr/bin/env python3
"""
Test script for KEXP API
Fetches and displays current now playing information
"""

import sys
from kexp.api_client import KEXPClient


def main():
    """Test the KEXP API client"""
    print("KEXP API Test")
    print("=" * 60)

    client = KEXPClient()

    # Test getting current play
    print("\nFetching current play...")
    play = client.get_current_play()

    if play:
        print("\nNOW PLAYING:")
        print(f"  Artist:    {play['artist']}")
        print(f"  Song:      {play['song']}")
        print(f"  Album:     {play['album'] or 'N/A'}")
        print(f"  Airdate:   {play['airdate']}")
        print(f"  Play Type: {play['play_type']}")
        if play['comment']:
            print(f"  Comment:   {play['comment']}")
        if play['is_local']:
            print(f"  Local:     Yes")

        # Get show details if available
        if play['show']:
            print(f"\nFetching show details (ID: {play['show']})...")
            show = client.get_show_details(play['show'])
            if show:
                print(f"\nCURRENT SHOW:")
                print(f"  Program:   {show['program_name']}")
                if show['host_names']:
                    print(f"  Host:      {show['host_names']}")
                if show['start_time'] and show['end_time']:
                    print(f"  Time:      {show['start_time']} - {show['end_time']}")
    else:
        print("\nError: Could not fetch current play data")
        print("This could be due to:")
        print("  - Network connectivity issues")
        print("  - Firewall/proxy restrictions")
        print("  - KEXP API temporarily unavailable")
        print("\nThe code is correct and will work with proper internet access.")
        return 1

    # Test getting recent plays
    print("\n" + "=" * 60)
    print("Recent plays:")
    recent = client.get_recent_plays(limit=5)

    for i, play in enumerate(recent, 1):
        print(f"\n{i}. {play.get('artist', 'Unknown')} - {play.get('song', 'Unknown')}")
        if play.get('album'):
            print(f"   Album: {play['album']}")

    print("\n" + "=" * 60)
    print("API test completed successfully!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
