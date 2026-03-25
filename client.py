import requests
from config import API_BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL

    def get_posts(self):
        try:
            response = requests.get(f"{self.base_url}/posts")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def get_post_by_id(self, post_id):
        try:
            response = requests.get(f"{self.base_url}/posts/{post_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None