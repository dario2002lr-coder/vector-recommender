from vector_recommender.ingestion.tmdb.mapper import tmdb_to_movie


def test_tmdb_to_movie_maps_extended_fields():
    payload = {
        "poster_path": "/IfB9hy4JH1eH6HEfIgIGORXi5h.jpg",
        "adult": False,
        "overview": "Jack Reacher must uncover the truth behind a major government conspiracy in order to clear his name.",
        "release_date": "2016-10-19",
        "genre_ids": [53, 28, 80],
        "id": 343611,
        "original_title": "Jack Reacher: Never Go Back",
        "original_language": "en",
        "title": "Jack Reacher: Never Go Back",
        "backdrop_path": "/4ynQYtSEuU5hyipcGkfD6ncwtwz.jpg",
        "popularity": 26.818468,
        "vote_count": 201,
        "video": False,
        "vote_average": 4.19,
    }

    movie = tmdb_to_movie(payload)

    assert movie.id == 343611
    assert movie.title == "Jack Reacher: Never Go Back"
    assert movie.poster_path == "/IfB9hy4JH1eH6HEfIgIGORXi5h.jpg"
    assert movie.adult is False
    assert movie.original_title == "Jack Reacher: Never Go Back"
    assert movie.original_language == "en"
    assert movie.genre_ids == [53, 28, 80]
    assert movie.backdrop_path == "/4ynQYtSEuU5hyipcGkfD6ncwtwz.jpg"
    assert movie.popularity == 26.818468
    assert movie.video is False
    assert movie.vote_count == 201
    assert movie.vote_average == 4.19


def test_tmdb_to_movie_derives_genre_ids_from_genres():
    payload = {
        "id": 603,
        "title": "The Matrix",
        "overview": "A computer hacker learns about the true nature of reality.",
        "release_date": "1999-03-31",
        "genres": [
            {"id": 28, "name": "Action"},
            {"id": 878, "name": "Science Fiction"},
        ],
    }

    movie = tmdb_to_movie(payload)

    assert movie.genres == ["Action", "Science Fiction"]
    assert movie.genre_ids == [28, 878]
