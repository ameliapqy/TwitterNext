from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=1000)
    # body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.body

    def __init__(self, request, body, created_at, author):
        #parse hashtags
        names = [c for c in self.body.split() if c.startswith('#')]
        for name in names:
            hashtag = Hashtag.object.filter(name=name)
            if hashtag.exists():
                Hashtag.object.filter(name=name).tweets.add(self)
            else:
                print("add hashtag: " + name)
                h1 = Hashtag(name=name)
                h1.save()
                h1.tweets.add(self)


class Hashtag(models.Model):
    name = models.CharField(unique=True,max_length=200)
    tweets = models.ManyToManyField(Tweet)

    def __str__(self):
        return self.name
    