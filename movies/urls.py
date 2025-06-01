from django.urls import path

from .views import MoviesView, MovieView, NewMovie, UpdateMovie, DeleteMovie

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
    path("<int:pk>", MovieView.as_view(), name="movie"),
    # path("<int:pk>/edit/", UpdateMovie.as_view(), name="movie_update" ),
    path("new", NewMovie.as_view(), name="movie_new"),
    path("delete/<str:slug>", DeleteMovie.as_view(), name="movie_delete"),
    path("update/<str:slug>", UpdateMovie.as_view(), name="movie_update")

]
