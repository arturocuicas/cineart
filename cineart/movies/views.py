from django.shortcuts import render

from cineart.movies.models import Movie


def list_movies(request):
    "List of Movies view"

    Movies = Movie.objects.all()

    context = {
        "title": "Billboard",
        "Movies": Movies
    }

    return render(request, "movie/list.html", context)


def detail_movie(request, pk):
    """Detail of a movie View"""

    Movie = Movie.objects.get(id=pk)

    context = {
        "Movie": Movie
    }

    return render(request, "movie/detail.html", context)
