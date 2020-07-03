from django.urls import path

from cineart.movies.views import list_movies, detail_movie

urlpatterns = [
  path("", list_movies, name="list-movie"),
  path("movie/<int:pk>", detail_movie, name="detail-movie")
]