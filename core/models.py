from django.db import models
from django.contrib.auth.models import User


class TextPair(models.Model):
    text = models.CharField(max_length=280)
    isHash = models.BooleanField()
    belongTo = models.ForeignKey('Tweet', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text


class Tweet(models.Model):
    body = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='likes')
    parsed = models.ManyToManyField('TextPair')

    def __str__(self):
        return self.body


class Hashtag(models.Model):
    name = models.CharField(unique=True, max_length=200, primary_key=True)
    tweeted = models.ManyToManyField(Tweet, related_name='tweeted')

    def __str__(self):
        return self.name
