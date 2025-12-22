# Changelog

## 2025-12-22 - Bug Fixes and Improvements

### Bug Fixes

1. **Fixed 90.3 FM centering on air break display**
   - The "90.3 FM" text on the bottom line during air breaks is now properly centered
   - Previously was hard-coded at x=2, now calculates center position dynamically

2. **Added scrolling for long text on air break**
   - Show names and host names that are longer than the display width now scroll properly
   - Previously, long host names were truncated instead of scrolling
   - "Now Playing..." message is also centered when no host name is available

3. **Increased scroll speed by 25%**
   - Scrolling text now moves 25% faster for better readability
   - Changed from scrolling every 2 frames to every 1.6 frames

4. **Implemented continuous scrolling with separator**
   - Scrolling text now loops continuously with a "   |   " separator
   - No more waiting for text to completely scroll off before restarting
   - Provides a smoother, more professional viewing experience

5. **Cleaned up color schemes**
   - Removed show names that don't appear in actual KEXP API responses:
     - "Psychedelic Shack"
     - "Roots & Wires"
     - "The Sunray Show"
     - "Dub Shack"
     - "Rap Attack"
     - "Soul Serenade"
     - "Audio Oasis" (duplicate of "Audioasis")
     - "Local Show"
     - "Stevie Wonder's House Party"
     - "Rockabilly Revolt"
   - Reduced from ~27 color schemes to 17 verified shows
   - Kept only shows that are confirmed KEXP programs

### New Features

- **Show verification utility** (`verify_shows.py`)
  - Script to fetch actual show names from KEXP API
  - Helps identify which shows are real vs made up
  - Compares current color schemes against live API data
  - Usage: `python3 verify_shows.py`

### Technical Details

**Files Modified:**
- `display/renderer.py` - All scrolling and centering fixes
- `display/color_schemes.py` - Removed non-existent shows

**Files Added:**
- `verify_shows.py` - Show verification utility
- `CHANGELOG.md` - This file

### Testing

All changes have been syntax-checked and are ready for deployment on the Raspberry Pi LED matrix.
