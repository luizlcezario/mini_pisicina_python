from django.db import models


class eEx00_movies(models.Model):
    title = models.CharField(unique=True, max_length=64, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)

