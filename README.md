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

### Daily Programming

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Early** | Sunrise morning | ![#FFB6C1](https://img.shields.io/badge/-FFB6C1-FFB6C1?style=flat-square) Light Pink | ![#FFDAB9](https://img.shields.io/badge/-FFDAB9-FFDAB9?style=flat-square) Peach | ![#FFEFD5](https://img.shields.io/badge/-FFEFD5-FFEFD5?style=flat-square&labelColor=FFEFD5) Papaya Whip |
| **The Morning Show** | Warm sunrise gradient | ![#FF7F50](https://img.shields.io/badge/-FF7F50-FF7F50?style=flat-square) Coral | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) Gold | ![#87CEEB](https://img.shields.io/badge/-87CEEB-87CEEB?style=flat-square&labelColor=87CEEB) Light Sky Blue |
| **The Midday Show** | Bright midday sun | ![#FFFF00](https://img.shields.io/badge/-FFFF00-FFFF00?style=flat-square&labelColor=FFFF00) Yellow | ![#FFA500](https://img.shields.io/badge/-FFA500-FFA500?style=flat-square) Orange | ![#87CEEB](https://img.shields.io/badge/-87CEEB-87CEEB?style=flat-square&labelColor=87CEEB) Light Sky Blue |
| **The Afternoon Show** | Balanced brightness | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) White | ![#4682B4](https://img.shields.io/badge/-4682B4-4682B4?style=flat-square) Steel Blue | ![#FFC34D](https://img.shields.io/badge/-FFC34D-FFC34D?style=flat-square&labelColor=FFC34D) Amber |
| **Drive Time** | Bold primaries | ![#DC143C](https://img.shields.io/badge/-DC143C-DC143C?style=flat-square) Crimson | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) White | ![#FFA500](https://img.shields.io/badge/-FFA500-FFA500?style=flat-square) Orange |

### Electronic & Dance

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Midnight in a Perfect World** | Deep space electronic | ![#8A2BE2](https://img.shields.io/badge/-8A2BE2-8A2BE2?style=flat-square) Blue Violet | ![#00BFFF](https://img.shields.io/badge/-00BFFF-00BFFF?style=flat-square&labelColor=00BFFF) Deep Sky Blue | ![#BA55D3](https://img.shields.io/badge/-BA55D3-BA55D3?style=flat-square) Medium Orchid |
| **Mechanical Breakdown** | Industrial metallic | ![#C0C0C0](https://img.shields.io/badge/-C0C0C0-C0C0C0?style=flat-square&labelColor=C0C0C0) Silver | ![#FF6347](https://img.shields.io/badge/-FF6347-FF6347?style=flat-square) Tomato Red | ![#00CED1](https://img.shields.io/badge/-00CED1-00CED1?style=flat-square&labelColor=00CED1) Dark Turquoise |
| **Astral Plane** | Cosmic psychedelic | ![#8A2BE2](https://img.shields.io/badge/-8A2BE2-8A2BE2?style=flat-square) Blue Violet | ![#FF00FF](https://img.shields.io/badge/-FF00FF-FF00FF?style=flat-square) Magenta | ![#00BFFF](https://img.shields.io/badge/-00BFFF-00BFFF?style=flat-square&labelColor=00BFFF) Deep Sky Blue |

### World Music

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Audioasis** | Desert palette | ![#CD5C5C](https://img.shields.io/badge/-CD5C5C-CD5C5C?style=flat-square) Indian Red | ![#BDB76B](https://img.shields.io/badge/-BDB76B-BDB76B?style=flat-square&labelColor=BDB76B) Dark Khaki | ![#F4A460](https://img.shields.io/badge/-F4A460-F4A460?style=flat-square) Sandy Brown |
| **Wo' Pop** | Vibrant eclectic | ![#FF69B4](https://img.shields.io/badge/-FF69B4-FF69B4?style=flat-square) Hot Pink | ![#40E0D0](https://img.shields.io/badge/-40E0D0-40E0D0?style=flat-square&labelColor=40E0D0) Turquoise | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) Gold |
| **El Sonido** | Spicy Latin warmth | ![#FF4500](https://img.shields.io/badge/-FF4500-FF4500?style=flat-square) Red-Orange | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) Gold | ![#9400D3](https://img.shields.io/badge/-9400D3-9400D3?style=flat-square) Dark Violet |
| **Eastern Echoes** | Eastern-inspired | ![#DC143C](https://img.shields.io/badge/-DC143C-DC143C?style=flat-square) Crimson Red | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) Gold | ![#008080](https://img.shields.io/badge/-008080-008080?style=flat-square) Teal |
| **Sounds of Survivance** | Earth and sky | ![#8B4513](https://img.shields.io/badge/-8B4513-8B4513?style=flat-square) Saddle Brown | ![#D2B48C](https://img.shields.io/badge/-D2B48C-D2B48C?style=flat-square&labelColor=D2B48C) Tan | ![#87CEEB](https://img.shields.io/badge/-87CEEB-87CEEB?style=flat-square&labelColor=87CEEB) Sky Blue |
| **The Continent** | African vibrant | ![#FF8C00](https://img.shields.io/badge/-FF8C00-FF8C00?style=flat-square) Dark Orange | ![#228B22](https://img.shields.io/badge/-228B22-228B22?style=flat-square) Forest Green | ![#DC143C](https://img.shields.io/badge/-DC143C-DC143C?style=flat-square) Crimson |

### Reggae & Caribbean

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Positive Vibrations** | Rasta colors | ![#FCD116](https://img.shields.io/badge/-FCD116-FCD116?style=flat-square&labelColor=FCD116) Rasta Gold | ![#009B3A](https://img.shields.io/badge/-009B3A-009B3A?style=flat-square) Rasta Green | ![#CE1126](https://img.shields.io/badge/-CE1126-CE1126?style=flat-square) Rasta Red |

### Hip-Hop, R&B & Soul

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Street Sounds** | Urban neon graffiti | ![#FF1493](https://img.shields.io/badge/-FF1493-FF1493?style=flat-square) Deep Pink | ![#00FFFF](https://img.shields.io/badge/-00FFFF-00FFFF?style=flat-square&labelColor=00FFFF) Cyan | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) Gold |
| **Sunday Soul** | Warm vintage soul | ![#B8860B](https://img.shields.io/badge/-B8860B-B8860B?style=flat-square) Dark Goldenrod | ![#DB7093](https://img.shields.io/badge/-DB7093-DB7093?style=flat-square) Pale Violet Red | ![#FFDAB9](https://img.shields.io/badge/-FFDAB9-FFDAB9?style=flat-square) Peach Puff |

### Jazz, Blues & Roots

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Expansions** | Smoky jazz club | ![#D2B48C](https://img.shields.io/badge/-D2B48C-D2B48C?style=flat-square&labelColor=D2B48C) Tan | ![#B0C4DE](https://img.shields.io/badge/-B0C4DE-B0C4DE?style=flat-square&labelColor=B0C4DE) Light Steel Blue | ![#DAA520](https://img.shields.io/badge/-DAA520-DAA520?style=flat-square) Goldenrod |
| **Jazz Theatre** | Smoky jazz club | ![#D2B48C](https://img.shields.io/badge/-D2B48C-D2B48C?style=flat-square&labelColor=D2B48C) Tan | ![#B0C4DE](https://img.shields.io/badge/-B0C4DE-B0C4DE?style=flat-square&labelColor=B0C4DE) Light Steel Blue | ![#DAA520](https://img.shields.io/badge/-DAA520-DAA520?style=flat-square) Goldenrod |
| **The Roadhouse** | Rustic honky tonk | ![#8B4513](https://img.shields.io/badge/-8B4513-8B4513?style=flat-square) Saddle Brown | ![#D2691E](https://img.shields.io/badge/-D2691E-D2691E?style=flat-square) Chocolate | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) Gold |

### Rock, Metal & Punk

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Seek & Destroy** | Aggressive metal | ![#FF0000](https://img.shields.io/badge/-FF0000-FF0000?style=flat-square) Pure Red | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) Pure White | ![#808080](https://img.shields.io/badge/-808080-808080?style=flat-square) Gray |
| **Sonic Reducer** | Punk chaos | ![#FFFF00](https://img.shields.io/badge/-FFFF00-FFFF00?style=flat-square&labelColor=FFFF00) Yellow | ![#FF00FF](https://img.shields.io/badge/-FF00FF-FF00FF?style=flat-square) Magenta | ![#00FF00](https://img.shields.io/badge/-00FF00-00FF00?style=flat-square&labelColor=00FF00) Lime Green |
| **90.TEEN** | Youth energy | ![#FF007F](https://img.shields.io/badge/-FF007F-FF007F?style=flat-square) Bright Pink | ![#00FFFF](https://img.shields.io/badge/-00FFFF-00FFFF?style=flat-square&labelColor=00FFFF) Cyan | ![#FFFF00](https://img.shields.io/badge/-FFFF00-FFFF00?style=flat-square&labelColor=FFFF00) Yellow |

### Pacific Northwest & Local

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Pacific Notions** | Mossy, misty PNW | ![#66CDAA](https://img.shields.io/badge/-66CDAA-66CDAA?style=flat-square&labelColor=66CDAA) Medium Aquamarine | ![#B0E0E6](https://img.shields.io/badge/-B0E0E6-B0E0E6?style=flat-square&labelColor=B0E0E6) Powder Blue | ![#778899](https://img.shields.io/badge/-778899-778899?style=flat-square) Light Slate Gray |
| **Vinelands** | Wine country | ![#800020](https://img.shields.io/badge/-800020-800020?style=flat-square) Dark Wine Red | ![#6B8E23](https://img.shields.io/badge/-6B8E23-6B8E23?style=flat-square) Olive Drab | ![#DAA520](https://img.shields.io/badge/-DAA520-DAA520?style=flat-square) Goldenrod |

### Special Programming

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Live on KEXP** | Stage lighting | ![#FF4500](https://img.shields.io/badge/-FF4500-FF4500?style=flat-square) Red-Orange | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) White Spotlight | ![#8A2BE2](https://img.shields.io/badge/-8A2BE2-8A2BE2?style=flat-square) Blue Violet |
| **Sound & Vision** | Bold multimedia | ![#FF1493](https://img.shields.io/badge/-FF1493-FF1493?style=flat-square) Deep Pink | ![#00FF7F](https://img.shields.io/badge/-00FF7F-00FF7F?style=flat-square&labelColor=00FF7F) Spring Green | ![#FFA500](https://img.shields.io/badge/-FFA500-FFA500?style=flat-square) Orange |
| **Variety Mix** | Eclectic rainbow | ![#FF6347](https://img.shields.io/badge/-FF6347-FF6347?style=flat-square) Tomato | ![#40E0D0](https://img.shields.io/badge/-40E0D0-40E0D0?style=flat-square&labelColor=40E0D0) Turquoise | ![#FFD700](https://img.shields.io/badge/-FFD700-FFD700?style=flat-square&labelColor=FFD700) Gold |

### Default

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **KEXP Default** | Classic station | ![#FFFFFF](https://img.shields.io/badge/-FFFFFF-FFFFFF?style=flat-square&labelColor=FFFFFF) White | ![#64C8FF](https://img.shields.io/badge/-64C8FF-64C8FF?style=flat-square&labelColor=64C8FF) Bright Blue | ![#FFC864](https://img.shields.io/badge/-FFC864-FFC864?style=flat-square&labelColor=FFC864) Warm Yellow |

*Used for shows without a specific color scheme or when show information is unavailable.*

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
