"""
KEXP API Client
Fetches current show and now playing data from KEXP API
"""

import requests
import logging

logger = logging.getLogger(__name__)


class KEXPClient:
    """Client for interacting with KEXP API"""

    BASE_URL = "https://api.kexp.org/v2"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'KEXP-Display/1.0'
        })

    def get_current_play(self):
        """
        Get the currently playing track from KEXP
        Returns the most recent play from the plays endpoint
        """
        try:
            url = f"{self.BASE_URL}/plays/"
            params = {
                'limit': 1,
                'ordering': '-airdate'
            }

            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data and 'results' in data and len(data['results']) > 0:
                play = data['results'][0]

                # Extract and format the play data
                return {
                    'artist': play.get('artist', 'Unknown Artist'),
                    'song': play.get('song', 'Unknown Track'),
                    'album': play.get('album', ''),
                    'airdate': play.get('airdate', ''),
                    'show': play.get('show'),
                    'show_uri': play.get('show_uri', ''),
                    'comment': play.get('comment', ''),
                    'play_type': play.get('play_type', ''),
                    'is_local': play.get('is_local', False),
                    'thumbnail_uri': play.get('thumbnail_uri', '')
                }

            return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching current play: {e}")
            return None

    def get_show_details(self, show_id):
        """
        Get details about a specific show
        """
        try:
            url = f"{self.BASE_URL}/shows/{show_id}/"

            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            show = response.json()

            return {
                'program_name': show.get('program_name', 'KEXP'),
                'program_tags': show.get('program_tags', ''),
                'host_names': show.get('host_names', ''),
                'start_time': show.get('start_time', ''),
                'end_time': show.get('end_time', '')
            }

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching show details: {e}")
            return None

    def get_recent_plays(self, limit=10):
        """
        Get recent plays from KEXP
        """
        try:
            url = f"{self.BASE_URL}/plays/"
            params = {
                'limit': limit,
                'ordering': '-airdate'
            }

            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data and 'results' in data:
                return data['results']

            return []

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching recent plays: {e}")
            return []
