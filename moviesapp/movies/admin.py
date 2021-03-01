from django.contrib import admin
from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rated', 'genre', 'director', 'released_on')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'rating', 'reviewed_movie')