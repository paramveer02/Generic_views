from django.db import models


class Artist(models.Model):
    """
    TODO:Document
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name


# Manager subclass that returns all albums belonging to artist_id=1
class CustomManager(models.Manager):
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

    objects = models.Manager()  # default manager
    paramveer_objects = CustomManager()  # custom manager

    def __str__(self) -> str:
        return self.name
