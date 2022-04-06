from rest_framework.serializers import ModelSerializer

from .models import Album, Artist


class ArtistSerializer(ModelSerializer):
    """
    TODO:Document
    """

    class Meta:
        model = Artist
        fields = "__all__"


class AlbumSerializer(ModelSerializer):
    """
    TODO:Document
    """

    class Meta:
        model = Album
        fields = ["id", "name", "artist", "stars"]
        # depth = 1
