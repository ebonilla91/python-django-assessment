# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

from .models import Movie


class MovieListView(ListView):
    """Show all movies."""
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movie_list'
    ordering = ['-released_on', '-rated']


class MovieDetailView(DetailView):
    """Show the requested movie."""
    model = Movie
    template_name = 'movies/movie_detail.html'

    def get_object(self, queryset=None):
        return Movie.objects.get(pk=self.kwargs.get("id"))


class MovieCreateView(CreateView):
    """Create a new movie."""
    model = Movie
    success_url = "/movies"

    fields = [
        "title",
        "plot",
        "year",
        "rated",
        "genre",
        "director",
        "released_on",
    ]


class MovieUpdateView(UpdateView):
    """Update the requested movie."""
    model = Movie
    success_url = "/movies"

    fields = [
        "title",
        "plot",
        "year",
        "rated",
        "genre",
        "director",
        "released_on",
    ]

    def get_object(self, queryset=None):
        try:
            movie, created = Movie.objects.get_or_create(pk=self.kwargs.get("id"))
            return movie
        except Movie.DoesNotExist:
            try:
                return Movie.objects.get(pk=self.kwargs.get("id"))
            except:
                return None


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""
    model = Movie
    success_url = "/movies"

    def get_object(self, queryset=None):
        return Movie.objects.get(pk=self.kwargs.get("id"))
