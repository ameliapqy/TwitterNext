from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=200)
    # body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)