from celery import shared_task
from django.conf import settings

from server.usecases import sync_movies_data


@shared_task
def fetch_movies_data_async():
    sync_movies_data()
    fetch_movies_data_async.s().apply_async(countdown=settings.STUDIO_GHIBLI_API_CONF['SYNC_INTERVAL_SEC'])
