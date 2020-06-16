from django.test import TestCase

from server.utils import get_movie_external_id_from_url


class TestUtils(TestCase):

    def test_get_movie_external_id_from_url(self):
        self.assertEqual(
            '1b67aa9a-2e4a-45af-ac98-64d6ad15b16c',
            get_movie_external_id_from_url('https://ghibliapi.herokuapp.com/films/1b67aa9a-2e4a-45af-ac98-64d6ad15b16c')
        )
        self.assertEqual(
            '',
            get_movie_external_id_from_url('')
        )
