from django.urls import path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
