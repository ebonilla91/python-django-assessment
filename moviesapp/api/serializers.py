from rest_framework import serializers
from moviesapp.movies.models import Movie, Rating


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'year', 'rated', 'released_on',
            'genre', 'director', 'plot',
            'created_at', 'updated_at',
        )


class RatingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rating
        fields = (
            'id', 'title', 'content', 'rating', 'reviewed_movie',
        )