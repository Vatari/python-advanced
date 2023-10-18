def movie_organizer(*args):
    genres = {}

    for movie, genre in args:
        if genre in genres:
            genres[genre].append(movie)
        else:
            genres[genre] = [movie]

    sorted_genres = sorted(genres.keys())

    for genre in sorted_genres:
        genres[genre] = sorted(genres[genre])

    sorted_genres = sorted(sorted_genres, key=lambda genre_: (-len(genres[genre_]), genre_))

    output = ""
    for genre in sorted_genres:
        movies = genres[genre]
        num_movies = len(movies)
        output += f"{genre} - {num_movies}\n"
        for movie in movies:
            output += f"* {movie}\n"

    return output
