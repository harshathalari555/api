from django.db import models
from jsonfield import JSONField
# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    year = models.IntegerField()
    data = JSONField(max_length=200, null=True)
    day = models.IntegerField(null=True)

    def __str__(self):
        return self.movie_name