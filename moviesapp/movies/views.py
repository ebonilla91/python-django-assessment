# -*- coding: utf-8 -*-
"""Movies views."""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Movie
from .forms import MovieForm


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
    form_class = MovieForm
    success_url = "/movies"


class MovieUpdateView(UpdateView):
    """Update the requested movie."""
    model = Movie
    form_class = MovieForm
    success_url = "/movies"

    def get_object(self, queryset=None):
        try:
            return Movie.objects.get(pk=self.kwargs.get("id"))
        except Movie.DoesNotExist:
            try:
                movie, created = Movie.objects.get_or_create(pk=self.kwargs.get("id"))
                return movie
            except:
                return None


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""
    model = Movie
    success_url = "/movies"

    def get_object(self, queryset=None):
        return Movie.objects.get(pk=self.kwargs.get("id"))


class MovieFormView(FormView):
    form_class = MovieForm
    template_name = "movies/movie_form.html"
    success_url = "/movies"

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        form.errors['title'] = 'This field is required.'
        return self.form_invalid(form)
