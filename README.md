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
| **Early** | Sunrise morning | ![#FFB6C1](https://via.placeholder.com/80x20/FFB6C1/FFB6C1.png) Light Pink | ![#FFDAB9](https://via.placeholder.com/80x20/FFDAB9/FFDAB9.png) Peach | ![#FFEFD5](https://via.placeholder.com/80x20/FFEFD5/000000.png?text=+) Papaya Whip |
| **The Morning Show** | Warm sunrise gradient | ![#FF7F50](https://via.placeholder.com/80x20/FF7F50/FF7F50.png) Coral | ![#FFD700](https://via.placeholder.com/80x20/FFD700/000000.png?text=+) Gold | ![#87CEEB](https://via.placeholder.com/80x20/87CEEB/000000.png?text=+) Light Sky Blue |
| **The Midday Show** | Bright midday sun | ![#FFFF00](https://via.placeholder.com/80x20/FFFF00/000000.png?text=+) Yellow | ![#FFA500](https://via.placeholder.com/80x20/FFA500/FFA500.png) Orange | ![#87CEEB](https://via.placeholder.com/80x20/87CEEB/000000.png?text=+) Light Sky Blue |
| **The Afternoon Show** | Balanced brightness | ![#FFFFFF](https://via.placeholder.com/80x20/FFFFFF/000000.png?text=+) White | ![#4682B4](https://via.placeholder.com/80x20/4682B4/4682B4.png) Steel Blue | ![#FFC34D](https://via.placeholder.com/80x20/FFC34D/000000.png?text=+) Amber |
| **Drive Time** | Bold primaries | ![#DC143C](https://via.placeholder.com/80x20/DC143C/DC143C.png) Crimson | ![#FFFFFF](https://via.placeholder.com/80x20/FFFFFF/000000.png?text=+) White | ![#FFA500](https://via.placeholder.com/80x20/FFA500/FFA500.png) Orange |

### Electronic & Dance

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Midnight in a Perfect World** | Deep space electronic | ![#8A2BE2](https://via.placeholder.com/80x20/8A2BE2/8A2BE2.png) Blue Violet | ![#00BFFF](https://via.placeholder.com/80x20/00BFFF/00BFFF.png) Deep Sky Blue | ![#BA55D3](https://via.placeholder.com/80x20/BA55D3/BA55D3.png) Medium Orchid |
| **Mechanical Breakdown** | Industrial metallic | ![#C0C0C0](https://via.placeholder.com/80x20/C0C0C0/000000.png?text=+) Silver | ![#FF6347](https://via.placeholder.com/80x20/FF6347/FF6347.png) Tomato Red | ![#00CED1](https://via.placeholder.com/80x20/00CED1/00CED1.png) Dark Turquoise |
| **Astral Plane** | Cosmic psychedelic | ![#8A2BE2](https://via.placeholder.com/80x20/8A2BE2/8A2BE2.png) Blue Violet | ![#FF00FF](https://via.placeholder.com/80x20/FF00FF/FF00FF.png) Magenta | ![#00BFFF](https://via.placeholder.com/80x20/00BFFF/00BFFF.png) Deep Sky Blue |

### World Music

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Audioasis** | Desert palette | ![#CD5C5C](https://via.placeholder.com/80x20/CD5C5C/CD5C5C.png) Indian Red | ![#BDB76B](https://via.placeholder.com/80x20/BDB76B/BDB76B.png) Dark Khaki | ![#F4A460](https://via.placeholder.com/80x20/F4A460/F4A460.png) Sandy Brown |
| **Wo' Pop** | Vibrant eclectic | ![#FF69B4](https://via.placeholder.com/80x20/FF69B4/FF69B4.png) Hot Pink | ![#40E0D0](https://via.placeholder.com/80x20/40E0D0/40E0D0.png) Turquoise | ![#FFD700](https://via.placeholder.com/80x20/FFD700/000000.png?text=+) Gold |
| **El Sonido** | Spicy Latin warmth | ![#FF4500](https://via.placeholder.com/80x20/FF4500/FF4500.png) Red-Orange | ![#FFD700](https://via.placeholder.com/80x20/FFD700/000000.png?text=+) Gold | ![#9400D3](https://via.placeholder.com/80x20/9400D3/9400D3.png) Dark Violet |
| **Eastern Echoes** | Eastern-inspired | ![#DC143C](https://via.placeholder.com/80x20/DC143C/DC143C.png) Crimson Red | ![#FFD700](https://via.placeholder.com/80x20/FFD700/000000.png?text=+) Gold | ![#008080](https://via.placeholder.com/80x20/008080/008080.png) Teal |
| **Sounds of Survivance** | Earth and sky | ![#8B4513](https://via.placeholder.com/80x20/8B4513/8B4513.png) Saddle Brown | ![#D2B48C](https://via.placeholder.com/80x20/D2B48C/000000.png?text=+) Tan | ![#87CEEB](https://via.placeholder.com/80x20/87CEEB/000000.png?text=+) Sky Blue |
| **The Continent** | African vibrant | ![#FF8C00](https://via.placeholder.com/80x20/FF8C00/FF8C00.png) Dark Orange | ![#228B22](https://via.placeholder.com/80x20/228B22/228B22.png) Forest Green | ![#DC143C](https://via.placeholder.com/80x20/DC143C/DC143C.png) Crimson |

### Reggae & Caribbean

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Positive Vibrations** | Rasta colors | ![#FCD116](https://via.placeholder.com/80x20/FCD116/000000.png?text=+) Rasta Gold | ![#009B3A](https://via.placeholder.com/80x20/009B3A/009B3A.png) Rasta Green | ![#CE1126](https://via.placeholder.com/80x20/CE1126/CE1126.png) Rasta Red |

### Hip-Hop, R&B & Soul

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Street Sounds** | Urban neon graffiti | ![#FF1493](https://via.placeholder.com/80x20/FF1493/FF1493.png) Deep Pink | ![#00FFFF](https://via.placeholder.com/80x20/00FFFF/00FFFF.png) Cyan | ![#FFD700](https://via.placeholder.com/80x20/FFD700/000000.png?text=+) Gold |
| **Sunday Soul** | Warm vintage soul | ![#B8860B](https://via.placeholder.com/80x20/B8860B/B8860B.png) Dark Goldenrod | ![#DB7093](https://via.placeholder.com/80x20/DB7093/DB7093.png) Pale Violet Red | ![#FFDAB9](https://via.placeholder.com/80x20/FFDAB9/FFDAB9.png) Peach Puff |

### Jazz, Blues & Roots

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Expansions** | Smoky jazz club | ![#D2B48C](https://via.placeholder.com/80x20/D2B48C/000000.png?text=+) Tan | ![#B0C4DE](https://via.placeholder.com/80x20/B0C4DE/000000.png?text=+) Light Steel Blue | ![#DAA520](https://via.placeholder.com/80x20/DAA520/DAA520.png) Goldenrod |
| **Jazz Theatre** | Smoky jazz club | ![#D2B48C](https://via.placeholder.com/80x20/D2B48C/000000.png?text=+) Tan | ![#B0C4DE](https://via.placeholder.com/80x20/B0C4DE/000000.png?text=+) Light Steel Blue | ![#DAA520](https://via.placeholder.com/80x20/DAA520/DAA520.png) Goldenrod |
| **The Roadhouse** | Rustic honky tonk | ![#8B4513](https://via.placeholder.com/80x20/8B4513/8B4513.png) Saddle Brown | ![#D2691E](https://via.placeholder.com/80x20/D2691E/D2691E.png) Chocolate | ![#FFD700](https://via.placeholder.com/80x20/FFD700/000000.png?text=+) Gold |

### Rock, Metal & Punk

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Seek & Destroy** | Aggressive metal | ![#FF0000](https://via.placeholder.com/80x20/FF0000/FF0000.png) Pure Red | ![#FFFFFF](https://via.placeholder.com/80x20/FFFFFF/000000.png?text=+) Pure White | ![#808080](https://via.placeholder.com/80x20/808080/808080.png) Gray |
| **Sonic Reducer** | Punk chaos | ![#FFFF00](https://via.placeholder.com/80x20/FFFF00/000000.png?text=+) Yellow | ![#FF00FF](https://via.placeholder.com/80x20/FF00FF/FF00FF.png) Magenta | ![#00FF00](https://via.placeholder.com/80x20/00FF00/00FF00.png) Lime Green |
| **90.TEEN** | Youth energy | ![#FF007F](https://via.placeholder.com/80x20/FF007F/FF007F.png) Bright Pink | ![#00FFFF](https://via.placeholder.com/80x20/00FFFF/00FFFF.png) Cyan | ![#FFFF00](https://via.placeholder.com/80x20/FFFF00/000000.png?text=+) Yellow |

### Pacific Northwest & Local

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Pacific Notions** | Mossy, misty PNW | ![#66CDAA](https://via.placeholder.com/80x20/66CDAA/66CDAA.png) Medium Aquamarine | ![#B0E0E6](https://via.placeholder.com/80x20/B0E0E6/000000.png?text=+) Powder Blue | ![#778899](https://via.placeholder.com/80x20/778899/778899.png) Light Slate Gray |
| **Vinelands** | Wine country | ![#800020](https://via.placeholder.com/80x20/800020/800020.png) Dark Wine Red | ![#6B8E23](https://via.placeholder.com/80x20/6B8E23/6B8E23.png) Olive Drab | ![#DAA520](https://via.placeholder.com/80x20/DAA520/DAA520.png) Goldenrod |

### Special Programming

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Live on KEXP** | Stage lighting | ![#FF4500](https://via.placeholder.com/80x20/FF4500/FF4500.png) Red-Orange | ![#FFFFFF](https://via.placeholder.com/80x20/FFFFFF/000000.png?text=+) White Spotlight | ![#8A2BE2](https://via.placeholder.com/80x20/8A2BE2/8A2BE2.png) Blue Violet |
| **Sound & Vision** | Bold multimedia | ![#FF1493](https://via.placeholder.com/80x20/FF1493/FF1493.png) Deep Pink | ![#00FF7F](https://via.placeholder.com/80x20/00FF7F/00FF7F.png) Spring Green | ![#FFA500](https://via.placeholder.com/80x20/FFA500/FFA500.png) Orange |
| **Variety Mix** | Eclectic rainbow | ![#FF6347](https://via.placeholder.com/80x20/FF6347/FF6347.png) Tomato | ![#40E0D0](https://via.placeholder.com/80x20/40E0D0/40E0D0.png) Turquoise | ![#FFD700](https://via.placeholder.com/80x20/FFD700/000000.png?text=+) Gold |

### Default

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **KEXP Default** | Classic station | ![#FFFFFF](https://via.placeholder.com/80x20/FFFFFF/000000.png?text=+) White | ![#64C8FF](https://via.placeholder.com/80x20/64C8FF/64C8FF.png) Bright Blue | ![#FFC864](https://via.placeholder.com/80x20/FFC864/000000.png?text=+) Warm Yellow |

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
