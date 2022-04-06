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


class Album(models.Model):
    """
    TODO:Document
    """

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    stars = models.IntegerField()

    def __str__(self) -> str:
        return self.name
