from django.contrib import admin
from core.models import Tweet, Hashtag, TextPair
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Hashtag)
admin.site.register(TextPair)
