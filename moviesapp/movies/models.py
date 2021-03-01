# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.FloatField()
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    # Todo: add Rating models

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-released_on', '-rated']

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.pk})


class Rating(models.Model):
    reviewed_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('review:detail', kwargs={'id': self.pk})


@receiver(post_save, sender=Rating)
def my_handler(sender, instance, **kwargs):
    related_movie = Movie.objects.get(pk=instance.reviewed_movie.pk)
    rating_avg = Rating.objects.filter(reviewed_movie=related_movie.pk).aggregate(Avg('rating')).get('rating__avg')
    related_movie.rated = "{:.1f}".format(rating_avg)
    related_movie.save()

