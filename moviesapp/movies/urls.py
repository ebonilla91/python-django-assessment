# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', view=views.MovieListView.as_view(), name='index'),
    path('(<int:isbn>/', view=views.MovieDetailView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('update/<int:isbn>/', view=views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:isbn>/', view=views.MovieDeleteView.as_view(), name='delete'),
    # API URL
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
