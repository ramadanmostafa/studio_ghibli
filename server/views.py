from django.conf import settings
from django.views.generic import TemplateView

from server.models import Movie


class MoviesTemplateView(TemplateView):
    template_name = "server/movies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all().order_by('-id')
        context['BASE_URL'] = settings.STUDIO_GHIBLI_API_CONF["BASE_URL"]
        context['PEOPLE_API_URL'] = settings.STUDIO_GHIBLI_API_CONF["PEOPLE_API_URL"]
        context['FILMS_API_URL'] = settings.STUDIO_GHIBLI_API_CONF["FILMS_API_URL"]
        return context
