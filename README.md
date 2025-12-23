# KEXP Now Playing Display

A Raspberry Pi RGB LED matrix display that shows the current show and now playing track from KEXP radio station.

## Features

- Real-time display of currently playing track from KEXP
- Shows artist, song title, and album information
- Scrolling text support for long track/artist names
- Configurable display settings and update intervals
- Automatic updates via KEXP's public API

## Hardware Requirements

- Raspberry Pi (tested on Pi Zero 2 W)
- RGB LED Matrix display 
- Adafruit RGB Matrix Bonnet HAT 
- Power supply for the LED matrix

This project uses the same hardware setup as [FlightTracker](https://github.com/ColinWaddell/FlightTracker/).

## Installation

### 1. Install RGB Matrix Library

First, install the rpi-rgb-led-matrix library:

```bash
cd ~
git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
cd rpi-rgb-led-matrix
make
cd bindings/python
sudo pip3 install -e .
```

### 2. Clone This Repository

```bash
cd ~
git clone https://github.com/yourusername/live-on-kexp.git
cd live-on-kexp
```

### 3. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Configure Settings

Copy the example environment file and adjust settings:

```bash
cp .env.example .env
nano .env
```

Key settings to configure:
- `MATRIX_ROWS` and `MATRIX_COLS` - Your display dimensions
- `BRIGHTNESS` - Display brightness (0-100)
- `UPDATE_INTERVAL` - How often to check for new tracks (seconds)
- `GPIO_MAPPING` - Usually 'adafruit-hat' for the RGB Matrix Bonnet

## Usage

### Test Mode (No Hardware Required)

You can test the application without hardware using simulation mode:

```bash
python3 kexp_display.py
```

If the RGB matrix library is not detected, it will automatically run in simulation mode and log the now playing information to the console.

### Test the API

To test the KEXP API connection:

```bash
python3 test_api.py
```

### Test Color Schemes

To cycle through all show color schemes and verify them on your display:

```bash
# Auto-cycle through all shows (5 seconds each)
sudo python3 test_colors.py

# Auto-cycle with custom delay (10 seconds per show)
sudo python3 test_colors.py --delay 10

# Manual mode with keyboard controls (space=next, b=previous, q=quit)
sudo python3 test_colors.py --manual
```

This is useful for:
- Verifying color palettes look good on your specific LED matrix
- Checking all shows have correct color schemes configured
- Testing display functionality without waiting for KEXP API data

### Run on Hardware

To run on actual RGB matrix hardware, you need sudo privileges:

```bash
sudo python3 kexp_display.py
```

### Run as a Service

To run the display automatically on boot, install the systemd service:

```bash
sudo cp kexp-display.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable kexp-display
sudo systemctl start kexp-display
```

Check service status:

```bash
sudo systemctl status kexp-display
```

View logs:

```bash
sudo journalctl -u kexp-display -f
```

## Configuration Options

All configuration can be done via the `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `UPDATE_INTERVAL` | Seconds between API checks | 10 |
| `MATRIX_ROWS` | Matrix height in pixels | 32 |
| `MATRIX_COLS` | Matrix width in pixels | 64 |
| `BRIGHTNESS` | Display brightness (0-100) | 50 |
| `GPIO_MAPPING` | Hardware mapping type | adafruit-hat |
| `GPIO_SLOWDOWN` | GPIO slowdown for flickering | 4 |

## Project Structure

```
live-on-kexp/
├── kexp_display.py          # Main application
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── test_api.py             # API testing script
├── kexp/
│   ├── __init__.py
│   └── api_client.py       # KEXP API client
├── display/
│   ├── __init__.py
│   ├── renderer.py         # RGB matrix renderer
│   └── color_schemes.py    # Color schemes for shows
└── kexp-display.service    # Systemd service file
```

## KEXP API

This project uses the [KEXP public API v2](https://api.kexp.org/v2/) to fetch currently playing tracks and show information.

API endpoints used:
- `https://api.kexp.org/v2/plays/` - Get recent plays (now playing)
- `https://api.kexp.org/v2/shows/{id}/` - Get show details

## Color Schemes

Each KEXP show has a unique, carefully crafted color palette that reflects its musical style and vibe. The display uses three colors for each show:
- **Artist Color**: Used for the artist name (top line)
- **Song Color**: Used for the song title (middle line)
- **Info Color**: Used for show name or station ID (bottom line)

| Show | Artist Color | Song Color | Info Color |
|------|--------------|------------|------------|
| **Early** | ![#FFB6C1](https://img.shields.io/badge/-FFB6C1-FFB6C1?style=flat-square) | ![#FFDAB9](https://img.shields.io/badge/-FFDAB9-FFDAB9?style=flat-square&labelColor=FFDAB9) | ![#FFEFD5](https://img.shields.io/badge/-FFEFD5-FFEFD5?style=flat-square&labelColor=FFEFD5) |
| **The Morning Show** | ![#FF7F50](https://img.shields.io/badge/-FF7F50-FF7F50?style=flat-square) | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) | ![#87CEFA](https://img.shields.io/badge/-87CEFA-87CEFA?style=flat-square&labelColor=87CEFA) |
| **The Midday Show** | ![#FFFF00](https://img.shields.io/badge/-FFFF00-FFFF00?style=flat-square&labelColor=FFFF00) | ![#FFA500](https://img.shields.io/badge/-FFA500-FFA500?style=flat-square) | ![#87CEFA](https://img.shields.io/badge/-87CEFA-87CEFA?style=flat-square&labelColor=87CEFA) |
| **The Afternoon Show** | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) | ![#4682B4](https://img.shields.io/badge/-4682B4-4682B4?style=flat-square) | ![#FFC34D](https://img.shields.io/badge/-FFC34D-FFC34D?style=flat-square&labelColor=FFC34D) |
| **Drive Time** | ![#CD1C00](https://img.shields.io/badge/-CD1C00-CD1C00?style=flat-square) | ![#FFC600](https://img.shields.io/badge/-FFC600-FFC600?style=flat-square) | ![#00B354](https://img.shields.io/badge/-00B354-00B354?style=flat-square) |
| **Midnight in a Perfect World** | ![#8A2BE2](https://img.shields.io/badge/-8A2BE2-8A2BE2?style=flat-square) | ![#00BFFF](https://img.shields.io/badge/-00BFFF-00BFFF?style=flat-square) | ![#BA55D3](https://img.shields.io/badge/-BA55D3-BA55D3?style=flat-square) |
| **Mechanical Breakdown** | ![#C0C0C0](https://img.shields.io/badge/-C0C0C0-C0C0C0?style=flat-square) | ![#FF6347](https://img.shields.io/badge/-FF6347-FF6347?style=flat-square) | ![#00CED1](https://img.shields.io/badge/-00CED1-00CED1?style=flat-square&labelColor=00CED1) |
| **Astral Plane** | ![#8A2BE2](https://img.shields.io/badge/-8A2BE2-8A2BE2?style=flat-square) | ![#FF00FF](https://img.shields.io/badge/-FF00FF-FF00FF?style=flat-square) | ![#00BFFF](https://img.shields.io/badge/-00BFFF-00BFFF?style=flat-square) |
| **Audioasis** | ![#547067](https://img.shields.io/badge/-547067-547067?style=flat-square) | ![#40595E](https://img.shields.io/badge/-40595E-40595E?style=flat-square) | ![#8EA091](https://img.shields.io/badge/-8EA091-8EA091?style=flat-square) |
| **Wo' Pop** | ![#FF69B4](https://img.shields.io/badge/-FF69B4-FF69B4?style=flat-square) | ![#40E0D0](https://img.shields.io/badge/-40E0D0-40E0D0?style=flat-square&labelColor=40E0D0) | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) |
| **El Sonido** | ![#FF4500](https://img.shields.io/badge/-FF4500-FF4500?style=flat-square) | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) | ![#9400D3](https://img.shields.io/badge/-9400D3-9400D3?style=flat-square) |
| **Eastern Echoes** | ![#DC143C](https://img.shields.io/badge/-DC143C-DC143C?style=flat-square) | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) | ![#008080](https://img.shields.io/badge/-008080-008080?style=flat-square) |
| **Sounds of Survivance** | ![#8B4513](https://img.shields.io/badge/-8B4513-8B4513?style=flat-square) | ![#D2B48C](https://img.shields.io/badge/-D2B48C-D2B48C?style=flat-square&labelColor=D2B48C) | ![#87CEEB](https://img.shields.io/badge/-87CEEB-87CEEB?style=flat-square&labelColor=87CEEB) |
| **The Continent** | ![#FF8C00](https://img.shields.io/badge/-FF8C00-FF8C00?style=flat-square) | ![#228B22](https://img.shields.io/badge/-228B22-228B22?style=flat-square) | ![#DC143C](https://img.shields.io/badge/-DC143C-DC143C?style=flat-square) |
| **Positive Vibrations** | ![#FCD116](https://img.shields.io/badge/-FCD116-FCD116?style=flat-square&labelColor=FCD116) | ![#009B3A](https://img.shields.io/badge/-009B3A-009B3A?style=flat-square) | ![#CE1126](https://img.shields.io/badge/-CE1126-CE1126?style=flat-square) |
| **Street Sounds** | ![#FF1493](https://img.shields.io/badge/-FF1493-FF1493?style=flat-square) | ![#00FFFF](https://img.shields.io/badge/-00FFFF-00FFFF?style=flat-square&labelColor=00FFFF) | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) |
| **Sunday Soul** | ![#B8860B](https://img.shields.io/badge/-B8860B-B8860B?style=flat-square) | ![#DB7093](https://img.shields.io/badge/-DB7093-DB7093?style=flat-square) | ![#FFDAB9](https://img.shields.io/badge/-FFDAB9-FFDAB9?style=flat-square&labelColor=FFDAB9) |
| **Expansions** | ![#8A629A](https://img.shields.io/badge/-8A629A-8A629A?style=flat-square) | ![#5F9EA0](https://img.shields.io/badge/-5F9EA0-5F9EA0?style=flat-square) | ![#D2691E](https://img.shields.io/badge/-D2691E-D2691E?style=flat-square) |
| **Jazz Theatre** | ![#8A629A](https://img.shields.io/badge/-8A629A-8A629A?style=flat-square) | ![#5F9EA0](https://img.shields.io/badge/-5F9EA0-5F9EA0?style=flat-square) | ![#D2691E](https://img.shields.io/badge/-D2691E-D2691E?style=flat-square) |
| **The Roadhouse** | ![#8B4513](https://img.shields.io/badge/-8B4513-8B4513?style=flat-square) | ![#D2691E](https://img.shields.io/badge/-D2691E-D2691E?style=flat-square) | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) |
| **Seek & Destroy** | ![#FF0000](https://img.shields.io/badge/-FF0000-FF0000?style=flat-square) | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) | ![#808080](https://img.shields.io/badge/-808080-808080?style=flat-square) |
| **Sonic Reducer** | ![#FFFF00](https://img.shields.io/badge/-FFFF00-FFFF00?style=flat-square&labelColor=FFFF00) | ![#FF00FF](https://img.shields.io/badge/-FF00FF-FF00FF?style=flat-square) | ![#00FF00](https://img.shields.io/badge/-00FF00-00FF00?style=flat-square&labelColor=00FF00) |
| **90.TEEN** | ![#FF007F](https://img.shields.io/badge/-FF007F-FF007F?style=flat-square) | ![#00FFFF](https://img.shields.io/badge/-00FFFF-00FFFF?style=flat-square&labelColor=00FFFF) | ![#FFFF00](https://img.shields.io/badge/-FFFF00-FFFF00?style=flat-square&labelColor=FFFF00) |
| **Pacific Notions** | ![#B0C4DE](https://img.shields.io/badge/-B0C4DE-B0C4DE?style=flat-square&labelColor=B0C4DE) | ![#C6D5D8](https://img.shields.io/badge/-C6D5D8-C6D5D8?style=flat-square) | ![#A9A9A9](https://img.shields.io/badge/-A9A9A9-A9A9A9?style=flat-square) |
| **Vinelands** | ![#800020](https://img.shields.io/badge/-800020-800020?style=flat-square) | ![#6B8E23](https://img.shields.io/badge/-6B8E23-6B8E23?style=flat-square) | ![#DAA520](https://img.shields.io/badge/-DAA520-DAA520?style=flat-square) |
| **Live on KEXP** | ![#EAE0F1](https://img.shields.io/badge/-EAE0F1-EAE0F1?style=flat-square) | ![#F8C762](https://img.shields.io/badge/-F8C762-F8C762?style=flat-square) | ![#D38CFB](https://img.shields.io/badge/-D38CFB-D38CFB?style=flat-square) |
| **Sound & Vision** | ![#FF1493](https://img.shields.io/badge/-FF1493-FF1493?style=flat-square) | ![#00FF7F](https://img.shields.io/badge/-00FF7F-00FF7F?style=flat-square&labelColor=00FF7F) | ![#FFA500](https://img.shields.io/badge/-FFA500-FFA500?style=flat-square) |
| **Variety Mix** | ![#FF6347](https://img.shields.io/badge/-FF6347-FF6347?style=flat-square) | ![#40E0D0](https://img.shields.io/badge/-40E0D0-40E0D0?style=flat-square&labelColor=40E0D0) | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) |
| **KEXP Default** | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) | ![#64C8FF](https://img.shields.io/badge/-64C8FF-64C8FF?style=flat-square) | ![#FFC864](https://img.shields.io/badge/-FFC864-FFC864?style=flat-square&labelColor=FFC864) |

*KEXP Default is used for shows without a specific color scheme or when show information is unavailable.*
## Troubleshooting

### Display is flickering

Try adjusting the `GPIO_SLOWDOWN` parameter in the `.env` file - setting this at 2 or 3 seems best for the Pi Zero 2W.

## Credits

- KEXP for their public API
- [FlightTracker](https://github.com/ColinWaddell/FlightTracker/) for hardware and software inspiration
- [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) for the display library

## License

GPL-3.0 License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
