from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from server.models import Movie


class TestMoviesTemplateView(TestCase):

    def setUp(self) -> None:
        self.url = reverse('movies')

    def test_no_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['BASE_URL'], settings.STUDIO_GHIBLI_API_CONF["BASE_URL"])
        self.assertEqual(response.context['PEOPLE_API_URL'], settings.STUDIO_GHIBLI_API_CONF["PEOPLE_API_URL"])
        self.assertEqual(response.context['FILMS_API_URL'], settings.STUDIO_GHIBLI_API_CONF["FILMS_API_URL"])
        self.assertQuerysetEqual(response.context['movies'], [])

    def test_with_data(self):
        Movie.objects.create(external_id='test')
        Movie.objects.create(external_id='test2')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['BASE_URL'], settings.STUDIO_GHIBLI_API_CONF["BASE_URL"])
        self.assertEqual(response.context['PEOPLE_API_URL'], settings.STUDIO_GHIBLI_API_CONF["PEOPLE_API_URL"])
        self.assertEqual(response.context['FILMS_API_URL'], settings.STUDIO_GHIBLI_API_CONF["FILMS_API_URL"])
        self.assertEqual(len(response.context['movies']), 2)
        self.assertEqual(response.context['movies'][0].external_id, 'test2')
        self.assertEqual(response.context['movies'][1].external_id, 'test')
