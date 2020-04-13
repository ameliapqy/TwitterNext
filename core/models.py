from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    body = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.body

class Hashtag(models.Model):
    name = models.CharField(unique=True,max_length=200)
    tweets = models.ManyToManyField(Tweet)

    def __str__(self):
        return self.name