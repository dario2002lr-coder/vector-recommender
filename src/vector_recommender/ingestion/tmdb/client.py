import requests

class TMDBClient:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, access_token: str):
        self.access_token = access_token

    def _get(self, endpoint: str, params: dict | None = None):
        if params is None:
            params = {}

        headers = {"Authorization": f"Bearer {self.access_token}"}

        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, params=params, headers=headers)

        response.raise_for_status()
        return response.json()

    def get_movie(self, movie_id: int):
        return self._get(f"/movie/{movie_id}")

    def search_movie(self, query: str):
        return self._get("/search/movie", {"query": query})