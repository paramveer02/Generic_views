from django.urls import path

from .views import ArtistView, SingleAlbumView

urlpatterns = [
    path("songs/", ArtistView.as_view()),
    path("songs/<int:pk>", SingleAlbumView.as_view()),
]
