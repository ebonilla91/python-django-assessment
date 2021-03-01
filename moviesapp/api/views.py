from rest_framework import viewsets, generics
from .serializers import MovieSerializer
from moviesapp.movies.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer