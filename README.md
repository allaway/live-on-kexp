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
