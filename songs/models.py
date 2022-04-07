from django.db import models
from django.db.models import Count


class CustomArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(album__release_date__gte="2011-09-23")


class Artist(models.Model):
    """
    TODO:Document
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name

    # Default Manager
    objects = models.Manager()

    # Custom Manager returns artists whose albums were released during and after '2011-09-23'
    custom_objects = CustomArtistManager()


# Manager subclass that returns all albums belonging to artist_id=1
class CustomAlbumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(artist_id=1)


class Album(models.Model):
    """
    TODO:Document
    """

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    stars = models.IntegerField()

    # default manager
    objects = models.Manager()

    # custom manager returns albums belonging to 'artist_id=1'
    paramveer_objects = CustomAlbumManager()

    def __str__(self) -> str:
        return self.name
