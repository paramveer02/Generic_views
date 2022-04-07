from rest_framework.filters import OrderingFilter, SearchFilter
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

    # Searching and Ordering
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ["first_name", "instrument"]
    ordering_fields = ["id", "first_name"]

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SingleAlbumView(RetrieveUpdateDestroyAPIView, GenericAPIView):
    """
    An endpoint that returns the information of an album belonging to a particular artist.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
