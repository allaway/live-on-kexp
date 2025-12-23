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
| **Early** | Sunrise morning | Light Pink (255, 182, 193) | Peach (255, 218, 185) | Papaya Whip (255, 239, 213) |
| **The Morning Show** | Warm sunrise gradient | Coral (255, 127, 80) | Gold (255, 215, 0) | Light Sky Blue (135, 206, 250) |
| **The Midday Show** | Bright midday sun | Yellow (255, 255, 0) | Orange (255, 165, 0) | Light Sky Blue (135, 206, 250) |
| **The Afternoon Show** | Balanced brightness | White (255, 255, 255) | Steel Blue (70, 130, 180) | Amber (255, 195, 77) |
| **Drive Time** | Bold primaries | Crimson (220, 20, 60) | White (255, 255, 255) | Orange (255, 165, 0) |

### Electronic & Dance

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Midnight in a Perfect World** | Deep space electronic | Blue Violet (138, 43, 226) | Deep Sky Blue (0, 191, 255) | Medium Orchid (186, 85, 211) |
| **Mechanical Breakdown** | Industrial metallic | Silver (192, 192, 192) | Tomato Red (255, 99, 71) | Dark Turquoise (0, 206, 209) |
| **Astral Plane** | Cosmic psychedelic | Blue Violet (138, 43, 226) | Magenta (255, 0, 255) | Deep Sky Blue (0, 191, 255) |

### World Music

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Audioasis** | Desert palette | Indian Red (205, 92, 92) | Dark Khaki (189, 183, 107) | Sandy Brown (244, 164, 96) |
| **Wo' Pop** | Vibrant eclectic | Hot Pink (255, 105, 180) | Turquoise (64, 224, 208) | Gold (255, 215, 0) |
| **El Sonido** | Spicy Latin warmth | Red-Orange (255, 69, 0) | Gold (255, 215, 0) | Dark Violet (148, 0, 211) |
| **Eastern Echoes** | Eastern-inspired | Crimson Red (220, 20, 60) | Gold (255, 215, 0) | Teal (0, 128, 128) |
| **Sounds of Survivance** | Earth and sky | Saddle Brown (139, 69, 19) | Tan (210, 180, 140) | Sky Blue (135, 206, 235) |
| **The Continent** | African vibrant | Dark Orange (255, 140, 0) | Forest Green (34, 139, 34) | Crimson (220, 20, 60) |

### Reggae & Caribbean

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Positive Vibrations** | Rasta colors | Rasta Gold (252, 209, 22) | Rasta Green (0, 155, 58) | Rasta Red (206, 17, 38) |

### Hip-Hop, R&B & Soul

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Street Sounds** | Urban neon graffiti | Deep Pink (255, 20, 147) | Cyan (0, 255, 255) | Gold (255, 215, 0) |
| **Sunday Soul** | Warm vintage soul | Dark Goldenrod (184, 134, 11) | Pale Violet Red (219, 112, 147) | Peach Puff (255, 218, 185) |

### Jazz, Blues & Roots

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Expansions** | Smoky jazz club | Tan (210, 180, 140) | Light Steel Blue (176, 196, 222) | Goldenrod (218, 165, 32) |
| **Jazz Theatre** | Smoky jazz club | Tan (210, 180, 140) | Light Steel Blue (176, 196, 222) | Goldenrod (218, 165, 32) |
| **The Roadhouse** | Rustic honky tonk | Saddle Brown (139, 69, 19) | Chocolate (210, 105, 30) | Gold (255, 215, 0) |

### Rock, Metal & Punk

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Seek & Destroy** | Aggressive metal | Pure Red (255, 0, 0) | Pure White (255, 255, 255) | Gray (128, 128, 128) |
| **Sonic Reducer** | Punk chaos | Yellow (255, 255, 0) | Magenta (255, 0, 255) | Lime Green (0, 255, 0) |
| **90.TEEN** | Youth energy | Bright Pink (255, 0, 127) | Cyan (0, 255, 255) | Yellow (255, 255, 0) |

### Pacific Northwest & Local

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Pacific Notions** | Mossy, misty PNW | Medium Aquamarine (102, 205, 170) | Powder Blue (176, 224, 230) | Light Slate Gray (119, 136, 153) |
| **Vinelands** | Wine country | Dark Wine Red (128, 0, 32) | Olive Drab (107, 142, 35) | Goldenrod (218, 165, 32) |

### Special Programming

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **Live on KEXP** | Stage lighting | Red-Orange (255, 69, 0) | White Spotlight (255, 255, 255) | Blue Violet (138, 43, 226) |
| **Sound & Vision** | Bold multimedia | Deep Pink (255, 20, 147) | Spring Green (0, 255, 127) | Orange (255, 165, 0) |
| **Variety Mix** | Eclectic rainbow | Tomato (255, 99, 71) | Turquoise (64, 224, 208) | Gold (255, 215, 0) |

### Default

| Show | Theme | Artist Color | Song Color | Info Color |
|------|-------|--------------|------------|------------|
| **KEXP Default** | Classic station | White (255, 255, 255) | Bright Blue (100, 200, 255) | Warm Yellow (255, 200, 100) |

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
