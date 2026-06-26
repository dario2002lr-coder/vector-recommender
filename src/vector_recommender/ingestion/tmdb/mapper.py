from vector_recommender.domain.movie import Movie

def tmdb_to_movie(data: dict) -> Movie:
    return Movie(
        id=data["id"],
        title=data["title"],
        overview=data.get("overview"),
        release_date=data.get("release_date"),
        genres=[g["name"] for g in data.get("genres", [])],
        vote_average=data.get("vote_average"),
        vote_count=data.get("vote_count"),
    )