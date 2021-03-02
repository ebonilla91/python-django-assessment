# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token 


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=255)
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

    def get_rating_movie(self):
        rating_avg = Rating.objects.filter(reviewed_movie=self.pk).aggregate(Avg('rating')).get('rating__avg')
        return "{:.1f}".format(rating_avg) if rating_avg else "0"



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
        return reverse('rating:detail', kwargs={'id': self.pk})


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
