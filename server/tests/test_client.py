from unittest.mock import patch, Mock

from django.conf import settings
from django.test import TestCase

from server.client import StudioGhibliAPIClient


class TestStudioGhibliAPIClient(TestCase):
    def setUp(self) -> None:
        self.ghibli_client = StudioGhibliAPIClient()

    def test_headers(self):
        self.assertEqual({"Content-Type": "application/json"}, self.ghibli_client._StudioGhibliAPIClient__get_headers())

    @patch('server.client.requests.get')
    def test_get_people(self, get_mock):
        mock = Mock()
        mock.json.return_value = 'success'
        get_mock.return_value = mock
        self.assertEqual('success', self.ghibli_client.get_people())
        get_mock.assert_called_with(
            f'{settings.STUDIO_GHIBLI_API_CONF["BASE_URL"]}{settings.STUDIO_GHIBLI_API_CONF["PEOPLE_API_URL"]}',
            headers={"Content-Type": "application/json"}
        )

    @patch('server.client.requests.get')
    def test_get_movies(self, get_mock):
        mock = Mock()
        mock.json.return_value = 'success2'
        get_mock.return_value = mock
        self.assertEqual('success2', self.ghibli_client.get_movies())
        get_mock.assert_called_with(
            f'{settings.STUDIO_GHIBLI_API_CONF["BASE_URL"]}{settings.STUDIO_GHIBLI_API_CONF["FILMS_API_URL"]}',
            headers={"Content-Type": "application/json"}
        )
