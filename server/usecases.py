from server.client import StudioGhibliAPIClient
from server.models import Movie, People
from server.utils import get_movie_external_id_from_url


def sync_movies_data() -> None:
    """
    call Studio Ghibli API and save the returned data to Movie and People models
    """
    client = StudioGhibliAPIClient()
    movies_json = client.get_movies()
    people_json = client.get_people()
    save_movies_data(movies_json)
    save_people_data(people_json)


def save_movies_data(movies: list) -> None:
    for movie in movies:
        Movie.objects.update_or_create(
            external_id=movie['id'],
            defaults={
                'title': movie.get('title', ''),
                'description': movie.get('description', ''),
                'director': movie.get('director', ''),
                'producer': movie.get('producer', ''),
                'release_date': movie.get('release_date', ''),
                'rt_score': movie.get('rt_score', ''),
            }
        )


def save_people_data(people_json: list) -> None:
    for person in people_json:
        created_person, _ = People.objects.update_or_create(
            external_id=person['id'],
            defaults={
                'name': person.get('name', ''),
                'gender': person.get('gender', ''),
                'age': person.get('age', ''),
                'eye_color': person.get('eye_color', ''),
                'hair_color': person.get('hair_color', ''),
            }
        )
        for film_url in person.get('films', []):
            try:
                film = Movie.objects.get(external_id=get_movie_external_id_from_url(film_url))
            except Movie.DoesNotExist:
                continue
            film.people.add(created_person)
