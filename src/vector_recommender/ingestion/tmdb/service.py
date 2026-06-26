from .mapper import tmdb_to_movie

class TMDBService:
    def __init__(self, client):
        self.client = client

    def get_movie(self, movie_id: int):
        data = self.client.get_movie(movie_id)
        return tmdb_to_movie(data)

    def search_movie(self, query: str):
        data = self.client.search_movie(query)
        return data["results"]