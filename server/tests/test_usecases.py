from unittest.mock import patch

from django.test import TestCase

from server.models import Movie, People
from server.usecases import sync_movies_data, save_movies_data, save_people_data


class TestUseCases(TestCase):

    @patch('server.usecases.StudioGhibliAPIClient.get_movies', return_value=[{'id': 'movie'}])
    @patch('server.usecases.StudioGhibliAPIClient.get_people', return_value=[{'id': 'person'}])
    def test_sync_movies_data(self, get_people, get_movies):
        self.assertIsNone(sync_movies_data())
        self.assertTrue(get_people.called)
        self.assertTrue(get_movies.called)
        self.assertEqual(1, Movie.objects.filter(external_id='movie').count())
        self.assertEqual(1, People.objects.filter(external_id='person').count())

    def test_save_movies_data_empty_list(self):
        self.assertIsNone(save_movies_data([]))
        self.assertEqual(0, Movie.objects.all().count())

    def test_save_movies_data_min_data(self):
        self.assertIsNone(save_movies_data([
            {'id': '1'}, {'id': '2'}
        ]))
        self.assertEqual(2, Movie.objects.filter(external_id__in=['1', '2']).count())

    def test_save_movies_data_full_data(self):
        movie_data = {
            'external_id': '1',
            'title': 'title',
            'description': 'description',
            'director': 'director',
            'producer': 'producer',
            'release_date': 'release_date',
            'rt_score': 'rt_score',
        }
        self.assertIsNone(save_movies_data([{**movie_data, 'id': 1}]))
        self.assertEqual(1, Movie.objects.filter(**movie_data).count())

    def test_save_people_data_empty_list(self):
        self.assertIsNone(save_people_data([]))
        self.assertEqual(0, People.objects.all().count())

    def test_save_people_data_min_data(self):
        self.assertIsNone(save_people_data([
            {'id': '1'}, {'id': '2'}
        ]))
        self.assertEqual(2, People.objects.filter(external_id__in=['1', '2']).count())

    def test_save_people_data_full_data(self):
        movie_data = {
            'external_id': '1',
            'name': 'name',
            'gender': 'male',
            'age': 'age',
            'eye_color': 'eye_color',
            'hair_color': 'hair_color',
        }
        self.assertIsNone(save_people_data([{**movie_data, 'id': 1}]))
        self.assertEqual(1, People.objects.filter(**movie_data).count())

    def test_save_people_data_full_data_with_not_existing_films(self):
        movie_data = {
            'external_id': '1',
            'name': 'name',
            'gender': 'male',
            'age': 'age',
            'eye_color': 'eye_color',
            'hair_color': 'hair_color',
        }
        self.assertIsNone(save_people_data([{
            **movie_data, 'id': 1,
            'films': ['https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6']
        }]))
        self.assertEqual(1, People.objects.filter(**movie_data).count())
        self.assertEqual(0, Movie.objects.all().count())

    def test_save_people_data_full_data_with_worng_film_url(self):
        movie_data = {
            'external_id': '1',
            'name': 'name',
            'gender': 'male',
            'age': 'age',
            'eye_color': 'eye_color',
            'hair_color': 'hair_color',
        }
        self.assertIsNone(save_people_data([{**movie_data, 'id': 1, 'films': ['test']}]))
        self.assertEqual(1, People.objects.filter(**movie_data).count())
        self.assertEqual(0, Movie.objects.all().count())

    def test_save_people_data_full_data_with_existing_films(self):
        movie = Movie.objects.create(
            external_id='0440483e-ca0e-4120-8c50-4c8cd9b965d6'
        )
        movie_data = {
            'external_id': '1',
            'name': 'name',
            'gender': 'male',
            'age': 'age',
            'eye_color': 'eye_color',
            'hair_color': 'hair_color',
        }
        self.assertIsNone(save_people_data([{
            **movie_data, 'id': 1,
            'films': ['https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6']
        }]))
        movie.refresh_from_db()
        person = People.objects.get(**movie_data)
        self.assertEqual(1, movie.people.all().count())
        self.assertEqual(person, movie.people.first())
