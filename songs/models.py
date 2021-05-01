from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    