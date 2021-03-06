from django.urls import include, path
from rest_framework import routers
from moviesapp.api import views as movie_views

router = routers.DefaultRouter()
router.register(r'movies', movie_views.MovieViewSet)
router.register(r'ratings', movie_views.RatingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]