from django.urls import path

from server.views import MoviesTemplateView

urlpatterns = [
    path('movies', MoviesTemplateView.as_view(), name='movies'),
]
