import requests
from django.conf import settings


class StudioGhibliAPIClient:

    def __get_headers(self):
        return {
            "Content-Type": "application/json"
        }

    def get_people(self):
        response = requests.get(
            f'{settings.STUDIO_GHIBLI_API_CONF["BASE_URL"]}{settings.STUDIO_GHIBLI_API_CONF["PEOPLE_API_URL"]}',
            headers=self.__get_headers()
        )
        return response.json()

    def get_movies(self):
        response = requests.get(
            f'{settings.STUDIO_GHIBLI_API_CONF["BASE_URL"]}{settings.STUDIO_GHIBLI_API_CONF["FILMS_API_URL"]}',
            headers=self.__get_headers()
        )
        return response.json()
