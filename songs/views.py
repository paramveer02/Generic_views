from cgitb import lookup

from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from songs.models import Album, Artist

from .serializers import AlbumSerializer, ArtistSerializer


class ArtistView(ListAPIView, CreateAPIView, GenericAPIView):
    """
    An endpoint that returns the list of all the available artists
    and allows user to create new artists.
    """

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SingleAlbumView(RetrieveUpdateDestroyAPIView, GenericAPIView):
    """
    An endpoint that returns the information of an album belong to a particular artist.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
