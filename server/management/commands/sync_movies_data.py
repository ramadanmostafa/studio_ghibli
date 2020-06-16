from django.conf import settings
from django.core.management import BaseCommand

from server.tasks import fetch_movies_data_async


class Command(BaseCommand):
    help = 'periodically sync movies data from STUDIO GHIBLI API'

    def handle(self, *args, **options):
        if settings.STUDIO_GHIBLI_API_CONF['IS_ENABLED']:
            fetch_movies_data_async.apply_async(countdown=settings.STUDIO_GHIBLI_API_CONF['SYNC_INTERVAL_SEC'])
