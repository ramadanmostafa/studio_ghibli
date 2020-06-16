def get_movie_external_id_from_url(film_url: str) -> str:
    return film_url.split('/')[-1]
