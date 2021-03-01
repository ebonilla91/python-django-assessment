from rest_framework import serializers
from moviesapp.movies.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'year', 'rated', 'released_on',
            'genre', 'director', 'plot',
            'created_at', 'updated_at',
        )