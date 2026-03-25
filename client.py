import requests
from config import API_BASE_URL


class APIClient:
    """
    A reusable API client to interact with REST endpoints.
    Designed with modular and developer-friendly structure.
    """

    def __init__(self, base_url=API_BASE_URL):
        self.base_url = base_url

    def _handle_response(self, response):
        """Internal helper to process API responses"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error: {http_err}")
        except Exception as err:
            print(f"Error: {err}")
        return None

    def get_posts(self):
        """Fetch all posts"""
        url = f"{self.base_url}/posts"
        response = requests.get(url)
        return self._handle_response(response)

    def get_post_by_id(self, post_id):
        """Fetch a single post by ID"""
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)
        return self._handle_response(response)

    def create_post(self, data):
        """Create a new post"""
        url = f"{self.base_url}/posts"
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def update_post(self, post_id, data):
        """Update an existing post"""
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.put(url, json=data)
        return self._handle_response(response)

    def delete_post(self, post_id):
        """Delete a post"""
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.delete(url)
        return self._handle_response(response)
