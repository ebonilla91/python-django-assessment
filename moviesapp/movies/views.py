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
    context_object_name = 'movie'


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


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""
    model = Movie
    success_url = "/movies"
